# leis_artigos — article-level Brazilian law database

Parses planalto.gov.br consolidated HTML into a structured table where
each row is one **leaf** of an article (caput, parágrafo, inciso,
alínea, item) with its current text, amendment history, and
date-versioned tracking.

This is the lookup backend for the compact backtick-form citations
used throughout the institutions reference. See
[`../../CLAUDE.md`](../../CLAUDE.md) (section "Citing statutes")
for the citation format.

## Quick start (end user)

If you just want to look up exact statutory text:

1. **Download `institutions.db`** from the latest
   [GitHub release](https://github.com/hsigstad/brazil-institutions/releases).
2. **Place at the default location**: `~/research/data/institutions.db`
   (or set `INSTITUTIONS_DB` env var to your chosen path).
3. **Query**:

   ```bash
   # Resolve a backtick-form citation
   python3 cite.py '`LIA.10.§1.II`'
   python3 cite.py '`LE.11.§10@2024-12-31`'
   python3 cite.py '`LIA.10 from:L14230-2021`'

   # Or use the lower-level lookup CLI (still reads from the
   # intermediate artigos.db — see "Maintainer" below)
   python3 lookup.py LIA 9
   python3 lookup.py LIA 9 --path II
   python3 lookup.py LE 36-A --as-of 2010-01-01
   python3 lookup.py --by-amending L14230-2021
   ```

You do **not** need the planalto scraper or the build pipeline.

## Database

`cite.py` reads from the consolidated `institutions.db` (the release
asset). `lookup.py` and `build.py` still read/write the intermediate
`artigos.db` — that stage exists so the amendment-tracking and
reparsing loop doesn't have to rebuild the annotation tables on
every iteration.

**Default locations**:

| DB | Path | Used by |
|---|---|---|
| `institutions.db` | `~/research/data/institutions.db` | `cite.py` (end-user lookup) |
| `artigos.db`      | `~/research/data/lei/artigos.db`  | `build.py`, `build_amendments.py`, `lookup.py`, `fix_dates_from_amendments.py`, `find_amending.py` (maintainer only) |
| `planalto_legislacao.db` | `~/research/data/planalto/planalto_legislacao.db` | `build.py` input (raw planalto scrape) |

Override with `INSTITUTIONS_DB`, `ARTIGOS_DB`, `PLANALTO_DB` env
vars or the corresponding CLI flags.

### `artigo` table schema

| column            | meaning |
|---|---|
| `apelido`         | short alias, e.g., `LIA`, `LE`, `L8666` |
| `numero_lei`, `ano_lei` | the law's identifying number + year |
| `capitulo`, `secao` | hierarchical context (Roman numerals) |
| `capitulo_titulo`, `secao_titulo` | human-readable titles |
| `artigo`, `artigo_letra` | article number + optional letter (e.g., 17, 'A' for 17-A) |
| `path`            | structural location within the article (see `PATH_CONVENTION.md`) |
| `texto`           | verbatim text of THIS leaf only |
| `vigente_desde`   | YYYY-MM-DD when this version came into force |
| `vigente_ate`     | YYYY-MM-DD when superseded, or NULL if currently in force |
| `fonte`           | display label, e.g., `Lei nº 14.230, de 2021` |
| `fonte_id`        | canonical key for joins/filtering: `L14230-2021`, `LC219-2025`, `EC45-2004` |
| `revogado`        | 1 if currently revoked |
| `ordem`           | document order for stable reconstruction |
| `raw_anchor`      | source planalto anchor (debugging) |
| `observacoes`     | free-text notes |

### `amendment` table schema

Tracks which amending lei touched which clause of which target lei
(populated by parsing the amending laws themselves, not just the
consolidated targets).

| column | meaning |
|---|---|
| `amending_fonte_id` | canonical id of the amending lei (e.g., `L14230-2021`) |
| `amending_label`    | display label |
| `amending_data`     | publication date of the amending lei |
| `target_apelido`    | target law's apelido if cataloged (e.g., `LIA`) |
| `target_filename`   | target lei filename in planalto (e.g., `L8429.htm`) |
| `target_tipo`       | target type (`L`, `LC`, `MP`, `DL`, `D`, `EC`) |
| `target_numero`     | target lei numero |
| `artigo`, `artigo_letra` | target article being changed |
| `path`              | structural path within the target article |
| `action`            | `add`, `modify`, or `revoke` |
| `source_anchor`     | the linked anchor in the target lei |
| `source_text`       | snippet of context from the amending lei |

## Catalog (as of 2026)

62 laws cataloged. Apelidos used in the backtick-form citations:

| apelido | lei | scope |
|---|---|---|
| **CC** | Lei 10.406/2002 | Código Civil |
| **CDC** | Lei 8.078/1990 | Código de Defesa do Consumidor |
| **CE** | Lei 4.737/1965 | Código Eleitoral |
| **CF** | CF/1988 | Constituição Federal |
| **CLT** | DL 5.452/1943 | Consolidação das Leis do Trabalho |
| **CP** | DL 2.848/1940 | Código Penal |
| **CPC** | Lei 13.105/2015 | Código de Processo Civil |
| **CPC1973** | Lei 5.869/1973 | CPC anterior (para citações históricas) |
| **CPP** | DL 3.689/1941 | Código de Processo Penal |
| **CTN** | Lei 5.172/1966 | Código Tributário Nacional |
| **EOAB** | Lei 8.906/1994 | Estatuto da OAB |
| **L8112** | Lei 8.112/1990 | RJU servidores federais |
| **L8666** | Lei 8.666/1993 | Lei de Licitações antiga |
| **L12414** | Lei 12.414/2011 | Cadastro Positivo |
| **L12891** | Lei 12.891/2013 | Modificações ao CE e LE |
| **L13019** | Lei 13.019/2014 | Lei das OSCs |
| **L13165** | Lei 13.165/2015 | Minirreforma eleitoral |
| **L13487** | Lei 13.487/2017 | Criação do FEFC |
| **L13488** | Lei 13.488/2017 | Limites de despesa eleitoral |
| **L14133** | Lei 14.133/2021 | Nova Lei de Licitações |
| **L14230** | Lei 14.230/2021 | Reforma da LIA |
| **LAC** | Lei 12.846/2013 | Lei Anticorrupção |
| **LACP** | Lei 7.347/1985 | Lei da Ação Civil Pública |
| **LAI** | Lei 12.527/2011 | Lei de Acesso à Informação |
| **LAP** | Lei 4.717/1965 | Lei da Ação Popular |
| **LC62** | LC 62/1989 | Fundos de Participação — critérios de rateio |
| **LC141** | LC 141/2012 | Gasto mínimo em saúde |
| **LC143** | LC 143/2013 | Ajustes ao rateio do FPE |
| **LC166** | LC 166/2019 | Ajustes ao FPM |
| **LCADE** | Lei 12.529/2011 | Lei do CADE / Defesa da Concorrência |
| **LCMP** | LC 75/1993 | Lei Orgânica do MPU |
| **LCO** | Lei 12.850/2013 | Lei das Organizações Criminosas |
| **LCOT** | Lei 8.137/1990 | Crimes contra a ordem tributária e econômica |
| **LCT** | LC 131/2009 | Lei da Transparência |
| **LE** | Lei 9.504/1997 | Lei das Eleições |
| **LFL** | LC 135/2010 | Lei da Ficha Limpa |
| **LGPD** | Lei 13.709/2018 | Lei Geral de Proteção de Dados |
| **LI** | LC 64/1990 | Lei das Inelegibilidades |
| **LIA** | Lei 8.429/1992 | Lei de Improbidade Administrativa |
| **LJE** | Lei 9.099/1995 | Lei dos Juizados Especiais |
| **LJEFP** | Lei 12.153/2009 | Juizados Especiais da Fazenda Pública |
| **LL** | Lei 9.613/1998 | Lei de Lavagem |
| **LL2** | Lei 12.683/2012 | Reforma da Lei de Lavagem |
| **LOMAN** | LC 35/1979 | Lei Orgânica da Magistratura Nacional |
| **LOMP** | Lei 8.625/1993 | Lei Orgânica Nacional do MP |
| **LOTCU** | Lei 8.443/1992 | Lei Orgânica do TCU |
| **LP** | Lei 10.520/2002 | Lei do Pregão |
| **LPC** | Lei 13.964/2019 | Pacote Anticrime |
| **LPP** | Lei 9.096/1995 | Lei dos Partidos Políticos |
| **LRF** | LC 101/2000 | Lei de Responsabilidade Fiscal |
| **LSUS** | Lei 8.080/1990 | Lei Orgânica do SUS |
| **RDC** | Lei 12.462/2011 | Regime Diferenciado de Contratações |
| **L6360** | Lei 6.360/1976 | Vigilância Sanitária (medicamentos) |
| **L8142** | Lei 8.142/1990 | Participação no SUS + transferências |
| **L9656** | Lei 9.656/1998 | Planos de saúde / ANS |
| **L12401** | Lei 12.401/2011 | CONITEC / RENAME (amende LSUS) |
| **L14454** | Lei 14.454/2022 | Rol da ANS exemplificativo |
| **EC29** | EC 29/2000 | Gasto mínimo em saúde |
| **EC86** | EC 86/2015 | Orçamento impositivo |
| **EC95** | EC 95/2016 | Teto de gastos |
| **EC113** | EC 113/2021 | Precatórios e teto de gastos |
| **EC126** | EC 126/2022 | PEC da Transição |

The full mapping with metadata, statuses, and reform relationships is
in [`../../leis_index.yaml`](../../leis_index.yaml).

## CLI tools

### `cite.py` — resolve backtick-form citations

The bridge between prose and database. Takes a citation string in the
canonical backtick form documented in `../../CLAUDE.md` and runs the
corresponding SQL query.

```bash
# Default form: current version
python3 cite.py '`LIA.9`'
python3 cite.py '`LIA.9.§1.II`'

# Date-versioned
python3 cite.py '`LE.11.§10@2024-12-31`'

# Source-versioned
python3 cite.py '`LIA.10 from:L14230-2021`'

# Original version shorthand
python3 cite.py '`LIA.10:original`'

# Whole law
python3 cite.py '`LIA`'

# Just parse, don't query
python3 cite.py --parse-only '`LIA.17-A.caput`'

# Find all citations in a file
python3 cite.py --find-in ../../improbidade.md
```

### `lookup.py` — direct database query

Lower-level CLI; takes apelido + article + path as positional args
and supports a wider set of query options.

```bash
# List all laws in the catalog
python3 lookup.py --list-laws

# List all articles of a law
python3 lookup.py LIA --list-articles

# Get one article (current version)
python3 lookup.py LIA 9                       # all current paths
python3 lookup.py LIA 9 --path caput          # just the caput
python3 lookup.py LIA 9 --path II             # inciso II
python3 lookup.py LIA 9 --path §1.II          # § 1º inciso II

# Show all historical versions of one path
python3 lookup.py LIA 9 --path IV --history

# Show what was in force on a specific date
python3 lookup.py LIA 9 --as-of 2020-01-01
python3 lookup.py LIA 9 --path caput --as-of 2015-06-15

# Include chapter/section context in output
python3 lookup.py LIA 9 --path II --full

# Article with letter (e.g., Art. 17-A)
python3 lookup.py LIA 17-A

# Show all amendments to a clause
python3 lookup.py LIA 9 --amendments
python3 lookup.py LIA 9 --path caput --amendments

# Show what an amending law touched
python3 lookup.py --by-amending L14230-2021
```

## Path syntax

See [`PATH_CONVENTION.md`](PATH_CONVENTION.md) for the strict grammar.
Quick reference:

| path | meaning |
|---|---|
| `caput` | article caput |
| `ementa` | the law's ementa (preamble) |
| `II` | inciso II under article caput |
| `II.a` | alínea a of inciso II |
| `§1` | caput of § 1º |
| `§unico` | parágrafo único caput |
| `§1.II` | inciso II of § 1º |
| `§1.II.a` | alínea a of § 1º inciso II |

## For maintainers — building and updating

The build pipeline reads from `planalto_legislacao.db` (the raw
planalto scrape produced by `../planalto_scraper/scraper.py`) and
writes the structured `artigos.db`.

### Build the article DB

```bash
# Build everything in the catalog
python3 build.py

# Build just one apelido
python3 build.py --apelido LIA

# Custom paths
PLANALTO_DB=/path/to/planalto.db ARTIGOS_DB=/path/to/artigos.db python3 build.py
```

`build.py` reads the `LAW_CATALOG` constant. Add a new entry tuple
`(apelido, numero, ano, planalto_id)` to add a law. Find the correct
`planalto_id` with:

```bash
sqlite3 ~/research/data/planalto/planalto_legislacao.db \
  "SELECT id, tipo, numero, data, substr(ementa,1,80) FROM legislacao WHERE numero='X'"
```

### Build the amendment table

```bash
python3 build_amendments.py
```

This populates the `amendment` table by parsing the amending laws
themselves (looking up their planalto HTML and extracting hyperlinks
to target articles).

### Manual overrides

When the parser produces wrong rows because of bugs in planalto's HTML
(typos, missing annotations, structural ambiguity), add an override
in `overrides/{apelido}.py`. See `overrides/README.md` for the format.

## Useful queries

```sql
-- All clauses currently in force that came from the LIA reform
SELECT * FROM artigo WHERE fonte_id='L14230-2021' AND vigente_ate IS NULL;

-- Everything affected by a specific amending law
SELECT * FROM artigo WHERE fonte_id='LC219-2025';

-- How much of L 8.666 is still original vs amended
SELECT
  SUM(CASE WHEN fonte_id='L8666-1993' AND vigente_ate IS NULL THEN 1 ELSE 0 END) AS original_in_force,
  SUM(CASE WHEN fonte_id != 'L8666-1993' AND vigente_ate IS NULL THEN 1 ELSE 0 END) AS amended_in_force
FROM artigo WHERE apelido='L8666';

-- Which amending laws touched a given target
SELECT DISTINCT fonte_id, fonte FROM artigo WHERE apelido='LE' ORDER BY fonte_id;

-- All amendments to LIA Art. 9
SELECT * FROM amendment WHERE target_apelido='LIA' AND artigo=9 ORDER BY amending_data;

-- Articles of LE that have been amended the most
SELECT artigo, COUNT(DISTINCT amending_fonte_id) AS n_amendments
FROM amendment
WHERE target_apelido='LE'
GROUP BY artigo
ORDER BY n_amendments DESC LIMIT 10;
```

## Known limitations

1. **Vetoed clauses produce noisy rows** (e.g., LIA Art. 17-A, all
   clauses `(VETADO)`) — planalto includes them with placeholder text.
2. **Planalto anchor typos** (e.g., `art17aiiii` for what should be
   `iii`) produce malformed paths. Data quality issue upstream.
3. **Structural changes that replace §unico with §1, §2, ...** can
   leave both formats coexisting in the consolidated text. The parser
   captures both as if currently in force; the user must manually
   disambiguate.
4. **Alíneas and items** that appear within an inciso are not
   currently extracted as separate rows — they're embedded in the
   inciso text.
5. **Articles added by amendment then revised** sometimes have an
   incorrect `vigente_desde` for the FIRST version, because the
   original anchor doesn't always carry an `(Incluído pela...)`
   annotation. The newer revision is dated correctly.
6. **Amendments to non-cataloged target laws** may have malformed
   paths because their anchor conventions differ. The amendment is
   still tracked correctly at the article level.
7. **Old amending laws (pre-2000)** often lack hyperlinks and produce
   0 amendments. Add manual overrides if needed.

When citing in a paper, **always verify the text against
planalto.gov.br** for any clause that depends on legally-current
details.
