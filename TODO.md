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

## Operational-reality baselines — needs data access

These items require running queries against research datasets in a
non-sandboxed session. Add results to the relevant topical files with
source citations.

- [ ] **Improbidade base rates** — from the audit-paper improbidade
  dataset: filing rates per year, MP vs entity filing share (pre-2021),
  conviction rates, average duration, sanction distribution by LIA
  category (Art. 9/10/11). Add to `topics/improbidade.md`.
- [ ] **TCE rejection rates** — from TCE-SP Audesp or contas data:
  what fraction of parecer prévio recommendations are rejection vs
  approval? How often does the câmara override? Add to
  `topics/contas-municipais.md`.
- [ ] **TJSP case-type composition** — from ESAJ data: what fraction
  of TJSP first-instance cases are execução fiscal, fazenda pública,
  improbidade, family, criminal? Add to `topics/justica-estadual.md`.
- [ ] **Labor court filing drop** — from TST data: quantify the
  post-Nov-2017 filing drop and the post-ADI-5766 partial recovery.
  Add to `topics/justica-trabalho.md`.
- [ ] **CNMP data extraction** — CNMP stopped PDF reports after 2018;
  post-2018 data is on an interactive Tableau dashboard at
  `https://www.cnmp.mp.br/portal/relatoriosbi/mp-um-retrato`.
  Visit in browser, extract IC counts, ACP counts, TAC counts by
  state, member counts by branch. The 2018 PDF (base year 2017) is at
  `https://www.cnmp.mp.br/portal/images/Publicacoes/documentos/2019/Anu%C3%A1rio_um_retrato_2018_ERRATA_1.pdf`
  but data is in image-based charts, not text-extractable.
  Add to `topics/ministerio-publico.md`.

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

All completed 2026-04-16:

- [x] Expand `glossario.md` — 12 new term-pair entries
- [x] Expand `pitfalls.md` — 6 empirical research traps
- [x] Cross-cutting flow narratives — `fluxo-corrupcao-municipal.md`
  (287 lines) and `fluxo-transferencia-federal.md` (239 lines)
- [x] `siglas.md` audit — 15 missing entries added
- [x] CLAUDE.md quick-start block — 7-line guide at top
- [x] `quasi-experimentos.md` — 4 new entries (#19–22: FUNDEB,
  judge random assignment, quinto constitucional, municipal
  emancipation)

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
