# CNJ e administração judicial

The Conselho Nacional de Justiça (CNJ) oversees the administrative,
financial, and disciplinary management of the Brazilian judiciary. It
does not rule on legal merits — that remains with each court — but it
issues resoluções that bind judicial administration, publishes the
authoritative judicial-statistics series (Justiça em Números), and
coordinates the unified electronic case-management platform (PJe).

This file focuses on **judicial administration**: CNJ's normative power,
the main case-management systems (PJe, e-Proc, ESAJ), metadata and
data-release conventions, and specialization rules. For the
institutional composition of CNJ, see `cortes-superiores.md`. For
judicial career, discipline, and selection, see `carreira-juizes.md`.

**Topics / keywords**: CNJ, Conselho Nacional de Justiça, Justiça em
Números, PJe, Processo Judicial eletrônico, e-Proc, ESAJ, SAJ, CNPJ
tribunais, Tabelas Unificadas, SGT, Assuntos Processuais, CNAE-like
classification for cases, conciliação, Cejusc, Semana Nacional da
Conciliação, Resolução CNJ, especialização, varas especializadas,
combate à corrupção, vara de ações de improbidade, varas de fazenda
pública.

**Snapshot as of 2026**: CNJ Resoluções change frequently — any specific
resolution number cited here is a snapshot. The Tabelas Unificadas
governance model has been stable since Res. 46/2007. PJe is the
CNJ-sponsored unified platform but multiple tribunals still run e-Proc
(CJF-developed, used by TRFs and some TJs) or ESAJ (TJSP) alongside or
instead of PJe. Interoperability remains partial.

Built from general knowledge, fragments in `cortes-superiores.md`, and
the CNJ public documentation.

---

## 1. CNJ — mandate and normative power

### Creation

- Created by **EC 45/2004** (Reforma do Judiciário); installed in June
  2005.
- Constitutional basis: **CF Art. 103-B**.
- Composed of 15 conselheiros serving 2-year renewable terms (see
  `cortes-superiores.md` §1 for composition).

### Mandate (CF Art. 103-B §4)

- **Administrative and financial control** of the judiciary.
- **Disciplinary oversight** of judges and court employees.
- **Normative power** via **Resoluções CNJ**.
- **No merits jurisdiction**: cannot review or overturn judicial decisions
  on their legal substance.

### Resoluções CNJ

- Binding normative acts that regulate judicial administration across
  all courts.
- Published on the CNJ website and indexed by subject.
- **Key examples** relevant to research:
  - **Res. 46/2007**: Tabelas Processuais Unificadas (the authoritative
    classification schema for case types, subjects, and movements —
    §3 below).
  - **Res. 65/2008**: numeração única de processos (the modern case
    number format: `NNNNNNN-DD.AAAA.J.TR.OOOO`).
  - **Res. 121/2010**: publication of judicial data to enable
    transparency.
  - **Res. 125/2010**: *Política Judiciária Nacional de Tratamento
    Adequado dos Conflitos* — created Cejusc and mandated conciliation
    policy.
  - **Res. 185/2013**: PJe as the unified case-management platform for
    the judiciary.
  - **Res. 215/2015**: LAI applied to the judiciary.
  - **Res. 238/2016**: health-litigation specialization (relevant to
    `projects/saude`).
  - **Res. 331/2020**: management of PJe and procedural data standards.
  - **Res. 363/2021**: LGPD compliance in the judiciary.
  - **Res. 547/2024**: authorized judges to extinguish low-value
    execuções fiscais (≤R$10,000), triggering mass extinction of tax
    enforcement cases.
- When referring to a specific Resolução, **always cite the number and
  year** — numbers are reused as old resoluções are revoked or
  consolidated.

### Disciplinary oversight

- **Reclamação disciplinar** and **Processo Administrativo Disciplinar
  (PAD)** against judges (CNJ Regimento Interno Arts. 67–77).
