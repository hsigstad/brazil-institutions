#!/usr/bin/env python3
"""
Use the amendment table to fix wrong vigente_desde dates in the artigo table.

# INTENT
# When the parser falls back to the original lei date for a clause that was
# actually added by an amendment (because planalto's consolidated text lacks
# the `(Incluído pela Lei X)` annotation), the artigo row gets the wrong
# vigente_desde. This script joins artigo with amendment to compute the
# correct date and update those rows in place.
#
# REASONING
# The amendment table is built independently from the amending laws' HTML
# (which has explicit hyperlinks to the target). When it says "L 12.034/2009
# touched LE Art 36-A", we can trust that more than the consolidated text's
# missing annotation.
#
# We apply fixes only in HIGH-CONFIDENCE cases:
#   1. Rows with artigo_letra IS NOT NULL (lettered articles like 36-A,
#      8-A) — these were definitely added by amendment since original laws
#      don't have letter suffixes.
#   2. The current fonte_id is the original lei (i.e., the parser fell
#      through to the default).
#   3. There exists an amendment row for this (apelido, artigo,
#      artigo_letra) tuple.
#
# For each match, we set vigente_desde to the earliest amendment date and
# update fonte/fonte_id accordingly. The observacoes column gets a note
# documenting the fix.
#
# We do NOT touch rows where artigo_letra IS NULL — those might have been
# in the original lei. Add more cases as we verify them.

# ASSUMES
# Both `artigo` and `amendment` tables have been populated (run build.py
# and build_amendments.py first).
"""

from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build import ARTIGOS_DB  # noqa: E402


