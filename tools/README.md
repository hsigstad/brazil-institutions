# tools/

Code that complements the markdown reference. The tools here are
optional — the prose reference works fine without them — but they
make the reference much more useful when you need exact statutory
text or want to resolve a citation programmatically.

## Subdirectories

### `leis_artigos/` — article-level law database

Parses planalto.gov.br consolidated HTML into a structured SQLite
table where each row is one **leaf** of an article (caput,
parágrafo, inciso, alínea, item) with its current text, amendment
history, and date-versioned tracking.

Currently catalogs 37 federal laws (as of 2026), including LIA,
L8666, L14133, LE, CC, CPC, CPP, CE, LRF, LFL, LAI, LGPD, LAC, LCO,
LP, LPP, and many others. See `leis_artigos/README.md` for the full
catalog and lookup instructions.

**Key files:**

- `cite.py` — resolves compact bracket-form citations
  (`[[LIA.10.§1.II]]`) directly to article rows. The bridge between
  the prose reference (`../*.md`) and the database.
- `lookup.py` — CLI for querying the article DB by apelido + article
  + path, with date-versioned and source-versioned options.
- `build.py` — rebuilds `artigos.db` from the planalto raw scrape.
  Maintainer-only; needs `planalto_legislacao.db`.
- `parser.py` — parses planalto consolidated HTML into structured
  leaves. Used by `build.py`.
- `amendments_parser.py`, `build_amendments.py`,
  `find_amending.py` — populate the `amendment` table tracking which
  amending lei touched which clause.
- `overrides/` — manual corrections for planalto HTML bugs.
- `PATH_CONVENTION.md` — strict grammar for the `path` column.

### `planalto_scraper/` — raw planalto.gov.br scraper

Downloads federal legislation from planalto.gov.br into
`planalto_legislacao.db` (a SQLite mirror). The article DB
(`leis_artigos/`) is built from this. Maintainer-only; the
prebuilt `artigos.db` is shipped via Dropbox so most users
don't need to scrape.

## Running the tools

The article DB lives outside the repo by convention:

```
~/research/data/planalto/planalto_legislacao.db   # raw planalto scrape
~/research/data/lei/artigos.db                    # parsed article-level DB
```

Override with environment variables:

```bash
export PLANALTO_DB=/path/to/planalto_legislacao.db
export ARTIGOS_DB=/path/to/artigos.db
```

Or pass `--db` / `--artigos-db` / `--planalto-db` on the CLI.

## Two paths for users

**End user** (you have the institutions reference and want to look
up exact text):

1. Download `artigos.db` from the Dropbox link in
   `leis_artigos/README.md` and place at `~/research/data/lei/artigos.db`.
2. Use `lookup.py` or `cite.py` to query.
3. You do **not** need `planalto_scraper/` or `build.py`.

**Maintainer** (you want to add laws to the catalog or fix parser
bugs):

1. Run `planalto_scraper/scraper.py` to build the raw planalto
   mirror (slow; ~57k laws; only needed once).
2. Edit the `LAW_CATALOG` in `leis_artigos/build.py` to add new
   apelidos.
3. Run `leis_artigos/build.py` to rebuild `artigos.db`.
4. Run `leis_artigos/build_amendments.py` to populate the
   `amendment` table.

## Why these tools live in this repo

The institutions reference cites statutes inline using the compact
bracket form `[[apelido.artigo.path]]` (see `../CLAUDE.md`). To make
those citations resolvable, the schema and lookup tooling must be
discoverable from the same place. Shipping the code here keeps the
contract local: the format used in the prose is the format the tools
parse.

The actual database files (`artigos.db`, `planalto_legislacao.db`)
do **not** live in this repo — they're build artifacts, distributed
separately via Dropbox.
