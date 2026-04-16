# TSE Código Eleitoral Anotado — scraper

Scrapes the TSE's annotated Electoral Code into a SQLite database,
enabling `cite.py --annotations` to show jurisprudence cross-references
alongside CE article text.

## Source

[TSE Código Eleitoral Anotado](https://www.tse.jus.br/legislacao/codigo-eleitoral/codigo-eleitoral-1/codigo-eleitoral-lei-nb0-4.737-de-15-de-julho-de-1965)
— the only freely available article-by-article annotated Brazilian
legislation with jurisprudence cross-references.

## Usage

```bash
# Fetch + build in one step
python3 scraper.py all

# Or separately
python3 scraper.py fetch     # download HTML to cache
python3 scraper.py build     # parse cached HTML → SQLite
```

## Output

`ce_anotado.db` with one table:

```sql
CREATE TABLE anotacao (
    id INTEGER PRIMARY KEY,
    lei TEXT NOT NULL,         -- 'CE'
    artigo INTEGER NOT NULL,   -- article number
    artigo_letra TEXT,         -- letter suffix if any (e.g., '22-A')
    tipo TEXT NOT NULL,         -- classification (see below)
    referencia TEXT,            -- extracted citation key
    texto TEXT NOT NULL          -- full annotation text
);
```

### Annotation types (`tipo`)

| Type | Count | Description |
|---|---|---|
| `acordao_tse` | ~72 | TSE court decisions |
| `acordao_stf` | ~5 | STF court decisions |
| `acordao_stj` | ~1 | STJ court decisions |
| `resolucao_tse` | ~43 | TSE resolutions |
| `cf` | ~48 | Constitutional cross-references |
| `lei` | ~102 | References to other laws |
| `lc` | ~10 | References to complementary laws |
| `redacao` | ~54 | Amendment history (wording changes) |
| `ver` | ~51 | Internal cross-references ("V. art. X") |
| `other` | ~36 | Miscellaneous notes |

Total: ~422 annotations across ~176 articles (of ~383 total CE articles).

## Integration with cite.py

```bash
# Show annotations alongside article lookup
python3 ../leis_artigos/cite.py 'CE.35' --annotations

# Works even without artigos.db — annotations are independent
python3 ../leis_artigos/cite.py 'CE.22' --annotations
```

## Cache

HTML is cached at `~/research/data/tse_ce_anotado/ce_anotado.html`
(override with `CE_CACHE` env var). Re-fetched if older than 7 days.

## Dependencies

Stdlib only (urllib, re, sqlite3). No external packages.
