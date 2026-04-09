# Path convention for `artigo` lookups

A `path` identifies a specific leaf within an article — a piece of legal
text that has its own existence (its own amendment history, its own legal
weight). Within a single `(apelido, artigo)` tuple, every leaf has exactly
one canonical path.

This convention is used by:

- The `artigo` table of the article-level law database (`artigos.db`).
- The compact citation form documented in `../../CLAUDE.md`
  (e.g., `[[LIA.10.§1.II]]`, where `§1.II` is the path).
- `cite.py` for parsing bracket-form citations.

## Strict syntax

```
PATH := ROOT ('.' SUFFIX)*
ROOT := 'caput' | 'ementa' | 'preambulo' | INCISO | PARAGRAFO
SUFFIX := INCISO | ALINEA | ITEM
INCISO := <uppercase Roman numeral>     I, II, III, IV, V, ..., XX, XXI, ...
ALINEA := <single lowercase letter>     a, b, c, ...
ITEM   := <arabic numeral>              1, 2, 3, ...
PARAGRAFO := '§' (NUMBER | 'unico')     §1, §2, §unico
NUMBER := <arabic numeral>              1, 2, ...
```

**Separator:** dot (`.`)
**Roman numerals:** ALWAYS uppercase, never lowercase
**Alínea letters:** ALWAYS lowercase
**Items:** arabic numerals
**Paragraph marker:** `§` followed by `unico` (no accent in path) or arabic numeral

## Examples

| Path | Meaning |
|---|---|
| `caput` | The article's caput (intro text) |
| `ementa` | The law's ementa (preamble describing what the law does) |
| `I` | Inciso I directly under the article caput |
| `II` | Inciso II directly under the article caput |
| `IV` | Inciso IV directly under the article caput |
| `IX.a` | Alínea a of inciso IX |
| `IX.a.1` | Item 1 of alínea a of inciso IX |
| `§1` | The caput of § 1º (the introductory text of paragraph 1) |
| `§2` | The caput of § 2º |
| `§unico` | Parágrafo único caput |
| `§1.I` | Inciso I under § 1º |
| `§1.I.a` | Alínea a of inciso I of § 1º |
| `§1.I.a.1` | Item 1 of alínea a of inciso I of § 1º |
| `§unico.II` | Inciso II of parágrafo único |

## Disambiguation

The path encodes the **structural location**, not the literal label.
This means:

- **An inciso "I" without `§` prefix is always under the article's caput.**
  If a paragraph also has an inciso I, that's `§N.I`, never just `I`.
- **A paragraph's caput** is `§N` (no further suffix). Paragraphs are
  themselves "leaves" — § 2º has its own text even before any incisos.
- **Parágrafo único** is `§unico`, never `§1` (even if it's the only
  paragraph). Use `§unico` only when the law literally says
  "Parágrafo único.", and use `§1`, `§2`, ... when the law uses numbered
  paragraphs.
- **Caput is always `caput`**, never an empty string.

## Sorting

Paths sort lexically *almost* correctly:
- `caput` < `I` ✗ (lex says `I` < `caput`)
- `I` < `II` < `III` < ... ✓ (Roman numerals sort by length then alphabetically when length matches, except `IV`/`IX` invert)
- `§1` < `§2` ✓
- `§1.I` < `§1.II` ✓
- `§1` < `§unico` ✓ (numbered before unico)

Because lex sort is imperfect, the `artigo` table also stores an `ordem`
column that preserves the document order. Use `ORDER BY ordem` for
reconstruction; use the path columns for lookup.

## Notes on parser behavior

- The parser was updated to canonicalize alínea paths as `<Roman>.<lowercase>`
  (e.g., `I.a`, `IV.c`, `II.g`). Earlier versions of the DB stored these as
  concatenated forms (`IA`, `IVC`, `IIG` — and in some cases dropped the
  alínea entirely when its letter wasn't in `ivxlcdm`). After rebuilding,
  all alíneas are stored in canonical dotted form.
- The resolver (`cite.py`, `lookup.py`) accepts both the canonical
  dotted form and the legacy concatenated form via path normalization,
  so older citations continue to work.

## Known parser limitations (not yet fixed)

- **Sub-paragraph numbering**: laws sometimes have `§ 4º-C`, `§ 4º-D`,
  etc. (paragraphs with letter suffixes, parallel to article letters).
  The parser currently stores these as `§4.C` (dot + uppercase), which
  is not strictly canonical. PATH_CONVENTION above does not cover this
  case yet — when adding a sub-paragraph syntax, decide between
  `§4-C` (parallel to article letters), `§4.C` (current), or
  something else.
- **Duplicate caput rows**: in laws with extensive amendment histories
  (e.g., LI Art. 1), the parser sometimes emits two `caput` rows when a
  law's article structure was reorganized but the original version is
  also captured in planalto's HTML. The `vigente_desde`/`vigente_ate`
  columns disambiguate.

## Validation regex

```python
import re
PATH_RE = re.compile(
    r'^(caput|ementa|preambulo'
    r'|§(?:unico|\d+)(?:\.[IVXLCDM]+(?:\.[a-z](?:\.\d+)?)?)?'
    r'|[IVXLCDM]+(?:\.[a-z](?:\.\d+)?)?'
    r')$'
)
```

The lookup CLI uses this to validate input paths and reject typos like
`i` (lowercase Roman), `Sec1` (wrong paragraph marker), `1` (bare arabic
without context).
