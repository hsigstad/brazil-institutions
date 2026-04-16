#!/usr/bin/env python3
"""cite.py — resolve compact backtick-form citations.

Parses a citation string like `LIA.10.§1.II` or `Tema1199`
into structured fields and resolves it against the appropriate index:

- **Statute citations** (`LIA.10.§1.II`, `L14230-2021`, `CF.5`)
  resolve to rows in artigos.db (article-level law database).
- **Jurisprudence citations** (`Tema1199`, `ADI4650`, `HC126292`,
  `ADPF982`, `ADC43`, `ARE652777`) resolve to entries in
  jurisprudencia_index.yaml.
- **Súmula Vinculante citations** (`SV14`, `SV37`, `SV13`)
  resolve to entries in sumulas_vinculantes.yaml with verbatim text.
- **TSE Súmula citations** (`STSE38`, `STSE47`, `STSE62`)
  resolve to entries in sumulas_tse.yaml with verbatim text.

Inside markdown, citations are wrapped in single backticks so they
render as monospace inline code on github.com. The parser accepts
either bare citations or backtick-wrapped ones; the leading/trailing
backtick is stripped before parsing. Case prefixes like Tema/ADI/HC
are reserved for case IDs and disambiguate syntactically from law
identifiers.

The bracket forms are documented in ../../CLAUDE.md. Path syntax for
statutes follows PATH_CONVENTION.md.

If the artigos.db isn't available locally, the statute parser still
works — callers can use the parsed Citation object to format a fallback
(e.g., a planalto link). Likewise, if the jurisprudência index isn't
present, case citations parse but don't resolve.
"""

from __future__ import annotations

import argparse
import os
import re
import sqlite3
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

# ---------------------------------------------------------------------------
# Default DB location. Override with --db or ARTIGOS_DB env var.
# ---------------------------------------------------------------------------
DEFAULT_DB = Path(
    os.environ.get(
        "ARTIGOS_DB",
        Path.home() / "research" / "data" / "lei" / "artigos.db"
    )
)

# ---------------------------------------------------------------------------
# Default jurisprudência index location. Override with JURIS_INDEX env var.
# ---------------------------------------------------------------------------
DEFAULT_JURIS_INDEX = Path(
    os.environ.get(
        "JURIS_INDEX",
        Path(__file__).resolve().parent.parent.parent / "jurisprudencia_index.yaml"
    )
)

# ---------------------------------------------------------------------------
# Default Súmulas Vinculantes index location.
# ---------------------------------------------------------------------------
DEFAULT_SV_INDEX = Path(
    os.environ.get(
        "SV_INDEX",
        Path(__file__).resolve().parent.parent.parent / "sumulas_vinculantes.yaml"
    )
)

# ---------------------------------------------------------------------------
# Default TSE súmulas index location.
# ---------------------------------------------------------------------------
DEFAULT_STSE_INDEX = Path(
    os.environ.get(
        "STSE_INDEX",
        Path(__file__).resolve().parent.parent.parent / "sumulas_tse.yaml"
    )
)


# ---------------------------------------------------------------------------
# Citation grammar
# ---------------------------------------------------------------------------
# Backtick form (in markdown): `<identifier>[.<artigo>[-<letra>]][.<path>][<modifier>]`
#
# Where:
#   <identifier> is one of:
#       - apelido for cataloged laws (LIA, LE, L8666, L14133)
#       - canonical fonte_id (L13709-2018, LC64-1990, EC97-2017, DL2848-1940)
#       - conventional abbreviation (CF, CP, CPP, CLT, CTN)
#   <artigo>  = integer article number (1, 2, 145, ...)
#   <letra>   = single uppercase letter article suffix (A, B, ...)
#   <path>    = PATH_CONVENTION syntax (caput, II, II.a, §1, §1.II, ementa, ...)
#   <modifier> = one of:
#       @YYYY-MM-DD     - version in force on date
#       :original       - original-publication version
#       :current        - explicit current (default)
#       <space>from:X   - version introduced by source X
#
# Special cases:
#   `LIA`                -> whole law (no article)
#   `LIA.ementa`         -> the law's ementa (path-only, no article)
#   `L14230-2021`        -> non-cataloged amending law as an entity

