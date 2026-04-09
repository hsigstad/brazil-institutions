#!/usr/bin/env python3
"""
Planalto.gov.br Legislation Scraper

Downloads all Brazilian federal legislation from planalto.gov.br and stores
in a SQLite database for querying.

Usage:
    python planalto_scraper.py discover    # Find all law URLs
    python planalto_scraper.py download    # Download all discovered laws
    python planalto_scraper.py search "saúde"  # Search for health laws
    python planalto_scraper.py stats       # Show database statistics
    python planalto_scraper.py all         # Run discover + download
"""

import argparse
import hashlib
import logging
import os
import re
import sqlite3
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

# Configuration
BASE_URL = "https://www.planalto.gov.br"
DB_PATH = Path(
    os.environ.get(
        "PLANALTO_DB",
        Path.home() / "research" / "data" / "planalto" / "planalto_legislacao.db"
    )
)
REQUEST_DELAY = 0.5  # seconds between requests (be polite)
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


@dataclass
class LegislationRecord:
    """Represents a piece of legislation."""
    url: str
    tipo: str  # lei, decreto, medida_provisoria, etc.
    numero: Optional[str] = None
    data: Optional[str] = None
    ementa: Optional[str] = None
    texto_completo: Optional[str] = None
    html_raw: Optional[str] = None
    downloaded_at: Optional[str] = None


