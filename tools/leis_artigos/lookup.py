#!/usr/bin/env python3
"""
Look up the text of a Brazilian law article from artigos.db.

# INTENT
# CLI for retrieving the verbatim text of a specific article (or part of an
# article) of a Brazilian law tracked in artigos.db. Supports lookup by
# apelido (LIA, CF, CPC, ...) + article number + structural path, with
# version selection by date or "currently in force".
#
# REASONING
# Henrik (and Claude) need to cite exact statutory text in papers and notes
# without paraphrasing. The artigos table is the source of truth; this CLI
# is the friendly interface.

# USAGE
#   lookup_artigo LIA 9                       # Art. 9, all current paths
#   lookup_artigo LIA 9 --path caput          # just the caput
#   lookup_artigo LIA 9 --path II             # inciso II
#   lookup_artigo LIA 9 --path II --history   # inciso II all versions
#   lookup_artigo LIA 9 --as-of 2020-01-01    # version in force on that date
#   lookup_artigo LIA --list-articles         # show all article numbers
#   lookup_artigo --list-laws                 # show all laws in the DB
"""

from __future__ import annotations

import argparse
import os
import re
import sqlite3
import sys
from pathlib import Path

ARTIGOS_DB = Path(
    os.environ.get(
        'ARTIGOS_DB',
        Path.home() / 'research/data/lei/artigos.db'
    )
)


# Path normalization: handles divergence between PATH_CONVENTION (dotted,
# 'I.a') and the DB's actual storage (concatenated, 'IA') for inciso +
# alínea paths. See cite.py for the full helper.
ROMAN_DIGITS = set("IVXLCDM")


def _is_roman_run(s: str) -> bool:
    return bool(s) and all(c in ROMAN_DIGITS for c in s)


def normalize_path_candidates(path):
    if not path:
        return [path]
    candidates = [path]
    parts = path.split(".")
    if (
        len(parts) == 2
        and _is_roman_run(parts[0])
        and len(parts[1]) == 1
        and parts[1].islower()
    ):
        candidates.append(f"{parts[0]}{parts[1].upper()}")
    elif (
        len(parts) == 3
        and parts[0].startswith("§")
        and _is_roman_run(parts[1])
        and len(parts[2]) == 1
        and parts[2].islower()
    ):
        candidates.append(f"{parts[0]}.{parts[1]}{parts[2].upper()}")
    elif (
        len(parts) == 3
        and _is_roman_run(parts[0])
        and len(parts[1]) == 1
        and parts[1].islower()
        and parts[2].isdigit()
    ):
        candidates.append(f"{parts[0]}{parts[1].upper()}{parts[2]}")
    elif (
        len(parts) == 4
        and parts[0].startswith("§")
        and _is_roman_run(parts[1])
        and len(parts[2]) == 1
        and parts[2].islower()
        and parts[3].isdigit()
    ):
        candidates.append(f"{parts[0]}.{parts[1]}{parts[2].upper()}{parts[3]}")
    return candidates


# Strict path validation per PATH_CONVENTION.md
PATH_RE = re.compile(
    r'^(caput|ementa|preambulo'
    r'|§(?:unico|\d+)(?:\.[IVXLCDM]+(?:\.[a-z](?:\.\d+)?)?)?'
    r'|[IVXLCDM]+(?:\.[a-z](?:\.\d+)?)?'
    r')$'
)


def validate_path(path: str) -> bool:
    return bool(PATH_RE.match(path))


def open_db(db_path: Path) -> sqlite3.Connection:
    if not db_path.exists():
        sys.exit(f'artigos.db not found at {db_path}. Run build.py first.')
    return sqlite3.connect(db_path)


def list_laws(con: sqlite3.Connection):
    cur = con.cursor()
    cur.execute(
        "SELECT apelido, numero_lei, ano_lei, COUNT(*) FROM artigo "
        "GROUP BY apelido ORDER BY apelido"
    )
    rows = cur.fetchall()
    if not rows:
        print('(empty database)')
        return
    print(f'{"apelido":<10} {"lei":<12} rows')
    print('-' * 40)
    for apelido, numero, ano, count in rows:
        lei = f'{numero}/{ano}'
        print(f'{apelido:<10} {lei:<12} {count}')