# Identifier regex: apelidos, fonte_ids, and conventional abbreviations.
#   - Cataloged apelidos: pure uppercase letters with optional digits (LIA, LE, L8666)
#   - Fonte_ids: <prefix><numero>-<ano> (L14230-2021, LC64-1990, EC97-2017)
#   - Conventional abbreviations: CF, CP, CPP, CLT, CTN, etc.
IDENTIFIER_RE = r"(?P<identifier>[A-Z][A-Z0-9]*(?:-\d{4})?)"

# Article number with optional letter suffix
ARTIGO_RE = r"(?P<artigo>\d+)(?:-(?P<letra>[A-Z]))?"

# Path: anything that follows the article through the modifiers
# We capture greedily up to the modifier marker, then strip trailing spaces.
# Path may include §, dots, lowercase letters, digits, uppercase Roman numerals.
PATH_RE = r"(?P<path>(?:caput|ementa|preambulo|§unico|§\d+|[IVXLCDM]+)(?:\.[A-Za-z0-9§]+)*)"

# Modifier markers
DATE_RE = r"@(?P<date>\d{4}-\d{2}-\d{2})"
VINTAGE_RE = r":(?P<vintage>original|current)"
FROM_RE = r"\s+from:(?P<from_id>[A-Z][A-Z0-9]*-\d{4}|[A-Z][A-Z0-9]*)"

# Whole-law citation: just the identifier, no article, no path, no modifier
WHOLE_LAW_RE = re.compile(rf"^{IDENTIFIER_RE}$")

# Whole-law-with-ementa: e.g., `LIA.ementa`
LAW_WITH_PATH_RE = re.compile(
    rf"^{IDENTIFIER_RE}\.(?P<path>ementa|preambulo)"
    rf"(?:{DATE_RE}|{VINTAGE_RE}|{FROM_RE})?$"
)

# Article-level citation: identifier.artigo[-letra][.path][modifier]
ARTICLE_RE = re.compile(
    rf"^{IDENTIFIER_RE}"
    rf"\.{ARTIGO_RE}"
    rf"(?:\.{PATH_RE})?"
    rf"(?:{DATE_RE}|{VINTAGE_RE}|{FROM_RE})?$"
)

# Citations enclosed in single backticks (for find_citations).
# We capture all inline-code spans here; parse() filters non-citations
# by raising ValueError, which find_citations swallows.
BRACKET_RE = re.compile(r"`([^`\n]+?)`")

# ---------------------------------------------------------------------------
# Jurisprudence citation grammar
# ---------------------------------------------------------------------------
# Case IDs are an enumerated set of STF/STJ classe prefixes followed by
# a digit run, e.g.:
#   Tema1199, Tema897   — repercussão geral theme number
#   ADI4650, ADC43, ADPF982, ADO123  — abstract control
#   RE852475, ARE843989, AI...         — recurso/agravo
#   HC126292, RHC..., MS..., MI..., Pet..., Inq..., Rcl..., AP..., AR...
#
# A second pattern catches compound/named keys ending in a 4-digit year
# (e.g., LulaMoro2021) — used sparingly for joint-trial entries that
# don't fit the prefix grammar.
CASE_PREFIXES = (
    "Tema",
    "ADI", "ADC", "ADPF", "ADO",
    "RE", "ARE", "AI",
    "HC", "RHC",
    "MS", "RMS", "MI", "MC",
    "Rcl", "Pet", "Inq", "AP", "AR", "ACO",
)
CASE_ID_RE = re.compile(
    r"^(?:" + "|".join(CASE_PREFIXES) + r")\d+$"
    r"|^[A-Z][A-Za-z]+\d{4}$"
)

