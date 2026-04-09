# Transparência e dados públicos

Legal framework for access to public information and personal data
protection in Brazil, plus the main public-data infrastructures that
matter for empirical research: Portal da Transparência, Comprasnet,
SICONV / Plataforma +Brasil, DATASUS, e-SIC, and state equivalents.

This file is the institutional reference — *where the rules come from
and what they permit*. For the actual catalog of datasets and their
variable structures used in this workspace, see the `data_catalog/`
directory, not this file.

**Topics / keywords**: LAI, Lei de Acesso à Informação, Lei 12.527, LGPD,
Lei 13.709, data protection, privacy, Portal da Transparência, e-SIC,
Fala.BR, transparência ativa, transparência passiva, sigilo, CGU, ANPD,
Comprasnet, SICONV, Plataforma +Brasil, open data, dados abertos,
Decreto 8.777, INDA, CEIS, CNEP.

**Snapshot as of 2026**: LAI (2011) and LGPD (2018, enforcement from
2020) are the two foundational statutes, with ongoing tension at the
intersection — especially over public-servant salary publication and
court-data scraping. ANPD (Autoridade Nacional de Proteção de Dados)
became an autarquia in 2022 (Lei 14.460/2022), consolidating its
enforcement role. LAI review doctrine continues to evolve via STF and
CGU guidance.

Not sourced from a specific project file; built from general knowledge.

---

## 1. Lei 12.527/2011 — Lei de Acesso à Informação (LAI)

### Constitutional basis

- **CF Art. 5 XXXIII**: "todos têm direito a receber dos órgãos públicos
  informações de seu interesse particular, ou de interesse coletivo ou
  geral, que serão prestadas no prazo da lei, sob pena de
  responsabilidade, ressalvadas aquelas cujo sigilo seja imprescindível
  à segurança da sociedade e do Estado."
- **Art. 37 §3 II**: access to administrative records and information on
  government acts.
- **Art. 216 §2**: cultural/historical documents.

### Statutory framework

- **Lei 12.527/2011** (promulgated November 2011, effective May 2012)
  regulates the constitutional right of access.
- Binds **all branches** (Executivo, Legislativo, Judiciário) at
  **all levels** (União, estados, DF, municípios), plus indirect
  administration, state-owned enterprises, and entities receiving public
  resources.

### Core principles

- **Publicidade como regra, sigilo como exceção** (Art. 3 I): publicity
  is the rule, secrecy the exception.
- **Divulgação proativa** (transparência ativa): agencies must publish
  a minimum set of information without waiting for a request — budgets,
  contracts, convênios, salary structure, organograms, work hours, etc.
- **Atendimento a pedidos** (transparência passiva): anyone can file a
  request (no justification required) and the agency must respond
  within 20 days (extendable by 10).
- **Procedimento informal**: requests must be simple; no need for a
  lawyer; no cost except reproduction.
- **Recurso hierárquico**: denials can be appealed internally, then to
  the competent external authority (CGU for federal Executivo;
  equivalent bodies elsewhere), then ultimately to the judiciary.

### Classification of sigilo (Arts. 23–25)

Information can be classified as sigilosa only if disclosure would
threaten:

1. National defense or sovereignty.
2. International relations.
3. Life, safety, or health of the population.
4. Financial/economic/monetary stability.
5. Strategic defense or intelligence information.
6. Investigations in course.
7. Personal information of others.

Classification levels:

- **Ultrassecreta**: 25 years max.
- **Secreta**: 15 years.
- **Reservada**: 5 years.

Classifications require authorization by high-ranking officials; any
classification can be reviewed and overturned via CGU recourse or
judicial action.

### Personal information (Art. 31)

- Personal information about **third parties** is protected for **100
  years** by default, but this protection does not override legitimate
  interests (historical research, public-interest investigation, etc.).
- Information about the **requester themselves** is always available.

### Transparência ativa — mandatory disclosures

Each agency must maintain a website publishing:

- Budget execution, contracts, convênios.
- List of servants and salary structure.
- LAI contacts and e-SIC / Fala.BR interface.
- Statistics on LAI requests received and answered.
- Organograms, work hours, and responsible officials.

Decree 7.724/2012 (federal regulamento) specifies details; states and
municipalities must adopt their own decrees and systems.

### e-SIC / Fala.BR

- Electronic system for LAI requests in federal Executivo.
- Now integrated into **Fala.BR** (the unified ouvidoria platform), also
  maintained by CGU.
- States, municipalities, Legislativo, Judiciário, and MP maintain their
  own SIC systems.

### CGU recourse — federal Executivo

- If a federal agency denies a LAI request, the requester can appeal:
  1. To the agency's own superior authority.
  2. To CGU.
  3. To the Comissão Mista de Reavaliação de Informações (CMRI) — a
     federal-level interministerial review board.
- CGU has published hundreds of decisions setting precedent on what
  constitutes legitimate sigilo and what must be disclosed. These
  decisions are searchable and are often cited by researchers seeking
  to obtain data.

### LAI for researchers — what works

