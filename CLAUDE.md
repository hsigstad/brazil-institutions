# CLAUDE.md — agent guide for this repository

You are working in a reference directory on Brazilian legal and
political institutions. This file is the entry point for Claude Code
and similar agents. **Read this once at session start; then grep the
indices below before reading topical files.**

## What this is and isn't

- **Is**: a topical reference compiled for empirical research on
  Brazilian institutions. Courts, procedure, MP, fiscal federalism,
  elections, procurement, corruption statutes. Notes are dense enough
  to inform research design but not exhaustive.
- **Is not**: an authoritative legal treatise, current binding law,
  or a substitute for reading the statute. Most claims cite a statute
  or jurisprudence inline; verify against the primary source for
  legally-current work.

## Repository layout

The repository is organized into two flat tiers:

- **Root**: meta files (`CLAUDE.md`, `README.md`, `CONTRIBUTING.md`,
  `LICENSE`), navigation indices (`siglas.md`, `glossario.md`,
  `jurisprudencia-stf.md`, `faq.md`, `pitfalls.md`, `timeline.md`,
  `quasi-experimentos.md`, `data_pointers.md`), and YAML data indices
  (`leis_index.yaml`, `jurisprudencia_index.yaml`,
  `sumulas_vinculantes.yaml`, `sumulas_tse.yaml`).
- **`topics/`**: all 26 topical files (one per institution / area).
  Cross-references between topical files are bare filenames
  (`licitacoes.md`, not `topics/licitacoes.md`) because they're
  siblings inside `topics/`. References from a topical file *out* to
  the root use `../` (e.g., `../jurisprudencia-stf.md`,
  `../tools/leis_artigos/`).
- **`tools/`**: scrapers, parsers, and the citation resolver.

This split keeps `ls` at the root readable and matches the load-bearing
distinction between *indices* (grep first) and *topics* (read second).

## How to navigate

**Always start with the indices**, not the topical files. The
indices are designed to surface the right topical file in one grep:

| Index | When to use |
|---|---|
| [`siglas.md`](siglas.md) | You hit an unfamiliar acronym (CGU, MPF, FPM, NTEP, FEFC, RGPS, etc.) — get full name + one-line function + pointer to the topical file |
| [`glossario.md`](glossario.md) | You hit a Portuguese legal term you might be misreading (*acórdão*, *súmula vinculante*, *prevenção*, *parecer prévio*, *contas de governo* vs *gestão*) |
| [`leis_index.yaml`](leis_index.yaml) | You need metadata about a specific law (status: vigente / parcialmente revogada / revogada; key articles; topics; files where discussed). Bridges to article-level law databases when available. |
| [`jurisprudencia-stf.md`](jurisprudencia-stf.md) | You need the canonical description of an STF case (Tema 157, Tema 1199, ADI 4650, ADI 5766, ADPF 982, HC 126.292, etc.) — described once here, cross-referenced from topical files |
| [`jurisprudencia_index.yaml`](jurisprudencia_index.yaml) | You need structured metadata about a case: status (vigente / superada / parcialmente_superada / modulada), supersession chain, theme, files where discussed. Resolvable via ``Tema1199``-style citations through `cite.py`. |
| [`sumulas_vinculantes.yaml`](sumulas_vinculantes.yaml) | You need the verbatim text of an STF Súmula Vinculante (all 63, scraped from the STF portal). Resolvable via ``SV14``-style citations through `cite.py`. |
| [`sumulas_tse.yaml`](sumulas_tse.yaml) | You need the verbatim text of a TSE Súmula (all 72, scraped from the TSE portal). Resolvable via ``STSE38``-style citations through `cite.py`. |
| [`README.md`](README.md) | The full topical file index, organized by section |

After consulting an index, **read the relevant topical file** for the
substantive answer.

## Grep conventions

Files are designed for grep-first reading. Useful patterns:

- **Topical content**: search `topics/*.md` (or `topics/` recursively).
  All 26 substantive files live here as siblings.
- **Indices**: search at the root (`*.md` excluding `topics/`) for
  acronyms, glossary terms, STF cases, FAQ entries, and timeline
  anchors.
- **Statute citations**: search `Lei \d+/\d+` (e.g., `Lei 8.666/93`),
  `LC \d+`, `CF Art\. \d+`, `STF Tema \d+`, `ADI \d+`, `HC \d+`. These
  appear inline at the point of assertion.
