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

## How to navigate

**Always start with the indices**, not the topical files. The
indices are designed to surface the right topical file in one grep:

| Index | When to use |
|---|---|
| [`siglas.md`](siglas.md) | You hit an unfamiliar acronym (CGU, MPF, FPM, NTEP, FEFC, RGPS, etc.) — get full name + one-line function + pointer to the topical file |
| [`glossario.md`](glossario.md) | You hit a Portuguese legal term you might be misreading (*acórdão*, *súmula vinculante*, *prevenção*, *parecer prévio*, *contas de governo* vs *gestão*) |
| [`leis_index.yaml`](leis_index.yaml) | You need metadata about a specific law (status: vigente / parcialmente revogada / revogada; key articles; topics; files where discussed). Bridges to article-level law databases when available. |
| [`jurisprudencia-stf.md`](jurisprudencia-stf.md) | You need the canonical description of an STF case (Tema 157, Tema 1199, ADI 4650, ADI 5766, ADPF 982, HC 126.292, etc.) — described once here, cross-referenced from topical files |
| [`README.md`](README.md) | The full topical file index, organized by section |

After consulting an index, **read the relevant topical file** for the
substantive answer.

## Grep conventions

Files are designed for grep-first reading. Useful patterns:

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

## Citing statutes — the canonical bracket form

This repository uses a canonical citation format that is designed to
**resolve directly against an article-level law database** (currently
in development under `tools/leis_artigos/`, with the database file
shipped separately). Following the format consistently is the contract
between the prose reference and the lookup tool.

### Form

```
[[apelido Art. N path :modifier]]
```

- **Double brackets** distinguish resolvable citations from inline
  prose mentions and from regular markdown link syntax `[text](url)`.
- **Inside the brackets**: identifier, optional article, optional
  path, optional vintage modifier — separated by single spaces.

### Identifier

- **Cataloged laws** use the apelido from `leis_index.yaml`. Currently
  cataloged: `LIA` (Lei 8.429/1992), `L8666` (Lei 8.666/1993),
  `L14133` (Lei 14.133/2021), `LE` (Lei 9.504/1997). New apelidos are
  added as the database grows.
- **Non-cataloged laws** use the long form: `Lei 13.709/2018`,
  `LC 64/1990`, `CF`, `CP`, `CPP`, `CLT`, etc. Same bracketed
  structure; same `Art. N path` syntax inside; just doesn't resolve
  via the lookup tool until cataloged.
- **Whole laws by canonical id** use the `fonte_id` form from the
  database: `L14230-2021`, `LC219-2025`, `EC45-2004`, `DL2848-1940`.

### Article and path

- `Art. N` for plain article number (e.g., `Art. 9`).
- `Art. N-X` for articles with letters (e.g., `Art. 17-A`).
- `path` follows the structural-path convention used by the database:
  `caput`, `II`, `II.a`, `§1`, `§1.II`, `§1.II.a`, `§unico`, `ementa`.
  See `tools/leis_artigos/PATH_CONVENTION.md` for the full grammar
  once the tool is in place.

### Vintage modifiers (optional)

| Modifier | Meaning | Maps to |
|---|---|---|
| (none) | Currently in force | `vigente_ate IS NULL` |
| `@YYYY-MM-DD` | Version in force on this date | `vigente_desde <= date AND (vigente_ate IS NULL OR date < vigente_ate)` |
| `from:fonte_id` | Version introduced by a specific source | `fonte_id = X` |
| `:original` | The first-published version | min(`vigente_desde`) for that path |
| `:current` | Explicit "currently in force" (same as no modifier) | `vigente_ate IS NULL` |

### Examples

```
[[LIA Art. 9]]                          ← whole article, all current paths
[[LIA Art. 9 §1.II]]                    ← specific leaf, current
[[LIA Art. 17-A caput]]                 ← article with letter
[[LIA Art. 11 §unico @2020-06-01]]      ← what § único said in mid-2020
[[LE Art. 11 §10 @2024-12-31]]          ← § 10 before LC 219/2025 revoked it
[[LIA Art. 10 from:L14230-2021]]        ← Art. 10 as rewritten by the 2021 reform
[[LIA Art. 10 :original]]               ← original 1992 wording
[[LIA ementa]]                          ← the law's preamble
[[LIA]]                                 ← refer to the law as a whole
[[L14230-2021]]                         ← refer to a non-cataloged amending law
[[Lei 13.709/2018 Art. 7]]              ← long form for non-cataloged law
[[CF Art. 31 §2]]                       ← long form for the constitution
```

### Citing amendment events

The database has a separate `amendment` table for tracking which
amending lei touched which clause, but **citations don't need a
separate amendment-event syntax**. Express the change as a combination
of leaf citations + amending-law citations:

> The 2021 reform [[L14230-2021]] rewrote [[LIA Art. 10]] and
> eliminated culposa improbidade. Pre-reform, [[LIA Art. 10 :original]]
> permitted both intentional and negligent conduct; post-reform,
> [[LIA Art. 10 from:L14230-2021]] requires proof of dolo.

When you need to query the amendment table directly (e.g., "what did
L14230-2021 touch?"), use the lookup tool with `--by-amending`
flag — but the prose stays in leaf-citation form.

### When to use the bracket form vs prose mention

- **Use the bracket form** when you want a *resolvable* citation —
  one that points to a specific row (or query) in the database. This
  is most useful when discussing a specific clause's text, comparing
  versions, or anchoring a claim to the precise statutory language.
- **Use prose mention** ("Lei 8.429/1992 Art. 9", "the 2021 reform")
  for narrative references that don't need to resolve to a specific
  database row.
- **Both styles can coexist in the same paragraph.** The bracket form
  is opt-in; existing topical files mostly use prose mentions and
  that's fine.

### Migration policy

- Don't sweep existing files to convert prose mentions to bracket
  form. That's high-effort and low-value.
- When you *touch* a topical file for other reasons, you may
  opportunistically convert the most prominent statutory anchors to
  bracket form — particularly for the four cataloged laws.
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

## When you make changes

- **Preserve the conventions**. Each topical file opens with: scope
  paragraph → `Topics / keywords` line → `Snapshot as of YYYY` →
  scope and cross-references → topical content → cross-references at
  bottom.
- **Cite sources inline.** New claims need a statute reference, a
  CNJ/CNMP resolution number, or a published source. Format like
  existing files: `Lei 8.666/93 Art. 23`, `STF Tema 157`, `CNJ Res.
  185/2013`.
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
- **Don't paste verbatim statute text.** Files should be explanatory
  notes and summaries, not statute copies. Link to planalto.gov.br
  for the actual text.
- **Don't add unsourced empirical findings** from in-progress research
  projects, personal communications, or unpublished work. The
  audience is public. If a claim isn't verifiable against a public
  source, leave it out or generalize it.

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
<https://github.com/hsigstad/brazil-institutions-reference>. It is
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
