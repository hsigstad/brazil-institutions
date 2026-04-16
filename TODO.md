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

- **AP 937 QO** — STF Plenário, decided 2018-05-03, Rel. Min.
  Roberto Barroso. Restricted criminal foro privilegiado to crimes
  committed *during the mandate* AND *in connection with the office
  held*. Companion case to `Pet3240` (decided one week later) on the
  improbidade-civil side. Currently flagged inline in
  `topics/procedimentos-legais.md` §"Foro privilegiado".
  Effort: ~30 min (one YAML entry + one description block in
  `jurisprudencia-stf.md`).

- **ADI 2797** — STF Plenário, decided 2005-09-15, Rel. Min.
  Sepúlveda Pertence. Declared unconstitutional § 2º of CPP Art. 84
  (introduced by Lei 10.628/2002), which had attempted to create a
  foro privilegiado for improbidade actions. Reaffirmed by `Pet3240`
  in 2018. Currently flagged inline in `topics/procedimentos-legais.md`,
  `topics/improbidade.md`, and the `nota` field of `Pet3240` in
  `jurisprudencia_index.yaml`. Effort: ~30 min.

## Statute catalog — prose mentions to sweep

These laws are cataloged (apelido exists, `cite.py` resolves) but
topical files still use prose mentions that the audit pass (rule 9)
should convert:

- **LRF** — already ingested. Prose mentions remain in
  `topics/contas-municipais.md`, `topics/federalismo-fiscal.md`,
  `topics/improbidade.md`.
- **CF** — ingested (2026-04-16). All topical files use prose
  CF references; audit pass should convert where `cite.py` resolves.
- **CP** — ingested (2026-04-16). Prose mentions in
  `topics/anticorrupcao-penal.md`, `topics/processo-penal.md`.
- **CLT** — ingested (2026-04-16). Prose mentions in
  `topics/justica-trabalho.md`.
- **CTN** — ingested (2026-04-16). Prose mentions in
  `topics/federalismo-fiscal.md`.
- **EC citations** — `EC<num>-<year>` now resolves to the CF articles
  the EC amended. Audit pass can convert prose EC mentions.

## Topical files — content gaps flagged inline

- **`topics/contas-municipais.md` §4** — diffusion of open voting in
  câmaras municipais relies on ad-hoc municipal records collected by
  hand. A systematic source (e.g., a CNM or IBGE survey, an academic
  dataset) would let the section move from "illustrative examples" to
  "census of N municipalities". Flagged with inline TODO comment in
  the file. Effort: depends on whether such a dataset exists.

- **`topics/procedimentos-legais.md` §"Foro privilegiado"** — the
  state-by-state list of which auxiliary officials carry foro
  (vereadores, auditores, delegados) is currently a one-line summary
  with São Paulo as the only worked example. Worth expanding to a
  table covering at least the largest 5–10 states if the data is
  retrievable from state constitutions. Effort: ~2 hours.

## Audit progress

Checklist for the topical-file audit pass (CLAUDE.md rules 1–9).
Mark each file `[x]` after its audit commit lands. Order is
suggested priority (most CF/LRF citations first), not mandatory.

- [x] `topics/contas-municipais.md` — audited (2026-04-16), rules 1–9 complete
- [x] `topics/improbidade.md` — audited (2026-04-16), rules 1–9 complete
- [x] `topics/federalismo-fiscal.md` — audited (2026-04-16), rules 1–9 complete
- [x] `topics/tribunais-contas.md` — audited (2026-04-16), rules 1–9 complete
- [ ] `topics/ministerio-publico.md`
- [ ] `topics/licitacoes.md`
- [ ] `topics/anticorrupcao-penal.md`
- [ ] `topics/procedimentos-legais.md`
- [ ] `topics/prestacao-contas-eleitorais.md`
- [ ] `topics/processo-eleitoral.md`
- [ ] `topics/partidos-e-sistema-eleitoral.md`
- [ ] `topics/justica-eleitoral.md`
- [ ] `topics/transparencia-dados.md`
- [ ] `topics/cgu-controle-interno.md`
- [ ] `topics/cnj-administracao-judicial.md`
- [ ] `topics/cortes-superiores.md`
- [ ] `topics/justica-federal.md`
- [ ] `topics/justica-estadual.md`
- [ ] `topics/justica-trabalho.md`
- [ ] `topics/juizes.md`
- [ ] `topics/carreira-juizes.md`
- [ ] `topics/funcoes-essenciais.md`
- [ ] `topics/processo-civil.md`
- [ ] `topics/processo-penal.md`
- [ ] `topics/reformas-judiciais.md`
- [ ] `topics/organizacao-historica.md`

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
