# Brazilian institutions — reference

Reference notes on Brazilian legal institutions, courts, and procedure.
Compiled from accumulated org-mode notes (`~/Dropbox/org/judiciario.org` and
`~/Dropbox/org/processo.org`), which span ~2018–2025. Migrated and split
into topical files in this directory.

**Status: snapshot, not authoritative.** Some details may be out of date
(e.g., post-2017 CPC reforms, recent CNJ resolutions, electoral law
changes). For project work that depends on legally-current details, verify
against the current law text. This is reference for orientation, not
citation.

**Language:** Portuguese where translation loses meaning, English otherwise.
Many legal terms have no clean English equivalent (`improbidade`, `prestação
de contas`, `recurso especial` etc.) and are kept in Portuguese throughout.

## Contents

### Constitutional framework

- [`juizes.md`](juizes.md) — Garantias, deveres, ingresso, promoções, subsídio, aposentadoria, remoção (constitutional provisions about individual judges)
- [`funcoes-essenciais.md`](funcoes-essenciais.md) — MP, advocacia pública, advocacia, defensoria (constitutional overview; see `ministerio-publico.md` for MP detail)

### Courts

- [`cortes-superiores.md`](cortes-superiores.md) — CNJ, CJF, STF, STJ
- [`justica-federal.md`](justica-federal.md) — Federal courts (lower)
- [`justica-estadual.md`](justica-estadual.md) — State courts
- [`justica-eleitoral.md`](justica-eleitoral.md) — Electoral courts (TSE, TREs)
- [`justica-trabalho.md`](justica-trabalho.md) — Labor courts (TST, TRTs, varas)
- [`tribunais-contas.md`](tribunais-contas.md) — TCU, TCEs, TCMs (audit courts)
- [`cnj-administracao-judicial.md`](cnj-administracao-judicial.md) — CNJ normative power, Justiça em Números, PJe/e-Proc/ESAJ, TPU, case numbering, specialization, execução fiscal

### Procedure (processo)

- [`processo-civil.md`](processo-civil.md) — Civil procedure (CPC, ação civil pública, improbidade, ação popular, recursos)
- [`processo-eleitoral.md`](processo-eleitoral.md) — Electoral procedure (AIPRC, AIME, AIJE, RCED, recursos)
- [`processo-penal.md`](processo-penal.md) — Criminal procedure
- [`procedimentos-legais.md`](procedimentos-legais.md) — General procedural notes

### Career & history

- [`carreira-juizes.md`](carreira-juizes.md) — Judicial career (selection, promotion, discipline)
- [`reformas.md`](reformas.md) — Judicial reforms (history of reforms to the judiciary)
- [`organizacao-historica.md`](organizacao-historica.md) — Historical organization, judicial districts

### Institutions (controle, prosecution, politics)

- [`ministerio-publico.md`](ministerio-publico.md) — MP structure (MPU/MPF/MPE/MPC), career, CNMP, inquérito civil, TAC, ACP, GAECO
- [`cgu-controle-interno.md`](cgu-controle-interno.md) — CGU: controle interno federal, Programa de Fiscalização por Sorteios (random audits), PAD, Lei Anticorrupção enforcement
- [`partidos-e-sistema-eleitoral.md`](partidos-e-sistema-eleitoral.md) — Open-list PR, cláusula de desempenho, coligações/federações, fundo partidário/FEFC, Ficha Limpa eligibility
- [`federalismo-fiscal.md`](federalismo-fiscal.md) — FPM, FPE, ICMS quota-parte, SUS transfers, royalties, IPTU/ISS, LRF limits, reforma tributária EC 132/2023

### Substantive areas

- [`licitacoes.md`](licitacoes.md) — Public procurement law (Lei 8.666/93, pregão, Lei 14.133/21), CADE cartel typology, bid-rigging red flags
- [`improbidade.md`](improbidade.md) — Lei 8.429/92 + Lei 14.230/21 reform, three categories, STF Tema 1199, MP standing, sanctions, prescription
- [`anticorrupcao-penal.md`](anticorrupcao-penal.md) — Criminal corruption statutes (CP, Lei 8.137, lavagem 9.613, orcrim 12.850, colaboração premiada) + Lei Anticorrupção 12.846 (corporate liability)
- [`contas-municipais.md`](contas-municipais.md) — Fiscal oversight of mayors: contas de governo vs. gestão, câmara vote, 2/3 rule, Ficha Limpa ineligibility, LRF
- [`prestacao-contas-eleitorais.md`](prestacao-contas-eleitorais.md) — Campaign finance accounting (electoral, not fiscal)
- [`transparencia-dados.md`](transparencia-dados.md) — LAI (Lei 12.527), LGPD (Lei 13.709), ANPD, Portal da Transparência, Comprasnet, SICONV, research implications

