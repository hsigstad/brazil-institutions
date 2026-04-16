# TODO

Open follow-ups for the reference repository. Contributions welcome
for any item — see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Annotated legislation — future scraping candidates

The TSE CE Anotado and STF CF Anotada are already scraped (see
`tools/tse_ce_anotado/` and `tools/stf_constituicao/`). Remaining
candidates:

- **STJ** — all endpoints return 403; would need browser automation
  (Playwright/Selenium). Not worth the fragility for now.
- **TSE SNE** — 8 thematic PDFs systematizing electoral norms. Would
  need PDF extraction.
- No free annotated CPC/CPP/CP/CLT/LIA exists in any scrapeable form.

## Topical areas not yet covered

The repo covers courts, elections, corruption, and fiscal federalism
in depth. Areas that would benefit from a topical file but are not
yet covered:

- **Previdência social / INSS** — social security litigation is >50%
  of federal court caseload.
- **Direito do consumidor / CDC** — consumer law drives a large share
  of state-court cases.
- **Direito ambiental** — environmental law, IBAMA, licensing.
- **Direito tributário** — tax procedure beyond what's in
  `federalismo-fiscal.md`.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for how to add a new topical
file.

## Operational baselines to add

These would strengthen the topical files with quantitative context
from public sources:

- [ ] **Improbidade base rates** — filing rates per year, conviction
  rates, average case duration, sanction distribution by LIA category.
  Sources: CNJ Painéis (improbidade dashboard), published literature.
- [ ] **TCE rejection rates** — what fraction of parecer prévio
  recommendations are rejection vs approval, by state? How often does
  the câmara override? Sources: TCE annual reports, published
  literature.
- [ ] **Labor court filing drop** — quantify the post-Nov-2017 filing
  decline and the post-ADI-5766 partial recovery. Source: TST
  statistics portal.

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
