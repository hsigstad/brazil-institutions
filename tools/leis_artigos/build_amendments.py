#!/usr/bin/env python3
"""
Build the `amendment` table by parsing amending laws.

# INTENT
# For each amending lei referenced as a `fonte_id` in the `artigo` table,
# look up its planalto HTML, parse it for hyperlinks to target lei anchors,
# and write one row per (target_lei, artigo, path) tuple to the
# `amendment` table.
#
# REASONING
# This gives us an authoritative map of "which lei changed which clause of
# which target lei", independent of whether the consolidated text on the
# target lei's page has the correct annotations. We use it to:
#   - Cross-verify that artigo.fonte_id assignments are correct
#   - Find missing amendments where the consolidated text lacks annotations
#   - Answer "what did Lei X change?" without parsing X every time
#
# ASSUMES
# build.py has already populated the artigo table. We discover the set
# of amending leis from artigo.fonte_id values that aren't the original
# lei of any cataloged target.
"""

from __future__ import annotations

import argparse
import re
import sqlite3
import sys
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent))
from build import (  # noqa: E402
    LAW_CATALOG, ARTIGOS_DB, PLANALTO_DB, parse_pt_date,
)
from amendments_parser import parse_amending_lei_html, Amendment  # noqa: E402


SCHEMA = """
CREATE TABLE IF NOT EXISTS amendment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amending_fonte_id TEXT NOT NULL,        -- 'L14230-2021'
    amending_label TEXT NOT NULL,           -- 'Lei nº 14.230, de 2021'
    amending_data TEXT NOT NULL,            -- 'YYYY-MM-DD'
    target_apelido TEXT,                    -- 'LIA' if in catalog, else NULL
    target_filename TEXT NOT NULL,          -- 'L8429.htm'
    target_tipo TEXT NOT NULL,              -- 'L', 'LC', 'MP', etc.
    target_numero TEXT NOT NULL,            -- '8429'
    artigo INTEGER NOT NULL,
    artigo_letra TEXT,
    path TEXT NOT NULL,
    action TEXT NOT NULL,                   -- 'add', 'modify', 'revoke'
    source_anchor TEXT NOT NULL,
    source_text TEXT,
    ordem INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_amendment_target ON amendment(target_apelido, artigo, path);
CREATE INDEX IF NOT EXISTS idx_amendment_amending ON amendment(amending_fonte_id);
CREATE INDEX IF NOT EXISTS idx_amendment_filename ON amendment(target_filename, artigo);
"""


# Parse a fonte_id like 'L14230-2021', 'LC219-2025', 'MP495-2010' → (tipo, numero, ano)
FONTE_ID_RE = re.compile(r'^([A-Z]+?)(\d+)-(\d{4})$')

TIPO_TO_PLANALTO_TYPE = {
    'L': 'lei',
    'LC': 'lei_complementar',
    'MP': 'medida_provisoria',
    'DL': 'decreto_lei',
    'D': 'decreto',
    'EC': 'emenda_constitucional',
}


def parse_fonte_id(fonte_id: str) -> Optional[tuple[str, str, str]]:
    m = FONTE_ID_RE.match(fonte_id)
    if not m:
        return None
    return m.group(1), m.group(2), m.group(3)


def find_planalto_lei(
    cur: sqlite3.Cursor,
    tipo: str,
    numero: str,
    ano: str,
) -> Optional[tuple[int, str, str]]:
    """Find the planalto record for an amending lei.

    Returns (id, html_raw, data) or None.
    """
    planalto_tipo = TIPO_TO_PLANALTO_TYPE.get(tipo, 'lei')
    cur.execute(
        "SELECT id, html_raw, data FROM legislacao "
        "WHERE numero = ? AND tipo = ? AND data LIKE ? "
        "LIMIT 1",
        (numero, planalto_tipo, f'%{ano}%'),
    )
    row = cur.fetchone()
    if not row:
        # Try less restrictive: any tipo containing 'lei'
        cur.execute(
            "SELECT id, html_raw, data FROM legislacao "
            "WHERE numero = ? AND tipo LIKE ? AND data LIKE ? "
            "LIMIT 1",
            (numero, f'%{tipo.lower()}%', f'%{ano}%'),
        )
        row = cur.fetchone()
    return row


def _catalog_fonte_id(entry) -> str:
    """Build the original fonte_id for a catalog entry."""
    if len(entry) == 4:
        _, numero, ano, _ = entry
        return f'L{numero}-{ano}'
    _, numero, ano, _, tipo = entry
    prefix_map = {
        'lei': 'L', 'lei_complementar': 'LC',
        'medida_provisoria': 'MP', 'decreto_lei': 'DL',
        'decreto': 'D', 'emenda_constitucional': 'EC',
    }
    prefix = prefix_map.get(tipo, 'L')
    return f'{prefix}{numero}-{ano}'