def find_fixable_rows(con: sqlite3.Connection) -> list[dict]:
    """Find rows whose vigente_desde looks wrong, with a candidate fix.

    HIGH-CONFIDENCE criteria (we apply only these):
    1. fonte_id = original lei id (parser fell through to default)
    2. STANDALONE row (only one row for this path — not part of a chain
       of original/revisions, which would mean planalto annotated it)
    3. There exists an amendment with action='add' for this exact tuple
       (apelido, artigo, artigo_letra, path)
    4. The amendment date is LATER than the current (wrong) vigente_desde

    Letter articles (artigo_letra IS NOT NULL) are the main case — they
    cannot have existed in the original lei.
    """
    cur = con.cursor()
    cur.row_factory = sqlite3.Row
    sql = """
        WITH chain_size AS (
            SELECT apelido, artigo,
                   COALESCE(artigo_letra, '__NULL__') AS letra_key,
                   path,
                   COUNT(*) AS n_rows
            FROM artigo
            GROUP BY apelido, artigo, letra_key, path
        )
        SELECT
            a.id,
            a.apelido,
            a.artigo,
            a.artigo_letra,
            a.path,
            a.vigente_desde AS old_vigente_desde,
            a.fonte AS old_fonte,
            a.fonte_id AS old_fonte_id,
            a.observacoes AS old_obs,
            (
                SELECT MIN(am.amending_data)
                FROM amendment am
                WHERE am.target_apelido = a.apelido
                  AND am.artigo = a.artigo
                  AND ((am.artigo_letra IS NULL AND a.artigo_letra IS NULL)
                       OR am.artigo_letra = a.artigo_letra)
                  AND am.path = a.path
                  AND am.action = 'add'
            ) AS earliest_add_date,
            (
                SELECT am.amending_label
                FROM amendment am
                WHERE am.target_apelido = a.apelido
                  AND am.artigo = a.artigo
                  AND ((am.artigo_letra IS NULL AND a.artigo_letra IS NULL)
                       OR am.artigo_letra = a.artigo_letra)
                  AND am.path = a.path
                  AND am.action = 'add'
                ORDER BY am.amending_data LIMIT 1
            ) AS earliest_add_label,
            (
                SELECT am.amending_fonte_id
                FROM amendment am
                WHERE am.target_apelido = a.apelido
                  AND am.artigo = a.artigo
                  AND ((am.artigo_letra IS NULL AND a.artigo_letra IS NULL)
                       OR am.artigo_letra = a.artigo_letra)
                  AND am.path = a.path
                  AND am.action = 'add'
                ORDER BY am.amending_data LIMIT 1
            ) AS earliest_add_fonte_id
        FROM artigo a
        JOIN chain_size c
          ON c.apelido = a.apelido
         AND c.artigo = a.artigo
         AND c.letra_key = COALESCE(a.artigo_letra, '__NULL__')
         AND c.path = a.path
        WHERE a.fonte_id = 'L' || a.numero_lei || '-' || a.ano_lei
          AND c.n_rows = 1   -- standalone, not part of a multi-version chain
    """
    cur.execute(sql)
    rows = []
    for r in cur.fetchall():
        if r['earliest_add_date'] is None:
            continue
        if r['earliest_add_date'] <= r['old_vigente_desde']:
            continue
        rows.append({
            'id': r['id'],
            'apelido': r['apelido'],
            'artigo': r['artigo'],
            'artigo_letra': r['artigo_letra'],
            'path': r['path'],
            'old_vigente_desde': r['old_vigente_desde'],
            'old_fonte': r['old_fonte'],
            'old_fonte_id': r['old_fonte_id'],
            'old_obs': r['old_obs'],
            'earliest_amendment_date': r['earliest_add_date'],
            'earliest_amendment_label': r['earliest_add_label'],
            'earliest_amendment_fonte_id': r['earliest_add_fonte_id'],
            'reason': 'add_amendment',
        })

    # Pass 2: letter articles where the CAPUT has a known add date.
    # Sub-elements (incisos, paragraphs) of an added article must be at
    # least as old as the article itself. We use the article-caput's add
    # date as a lower bound for sub-element vigente_desde.
    sql2 = """
        WITH letter_caput_adds AS (
            SELECT target_apelido, artigo, artigo_letra,
                   MIN(amending_data) AS earliest_caput_add,
                   (SELECT amending_label FROM amendment a2
                    WHERE a2.target_apelido=a.target_apelido AND a2.artigo=a.artigo
                      AND a2.artigo_letra=a.artigo_letra AND a2.path='caput'
                      AND a2.action='add'
                    ORDER BY a2.amending_data LIMIT 1) AS label,
                   (SELECT amending_fonte_id FROM amendment a2
                    WHERE a2.target_apelido=a.target_apelido AND a2.artigo=a.artigo
                      AND a2.artigo_letra=a.artigo_letra AND a2.path='caput'
                      AND a2.action='add'
                    ORDER BY a2.amending_data LIMIT 1) AS fid
            FROM amendment a
            WHERE artigo_letra IS NOT NULL AND path='caput' AND action='add'
            GROUP BY target_apelido, artigo, artigo_letra
        ),
        chain_size AS (
            SELECT apelido, artigo,
                   COALESCE(artigo_letra, '__NULL__') AS letra_key,
                   path,
                   COUNT(*) AS n_rows
            FROM artigo
            GROUP BY apelido, artigo, letra_key, path
        )
        SELECT a.id, a.apelido, a.artigo, a.artigo_letra, a.path,
               a.vigente_desde AS old_vigente_desde,
               a.fonte AS old_fonte, a.fonte_id AS old_fonte_id,
               a.observacoes AS old_obs,
               lca.earliest_caput_add AS earliest_amendment_date,
               lca.label AS earliest_amendment_label,
               lca.fid AS earliest_amendment_fonte_id
        FROM artigo a
        JOIN letter_caput_adds lca
          ON lca.target_apelido = a.apelido
         AND lca.artigo = a.artigo
         AND lca.artigo_letra = a.artigo_letra
        JOIN chain_size c
          ON c.apelido = a.apelido AND c.artigo = a.artigo
         AND c.letra_key = COALESCE(a.artigo_letra, '__NULL__')
         AND c.path = a.path
        WHERE a.artigo_letra IS NOT NULL
          AND a.fonte_id = 'L' || a.numero_lei || '-' || a.ano_lei
          AND c.n_rows = 1
          AND a.path != 'caput'  -- caput is handled by pass 1
    """
    cur.execute(sql2)
    seen_ids = {row['id'] for row in rows}
    for r in cur.fetchall():
        if r['id'] in seen_ids:
            continue
        if r['earliest_amendment_date'] is None:
            continue
        if r['earliest_amendment_date'] <= r['old_vigente_desde']:
            continue
        rows.append({
            'id': r['id'],
            'apelido': r['apelido'],
            'artigo': r['artigo'],
            'artigo_letra': r['artigo_letra'],
            'path': r['path'],
            'old_vigente_desde': r['old_vigente_desde'],
            'old_fonte': r['old_fonte'],
            'old_fonte_id': r['old_fonte_id'],
            'old_obs': r['old_obs'],
            'earliest_amendment_date': r['earliest_amendment_date'],
            'earliest_amendment_label': r['earliest_amendment_label'],
            'earliest_amendment_fonte_id': r['earliest_amendment_fonte_id'],
            'reason': 'letter_caput_inheritance',
        })
    return rows


