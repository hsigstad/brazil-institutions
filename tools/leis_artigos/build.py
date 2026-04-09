#!/usr/bin/env python3
"""
Build the article-level law database from planalto consolidated HTML.

# INTENT
# Read selected laws from the planalto_legislacao.db (raw scrape), parse the
# HTML into structured leaves using parser.py, resolve amendment dates by
# looking up amending laws in the same DB, and write rows to artigos.db.
#
# REASONING
# The parser produces "leaves" — one per (article, path) — but does NOT
# resolve dates. This module:
#   1. Looks up the publication date of each amending lei referenced in
#      annotations (e.g., "Lei nº 14.230, de 2021" → 2021-10-25).
#   2. Computes vigente_desde / vigente_ate / fonte for each leaf based on
#      strike/revision/annotation flags.
#   3. Writes the artigo table with all the columns.
#
# The pairing logic for old vs new versions:
#   - A struck leaf (is_struck=True) is the original version. It was in
#     force from the law's publication date until the amending law's
#     publication date.
#   - A non-struck leaf with revision=0 (or higher) is a current version
#     resulting from an amendment. Use the annotation's lei reference to
#     find when the amendment took effect.
#   - A non-struck leaf with no revision and no annotation is unchanged
#     since original publication; vigente_desde = original date,
#     vigente_ate = NULL.
#   - A leaf with annotation kind='incluido' was added by the amending lei;
#     vigente_desde = amending lei date, no original predecessor.
#   - A leaf with annotation kind='revogado' is currently revoked;
#     vigente_desde for the revoking event, vigente_ate = NULL but the
#     text is "(Revogado)" — we record this as a row with empty/marker text.
#
# ASSUMES
# planalto_legislacao.db is at PLANALTO_DB. The database has a table
# `legislacao` with `numero`, `data`, `texto_completo`, `html_raw` columns.
# It is produced by tools/planalto_scraper/scraper.py.
# The artigos.db is created if missing.

# SOURCE
# Default: ~/research/data/planalto/planalto_legislacao.db
# Override: PLANALTO_DB env var or --planalto-db CLI flag.
"""

from __future__ import annotations

import argparse
import os
import re
import sqlite3
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

# Import parser from same package
sys.path.insert(0, str(Path(__file__).parent))
from parser import Leaf, parse_law_html  # noqa: E402
from overrides_engine import apply_overrides  # noqa: E402

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

PLANALTO_DB = Path(
    os.environ.get(
        'PLANALTO_DB',
        Path.home() / 'research/data/planalto/planalto_legislacao.db'
    )
)
ARTIGOS_DB = Path(
    os.environ.get(
        'ARTIGOS_DB',
        Path.home() / 'research/data/lei/artigos.db'
    )
)

# Backwards-compatible alias for any caller still importing SAUDE_PLANALTO_DB
SAUDE_PLANALTO_DB = PLANALTO_DB


# ---------------------------------------------------------------------------
# Date resolution
# ---------------------------------------------------------------------------

# Brazilian month names (lowercase, with and without accents) → number
PT_MONTHS = {
    'janeiro': 1, 'fevereiro': 2, 'março': 3, 'marco': 3, 'abril': 4,
    'maio': 5, 'junho': 6, 'julho': 7, 'agosto': 8, 'setembro': 9,
    'outubro': 10, 'novembro': 11, 'dezembro': 12,
}

DATE_RE = re.compile(
    r'(\d{1,2})\s*de\s*([a-zçãéí]+)\s*(?:de\s*)?(\d{4})',
    re.IGNORECASE,
)


def parse_pt_date(s: str) -> Optional[str]:
    """Parse a Portuguese date like '2 de junho de 1992' → '1992-06-02'.

    Returns None if parsing fails.
    """
    if not s:
        return None
    m = DATE_RE.search(s.lower())
    if not m:
        return None
    day = int(m.group(1))
    month_name = m.group(2)
    month = PT_MONTHS.get(month_name)
    if month is None:
        return None
    year = int(m.group(3))
    return f'{year:04d}-{month:02d}-{day:02d}'


