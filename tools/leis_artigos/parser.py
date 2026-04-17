"""
Parser for Brazilian consolidated law HTML from planalto.gov.br.

# INTENT
# Convert a planalto.gov.br consolidated HTML page into a list of structured
# `Leaf` objects, one per "leaf" of the article tree (caput, paragraph, inciso,
# alínea, item). Each leaf carries its raw text, structural location (path),
# revision marker, and any amendment annotation.
#
# REASONING
# Planalto consolidated HTML uses <a name="..."> anchors with a consistent
# naming scheme that encodes the structural location, plus <strike> tags to
# mark text that has been superseded by amendments. Parsing the HTML directly
# is dramatically more reliable than regex over the stripped text — the text
# version loses the <strike> markers and the anchor names.
#
# Anchor naming convention (planalto):
#   art{N}             article N caput, original version
#   art{N}.0           article N caput, 1st revision
#   art{N}.1           article N caput, 2nd revision
#   art{N}{letter}     article N-LETTER (e.g., art10a → art 10-A)
#   art{N}p            article N parágrafo único
#   art{N}§{M}         article N, paragraph M (caput of paragraph)
#   art{N}{roman}      article N inciso (lowercase Roman)
#   art{N}§{M}{roman}  article N paragraph M inciso
#   art{N}{stuff}.0    revised version of any of the above
#
# Within an article block, lowercase Roman numerals after the article number
# are incisos. Items inside paragraphs use § followed by the paragraph number.
#
# Output paths use the strict convention in PATH_CONVENTION.md.
#
# ASSUMES
# Input is well-formed HTML scraped by planalto_scraper.py and stored in the
# `html_raw` column of the `legislacao` table. Anchor names follow the planalto
# convention. Annotations are inside <a href="..."> links to the amending law's
# planalto page.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from typing import List, Optional

from bs4 import BeautifulSoup, NavigableString, Tag


# ---------------------------------------------------------------------------
# Roman numeral handling
# ---------------------------------------------------------------------------

ROMAN_VALUES = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def is_roman(s: str) -> bool:
    """True if s is a valid uppercase Roman numeral string (loose check)."""
    if not s:
        return False
    return all(c in ROMAN_VALUES for c in s.upper())


def is_strict_roman(s: str) -> bool:
    """True if s is a CANONICAL Roman numeral (e.g., XCIX, not IC).

    Round-trips s → integer → canonical string and compares.
    """
    if not s:
        return False
    s = s.upper()
    if not all(c in ROMAN_VALUES for c in s):
        return False
    # Decode
    total = 0
    prev = 0
    for c in reversed(s):
        v = ROMAN_VALUES[c]
        if v < prev:
            total -= v
        else:
            total += v
        prev = v
    if total <= 0:
        return False
    # Re-encode and compare
    n = total
    out = ''
    for value, sym in [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
    ]:
        while n >= value:
            out += sym
            n -= value
    return out == s


def split_roman_alinea(s: str) -> tuple[Optional[str], Optional[str]]:
    """Split a lowercase letter run into (inciso_roman_uppercase, alinea_lowercase).

    The challenge: planalto anchors concatenate inciso + alínea without
    a separator (e.g., 'ig' = inciso I alínea g, 'ivc' = inciso IV alínea c,
    'iic' = inciso II alínea c). The greedy "consume all Roman digits"
    approach mis-parses 'ic' as Roman 'IC' (which isn't even canonical),
    and drops 'ig' entirely because 'g' isn't a Roman digit.

    The correct algorithm: try the longest STRICT-Roman prefix that leaves
    either nothing or a single lowercase letter (the alínea) as remainder.
    """
    if not s:
        return None, None
    s = s.lower()

    # Try the whole string as a strict Roman numeral.
    if is_strict_roman(s.upper()):
        return s.upper(), None

    # Try shrinking by one character — treat the last char as alínea.
    if len(s) >= 2 and is_strict_roman(s[:-1].upper()):
        return s[:-1].upper(), s[-1]

    return None, None


def normalize_anchor_roman(s: str) -> str:
    """Convert lowercase roman in an anchor (e.g., 'iv') to uppercase ('IV')."""
    return s.upper()


# ---------------------------------------------------------------------------
# Anchor parsing
# ---------------------------------------------------------------------------

# The anchor name encodes structural location. We parse it into components.
# Pattern (loose): art{number}{optional_letter}{optional_subscript}.{revision}
#
# Examples:
#   art1            -> article=1, sub=None, revision=None
#   art1.0          -> article=1, sub=None, revision=0
#   art10           -> article=10, sub=None, revision=None
#   art10a          -> article=10, sub='a', revision=None  (= Art. 10-A)
#   art1§1          -> article=1, sub='§1', revision=None
#   art1§1.0        -> article=1, sub='§1', revision=0
#   art9i           -> article=9, sub='i', revision=None
#   art9iv.0        -> article=9, sub='iv', revision=0
#   art10§1i        -> article=10, sub='§1i', revision=None
#   art12p          -> article=12, sub='p', revision=None  (parágrafo único)
#   ementa          -> special: the law's ementa
#   capituloi       -> special: chapter
#   capituloii      -> special: chapter

ANCHOR_RE = re.compile(
    r'^art'
    r'(?P<num>\d+)'
    r'(?P<rest>[a-z§\d]*?)'
    r'(?:\.(?P<rev>\d*))?$'   # trailing '.' (no digit) is also a revision marker
)
CAP_RE = re.compile(r'^capitulo([ivxlcdm]+)(?:-?[a-z])?$')
# Section anchors come in two flavors:
#   capitulo{cap}secao{sec}        e.g., capituloiisecaoi
#   secao{sec}{optional_letter}    e.g., secaoiia (Seção II-A)
SEC_RE = re.compile(r'^(?:capitulo[ivxlcdm]+)?secao([ivxlcdm]+)(-?[a-z])?$')
ANCHOR_EMENTA = 'ementa'


@dataclass
class AnchorParse:
    article: int                      # article number, e.g. 9
    article_letter: Optional[str]     # e.g. 'A' for art 10-A
    path: str                         # canonical path per PATH_CONVENTION.md
    revision: Optional[int]           # None, 0, 1, ... (planalto revision counter)


def parse_anchor(name: str) -> Optional[AnchorParse]:
    """Convert a planalto anchor name into structural components.

    Returns None if the anchor is not a content anchor (e.g., capitulo).
    """
    if name == ANCHOR_EMENTA:
        return AnchorParse(article=0, article_letter=None, path='ementa', revision=None)

    m = ANCHOR_RE.match(name)
    if not m:
        return None

    article = int(m.group('num'))
    rest = m.group('rest') or ''
    rev_str = m.group('rev')
    # Revision marker conventions in planalto:
    #   no marker     → original (revision=None)
    #   '.0' '.1' ... → numbered revision
    #   '.' (trailing dot, no number) → also a revision (treat as 0)
    if rev_str is None:
        revision = None
    elif rev_str == '':
        revision = 0
    else:
        revision = int(rev_str)

    # Pull off the article letter suffix if present (e.g., "a" in art10a)
    # Letter is a single lowercase letter at the START of `rest`, NOT followed
    # by another letter (which would be a Roman numeral like "iv") and NOT a
    # paragraph marker.
    article_letter = None
    if rest and rest[0].isalpha() and rest[0] not in 'ivxlcdm§p':
        # e.g., 'a' in art10a, 'b' in art10b
        article_letter = rest[0].upper()
        rest = rest[1:]

    # Special: 'p' alone means parágrafo único
    if rest == 'p':
        return AnchorParse(
            article=article,
            article_letter=article_letter,
            path='§unico',
            revision=revision,
        )

    # No suffix → it's the article caput
    if not rest:
        return AnchorParse(
            article=article,
            article_letter=article_letter,
            path='caput',
            revision=revision,
        )

    # Parse the suffix into a path
    # Suffix grammar: ('§' NUM)? ROMAN? ALINEA? ITEM?
    # We walk left to right.
    path_parts: list[str] = []
    i = 0
    s = rest

    # Optional: § + number  (or 'p' = unico, but we handled that above)
    if i < len(s) and s[i] == '§':
        i += 1
        j = i
        while j < len(s) and s[j].isdigit():
            j += 1
        if j == i:
            # § followed by something else — give up
            return None
        para_num = s[i:j]
        path_parts.append(f'§{para_num}')
        i = j

    # Optional: lowercase Roman numeral (inciso) possibly followed by an
    # alínea letter. The anchor concatenates them without a separator
    # (e.g., 'ig' = inciso I alínea g, 'ivc' = inciso IV alínea c).
    # We greedily consume any run of lowercase letters and split it into
    # (strict Roman prefix, optional single-letter alínea) using
    # split_roman_alinea.
    if i < len(s):
        j = i
        while j < len(s) and s[j].isalpha() and s[j].islower():
            j += 1
        if j > i:
            roman, alinea = split_roman_alinea(s[i:j])
            if roman is not None:
                path_parts.append(roman)
                if alinea is not None:
                    path_parts.append(alinea)
                i = j

    # Optional: arabic numeral (item) — sub-leaf within an alínea.
    if i < len(s) and s[i].isdigit():
        k = i
        while k < len(s) and s[k].isdigit():
            k += 1
        path_parts.append(s[i:k])
        i = k

    if i != len(s):
        # We didn't consume everything — log and skip for safety.
        return None

    if not path_parts:
        return None

    return AnchorParse(
        article=article,
        article_letter=article_letter,
        path='.'.join(path_parts),
        revision=revision,
    )


# ---------------------------------------------------------------------------
# Annotation extraction
# ---------------------------------------------------------------------------

# Annotations look like: (Redação dada pela Lei nº 14.230, de 2021)
#                        (Incluído pela Lei nº 14.230, de 2021)
#                        (Revogado pela Lei nº ...)
#                        (Vide Lei nº ...)
#
# We capture: kind ('redacao' | 'incluido' | 'revogado' | 'vide'),
#             lei_numero ('14230'), lei_ano ('2021'), and the URL of the
#             amending law's planalto page (if available from a nearby <a href>).

ANNOTATION_RE = re.compile(
    r'\((?P<kind>Redação dada|Incluíd[oa]|Revogad[oa]|Vide)\s*'
    r'(?:pel[oa]s?\s+)?'
    r'(?P<lei_tipo>Medida Provisória|Lei\s+Complementar|Lei|Decreto-Lei|Decreto|Emenda Constitucional)?\s*'
    r'(?:n[º°o]?\.?\s*)?'
    r'(?P<numero>[\d.]+)?'
    r'[,\s]*(?:de\s+)?'
    r'(?P<ano>\d{4})?'
    r'[^)]*\)',
    re.IGNORECASE | re.DOTALL,
)


@dataclass
class Annotation:
    kind: str            # 'redacao', 'incluido', 'revogado', 'vide'
    lei_tipo: Optional[str]   # 'Lei', 'Lei Complementar', 'Medida Provisória', etc.
    lei_numero: Optional[str]
    lei_ano: Optional[str]
    raw_text: str        # the full annotation text


def _annotation_kind(kind_raw: str) -> str:
    kind_raw = kind_raw.lower()
    if kind_raw.startswith('redação'):
        return 'redacao'
    if kind_raw.startswith('incluí'):
        return 'incluido'
    if kind_raw.startswith('revogad'):
        return 'revogado'
    if kind_raw == 'vide':
        return 'vide'
    return kind_raw


def _normalize_lei_tipo(s: Optional[str]) -> Optional[str]:
    if not s:
        return None
    s = re.sub(r'\s+', ' ', s).strip()
    # Title-case canonicalize: "lei complementar" → "Lei Complementar"
    return ' '.join(w.capitalize() if w.lower() != 'de' else 'de'
                    for w in s.split())


def parse_annotations(text: str) -> list[Annotation]:
    """Find ALL annotations in `text`, in document order.

    Some leaves have multiple annotations — e.g., a revoked parágrafo único
    that says "(Revogado)" followed by "(Redação dada pela Lei nº 14.230,
    de 2021)" to indicate WHO revoked it. We need both pieces.
    """
    out: list[Annotation] = []
    for m in ANNOTATION_RE.finditer(text):
        numero = m.group('numero')
        if numero:
            numero = numero.replace('.', '')
        ano = m.group('ano')
        # Fallback: the main regex anchors <ano> right after "de ", so it
        # fails on variants seen in planalto HTML — "de 4 de junho de
        # 2024", "de 19.1.1982", "de 10.12.97" (2-digit), "de 15/08/95:"
        # (slashes), "de1997" (no space), "de 2 019" / "de 2.010" (split
        # year from HTML whitespace glitches), "de 1º . 6 .19 7 6"
        # (extreme whitespace). Rescue by concatenating all remaining
        # digits after stripping the lei numero, then taking the last 4
        # as a 4-digit year (if 1800–2100) or the last 2 as a 2-digit
        # year (1940–1999 / 2000–2039).
        if not ano:
            text = m.group(0)
            if numero:
                if len(numero) >= 4:
                    text = text.replace(f'{numero[:-3]}.{numero[-3:]}', '', 1)
                text = text.replace(numero, '', 1)
            digits = re.sub(r'\D', '', text)
            if len(digits) >= 4 and 1800 <= int(digits[-4:]) <= 2100:
                ano = digits[-4:]
            elif len(digits) >= 2:
                yy = int(digits[-2:])
                ano = str(1900 + yy) if yy >= 40 else str(2000 + yy)
        out.append(Annotation(
            kind=_annotation_kind(m.group('kind')),
            lei_tipo=_normalize_lei_tipo(m.group('lei_tipo')),
            lei_numero=numero,
            lei_ano=ano,
            raw_text=m.group(0),
        ))
    return out


def parse_annotation(text: str) -> Optional[Annotation]:
    """Single-annotation lookup. Returns the first annotation found."""
    annotations = parse_annotations(text)
    return annotations[0] if annotations else None


def merge_annotations(annotations: list[Annotation]) -> Optional[Annotation]:
    """Combine a list of annotations into a single effective annotation.

    When a leaf has multiple annotations:
    - "(Revogado)" alone means the clause was repealed; if a "(Redação dada
      pela Lei nº X, de Y)" follows, X/Y is the revoking law.
    - "(Incluído pela Lei nº X)" means added by amendment.
    - "(Redação dada pela Lei nº X)" means the current text was set by X.
    Priority: revogado > incluido > redacao > vide.
    """
    if not annotations:
        return None

    # Revoked takes priority. Borrow lei reference from siblings if absent.
    revogados = [a for a in annotations if a.kind == 'revogado']
    if revogados:
        rev = revogados[-1]
        if rev.lei_numero is None:
            for other in annotations:
                if other.lei_numero is not None:
                    return Annotation(
                        kind='revogado',
                        lei_tipo=other.lei_tipo,
                        lei_numero=other.lei_numero,
                        lei_ano=other.lei_ano,
                        raw_text='; '.join(a.raw_text for a in annotations),
                    )
        return rev

    incluidos = [a for a in annotations if a.kind == 'incluido']
    if incluidos:
        return incluidos[-1]

    redacoes = [a for a in annotations if a.kind == 'redacao']
    if redacoes:
        return redacoes[-1]

    return annotations[-1]


# ---------------------------------------------------------------------------
# HTML walking
# ---------------------------------------------------------------------------

@dataclass
class Leaf:
    """One leaf of the article tree as extracted from the HTML."""
    article: int
    article_letter: Optional[str]
    path: str
    text: str
    is_struck: bool                       # wrapped in <strike> → superseded
    revision: Optional[int]               # planalto revision counter from anchor
    annotations: list = field(default_factory=list)  # ALL annotations on this leaf, in document order
    annotation: Optional[Annotation] = None           # merged single annotation (back-compat)
    chapter: Optional[str] = None         # roman, e.g., 'I'
    chapter_titulo: Optional[str] = None
    section: Optional[str] = None
    section_titulo: Optional[str] = None
    ordem: int = 0                        # set by walker for stable order
    raw_anchor: str = ''                  # original anchor name (for debugging)


def normalize_text(s: str) -> str:
    """Normalize whitespace in a leaf text fragment.

    Uses NFC (canonical composition) — NOT NFKC, because NFKC has
    compatibility decompositions that destroy meaningful characters like
    'º' (masculine ordinal, U+00BA → plain 'o'), which would make
    "Art. 1º" indistinguishable from "Art. 1o" and break annotation regex
    matching for "Lei nº 14.230".
    """
    s = unicodedata.normalize('NFC', s)
    # Replace non-breaking spaces with regular ones
    s = s.replace('\xa0', ' ')
    s = re.sub(r'\s+', ' ', s)
    return s.strip()


def is_struck(elem: Tag) -> bool:
    """True if `elem` or any ancestor is a <strike> tag."""
    cur = elem
    while cur is not None:
        if isinstance(cur, Tag) and cur.name in ('strike', 's'):
            return True
        cur = cur.parent
    return False


def walk_html(html: str) -> list[Leaf]:
    """Walk planalto consolidated HTML and return Leaf objects in document order.

    Strategy: find every <a name="..."> anchor that maps to a content path,
    then extract the text immediately following the anchor up to the next
    content anchor.
    """
    soup = BeautifulSoup(html, 'html.parser')

    # Track chapter/section context as we walk
    chapter: Optional[str] = None
    chapter_titulo: Optional[str] = None
    section: Optional[str] = None
    section_titulo: Optional[str] = None

    leaves: list[Leaf] = []
    ordem = 0

    # Get all anchors in document order
    anchors = soup.find_all('a', attrs={'name': True})

    for idx, anchor in enumerate(anchors):
        name = anchor.get('name', '')

        # Section anchor (check before chapter — compound names start with capitulo)
        sec_match = SEC_RE.match(name)
        if sec_match:
            sec_roman = sec_match.group(1).upper()
            sec_letter = sec_match.group(2) or ''
            sec_letter = sec_letter.replace('-', '').upper()
            section = sec_roman + (f'-{sec_letter}' if sec_letter else '')
            section_titulo = _extract_heading_title(anchor)
            # Compound anchors (capituloiisecaoi) also imply chapter; if we
            # don't have it set yet, infer from the anchor name
            if name.startswith('capitulo'):
                cap_part = name[len('capitulo'):name.index('secao')]
                if cap_part:
                    chapter = cap_part.upper()
            continue

        # Chapter heading (standalone)
        cap_match = CAP_RE.match(name)
        if cap_match:
            roman = cap_match.group(1).upper()
            chapter = roman
            section = None  # new chapter resets section
            section_titulo = None
            title = _extract_heading_title(anchor)
            chapter_titulo = title
            continue

        parsed = parse_anchor(name)
        if parsed is None:
            continue

        # Extract text from this anchor
        text, struck, annotations = _extract_leaf_from_anchor(anchor, anchors, idx)
        # Allow empty text only if there's at least one annotation (e.g.,
        # revoked clauses with no residual content).
        if not text and not annotations:
            continue

        ordem += 1
        leaves.append(Leaf(
            article=parsed.article,
            article_letter=parsed.article_letter,
            path=parsed.path,
            text=text,
            is_struck=struck,
            revision=parsed.revision,
            annotations=annotations,
            annotation=merge_annotations(annotations),
            chapter=chapter,
            chapter_titulo=chapter_titulo,
            section=section,
            section_titulo=section_titulo,
            ordem=ordem,
            raw_anchor=name,
        ))

    return leaves


def _extract_heading_title(anchor: Tag) -> Optional[str]:
    """Extract the title text following a chapter/section anchor.

    The anchor is usually inside a <p> like:
      <p><a name="capituloi"></a>CAPÍTULO I<br>Das Disposições Gerais</p>
    """
    p = anchor.find_parent('p')
    if p is None:
        return None
    text = p.get_text(' ', strip=True)
    # Strip the "CAPÍTULO X" / "Seção X" prefix to get just the title
    text = re.sub(r'^(CAPÍTULO|Seção)\s+[IVXLCDM]+(-[A-Z])?\s*', '', text, flags=re.IGNORECASE)
    return normalize_text(text) or None


def _extract_leaf_from_anchor(
    anchor: Tag,
    all_anchors: list[Tag],
    idx: int,
) -> tuple[str, bool, list[Annotation]]:
    """Extract the leaf text starting at this anchor.

    Returns (text, is_struck, annotations).
    """
    p = anchor.find_parent('p')
    if p is None:
        return '', False, []

    raw = p.get_text(' ', strip=False)
    text = normalize_text(raw)

    struck = bool(p.find('strike') or p.find('s'))

    # A leaf can have multiple annotations. We return them all and let the
    # builder decide how to interpret them.
    annotations = parse_annotations(text)
    if annotations:
        text = ANNOTATION_RE.sub('', text).strip()
        text = normalize_text(text)
        text = text.rstrip('. ').strip()

    return text, struck, annotations


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Fallback: class="Artigo" markup (no anchors)
# ---------------------------------------------------------------------------
#
# Some older planalto pages use <p class="Artigo"> tags instead of
# <a name="art..."> anchors. These are non-compilado pages without
# revision tracking or <strike> markup. Each <p class="Artigo">
# contains one structural unit whose type is determined from the text.

# Article caput pattern: "Art. 1o", "Art. 10.", "Art. 19-M"
_ART_CAPUT_RE = re.compile(
    r'^Art\.\s*(\d+)(?:-([A-Z]))?'
)
# Paragraph pattern: "§ 1o", "§ 2º", "Parágrafo único"
_PARA_RE = re.compile(
    r'^§\s*(\d+)|^Parágrafo\s+único',
    re.IGNORECASE,
)
# Inciso pattern: "I –", "II -", "XIV –"
_INCISO_RE = re.compile(
    r'^([IVXLCDM]+)\s*[–—\-]',
)
# Alínea pattern: "a)", "b)", "c)"
_ALINEA_RE = re.compile(
    r'^([a-z])\)',
)


def walk_html_artigo_class(html: str) -> list[Leaf]:
    """Fallback parser for pages using <p class="Artigo"> markup."""
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = soup.find_all('p', class_='Artigo')
    if not paragraphs:
        return []

    leaves: list[Leaf] = []
    ordem = 0
    # Current context
    cur_article: Optional[int] = None
    cur_letter: Optional[str] = None
    cur_para: Optional[str] = None   # '§1', '§unico', or None (caput)
    cur_inciso: Optional[str] = None  # 'I', 'II', etc.

    for p in paragraphs:
        raw = p.get_text(' ', strip=False)
        text = normalize_text(raw)
        if not text:
            continue

        annotations = parse_annotations(text)
        if annotations:
            text = ANNOTATION_RE.sub('', text).strip()
            text = normalize_text(text)
            text = text.rstrip('. ').strip()

        # Determine structural type from text content
        art_m = _ART_CAPUT_RE.match(text)
        para_m = _PARA_RE.match(text)
        inciso_m = _INCISO_RE.match(text)
        alinea_m = _ALINEA_RE.match(text)

        if art_m:
            cur_article = int(art_m.group(1))
            cur_letter = art_m.group(2) or None
            cur_para = None
            cur_inciso = None
            path = 'caput'
        elif para_m and cur_article is not None:
            if para_m.group(1):
                cur_para = f'§{para_m.group(1)}'
            else:
                cur_para = '§unico'
            cur_inciso = None
            path = cur_para
        elif inciso_m and cur_article is not None:
            roman = inciso_m.group(1).upper()
            if is_roman(roman):
                cur_inciso = roman
                if cur_para:
                    path = f'{cur_para}.{roman}'
                else:
                    path = roman
            else:
                continue
        elif alinea_m and cur_article is not None:
            letter = alinea_m.group(1)
            if cur_inciso:
                if cur_para:
                    path = f'{cur_para}.{cur_inciso}.{letter}'
                else:
                    path = f'{cur_inciso}.{letter}'
            elif cur_para:
                path = f'{cur_para}.{letter}'
            else:
                path = letter
        else:
            # Unrecognized structure — skip
            continue

        if cur_article is None:
            continue

        ordem += 1
        leaves.append(Leaf(
            article=cur_article,
            article_letter=cur_letter,
            path=path,
            text=text,
            is_struck=False,
            revision=None,
            annotations=annotations,
            annotation=merge_annotations(annotations),
            ordem=ordem,
            raw_anchor=f'artigo_class_{cur_article}_{path}',
        ))

    return leaves


def parse_law_html(html: str) -> list[Leaf]:
    """Parse a planalto consolidated law HTML into a list of leaves.

    Tries anchor-based parsing first; falls back to class="Artigo"
    parsing for older pages without <a name="art..."> anchors.
    """
    leaves = walk_html(html)
    if leaves:
        return leaves
    return walk_html_artigo_class(html)