# ---------------------------------------------------------------------------
# Súmula Vinculante grammar
# ---------------------------------------------------------------------------
# `SV14`, `SV37` etc. — STF Súmulas Vinculantes by number.
# Resolves against sumulas_vinculantes.yaml. Strictly numeric; the
# canonical key in the YAML is "SV<number>" (e.g., SV14).
SV_RE = re.compile(r"^SV(\d+)$")

# ---------------------------------------------------------------------------
# TSE Súmula grammar
# ---------------------------------------------------------------------------
# `STSE38`, `STSE47` etc. — TSE Súmulas by number.
# Resolves against sumulas_tse.yaml. Canonical key: "STSE<number>".
# The "S" prefix mirrors `SV` (Súmula Vinculante) so all súmula
# citations begin with S; the court code follows.
STSE_RE = re.compile(r"^STSE(\d+)$")


# ---------------------------------------------------------------------------
# Path normalization
# ---------------------------------------------------------------------------
# PATH_CONVENTION specifies dotted paths (e.g., 'I.a' for inciso I alínea a),
# but the parser currently emits some leaves with concatenated paths
# (e.g., 'IA' instead of 'I.a', 'IIC' instead of 'II.c'). To make the
# resolver tolerant of both forms, we expand a canonical path into all
# candidate forms before querying.

ROMAN_DIGITS = set("IVXLCDM")


def _is_roman_run(s: str) -> bool:
    """True if s consists only of uppercase Roman digit characters (loose check)."""
    return bool(s) and all(c in ROMAN_DIGITS for c in s)


def normalize_path_candidates(path: str) -> List[str]:
    """Return candidate paths to try for the same logical location.

    Handles the divergence between PATH_CONVENTION (dotted, e.g., 'I.a')
    and the DB's actual storage (concatenated, e.g., 'IA') for inciso +
    alínea (and inciso + alínea + item) paths.

    Examples:
        'I.a'      -> ['I.a', 'IA']
        'II.c'     -> ['II.c', 'IIC']
        '§1.II.a'  -> ['§1.II.a', '§1.IIA']
        'I.a.1'    -> ['I.a.1', 'IA1']
        'caput'    -> ['caput']        (no expansion)
        'IV'       -> ['IV']           (no expansion — pure Roman)
    """
    if not path:
        return [path]

    candidates = [path]
    parts = path.split(".")

    # Pattern: <Roman>.<lowercase letter> -> add <Roman><UPPER>
    if len(parts) == 2 and _is_roman_run(parts[0]) and len(parts[1]) == 1 and parts[1].islower():
        candidates.append(f"{parts[0]}{parts[1].upper()}")

    # Pattern: §N.<Roman>.<lowercase letter> -> add §N.<Roman><UPPER>
    elif (
        len(parts) == 3
        and parts[0].startswith("§")
        and _is_roman_run(parts[1])
        and len(parts[2]) == 1
        and parts[2].islower()
    ):
        candidates.append(f"{parts[0]}.{parts[1]}{parts[2].upper()}")

    # Pattern: <Roman>.<lowercase letter>.<digit> -> add <Roman><UPPER><digit>
    elif (
        len(parts) == 3
        and _is_roman_run(parts[0])
        and len(parts[1]) == 1
        and parts[1].islower()
        and parts[2].isdigit()
    ):
        candidates.append(f"{parts[0]}{parts[1].upper()}{parts[2]}")

    # Pattern: §N.<Roman>.<lowercase letter>.<digit> -> add §N.<Roman><UPPER><digit>
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


