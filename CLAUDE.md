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