- CNJ has concurrent disciplinary jurisdiction with each tribunal's
  **Corregedoria** and can avocate cases.
- Sanctions: advertência, censura, removal, aposentadoria compulsória,
  disponibilidade.

**Source**: [CF Art. 103-B](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm); [Resoluções CNJ (portal)](https://atos.cnj.jus.br/).

---

## 2. Justiça em Números — the authoritative statistics series

Annual statistical report published by CNJ, covering all branches of the
Brazilian judiciary.

- **Publication**: annual, typically late in the year (e.g., *Justiça em
  Números 2024* reports base-year 2023 data).
- **Coverage**: Justiça Estadual, Federal, do Trabalho, Eleitoral,
  Militar, Superior Tribunals.
- **Key indicators**:
  - New cases (*casos novos*), pending cases (*pendentes*), cases
    resolved (*baixados* and *julgados*).
  - Congestion rate (*taxa de congestionamento*): share of cases
    unresolved.
  - Productivity per judge (*IPM-Mag*, *IPM-Serv*).
  - Average case duration by phase (*tempo de tramitação*).
  - Expenditure per branch.
  - Conciliation rate by branch.
- **Underlying dataset**: aggregated by CNJ from tribunal-reported data;
  the micro-level underlying data are not released in Justiça em Números
  itself but are partially available through DataJud (below).
- Used extensively for Brazilian judicial research as the **authoritative
  macro-level reference**.

### DataJud

- **Base Nacional de Dados do Poder Judiciário (DataJud)**: CNJ
  initiative to centralize procedural data from all tribunals into a
  unified base. Provides a standardized data layer underlying Justiça
  em Números.
- Regulated by **Res. 331/2020**.
- Tribunals must feed DataJud on a monthly basis with structured case
  metadata.
- Access to DataJud for researchers has historically been limited;
  most research still relies on scraping tribunal-level web systems.

---

## 3. Tabelas Processuais Unificadas (TPUs)

CNJ Res. 46/2007 established the mandatory unified classification
schema for case metadata across all Brazilian courts. This is the
backbone of any structured analysis of court data.

### Three main tables

1. **Classe processual**: the formal class of the case (e.g.,
   *Procedimento Comum Cível*, *Ação Civil Pública*, *Execução Fiscal*).
   Classes form a hierarchical tree.
2. **Assunto**: the substantive subject matter (e.g.,
   *Direito Tributário → Crédito Tributário → Execução Fiscal*). Also
   hierarchical, with several thousand leaf nodes.
3. **Movimentação**: the types of procedural acts that can be recorded
   in a case (e.g., *Distribuição*, *Conclusão ao Juiz*, *Sentença*).

### Properties

- **Hierarchical**: each code has a parent, enabling aggregation.
- **Controlled vocabulary**: tribunals must use TPU codes in their case
  management systems; local codes are not valid for CNJ reporting.
- **Periodically updated**: new classes / assuntos are added by CNJ
  deliberation. Old codes are retired but remain valid for historical
  records.
- **Research use**: any cross-tribunal or longitudinal analysis must
  map to TPU to be comparable. When scraping from ESAJ or e-Proc,
  verify the TPU code is captured.

### CNJ case numbering (Res. 65/2008)

- Unified format: `NNNNNNN-DD.AAAA.J.TR.OOOO`
  - `NNNNNNN` — sequential number.
  - `DD` — check digit.
  - `AAAA` — filing year.
  - `J` — segmento do judiciário (1=STF, 2=CNJ, 3=STJ, 4=Federal,
    5=Trabalho, 6=Eleitoral, 7=Militar União, 8=Estadual, 9=Militar
    Estadual).
  - `TR` — tribunal (each TJ, TRT, TRE, TRF has a two-digit code).
  - `OOOO` — unidade de origem (vara, comarca, juizado).
- Example: `0007153-26.2009.8.26.0081` = sequential 0007153,
  check 26, year 2009, estadual (8), TJSP (26), vara 0081
  (Adamantina).
- **Implication**: the case number itself encodes the tribunal, year,
  and originating vara — useful for parsing without reading other fields.

---

## 4. Case management systems

### PJe — Processo Judicial Eletrônico

- **CNJ-sponsored** unified platform (Res. 185/2013).
- Intended to be adopted across all tribunals.
- **Adoption is partial**: as of 2026, most tribunais federais, a growing
  number of TJs, and the Justiça do Trabalho use PJe. TJSP remains on
  ESAJ; some TRFs use e-Proc.
- Interoperability via APIs is improving but still inconsistent.

### e-Proc

- Developed by CJF for the **Justiça Federal** (TRFs). Now also used by
  several TJs (notably TJRS).
- Widely considered more user-friendly than PJe; CNJ has debated
  consolidation but neither platform has fully displaced the other.

### ESAJ / SAJ

- Platform developed by **Softplan** and used by **TJSP** (the largest
  court in Brazil) and many other TJs.
- Proprietary; access is via TJSP's web consultation (*Consulta
  Processual*), with scrape-based research dominant.