@dataclass
class Citation:
    """A parsed citation. All fields except `identifier` may be None."""

    identifier: str
    artigo: Optional[int] = None
    letra: Optional[str] = None
    path: Optional[str] = None
    date: Optional[str] = None  # @YYYY-MM-DD
    from_id: Optional[str] = None  # from:X
    vintage: Optional[str] = None  # :original or :current
    raw: Optional[str] = None  # original bracket string
    is_case: bool = False  # True for jurisprudence citations like `Tema1199`
    is_sv: bool = False  # True for `SV14` STF súmula vinculante citations
    is_stse: bool = False  # True for `STSE38` TSE súmula citations

    @property
    def is_whole_law(self) -> bool:
        return (
            self.artigo is None
            and self.path is None
            and not self.is_case
            and not self.is_sv
            and not self.is_stse
        )

    def to_lookup_args(self) -> List[str]:
        """Return the equivalent lookup.py CLI arguments for this citation."""
        args = [self.identifier]
        if self.artigo is not None:
            arg = str(self.artigo)
            if self.letra:
                arg += f"-{self.letra}"
            args.append(arg)
        if self.path:
            args += ["--path", self.path]
        if self.date:
            args += ["--as-of", self.date]
        if self.from_id:
            args += ["--from", self.from_id]
        return args

    def __str__(self) -> str:
        if self.is_case or self.is_sv or self.is_stse:
            return f"`{self.identifier}`"
        s = self.identifier
        if self.artigo is not None:
            s += f".{self.artigo}"
            if self.letra:
                s += f"-{self.letra}"
        if self.path:
            s += f".{self.path}"
        if self.date:
            s += f"@{self.date}"
        if self.from_id:
            s += f" from:{self.from_id}"
        if self.vintage:
            s += f":{self.vintage}"
        return f"`{s}`"


def parse(citation: str) -> Citation:
    """Parse a single citation string (with or without surrounding backticks).

    Raises ValueError if the citation cannot be parsed.
    """
    raw = citation
    body = citation.strip()
    # Strip a single pair of surrounding backticks if present
    if len(body) >= 2 and body.startswith("`") and body.endswith("`"):
        body = body[1:-1].strip()
    # Backward compatibility: also accept the old [[ ]] form
    elif body.startswith("[[") and body.endswith("]]"):
        body = body[2:-2].strip()

    # TSE Súmula? (`STSE38`, `STSE47`, ...) — checked before SV so the
    # longer prefix wins.
    if STSE_RE.match(body):
        return Citation(identifier=body, is_stse=True, raw=raw)

    # Súmula Vinculante? (`SV14`, `SV37`, ...) — checked before case
    # grammar so SV-prefixed identifiers are not misread.
    if SV_RE.match(body):
        return Citation(identifier=body, is_sv=True, raw=raw)

    # Case citation? (Tema1199, ADI4650, HC126292, LulaMoro2021, ...)
    # Checked first because case prefixes like RE, ADI overlap syntactically
    # with the law identifier grammar.
    if CASE_ID_RE.match(body):
        return Citation(identifier=body, is_case=True, raw=raw)

    # Try whole-law form first
    m = WHOLE_LAW_RE.match(body)
    if m:
        return Citation(identifier=m["identifier"], raw=raw)

    # Try identifier.path form (ementa/preambulo without article)
    m = LAW_WITH_PATH_RE.match(body)
    if m:
        return Citation(
            identifier=m["identifier"],
            path=m["path"],
            date=m["date"],
            from_id=m["from_id"],
            vintage=m["vintage"],
            raw=raw,
        )

    # Try article-level form
    m = ARTICLE_RE.match(body)
    if m:
        return Citation(
            identifier=m["identifier"],
            artigo=int(m["artigo"]),
            letra=m["letra"],
            path=m["path"],
            date=m["date"],
            from_id=m["from_id"],
            vintage=m["vintage"],
            raw=raw,
        )

    raise ValueError(f"Cannot parse citation: {citation!r}")


def find_citations(text: str) -> List[Citation]:
    """Find all backtick-form citations in a markdown/text body.

    Captures every inline-code span, attempts to parse each, and keeps
    only those that successfully resolve to a Citation. Non-citation
    inline code (function names, file paths, etc.) is silently skipped.
    """
    out: List[Citation] = []
    for match in BRACKET_RE.finditer(text):
        try:
            out.append(parse(match.group(1)))
        except ValueError:
            # Not a citation we can parse — skip silently. Most inline
            # code in these files is not a citation.
            continue
    return out


