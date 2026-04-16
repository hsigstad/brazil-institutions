# TODO

Open follow-ups for the reference repository. Each item names what
needs to be done, why it matters, where it's currently flagged, and
the rough effort to resolve it.

This file is the central index of pending work. Inline `<!-- TODO: -->`
comments in topical files are the source of truth at the point of
relevance; this file aggregates them plus structural items that don't
have a natural inline home. Periodically re-grep
`grep -rn 'TODO:' --include='*.md'` and reconcile.

## Jurisprudence index — cases referenced but not yet cataloged

These cases are mentioned in topical files (with prose attribution)
but not yet present in `jurisprudencia_index.yaml`. Adding them
unlocks backtick-form citations and structured metadata. For each:
verify against the STF process page or Lexml acórdão record before
adding; do not fabricate from memory.

- ~~**AP 937 QO**~~ — added to `jurisprudencia_index.yaml` and
  `jurisprudencia-stf.md` (2026-04-16).

- ~~**ADI 2797**~~ — added to `jurisprudencia_index.yaml` and
  `jurisprudencia-stf.md` (2026-04-16).

## Statute catalog — uncataloged laws still referenced in prose

These laws appear in topical files as prose mentions but lack an
apelido in `leis_index.yaml`. Adding them enables backtick citations.

- ~~**Lei 13.467/2017**~~ (Reforma Trabalhista) — added as `LRT`
  (2026-04-16).
- ~~**Lei 14.208/2021**~~ (Federações partidárias) — added as `LFED`
  (2026-04-16).
- ~~**DL 201/1967**~~ (Crimes de prefeitos) — added as `DL201`
  (2026-04-16).
- ~~**Lei 10.628/2002**~~ (foro improbidade, inconstitucional) — added
  as `L10628` (2026-04-16).
- ~~**Lei 11.798/2008**~~ (CJF) — added as `LCJF` (2026-04-16).

Previously listed sweep items (LRF, CF, CP, CLT, CTN, EC citations)
were completed by the 2026-04-16 audit pass.

## Topical files — content gaps flagged inline


- ~~**`topics/justica-estadual.md`**~~ — added cross-state comarca
  count table (2,666 comarcas, 26 states, from diarios module) and
  TJSP historical time series (352 comarcas, 1700–2016, from justica
  pipeline). Completed 2026-04-16.

- ~~`CF.31.§1`~~ — resolved. Issue was missing DB, not a parse
  problem. Converted to backtick form (2026-04-16).

## Annotated legislation — scraping

~~**TSE Código Eleitoral Anotado**~~ — completed (2026-04-16).
Scraper at `tools/tse_ce_anotado/scraper.py`, DB at
`tools/tse_ce_anotado/ce_anotado.db` (422 annotations, 176 articles).

~~**STF "A Constituição e o Supremo"**~~ — completed (2026-04-16).
Scraper at `tools/stf_constituicao/scraper.py`, DB at
`tools/stf_constituicao/cf_stf_anotada.db` (1,758 annotations, 183
articles, 1,655 case citations).

Both integrated with `cite.py --annotations`.

**Future candidates** (lower priority, harder to scrape):
- TSE SNE (8 thematic PDFs — would need PDF extraction)
- Dizer o Direito blog (unstructured blog posts, not article-indexed)
- **STJ** — all endpoints return 403; would need browser automation
  (Playwright/Selenium) to access the jurisprudence search at
  scon.stj.jus.br. Not worth the fragility for now.
- ~~**TST**~~ — completed (2026-04-16) via Playwright. 463 súmulas
  in `sumulas_tst.yaml`. Resolved via `STST<number>` in cite.py.
- No free annotated CPC/CPP/CP/CLT/LIA exists in any scrapeable form

## Repo quality improvements

Work items to increase the repo's value as an LLM reference for
Brazilian institutions. Ordered by estimated impact.

### 1. Expand `glossario.md` — common confusions (~30 min)

Add entries for terms that trip up non-specialists. Currently covers
basics but misses:

- [ ] *competência absoluta* vs *relativa*
- [ ] *prescrição* vs *decadência*
- [ ] *litispendência* vs *coisa julgada*
- [ ] *tutela provisória* vs *tutela antecipada* vs *tutela cautelar*
- [ ] *agravo de instrumento* vs *agravo interno*
- [ ] *recurso ordinário* vs *recurso especial* vs *recurso extraordinário*
- [ ] *inquérito civil* vs *inquérito policial*
- [ ] *ação civil pública* vs *ação popular* vs *ação de improbidade*
- [ ] *servidor público* vs *empregado público* vs *agente político*
- [ ] *autarquia* vs *fundação* vs *empresa pública* vs *sociedade de economia mista*
- [ ] *foro* vs *vara* vs *comarca* vs *seção judiciária*
- [ ] *entrância* vs *instância*

### 2. Expand `pitfalls.md` — researcher traps (~30 min)

Common mistakes in empirical work on Brazilian institutions:

- [ ] Don't compare pre/post-2017 labor court filings without cost-regime adjustment (Lei 13.467 + ADI 5766)
- [ ] TCE rejection ≠ judicial finding of improbidade (different proceedings, different standards)
- [ ] Execução fiscal volume distorts aggregate court statistics (34% of pending cases)
- [ ] Post-2024 CNJ congestion-rate improvements are driven by Res. 547/2024 mass extinctions, not genuine efficiency
- [ ] Pre-2020 vs post-2020 proportional elections differ structurally (coligações banned by EC 97/2017)
- [ ] "Conviction rate" must specify which regime (criminal, improbidade, administrative, electoral)
- [ ] CF article counts from Justiça em Números changed methodology across years
- [ ] Pre-2012 vs post-2012 data availability differs dramatically (LAI effective May 2012)

