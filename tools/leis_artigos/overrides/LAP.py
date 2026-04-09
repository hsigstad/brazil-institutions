"""Manual overrides for LAP (Lei 4.717/1965 — Ação Popular)."""

OVERRIDES = [
    {
        # The planalto scraper stored this lei with wrong numero (6513
        # instead of 4717) and a corrupted data field. As a result the
        # parser fell back to vigente_desde='1900-01-01'. The real
        # publication date is 29 June 1965.
        'match': {'apelido': 'LAP', 'vigente_desde': '1900-01-01'},
        'set': {'vigente_desde': '1965-06-29'},
        'note': 'Date corrected from planalto scrape error. LAP was published '
                '29 June 1965. Verified against planalto.gov.br/ccivil_03/LEIS/L4717.htm.',
        'verified': '2026-04-09',
        'verified_by': 'henrik',
    },
]
