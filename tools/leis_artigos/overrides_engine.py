"""
Apply manual overrides to parsed rows.

# INTENT
# When planalto's HTML is buggy (typos, missing annotations, structural
# ambiguity), we layer hand-verified corrections on top of the parsed
# data. This module loads override files from overrides/{apelido}.py and
# applies them to a list of Row dataclass instances.
#
# REASONING
# Override files in overrides/{apelido}.py are the hand-curated source
# of truth for known planalto data quality issues. Each override carries
# its own verification note (stored in observacoes) so the corrections
# are auditable from the DB.
#
# ASSUMES
# Override files exist as overrides/{apelido}.py and export an OVERRIDES
# list of dicts with at least `match`, `note`, `verified`.
"""

from __future__ import annotations

import importlib.util
from dataclasses import asdict
from pathlib import Path
from typing import Any


OVERRIDES_DIR = Path(__file__).parent / 'overrides'


def load_overrides(apelido: str) -> list[dict]:
    """Load OVERRIDES list from overrides/{apelido}.py if present."""
    path = OVERRIDES_DIR / f'{apelido}.py'
    if not path.exists():
        return []
    spec = importlib.util.spec_from_file_location(f'overrides_{apelido}', path)
    if spec is None or spec.loader is None:
        return []
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    overrides = getattr(mod, 'OVERRIDES', [])
    for o in overrides:
        if 'match' not in o:
            raise ValueError(f'{apelido}: override missing "match": {o}')
        if 'note' not in o:
            raise ValueError(f'{apelido}: override missing "note": {o}')
        if 'verified' not in o:
            raise ValueError(f'{apelido}: override missing "verified": {o}')
    return overrides


def _row_matches(row: dict, criteria: Any) -> bool:
    if criteria == 'all':
        return True
    if not isinstance(criteria, dict):
        return False
    for col, expected in criteria.items():
        if row.get(col) != expected:
            return False
    return True


def apply_overrides(rows: list, apelido: str) -> tuple[list, int]:
    """Apply overrides to a list of Row dataclass instances.

    Returns (new_rows, n_modifications).
    """
    overrides = load_overrides(apelido)
    if not overrides:
        return rows, 0

    n_mods = 0
    keep = []
    for row in rows:
        row_dict = asdict(row)
        delete_this = False
        notes: list[str] = []
        for o in overrides:
            if not _row_matches(row_dict, o['match']):
                continue
            if o.get('delete'):
                delete_this = True
                n_mods += 1
                continue
            for col, val in (o.get('set') or {}).items():
                if not hasattr(row, col):
                    raise ValueError(
                        f'{apelido}: override sets unknown column {col!r}: {o}'
                    )
                setattr(row, col, val)
                row_dict[col] = val
                n_mods += 1
            notes.append(f"[{o['verified']}] {o['note']}")
        if delete_this:
            continue
        if notes:
            existing = row.observacoes or ''
            combined = (existing + '\n' if existing else '') + '\n'.join(notes)
            row.observacoes = combined
        keep.append(row)
    return keep, n_mods
