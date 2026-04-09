# planalto_scraper — raw planalto.gov.br legislation scraper

Downloads federal legislation from planalto.gov.br into a SQLite
database for querying. The output is then consumed by
`../leis_artigos/` to build the article-level database.

This is a maintainer tool. End users who just want to query existing
parsed laws should use `../leis_artigos/` and download the prebuilt
`artigos.db` from Dropbox — see `../leis_artigos/README.md`.

## What it does

- Discovers and downloads consolidated HTML for all federal laws,
  leis complementares, decretos, decretos-lei, emendas
  constitucionais, medidas provisórias, etc., from
  <https://www.planalto.gov.br>.
- Extracts metadata (tipo, número, data, ementa) and the full
  rendered text.
- Stores everything in a single SQLite file (`planalto_legislacao.db`)
  with FTS5 full-text search over the law text.
- Polite by default: 0.5s delay between requests, retries on transient
  errors, resumable.
- Idempotent: re-running won't re-download already-fetched laws unless
  forced.

## Database

**Default location**: `~/research/data/planalto/planalto_legislacao.db`

Override with the `PLANALTO_DB` environment variable.

### Schema

```
legislacao
├── id              INTEGER PRIMARY KEY
├── url             TEXT       (planalto canonical URL)
├── tipo            TEXT       (Lei, Lei Complementar, Decreto, ...)
├── numero          TEXT
├── data            TEXT       (publication date)
├── ementa          TEXT       (one-paragraph subject)
├── texto_completo  TEXT       (rendered plain text)
├── html_raw        TEXT       (consolidated HTML; used by parser)
├── hash            TEXT       (sha256 of html_raw for change detection)
└── fetched_at      TEXT
```

Plus an FTS5 virtual table over `ementa` and `texto_completo` for
search.

## Usage

```bash
# Step 1: discover all law URLs (fast — just the index pages)
python3 scraper.py discover

# Step 2: download all discovered laws (slow — ~57k laws, hours)
python3 scraper.py download

# Or run both in sequence
python3 scraper.py all

# Search for laws by topic
python3 scraper.py search "improbidade"

# Database statistics
python3 scraper.py stats
```

## Status

This tool is optional infrastructure. The institutions reference does
not need it to function — the relevant article-level data is shipped
separately as `artigos.db`. The scraper is included so:

1. The pipeline that produced `artigos.db` is fully reproducible.
2. Users who want to ingest more laws into the catalog can rebuild
   from sources.
3. The scraping methodology is auditable.

## Output flow

```
planalto.gov.br
      │
      │ scraper.py
      ▼
~/research/data/planalto/planalto_legislacao.db    (this tool's output)
      │
      │ ../leis_artigos/build.py
      ▼
~/research/data/lei/artigos.db                     (article-level structured DB)
      │
      │ ../leis_artigos/cite.py / lookup.py
      ▼
prose citations in ../*.md
```

## Reliability and politeness

- 0.5 second delay between requests by default. Don't lower this
  without a reason — planalto is a federal government service.
- Retries on transient HTTP errors with exponential backoff.
- All fetches are logged with timestamp.
- The `hash` column lets you detect when planalto has updated a law's
  consolidated text and re-parse it without re-downloading the whole
  catalog.

## Caveats

- Planalto's HTML is inconsistent across eras. Older laws may have
  malformed structure that the article-level parser
  (`../leis_artigos/parser.py`) handles via overrides.
- The scraper does not handle PDF-only laws (very old decretos-lei).
  These are out of scope for the article DB.
- Some laws have multiple consolidations (e.g., the version with
  amendments through different cutoff dates). The scraper takes the
  most-recent consolidation; the article DB tracks version history
  separately via the `vigente_desde` / `vigente_ate` columns.

## See also

- [`../leis_artigos/`](../leis_artigos/) — the article-level parser
  that consumes this database.
- [`../README.md`](../README.md) — overview of the `tools/` directory.
- [`../../CLAUDE.md`](../../CLAUDE.md) — citation format and how this
  pipeline supports the bracket-form citations.