- **Acronyms**: most appear in `siglas.md` first; topical files
  define acronyms on first use, then use the bare acronym thereafter.
- **Topic keywords**: each topical file has a `Topics / keywords` line
  near the top with both Portuguese and English terms. Search
  bilingually — "bid rigging" won't hit, but `cartel` and `licitação`
  will.
- **Snapshot dates**: each topical file has a `Snapshot as of YYYY`
  note. Time-volatile claims (monetary thresholds, lists of
  municipalities, current officeholders) are flagged with "as of YYYY"
  inline. Treat anything without a date as durable; treat anything
  with a date as needing verification before being cited as current.

## Citing statutes — the canonical compact form

This repository uses a canonical citation format that is designed to
**resolve directly against an article-level law database** under
`tools/leis_artigos/` (database file shipped separately). Following
the format consistently is the contract between the prose reference
and the lookup tool.

The format is intentionally compact: most citations are 5–15
characters between the backticks.

### Form

Citations are wrapped in single backticks so they render as inline
code (monospace) on github.com and remain a single, distinctive
greppable token:

```
`<identifier>.<artigo>[-<letra>][.<path>][<modifier>]`
```

- **Single backticks** wrap every resolvable citation. The contract
  for the resolver is "inline-code spans whose contents start with a
  known apelido or fonte_id"; non-citation inline code (file paths,
  function names, ordinary technical strings) is silently ignored
  by the parser. The apelido catalog in `leis_index.yaml` is the
  source of truth for what counts as a citation.
- **Dot is the universal separator** between identifier, article,
  and path. The hyphen is reserved for article letters
  (e.g., `17-A`), so paths and article letters never collide.
- **Most parts are optional** — citing just the law (`LIA`) or
  just the article (`LIA.9`) is valid.

### Identifier

- **Cataloged laws** use the apelido from `leis_index.yaml`. Currently
  cataloged: `LIA` (Lei 8.429/1992), `L8666` (Lei 8.666/1993),
  `L14133` (Lei 14.133/2021), `LE` (Lei 9.504/1997). New apelidos are
  added as the database grows.
- **Non-cataloged laws** use the canonical fonte_id form from the
  database: `L<numero>-<ano>` for leis (`L13709-2018`),
  `LC<numero>-<ano>` for leis complementares (`LC64-1990`),
  `EC<numero>-<ano>` for emendas constitucionais (`EC97-2017`),
  `DL<numero>-<ano>` for decretos-lei (`DL2848-1940`).
- **Conventional abbreviations** for codes and the constitution:
  `CF`, `CP`, `CPP`, `CLT`, `CTN`. These are not cataloged as
  separate fonte_ids but follow the same syntax.

### Article and path

- `<artigo>` is the article number. Plain integer (`9`, `145`).
- `<letra>` (optional) is an article letter, separated by hyphen
  (`17-A`, `21-B`).
- `<path>` (optional) follows the structural-path convention used by
  the database: `caput`, `II`, `II.a`, `§1`, `§1.II`, `§1.II.a`,
  `§unico`, `ementa`. See `tools/leis_artigos/PATH_CONVENTION.md`
  for the full grammar once the tool is in place.
- The article and path are separated by a dot, as is anything inside
  the path.

### Vintage modifiers (optional)

| Modifier | Meaning | Maps to |
|---|---|---|
| (none) | Currently in force | `vigente_ate IS NULL` |
| `@YYYY-MM-DD` | Version in force on this date | `vigente_desde <= date AND (vigente_ate IS NULL OR date < vigente_ate)` |
| ` from:fonte_id` | Version introduced by a specific source | `fonte_id = X` |
| `:original` | The first-published version | min(`vigente_desde`) for that path |
| `:current` | Explicit "currently in force" (same as no modifier) | `vigente_ate IS NULL` |

The `@date` and `:original`/`:current` modifiers are appended directly
with no space. The `from:` modifier requires a leading space because
the source identifier itself contains a hyphen.

### Examples