- **Salary and identification of public servants**: generally
  disclosable (affirmed by STF in ARE 652,777, 2015, repercussão geral).
- **Contract details, contractor names, payment records**: generally
  disclosable.
- **Individual beneficiary data in social programs**: partially
  restricted after Bolsa Família disclosure reversals; requests case by
  case.
- **Court records**: governed by separate judicial transparency rules
  (see §4 below and `cnj-administracao-judicial.md`).
- **Ongoing investigations**: sigilo usually upheld until conclusion.

**Source**: [Lei 12.527/2011](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm); [Decreto 7.724/2012](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/decreto/d7724.htm); STF ARE 652,777.

---

## 2. Lei 13.709/2018 — Lei Geral de Proteção de Dados (LGPD)

### Overview

Brazil's comprehensive data protection statute, modeled on the EU GDPR.

- **Promulgated**: August 2018.
- **Effective**: general provisions from September 2020 (originally
  2020, delayed slightly by pandemic); sanction provisions from August
  2021.
- **Scope**: processing of personal data by any natural or legal entity
  operating in Brazil, regardless of where the processing occurs, when
  the data subject is in Brazil, the data was collected in Brazil, or
  the processing aims to offer services to individuals in Brazil
  (Art. 3).

### Legal bases for processing (Art. 7)

Ten legal bases, any one sufficient:

1. Consent.
2. Compliance with legal or regulatory obligation.
3. Execution of public policy by the public administration.
4. **Studies by research entities** (with anonymization when possible).
5. Execution of contract.
6. Exercise of rights in judicial/administrative/arbitration process.
7. Protection of life or physical integrity.
8. Protection of health, in procedures by health professionals.
9. **Legitimate interest** of the controller or third party (subject to
   balancing).
10. Protection of credit.

### Research-specific exemption

- **Art. 7 IV** permits processing for **research by research entities**
  (defined in Art. 5 XVIII as bodies dedicated to basic or applied
  historical, scientific, or statistical research).
- Anonymization should be applied "whenever possible".
- **Art. 11 II c** allows processing of *sensitive* personal data
  (health, race, religion, politics, etc.) for research by research
  entities.
- **Article 13**: specific allowance for public-health research
  (pandemic, epidemiology).
- Research entities can process personal data without consent but must
  apply the principles of adequacy, necessity, finality, security,
  non-discrimination, and accountability.

### Data subject rights (Art. 18)

- Confirmation of processing.
- Access to data.
- Correction of incomplete/inaccurate data.
- Anonymization, blocking, or deletion of unnecessary or excessive data.
- Portability.
- Information about sharing.
- Revocation of consent.

### Sanctions (Art. 52)

- Warning, obligation to publicize the violation, blocking, erasure,
  and **fines up to 2% of revenue (max R$50M per infraction)**.
- Enforcement by ANPD.

### ANPD — Autoridade Nacional de Proteção de Dados

- Originally created as a body within the Presidência (Lei 13.853/2019).
- **Transformed into an autarquia de natureza especial** by **Lei
  14.460/2022** — gained institutional independence, own budget, own
  career track.
- Functions: normative guidance, enforcement, public consultation,
  issuing regulations, sanctioning violators.

### Tension with LAI

- **Public salary disclosure**: LGPD does not override LAI — public
  servant salaries, individually identified, remain disclosable under
  STF ARE 652,777. LGPD applies to the data controller's duties but
  the public-interest legal basis (Art. 7 III) covers the processing.
- **Court data**: scraping identified court records is more contested.
  CNJ and STF guidance is that identified data in judicial proceedings
  remains accessible under the publicity principle (CF Art. 93 IX),
  with **limited** restrictions for specific categories (segredo de
  justiça). Researchers should document their legal basis and consider
  anonymization for publication.
- **Scraped personal data**: projects that scrape identified data
  should document Art. 7 IV as the legal basis, minimize personal data
  retention, anonymize for analysis where possible, and keep LGPD
  DPIA-style documentation of processing purposes.

**Source**: [Lei 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm); [Lei 14.460/2022](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14460.htm).

---

## 3. Main federal transparency infrastructures

### Portal da Transparência

- **portaltransparencia.gov.br** — maintained by CGU.
- Data on federal expenditures, transfers (convênios, SUS, FPM, FUNDEB),
  servant salaries, beneficiaries of some social programs.
- Updated daily for most series.
- Accessible via web interface and downloads; some endpoints available
  via API.

### Comprasnet

- **compras.gov.br** — maintained by Ministério da Gestão (formerly
  Ministério da Economia / Ministério do Planejamento).
- Federal procurement platform: licitações, contracts, catálogo de
  materiais/serviços.
