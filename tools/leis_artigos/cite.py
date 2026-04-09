#!/usr/bin/env python3
"""cite.py — resolve compact bracket-form citations to artigo rows.

Parses a citation string like '[[LIA.10.§1.II]]' or
'[[LE.11.§10@2024-12-31]]' into structured fields and runs the
corresponding query against artigos.db. This is the bridge between
prose citations in the institutions reference and the article-level
law database.

The bracket form is documented in ../../CLAUDE.md (section 'Citing
statutes'). Path syntax follows PATH_CONVENTION.md.

The resolver returns rows from artigos.db directly. If the database
isn't available locally, the parser still works — callers can use the
parsed Citation object to format a fallback (e.g., a planalto link).
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
# Citation grammar
# ---------------------------------------------------------------------------
# Bracket form: [[<identifier>[.<artigo>[-<letra>]][.<path>][<modifier>]]]
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
#   [[LIA]]              -> whole law (no article)
#   [[LIA.ementa]]       -> the law's ementa (path-only, no article)
#   [[L14230-2021]]      -> non-cataloged amending law as an entity

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

# Whole-law-with-ementa: e.g., [[LIA.ementa]]
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

# Citation enclosed in [[ ]] (for find_citations)
BRACKET_RE = re.compile(r"\[\[([^\[\]]+?)\]\]")


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

    @property
    def is_whole_law(self) -> bool:
        return self.artigo is None and self.path is None

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
        return f"[[{s}]]"


def parse(citation: str) -> Citation:
    """Parse a single citation string (with or without surrounding [[ ]]).

    Raises ValueError if the citation cannot be parsed.
    """
    raw = citation
    body = citation.strip()
    if body.startswith("[[") and body.endswith("]]"):
        body = body[2:-2].strip()

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
    """Find all bracket-form citations in a markdown/text body."""
    out: List[Citation] = []
    for match in BRACKET_RE.finditer(text):
        try:
            out.append(parse(f"[[{match.group(1)}]]"))
        except ValueError:
            # Not a citation we can parse — skip silently. Could log.
            continue
    return out


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
        sql += " AND path = ?"
        args.append(citation.path)

    # Vintage filter
    if citation.date:
        sql += (
            " AND vigente_desde <= ?"
            " AND (vigente_ate IS NULL OR ? < vigente_ate)"
        )
        args += [citation.date, citation.date]
    elif citation.from_id:
        sql += " AND fonte_id = ?"
        args.append(citation.from_id)
    elif citation.vintage == "original":
        sql += " ORDER BY vigente_desde ASC"
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
        description="Resolve a compact bracket-form citation against artigos.db.",
        epilog=(
            "Examples:\n"
            "  cite.py '[[LIA.9]]'\n"
            "  cite.py '[[LIA.10.§1.II]]'\n"
            "  cite.py '[[LIA.11.§unico@2020-06-01]]'\n"
            "  cite.py '[[LIA.10 from:L14230-2021]]'\n"
            "  cite.py --parse-only '[[LE.17-A.caput]]'\n"
            "  cite.py --find-in path/to/file.md\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("citation", nargs="?", help="Bracket-form citation, with or without [[ ]].")
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
        print(f"  artigo:     {c.artigo}")
        print(f"  letra:      {c.letra}")
        print(f"  path:       {c.path}")
        print(f"  date:       {c.date}")
        print(f"  from_id:    {c.from_id}")
        print(f"  vintage:    {c.vintage}")
        print(f"  lookup args: {' '.join(c.to_lookup_args())}")
        return 0

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
