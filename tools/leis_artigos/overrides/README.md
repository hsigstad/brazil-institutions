# Manual overrides for parsed law data

When the parser produces wrong rows because of bugs in planalto's source
HTML (typos, missing annotations, structural ambiguities), we apply
**manual overrides** that get layered on top of the parsed data during
the build.

## When to use an override

Use one when the planalto data is wrong (or ambiguous) and you've
**verified the correct value against an authoritative source** —
typically:
- The actual planalto.gov.br page
- The amending lei's text
- The Diário Oficial publication
- Cross-references in academic legal commentary

Do NOT use overrides to "improve" formatting, paraphrase legal text, or
fix things that are merely stylistically odd. Stick to factual
corrections.

## File format

One file per law, named by `apelido` (e.g., `LIA.py`, `L8666.py`,
`LE.py`). Each file exports an `OVERRIDES` list of dicts:

```python
# overrides/LIA.py
"""Manual overrides for LIA (Lei 8.429/1992)."""

OVERRIDES = [
    {
        # criteria to find the row(s) to fix — any column name in artigo table
        'match': {'raw_anchor': 'art17aiiii'},
        # fields to update on matching row(s)
        'set': {'path': 'III'},
        # plain-language explanation, stored in observacoes
        'note': 'Path corrected from planalto typo art17aiiii (IIII not Roman) → III. '
                'Verified against L 13.964/2019 art. 6 which inserted Art. 17-A III.',
        # date when this override was verified by a human
        'verified': '2026-04-09',
        # who verified
        'verified_by': 'henrik',
    },
]
```

## Override actions

Each override has:

- **match** (dict): column → value criteria. Matches rows where ALL given
  columns equal the given values. Special: `'match': 'all'` matches every
  row for the law (use sparingly).
- **set** (dict, optional): column → new value. Updates the matching rows.
- **delete** (bool, optional): if True, drops the matching rows entirely.
- **note** (str, required): human-readable explanation of why the
  correction is needed and how it was verified. Stored in observacoes.
- **verified** (str, required): YYYY-MM-DD date of verification.
- **verified_by** (str, optional): person who verified.

## Order of application

1. Parser produces raw rows from planalto HTML
2. Build script resolves dates and creates Row objects
3. Overrides applied in the order they appear in the OVERRIDES list
4. Rows inserted into artigos.db

If multiple overrides match the same row, they all apply (last write
wins for set, delete short-circuits).

## Why store the note in observacoes

The `observacoes` column on each artigo row preserves the override note,
so anyone querying the DB sees both the corrected value AND why it was
corrected. This means:
- Future-Henrik can audit the corrections
- The override is self-documenting at the data level
- If we re-build from a new planalto scrape and the upstream bug is
  fixed, the observacao still flags that this row had a manual fix
  history