def list_amendments_for_article(
    con: sqlite3.Connection,
    apelido: str,
    artigo: int,
    artigo_letra,
    path,
):
    """Show all amendments that touched a given article."""
    cur = con.cursor()
    cur.row_factory = sqlite3.Row
    sql = """
        SELECT amending_fonte_id, amending_label, amending_data, action, path
        FROM amendment
        WHERE target_apelido = ? AND artigo = ?
    """
    params = [apelido, artigo]
    if artigo_letra:
        sql += " AND artigo_letra = ?"
        params.append(artigo_letra)
    else:
        sql += " AND artigo_letra IS NULL"
    if path:
        candidates = normalize_path_candidates(path)
        if len(candidates) == 1:
            sql += " AND path = ?"
            params.append(candidates[0])
        else:
            placeholders = ",".join("?" * len(candidates))
            sql += f" AND path IN ({placeholders})"
            params.extend(candidates)
    sql += " ORDER BY amending_data, path"
    cur.execute(sql, params)
    rows = cur.fetchall()
    if not rows:
        msg = f'No amendments found for {apelido} Art. {artigo}'
        if artigo_letra:
            msg += f'-{artigo_letra}'
        if path:
            msg += f' path={path}'
        print(msg)
        return
    label = f'Art. {artigo}{"-" + artigo_letra if artigo_letra else ""}'
    print(f'## {len(rows)} amendments to {apelido} {label}'
          + (f' (path={path})' if path else ''))
    print()
    print(f'{"date":<12} {"action":<8} {"path":<10} fonte')
    print('-' * 70)
    for r in rows:
        print(f'{r["amending_data"]:<12} {r["action"]:<8} {r["path"]:<10} {r["amending_label"]}')


def list_by_amending(con: sqlite3.Connection, fonte_id: str):
    """Show all amendments made by a given amending lei."""
    cur = con.cursor()
    cur.row_factory = sqlite3.Row
    cur.execute(
        """
        SELECT target_apelido, target_filename, target_numero, action,
               artigo, artigo_letra, path
        FROM amendment
        WHERE amending_fonte_id = ?
        ORDER BY target_apelido, artigo, artigo_letra, path
        """,
        (fonte_id,),
    )
    rows = cur.fetchall()
    if not rows:
        sys.exit(f'No amendments found for {fonte_id}')
    print(f'## {len(rows)} amendments by {fonte_id}')
    print()
    by_target: dict = {}
    for r in rows:
        target = r['target_apelido'] or f'L{r["target_numero"]} ({r["target_filename"]})'
        by_target.setdefault(target, []).append(r)
    for target, recs in by_target.items():
        print(f'### {target} — {len(recs)} amendments')
        for r in recs:
            label = f'Art. {r["artigo"]}{"-" + r["artigo_letra"] if r["artigo_letra"] else ""}'
            print(f'  {r["action"]:8} {label:10} {r["path"]}')
        print()


def list_articles(con: sqlite3.Connection, apelido: str):
    cur = con.cursor()
    cur.execute(
        "SELECT artigo, artigo_letra, COUNT(DISTINCT path) "
        "FROM artigo WHERE apelido = ? AND vigente_ate IS NULL "
        "GROUP BY artigo, artigo_letra ORDER BY artigo, artigo_letra"
    )
    rows = cur.fetchall()
    if not rows:
        print(f'No articles found for apelido {apelido!r}')
        return
    for artigo, letra, n_paths in rows:
        label = f'Art. {artigo}{"-" + letra if letra else ""}'
        print(f'  {label}  ({n_paths} paths)')


def format_row(row: dict, full: bool = False) -> str:
    """Format a single row for display."""
    artigo = row['artigo']
    letra = row['artigo_letra']
    label = f'Art. {artigo}{"-" + letra if letra else ""}'
    path = row['path']
    fonte = row['fonte']
    desde = row['vigente_desde']
    ate = row['vigente_ate'] or 'em vigor'
    revogado = ' [REVOGADO]' if row['revogado'] else ''
    out = []
    out.append(f'## {row["apelido"]} {label}, {path}{revogado}')
    if full:
        cap = row['capitulo']
        cap_t = row['capitulo_titulo']
        sec = row['secao']
        sec_t = row['secao_titulo']
        if cap:
            out.append(f'   Capitulo {cap}{": " + cap_t if cap_t else ""}')
        if sec:
            out.append(f'   Secao {sec}{": " + sec_t if sec_t else ""}')
    out.append(f'   Vigencia: {desde} -> {ate}')
    out.append(f'   Fonte: {fonte}')
    out.append('')
    out.append(f'   {row["texto"]}')
    return '\n'.join(out)