def resolve_lei_date(
    cur: sqlite3.Cursor,
    lei_numero: str,
    lei_ano: str,
) -> Optional[str]:
    """Look up the publication date of a lei in planalto_legislacao.db.

    Returns YYYY-MM-DD or None if not found.
    Falls back to YYYY-01-01 if we have ano but no exact date.
    """
    if not lei_numero:
        return f'{lei_ano}-01-01' if lei_ano else None

    # Planalto stores numero with no dots (we already stripped them in parser).
    # The data column is like "2 de JUNHO de 1992" or "25 de outubro de 2021".
    cur.execute(
        "SELECT data FROM legislacao WHERE numero = ? AND tipo LIKE '%lei%' AND data LIKE ? LIMIT 1",
        (lei_numero, f'%{lei_ano}%'),
    )
    row = cur.fetchone()
    if row and row[0]:
        date = parse_pt_date(row[0])
        if date:
            return date

    # Try without ano filter
    cur.execute(
        "SELECT data FROM legislacao WHERE numero = ? AND tipo LIKE '%lei%' LIMIT 1",
        (lei_numero,),
    )
    row = cur.fetchone()
    if row and row[0]:
        date = parse_pt_date(row[0])
        if date:
            return date

    # Fallback
    return f'{lei_ano}-01-01' if lei_ano else None


# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------

SCHEMA = """
CREATE TABLE IF NOT EXISTS artigo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    apelido TEXT NOT NULL,
    numero_lei TEXT NOT NULL,
    ano_lei TEXT NOT NULL,
    capitulo TEXT,
    capitulo_titulo TEXT,
    secao TEXT,
    secao_titulo TEXT,
    artigo INTEGER NOT NULL,
    artigo_letra TEXT,
    path TEXT NOT NULL,
    texto TEXT NOT NULL,
    vigente_desde TEXT NOT NULL,    -- 'YYYY-MM-DD'
    vigente_ate TEXT,               -- 'YYYY-MM-DD' or NULL if in force
    fonte TEXT NOT NULL,            -- display: 'Lei nº 14.230, de 2021'
    fonte_id TEXT NOT NULL,         -- canonical: 'L14230-2021', 'LC219-2025', 'EC45-2004', etc.
    revogado INTEGER NOT NULL DEFAULT 0,  -- 1 if currently revoked
    ordem INTEGER NOT NULL,
    raw_anchor TEXT,
    observacoes TEXT
);
CREATE INDEX IF NOT EXISTS idx_artigo_lookup ON artigo(apelido, artigo, path, vigente_ate);
CREATE INDEX IF NOT EXISTS idx_artigo_lei ON artigo(numero_lei, ano_lei, artigo);
CREATE INDEX IF NOT EXISTS idx_artigo_apelido ON artigo(apelido);
CREATE INDEX IF NOT EXISTS idx_artigo_fonte ON artigo(fonte_id);
"""