- `projects/procure`, `projects/decompose`, `projects/electoral-justice`,
  and `projects/judgeGPT` rely on ESAJ data scraped from TJSP.

### Other systems

- Smaller tribunais may use Apolo, e-SAJ variants, or custom systems.
- The **Justiça do Trabalho** has a unified PJe deployment but historical
  data from pre-PJe systems is held separately and has uneven
  availability.

---

## 5. Specialization of varas and tribunais

### Specialization rules

- **CF Art. 96 I**: tribunals have constitutional authority to organize
  their own structure, including creating specialized varas.
- In practice, specialization is driven by:
  - Local caseload pressure (e.g., dedicated execução fiscal varas in
    large comarcas).
  - CNJ resoluções recommending specialization (health, environment,
    anti-corruption).
  - State law (estadual organization statutes).
- **Key examples**:
  - **Varas da Fazenda Pública**: specialized in cases involving public
    entities (state, municipalities, state-owned enterprises). Common
    in large comarcas.
  - **Varas de combate a crimes organizados e corrupção**: e.g., the
    13ª Vara Federal Criminal de Curitiba (Lava Jato), specialized
    varas in São Paulo and Rio.
  - **Varas especializadas em saúde**: CNJ Res. 238/2016 mandates
    specialized health-litigation varas in large comarcas.
  - **Varas cíveis vs. criminais**: the fundamental cível/criminal
    divide; most small comarcas have a single vara handling both.

### Implications for research

- **Case assignment quasi-randomness** depends on the specialization
  structure: within a specialized vara-group, assignment is typically
  random; across specialization types, it is deterministic by subject
  matter. Always document the specialization structure when claiming
  random assignment.
- **Judge identity is often recoverable** from the case number + vara
  + date, using tribunal lotações data.

---

## 6. Conciliation infrastructure

### Política Nacional de Tratamento Adequado de Conflitos (Res. 125/2010)

- CNJ committed the judiciary to a conciliation-first policy.
- Created the framework for **Cejusc** (Centros Judiciários de Solução
  Consensual de Conflitos) in every tribunal.

### Cejusc

- Specialized conciliation/mediation centers.
- Handle pre-litigation and in-process conciliation.
- Staffed by trained conciliators/mediators (often volunteers or
  interns under judge supervision).
- High conciliation rates in Cejusc-managed cases (e.g., Cejusc/TST
  achieved >68% conciliation in referred cases — see
  `justica-trabalho.md`).

### Semana Nacional da Conciliação

- Annual campaign (typically November) in which all tribunals
  concentrate conciliation efforts, with CNJ setting targets and
  tracking results.

### Conciliation rates by branch (see Justiça em Números 2019)

- **Justiça do Trabalho**: ~24% overall, 42.9% at first instance —
  highest among branches.