class Database:
    """SQLite database handler."""

    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._init_schema()

    def _init_schema(self):
        """Initialize database schema."""
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT UNIQUE NOT NULL,
                tipo TEXT,
                discovered_at TEXT DEFAULT CURRENT_TIMESTAMP,
                downloaded_at TEXT,
                status TEXT DEFAULT 'pending'  -- pending, downloaded, error
            );

            CREATE TABLE IF NOT EXISTS legislacao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT UNIQUE NOT NULL,
                tipo TEXT,
                numero TEXT,
                data TEXT,
                ementa TEXT,
                texto_completo TEXT,
                html_raw TEXT,
                html_hash TEXT,
                downloaded_at TEXT,
                parsed_at TEXT,
                FOREIGN KEY (url) REFERENCES urls(url)
            );

            CREATE INDEX IF NOT EXISTS idx_urls_status ON urls(status);
            CREATE INDEX IF NOT EXISTS idx_urls_tipo ON urls(tipo);
            CREATE INDEX IF NOT EXISTS idx_legislacao_tipo ON legislacao(tipo);
            CREATE INDEX IF NOT EXISTS idx_legislacao_numero ON legislacao(numero);
            CREATE INDEX IF NOT EXISTS idx_legislacao_ementa ON legislacao(ementa);

            -- Full-text search index
            CREATE VIRTUAL TABLE IF NOT EXISTS legislacao_fts USING fts5(
                url,
                tipo,
                numero,
                ementa,
                texto_completo,
                content='legislacao',
                content_rowid='id'
            );

            -- Triggers to keep FTS in sync
            CREATE TRIGGER IF NOT EXISTS legislacao_ai AFTER INSERT ON legislacao BEGIN
                INSERT INTO legislacao_fts(rowid, url, tipo, numero, ementa, texto_completo)
                VALUES (new.id, new.url, new.tipo, new.numero, new.ementa, new.texto_completo);
            END;

            CREATE TRIGGER IF NOT EXISTS legislacao_ad AFTER DELETE ON legislacao BEGIN
                INSERT INTO legislacao_fts(legislacao_fts, rowid, url, tipo, numero, ementa, texto_completo)
                VALUES ('delete', old.id, old.url, old.tipo, old.numero, old.ementa, old.texto_completo);
            END;

            CREATE TRIGGER IF NOT EXISTS legislacao_au AFTER UPDATE ON legislacao BEGIN
                INSERT INTO legislacao_fts(legislacao_fts, rowid, url, tipo, numero, ementa, texto_completo)
                VALUES ('delete', old.id, old.url, old.tipo, old.numero, old.ementa, old.texto_completo);
                INSERT INTO legislacao_fts(rowid, url, tipo, numero, ementa, texto_completo)
                VALUES (new.id, new.url, new.tipo, new.numero, new.ementa, new.texto_completo);
            END;
        """)
        self.conn.commit()

    def add_url(self, url: str, tipo: str) -> bool:
        """Add a URL to the discovery queue. Returns True if new."""
        try:
            self.conn.execute(
                "INSERT OR IGNORE INTO urls (url, tipo) VALUES (?, ?)",
                (url, tipo)
            )
            self.conn.commit()
            return self.conn.total_changes > 0
        except sqlite3.Error as e:
            logger.error(f"Error adding URL {url}: {e}")
            return False

    # Health-related URL patterns for prioritization
    HEALTH_URL_PATTERNS = [
        r'saude', r'sus\b', r'anvisa', r'vigilancia', r'sanitari',
        r'medicament', r'farmac', r'epidemi', r'vacina', r'imuniz',
        r'hospital', r'medic[oa]', r'enferma', r'plano.*saude',
        r'8080', r'9656', r'9782', r'9961', r'9797',  # Key health law numbers
    ]

    def get_pending_urls(self, limit: int = 100, priority: bool = True) -> list[dict]:
        """Get URLs that haven't been downloaded yet.

        Args:
            limit: Maximum number of URLs to return
            priority: If True, prioritize compilados and health laws
        """
        if not priority:
            cursor = self.conn.execute(
                "SELECT url, tipo FROM urls WHERE status = 'pending' LIMIT ?",
                (limit,)
            )
            return [dict(row) for row in cursor.fetchall()]

        # Priority ordering: compilados first, then health laws, then others
        cursor = self.conn.execute("""
            SELECT url, tipo,
                CASE
                    WHEN lower(url) LIKE '%compilado%' THEN 1
                    ELSE 3
                END as priority
            FROM urls
            WHERE status = 'pending'
            ORDER BY priority, id
            LIMIT ?
        """, (limit,))

        results = [dict(row) for row in cursor.fetchall()]

        # If we have results, further prioritize health laws within non-compilado
        if results:
            health_pattern = '|'.join(self.HEALTH_URL_PATTERNS)
            prioritized = []
            health_laws = []
            others = []

            for item in results:
                url_lower = item['url'].lower()
                if 'compilado' in url_lower:
                    prioritized.append(item)
                elif re.search(health_pattern, url_lower, re.IGNORECASE):
                    health_laws.append(item)
                else:
                    others.append(item)

            return prioritized + health_laws + others

        return results

    def mark_url_downloaded(self, url: str):
        """Mark a URL as downloaded."""
        self.conn.execute(
            "UPDATE urls SET status = 'downloaded', downloaded_at = CURRENT_TIMESTAMP WHERE url = ?",
            (url,)
        )
        self.conn.commit()

    def mark_url_error(self, url: str):
        """Mark a URL as having an error."""
        self.conn.execute(
            "UPDATE urls SET status = 'error' WHERE url = ?",
            (url,)
        )
        self.conn.commit()

    def save_legislation(self, record: LegislationRecord):
        """Save or update a legislation record."""
        html_hash = hashlib.md5(record.html_raw.encode()).hexdigest() if record.html_raw else None

        self.conn.execute("""
            INSERT INTO legislacao (url, tipo, numero, data, ementa, texto_completo, html_raw, html_hash, downloaded_at, parsed_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(url) DO UPDATE SET
                tipo = excluded.tipo,
                numero = excluded.numero,
                data = excluded.data,
                ementa = excluded.ementa,
                texto_completo = excluded.texto_completo,
                html_raw = excluded.html_raw,
                html_hash = excluded.html_hash,
                downloaded_at = excluded.downloaded_at,
                parsed_at = CURRENT_TIMESTAMP
        """, (
            record.url, record.tipo, record.numero, record.data,
            record.ementa, record.texto_completo, record.html_raw,
            html_hash, record.downloaded_at
        ))
        self.conn.commit()

    def search(self, query: str, limit: int = 100) -> list[dict]:
        """Full-text search across legislation."""
        cursor = self.conn.execute("""
            SELECT l.url, l.tipo, l.numero, l.data, l.ementa,
                   snippet(legislacao_fts, 4, '<mark>', '</mark>', '...', 50) as snippet
            FROM legislacao_fts f
            JOIN legislacao l ON f.rowid = l.id
            WHERE legislacao_fts MATCH ?
            ORDER BY rank
            LIMIT ?
        """, (query, limit))
        return [dict(row) for row in cursor.fetchall()]

    def reset_urls_by_numero(self, numeros: list[str]) -> int:
        """Reset URLs for specific law numbers to pending status for re-scraping."""
        count = 0
        for numero in numeros:
            # Find URLs that match this numero
            cursor = self.conn.execute("""
                SELECT url FROM legislacao WHERE numero LIKE ?
            """, (f"%{numero}%",))
            urls = [row[0] for row in cursor.fetchall()]

            for url in urls:
                # Reset URL status to pending
                self.conn.execute(
                    "UPDATE urls SET status = 'pending', downloaded_at = NULL WHERE url = ?",
                    (url,)
                )
                # Delete existing legislation record
                self.conn.execute("DELETE FROM legislacao WHERE url = ?", (url,))
                count += 1

        self.conn.commit()
        return count

    def get_short_text_laws(self, min_length: int = 1000) -> list[dict]:
        """Find laws with suspiciously short text that may need re-scraping."""
        cursor = self.conn.execute("""
            SELECT url, numero, tipo, length(texto_completo) as text_len, length(html_raw) as html_len
            FROM legislacao
            WHERE length(texto_completo) < ? AND length(html_raw) > ?
            ORDER BY html_len DESC
        """, (min_length, min_length * 5))
        return [dict(row) for row in cursor.fetchall()]

    def get_stats(self) -> dict:
        """Get database statistics."""
        stats = {}

        # URL counts by status
        cursor = self.conn.execute("""
            SELECT status, COUNT(*) as count FROM urls GROUP BY status
        """)
        stats['urls'] = {row['status']: row['count'] for row in cursor.fetchall()}

        # Pending URL breakdown by priority
        cursor = self.conn.execute("""
            SELECT
                SUM(CASE WHEN lower(url) LIKE '%compilado%' THEN 1 ELSE 0 END) as compilados,
                COUNT(*) as total
            FROM urls WHERE status = 'pending'
        """)
        row = cursor.fetchone()
        stats['pending_compilados'] = row['compilados'] if row else 0
        stats['pending_total'] = row['total'] if row else 0

        # Legislation counts by type
        cursor = self.conn.execute("""
            SELECT tipo, COUNT(*) as count FROM legislacao GROUP BY tipo ORDER BY count DESC
        """)
        stats['legislacao_by_tipo'] = {row['tipo']: row['count'] for row in cursor.fetchall()}

        # Total legislation
        cursor = self.conn.execute("SELECT COUNT(*) as count FROM legislacao")
        stats['total_legislacao'] = cursor.fetchone()['count']

        return stats

    def close(self):
        """Close database connection."""
        self.conn.close()


class PlanaltoScraper:
    """Scraper for planalto.gov.br legislation."""

    # Main index pages that list year/period sub-indexes
    MAIN_INDEXES = {
        'lei': '/ccivil_03/LEIS/_Lei-Ordinaria.htm',
        'lei_complementar': '/ccivil_03/LEIS/LCP/Quadro_Lcp.htm',
        'lei_delegada': '/ccivil_03/LEIS/Ldl/Quadro_LDL.htm',
        'decreto': '/ccivil_03/decreto/_Dec_principal.htm',
        'decreto_lei': '/ccivil_03/Decreto-Lei/principal_ano.htm',
        'medida_provisoria': '/ccivil_03/MPV/Principal.htm',
        'constituicao': '/ccivil_03/Constituicao/Constituicao.htm',
        'emenda_constitucional': '/ccivil_03/Constituicao/Emendas/Emc/Quadro_emc.htm',
    }

    # Patterns to identify legislation URLs (vs index pages)
    LEGISLATION_FILE_PATTERNS = [
        # Laws: L12345.htm, Lcp123.htm, Ldl12.htm (and compilado versions)
        re.compile(r'/L\d+[A-Za-z]*\.htm$', re.IGNORECASE),
        re.compile(r'/L\d+compilado\.htm$', re.IGNORECASE),
        re.compile(r'/Lcp\d+\.htm$', re.IGNORECASE),
        re.compile(r'/Lcp\d+compilado\.htm$', re.IGNORECASE),
        re.compile(r'/Ldl\d+\.htm$', re.IGNORECASE),
        # Decrees: D12345.htm, Del1234.htm (and compilado versions)
        re.compile(r'/D\d+[A-Za-z]*\.htm$', re.IGNORECASE),
        re.compile(r'/D\d+compilado\.htm$', re.IGNORECASE),
        re.compile(r'/Del\d+\.htm$', re.IGNORECASE),
        re.compile(r'/Del\d+compilado\.htm$', re.IGNORECASE),
        # Provisional measures: Mpv123.htm
        re.compile(r'/Mpv\d+[A-Za-z]*\.htm$', re.IGNORECASE),
        re.compile(r'/Mpv\d+compilado\.htm$', re.IGNORECASE),
        # Constitutional amendments: Emc12.htm
        re.compile(r'/Emc\d+\.htm$', re.IGNORECASE),
        # Constitution
        re.compile(r'/[Cc]onstituicao\.htm$', re.IGNORECASE),
        re.compile(r'/[Cc]onstituicao[Cc]ompilado\.htm$', re.IGNORECASE),
    ]

    # Compilado URL patterns - for generating compilado URLs from original URLs
    COMPILADO_PATTERNS = [
        (re.compile(r'(/L\d+)(\.htm)$', re.IGNORECASE), r'\1compilado\2'),
        (re.compile(r'(/Lcp\d+)(\.htm)$', re.IGNORECASE), r'\1compilado\2'),
        (re.compile(r'(/D\d+)(\.htm)$', re.IGNORECASE), r'\1compilado\2'),
        (re.compile(r'(/Del\d+)(\.htm)$', re.IGNORECASE), r'\1compilado\2'),
        (re.compile(r'(/Mpv\d+)(\.htm)$', re.IGNORECASE), r'\1compilado\2'),
    ]

    # Patterns to identify index/quadro pages (need further crawling)
    INDEX_FILE_PATTERNS = [
        re.compile(r'quadro', re.IGNORECASE),
        re.compile(r'_leis\d{4}\.htm$', re.IGNORECASE),
        re.compile(r'_dec\d{4}\.htm$', re.IGNORECASE),
        re.compile(r'principal', re.IGNORECASE),
        re.compile(r'_Lei-Ordinaria\.htm$', re.IGNORECASE),
    ]

    def __init__(self, db: Database):
        self.db = db
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
        })

    def _fetch(self, url: str) -> Optional[str]:
        """Fetch a URL with retry logic."""
        for attempt in range(MAX_RETRIES):
            try:
                response = self.session.get(url, timeout=REQUEST_TIMEOUT)
                response.raise_for_status()
                # Try to detect encoding
                response.encoding = response.apparent_encoding or 'iso-8859-1'
                return response.text
            except requests.RequestException as e:
                logger.warning(f"Attempt {attempt + 1}/{MAX_RETRIES} failed for {url}: {e}")
                if attempt < MAX_RETRIES - 1:
                    time.sleep(REQUEST_DELAY * 2)
        return None

    def _is_legislation_url(self, url: str) -> bool:
        """Check if URL points to an actual legislation document."""
        for pattern in self.LEGISLATION_FILE_PATTERNS:
            if pattern.search(url):
                return True
        return False

    def _is_index_url(self, url: str) -> bool:
        """Check if URL is an index page that needs further crawling."""
        for pattern in self.INDEX_FILE_PATTERNS:
            if pattern.search(url):
                return True
        return False

    def _classify_url(self, url: str) -> Optional[str]:
        """Classify a URL by legislation type."""
        url_lower = url.lower()

        # Check if it's a compilado version
        is_compilado = 'compilado' in url_lower

        if '/lcp/' in url_lower or '/lcp' in url_lower:
            return 'lei_complementar_compilado' if is_compilado else 'lei_complementar'
        if '/ldl/' in url_lower:
            return 'lei_delegada_compilado' if is_compilado else 'lei_delegada'
        if '/decreto-lei/' in url_lower or '/del' in url_lower:
            return 'decreto_lei_compilado' if is_compilado else 'decreto_lei'
        if '/decreto/' in url_lower or '/d' in url_lower and re.search(r'/d\d+', url_lower):
            return 'decreto_compilado' if is_compilado else 'decreto'
        if '/mpv/' in url_lower:
            return 'medida_provisoria_compilado' if is_compilado else 'medida_provisoria'
        if '/constituicao/' in url_lower:
            if '/emc/' in url_lower or '/emc' in url_lower:
                return 'emenda_constitucional'
            return 'constituicao_compilado' if is_compilado else 'constituicao'
        if '/leis/' in url_lower or '/lei/' in url_lower or re.search(r'/l\d+', url_lower):
            return 'lei_compilado' if is_compilado else 'lei'
        return None

    def _get_compilado_url(self, url: str) -> Optional[str]:
        """Generate compilado URL from an original URL."""
        for pattern, replacement in self.COMPILADO_PATTERNS:
            if pattern.search(url):
                return pattern.sub(replacement, url)
        return None

    def _extract_links(self, html: str, base_url: str) -> list[str]:
        """Extract all .htm links from HTML page."""
        soup = BeautifulSoup(html, 'html.parser')
        links = []

        for a in soup.find_all('a', href=True):
            href = a['href']
            # Skip anchors, mailto, javascript
            if href.startswith('#') or href.startswith('mailto:') or href.startswith('javascript:'):
                continue

            # Resolve relative URLs
            full_url = urljoin(base_url, href)

            # Only keep planalto.gov.br URLs with .htm extension
            if 'planalto.gov.br' not in full_url:
                continue
            if not (full_url.endswith('.htm') or full_url.endswith('.html')):
                continue

            # Normalize URL (remove anchors)
            full_url = full_url.split('#')[0]
            links.append(full_url)

        return list(set(links))  # Deduplicate

    def discover_urls(self):
        """Discover all legislation URLs by crawling index pages."""
        visited = set()
        to_visit = []
        discovered_legislation = 0
        discovered_indexes = 0

        # Start with main index pages
        for tipo, path in self.MAIN_INDEXES.items():
            to_visit.append((urljoin(BASE_URL, path), tipo))

        while to_visit:
            url, source_tipo = to_visit.pop(0)

            if url in visited:
                continue
            visited.add(url)

            logger.info(f"Crawling index: {url}")

            html = self._fetch(url)
            if not html:
                logger.warning(f"Failed to fetch: {url}")
                continue

            time.sleep(REQUEST_DELAY)

            # Extract all links
            links = self._extract_links(html, url)

            for link in links:
                if link in visited:
                    continue

                # Check if it's a legislation document
                if self._is_legislation_url(link):
                    tipo = self._classify_url(link) or source_tipo
                    if self.db.add_url(link, tipo):
                        discovered_legislation += 1
                        if discovered_legislation % 100 == 0:
                            logger.info(f"Discovered {discovered_legislation} legislation URLs...")

                    # Also try to discover compilado version if this is an original
                    if 'compilado' not in link.lower():
                        compilado_url = self._get_compilado_url(link)
                        if compilado_url and compilado_url not in visited:
                            compilado_tipo = self._classify_url(compilado_url)
                            if self.db.add_url(compilado_url, compilado_tipo):
                                discovered_legislation += 1

                # Check if it's another index page to crawl
                elif self._is_index_url(link):
                    to_visit.append((link, source_tipo))
                    discovered_indexes += 1

        logger.info(f"Discovery complete. Found {discovered_legislation} legislation URLs from {len(visited)} index pages.")
        return discovered_legislation

    def _parse_legislation(self, html: str, url: str, tipo: str) -> LegislationRecord:
        """Parse legislation content from HTML."""
        soup = BeautifulSoup(html, 'html.parser')

        # Check if this is a compilado version
        is_compilado = 'compilado' in url.lower() or 'compilado' in (tipo or '').lower()

        # For compilado versions, convert strike tags to markdown-style annotations
        if is_compilado:
            for strike in soup.find_all('strike'):
                strike.insert_before('[REVOGADO: ')
                strike.insert_after(']')
                strike.unwrap()

            # Mark red text (usually amendments) - common patterns
            for font in soup.find_all('font', color=re.compile(r'red|#ff0000|#800000', re.IGNORECASE)):
                font.insert_before('[ALTERADO: ')
                font.insert_after(']')

        # Remove scripts, styles, navigation
        for tag in soup.find_all(['script', 'style', 'nav', 'header', 'footer']):
            tag.decompose()

        # Try multiple strategies to extract text
        texto_completo = None

        # Strategy 1: Look for main content div (some pages use this)
        main_content = soup.find('div', {'id': 'conteudo'}) or soup.find('div', {'class': 'conteudo'})
        if main_content:
            texto_completo = main_content.get_text(separator='\n', strip=True)

        # Strategy 2: Look for article text in paragraphs with specific patterns
        if not texto_completo or len(texto_completo) < 1000:
            # Find all paragraphs that look like law articles
            article_paragraphs = []
            for p in soup.find_all(['p', 'font']):
                text = p.get_text(strip=True)
                # Look for article markers or substantive content
                if (re.search(r'^Art\.?\s*\d+', text) or
                    re.search(r'^§\s*\d+', text) or
                    re.search(r'^Parágrafo único', text, re.IGNORECASE) or
                    re.search(r'^[IVX]+\s*[-–]', text) or
                    len(text) > 100):
                    article_paragraphs.append(text)

            if article_paragraphs:
                texto_completo = '\n\n'.join(article_paragraphs)

        # Strategy 3: Get all text from body (fallback)
        if not texto_completo or len(texto_completo) < 500:
            body = soup.find('body')
            texto_completo = body.get_text(separator='\n', strip=True) if body else soup.get_text(separator='\n', strip=True)

        # Strategy 4: If still too short, try getting text from all table cells
        if len(texto_completo) < 500:
            all_text = []
            for td in soup.find_all('td'):
                cell_text = td.get_text(separator=' ', strip=True)
                if len(cell_text) > 50:  # Skip short cells (navigation, etc.)
                    all_text.append(cell_text)
            if all_text:
                texto_completo = '\n\n'.join(all_text)

        # Clean up excessive whitespace
        texto_completo = re.sub(r'\n{3,}', '\n\n', texto_completo)
        texto_completo = re.sub(r' +', ' ', texto_completo)

        # Extract numero and data from title/epigraph
        numero = None
        data = None
        ementa = None

        # Get first 3000 chars for metadata extraction
        title_text = texto_completo[:3000]

        # Try to find law number
        # Pattern: "LEI Nº 8.080, DE 19 DE SETEMBRO DE 1990"
        # Or: "DECRETO Nº 12.345, DE 1º DE JANEIRO DE 2024"
        number_patterns = [
            re.compile(r'(?:lei|decreto|medida\s+provis[óo]ria|emenda\s+constitucional)\s*(?:complementar\s+)?(?:n[ºo°]?\s*)?([\d.,]+)', re.IGNORECASE),
            re.compile(r'(?:n[ºo°]\s*)?([\d.]+)\s*,?\s*de\s+\d{1,2}', re.IGNORECASE),
        ]

        for pattern in number_patterns:
            match = pattern.search(title_text)
            if match:
                numero = match.group(1).replace('.', '').replace(',', '').strip()
                if numero:
                    break

        # Try to extract date
        date_pattern = re.compile(
            r'de\s+(\d{1,2})[°ºo]?\s+de\s+(\w+)\s+de\s+(\d{4})',
            re.IGNORECASE
        )
        date_match = date_pattern.search(title_text)
        if date_match:
            data = f"{date_match.group(1)} de {date_match.group(2)} de {date_match.group(3)}"

        # Try to find ementa (summary)
        ementa_patterns = [
            r'(Dispõe sobre[^.]+\.)',
            r'(Altera[^.]+\.)',
            r'(Institui[^.]+\.)',
            r'(Estabelece[^.]+\.)',
            r'(Regulamenta[^.]+\.)',
            r'(Cria[^.]+\.)',
            r'(Autoriza[^.]+\.)',
            r'(Dá nova redação[^.]+\.)',
            r'(Acrescenta[^.]+\.)',
            r'(Revoga[^.]+\.)',
        ]

        for pattern in ementa_patterns:
            match = re.search(pattern, texto_completo[:5000], re.IGNORECASE)
            if match:
                ementa = match.group(1)[:500]
                break

        return LegislationRecord(
            url=url,
            tipo=tipo,
            numero=numero,
            data=data,
            ementa=ementa,
            texto_completo=texto_completo,
            html_raw=html,
            downloaded_at=datetime.now().isoformat(),
        )

    def reparse_legislation(self, batch_size: int = 100, min_text_len: int = 0, max_text_len: int = 1000):
        """Re-parse legislation from stored HTML without re-downloading.

        Args:
            batch_size: Number of records to process at a time
            min_text_len: Only reparse records with text shorter than this
            max_text_len: Only reparse records with text shorter than this
        """
        total_reparsed = 0
        total_errors = 0

        # Mark start time to avoid reparsing same records twice
        # Use UTC to match SQLite CURRENT_TIMESTAMP (which is always UTC)
        start_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        while True:
            # Get records with stored HTML that need reparsing
            # Skip records reparsed after this session started
            cursor = self.db.conn.execute("""
                SELECT url, tipo, html_raw
                FROM legislacao
                WHERE html_raw IS NOT NULL
                  AND length(html_raw) > 1000
                  AND (length(texto_completo) < ? OR texto_completo IS NULL)
                  AND (parsed_at IS NULL OR parsed_at < ?)
                LIMIT ?
            """, (max_text_len, start_time, batch_size))

            rows = cursor.fetchall()
            if not rows:
                break

            for url, tipo, html_raw in rows:
                logger.info(f"Reparsing [{tipo}]: {url}")

                try:
                    record = self._parse_legislation(html_raw, url, tipo)

                    # Update only parsed fields, keep html_raw
                    self.db.conn.execute("""
                        UPDATE legislacao SET
                            numero = ?,
                            data = ?,
                            ementa = ?,
                            texto_completo = ?,
                            parsed_at = CURRENT_TIMESTAMP
                        WHERE url = ?
                    """, (record.numero, record.data, record.ementa,
                          record.texto_completo, url))
                    self.db.conn.commit()

                    total_reparsed += 1

                    if total_reparsed % 50 == 0:
                        logger.info(f"Progress: {total_reparsed} reparsed, {total_errors} errors")

                except Exception as e:
                    logger.error(f"Error reparsing {url}: {e}")
                    total_errors += 1

        logger.info(f"Reparse complete. Reparsed: {total_reparsed}, Errors: {total_errors}")
        return total_reparsed

    def download_legislation(self, batch_size: int = 100, priority: bool = True):
        """Download pending legislation URLs.

        Args:
            batch_size: Number of URLs to fetch per batch
            priority: If True, prioritize compilados and health laws first
        """
        total_downloaded = 0
        total_errors = 0

        if priority:
            logger.info("Priority mode: downloading compilados and health laws first")

        while True:
            pending = self.db.get_pending_urls(batch_size, priority=priority)
            if not pending:
                break

            for item in pending:
                url = item['url']
                tipo = item['tipo']

                logger.info(f"Downloading [{tipo}]: {url}")

                html = self._fetch(url)
                if html:
                    try:
                        record = self._parse_legislation(html, url, tipo)
                        self.db.save_legislation(record)
                        self.db.mark_url_downloaded(url)
                        total_downloaded += 1

                        if total_downloaded % 50 == 0:
                            logger.info(f"Progress: {total_downloaded} downloaded, {total_errors} errors")
                    except Exception as e:
                        logger.error(f"Error parsing {url}: {e}")
                        self.db.mark_url_error(url)
                        total_errors += 1
                else:
                    self.db.mark_url_error(url)
                    total_errors += 1

                time.sleep(REQUEST_DELAY)

        logger.info(f"Download complete. Downloaded: {total_downloaded}, Errors: {total_errors}")
        return total_downloaded


def main():
    parser = argparse.ArgumentParser(
        description="Scrape Brazilian legislation from planalto.gov.br"
    )
    parser.add_argument(
        'command',
        choices=['discover', 'download', 'search', 'stats', 'all', 'reset', 'find-short', 'add-compilados', 'reparse'],
        help="Command to run"
    )
    parser.add_argument(
        'query',
        nargs='?',
        help="Search query (for search command)"
    )
    parser.add_argument(
        '--db',
        type=Path,
        default=DB_PATH,
        help="Path to SQLite database"
    )
    parser.add_argument(
        '--batch',
        type=int,
        default=100,
        help="Batch size for downloads"
    )
    parser.add_argument(
        '--priority',
        action='store_true',
        default=True,
        help="Prioritize compilados and health laws (default: True)"
    )
    parser.add_argument(
        '--no-priority',
        action='store_true',
        help="Disable priority ordering, download in discovery order"
    )

    args = parser.parse_args()
    args.use_priority = args.priority and not args.no_priority

    db = Database(args.db)
    scraper = PlanaltoScraper(db)

    try:
        if args.command == 'discover':
            scraper.discover_urls()

        elif args.command == 'download':
            scraper.download_legislation(batch_size=args.batch, priority=args.use_priority)

        elif args.command == 'all':
            logger.info("Running full pipeline: discover + download")
            scraper.discover_urls()
            scraper.download_legislation(batch_size=args.batch, priority=args.use_priority)

        elif args.command == 'search':
            if not args.query:
                parser.error("search command requires a query")
            results = db.search(args.query)
            print(f"\nFound {len(results)} results for '{args.query}':\n")
            for r in results:
                print(f"  [{r['tipo']}] {r['numero'] or 'N/A'} - {r['data'] or 'N/A'}")
                print(f"    URL: {r['url']}")
                if r['ementa']:
                    print(f"    Ementa: {r['ementa'][:100]}...")
                if r.get('snippet'):
                    print(f"    Match: {r['snippet']}")
                print()

        elif args.command == 'stats':
            stats = db.get_stats()
            print("\n=== Database Statistics ===\n")
            print("URL Status:")
            for status, count in stats.get('urls', {}).items():
                print(f"  {status}: {count}")

            if stats.get('pending_total', 0) > 0:
                print(f"\nPending Priority Breakdown:")
                print(f"  compilados: {stats['pending_compilados']}")
                print(f"  other: {stats['pending_total'] - stats['pending_compilados']}")

            print(f"\nTotal Legislation Downloaded: {stats['total_legislacao']}")
            print("\nBy Type:")
            for tipo, count in stats.get('legislacao_by_tipo', {}).items():
                print(f"  {tipo}: {count}")

        elif args.command == 'reset':
            if not args.query:
                parser.error("reset command requires law numbers (comma-separated)")
            numeros = [n.strip() for n in args.query.split(',')]
            count = db.reset_urls_by_numero(numeros)
            print(f"Reset {count} URLs for re-scraping: {numeros}")
            print("Run 'download' to re-scrape these laws.")

        elif args.command == 'find-short':
            short_laws = db.get_short_text_laws(min_length=1000)
            print(f"\n=== Laws with short text (< 1000 chars but HTML > 5000) ===\n")
            print(f"Found {len(short_laws)} laws that may need re-scraping:\n")
            for law in short_laws[:30]:
                print(f"  {law['tipo']} {law['numero']}: text={law['text_len']}, html={law['html_len']}")
                print(f"    {law['url']}")

        elif args.command == 'reparse':
            # Reparse all records with short text from stored HTML
            max_len = int(args.query) if args.query else 1000
            logger.info(f"Reparsing records with text < {max_len} chars from stored HTML...")
            scraper.reparse_legislation(batch_size=args.batch, max_text_len=max_len)

        elif args.command == 'add-compilados':
            # Get all existing non-compilado URLs
            cursor = db.conn.execute("""
                SELECT DISTINCT url FROM urls
                WHERE url NOT LIKE '%compilado%'
                  AND (url LIKE '%.htm' OR url LIKE '%.html')
            """)
            original_urls = [row[0] for row in cursor.fetchall()]

            added = 0
            for url in original_urls:
                compilado_url = scraper._get_compilado_url(url)
                if compilado_url:
                    tipo = scraper._classify_url(compilado_url)
                    if db.add_url(compilado_url, tipo):
                        added += 1
                        if added % 500 == 0:
                            logger.info(f"Added {added} compilado URLs...")

            print(f"\nAdded {added} compilado URLs to download queue.")
            print("Run 'download' to fetch them.")

    finally:
        db.close()


if __name__ == '__main__':
    main()
