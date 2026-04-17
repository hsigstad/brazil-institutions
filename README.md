# Brazilian institutions — a structured reference for research

A dense, citation-backed reference on Brazilian legal and political
institutions, designed to be read by both researchers and LLM agents.
Covers courts, procedure, the Ministério Público, fiscal federalism,
electoral system, procurement, corruption statutes, labor justice,
and related topics.

**What this gives you:**

- **32 topical files** with inline statute and jurisprudence citations
- **Citation resolver** (`cite.py`) that looks up any statute article,
  STF case, or súmula from a compact backtick citation
- **Annotated legislation databases** — STF decisions mapped to each CF
  article; TSE jurisprudence mapped to each Electoral Code article
- **463 TST súmulas**, 72 TSE súmulas, 63 STF Súmulas Vinculantes,
  3 STJ súmulas — all resolvable via cite.py
- **Common-pitfalls list** so you don't make the mistakes everyone
  makes about Brazilian institutions

**What this is not:** an authoritative legal treatise, current binding
law, or a substitute for reading the statute. Coverage reflects the
maintainer's research areas (corruption, courts, elections, fiscal
federalism). Most claims cite statutes or jurisprudence inline; verify
against the primary source for legally-current work.

## Quick start

```bash
# Look up a statute article
python3 tools/leis_artigos/cite.py 'LIA.9'

# Look up an STF case
python3 tools/leis_artigos/cite.py 'Tema1199'

# Look up a súmula (STF SV, TSE, TST, STJ)
python3 tools/leis_artigos/cite.py 'SV14'
python3 tools/leis_artigos/cite.py 'STSE38'
python3 tools/leis_artigos/cite.py 'STST331'

# Show STF jurisprudence for a CF article
python3 tools/leis_artigos/cite.py 'CF.37' --annotations

# Show TSE jurisprudence for a CE article
python3 tools/leis_artigos/cite.py 'CE.35' --annotations

# Find all citations in a markdown file
python3 tools/leis_artigos/cite.py --find-in topics/improbidade.md
```