```
`LIA.9`                          ← whole article, all current paths
`LIA.9.§1.II`                    ← specific leaf, current
`LIA.17-A`                       ← article with letter
`LIA.17-A.caput`                 ← caput of Art. 17-A
`LIA.17-A.§1.II.a`               ← alínea a of inciso II of § 1 of Art. 17-A
`LE.28.§1`                       ← § 1 of Art. 28 of Lei das Eleições
`LE.11.§10@2024-12-31`           ← § 10 before LC 219/2025 revoked it
`L14133.75.II`                   ← inciso II of Art. 75 of Nova Lei de Licitações
`L13709-2018.7`                  ← Art. 7 of Lei 13.709/2018 (LGPD; non-cataloged)
`LI.1.I.g`                       ← Lei das Inelegibilidades Art. 1 I g (Ficha Limpa contas)
`CF.31.§2`                       ← Constituição Art. 31 § 2
`CP.312`                         ← Código Penal Art. 312
`LIA.11.§unico@2020-06-01`       ← what § único said in mid-2020
`LIA.10 from:L14230-2021`        ← Art. 10 as rewritten by the 2021 reform
`LIA.10:original`                ← original 1992 wording of Art. 10
`LIA.ementa`                     ← the law's preamble
`LIA`                            ← refer to the law as a whole
`L14230-2021`                    ← refer to a non-cataloged amending law as an entity
```

### Citing amendment events

The database has a separate `amendment` table for tracking which
amending lei touched which clause, but **citations don't need a
separate amendment-event syntax**. Express the change as a combination
of leaf citations + amending-law citations:

> The 2021 reform `L14230-2021` rewrote `LIA.10` and eliminated
> culposa improbidade. Pre-reform, `LIA.10:original` permitted both
> intentional and negligent conduct; post-reform,
> `LIA.10 from:L14230-2021` requires proof of dolo.