# ---------------------------------------------------------------------------
# Jurisprudência index loader
# ---------------------------------------------------------------------------
_juris_cache: Optional[dict] = None


def load_juris_index(path: Optional[Path] = None) -> dict:
    """Load and cache jurisprudencia_index.yaml.

    Returns a dict with keys 'cases' (the raw mapping) and '_alias_map'
    (resolved alias → canonical key). On missing file, returns empty
    structures rather than raising — case parsing still works, lookups
    just return None.
    """
    global _juris_cache
    if _juris_cache is not None:
        return _juris_cache
    if path is None:
        path = DEFAULT_JURIS_INDEX
    if not path.exists():
        _juris_cache = {"cases": {}, "_alias_map": {}}
        return _juris_cache

    try:
        import yaml  # PyYAML; optional dependency
    except ImportError:
        _juris_cache = {"cases": {}, "_alias_map": {}}
        return _juris_cache

    data = yaml.safe_load(path.read_text()) or {}
    cases = data.get("cases", {}) or {}
    alias_map: dict = {}
    for key, entry in cases.items():
        alias_map[key] = key
        for alias in (entry or {}).get("aliases", []) or []:
            alias_map[alias] = key
    _juris_cache = {"cases": cases, "_alias_map": alias_map}
    return _juris_cache


def lookup_case(identifier: str, index_path: Optional[Path] = None) -> Optional[dict]:
    """Look up a case by canonical key or alias. Returns the entry merged
    with its canonical id under 'id', or None if not found."""
    idx = load_juris_index(index_path)
    key = idx["_alias_map"].get(identifier)
    if key is None:
        return None
    entry = idx["cases"].get(key)
    if entry is None:
        return None
    return {"id": key, **entry}


# ---------------------------------------------------------------------------
# Súmulas Vinculantes index loader
# ---------------------------------------------------------------------------
_sv_cache: Optional[dict] = None


def load_sv_index(path: Optional[Path] = None) -> dict:
    """Load and cache sumulas_vinculantes.yaml. Empty on missing file."""
    global _sv_cache
    if _sv_cache is not None:
        return _sv_cache
    if path is None:
        path = DEFAULT_SV_INDEX
    if not path.exists():
        _sv_cache = {"sumulas": {}}
        return _sv_cache
    try:
        import yaml
    except ImportError:
        _sv_cache = {"sumulas": {}}
        return _sv_cache
    data = yaml.safe_load(path.read_text()) or {}
    _sv_cache = {"sumulas": data.get("sumulas", {}) or {}}
    return _sv_cache


def lookup_sv(identifier: str, index_path: Optional[Path] = None) -> Optional[dict]:
    """Look up a SV by canonical key (e.g., 'SV14'). Returns the entry merged
    with its id, or None if not found."""
    idx = load_sv_index(index_path)
    entry = idx["sumulas"].get(identifier)
    if entry is None:
        return None
    return {"id": identifier, **entry}


# ---------------------------------------------------------------------------
# TSE Súmulas index loader
# ---------------------------------------------------------------------------
_stse_cache: Optional[dict] = None


def load_stse_index(path: Optional[Path] = None) -> dict:
    """Load and cache sumulas_tse.yaml. Empty on missing file."""
    global _stse_cache
    if _stse_cache is not None:
        return _stse_cache
    if path is None:
        path = DEFAULT_STSE_INDEX
    if not path.exists():
        _stse_cache = {"sumulas": {}}
        return _stse_cache
    try:
        import yaml
    except ImportError:
        _stse_cache = {"sumulas": {}}
        return _stse_cache
    data = yaml.safe_load(path.read_text()) or {}
    _stse_cache = {"sumulas": data.get("sumulas", {}) or {}}
    return _stse_cache