def lookup(
    con: sqlite3.Connection,
    apelido: str,
    artigo: int,
    artigo_letra,
    path,
    history: bool,
    as_of,
    full: bool,
):
    cur = con.cursor()
    cur.row_factory = sqlite3.Row

    sql = "SELECT * FROM artigo WHERE apelido = ? AND artigo = ?"
    params = [apelido, artigo]

    if artigo_letra:
        sql += " AND artigo_letra = ?"
        params.append(artigo_letra)
    else:
        sql += " AND artigo_letra IS NULL"

    if path:
        candidates = normalize_path_candidates(path)
        if len(candidates) == 1:
            sql += " AND path = ?"
            params.append(candidates[0])
        else:
            placeholders = ",".join("?" * len(candidates))
            sql += f" AND path IN ({placeholders})"
            params.extend(candidates)

    if not history:
        if as_of:
            sql += " AND vigente_desde <= ? AND (vigente_ate IS NULL OR vigente_ate > ?)"
            params.extend([as_of, as_of])
        else:
            sql += " AND vigente_ate IS NULL"

    sql += " ORDER BY ordem, vigente_desde"

    cur.execute(sql, params)
    rows = cur.fetchall()

    if not rows:
        msg = f'No matches for {apelido} Art. {artigo}'
        if artigo_letra:
            msg += f'-{artigo_letra}'
        if path:
            msg += f' path={path}'
        if as_of:
            msg += f' as of {as_of}'
        if not history and not as_of:
            msg += ' (currently in force)'
        sys.exit(msg)

    for r in rows:
        d = {k: r[k] for k in r.keys()}
        print(format_row(d, full=full))
        print()


def main():
    ap = argparse.ArgumentParser(
        description='Look up Brazilian law articles from artigos.db',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    ap.add_argument('apelido', nargs='?', help='Law apelido, e.g., LIA')
    ap.add_argument('artigo', nargs='?', type=str,
                    help='Article number (e.g., 9 or 17-A)')
    ap.add_argument('--path', '-p', help='Specific path within the article (e.g., II, §1, §1.II)')
    ap.add_argument('--history', action='store_true',
                    help='Show all historical versions, not just the one in force')
    ap.add_argument('--as-of', metavar='YYYY-MM-DD',
                    help='Show version in force on this date')
    ap.add_argument('--full', '-f', action='store_true',
                    help='Show chapter/section context too')
    ap.add_argument('--list-laws', action='store_true', help='List all laws in the DB')
    ap.add_argument('--list-articles', action='store_true',
                    help='List all article numbers for the given apelido')
    ap.add_argument('--amendments', action='store_true',
                    help='Show all amendments that touched the given article')
    ap.add_argument('--by-amending', metavar='FONTE_ID',
                    help='List all amendments made by a given amending lei (e.g., L14230-2021)')
    ap.add_argument('--db', type=Path, default=ARTIGOS_DB, help='Path to artigos.db')
    args = ap.parse_args()

    con = open_db(args.db)

    if args.list_laws:
        list_laws(con)
        return

    if args.list_articles:
        if not args.apelido:
            sys.exit('--list-articles requires an apelido argument')
        list_articles(con, args.apelido)
        return

    if args.by_amending:
        list_by_amending(con, args.by_amending)
        return

    if not args.apelido or args.artigo is None:
        ap.print_help()
        sys.exit(1)

    # Parse "9" or "17-A"
    artigo_letra = None
    artigo_str = args.artigo
    if '-' in artigo_str:
        parts = artigo_str.split('-', 1)
        artigo_num = int(parts[0])
        artigo_letra = parts[1].upper()
    else:
        artigo_num = int(artigo_str)

    if args.path and not validate_path(args.path):
        sys.exit(
            f'Invalid path {args.path!r}. See PATH_CONVENTION.md.\n'
            'Examples: caput, II, §1, §1.II, §1.II.a, §unico'
        )

    if args.amendments:
        list_amendments_for_article(con, args.apelido, artigo_num, artigo_letra, args.path)
        return

    lookup(
        con=con,
        apelido=args.apelido,
        artigo=artigo_num,
        artigo_letra=artigo_letra,
        path=args.path,
        history=args.history,
        as_of=args.as_of,
        full=args.full,
    )


if __name__ == '__main__':
    main()
