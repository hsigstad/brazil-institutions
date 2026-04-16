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

## Annotated legislation — scraping project

The TSE Código Eleitoral Anotado is freely available with clean,
scrapeable HTML linking each CE article to TSE acórdãos, resoluções,
and CF cross-references. Worth scraping into a structured DB so that
`cite.py 'CE.35'` can optionally show the jurisprudence annotations.

**Target**: <https://www.tse.jus.br/legislacao/codigo-eleitoral/codigo-eleitoral-1/codigo-eleitoral-lei-nb0-4.737-de-15-de-julho-de-1965>

**HTML structure** (confirmed by inspection):
- Article text: `<p class="texto-corrido">`
- Annotations: `<ul><li class="marcador-quadrado">` or
  `<ul class="marcadorTicado"><li>`
- Citation patterns: `Ac.-TSE nº XXXXX/YYYY`, `Res.-TSE nº XXXXX/YYYY`,
  `CF/1988, art. X`, `Lei nº X/YYYY, art. Z`

**Proposed architecture**:
```
tools/tse_scraper/
├── scrape_ce_anotado.py    # scraper
├── ce_anotado.db           # SQLite: ~600 rows (200 arts × ~3 annotations)
└── README.md
```

**DB schema**:
```sql
CREATE TABLE anotacao (
    lei TEXT,           -- 'CE'
    artigo INTEGER,     -- 22, 35
    alinea TEXT,        -- 'a', 'b', NULL
    tipo TEXT,          -- 'acordao', 'resolucao', 'cf', 'lei', 'lc'
    referencia TEXT,    -- 'Ac.-TSE 23291/2004'
    texto TEXT          -- full annotation text
);
```

**Integration**: extend `cite.py` with `--annotations` flag to show
jurisprudence cross-references alongside article text. Small DB,
high value — turns CE lookups from "what does the article say?" to
"what does the article say and how has TSE interpreted it?"

**Other candidates** (lower priority, harder to scrape):
- TSE SNE (8 thematic PDFs — would need PDF extraction)
- Dizer o Direito blog (unstructured blog posts, not article-indexed)
- No free annotated CF/CPC/CPP/CP/CLT/LIA exists

Effort: ~2–3 hours for scraper + DB + cite.py integration.

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