def lookup_stse(identifier: str, index_path: Optional[Path] = None) -> Optional[dict]:
    """Look up a TSE súmula by canonical key (e.g., 'STSE38'). Returns the
    entry merged with its id, or None if not found."""
    idx = load_stse_index(index_path)
    entry = idx["sumulas"].get(identifier)
    if entry is None:
        return None
    return {"id": identifier, **entry}


# ---------------------------------------------------------------------------
# SQL resolver
# ---------------------------------------------------------------------------
def resolve(
    citation: Citation,
    db_path: Optional[Path] = None,
) -> List[sqlite3.Row]:
    """Run the SQL query for a parsed citation against artigos.db.

    Returns a list of sqlite3.Row objects from the artigo table. Empty list
    if no rows match. Raises FileNotFoundError if the DB isn't available.
    """
    if db_path is None:
        db_path = DEFAULT_DB
    if not db_path.exists():
        raise FileNotFoundError(
            f"artigos.db not found at {db_path}. "
            f"Set CITE_DB env var or pass --db.\n"
            f"Citation parsed OK: {citation}"
        )

    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row

    # EC citations (EC45-2004, EC97-2017, ...) resolve to the CF articles
    # that the emenda constitucional introduced or rewrote, identified by
    # matching fonte_id in the CF rows.
    ec_match = re.match(r'^EC\d+-\d{4}$', citation.identifier)
    if ec_match and citation.is_whole_law:
        sql = ("SELECT * FROM artigo WHERE apelido = 'CF'"
               " AND fonte_id = ? AND vigente_ate IS NULL"
               " ORDER BY ordem ASC")
        rows = con.execute(sql, [citation.identifier]).fetchall()
        con.close()
        return rows

    sql = "SELECT * FROM artigo WHERE apelido = ?"
    args: List = [citation.identifier]

    if citation.artigo is not None:
        sql += " AND artigo = ?"
        args.append(citation.artigo)
    if citation.letra:
        sql += " AND artigo_letra = ?"
        args.append(citation.letra)
    elif citation.artigo is not None:
        sql += " AND (artigo_letra IS NULL OR artigo_letra = '')"

    if citation.path:
        candidates = normalize_path_candidates(citation.path)
        if len(candidates) == 1:
            sql += " AND path = ?"
            args.append(candidates[0])
        else:
            placeholders = ",".join("?" * len(candidates))
            sql += f" AND path IN ({placeholders})"
            args.extend(candidates)

    # Vintage filter
    if citation.date:
        sql += (
            " AND vigente_desde <= ?"
            " AND (vigente_ate IS NULL OR ? < vigente_ate)"
        )
        args += [citation.date, citation.date]
        sql += " ORDER BY ordem ASC"
    elif citation.from_id:
        sql += " AND fonte_id = ?"
        args.append(citation.from_id)
        sql += " ORDER BY ordem ASC"
    elif citation.vintage == "original":
        # Sort by earliest vigente_desde so the first row per (artigo, path)
        # is the original-publication version. The post-query dedup keeps
        # one row per location.
        sql += " ORDER BY ordem ASC, vigente_desde ASC"
    else:
        # Default: current version
        sql += " AND vigente_ate IS NULL"
        sql += " ORDER BY ordem ASC"

    rows = con.execute(sql, args).fetchall()

    # If :original requested, keep only the first row per (artigo, path)
    if citation.vintage == "original" and rows:
        seen = set()
        unique = []
        for r in rows:
            k = (r["artigo"], r["artigo_letra"], r["path"])
            if k not in seen:
                seen.add(k)
                unique.append(r)
        rows = unique

    con.close()
    return rows


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def _print_sumula(entry: dict, label: str, full: bool = False) -> None:
    """Print a súmula index entry (SV or STSE) to stdout.

    `label` is the human-readable header (e.g., "Súmula Vinculante 14",
    "Súmula TSE 38"). The structure is the same across courts.
    """
    sid = entry.get("id", "?")
    status = entry.get("status", "")
    enunciado = entry.get("enunciado") or ""

    print(f"--- `{sid}`  {label}")
    print(f"  status:    {status}")
    if entry.get("publicacao"):
        print(f"  publicada: {entry['publicacao']}")
    print()
    print(enunciado)
    if full and entry.get("fonte"):
        print()
        print(f"  fonte: {entry['fonte']}")
    print()