### 3. Cross-cutting flow narratives (~1 hour)

Two new files in `topics/` that walk through complete institutional
flows, connecting multiple topical files:

- [ ] `topics/fluxo-corrupcao-municipal.md` — life cycle of a municipal
  corruption case: irregularity → CGU audit → TCE parecer → MP
  inquérito civil → ACP (improbidade) → sentença → appeal → Ficha
  Limpa ineligibility. References: cgu-controle-interno.md,
  tribunais-contas.md, ministerio-publico.md, improbidade.md,
  contas-municipais.md, processo-civil.md.

- [ ] `topics/fluxo-transferencia-federal.md` — how a federal transfer
  becomes a municipal expenditure: FPM/SUS allocation → municipal
  budget (LOA) → licitação → contract → execution → TCE audit → LRF
  reporting. References: federalismo-fiscal.md, licitacoes.md,
  tribunais-contas.md, contas-municipais.md.

### 4. `siglas.md` audit (~15 min)

Grep all acronyms used in topical files and verify each appears in
siglas.md. Quick automated check:
```bash
grep -ohP '\b[A-Z]{2,}\b' topics/*.md | sort | uniq -c | sort -rn | head -40
```
Compare against siglas.md entries.

### 5. CLAUDE.md "how to use" block (~10 min)

Add a 5-line quick-start block at the top of CLAUDE.md for cold-start
agents: "If you need to answer a question about Brazilian institutions,
(1) grep siglas.md for acronyms, (2) check glossario.md for terms,
(3) read the topical file, (4) use cite.py for statute/case detail."

### 6. `quasi-experimentos.md` expansion (~30 min)

Catalog more RD/DiD/IV designs from the Brazilian institutions
literature beyond what's already there. Each entry: design, source of
variation, key paper, relevant topical file.

## Audit progress

Checklist for the topical-file audit pass (CLAUDE.md rules 1–9).
Mark each file `[x]` after its audit commit lands. Order is
suggested priority (most CF/LRF citations first), not mandatory.

- [x] `topics/contas-municipais.md` — audited (2026-04-16), rules 1–9 complete
- [x] `topics/improbidade.md` — audited (2026-04-16), rules 1–9 complete
- [x] `topics/federalismo-fiscal.md` — audited (2026-04-16), rules 1–9 complete
- [x] `topics/tribunais-contas.md` — audited (2026-04-16), rules 1–9 complete
- [x] `topics/ministerio-publico.md` — audited (2026-04-16), rules 1–9 complete
- [x] `topics/licitacoes.md` — audited (2026-04-16), rules 1–9 complete
- [x] `topics/anticorrupcao-penal.md` — audited (2026-04-16), rules 1–9 complete
- [x] `topics/procedimentos-legais.md` — audited (2026-04-16), rules 1–9 complete
- [x] `topics/prestacao-contas-eleitorais.md` — stub (27 lines), no actionable conversions
- [x] `topics/processo-eleitoral.md` — audited (2026-04-16), rules 1–9 complete
- [x] `topics/partidos-e-sistema-eleitoral.md` — audited (2026-04-16), rules 1–9 complete
- [x] `topics/justica-eleitoral.md` — audited (2026-04-16), raw notes, 1 citation converted
- [x] `topics/transparencia-dados.md` — audited (2026-04-16), rules 1–9 complete
- [x] `topics/cgu-controle-interno.md` — audited (2026-04-16), rules 1–9 complete
- [x] `topics/cnj-administracao-judicial.md` — audited (2026-04-16), rules 1–9 complete
- [x] `topics/cortes-superiores.md` — audited (2026-04-16), raw notes, no changes
- [x] `topics/justica-federal.md` — audited (2026-04-16), raw notes, no changes
- [x] `topics/justica-estadual.md` — audited (2026-04-16), raw notes, no changes
- [x] `topics/justica-trabalho.md` — audited (2026-04-16), rules 1–9 complete
- [x] `topics/juizes.md` — audited (2026-04-16), raw notes, no changes
- [x] `topics/carreira-juizes.md` — audited (2026-04-16), raw notes, no changes
- [x] `topics/funcoes-essenciais.md` — audited (2026-04-16), raw notes, no changes
- [x] `topics/processo-civil.md` — audited (2026-04-16), raw notes, no changes
- [x] `topics/processo-penal.md` — audited (2026-04-16), raw notes, no changes
- [x] `topics/reformas-judiciais.md` — audited (2026-04-16), raw notes, no changes
- [x] `topics/organizacao-historica.md` — audited (2026-04-16), raw notes, no changes

## Conventions reminders

- Cases added to `jurisprudencia_index.yaml` need: canonical key,
  `tipo`, `numero`, `processo`, `aliases`, `relator`, `decidido`,
  `tema`, `status`, `holding_short`, `discussed_in`, `related_leis`,
  `supera`/`superado_por`, `fonte`. See existing entries for shape.
- Laws added to `leis_index.yaml` need: apelido, fonte_id, status,
  url, key articles, topics, files where discussed.
- After adding any case or law, sweep the topical files that mention
  it to convert prose attribution to backtick form, then verify with
  `python3 tools/leis_artigos/cite.py --find-in topics/X.md`.

## How to add to this list

When you finish a piece of work that uncovers a new follow-up:

1. Add an entry under the appropriate section above.
2. If the follow-up belongs at a specific point in a topical file,
   also add an inline `<!-- TODO: ... -->` comment there.
3. Remove the entry from this file when the work is done.
