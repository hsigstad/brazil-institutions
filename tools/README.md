# tools/

Code that complements the markdown reference. The tools here are
optional — the prose reference works fine without them — but they
make the reference much more useful when you need exact statutory
text or want to resolve a citation programmatically.

## Subdirectories

### `tse_ce_anotado/` — TSE annotated Electoral Code

Scrapes the TSE's Código Eleitoral Anotado into `ce_anotado.db`.
Each CE article is mapped to its TSE jurisprudence annotations
(acórdãos, resoluções, CF cross-references). 422 annotations across
176 articles. Integrated with `cite.py --annotations`.

### `stf_constituicao/` — STF annotated Constitution

Scrapes "A Constituição e o Supremo" via the STF's JSON API into
`cf_stf_anotada.db`. Each CF article is mapped to STF decisions
(controle concentrado, repercussão geral, julgados correlatos).
1,758 annotations across 183 articles, 1,655 with extractable case
citations. Integrated with `cite.py --annotations`.

### `tst_scraper/` — TST Súmulas (via Playwright)

Scrapes all 463 TST Súmulas via browser automation (TST blocks
non-browser API access). Output: `sumulas_tst.yaml` at repo root.
Requires `pip install playwright && playwright install chromium`.

### `sumulas_scraper/` — STF SV and TSE súmula scrapers

Scrapes STF Súmulas Vinculantes and TSE Súmulas. Output:
`sumulas_vinculantes.yaml` and `sumulas_tse.yaml` at repo root.

### `leis_artigos/` — article-level law database and citation resolver

Parses planalto.gov.br consolidated HTML into a structured SQLite
table where each row is one **leaf** of an article (caput,
parágrafo, inciso, alínea, item) with its current text, amendment
history, and date-versioned tracking.

Currently catalogs 52 federal laws (as of 2026), including LIA,
L8666, L14133, LE, CC, CPC, CPP, CE, LRF, LFL, LAI, LGPD, LAC, LCO,
LP, LPP, and many others. See `leis_artigos/README.md` for the full
catalog and lookup instructions.

**Key files:**

- `cite.py` — resolves compact backtick-form citations
  (``LIA.10.§1.II``) directly to article rows. The bridge between
  the prose reference (`../*.md`) and the database.
- `lookup.py` — CLI for querying the article DB by apelido + article
  + path, with date-versioned and source-versioned options.
- `build.py` — rebuilds `artigos.db` from the planalto raw scrape.
  Maintainer-only; needs `planalto_legislacao.db`.
- `build_institutions.py` — merges `artigos.db`, `cf_stf_anotada.db`,
  and `ce_anotado.db` into the distributable `institutions.db`
  (the release asset).
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
prebuilt `institutions.db` is shipped as a GitHub release asset so
most users don't need to scrape.

## Running the tools

Databases live outside the repo by convention:

```
~/research/data/institutions.db                   # consolidated release DB (cite.py reads this)
~/research/data/lei/artigos.db                    # intermediate article-level DB (build.py output)
~/research/data/planalto/planalto_legislacao.db   # raw planalto scrape (build input)
```

Override with environment variables:

```bash
export INSTITUTIONS_DB=/path/to/institutions.db    # used by cite.py
export ARTIGOS_DB=/path/to/artigos.db              # used by build.py, build_amendments.py, lookup.py
export PLANALTO_DB=/path/to/planalto_legislacao.db
```

Or pass `--db` / `--artigos-db` / `--planalto-db` on the CLI.

## Two paths for users

**End user** (you have the institutions reference and want to look
up exact text):

1. Download `institutions.db` from the latest
   [GitHub release](https://github.com/hsigstad/brazil-institutions/releases)
   and place at `~/research/data/institutions.db`.
2. Use `cite.py` to query.
3. You do **not** need `planalto_scraper/`, `build.py`, or the
   individual scraper DBs.

**Maintainer** (you want to add laws to the catalog or fix parser
bugs):

1. Run `planalto_scraper/scraper.py` to build the raw planalto
   mirror (slow; ~57k laws; only needed once).
2. Edit the `LAW_CATALOG` in `leis_artigos/build.py` to add new
   apelidos.
3. Run `leis_artigos/build.py` to rebuild `artigos.db`.
4. Run `leis_artigos/build_amendments.py` to populate the
   `amendment` table.
5. Run `leis_artigos/build_institutions.py` to merge
   `artigos.db` + `cf_stf_anotada.db` + `ce_anotado.db` into
   `institutions.db`, and upload to a new release.

## Why these tools live in this repo

The institutions reference cites statutes inline using the compact
backtick form ``apelido.artigo.path`` (see `../CLAUDE.md`). To make
those citations resolvable, the schema and lookup tooling must be
discoverable from the same place. Shipping the code here keeps the
contract local: the format used in the prose is the format the tools
parse.

The actual database files (`institutions.db`, `artigos.db`,
`planalto_legislacao.db`) do **not** live in this repo — they're
build artifacts. `institutions.db` is distributed via GitHub
releases; the intermediate build artifacts stay on the maintainer's
machine.
