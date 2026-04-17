# AUDITING.md — rules and workflow for topical-file audits

These rules apply when an agent (sandboxed or otherwise) is asked to
*bring an existing file in `topics/` into compliance* with the
content rules in [`CLAUDE.md`](CLAUDE.md) (§"What belongs in a
topical file" and §"When you make changes"). They are stricter than
the rules for normal edits, because audits run with less human
oversight per change and the failure modes are subtle.

**These guard rails are a contract: if an audit run produces output
that breaks any of them, the audit failed and the diff should be
discarded, not partially applied.**

## Rules

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

## Workflow — practical steps

The rules above define *what* to do; this section defines *how*.

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
