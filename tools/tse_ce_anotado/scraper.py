#!/usr/bin/env python3
"""
TSE Código Eleitoral Anotado scraper.

Fetches the annotated Electoral Code from the TSE website and builds
a SQLite database mapping each article to its TSE jurisprudence
annotations (acórdãos, resoluções, CF cross-references, etc.).

# INTENT
# Produce ce_anotado.db so that cite.py can optionally show
# jurisprudence annotations alongside article text when looking up
# CE articles.
#
# REASONING
# The TSE publishes the only freely available article-by-article
# annotated legislation in Brazil. The HTML structure is clean:
# article text in <p class="texto-corrido">, annotations in
# <li class="marcador-quadrado"> or <ul class="marcadorTicado"><li>.
#
# Stdlib only (urllib + re + html + sqlite3). No requests/bs4.

Usage:
    python3 scraper.py fetch        # download the annotated CE page
    python3 scraper.py build        # parse cached HTML -> SQLite
    python3 scraper.py all          # fetch + build
    python3 scraper.py --help

Cache:
    ~/research/data/tse_ce_anotado/         (override with CE_CACHE)
    └── ce_anotado.html

Output:
    <script_dir>/ce_anotado.db              (override with CE_DB)
"""

from __future__ import annotations

import argparse
import logging
import os
import re
import sqlite3
import ssl
import sys
import time
import urllib.request
from pathlib import Path
from typing import List, Optional, Tuple

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

CE_URL = (
    "https://www.tse.jus.br/legislacao/codigo-eleitoral/"
    "codigo-eleitoral-1/"
    "codigo-eleitoral-lei-nb0-4.737-de-15-de-julho-de-1965"
)

DEFAULT_CACHE = Path.home() / "research" / "data" / "tse_ce_anotado"
DEFAULT_DB = Path(__file__).resolve().parent / "ce_anotado.db"

log = logging.getLogger("tse_ce_anotado")

# ---------------------------------------------------------------------------
# Fetch
# ---------------------------------------------------------------------------


def fetch(cache_dir: Path) -> Path:
    """Download the annotated CE HTML page to cache."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    out = cache_dir / "ce_anotado.html"

    if out.exists():
        age_h = (time.time() - out.stat().st_mtime) / 3600
        if age_h < 24 * 7:
            log.info("Using cached %s (%.1f hours old)", out, age_h)
            return out
        log.info("Cache stale (%.1f hours), re-fetching", age_h)

    log.info("Fetching %s", CE_URL)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(
        CE_URL,
        headers={"User-Agent": "brazil-institutions-scraper/1.0"},
    )
    with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
        data = resp.read()

    out.write_bytes(data)
    log.info("Saved %d bytes to %s", len(data), out)
    return out


# ---------------------------------------------------------------------------
# Parse
# ---------------------------------------------------------------------------


def classify_reference(text: str) -> Tuple[str, Optional[str]]:
    """Classify an annotation into (tipo, referencia).

    Returns:
        tipo: 'acordao_tse', 'acordao_stf', 'acordao_stj', 'acordao',
              'resolucao_tse', 'resolucao_cnj', 'cf', 'lei', 'lc',
              'decreto', 'sumula', 'other'
        referencia: extracted citation key or None
    """
    t = text.strip()

    # Acórdãos — match "Ac.-TSE" anywhere, extract whatever ID follows
    if re.search(r"Ac\.-TSE", t):
        m = re.search(r"Ac\.-TSE[^,;]*?n[ºo°.]?\s*([\d.]+(?:/\d{4})?)", t)
        ref = f"Ac.-TSE {m.group(1)}" if m else None
        return "acordao_tse", ref

    if re.search(r"Ac\.-STF", t):
        m = re.search(r"Ac\.-STF[^,;]*?n[ºo°.]?\s*([\d.]+(?:/\d{4})?)", t)
        ref = f"Ac.-STF {m.group(1)}" if m else None
        return "acordao_stf", ref

    if re.search(r"Ac\.-STJ", t):
        m = re.search(r"Ac\.-STJ[^,;]*?n[ºo°.]?\s*([\d.]+(?:/\d{4})?)", t)
        ref = f"Ac.-STJ {m.group(1)}" if m else None
        return "acordao_stj", ref

    # Resoluções — match anywhere
    if re.search(r"Res\.-TSE", t):
        m = re.search(r"Res\.-TSE\s*n[ºo°.]?\s*([\d.]+(?:/\d{4})?)", t)
        ref = f"Res.-TSE {m.group(1)}" if m else None
        return "resolucao_tse", ref

    if re.search(r"Res\.-CNJ", t):
        m = re.search(r"Res\.-CNJ\s*n[ºo°.]?\s*([\d.]+(?:/\d{4})?)", t)
        ref = f"Res.-CNJ {m.group(1)}" if m else None
        return "resolucao_cnj", ref

    if re.match(r"Res\.", t):
        return "resolucao_tse", None

    # CF cross-reference
    if re.match(r"CF/1988", t) or re.match(r"V\.\s.*CF/1988", t):
        return "cf", None

    # Súmulas
    if re.search(r"S[uú]mula", t, re.IGNORECASE):
        return "sumula", None

    # Amendment history notes
    if re.match(r"(Caput|Inciso|Alínea|Parágrafo|Artigo)\s", t):
        return "redacao", None

    # "Dec. monocrática" — monocratic decision
    if re.match(r"Dec\.\s*monocrática", t):
        return "acordao_tse", None

    # LC
    if re.match(r"LC\s", t):
        return "lc", None

    # Lei
    if re.match(r"Lei\s", t):
        return "lei", None

    # Decreto
    if re.match(r"Decreto", t):
        return "decreto", None

    # V. (see / cross-reference to other articles)
    if re.match(r"V\.\s", t):
        return "ver", None

    return "other", None


def parse_annotations(html: str) -> List[dict]:
    """Parse the annotated CE HTML into a list of annotation dicts."""
    # Find main content — starts at Art. 1
    content_start = html.find("Art. 1")
    if content_start < 0:
        raise ValueError("Could not find 'Art. 1' in HTML")
    content = html[content_start:]

    # Split by article markers
    art_pattern = re.compile(r"(?=Art\.\s*(\d+[-A-Z]*)[º.])")
    splits = list(art_pattern.finditer(content))

    if not splits:
        raise ValueError("No article markers found")

    log.info("Found %d article markers", len(splits))

    rows = []
    seen_articles = set()

    for i, m in enumerate(splits):
        art_num = m.group(1)
        start = m.start()
        end = splits[i + 1].start() if i + 1 < len(splits) else len(content)
        section = content[start:end]

        # Extract annotations from both marker styles
        annots_sq = re.findall(
            r'<li[^>]*class="marcador-quadrado"[^>]*>(.*?)</li>',
            section,
            re.DOTALL,
        )
        annots_ck = re.findall(
            r'<ul class="marcadorTicado"><li>(.*?)</li>',
            section,
            re.DOTALL,
        )
        # Also catch marcadorTicado with class on the li
        annots_ck2 = re.findall(
            r'<li[^>]*class="[^"]*marcadorTicado[^"]*"[^>]*>(.*?)</li>',
            section,
            re.DOTALL,
        )

        all_annots = annots_sq + annots_ck + annots_ck2

        for raw_html in all_annots:
            # Strip HTML tags
            text = re.sub(r"<[^>]+>", "", raw_html).strip()
            text = re.sub(r"\s+", " ", text)

            if not text or len(text) < 5:
                continue

            tipo, referencia = classify_reference(text)

            rows.append(
                {
                    "lei": "CE",
                    "artigo": int(re.match(r"\d+", art_num).group()),
                    "artigo_letra": art_num if not art_num.isdigit() else None,
                    "tipo": tipo,
                    "referencia": referencia,
                    "texto": text,
                }
            )

        if all_annots:
            seen_articles.add(art_num)

    log.info(
        "Parsed %d annotations across %d articles",
        len(rows),
        len(seen_articles),
    )
    return rows


# ---------------------------------------------------------------------------
# Build DB
# ---------------------------------------------------------------------------

SCHEMA = """\
CREATE TABLE IF NOT EXISTS anotacao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lei TEXT NOT NULL DEFAULT 'CE',
    artigo INTEGER NOT NULL,
    artigo_letra TEXT,
    tipo TEXT NOT NULL,
    referencia TEXT,
    texto TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_anotacao_artigo ON anotacao(lei, artigo);