When you need to query the amendment table directly (e.g., "what did
L14230-2021 touch?"), use the lookup tool with `--by-amending`
flag — but the prose stays in leaf-citation form.

### When to use the backtick form vs prose mention

- **Use the backtick form** when you want a *resolvable* citation —
  one that points to a specific row (or query) in the database. This
  is most useful when discussing a specific clause's text, comparing
  versions, or anchoring a claim to the precise statutory language.
- **Use prose mention** ("Lei 8.429/1992 Art. 9", "the 2021 reform")
  for narrative references that don't need to resolve to a specific
  database row.
- **Both styles can coexist in the same paragraph.** The backtick form
  is opt-in; existing topical files mostly use prose mentions and
  that's fine.

### Migration policy

- Don't sweep existing files to convert prose mentions to backtick
  form. That's high-effort and low-value.
- When you *touch* a topical file for other reasons, you may
  opportunistically convert the most prominent statutory anchors to
  backtick form — particularly for the four cataloged laws.
- When a new law gets cataloged, its apelido is added to
  `leis_index.yaml` and topical files can reference it with the new
  apelido.

### Apelido naming policy

- Apelidos are short, distinct, and assigned in `leis_index.yaml`.
- For most ordinary leis, the apelido is `L<numero>` (e.g., `L8666`,
  `L14133`).
- For laws with a widely-known acronym, the acronym is preferred
  (e.g., `LIA` for Lei de Improbidade Administrativa, `LE` for Lei
  Eleitoral, `LRF` for Lei de Responsabilidade Fiscal, `LAI`,
  `LGPD`).
- For ambiguity (`CC` could be Código Civil 2002 or Código Comercial
  1850), the first cataloged law gets the apelido and conflicts are
  resolved with a year suffix (`CC2002`, `CC1850`).

## Citing jurisprudência — backtick form for cases

The same backtick grammar also accepts STF (and selected STJ) case
identifiers. These resolve against
[`jurisprudencia_index.yaml`](jurisprudencia_index.yaml) via the same
`cite.py` tool used for statutes.

### Form

```
`<case-id>`
```

`<case-id>` is the case's classe prefix concatenated with its number,
no spaces, no dots:

```
`Tema1199`      ← repercussão geral Tema 1199
`Tema157`       ← repercussão geral Tema 157
`ADI4650`       ← ADI 4650
`ADC43`         ← ADC 43 (compound — also covers ADC 44 and 54 via aliases)
`ADPF982`       ← ADPF 982
`HC126292`      ← HC 126.292
`ARE652777`     ← ARE 652.777
`ARE843989`     ← alias for Tema 1199; resolves to the same entry
```

Recognized prefixes: `Tema`, `ADI`, `ADC`, `ADPF`, `ADO`, `RE`, `ARE`,
`AI`, `HC`, `RHC`, `MS`, `RMS`, `MI`, `MC`, `Rcl`, `Pet`, `Inq`, `AP`,
`AR`, `ACO`. A second pattern accepts compound named keys ending in a
4-digit year (e.g., `LulaMoro2021`) for joint-trial entries that don't
fit the prefix grammar.

### What lookup returns

Each entry in the YAML index carries:

- **id, tipo, processo / processos, aliases** — identification
- **decidido, relator, votacao, tese_certificada** — provenance
- **tema, holding_short** — what the case is about
- **status** — `vigente`, `superada`, `parcialmente_superada`,
  `modulada`. Always check this before relying on a case as good law.
- **supera, superado_por, complementa, complementado_por** —
  supersession and complementarity chains. Lets you trace whether a
  citation has been overruled (e.g., `HC126292` has
  `superado_por: ADC43`).
- **discussed_in, related_leis** — cross-references to topical files
  and to `leis_index.yaml` apelidos.
- **fonte** — link to the STF portal or other authoritative source.

### When to use backtick form vs prose mention

Same policy as for statute citations:

- **Use the backtick form** when you want a *resolvable* citation —
  one that points to a structured entry, particularly when you want to
  signal "still good law" or anchor a claim to the canonical case.
- **Use prose mention** ("Tema 1199", "the 2019 reversal of execução
  provisória") for narrative references.
- **The substantive prose description stays in
  `jurisprudencia-stf.md`.** The YAML index is metadata, not a
  duplicate of the case description.

## Citing Súmulas Vinculantes — backtick form for SVs

The backtick grammar also accepts STF Súmulas Vinculantes by number,
resolved against [`sumulas_vinculantes.yaml`](sumulas_vinculantes.yaml)
through `cite.py`. The YAML stores the **verbatim enunciado** as
published by STF, so a lookup returns the exact text — no
paraphrasing, no transcription risk.

### Form

```
`SV<number>`
```

```
`SV14`    ← acesso amplo da defesa aos elementos de prova
`SV13`    ← nepotismo
`SV37`    ← atualização monetária / honorários
`SV47`    ← natureza alimentar dos honorários
`SV9`     ← (cancelada — verifique status antes de citar)
```

### What lookup returns

- **numero** — the SV number
- **enunciado** — the verbatim text as published by STF
- **status** — `vigente`, `cancelada`, or `revogada`
- **fonte** — canonical STF portal URL
- **publicacao** — DOU/DJE date (currently null for most entries; not
  auto-extracted from the STF portal — fill by hand when known)

### Coverage and policy

- All **63** STF Súmulas Vinculantes are present (the closed set as
  of the 2026-04-09 scrape). SV 9 is the only one currently
  `cancelada`.
- Súmulas vinculantes are a closed, small, high-importance set —
  binding under CF Art. 103-A. Worth bulk collection.
- When STF cancels or revokes a SV, update the YAML entry's `status`
  field and add a `nota` line explaining the change. Do not delete the
  entry — superseded SVs remain citable for historical analysis.

## Citing Súmulas TSE — backtick form for STSE

The bracket grammar also accepts TSE (Tribunal Superior Eleitoral)
súmulas by number, resolved against [`sumulas_tse.yaml`](sumulas_tse.yaml).
TSE súmulas are non-binding (the electoral justice system has no
equivalent of súmula vinculante) but highly persuasive — TSE is the
final word on electoral law and lower electoral courts treat its
súmulas as the operational rule.

### Form

```
`STSE<number>`
```

```
`STSE38`    ← litisconsórcio passivo necessário em ações majoritárias
`STSE47`    ← inelegibilidade superveniente (RCED)
`STSE62`    ← limites do pedido pelos fatos imputados
`STSE30`    ← dissídio jurisprudencial conforme TSE
`STSE1`     ← (cancelada — verifique status antes de citar)
```

The `S` prefix mirrors `SV` (Súmula Vinculante), and the court code
follows. STJ uses `SSTJ` (see below); if we add TST, it'll use `STST`
on the same pattern.

### What lookup returns

- **numero** — the TSE súmula number
- **enunciado** — the verbatim text as published by TSE
- **status** — `vigente`, `cancelada`, `revogada`, or `alterada`
- **fonte** — canonical TSE listing URL (TSE doesn't expose stable
  per-súmula URLs, so all entries point to the listing index)

### Coverage and policy

- All **72** numbered TSE súmulas are present (scrape of 2026-04-09).
  7 are currently `cancelada` (1, 7, 8, 14, 16, 17, 21).
- TSE súmulas are bulk-collected because the set is small (~72),
  the topical surface area covered by this repo is heavy in electoral
  law, and the verbatim text is short and stable.
- **STJ súmulas** are added on demand to
  [`sumulas_stj.yaml`](sumulas_stj.yaml) and resolved via `SSTJ<number>`
  (e.g., `SSTJ359`, `SSTJ385`, `SSTJ404`). Currently 3 entries. Not
  bulk-collected — add when a topical or project file cites one.
- **TST and ordinary STF súmulas** are *not* yet collected.
  When a topical file cites one (e.g., Súmula TST 331),
  add an entry to a future `sumulas_<court>.yaml` by hand.
  The reference repo's job is making *cited* things resolvable,
  not mirroring all of Brazilian jurisprudence.
- When TSE cancels or revokes a súmula, re-run the scraper — TSE marks
  cancellations directly on the listing page, so the status flips
  automatically. Do not delete the entry — superseded súmulas remain
  citable for historical analysis.

## Citing Súmulas STJ — backtick form for SSTJ

STJ (Superior Tribunal de Justiça) súmulas are resolved against
[`sumulas_stj.yaml`](sumulas_stj.yaml). Unlike SVs (bulk-collected) and
TSE súmulas (bulk-collected), STJ súmulas are added **on demand** when
cited by a topical file or project-level `institutions.md`.

### Form

```
`SSTJ<number>`
```

```
`SSTJ359`   ← notificação pelo órgão mantenedor antes da inscrição
`SSTJ385`   ← dano moral x inscrição preexistente legítima
`SSTJ404`   ← AR dispensável na carta de comunicação
```

### What lookup returns

- **numero** — the STJ súmula number
- **enunciado** — the verbatim text as published by STJ
- **status** — `vigente`, `cancelada`, `revogada`, or `superada`
- **aprovada** — approval date (YYYY-MM-DD)
- **fonte** — canonical URL
- **nota** — cross-references and context

### Coverage and policy

- Currently **3** entries (359, 385, 404 — all consumer-credit-registry
  súmulas cited by `serasa/docs/institutions.md`).
- Add entries when a topical or project file cites an STJ súmula. Do
  not bulk-collect — STJ has ~700 súmulas and most are irrelevant.
- When adding: copy the verbatim enunciado from the STJ portal, set
  status, and include the approval date and a fonte URL.

### When to add a new case

When a topical file cites a previously-unseen STF case:

1. Add the substantive description to `jurisprudencia-stf.md` (one
   canonical entry per case).
2. Add a structured entry to `jurisprudencia_index.yaml` keyed by
   the canonical backtick-form id.
3. Set `status` honestly. If the case has been overruled, set
   `status: superada` and fill `superado_por`.
4. Cross-reference both ways: `discussed_in` in the YAML, and a
   `Cited in:` line in `jurisprudencia-stf.md`.

## What belongs in a topical file

Topical files are the substantive layer of this repository. The
indices (siglas, glossario, jurisprudencia-stf, leis_index, etc.) tell
a reader *where to look*; topical files tell them *what's there and
why it matters*.

**Audience.** The primary consumers of these files are LLM agents
(Claude) assisting with research design. Human researchers read them
too, but the writing should optimize for an agent that benefits from
density and precision, not from narrative scaffolding, worked
examples, or restating what a heading already conveys. Every sentence
should carry information the reader can't derive from the heading,
the citation, or the statute text itself.

The structure of a topical file is **emergent from
its substance**, not imposed by a template — a file has as many or as
few sections as its topic justifies. The header is mandatory; the
body is whatever the substance demands.

**Mandatory header** (in this order):

1. Title (`# Topic name`)
2. Scope paragraph: who/what/when this topic covers, plus the
   load-bearing disambiguation against neighboring files
3. `**Topics / keywords**:` line with both Portuguese and English
   search terms
4. `**Snapshot as of YYYY**:` line, optionally listing the load-bearing
   recent jurisprudence or statutory changes
5. Cross-references (`For X, see Y.md.`) to related topical files
6. Horizontal rule (`---`)

**What belongs in the body:**

- **Substantive law specific to this topic.** Structure of the
  statute, key articles, vintage-anchored citations via `cite.py`.
  Characterize what's there and explain *why it matters*; do not
  paraphrase the statute text — that's what `artigos.db` is for.
- **Jurisprudence specific to this topic.** STF/TSE/STJ cases that
  shape interpretation. Use the backtick form (`` `Tema1199` ``) when
  the case is in `jurisprudencia_index.yaml`; describe the canonical
  version once in `jurisprudencia-stf.md` and reference it from here.
- **Institutional context that isn't in any single statute.** How the
  topic works in practice — who runs it, where the discretion lives,
  what the operational rule is. This is the "ground truth" layer that
  the database can't serve.
- **Empirical facts useful for research design.** Timing, caseload
  composition, selection effects, sample-size signals, with sources.

**What does NOT belong in a topical file:**

- **Verbatim statute text.** Resolve via `cite.py`. Use a
  planalto.gov.br link as fallback when the law isn't in the catalog
  yet.
- **Generic civil/criminal/administrative procedure** that applies to
  any action of that type. **Deletion test:** if a section could be
  copy-pasted into another topic with only the topic name changed,
  it doesn't belong here — cross-reference the relevant `processo-*.md`
  instead.
- **Acronym definitions** (those live in `siglas.md`).
- **Glossary entries** for Portuguese legal terms (those live in
  `glossario.md`).
- **Speculation or unsourced empirical findings** from in-progress
  research, personal communications, or unpublished work. The
  audience is public.
- **Filler sections** that exist to satisfy a perceived template but
  don't carry substantive content for *this* topic. The right amount
  of structure is what the substance demands; no padding.

## When you make changes

- **Apply the deletion test.** Before adding a section, check whether
  its content is specific to this topic or could be copy-pasted into a
  neighboring file. If it's generic, cross-reference instead of
  duplicating.
- **Cite sources inline.** New claims need a statute reference, a
  CNJ/CNMP resolution number, or a published source. Use the backtick
  form for resolvable citations; use prose for narrative references
  ("the 2021 reform", "STF Tema 157").
- **Update the indices** when you add or remove material:
  - New statute → add to `leis_index.yaml`.
  - New STF case → add to `jurisprudencia-stf.md` (canonical
    description) and reference it from the topical file.
  - New acronym → add to `siglas.md`.
  - New Portuguese legal term that needs disambiguation → add to
    `glossario.md`.
- **Cross-reference both ways.** If you add content to one file that
  relates to another, add a "See also" pointer or inline link in
  both directions.

### When auditing an existing topical file

These rules apply when an agent (sandboxed or otherwise) is asked to
*bring an existing file into compliance* with the content rules
above. They are stricter than the rules for normal edits, because
audits run with less human oversight per change and the failure modes
are subtle.

1. **Verify every backtick citation before adding it.**
   For any new `` `LIA.10` ``, `` `Tema1199` ``, etc. you write into
   the file, run `tools/leis_artigos/cite.py 'X'` first and confirm
   it returns a row. A citation **resolves** if `cite.py` exits 0
   and prints at least one `--- <header>` / text-body pair. A
   citation **fails** if `cite.py` exits non-zero or prints
   "No rows match" — revert to prose mention. If it doesn't
   resolve, use prose mention instead — do **not** invent the
   citation, do **not** add a speculative entry to
   `jurisprudencia_index.yaml` or `leis_index.yaml`, and do **not**
   modify the YAML indices in any way during a topical audit.

2. **Audit ≠ expand scope.**
   The goal is to bring the file into compliance with the rules,
   not to add new substantive content the rules now permit. If you
   feel an audited file is missing a fact, a case, or a statute,
   leave a `<!-- TODO: consider adding X -->` comment and report it.
   Do not add the content yourself.

3. **Preserve voice; prefer terse.**
   Match the existing register: terse, citation-dense,
   research-design-framed, Portuguese where translation loses
   meaning. Do **not** rewrite content that already passes the
   rules just to use different wording. Reword only sections you
   are restructuring, fixing, or tightening per rule 8.

4. **Apply the load-bearing test alongside the deletion test.**
   The deletion test catches generic procedure that doesn't belong
   in a topical file. But before deleting any section that fails
   it, ask the second question: *does this carry a research-design
   hook?* — a ratio, a threshold, a timing fact, a selection
   effect, a structural number that matters for empirical work.
   If yes, keep it even if it looks like statute paraphrase.
   Example: `LIA.12`'s 14/12/4-year sanction structure paraphrases
   the statute, but the ratio is the load-bearing fact that
   determines which category the MP charges under, so it stays.

5. **Flag factual uncertainty; do not silently rewrite.**
   If a claim in the existing file looks wrong but you cannot
   verify it against `cite.py` (statutes), `jurisprudencia_index.yaml`
   (cases), or a primary source you can fetch, leave a
   `<!-- TODO: verify — original claim was X -->` marker and skip
   the rewrite. Do **not** rewrite from memory; do **not** delete
   on suspicion alone. The point of these files is correctness;
   silently introduced errors are worse than uncited claims.

6. **Topical audits do not modify other files** (with one
   exception). When auditing `topics/X.md`, do not edit `CLAUDE.md`,
   `README.md`, `siglas.md`, `glossario.md`, `jurisprudencia-stf.md`,
   any YAML index, or any other topical file. If you find a needed
   update elsewhere (e.g., a stub in `procedimentos-legais.md` is out
   of date, or `jurisprudencia_index.yaml` is missing a case the
   audited file references), flag it in your report and stop.
   Cross-file changes need the human to coordinate.
   **Exception:** after committing the audit, mark the file `[x]` in
   `TODO.md` §"Audit progress" — this is bookkeeping, not a
   substantive change. Include it in the same commit.

7. **One file per commit.**
   Each topical-file audit produces exactly one commit. The commit
   message names the file, summarizes which rules were applied
   (deletion test → which sections cut; verification → which
   citations checked; etc.), and lists any TODO markers added.
   Don't bundle multiple files. The user reviews each diff
   independently, and the cost of a bad audit should never exceed
   one file's worth of damage. Multiple files may be audited in a
   single session, but always commit one file before starting the
   next. Between files, verify the previous commit is clean
   (`git status` shows no uncommitted changes) before proceeding.
   Stop after 5 files or when quality visibly degrades (e.g.,
   post-edit verification shows regressions) — whichever comes
   first.

8. **Tighten prose.**
   The primary audience is an LLM agent, not a human reading for
   narrative flow. Apply these cuts:
   - **Preambles that restate the heading.** If a section heading
     says "Contas de governo vs. contas de gestão", the first
     sentence should not say "The distinction between contas de
     governo and contas de gestão matters because..." — start with
     the substance.
   - **Worked examples of a single municipality / case history**
     that illustrate a general point but don't carry a
     research-design hook. One-line mentions are fine; multi-paragraph
     narratives of how Pedralva/MG reformed its Lei Orgânica are not.
   - **Statements of the obvious for the audience.** "For empirical
     work, the legal rule is at best a noisy proxy" — an agent doing
     research design already knows this.
   - **Redundant restatement.** If a table and the surrounding prose
     say the same thing, keep whichever is more compact and cut the
     other.
   - **External links that duplicate a cataloged citation.** If `LRF`
     resolves via `cite.py`, a trailing planalto.gov.br link to the
     same law is clutter.
   The goal is to tighten each file without losing any load-bearing
   content. When in doubt whether something is redundant or
   load-bearing, keep it — false negatives (leaving clutter) are
   cheaper than false positives (deleting substance). Do not set a
   percentage-reduction target; some files are already tight and
   forcing cuts leads to substance loss.

9. **Convert prose statute references to backtick form.**
   When a file mentions a statute in prose (e.g., "LRF Arts. 19–20",
   "CF Art. 31 §2") and the backtick form resolves via `cite.py`,
   convert it (e.g., `` `LRF.19` ``, `` `CF.31.§2` ``). Run `cite.py`
   to confirm resolution before converting — do not guess. If the
   citation doesn't resolve (uncataloged law, missing article), leave
   the prose mention as-is.

These guard rails are a contract: if an audit run produces output
that breaks any of them, the audit failed and the diff should be
discarded, not partially applied.

### Audit workflow — practical steps

This section describes the concrete steps an agent should follow when
running a topical-file audit. The rules above (1–9) define *what* to
do; this section defines *how*.

1. **Pick the file.** Check `TODO.md` §"Audit progress" for the next
   unaudited file (process in the order listed). If all are marked
   done, stop. If the file is under ~50 lines, it's a stub: run
   `--find-in`, convert any citations that resolve, and move on —
   don't try to tighten a file that has nothing to tighten.

2. **Baseline check.** Run
   `python3 tools/leis_artigos/cite.py --find-in topics/X.md` to
   list every citation the file already contains and whether it
   resolves. Note any that fail — these need investigation (typo?
   uncataloged law?) but do **not** delete them.

3. **Read the file end-to-end.** Identify sections to tighten
   (rule 8), prose statute/case references to convert (rule 9),
   and content that fails the deletion test (rule 4).

4. **For each new backtick citation you write**, run
   `python3 tools/leis_artigos/cite.py '<citation>'` and confirm it
   returns a row. Do this *before* editing, not after. Calling
   `cite.py` many times per file is expected and fine (it's a local
   SQLite lookup). Do not batch or skip verification to save time.

5. **Scope check for large files.** If `--find-in` (step 2) reports
   more than ~40 prose citations to convert, prioritize the
   most-cited laws (CF, LRF, LIA, LE, CP, etc.) and leave
   low-frequency or ambiguous conversions for a second pass. Flag
   skipped conversions in the report. The goal is reliable
   conversions, not exhaustive ones.

6. **Edit the file.** Apply rules 1–9. One pass, all changes in one
   commit.

7. **Post-edit verification.** Run `--find-in` again on the edited
   file. Every citation that resolved before should still resolve;
   every new citation should resolve. If any new citation fails,
   revert that specific citation to prose (targeted edit, not a
   whole-file revert) and note the regression in the report.

8. **Commit.** One file, one commit. The commit message should
   summarize: which rules were applied, approximate line reduction,
   any TODO markers added, any cross-file issues flagged.

9. **Report.** After committing, output a structured summary:
   - **File**: `topics/X.md`
   - **Lines**: before → after (reduction %)
   - **Citations converted**: list of prose → backtick conversions
   - **Citations that didn't resolve**: list (left as prose)
   - **TODOs added**: list
   - **Cross-file issues**: anything that needs human coordination
     (missing YAML entries, stale cross-references, etc.)

## Things to avoid

- **Don't invent statute numbers, article numbers, STF case numbers,
  or dates.** If you're not sure, say so or look it up. The whole
  value of this reference depends on its citations being correct.
- **Don't conflate similar terms.** *Súmula* ≠ *súmula vinculante*.
  *Conexão* ≠ *prevenção*. *Impedimento* (objective, ex officio) ≠
  *suspeição* (subjective, party-raised). *Contas de governo* (TCE
  parecer + câmara vote) ≠ *contas de gestão* (TCE direct judgment).
  When in doubt, check `glossario.md`.
- **Don't extrapolate from one branch to another.** Procedural rules,
  case-assignment mechanics, evidentiary standards, and reform
  histories differ substantially across the Justiça Estadual,
  Federal, do Trabalho, and Eleitoral. Each has its own file.
- **Don't treat absence of a topic as a gap to fill.** Health-law
  detail, causation doctrine, and several other specialized topics
  are deliberately not in this directory because they're not
  cross-cutting enough. If a topic doesn't appear here, that's a
  signal — not an invitation to add it.
- **Don't refactor for the sake of refactoring.** The file structure
  has settled across multiple iterations; large reorganizations are
  high-cost and low-value.

## Repository setup

This repository is a standalone public reference, hosted at
<https://github.com/hsigstad/brazil-institutions>. It is
designed to be used in two modes:

1. **Standalone**: clone and use directly.
2. **Nested into a research workspace**: clone into a working
   directory and add the path to the parent repo's `.gitignore`. The
   parent repo never touches the reference; edits commit and push to
   the public repo only. This is the recommended setup for working
   on related research without risk of cross-contamination.

## Style

- **Portuguese where translation loses meaning, English otherwise.**
  Many legal terms (*improbidade*, *parecer prévio*, *recurso
  especial*) have no clean English equivalent and stay in Portuguese.
- **Terse and citation-dense, not narrative.** Bullet points with
  inline citations are preferred over flowing prose.
- **Self-contained subsections.** A reader landing on a heading via
  grep should be able to understand the section without reading the
  whole file. Define key terms in context or link to `glossario.md`.