Statute and annotation lookups (`LIA.9`, `CF.37 --annotations`) need
`institutions.db` — the consolidated SQLite database bundling statute
text + STF/TSE annotations. Download it from the latest
[release](https://github.com/hsigstad/brazil-institutions/releases)
and place it at `~/research/data/institutions.db`, or set the
`INSTITUTIONS_DB` env var. Jurisprudence and súmula lookups (`Tema1199`,
`SV14`, `STSE38`) work without the database — they use YAML indices
shipped in the repo.

## Using with LLM agents

This repo is optimized for [Claude Code](https://claude.com/claude-code)
and similar agents. The format conventions — topic keywords, inline
statute citations, cross-reference backlinks, alphabetical indices —
are designed for fast grep and self-contained claims that survive being
read out of context.

**For agents:** [`CLAUDE.md`](CLAUDE.md) is the entry point (auto-loaded
by Claude Code). It has a quick-start guide, navigation instructions,
and the full citation grammar.

**For humans:** start here, then grep [`siglas.md`](siglas.md) for
acronyms and [`glossario.md`](glossario.md) for Portuguese legal terms.

## Contents

### Cross-cutting flows

- [`topics/fluxo-corrupcao-municipal.md`](topics/fluxo-corrupcao-municipal.md) — Life cycle of a municipal corruption case: detection → TCE → câmara → MP → improbidade → sanctions → Ficha Limpa
- [`topics/fluxo-transferencia-federal.md`](topics/fluxo-transferencia-federal.md) — How a federal transfer becomes a municipal expenditure: allocation → budget → procurement → audit → enforcement

### Constitutional framework

- [`topics/juizes.md`](topics/juizes.md) — Judicial guarantees, duties, entry, promotion (CF provisions)
- [`topics/funcoes-essenciais.md`](topics/funcoes-essenciais.md) — MP, advocacia pública, advocacia, defensoria

### Courts

- [`topics/cortes-superiores.md`](topics/cortes-superiores.md) — STF, STJ, TSE, TST, STM, CNJ composition and competence
- [`topics/justica-federal.md`](topics/justica-federal.md) — TRFs, varas federais, federal competence
- [`topics/justica-estadual.md`](topics/justica-estadual.md) — TJs, comarcas, entrância system
- [`topics/justica-eleitoral.md`](topics/justica-eleitoral.md) — TSE, TREs, zonas eleitorais
- [`topics/justica-trabalho.md`](topics/justica-trabalho.md) — TST, TRTs, varas do trabalho, 2017 reform
- [`topics/tribunais-contas.md`](topics/tribunais-contas.md) — TCU, TCEs, TCMs (audit courts)
- [`topics/cnj-administracao-judicial.md`](topics/cnj-administracao-judicial.md) — CNJ normative power, Justiça em Números, PJe, case numbering

### Procedure

- [`topics/processo-civil.md`](topics/processo-civil.md) — CPC 2015, recursos, execução, tutela provisória
- [`topics/processo-eleitoral.md`](topics/processo-eleitoral.md) — AIPRC, AIME, AIJE, RCED, recursos eleitorais
- [`topics/processo-penal.md`](topics/processo-penal.md) — CPP, prescrição, recursos criminais
- [`topics/procedimentos-legais.md`](topics/procedimentos-legais.md) — Foro privilegiado, case assignment, segredo de justiça

### Career and history

- [`topics/carreira-juizes.md`](topics/carreira-juizes.md) — Concurso, entrância, promoção, quinto constitucional
- [`topics/reformas-judiciais.md`](topics/reformas-judiciais.md) — Chronology of reforms 1965–2019
- [`topics/organizacao-judiciario.md`](topics/organizacao-judiciario.md) — Judiciary structural overview

### Institutions

- [`topics/ministerio-publico.md`](topics/ministerio-publico.md) — MP structure, career, CNMP, investigative instruments
- [`topics/policia-federal.md`](topics/policia-federal.md) — Polícia Federal, jurisdiction, operações, PF–MP triangular relationship
- [`topics/policias-estaduais.md`](topics/policias-estaduais.md) — Polícia Civil, Polícia Militar, Guarda Municipal; state-level PC–MPE flow
- [`topics/cgu-controle-interno.md`](topics/cgu-controle-interno.md) — CGU, random municipal audits, PAD, Lei Anticorrupção
- [`topics/controladorias-estaduais.md`](topics/controladorias-estaduais.md) — CGE / state controladorias, state-level PAD, PAR, state leniency
- [`topics/controle-legislativo.md`](topics/controle-legislativo.md) — CPIs, impeachment, decoro parlamentar, Senate approvals, congressional contas review
- [`topics/partidos-e-sistema-eleitoral.md`](topics/partidos-e-sistema-eleitoral.md) — Open-list PR, coligações/federações, campaign finance, Ficha Limpa
- [`topics/federalismo-fiscal.md`](topics/federalismo-fiscal.md) — FPM, ICMS, SUS transfers, LRF limits

### Substantive areas

- [`topics/licitacoes.md`](topics/licitacoes.md) — Procurement law, CADE cartel typology, bid-rigging
- [`topics/improbidade.md`](topics/improbidade.md) — Lei 8.429/92, 2021 reform, Tema 1199
- [`topics/anticorrupcao-penal.md`](topics/anticorrupcao-penal.md) — Criminal corruption, lavagem, colaboração premiada, Lei Anticorrupção
- [`topics/contas-municipais.md`](topics/contas-municipais.md) — Mayoral accounts, TCE parecer, câmara vote, Ficha Limpa
- [`topics/prestacao-contas-eleitorais.md`](topics/prestacao-contas-eleitorais.md) — Campaign finance accounting
- [`topics/transparencia-dados.md`](topics/transparencia-dados.md) — LAI, LGPD, data infrastructure

### Indices (start here when navigating)

| Index | What it answers |
|---|---|
| [`siglas.md`](siglas.md) | "What does this acronym mean?" |
| [`glossario.md`](glossario.md) | "What does this Portuguese legal term mean?" |
| [`pitfalls.md`](pitfalls.md) | "Am I about to make a common mistake?" |
| [`leis_index.yaml`](leis_index.yaml) | "What's the status/apelido of this law?" |
| [`jurisprudencia-stf.md`](jurisprudencia-stf.md) | "What did the STF decide in this case?" |
| [`quasi-experimentos.md`](quasi-experimentos.md) | "What natural experiments exist in Brazilian institutions?" |
| [`data_pointers.md`](data_pointers.md) | "Where does this data live?" |
| [`timeline.md`](timeline.md) | "When did this reform/decision happen?" |
| [`faq.md`](faq.md) | "How do I find X?" (by research question) |

### Súmula indices

| File | Court | Count | Citation prefix |
|---|---|---|---|
| [`sumulas_vinculantes.yaml`](sumulas_vinculantes.yaml) | STF (binding) | 63 | `SV14` |
| [`sumulas_tse.yaml`](sumulas_tse.yaml) | TSE | 72 | `STSE38` |
| [`sumulas_tst.yaml`](sumulas_tst.yaml) | TST | 463 | `STST331` |
| [`sumulas_stj.yaml`](sumulas_stj.yaml) | STJ (on demand) | 3 | `SSTJ359` |

## Tools

| Tool | Purpose |
|---|---|
| [`tools/leis_artigos/cite.py`](tools/leis_artigos/) | Citation resolver — statutes, cases, súmulas, annotations |
| [`tools/planalto_scraper/`](tools/planalto_scraper/) | Scraper for statute text from planalto.gov.br |
| [`tools/tse_ce_anotado/`](tools/tse_ce_anotado/) | TSE annotated Electoral Code → SQLite (422 annotations) |
| [`tools/stf_constituicao/`](tools/stf_constituicao/) | STF annotated Constitution → SQLite (1,758 annotations) |
| [`tools/tst_scraper/`](tools/tst_scraper/) | TST Súmulas via Playwright (463 entries) |
| [`tools/sumulas_scraper/`](tools/sumulas_scraper/) | STF SV and TSE súmula scrapers |

## Extending to new areas

This repo covers the institutional areas most relevant to the
maintainer's research (corruption, courts, elections, fiscal
federalism). If your research touches a different area — health law,
environmental regulation, tax procedure, social security — the
architecture is designed to extend:

1. **Add a topical file** in `topics/` following the existing format
   (header with scope, keywords, snapshot date, cross-references).
2. **Add statutes** to `leis_index.yaml` with an apelido so cite.py
   can resolve them.
3. **Add cases** to `jurisprudencia_index.yaml` and
   `jurisprudencia-stf.md` as needed.
4. **Add acronyms** to `siglas.md` and terms to `glossario.md`.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines.

## Status

A living reference, updated as research projects surface new material.
Coverage is uneven — not every file is revisited on every change in
the law. Each topical file carries a `Snapshot as of YYYY` line. For
legally-current details, verify against the primary source.

## License

Released under **CC BY 4.0** (see [`LICENSE`](LICENSE)). You are free
to use, share, and adapt the material with attribution.
