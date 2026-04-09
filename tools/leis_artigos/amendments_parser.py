"""
Parse amending laws to extract which clauses they touch.

# INTENT
# An amending lei (e.g., Lei 14.230/2021) modifies clauses of a target lei
# (e.g., Lei 8.429/1992 = LIA). This module parses the amending lei's HTML
# and produces an `Amendment` per (target, artigo, path) tuple, marking the
# action ('add', 'modify', 'revoke').
#
# REASONING
# Planalto consolidated HTML for amending laws contains hyperlinks DIRECTLY
# to the target lei's anchors:
#
#   <a href="../../../LEIS/L8429.htm#art9.0">"Art. 9º</a> Constitui ato ..." (NR)
#   <a href="../../../LEIS/L8429.htm#art10xxi.0">XXI -</a> (revogado);
#   <a href="../../../LEIS/L8429.htm#art17a">"Art. 17-A</a> ...
#
# This means we can parse hyperlinks instead of doing fragile text parsing.
# The href tells us:
#   - target lei (filename, e.g., L8429.htm → numero=8429)
#   - target anchor (fragment, e.g., art9.0 → article 9, path caput, revision 0)
# The text/context tells us the action:
#   - "(revogado)" near the link → revoke
#   - "(NR)" at end of paragraph → modify (Nova Redação)
#   - new article number not in target → add
#
# ASSUMES
# Amending laws follow the standard planalto format with `<a href="..">` links
# to the target lei. Newer laws (post-2000) generally do; older ones may not.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional
from urllib.parse import urlparse, unquote

from bs4 import BeautifulSoup, Tag

# Reuse the anchor parser from the main parser module
from parser import parse_anchor, AnchorParse  # noqa: E402


# Pattern to extract target lei filename from href.
# Examples that should match:
#   ../../../LEIS/L8429.htm
#   ../LEIS/L9504.htm
#   ../../../_Ato2019-2022/2021/Lei/L14230.htm
#   LCP/Lcp64.htm
#   LCP/Lcp219.htm
#   ../LCP/Lcp64.htm
TARGET_LEI_RE = re.compile(
    r'(?:[Ll]([Cc][Pp])?(\d+)(?:-?[A-Za-z]+)?\.htm)$'
)
# Simpler: extract lei number from filename L{NNN}.htm or Lcp{NNN}.htm
LEI_FILENAME_RE = re.compile(r'(L|Lcp|LCP|LC|Mp|MP|Dl|DL|Dec|D)(\d+)\.htm$', re.IGNORECASE)


@dataclass
class Amendment:
    """One change made by an amending lei to a target lei."""
    target_filename: str           # e.g., 'L8429.htm'
    target_tipo: str               # 'L', 'LC', 'MP', 'DL', 'D'
    target_numero: str             # '8429'
    artigo: int
    artigo_letra: Optional[str]
    path: str
    action: str                    # 'add', 'modify', 'revoke'
    source_anchor: str             # the linked anchor name (e.g., 'art9.0')
    source_text: str               # text snippet around the link
    ordem: int


def _parse_target_filename(href: str) -> Optional[tuple[str, str]]:
    """Extract (tipo, numero) from a planalto href like '../LEIS/L8429.htm'.

    Returns (tipo, numero) or None if not parseable.
    Tipo is normalized: L, LC, MP, DL, D, EC.
    """
    if not href:
        return None
    # Strip the fragment and query
    parsed = urlparse(href)
    path = parsed.path
    # Get the filename
    filename = path.rsplit('/', 1)[-1]
    if not filename:
        return None

    m = LEI_FILENAME_RE.match(filename)
    if not m:
        return None

    raw_tipo = m.group(1).lower()
    numero = m.group(2)

    tipo_map = {
        'l': 'L',
        'lcp': 'LC',
        'lc': 'LC',
        'mp': 'MP',
        'dl': 'DL',
        'dec': 'D',
        'd': 'D',
    }
    tipo = tipo_map.get(raw_tipo, 'L')
    return tipo, numero


AMENDING_MARKERS = (
    '(nr)',                   # Nova Redação — modification marker
    'revogad',                # revogado/revogada/revogados/revogadas
    'passa a vigorar',        # "X passa a vigorar com a seguinte redação"
    'fica acrescid',          # "fica acrescido" / "fica acrescida"
    'ficam acrescid',
    'acrescido',
    'acrescentar',
    'introduz',               # "introduz o seguinte artigo"
    'inclui',                 # "inclui o seguinte"
    'altera',                 # "altera o art. X"
)


def _is_amending_context(link: Tag) -> bool:
    """True if the link is in a paragraph that's clearly making an amendment.

    Requires at least one amending marker in the parent paragraph's text.
    Otherwise the link is likely just a cross-reference, not an amendment.
    """
    p = link.find_parent('p')
    if p is None:
        return False
    text_lower = p.get_text(' ', strip=True).lower()
    return any(marker in text_lower for marker in AMENDING_MARKERS)


def _detect_action(link: Tag, fragment: str) -> str:
    """Determine if this amendment is add/modify/revoke based on context."""
    p = link.find_parent('p')
    context_text = p.get_text(' ', strip=True) if p else ''
    context_lower = context_text.lower()

    # Revocation: explicit "revogado"
    if 'revogad' in context_lower:
        return 'revoke'

    # Addition markers
    if any(m in context_lower for m in ('acrescid', 'acrescentar', 'incluí', 'inclui')):
        return 'add'

    # Revision marker in fragment usually means modification
    if re.search(r'\.\d+$', fragment) or fragment.endswith('.'):
        return 'modify'

    # Article with letter and no revision suffix = likely addition
    if re.match(r'^art\d+[a-z]', fragment):
        return 'add'

    return 'modify'


PASSA_A_VIGORAR_RE = re.compile(
    r'passa(?:m)?\s+a\s+vigorar',
    re.IGNORECASE,
)
FICAM_REVOGADOS_RE = re.compile(
    r'(?:ficam?\s+revogad[oa]s?|revoga(?:m)?-se)',
    re.IGNORECASE,
)
NEW_AMENDING_ART_RE = re.compile(r'^\s*Art\.\s*\d+', re.IGNORECASE)

# Pattern to extract a lei reference from text in a marker paragraph
# Matches things like:
#   "Lei nº 9.504, de 30 de setembro de 1997"
#   "Lei nº 8.429, de 1992"
#   "Lei Complementar nº 64, de 18 de maio de 1990"
LEI_TEXT_REF_RE = re.compile(
    r'(?P<tipo>Lei(?:\s+Complementar)?|Decreto(?:-Lei)?|Medida\s+Provis[óo]ria|Emenda\s+Constitucional)'
    # 'n' or 'nº' or 'n o' (when <sup> tags create spaces) — flexible spacing
    r'\s+n\s*[º°o]?\.?\s*'
    r'(?P<numero>[\d.]+)'
    r'(?:[,\s]+de\s+(?:\d{1,2}\s+de\s+\w+\s+de\s+)?(?P<ano>\d{4}))?',
    re.IGNORECASE,
)


def _extract_lei_filename_from_text(text: str) -> Optional[str]:
    """Try to extract a planalto-style filename from a textual lei reference.

    Returns 'L9504.htm', 'Lcp64.htm', etc. or None.
    """
    # Collapse internal whitespace — bs4 preserves newlines from inline tags
    # like <u><sup>o</sup></u>, so "Lei nº 9.504" can come out as "Lei \nn o 9.504"
    text = re.sub(r'\s+', ' ', text)
    m = LEI_TEXT_REF_RE.search(text)
    if not m:
        return None
    tipo = m.group('tipo').lower()
    numero = m.group('numero').replace('.', '')
    if 'complementar' in tipo:
        return f'Lcp{numero}.htm'
    if 'medida' in tipo:
        return f'Mpv{numero}.htm'
    if 'decreto-lei' in tipo:
        return f'Del{numero}.htm'
    if 'decreto' in tipo:
        return f'D{numero}.htm'
    if 'emenda' in tipo:
        return f'emc{numero}.htm'
    return f'L{numero}.htm'


def parse_amending_lei_html(
    html: str,
    only_target_filename: Optional[str] = None,
) -> list[Amendment]:
    """Walk an amending lei's HTML and extract Amendment records.

    Strategy:
    Track section state by walking <p> elements in document order. When we
    enter a "passa a vigorar" or "ficam revogados" block, all subsequent
    hyperlinks (until the next amending-lei article boundary) are
    amendments. The block's target lei is identified at the start.

    Args:
        html: the amending lei's html_raw from planalto_legislacao.db
        only_target_filename: if set, only return amendments to that target.
    """
    soup = BeautifulSoup(html, 'html.parser')

    state: Optional[str] = None  # None | 'modify' | 'revoke'
    state_target_filename: Optional[str] = None
    out: list[Amendment] = []
    ordem = 0

    # Walk all <p> elements in document order
    for p in soup.find_all('p'):
        text = p.get_text(' ', strip=True)
        text_lower = text.lower()

        # Detect state-changing markers in this paragraph
        is_modify_block = bool(PASSA_A_VIGORAR_RE.search(text_lower))
        is_revoke_block = bool(FICAM_REVOGADOS_RE.search(text_lower))

        if is_modify_block or is_revoke_block:
            # Find the target lei filename. First try links in the
            # paragraph (preferred); fall back to parsing the lei
            # reference from text (e.g., "Lei nº 9.504, de 1997").
            new_target = None
            for a in p.find_all('a', href=True):
                tgt = _parse_target_filename(a['href'].split('#')[0])
                if tgt:
                    filename = a['href'].split('#')[0].rsplit('/', 1)[-1]
                    new_target = filename
                    break
            if new_target is None:
                new_target = _extract_lei_filename_from_text(text)
            if new_target is not None:
                state = 'modify' if is_modify_block else 'revoke'
                state_target_filename = new_target

        # If we're in an amending state, process hyperlinks in this paragraph
        if state is None:
            continue

        for a in p.find_all('a', href=True):
            href = a['href']
            if '#' not in href:
                continue
            path_part, _, fragment = href.partition('#')
            if not fragment.startswith('art'):
                continue

            filename = path_part.rsplit('/', 1)[-1]
            # Only count as amendment if the link target matches the
            # current state's target lei
            if state_target_filename and filename.lower() != state_target_filename.lower():
                continue

            target = _parse_target_filename(path_part)
            if target is None:
                continue
            target_tipo, target_numero = target

            if only_target_filename and filename.lower() != only_target_filename.lower():
                continue

            parsed = parse_anchor(fragment)
            if parsed is None:
                continue

            # Action: state gives the default; per-link context can refine
            if state == 'revoke':
                action = 'revoke'
            else:
                action = _detect_action(a, fragment)
                # In a modify block, force 'add' or 'modify' (not 'revoke')
                if action == 'revoke':
                    action = 'modify'

            snippet = ' '.join(text.split())[:300]
            ordem += 1
            out.append(Amendment(
                target_filename=filename,
                target_tipo=target_tipo,
                target_numero=target_numero,
                artigo=parsed.article,
                artigo_letra=parsed.article_letter,
                path=parsed.path,
                action=action,
                source_anchor=fragment,
                source_text=snippet,
                ordem=ordem,
            ))

    return out
