# Data pointers — Brazilian institutional data

A guide to where Brazilian institutional data lives, organized by topic.
For each topic: authoritative sources, access methods, and pointers to
the topical files where the institutional context is explained.

This file describes **public data sources** — websites, APIs, bulk
downloads. It is **not** a catalog of cleaned datasets that anyone has
prepared and shared. For that, look at [basedosdados](https://basedosdados.org/)
(the closest thing Brazil has to an authoritative aggregator) and the
specific source pages linked below.

**Topics / keywords**: data, datasets, basedosdados, TSE, CNJ, DataJud,
DATASUS, IBGE, INEP, RAIS, SICONFI, SIOPS, Comprasnet, Audesp, Portal
da Transparência, Receita Federal, CNPJ, scraping, open data, dados
abertos, BigQuery, microdados.

**Snapshot as of 2026**: URLs and dataset coverage change. Verify
URLs before relying on them; basedosdados table IDs change occasionally
as the project re-harmonizes datasets.

## How to use this file

- **By topic**: jump to the section for the topic you need (electoral,
  fiscal, court, etc.). Each section lists the canonical sources with
  one-line descriptions and access notes.
- **Cross-references**: each section links back to the topical files
  in this directory that explain the institutional context behind the
  data.
- **basedosdados first**: when basedosdados has a cleaned version of
  a dataset, prefer it — it's harmonized, documented, and BigQuery-
  queryable. Fall back to the raw source only when basedosdados doesn't
  cover what you need.

---

## Authoritative aggregators

These are the starting points before going to individual source portals.

### basedosdados

- **URL**: <https://basedosdados.org/>
- **What it is**: an open-data project that harmonizes and republishes
  hundreds of Brazilian datasets in a unified BigQuery instance with
  documented schemas. Mediated by the *Base dos Dados* organization
  (now part of *Data.B*).
- **Access**: BigQuery (query directly via SQL), Python SDK
  (`basedosdados`), R package, and dataset download from the web.
- **Free tier**: queries up to a per-user budget; non-trivial volumes
  may require BigQuery billing.
- **Coverage** (representative): TSE elections (`br_tse_eleicoes`),
  IBGE demographic and economic (`br_ibge_*`), INEP education
  (`br_inep_*`), RAIS labor (`br_me_rais`), CAGED hires/separations
  (`br_me_caged`), CNPJ firm registry (`br_receita_federal_cnpj`),
  SUS health (`br_ms_*`), SICONFI fiscal (`br_me_siconfi`), CADE
  cartel cases, BCB monetary series, Mais Médicos, Programa Bolsa
  Família, and many others.
- **License**: CC BY 4.0 for the harmonized data; original sources
  retain their own terms.
- **Citing convention**: when citing in papers, follow basedosdados
  guidance — credit both the original source and the basedosdados
  harmonization.

### IPEA dados

- **URL**: <http://www.ipeadata.gov.br/>
- **What it is**: macroeconomic, regional, and historical time series
  curated by IPEA. Strong on aggregate indicators going back decades.
- **Access**: web interface with download to CSV/Excel; Python wrapper
  (`ipeadatapy`).
- **Coverage**: GDP series, inflation, interest rates, fiscal,
  demographic, regional indicators.

### dados.gov.br

- **URL**: <https://dados.gov.br/>
- **What it is**: federal open-data catalog (INDA — Infraestrutura
  Nacional de Dados Abertos).
- **Coverage**: heterogeneous; some agencies maintain their datasets
  here, others don't. Quality varies dramatically.
- **Best for**: discovering what federal agencies have published; not
  for serious replication.

---

## Electoral data

### TSE — Repositório de Dados Eleitorais

- **URL**: <https://dadosabertos.tse.jus.br/>
- **What it is**: the canonical source for Brazilian electoral data.
  Bulk downloads by election year for: candidates, results, donations,
  filings, biographical info, voter demographics by município/zona/seção.
- **Access**: bulk CSV downloads per election year and dataset type.
- **Coverage**: every federal/state/municipal election since at least
  1994 (some series back to the 1980s).
- **basedosdados**: `br_tse_eleicoes` (cleaned, harmonized across
  years).
- **Notable subsets**:
  - Candidates (`consulta_cand_*`): name, party, office, status.
  - Results (`votacao_candidato_munzona_*`): votes by município and
    zone.
  - Donations (`receitas_candidatos_*`): campaign finance filings.
  - Voter demographics (`perfil_eleitorado_*`): age, sex, education
    by zone.
- **License**: public; TSE attributes itself as the source.
- **See**: [`topics/partidos-e-sistema-eleitoral.md`](topics/partidos-e-sistema-eleitoral.md),
  [`topics/processo-eleitoral.md`](topics/processo-eleitoral.md),
  [`topics/prestacao-contas-eleitorais.md`](topics/prestacao-contas-eleitorais.md),
  [`topics/justica-eleitoral.md`](topics/justica-eleitoral.md).

### CEPESP-FGV

- **URL**: <http://cepesp.io/>
- **What it is**: an FGV-EAESP project that re-publishes TSE electoral
  data with cleaning, additional variables (gender inferred from
  names, party group classification), and an R package.
- **Best for**: research that needs derived/inferred variables that
  TSE doesn't publish directly.

### TSE candidate filings

- **URL**: <https://divulgacandcontas.tse.jus.br/>
- **What it is**: per-candidate filings page (registration documents,
  asset declarations, criminal record certificates). Web only — no
  bulk export. Scraping required.
- **Useful for**: candidate-level qualitative data, asset evolution.

---

## Câmara dos Deputados and Senado

### Câmara dos Deputados — Open Data Portal

- **URL**: <https://dadosabertos.camara.leg.br/>
- **What it is**: API + bulk downloads for: deputados (current and
  historical), votações nominais, proposições, despesas (cota
  parlamentar), órgãos, mesas, convocações.
- **Access**: REST API (well-documented), JSON/XML responses, plus
  bulk downloads.
- **Coverage**: detailed from ~2003 onward; some series further back.
- **Useful for**: roll-call voting analysis, individual deputy
  spending, proposição co-authorship networks.

### Senado Federal — Open Data

- **URL**: <https://legis.senado.leg.br/dadosabertos/>
- **What it is**: equivalent for the Senate. Senadores, votações,
  matérias, comissões.
- **Access**: REST API (less mature than Câmara's).

### Câmaras municipais (subnational)

- No unified portal. Each câmara municipal publishes (or doesn't)
  its own data. Larger cities (São Paulo, Rio, Belo Horizonte) have
  dedicated open-data efforts; most small municipalities have only
  PDF atas.
- **Best for**: case studies of specific municipalities. Not a
  cross-municipal comparable source.

---

## Court records

### CNJ DataJud (BNDP — Base Nacional de Dados do Poder Judiciário)

- **URL**: <https://www.cnj.jus.br/sistemas/datajud/>
- **What it is**: CNJ initiative to centralize structured procedural
  data from all Brazilian tribunals. Schema documented in CNJ Res.
  331/2020.
- **Access**: not a fully public download by default. Access typically
  requires institutional or research-purpose authorization. Some
  derived dashboards are public.
- **Coverage**: aspires to all tribunals; actual completeness varies
  by tribunal.
- **See**: [`topics/cnj-administracao-judicial.md`](topics/cnj-administracao-judicial.md) §2.

### CNJ Justiça em Números

- **URL**: <https://www.cnj.jus.br/pesquisas-judiciarias/justica-em-numeros/>
- **What it is**: annual statistical report on the Brazilian judiciary
  with macro-level indicators per branch and tribunal. PDF + Excel.
- **Coverage**: 2009–present.
- **Useful for**: macro indicators, congestion rates, productivity,
  expenditure per branch.

### CNJ Painéis (dashboards)

- **URL**: <https://paineis.cnj.jus.br/>
- **What it is**: thematic dashboards built on DataJud — improbidade,
  feminicídio, ações trabalhistas, execução fiscal, etc.
- **Useful for**: descriptive aggregates without needing DataJud
  access.

### STF jurisprudência

- **URL**: <https://portal.stf.jus.br/jurisprudencia/>
- **What it is**: search interface for STF decisions. Per-case detail
  pages including votes, rapporteur, parties, full text. Web only.
- **Bulk export**: not generally available; scrapeable via the search
  pages.
- **Useful for**: building a corpus of STF decisions on specific
  topics.

### STJ jurisprudência

- **URL**: <https://www.stj.jus.br/sites/portalp/Inicio>
- Similar interface for STJ decisions.

### TJSP — Consulta Processual

- **URL**: <https://esaj.tjsp.jus.br/cpopg/open.do>
- **What it is**: web consultation interface for TJSP first-instance
  cases (and equivalents for second-instance). Per-case detail pages
  with movements, parties, decisions.
- **Bulk export**: NONE. Scraping is the only path; CAPTCHA-protected
  in places.
- **Useful for**: building case-level datasets on specific subjects
  (improbidade, family law, civil disputes, etc.).
- **See**: [`topics/cnj-administracao-judicial.md`](topics/cnj-administracao-judicial.md) §4.

### TRFs and Justiça Federal

- Each TRF has its own consultation interface, plus the federal
  e-Proc system used by several TRFs.
- **Trf1**: <https://www.trf1.jus.br/>
- **Trf2**: <https://www.trf2.jus.br/>
- (analogous for TRF3, TRF4, TRF5, TRF6)

### TRTs (labor courts)

- Each TRT has a PJe consultation interface. The Justiça do Trabalho
  also publishes some aggregated statistics via TST.
- **TST estatísticas**: <https://www.tst.jus.br/web/estatistica>
- **TRT2 (São Paulo)**: <https://ww2.trt2.jus.br/>
- **See**: [`topics/justica-trabalho.md`](topics/justica-trabalho.md).

### Electoral courts (TSE/TREs)

- **TSE**: <https://www.tse.jus.br/sai>
- **Diários da Justiça Eleitoral** are scraped from each TRE.

### Annotated legislation (legislação anotada)

Freely available commented legislation with article-by-article
jurisprudence cross-references:

- **TSE Código Eleitoral Anotado** — the single best free resource.
  Article-by-article annotations of `CE` (Lei 4.737/1965) with
  TSE acórdãos, resoluções, and CF cross-references. Shows whether
  provisions were received by CF/88, links to implementing rules.
  **URL**: <https://www.tse.jus.br/legislacao/codigo-eleitoral/codigo-eleitoral-1/codigo-eleitoral-lei-nb0-4.737-de-15-de-julho-de-1965>.
  HTML structure is clean and scrapeable (`<li class="marcador-quadrado">`
  for annotations, `<p class="texto-corrido">` for article text).
- **TSE Sistematização das Normas Eleitorais (SNE)** — consolidation of
  all electoral norms across 8 thematic axes, identifying conflicts
  and obsolete provisions. Free PDFs.
  **URL**: <https://www.tse.jus.br/legislacao/sne/sistematizacao-das-normas-eleitorais>.
- **Dizer o Direito** — free blog with STF/STJ decision summaries
  organized by law/article. Not structured as annotated legislation
  but effectively functions as one for recent jurisprudence. Archive
  from 2011.
  **URL**: <https://www.dizerodireito.com.br/>.

**Not freely available**: annotated versions of CPC, CPP, CP, CLT,
CF, or LIA exist only in paid platforms (RT Online, Vade Mecum
Saraiva, JusBrasil Pro). LexML indexes legislation and jurisprudence
separately but does not cross-reference them. Planalto.gov.br
provides raw text with amendment notes only.

### Comarcas and judicial organization

- **CNJ Justiça em Números**: annual comarca and vara counts per state
  are published in the report annexes. The authoritative public source
  for cross-state comparison of judicial infrastructure.
- **State COJs** (Códigos de Organização Judiciária): each state's
  legislative assembly publishes the statute governing comarca
  creation, classification by entrância, and vara allocation.
  Thresholds (population, electors, feitos judiciais) vary by state
  and era — see [`topics/justica-estadual.md`](topics/justica-estadual.md) §3
  for a summary table.
- **TJSP**: the largest state court publishes its current comarca/vara
  structure on [tjsp.jus.br](https://www.tjsp.jus.br/). Historical
  comarca creation decrees (Decreto 9.775/1938, Lei 1.940/1952) are
  available via the ALESP legislative archive.
- **See**: [`topics/justica-estadual.md`](topics/justica-estadual.md),
  [`topics/organizacao-historica.md`](topics/organizacao-historica.md) §4.

---

## Procurement

### Comprasnet (compras.gov.br)

- **URL**: <https://www.gov.br/compras/>
- **What it is**: federal procurement platform. Tracks all federal
  licitações, contracts, registros de preços. Includes the catálogo
  de materiais and serviços.
- **Access**: web interface + API + Painel de Compras for aggregated
  views. Bulk export available for some series.
- **Coverage**: federal government only.
- **basedosdados**: partial coverage in `br_governo_compras_*`.
- **See**: [`topics/licitacoes.md`](topics/licitacoes.md).

### Painel de Compras

- **URL**: <https://paineldecompras.economia.gov.br/>
- **What it is**: aggregated analytical dashboard built on Comprasnet
  data.
- **Useful for**: descriptive aggregates without needing the raw API.

### Audesp (TCE-SP)

- **URL**: <https://www.tce.sp.gov.br/audesp>
- **What it is**: Auditoria Eletrônica de Órgãos Públicos. Mandatory
  reporting system for São Paulo state municipalities — uploads
  detailed procurement and contract data (licitações, ajustes,
  empenhos, with firm CNPJ identifiers).
- **Access**: limited public download; the underlying data is more
  accessible via TCE-SP open data portal and via direct request.
- **Coverage**: 644 non-capital São Paulo municipalities.
- **Useful for**: the canonical source for São Paulo municipal
  procurement research.
- **See**: [`topics/tribunais-contas.md`](topics/tribunais-contas.md),
  [`topics/licitacoes.md`](topics/licitacoes.md).

### Other state TCEs

- Most state Tribunais de Contas have some open data portal, but
  quality and coverage vary enormously. Examples:
  - **TCE-MG**: <https://www.tce.mg.gov.br/>
  - **TCE-RJ**: <https://www.tce.rj.gov.br/>
  - **TCE-PR**: <https://www1.tce.pr.gov.br/>
  - **TCE-RS**: <https://portal.tce.rs.gov.br/>
- **TCE-MG SIACE-LRF** publishes municipal fiscal data quarterly.
- **For São Paulo capital**: TCM-SP (separate from TCE-SP).

### CADE — Processos Administrativos

- **URL**: <https://www.gov.br/cade/pt-br>
- **What it is**: administrative cartel and merger cases at CADE.
  Per-process detail with documents (often heavily redacted) plus
  the aggregated annual reports.
- **Access**: web search + per-case detail pages. Bulk export limited.
- **Useful for**: cartel-prosecution research, merger control.
- **See**: [`topics/licitacoes.md`](topics/licitacoes.md),
  [`topics/anticorrupcao-penal.md`](topics/anticorrupcao-penal.md).

---

## Fiscal and federalism

### SICONFI (Sistema de Informações Contábeis e Fiscais do Setor Público Brasileiro)

- **URL**: <https://siconfi.tesouro.gov.br/>
- **What it is**: STN's unified portal for fiscal and accounting
  data of all three federative levels (União, estados, municípios).
  Includes RREO, RGF, DCA (Declaração de Contas Anuais), MSC
  (Matriz de Saldos Contábeis).
- **Access**: API + bulk download per municipality and year.
- **Coverage**: 5,570 municipalities + 26 states + DF + União.
  Annual through ~2002 with monthly granularity for some series.
- **basedosdados**: `br_me_siconfi`.
- **Useful for**: the single most comprehensive municipal fiscal
  source. Standardized across all levels.
- **See**: [`topics/federalismo-fiscal.md`](topics/federalismo-fiscal.md) §5,
  [`topics/contas-municipais.md`](topics/contas-municipais.md).

### SIOPS (Sistema de Informações sobre Orçamentos Públicos em Saúde)

- **URL**: <http://siops.datasus.gov.br/>
- **What it is**: standardized municipal/state health-spending
  reports, mandatory under LC 141/2012.
- **Coverage**: all Brazilian municipalities, ~2000–present.
- **Access**: web interface + downloadable per município/state.
- **Useful for**: studies of municipal health spending,
  constitutional minimums (15% of own-source revenue rule).
- **See**: [`topics/federalismo-fiscal.md`](topics/federalismo-fiscal.md) §5.

### SIOPE (Sistema de Informações sobre Orçamentos Públicos em Educação)

- **URL**: <https://www.gov.br/inep/pt-br>
- **What it is**: equivalent of SIOPS for education spending.
- **Coverage**: all Brazilian municipalities.
- **Useful for**: studies of municipal education spending and FUNDEB
  outcomes.

### FINBRA (Finanças do Brasil) — legacy

- The legacy STN database, largely absorbed into SICONFI. Older
  series (pre-2014) are sometimes more accessible via FINBRA than
  SICONFI.
- **URL**: <https://www.tesourotransparente.gov.br/temas/financas-publicas/financas-publicas>

### Tesouro Transparente

- **URL**: <https://www.tesourotransparente.gov.br/>
- **What it is**: federal-level fiscal data, debt management, RREO at
  the federal level.

### CFM — Compensação Financeira pela Exploração Mineral (CFEM)

- **URL**: <https://app.anm.gov.br/>
- **What it is**: ANM (Agência Nacional de Mineração) data on mining
  royalties (CFEM). Per-municipality royalty distributions.
- **Useful for**: studies using mining-windfall identification.

### Royalties petrolíferos (pre-sal)

- **URL**: <https://www.gov.br/anp/>
- **What it is**: ANP data on oil royalty distributions per
  município/state.

### Receita corrente líquida (RCL)

- Computed by each entity and published in RGF reports (in SICONFI).
  No single canonical national series — derived from SICONFI for
  cross-municipal work.

---

## Health (DATASUS)

### DATASUS — TabNet

- **URL**: <http://www2.datasus.gov.br/DATASUS/index.php?area=02>
- **What it is**: the unified portal for SUS health data. Microdata
  via TabNet (web tabulator) and bulk DBC files.
- **Subsets**:
  - **SIH** (Sistema de Informações Hospitalares) — hospital
    admissions (AIH).
  - **SIA** (Sistema de Informações Ambulatoriais) — ambulatory
    procedures.
  - **SIM** (Sistema de Informações de Mortalidade) — death records.
  - **SINASC** (Sistema de Informações de Nascidos Vivos) — birth
    records.
  - **SINAN** (Sistema de Informação de Agravos de Notificação) —
    notifiable diseases.
  - **SISAB** (Sistema de Informação em Saúde para a Atenção Básica)
    — primary care registry.
  - **SI-PNI** — immunizations.
  - **CNES** (Cadastro Nacional de Estabelecimentos de Saúde) —
    facility registry.
- **Access**: TabNet web interface + bulk DBC files (datasus.saude.gov.br
  FTP). Multiple Python and R packages exist for parsing DBC
  (`microdatasus` in R; `pysus` in Python).
- **basedosdados**: partial coverage in `br_ms_*` (SIM, SINASC,
  SIH, SIA, SISAB, CNES).
- **License**: public, with caveats around small-area patient
  identifiability.

### Cadastro Nacional de Estabelecimentos de Saúde (CNES)

- See above (part of DATASUS).
- **Useful for**: facility-level data on hospitals, clinics, beds,
  doctors per município.

### Mais Médicos

- Historical data on Mais Médicos placements available via SUS portal
  and academic replication archives. No single canonical bulk source.

---

## Education

### INEP — Censo Escolar

- **URL**: <https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar>
- **What it is**: annual census of all Brazilian schools (~180k
  schools), students, teachers. School-level microdata available
  for download.
- **Coverage**: 1995–present (modern format from ~2007).
- **basedosdados**: `br_inep_censo_escolar`.
- **Useful for**: school-level outcomes, teacher characteristics,
  enrollment.

### INEP — ENEM (Exame Nacional do Ensino Médio)

- **URL**: <https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enem>
- **What it is**: national high-school exit exam. Microdata with
  per-student scores, demographic info, school identifier.
- **Coverage**: 1998–present.
- **basedosdados**: `br_inep_enem`.

### INEP — SAEB / Prova Brasil / IDEB

- **URL**: <https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb>
- **What it is**: standardized assessment of basic education.
  School-level scores published as IDEB.
- **basedosdados**: `br_inep_saeb`, `br_inep_ideb`.

### INEP — Censo da Educação Superior

- Annual census of higher education institutions and students.
- **basedosdados**: `br_inep_censo_educacao_superior`.

### FUNDEB data

- Distribution data via STN and the FNDE.
- **URL**: <https://www.gov.br/fnde/>

---

## Economic and labor

### RAIS (Relação Anual de Informações Sociais)

- **URL**: <https://www.gov.br/trabalho-e-emprego/pt-br>
- **What it is**: mandatory annual reporting by all formal-sector
  employers. Worker-level: hire/separation dates, wages, occupation
  (CBO), establishment, education. Establishment-level: CNPJ, sector
  (CNAE), location (município).
- **Access**: bulk microdata under restricted-use access (signed data
  use agreement). Public aggregates available.
- **Coverage**: 1985–present, comprehensive after 2003.
- **basedosdados**: `br_me_rais`.
- **Useful for**: the canonical source for Brazilian labor-market
  research. Linkable to firms and workers via CPF/CNPJ.

### CAGED (Cadastro Geral de Empregados e Desempregados)

- **URL**: same as RAIS.
- **What it is**: monthly hires/separations in the formal sector.
- **Access**: monthly bulk files; aggregates public, microdata
  restricted.
- **Coverage**: 1992–present.
- **basedosdados**: `br_me_caged`.

### IBGE — PNAD Contínua

- **URL**: <https://www.ibge.gov.br/estatisticas/sociais/trabalho/>
- **What it is**: continuous national household survey covering
  labor force, income, household characteristics.
- **Access**: microdata download + IBGE Sidra portal for aggregates.
- **basedosdados**: `br_ibge_pnadc`.

### IBGE — Censo Demográfico

- **URL**: <https://www.ibge.gov.br/estatisticas/sociais/populacao/22827-censo-demografico-2022.html>
- **What it is**: decennial census. Latest: 2022 (released
  progressively 2023–2024). Pre-2022: 2010, 2000, 1991.
- **Access**: per-municipality aggregates via Sidra; sample
  microdata (10–25% sample) via IBGE.
- **basedosdados**: `br_ibge_censo_demografico`.

### IBGE — Estimativas anuais de população

- Annual population estimates per municipality (used to update FPM
  coefficients). Released annually around August.
- **URL**: <https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-populacao.html>

### IBGE — PIB Municipal

- Annual GDP per município, with sectoral breakdown.
- **basedosdados**: `br_ibge_pib`.

### BCB — Sistema Gerenciador de Séries Temporais (SGS)

- **URL**: <https://www3.bcb.gov.br/sgspub/>
- **What it is**: Brazilian Central Bank time series — interest rates,
  monetary aggregates, exchange rates, credit, inflation.
- **Access**: web interface + REST API + Python wrappers.
- **Useful for**: macro time series.

---

## Firms and taxation

### Receita Federal — CNPJ base (Cadastro Nacional da Pessoa Jurídica)

- **URL**: <https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/cnpj>
- **What it is**: registry of all legal entities (firms, foundations,
  associations) operating in Brazil. Includes razão social, CNAE,
  endereço, sócios (shareholders/partners), capital social.
- **Access**: bulk download (large; updated periodically). Per-CNPJ
  lookup via web interface.
- **basedosdados**: `br_receita_federal_cnpj`.
- **Useful for**: foundational firm-level data; linkable to
  procurement (Comprasnet, Audesp), employment (RAIS), and political
  donations (TSE).
- **See**: [`pipelines/cnpj`](../../pipelines/cnpj/) for one
  community-maintained snapshotting effort.

### Receita Federal — sócios (corporate ownership)

- Same source as CNPJ base. Each CNPJ has linked records of *sócios*
  (with CPF, name, role, ownership share). The basedosdados table
  includes this.
- **Useful for**: corporate-network analysis, ultimate ownership.

### JUCESP / state JUCESPs (juntas comerciais)

- State commercial registries. Per-state, varied access. JUCESP (São
  Paulo): <https://www.jucesponline.sp.gov.br/>.
- **Useful for**: when you need information not in the federal CNPJ
  base (e.g., specific state filings).

### CADE — Sistema Eletrônico de Informações (SEI)

- **URL**: <https://sei.cade.gov.br/sei/>
- **What it is**: per-process documents from CADE administrative
  proceedings (cartel cases, merger reviews).

---

## Anti-corruption and sanctions

### CEIS — Cadastro Nacional de Empresas Inidôneas e Suspensas

- **URL**: <https://portaldatransparencia.gov.br/sancoes/ceis>
- **What it is**: public list of firms barred from contracting with
  the public administration due to sanctions under Lei 8.666,
  Lei 14.133, Lei 12.846, etc.
- **Access**: web search + bulk download (CSV).
- **Useful for**: linking firm-level corruption sanctions to
  procurement and political activity.
- **See**: [`topics/anticorrupcao-penal.md`](topics/anticorrupcao-penal.md) §5,
  [`topics/cgu-controle-interno.md`](topics/cgu-controle-interno.md) §4.

### CNEP — Cadastro Nacional de Empresas Punidas

- **URL**: <https://portaldatransparencia.gov.br/sancoes/cnep>
- **What it is**: public list of firms specifically sanctioned under
  Lei Anticorrupção (Lei 12.846/2013).
- **Access**: web + bulk CSV.

### CEPIM — Cadastro de Entidades Privadas Sem Fins Lucrativos Impedidas

- **URL**: <https://portaldatransparencia.gov.br/sancoes/cepim>
- Public list of impeded private non-profit entities.

### CGU PFS — Programa de Fiscalização por Sorteios

- **URL**: <https://www.gov.br/cgu/pt-br/assuntos/auditoria-e-fiscalizacao>
- **What it is**: CGU's random municipal audit reports (2003–2015).
  Reports per-municipality with detailed irregularities classified
  by type and severity.
- **Access**: PDF reports per audit; **canonical replication
  datasets** from Ferraz–Finan and Avis–Ferraz–Finan papers.
- **Coverage**: 2003–2015 (40 lotteries). Post-2015 audits use
  risk-based selection.
- **Useful for**: the canonical Brazilian RD on corruption — see
  [`quasi-experimentos.md`](quasi-experimentos.md) §1.
- **See**: [`topics/cgu-controle-interno.md`](topics/cgu-controle-interno.md) §3.

### Portal da Transparência (federal)

- **URL**: <https://portaldatransparencia.gov.br/>
- **What it is**: federal expenditures, transfers (convênios, SUS,
  FPM, FUNDEB), servant salaries, beneficiaries of social programs.
  Maintained by CGU.
- **Access**: web interface + bulk downloads + some API endpoints.
- **See**: [`topics/transparencia-dados.md`](topics/transparencia-dados.md) §3.

### SICONV / Plataforma +Brasil

- **URL**: <https://www.gov.br/plataformamaisbrasil/>
- **What it is**: federal convênios with states, municipalities, and
  civil society entities. Agreement terms, values, execution,
  payments.
- **Useful for**: research on federal-subnational transfers and
  political alignment.

---

## Geographic and demographic

### IBGE — Malhas geográficas

- **URL**: <https://www.ibge.gov.br/geociencias/downloads-geociencias.html>
- **What it is**: shapefiles for municípios, microrregiões,
  mesorregiões, estados, grade estatística, biomas, etc.
- **Coverage**: per census year (2000, 2010, 2022).
- **Useful for**: any GIS work on Brazilian municípios.

### IBGE — Códigos de municípios

- 7-digit IBGE codes are the canonical municipal identifier in
  Brazilian data. Different sources use different prefixes (e.g.,
  TSE uses its own codes — TSE → IBGE crosswalk needed).
- **basedosdados**: `br_bd_diretorios_brasil` (the canonical
  crosswalk).

### INPE — TerraBrasilis

- **URL**: <http://terrabrasilis.dpi.inpe.br/>
- **What it is**: deforestation monitoring (PRODES, DETER), fire
  events, land-use change.

### IBGE — Sidra

- **URL**: <https://sidra.ibge.gov.br/>
- **What it is**: aggregated statistical tables — IBGE's main
  query interface for non-microdata.

---

## Transparency portals (LAI infrastructure)

### Portal da Transparência

- See above (federal expenditures).

### e-SIC / Fala.BR

- **URL**: <https://falabr.cgu.gov.br/>
- **What it is**: federal LAI request intake system. Maintained by
  CGU.
- **Useful for**: when public data isn't accessible elsewhere — file
  a LAI request.
- **See**: [`topics/transparencia-dados.md`](topics/transparencia-dados.md) §1.

### State and municipal transparency portals

- Each state and municipality must maintain LAI compliance, but
  implementation quality varies enormously. CGE-SP (Controladoria
  Geral do Estado de São Paulo) is the most institutionalized state
  example.

---

## Sources requiring scraping

These sources have public web interfaces but no bulk download. Building
a dataset means scraping (with the usual caveats: rate limiting, terms
of service, ongoing maintenance).

- **TJSP first-instance sentenças** — [esaj.tjsp.jus.br](https://esaj.tjsp.jus.br/cpopg/open.do).
  CAPTCHA in places. Schema captured by case classes (CNJ TPU).
- **Other state TJ consultas processuais** — every state has one;
  format varies by software vendor (Softplan ESAJ, PJe, others).
- **Diários Oficiais** — most states publish DOEs as PDFs only;
  some have web search but no bulk export.
- **Câmaras municipais atas** — typically PDF only.
- **Specific TCEs** that don't expose Audesp-style data — case-by-
  case scraping.
- **STF case detail pages** — searchable but no bulk export.

---

## Cross-references

- [`topics/partidos-e-sistema-eleitoral.md`](topics/partidos-e-sistema-eleitoral.md)
  — institutional context for TSE data.
- [`topics/federalismo-fiscal.md`](topics/federalismo-fiscal.md) — institutional
  context for SICONFI, SIOPS, FPM, etc.
- [`topics/tribunais-contas.md`](topics/tribunais-contas.md) — institutional context
  for Audesp and TCE data.
- [`topics/licitacoes.md`](topics/licitacoes.md) — institutional context for
  Comprasnet, Audesp, CADE.
- [`topics/improbidade.md`](topics/improbidade.md) — institutional context for
  TJSP improbidade case data.
- [`topics/cgu-controle-interno.md`](topics/cgu-controle-interno.md) — CGU PFS
  random audits, CEIS/CNEP.
- [`topics/cnj-administracao-judicial.md`](topics/cnj-administracao-judicial.md) —
  DataJud, CNJ Painéis, Justiça em Números.
- [`topics/transparencia-dados.md`](topics/transparencia-dados.md) — LAI/LGPD,
  Portal da Transparência, judicial data regime.
- [`quasi-experimentos.md`](quasi-experimentos.md) — natural
  experiments using these data sources.
- [`faq.md`](faq.md) — common research questions, including data
  access questions.

---

## Adding to this file

When you find a data source that should be listed here:

1. **Confirm it's public** — no private scrapes, no datasets that
   require an institutional agreement that not all readers can sign.
2. **Add to the right topic section**, or create a new one.
3. **Compact format**: name, URL, one-line description, access method,
   coverage, basedosdados table ID if applicable, license, cross-ref.
4. **Don't enumerate every column** — that's what the source's own
   data dictionary is for. Link to it.
5. **Note known scraping requirements** explicitly so readers don't
   waste time looking for an API that doesn't exist.