def init_db(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(db_path)
    con.executescript(SCHEMA)
    return con


# ---------------------------------------------------------------------------
# Resolve leaves → DB rows
# ---------------------------------------------------------------------------

@dataclass
class Row:
    apelido: str
    numero_lei: str
    ano_lei: str
    capitulo: Optional[str]
    capitulo_titulo: Optional[str]
    secao: Optional[str]
    secao_titulo: Optional[str]
    artigo: int
    artigo_letra: Optional[str]
    path: str
    texto: str
    vigente_desde: str
    vigente_ate: Optional[str]
    fonte: str
    fonte_id: str
    revogado: int
    ordem: int
    raw_anchor: str
    observacoes: Optional[str] = None


TIPO_TO_PREFIX = {
    'Lei': 'L',
    'Lei Complementar': 'LC',
    'Medida Provisória': 'MP',
    'Decreto-Lei': 'DL',
    'Decreto': 'D',
    'Emenda Constitucional': 'EC',
}


def fonte_label(
    numero: Optional[str],
    ano: Optional[str],
    original_fonte: str,
    lei_tipo: Optional[str] = None,
) -> str:
    """Build a human-readable fonte label like 'Lei Complementar nº 219, de 2025'."""
    if not numero:
        return original_fonte
    n = numero
    if len(n) >= 4:
        n = f'{n[:-3]}.{n[-3:]}'
    tipo = lei_tipo or 'Lei'
    return f'{tipo} nº {n}, de {ano}'


def fonte_id_label(
    numero: Optional[str],
    ano: Optional[str],
    original_id: str,
    lei_tipo: Optional[str] = None,
) -> str:
    """Build a canonical fonte_id like 'L14230-2021', 'LC219-2025', 'EC45-2004'."""
    if not numero:
        return original_id
    prefix = TIPO_TO_PREFIX.get(lei_tipo or 'Lei', 'L')
    return f'{prefix}{numero}-{ano}'


def resolve_leaves_to_rows(
    leaves: list[Leaf],
    apelido: str,
    numero_lei: str,
    ano_lei: str,
    original_date: str,
    cur: sqlite3.Cursor,
) -> list[Row]:
    """Convert parsed leaves into DB rows with date resolution.

    Pairing logic:
    - For each (article, path), there may be multiple leaves: a struck
      original and a current revision (rev=0+).
    - The struck one's vigente_ate = the next version's vigente_desde.
    - The current version's vigente_desde = its annotation's lei date,
      vigente_ate = NULL (or the date of any later revision).
    """
    original_fonte = f'Lei nº {numero_lei[:-3]}.{numero_lei[-3:]}, de {ano_lei}' \
        if len(numero_lei) >= 4 else f'Lei nº {numero_lei}, de {ano_lei}'
    original_fonte_id = f'L{numero_lei}-{ano_lei}'

    def date_for(ann) -> Optional[str]:
        if not ann:
            return None
        return resolve_lei_date(cur, ann.lei_numero or '', ann.lei_ano or '')

    def fonte_for(ann) -> tuple[str, str]:
        if not ann:
            return original_fonte, original_fonte_id
        return (
            fonte_label(ann.lei_numero, ann.lei_ano, original_fonte, ann.lei_tipo),
            fonte_id_label(ann.lei_numero, ann.lei_ano, original_fonte_id, ann.lei_tipo),
        )

    # Group leaves by (article, article_letter, path) — same path can appear
    # multiple times: original + revisions
    groups: dict[tuple[int, Optional[str], str], list[Leaf]] = {}
    for L in leaves:
        key = (L.article, L.article_letter, L.path)
        groups.setdefault(key, []).append(L)

    rows: list[Row] = []
    for key, group in groups.items():
        # Sort group: struck (original/superseded) first, then by revision number
        group.sort(key=lambda L: (
            0 if L.is_struck else 1,
            L.revision if L.revision is not None else -1,
            L.ordem,
        ))

        # Pass 1: compute vigente_desde and fonte for each row, looking at
        # the leaf's annotation list to find the most informative source.
        desde_list: list[str] = []
        fontes: list[str] = []
        fonte_ids: list[str] = []
        for L in group:
            # Find the annotation that tells us when THIS version came into force.
            # Priority: 'incluido' (this clause was added) > 'redacao' (this
            # clause was rewritten). 'revogado' tells us when superseded, not
            # when introduced, so it's NOT used here.
            incluido = next((a for a in L.annotations if a.kind == 'incluido'), None)
            redacao = next((a for a in L.annotations if a.kind == 'redacao'), None)
            origin_ann = incluido or redacao

            if origin_ann and origin_ann.lei_numero:
                d = date_for(origin_ann)
                desde_list.append(d or original_date)
                f_label, f_id = fonte_for(origin_ann)
                fontes.append(f_label)
                fonte_ids.append(f_id)
            else:
                desde_list.append(original_date)
                fontes.append(original_fonte)
                fonte_ids.append(original_fonte_id)

        # Pass 2: vigente_ate. The chain logic:
        #   1. If this row has a 'revogado' annotation, vigente_ate = revoking lei date
        #   2. Else if there's a next row in the group, vigente_ate = next.vigente_desde
        #   3. Else NULL (currently in force)
        for i, L in enumerate(group):
            revogado_ann = next((a for a in L.annotations if a.kind == 'revogado'), None)

            ate: Optional[str] = None
            if revogado_ann:
                rev_date = date_for(revogado_ann)
                ate = rev_date

            if ate is None and i + 1 < len(group):
                ate = desde_list[i + 1]

            # 'revogado' flag: only set if THIS row is the currently-revoked
            # state — i.e., it's the last row in the chain AND it's revoked
            # AND it has no real text content (just '(Revogado)').
            is_current = (i == len(group) - 1)
            is_currently_revoked = (
                is_current
                and revogado_ann is not None
                and (not L.text or len(L.text) < 30)
            )

            if is_currently_revoked:
                revogado = 1
                texto = '[Revogado]'
            else:
                revogado = 0
                texto = L.text or '[no text]'

            rows.append(Row(
                apelido=apelido,
                numero_lei=numero_lei,
                ano_lei=ano_lei,
                capitulo=L.chapter,
                capitulo_titulo=L.chapter_titulo,
                secao=L.section,
                secao_titulo=L.section_titulo,
                artigo=L.article,
                artigo_letra=L.article_letter,
                path=L.path,
                texto=texto,
                vigente_desde=desde_list[i],
                vigente_ate=ate,
                fonte=fontes[i],
                fonte_id=fonte_ids[i],
                revogado=revogado,
                ordem=L.ordem,
                raw_anchor=L.raw_anchor,
            ))

    return rows


def insert_rows(con: sqlite3.Connection, apelido: str, rows: list[Row]) -> None:
    """Replace all rows for `apelido` with the new ones."""
    cur = con.cursor()
    cur.execute("DELETE FROM artigo WHERE apelido = ?", (apelido,))
    cur.executemany(
        """
        INSERT INTO artigo (
            apelido, numero_lei, ano_lei, capitulo, capitulo_titulo,
            secao, secao_titulo, artigo, artigo_letra, path, texto,
            vigente_desde, vigente_ate, fonte, fonte_id, revogado, ordem,
            raw_anchor, observacoes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (r.apelido, r.numero_lei, r.ano_lei, r.capitulo, r.capitulo_titulo,
             r.secao, r.secao_titulo, r.artigo, r.artigo_letra, r.path, r.texto,
             r.vigente_desde, r.vigente_ate, r.fonte, r.fonte_id, r.revogado,
             r.ordem, r.raw_anchor, r.observacoes)
            for r in rows
        ],
    )
    con.commit()


# ---------------------------------------------------------------------------
# Lei catalog (curated set of laws to ingest)
# ---------------------------------------------------------------------------

# Each entry: (apelido, numero_lei, ano_lei, planalto_id_or_None)
# planalto_id is the legislacao.id; we'll look it up if None.
LAW_CATALOG = [
    # (apelido, numero, ano, planalto_id_or_None, tipo)
    # tipo defaults to 'lei'; use 'lei_complementar' for LCs.
    ('LIA',     '8429',  '1992', 3220, 'lei'),
    ('L8666',   '8666',  '1993', 247,  'lei'),
    ('L14133',  '14133', '2021', 2607, 'lei'),
    ('LE',      '9504',  '1997', 5450, 'lei'),
    # Constitutional / judicial framework
    ('LOMAN',   '35',    '1979', None, 'lei_complementar'),  # LC 35 — Lei Orgânica da Magistratura
    # Electoral
    ('CE',      '4737',  '1965', None, 'lei'),                # Código Eleitoral
    ('LPP',     '9096',  '1995', None, 'lei'),                # Lei dos Partidos Políticos
    ('LI',      '64',    '1990', None, 'lei_complementar'),   # LC 64 — Inelegibilidades
    ('LFL',     '135',   '2010', None, 'lei_complementar'),   # LC 135 — Ficha Limpa
    ('L13165',  '13165', '2015', None, 'lei'),                # Reforma eleitoral
    ('L13487',  '13487', '2017', None, 'lei'),
    ('L13488',  '13488', '2017', None, 'lei'),
    ('L12891',  '12891', '2013', None, 'lei'),
    # MP / prosecutorial
    ('LOMP',    '8625',  '1993', None, 'lei'),                # Lei Orgânica do MP
    ('LCMP',    '75',    '1993', None, 'lei_complementar'),   # LC 75 — Estatuto do MP da União
    # Public administration / fiscal
    ('LRF',     '101',   '2000', None, 'lei_complementar'),   # Lei de Responsabilidade Fiscal
    ('LCT',     '131',   '2009', None, 'lei_complementar'),   # Lei da Transparência
    ('LAI',     '12527', '2011', None, 'lei'),                # Lei de Acesso à Informação
    ('LOTCU',   '8443',  '1992', None, 'lei'),                # Lei Orgânica do TCU
    ('L8112',   '8112',  '1990', None, 'lei'),                # Estatuto dos Servidores
    # Procurement / pregão
    # Note: planalto scraper stored these with wrong numero, hardcode the id
    ('LP',      '10520', '2002', 12804, 'lei'),               # Pregão
    ('RDC',     '12462', '2011', None, 'lei'),                # Regime Diferenciado
    # Anti-corruption / crime
    ('LAC',     '12846', '2013', None, 'lei'),                # Lei Anticorrupção
    ('LCO',     '12850', '2013', None, 'lei'),                # Crime Organizado
    ('LL',      '9613',  '1998', None, 'lei'),                # Lavagem
    ('LL2',     '12683', '2012', None, 'lei'),                # Lavagem reforma
    ('LCOT',    '8137',  '1990', None, 'lei'),                # Crimes ordem tributária
    ('LPC',     '13964', '2019', None, 'lei'),                # Pacote Anticrime
    ('L14230',  '14230', '2021', None, 'lei'),                # LIA reform
    # Civil / process
    ('CPC',     '13105', '2015', None, 'lei'),                # Código de Processo Civil
    ('CPP',     '3689',  '1941', None, 'decreto_lei'),        # Código de Processo Penal
    ('CC',      '10406', '2002', None, 'lei'),                # Código Civil
    ('LACP',    '7347',  '1985', None, 'lei'),                # Ação Civil Pública
    # Note: planalto scraper stored with wrong numero, hardcode the id
    ('LAP',     '4717',  '1965', 10390, 'lei'),               # Ação Popular
    # Antitrust
    ('LCADE',   '12529', '2011', None, 'lei'),                # Lei de Defesa da Concorrência
    # Other
    ('LGPD',    '13709', '2018', None, 'lei'),                # LGPD
    ('L13019',  '13019', '2014', None, 'lei'),                # MROSC
]


def fetch_law_html(cur: sqlite3.Cursor, planalto_id: int) -> Optional[tuple[str, str]]:
    """Fetch (html, original_date) for a law by its legislacao.id."""
    cur.execute("SELECT html_raw, data FROM legislacao WHERE id = ?", (planalto_id,))
    row = cur.fetchone()
    if not row:
        return None
    html, data = row
    original_date = parse_pt_date(data) or '1900-01-01'
    return html, original_date


def find_planalto_id(
    cur: sqlite3.Cursor,
    numero: str,
    ano: str,
    tipo: str = 'lei',
) -> Optional[int]:
    """Find a planalto record by (numero, tipo), preferring matches that
    look like the actual consolidated target law (not an amending lei
    that mentions it).

    Planalto's `numero` column isn't a reliable identifier — multiple
    records can share the same numero (the law itself + amending laws
    that reference it in their text). We score candidates by:

      1. anchor count (more anchors = more parseable content; the
         consolidated target law has the most because each leaf has
         its own anchor)
      2. html length
      3. year match in `data` field (tiebreaker)
    """
    cur.execute(
        "SELECT id, data, length(html_raw), "
        " (length(html_raw) - length(replace(html_raw, '<a name=\"art', ''))) "
        "  / length('<a name=\"art') AS n_anchors "
        "FROM legislacao WHERE numero = ? AND tipo = ?",
        (numero, tipo),
    )
    candidates = cur.fetchall()
    if not candidates:
        return None

    def score(row):
        _, data, length, n_anchors = row
        year_match = 1 if data and ano in (data or '') else 0
        return (n_anchors, length, year_match)

    candidates.sort(key=score, reverse=True)
    best = candidates[0]
    if best[3] == 0:  # zero anchors → unparseable
        return None
    return best[0]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description='Build artigos.db from planalto HTML')
    ap.add_argument('--planalto-db', type=Path, default=PLANALTO_DB,
                    help='Path to planalto_legislacao.db (raw scrape)')
    ap.add_argument('--artigos-db', type=Path, default=ARTIGOS_DB,
                    help='Path to artigos.db (output)')
    ap.add_argument('--apelido', type=str, default=None,
                    help='Build only this apelido (default: all in catalog)')
    args = ap.parse_args()

    # ASSUMES: planalto_db exists and is readable
    if not args.planalto_db.exists():
        sys.exit(f'planalto DB not found: {args.planalto_db}')

    src = sqlite3.connect(args.planalto_db)
    src_cur = src.cursor()

    out = init_db(args.artigos_db)

    # SOURCE: planalto_legislacao.db, table `legislacao`
    catalog = LAW_CATALOG
    if args.apelido:
        catalog = [c for c in catalog if c[0] == args.apelido]
        if not catalog:
            sys.exit(f'apelido {args.apelido!r} not in catalog')

    for entry in catalog:
        # Catalog entries can be (apelido, numero, ano, id) (4-tuple, legacy)
        # or (apelido, numero, ano, id, tipo) (5-tuple, new format).
        if len(entry) == 4:
            apelido, numero, ano, planalto_id = entry
            tipo = 'lei'
        else:
            apelido, numero, ano, planalto_id, tipo = entry

        print(f'Processing {apelido} ({tipo} {numero}/{ano})...', file=sys.stderr)

        # If no planalto_id provided, look it up from (numero, ano, tipo)
        if planalto_id is None:
            planalto_id = find_planalto_id(src_cur, numero, ano, tipo)
            if planalto_id is None:
                print(f'  not found in planalto DB ({tipo} {numero}/{ano})',
                      file=sys.stderr)
                continue

        result = fetch_law_html(src_cur, planalto_id)
        if result is None:
            print(f'  not found in planalto DB (id={planalto_id})', file=sys.stderr)
            continue
        html, original_date = result
        leaves = parse_law_html(html)
        rows = resolve_leaves_to_rows(leaves, apelido, numero, ano, original_date, src_cur)
        rows, n_overrides = apply_overrides(rows, apelido)
        insert_rows(out, apelido, rows)
        msg = f'  → {len(rows)} rows inserted'
        if n_overrides:
            msg += f' ({n_overrides} manual overrides applied)'
        print(msg, file=sys.stderr)

    src.close()
    out.close()
    print(f'Done. DB at {args.artigos_db}', file=sys.stderr)


if __name__ == '__main__':
    main()