- Structured data on every federal procurement process.
- Data used in the federal-procurement research literature (parallel
  to TCE-SP Audesp data used in this workspace's municipal-level work).

### SICONV / Plataforma +Brasil

- **plataformamaisbrasil.gov.br** — maintained by Ministério da Gestão.
- Federal convênios with states, municipalities, and civil-society
  entities.
- Data on agreement terms, values, execution status, payments.
- Heavily used in research on federal-subnational transfers and
  political alignment.

### Painel de Compras

- Aggregated analytical dashboard for federal procurement data, built
  on Comprasnet.

### Dados abertos

- **dados.gov.br** — federal open-data catalog.
- **INDA — Infraestrutura Nacional de Dados Abertos**: federal
  coordinating framework for open data (Instrução Normativa 4/2012).
- **Decreto 8.777/2016** established the federal open-data policy
  requiring agencies to publish datasets in structured, machine-readable
  formats.

### DATASUS

- SUS data — hospital admissions (SIH/AIH), ambulatory (SIA/APAC),
  mortality (SIM), live births (SINASC), notifiable diseases (SINAN),
  primary care (SISAB), pharmaceutical dispensing (HORUS), and many
  others.
- Primary data source for health-related research.

### SIOPS / SIOPE / FINBRA / SICONFI

- Fiscal and budget reporting databases — see `federalismo-fiscal.md` §5.

### Receita Federal — CNPJ base

- Public registry of legal entities. Used extensively in this workspace
  through the `cnpj` pipeline. Accessible via bulk download (Receita
  Federal makes full CNPJ snapshots available; see `pipelines/cnpj/`).

### TSE — electoral data

- **cdn.tse.jus.br/estatistica** — candidates, results, donations, filings.
- Primary source for electoral research.

### Sanctioned-entity registries

- **CEIS** — firms barred from public contracting (Lei 12.846 Art. 23,
  Lei 8.666, Lei 14.133 sanctions). Maintained by CGU.
- **CNEP** — firms sanctioned under Lei 12.846 specifically. CGU.
- **CEPIM** — entities impeded under Lei 10.522/02 (tax debtors).
- See `cgu-controle-interno.md`.

---

## 4. Judicial transparency — a separate regime

Judicial data has its own transparency framework anchored in:

- **CF Art. 93 IX**: publicity of judicial acts (with exceptions for
  privacy and public interest).
- **CNJ Resoluções**: Res. 121/2010 (publication of judicial data),
  Res. 215/2015 (LAI applied to judiciary), Res. 331/2020 (PJe and
  data-management).
- **LGPD interaction**: CNJ Res. 363/2021 addressed data protection in
  judicial context; processing for judicial purposes has its own legal
  basis under LGPD Art. 7 VI.

Practical consequences for researchers:

- Most court decisions are public, but access mechanisms vary by
  tribunal: web consultation, e-Proc / PJe APIs, bulk exports where
  available.
- **Segredo de justiça**: specific case types (family law, certain
  criminal investigations, juveniles) are restricted.
- **Anonymization in publication**: LGPD pushes toward anonymizing
  identified parties when academic publications use scraped court data,
  even where the original data is public.

See `cnj-administracao-judicial.md` for CNJ case-management systems (PJe,
e-Proc), tribunal-level data-release rules, and Justiça em Números.

---

## 5. State and municipal transparency

- Each state and municipality must maintain LAI/transparency compliance,
  but implementation quality varies enormously.
- **CGE — Controladoria-Geral do Estado**: state-level equivalent of
  CGU. CGE-SP is the largest and most institutionalized.
- **Portal da Transparência estadual/municipal**: some states and large
  municipalities maintain high-quality portals; many small municipalities
  have minimal or non-functional portals, which is itself a research
  outcome (*transparência observada*).
- **TCE audits** of LAI compliance are periodic but not uniform across
  states.

---

## 6. Research design implications

- **LAI as an instrument**: a researcher can file an LAI request and, if
  refused, appeal through CGU, generating a binding precedent and
  opening data for analysis. This has been used strategically to obtain
  datasets.
- **Pre-LAI vs. post-LAI** (2012 cutoff): dramatic change in data
  availability; projects spanning this boundary should account for
  measurement differences.
- **LGPD considerations in empirical work**: document the legal basis
  for personal-data processing (Art. 7 IV or V); anonymize in
  publications where possible; set retention limits; keep processing
  documentation.
- **CEIS/CNEP linkage**: the sanctioned-entity registries can be
  linked to procurement / improbidade / financial datasets through
  CNPJ, generating rich cross-source variables.

---

## 7. Sources and cross-references

**Statutes**:
- [Lei 12.527/2011 — LAI](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm)
- [Decreto 7.724/2012 — LAI regulamento federal](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/decreto/d7724.htm)
- [Lei 13.709/2018 — LGPD](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- [Lei 14.460/2022 — ANPD autarquia](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14460.htm)
- [Decreto 8.777/2016 — dados abertos](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2016/decreto/d8777.htm)
- CNJ Res. 121/2010, 215/2015, 331/2020, 363/2021

**Cross-references**:
- `cgu-controle-interno.md` — CGU runs most federal transparency infra
- `cnj-administracao-judicial.md` — judicial data specifically
- `federalismo-fiscal.md` — fiscal reporting databases
- `data_catalog/` directory (workspace) — actual dataset inventory