### Other

- [`nao-judicial.md`](nao-judicial.md) — Non-judicial institutions (diplomats, etc.)

## How to use

When starting a new project that needs Brazilian institutional context, grep
this directory for relevant terms before searching the web. For project-specific
detail (e.g., a particular CADE resolution), web search supplements.

### Reading guidance for future sessions

- **Grep first, then read the whole file.** Headers and subheaders are
  descriptive; topic keywords appear near the top of newer files. Try both
  Portuguese and English terms — e.g., "bid rigging" won't hit, but
  "cartel" and "licitação" will. Most files include a `Topics / keywords`
  line at the top for exactly this reason.
- **Verify before citing for legal-current work.** This directory is a
  snapshot (compiled ~2018–2025, with 2026 additions from project-level
  docs). Time-volatile claims — monetary thresholds, lists of
  municipalities/TCEs, pending STF theses, most recent reforms — are
  flagged with "as of YYYY" where possible. For anything that depends on
  currently-binding law text, verify against the planalto database (below)
  or the primary source.
- **Some files are project-sourced.** Newer files (`licitacoes.md`,
  `contas-municipais.md`, `tribunais-contas.md`, expanded
  `justica-trabalho.md`) were built from specific project `docs/institutions.md`
  files and may inherit that project's emphasis. Each such file names its
  provenance in the header. If a claim looks narrowly framed, check the
  source project for fuller context.
- **Intentional omissions.** Topics that appear in individual projects
  but are not cross-project — e.g., SUS / health-law institutional detail
  (lives in `projects/saude/docs/institutions.md`), Brazilian causation
  doctrine for labor accidents (`projects/causal-judge/docs/institutions.md`),
  the corruption-role typology (`projects/network/docs/institutions.md`)
  — are deliberately not migrated here. Don't treat their absence as a
  gap to fill; read the project file directly if relevant.
- **Cross-reference the new + old files.** Several old files
  (`justica-estadual.md`, `procedimentos-legais.md`, `justica-eleitoral.md`)
  now have "See also" pointers at the top to the new substantive-area
  files. Follow them when the topic spans multiple files.

**Avoid pasting verbatim law text into these files.** Files here should be
explanatory notes, summaries, and Henrik's own observations — not statute
copies. For the actual text of a law, query the planalto database (next
section).

## Looking up the text of a Brazilian law

The full text of all 57,255 federal laws scraped from planalto.gov.br lives
in a SQLite database with FTS5 full-text search:

```
~/research/projects/saude/data/planalto/planalto_legislacao.db
```

Schema (`legislacao` table): `tipo`, `numero`, `data`, `ementa`,
`texto_completo`, `url`. Indexed on `numero` and `tipo`. There's also a
`legislacao_fts` virtual table for FTS5 queries.

**Examples:**

```bash
# Full text of Lei 8.666/93 (procurement)
sqlite3 ~/research/projects/saude/data/planalto/planalto_legislacao.db \
  "SELECT texto_completo FROM legislacao WHERE numero='8666' AND tipo LIKE '%lei%' AND data LIKE '%1993%' LIMIT 1"

# Search for laws mentioning "improbidade administrativa"
sqlite3 ~/research/projects/saude/data/planalto/planalto_legislacao.db \
  "SELECT tipo, numero, data, substr(ementa, 1, 80) FROM legislacao_fts WHERE legislacao_fts MATCH 'improbidade administrativa' LIMIT 20"
```

**Caveats:**

- The DB lives under `saude/data/` for historical reasons. The scraping code
  is at `~/research/pipelines/bdata/source/scrape/planalto_scraper.py`.
  This DB should eventually move to `pipelines/bdata/data/planalto/` so that
  any project can use it without depending on saude. Tracked as a TODO.
- Articles are not parsed out individually — `texto_completo` is the full
  law as plain text. To extract `Art. 93` from a lei, regex on
  `Art\.\s*93[º°]?` and read until the next `Art\.\s*\d+`. A small
  utility (`bdata/source/lookup/lei.py`) is on the TODO list to make this
  ergonomic and to optionally build an article-level table.
- Last full scrape: 2025-02-07 (recent reforms may not be reflected).