- **Justiça Estadual**: ~12% overall.
- **Justiça Federal**: ~8% overall.

---

## 7. The execução fiscal problem

A single largest source of judicial congestion. Relevant because it
distorts aggregate statistics and because recent CNJ action has altered
the case stock substantially.

- **Stock (end 2022)**: >27 million pending execuções fiscais, ~34–35%
  of total pending cases in the judiciary.
- **Congestion rate**: ~88% (Justiça em Números 2023).
- **Average duration**: 6 years and 7 months.
- **Distribution**: ~86% in state courts (state + municipal tax
  debts); remainder in federal courts.

### Res. 547/2024 — mass extinction

- Authorized judges to extinguish execuções fiscais ≤R$10,000 on
  economic-unviability grounds.
- Resulted in >10 million case extinctions in <2 years.
- Stock fell from 26.9M (Dec 2023) to ~16.5M (Dec 2025) — a ~37%
  reduction.
- **Implication**: post-2024 Justiça em Números statistics show sudden
  improvements in congestion rate that are driven by this administrative
  cleanup rather than by genuine changes in case processing.

---

## 8. Judicial data governance — what researchers should know

### Access mechanisms (in order of ease)

1. **Consulta Processual via web** — every tribunal offers basic web
   consultation. Limited to one case at a time, CAPTCHA-protected.
2. **Bulk exports** — some tribunals (e.g., TJSP for sentences) release
   bulk files. Quality and completeness vary.
3. **API access** — PJe has standardized APIs (not all enabled
   publicly); e-Proc and ESAJ have partial APIs.
4. **DataJud** — in principle the authoritative source, but researcher
   access is limited.
5. **CNJ Painéis** — aggregated dashboards for specific topics
   (improbidade, feminicídio, etc.), useful for descriptive work.
6. **LAI requests** — requests to tribunals for structured data can
   produce results but are inconsistent; appeal via CNJ.

### Data governance principles

- **Publicity is the rule** (CF Art. 93 IX), subject to segredo de
  justiça for specific case categories.
- **LGPD applies** to the judiciary but has its own balancing framework
  (CNJ Res. 363/2021). See `transparencia-dados.md` §4.
- **Anonymization for publication**: even where raw data is publicly
  accessible, academic publications should consider anonymizing
  identified parties, especially for victims, minors, and non-public
  figures.

### Common research pitfalls

- **Count of "cases" vs. "processos"**: a single *processo* can spawn
  multiple incidents, appeals, and derivative actions that may or may
  not be counted separately depending on the tribunal and the
  methodology.
- **Baixa vs. arquivamento**: a case "baixado" is closed administratively
  (e.g., sentence issued) but may not be "arquivado definitivamente"
  (final archiving after all appeals).
- **Tabelas Unificadas coverage**: older cases (pre-2007) use legacy
  classifications that do not map cleanly to TPU codes. Longitudinal
  work must document how the mapping was done.
- **Execução vs. conhecimento phases**: many case "durations" conflate
  the two phases; CNJ statistics break them out separately.

---

## 9. Cross-references

- `cortes-superiores.md` — CNJ composition, STF/STJ structure.
- `carreira-juizes.md` — judicial career, promotions, discipline.
- `justica-trabalho.md` — conciliation, case-assignment mechanics.
- `justica-estadual.md` — state-court organization.
- `justica-federal.md` — federal-court organization.
- `transparencia-dados.md` — LAI/LGPD as applied to judicial data.
- `data_catalog/` (workspace) — actual datasets derived from tribunal
  systems.

**Sources**: [CF Art. 103-B](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm); [Portal de atos CNJ](https://atos.cnj.jus.br/); [Justiça em Números](https://www.cnj.jus.br/pesquisas-judiciarias/justica-em-numeros/); [DataJud — Res. 331/2020](https://atos.cnj.jus.br/atos/detalhar/3412).