def apply_fix(con: sqlite3.Connection, row: dict, dry_run: bool = False) -> None:
    """Update one row with the corrected date and source."""
    reason = row.get('reason', 'add_amendment')
    if reason == 'letter_caput_inheritance':
        explain = (
            f'inferred from amendment table: the caput of Art. '
            f'{row["artigo"]}-{row["artigo_letra"]} was added by '
            f'{row["earliest_amendment_label"]}, so this sub-element '
            f'cannot be older.'
        )
    else:
        explain = (
            f'based on amendment table: {row["earliest_amendment_label"]} '
            f'first added this clause.'
        )
    note = (
        f'[auto-fix {row["earliest_amendment_date"]}] '
        f'vigente_desde corrected from {row["old_vigente_desde"]} '
        f'to {row["earliest_amendment_date"]} — {explain}'
    )
    new_obs = (row['old_obs'] + '\n' if row['old_obs'] else '') + note

    if dry_run:
        return

    con.execute(
        """
        UPDATE artigo
        SET vigente_desde = ?,
            fonte = ?,
            fonte_id = ?,
            observacoes = ?
        WHERE id = ?
        """,
        (
            row['earliest_amendment_date'],
            row['earliest_amendment_label'],
            row['earliest_amendment_fonte_id'],
            new_obs,
            row['id'],
        ),
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--db', type=Path, default=ARTIGOS_DB)
    ap.add_argument('--dry-run', action='store_true',
                    help='Show what would change without modifying the DB')
    ap.add_argument('--limit', type=int, help='Process only first N fixes (for testing)')
    args = ap.parse_args()

    if not args.db.exists():
        sys.exit(f'artigos.db not found at {args.db}')

    con = sqlite3.connect(args.db)

    fixes = find_fixable_rows(con)
    if args.limit:
        fixes = fixes[: args.limit]

    if not fixes:
        print('No fixable rows found.')
        return

    print(f'Found {len(fixes)} rows with wrong vigente_desde.')
    print()
    print(f'{"apelido":<8} {"art":<10} {"path":<10} {"old_date":<12} → {"new_date":<12} {"new_fonte"}')
    print('-' * 100)
    for f in fixes[:30]:
        label = f'{f["artigo"]}-{f["artigo_letra"]}'
        old_d = f['old_vigente_desde']
        new_d = f['earliest_amendment_date']
        new_f = f['earliest_amendment_fonte_id']
        print(f'{f["apelido"]:<8} {label:<10} {f["path"]:<10} {old_d:<12} → {new_d:<12} {new_f}')
    if len(fixes) > 30:
        print(f'... and {len(fixes) - 30} more')

    if args.dry_run:
        print()
        print('(dry run — no changes made. Re-run without --dry-run to apply.)')
        return

    print()
    for f in fixes:
        apply_fix(con, f)
    con.commit()
    con.close()
    print(f'Applied {len(fixes)} fixes.')


if __name__ == '__main__':
    main()