CREATE INDEX IF NOT EXISTS idx_anotacao_tipo ON anotacao(tipo);
"""


def build_db(rows: List[dict], db_path: Path) -> None:
    """Write parsed annotations to SQLite."""
    if db_path.exists():
        db_path.unlink()

    con = sqlite3.connect(str(db_path))
    con.executescript(SCHEMA)

    con.executemany(
        "INSERT INTO anotacao (lei, artigo, artigo_letra, tipo, referencia, texto) "
        "VALUES (:lei, :artigo, :artigo_letra, :tipo, :referencia, :texto)",
        rows,
    )
    con.commit()

    count = con.execute("SELECT COUNT(*) FROM anotacao").fetchone()[0]
    arts = con.execute(
        "SELECT COUNT(DISTINCT artigo) FROM anotacao"
    ).fetchone()[0]
    tipos = con.execute(
        "SELECT tipo, COUNT(*) FROM anotacao GROUP BY tipo ORDER BY COUNT(*) DESC"
    ).fetchall()

    con.close()

    log.info("Wrote %d annotations for %d articles to %s", count, arts, db_path)
    log.info("By type:")
    for tipo, cnt in tipos:
        log.info("  %-20s %d", tipo, cnt)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    ap = argparse.ArgumentParser(
        description="Scrape TSE Código Eleitoral Anotado into SQLite.",
    )
    ap.add_argument(
        "command",
        choices=["fetch", "build", "all"],
        help="fetch = download HTML; build = parse -> DB; all = both",
    )
    ap.add_argument(
        "--cache",
        type=Path,
        default=Path(os.environ.get("CE_CACHE", str(DEFAULT_CACHE))),
        help=f"Cache directory (default: {DEFAULT_CACHE})",
    )
    ap.add_argument(
        "--db",
        type=Path,
        default=Path(os.environ.get("CE_DB", str(DEFAULT_DB))),
        help=f"Output DB path (default: {DEFAULT_DB})",
    )
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    if args.command in ("fetch", "all"):
        html_path = fetch(args.cache)

    if args.command in ("build", "all"):
        if args.command == "build":
            html_path = args.cache / "ce_anotado.html"
            if not html_path.exists():
                log.error("No cached HTML at %s — run 'fetch' first", html_path)
                return 1

        html = html_path.read_text(encoding="utf-8", errors="replace")
        rows = parse_annotations(html)
        build_db(rows, args.db)

    return 0


if __name__ == "__main__":
    sys.exit(main())