def _print_sv(entry: dict, full: bool = False) -> None:
    _print_sumula(entry, f"Súmula Vinculante {entry.get('numero', '?')}", full=full)


def _print_stse(entry: dict, full: bool = False) -> None:
    _print_sumula(entry, f"Súmula TSE {entry.get('numero', '?')}", full=full)


def _print_case(entry: dict, full: bool = False) -> None:
    """Print a jurisprudência index entry to stdout."""
    cid = entry.get("id", "?")
    tipo = entry.get("tipo", "")
    processo = entry.get("processo") or ", ".join(entry.get("processos", []) or [])
    decidido = entry.get("decidido", "")
    status = entry.get("status", "")
    tema = entry.get("tema", "")

    print(f"--- `{cid}`  {tipo} {processo}".rstrip())
    if tema:
        print(f"  tema:     {tema}")
    if decidido:
        print(f"  decidido: {decidido}")
    print(f"  status:   {status}")

    holding = entry.get("holding_short")
    if holding:
        # Collapse YAML folded scalar whitespace for clean stdout.
        text = " ".join(holding.split())
        print(f"  holding:  {text}")

    if full:
        for k in ("relator", "votacao", "tese_certificada"):
            if entry.get(k):
                print(f"  {k}: {entry[k]}")
        if entry.get("supera"):
            print(f"  supera:       {', '.join(entry['supera'])}")
        if entry.get("superado_por"):
            print(f"  superado_por: {entry['superado_por']}")
        if entry.get("complementa"):
            print(f"  complementa:  {', '.join(entry['complementa'])}")
        if entry.get("complementado_por"):
            print(f"  complementado_por: {', '.join(entry['complementado_por'])}")
        if entry.get("discussed_in"):
            print(f"  discussed_in: {', '.join(entry['discussed_in'])}")
        if entry.get("related_leis"):
            print(f"  related_leis: {', '.join(entry['related_leis'])}")
        if entry.get("fonte"):
            print(f"  fonte:    {entry['fonte']}")
    print()