def get_amending_fonte_ids(con: sqlite3.Connection) -> list[str]:
    """Return distinct fonte_id values that are NOT the original of a cataloged law."""
    original_ids = {_catalog_fonte_id(entry) for entry in LAW_CATALOG}
    cur = con.cursor()
    cur.execute("SELECT DISTINCT fonte_id FROM artigo ORDER BY fonte_id")
    all_ids = [row[0] for row in cur.fetchall()]
    return [fid for fid in all_ids if fid not in original_ids]


def target_apelido_for_filename(filename: str) -> Optional[str]:
    """Map a planalto filename like 'L8429.htm' to a catalog apelido if known."""
    name = filename.lower().rstrip('.htm')
    m = re.match(r'^(l|lc|lcp|mp|dl|d|ec)(\d+)$', name)
    if not m:
        return None
    target_numero = m.group(2)
    for entry in LAW_CATALOG:
        numero = entry[1]
        if numero == target_numero:
            return entry[0]
    return None


def fonte_id_label(tipo: str, numero: str, ano: str) -> str:
    """Build the human-readable label from a fonte_id."""
    n = numero
    if len(n) >= 4:
        n = f'{n[:-3]}.{n[-3:]}'
    tipo_label_map = {
        'L': 'Lei',
        'LC': 'Lei Complementar',
        'MP': 'Medida Provisória',
        'DL': 'Decreto-Lei',
        'D': 'Decreto',
        'EC': 'Emenda Constitucional',
    }
    return f'{tipo_label_map.get(tipo, "Lei")} nº {n}, de {ano}'


def insert_amendments(
    con: sqlite3.Connection,
    fonte_id: str,
    label: str,
    data: str,
    amendments: list[Amendment],
) -> None:
    cur = con.cursor()
    cur.execute("DELETE FROM amendment WHERE amending_fonte_id = ?", (fonte_id,))
    cur.executemany(
        """
        INSERT INTO amendment (
            amending_fonte_id, amending_label, amending_data,
            target_apelido, target_filename, target_tipo, target_numero,
            artigo, artigo_letra, path, action, source_anchor, source_text,
            ordem
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (
                fonte_id, label, data,
                target_apelido_for_filename(a.target_filename),
                a.target_filename,
                a.target_tipo,
                a.target_numero,
                a.artigo,
                a.artigo_letra,
                a.path,
                a.action,
                a.source_anchor,
                a.source_text,
                a.ordem,
            )
            for a in amendments
        ],
    )
    con.commit()


def main():
    ap = argparse.ArgumentParser(description='Build amendment table from amending laws')
    ap.add_argument('--planalto-db', type=Path, default=PLANALTO_DB)
    ap.add_argument('--artigos-db', type=Path, default=ARTIGOS_DB)
    ap.add_argument('--limit', type=int, help='Process only first N amending leis (for testing)')
    args = ap.parse_args()

    if not args.artigos_db.exists():
        sys.exit(f'artigos.db not found at {args.artigos_db}. Run build.py first.')

    src = sqlite3.connect(args.planalto_db)
    src_cur = src.cursor()

    out = sqlite3.connect(args.artigos_db)
    out.executescript(SCHEMA)

    fonte_ids = get_amending_fonte_ids(out)
    if args.limit:
        fonte_ids = fonte_ids[: args.limit]

    print(f'Processing {len(fonte_ids)} amending leis...', file=sys.stderr)

    total_amendments = 0
    not_found = []
    for fid in fonte_ids:
        parsed = parse_fonte_id(fid)
        if parsed is None:
            print(f'  skip: {fid} (could not parse fonte_id)', file=sys.stderr)
            continue
        tipo, numero, ano = parsed

        record = find_planalto_lei(src_cur, tipo, numero, ano)
        if record is None:
            not_found.append(fid)
            continue
        planalto_id, html, data_str = record
        data = parse_pt_date(data_str) or f'{ano}-01-01'

        amendments = parse_amending_lei_html(html)
        if not amendments:
            print(f'  {fid}: no amendments parsed', file=sys.stderr)
            continue

        label = fonte_id_label(tipo, numero, ano)
        insert_amendments(out, fid, label, data, amendments)
        total_amendments += len(amendments)
        print(f'  {fid}: {len(amendments)} amendments', file=sys.stderr)

    print(file=sys.stderr)
    print(f'Total: {total_amendments} amendments inserted', file=sys.stderr)
    if not_found:
        print(f'Not found in planalto DB: {len(not_found)} fonte_ids', file=sys.stderr)
        for fid in not_found[:10]:
            print(f'  {fid}', file=sys.stderr)

    src.close()
    out.close()


if __name__ == '__main__':
    main()
