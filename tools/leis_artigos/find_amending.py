#!/usr/bin/env python3
"""
Find candidate amending laws for a given article in planalto_legislacao.db.

# INTENT
# When a row in artigos.db has a wrong vigente_desde (e.g., the article
# was added by an amendment but the parser fell back to the original lei
# date), this utility helps find the AMENDING lei by searching the
# planalto FTS5 index. Output is a candidate list — the user verifies
# and writes an override.
#
# REASONING
# Cross-referencing within the planalto corpus is far more reliable than
# external web search: every federal lei is here, full text included.
# But mapping "art X of lei Y" → "the lei that amended this clause"
# requires text search across 57k laws. FTS5 makes that fast.
#
# USAGE
#   find_amending.py LE 36 --letter A
#       Find laws that mention "Art. 36-A" and "L 9.504" or "9.504/1997"
#
#   find_amending.py LIA 17 --letter A --before 2021
#       Same but only laws published before 2021
#
#   find_amending.py LE 11 --paragrafo 10
#       Find laws that mention "art. 11, § 10" of L 9.504
"""

from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

# Catalog must agree with build.py
sys.path.insert(0, str(Path(__file__).parent))
from build import LAW_CATALOG, PLANALTO_DB, parse_pt_date  # noqa: E402


def get_target_lei(apelido: str) -> tuple[str, str]:
    """Return (numero, ano) for an apelido in the catalog."""
    for entry in LAW_CATALOG:
        if entry[0] == apelido:
            return entry[1], entry[2]
    sys.exit(f'Apelido {apelido!r} not in catalog')


def search_amending(
    cur: sqlite3.Cursor,
    target_numero: str,
    target_ano: str,
    artigo: int,
    letter: str | None = None,
    paragrafo: str | None = None,
    before: str | None = None,
) -> list[tuple]:
    """Search planalto FTS for laws that mention a specific article.

    Returns list of (id, numero, data, parsed_date, ementa).
    """
    # Build FTS query: must mention BOTH the article AND the target lei
    art_str = f'Art. {artigo}'
    if letter:
        art_str += f'-{letter.upper()}'

    # Target lei reference: planalto often writes it as "Lei nº 9.504"
    # or "9.504/97" or "Lei 9504". Use the formatted version.
    if len(target_numero) >= 4:
        formatted = f'{target_numero[:-3]}.{target_numero[-3:]}'
    else:
        formatted = target_numero
    lei_ref = f'"{formatted}"'

    fts_query = f'"{art_str}" AND {lei_ref}'

    cur.execute(
        """
        SELECT l.id, l.tipo, l.numero, l.data, l.ementa
        FROM legislacao l JOIN legislacao_fts f ON l.id = f.rowid
        WHERE f.legislacao_fts MATCH ?
        """,
        (fts_query,),
    )
    raw = cur.fetchall()

    # Parse dates and filter
    results = []
    for row in raw:
        id_, tipo, numero, data, ementa = row
        if numero == target_numero:
            # Skip the target lei itself
            continue
        parsed = parse_pt_date(data) if data else None
        if before and parsed and parsed >= before:
            continue
        results.append((id_, tipo, numero, data, parsed, ementa))

    # Sort by parsed date (oldest first)
    results.sort(key=lambda r: r[4] or '9999-99-99')
    return results


def main():
    ap = argparse.ArgumentParser(
        description='Find candidate amending laws for a given article',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    ap.add_argument('apelido', help='Target law apelido (must be in catalog)')
    ap.add_argument('artigo', type=int, help='Article number')
    ap.add_argument('--letter', help='Article letter suffix (e.g., A for 36-A)')
    ap.add_argument('--paragrafo', help='Optional paragraph number to refine search')
    ap.add_argument('--before', metavar='YYYY-MM-DD',
                    help='Only consider laws published before this date')
    ap.add_argument('--planalto-db', type=Path, default=PLANALTO_DB)
    args = ap.parse_args()

    target_numero, target_ano = get_target_lei(args.apelido)

    con = sqlite3.connect(args.planalto_db)
    cur = con.cursor()

    print(f'Searching planalto for laws mentioning Art. {args.artigo}'
          + (f'-{args.letter.upper()}' if args.letter else '')
          + f' of {args.apelido} (Lei {target_numero}/{target_ano})...')
    if args.before:
        print(f'  filtered to laws published before {args.before}')
    print()

    results = search_amending(
        cur, target_numero, target_ano,
        args.artigo, args.letter, args.paragrafo, args.before,
    )

    if not results:
        print('No candidates found.')
        return

    print(f'{len(results)} candidate(s):')
    print()
    print(f'{"date":<12} {"tipo":<18} {"numero":<8}  ementa')
    print('-' * 100)
    for id_, tipo, numero, data, parsed, ementa in results:
        ementa_clean = ' '.join((ementa or '').split())[:70]
        date_str = parsed or '?'
        print(f'{date_str:<12} {(tipo or "")[:18]:<18} {numero:<8}  {ementa_clean}')

    print()
    print('To verify a candidate, fetch its text:')
    print(f'  sqlite3 {args.planalto_db} "SELECT texto_completo FROM legislacao WHERE id=ID" | less')
    print()
    print('Then write an override in overrides/{}.py:'.format(args.apelido))
    print("""    {
        'match': {{'artigo': %d, ..., 'vigente_desde': 'WRONG_DATE'}},
        'set': {{'vigente_desde': 'CORRECT_DATE'}},
        'note': 'Art %d was added by Lei X/YYYY. Verified by checking texto of L X.',
        'verified': 'YYYY-MM-DD',
    }""" % (args.artigo, args.artigo))


if __name__ == '__main__':
    main()