def _print_row(row: sqlite3.Row, full: bool = False) -> None:
    artigo_label = f"Art. {row['artigo']}"
    if row["artigo_letra"]:
        artigo_label += f"-{row['artigo_letra']}"
    path = row["path"] or ""

    print(f"--- {row['apelido']} {artigo_label} {path}")
    if full:
        if row["capitulo"]:
            print(f"  Capítulo: {row['capitulo']} {row['capitulo_titulo'] or ''}")
        if row["secao"]:
            print(f"  Seção:    {row['secao']} {row['secao_titulo'] or ''}")
        print(f"  fonte:    {row['fonte'] or '—'}")
        print(f"  desde:    {row['vigente_desde'] or '—'}")
        print(f"  até:      {row['vigente_ate'] or '(in force)'}")
    print(row["texto"] or "")
    print()


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Resolve a compact backtick-form citation against artigos.db.",
        epilog=(
            "Examples (statute):\n"
            "  cite.py 'LIA.9'\n"
            "  cite.py 'LIA.10.§1.II'\n"
            "  cite.py 'LIA.11.§unico@2020-06-01'\n"
            "  cite.py 'LIA.10 from:L14230-2021'\n"
            "  cite.py --parse-only 'LE.17-A.caput'\n"
            "\n"
            "Examples (jurisprudence):\n"
            "  cite.py 'Tema1199'\n"
            "  cite.py 'ADI4650' --full\n"
            "  cite.py 'HC126292'              # superada — see superado_por\n"
            "\n"
            "Examples (súmula vinculante):\n"
            "  cite.py 'SV14'                  # acesso amplo da defesa\n"
            "  cite.py 'SV13'                  # nepotismo\n"
            "  cite.py 'SV9' --full            # cancelada\n"
            "\n"
            "Examples (súmula TSE):\n"
            "  cite.py 'STSE38'                # litisconsórcio passivo majoritário\n"
            "  cite.py 'STSE47'                # inelegibilidade superveniente\n"
            "  cite.py 'STSE1'                 # cancelada\n"
            "\n"
            "  cite.py --find-in path/to/file.md\n"
            "\n"
            "Backticks around the citation are accepted but not required\n"
            "from the shell. Inside markdown, citations are wrapped in\n"
            "single backticks (e.g., `LIA.9`) so they render as inline\n"
            "code on github.com.\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("citation", nargs="?", help="Citation, with or without surrounding backticks.")
    ap.add_argument("--db", type=Path, default=None, help=f"Path to artigos.db (default: {DEFAULT_DB})")
    ap.add_argument("--parse-only", action="store_true", help="Parse but don't query the DB.")
    ap.add_argument("--full", action="store_true", help="Show capítulo/seção/fonte metadata.")
    ap.add_argument("--find-in", metavar="FILE", help="Find and parse all citations in a file.")

    args = ap.parse_args()

    if args.find_in:
        text = Path(args.find_in).read_text()
        cites = find_citations(text)
        if not cites:
            print(f"No citations found in {args.find_in}")
            return 0
        for c in cites:
            print(c)
        return 0

    if not args.citation:
        ap.print_help()
        return 1

    try:
        c = parse(args.citation)
    except ValueError as e:
        print(f"Parse error: {e}", file=sys.stderr)
        return 1

    if args.parse_only:
        print(f"Parsed: {c}")
        print(f"  identifier: {c.identifier}")
        print(f"  is_case:    {c.is_case}")
        print(f"  is_sv:      {c.is_sv}")
        print(f"  is_stse:    {c.is_stse}")
        if not c.is_case and not c.is_sv and not c.is_stse:
            print(f"  artigo:     {c.artigo}")
            print(f"  letra:      {c.letra}")
            print(f"  path:       {c.path}")
            print(f"  date:       {c.date}")
            print(f"  from_id:    {c.from_id}")
            print(f"  vintage:    {c.vintage}")
            print(f"  lookup args: {' '.join(c.to_lookup_args())}")
        return 0

    # Súmula Vinculante: resolve against the SV YAML
    if c.is_sv:
        entry = lookup_sv(c.identifier)
        if entry is None:
            print(
                f"No SV match for {c} in {DEFAULT_SV_INDEX}",
                file=sys.stderr,
            )
            return 3
        _print_sv(entry, full=args.full)
        return 0

    # TSE Súmula: resolve against the STSE YAML
    if c.is_stse:
        entry = lookup_stse(c.identifier)
        if entry is None:
            print(
                f"No TSE súmula match for {c} in {DEFAULT_STSE_INDEX}",
                file=sys.stderr,
            )
            return 3
        _print_stse(entry, full=args.full)
        return 0

    # Jurisprudence citation: resolve against the YAML index
    if c.is_case:
        entry = lookup_case(c.identifier)
        if entry is None:
            print(
                f"No case match for {c} in {DEFAULT_JURIS_INDEX}",
                file=sys.stderr,
            )
            return 3
        _print_case(entry, full=args.full)
        return 0

    # Statute citation: resolve against artigos.db
    try:
        rows = resolve(c, args.db)
    except FileNotFoundError as e:
        print(str(e), file=sys.stderr)
        return 2

    if not rows:
        print(f"No rows match {c}", file=sys.stderr)
        return 3

    for row in rows:
        _print_row(row, full=args.full)
    return 0


if __name__ == "__main__":
    sys.exit(main())
