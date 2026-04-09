# Federalismo fiscal

Fiscal framework of Brazilian federalism: how tax revenue is assigned
across União / estados / municípios, the intergovernmental transfer
system (FPM, FPE, SUS, royalties), municipal taxation, and LRF limits.
Essential context for any project that exploits municipal-budget
variation as a source of identification (saude, segredo, audit, decompose,
procure) or that treats municipal fiscal capacity as an outcome.

**Topics / keywords**: federalismo fiscal, FPM, FPE, ICMS, quota-parte,
transferências constitucionais, SUS, royalties, pre-sal, Lei Kandir,
LRF, personnel spending limit, receita corrente líquida, IPTU, ISS,
compensação financeira, cota-parte.

**Snapshot as of 2026**: the FPM/FPE coefficient structure and the LRF
personnel-spending limits are stable (constitutional / LC level). What
moves year to year: annually indexed thresholds, FPM coefficient
re-classification based on IBGE population estimates, new royalty
distribution rules for oil/mining, and post-reforma tributária transition
arrangements (EC 132/2023 phase-in begins 2026 with full effect by 2033).

Sourced from general knowledge + fragments in segredo and saude project
docs; not from a single project file.

---

## 1. Constitutional tax assignment

The 1988 Constitution divides tax competences across three federative
levels (Arts. 145–162 CF/88). Each level has its own exclusive taxes,
plus a system of mandatory revenue sharing.

### União (federal) taxes

- **IR** (imposto de renda) — Art. 153 III.
- **IPI** (imposto sobre produtos industrializados) — Art. 153 IV.
- **IOF** (operações financeiras) — Art. 153 V.
- **ITR** (territorial rural) — Art. 153 VI.
- **Importação / Exportação** — Art. 153 I, II.
- **Contribuições sociais** (PIS, COFINS, CSLL, contribuição
  previdenciária) — Arts. 195, 239.

### Estado / DF taxes

- **ICMS** (circulação de mercadorias e serviços) — Art. 155 II. **Largest
  single tax base in Brazil**; the state equivalent of a VAT.
- **IPVA** (veículos automotores) — Art. 155 III.
- **ITCMD** (transmissão causa mortis e doação) — Art. 155 I.

### Município taxes

- **IPTU** (propriedade predial e territorial urbana) — Art. 156 I.
- **ISS** (serviços de qualquer natureza) — Art. 156 III.
- **ITBI** (transmissão inter vivos de bens imóveis) — Art. 156 II.

### Reforma tributária — EC 132/2023

Promulgated December 2023. Replaces ICMS, ISS, IPI, PIS, COFINS with a
dual VAT:

- **CBS** (federal) — replaces PIS/COFINS.
- **IBS** (state + municipal) — replaces ICMS and ISS.
- **IS** ("imposto seletivo") — excise on goods harmful to health/environment.

Phase-in: 2026 pilot rates, full transition by 2033. Until transition
completes, the old tax system coexists with the new one. **For the bulk
of the project sample periods, the pre-EC 132 system is the relevant one.**

**Source**: [CF/1988 Arts. 145–162](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm); [EC 132/2023](https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc132.htm).

---

## 2. Intergovernmental transfers — the transfer-dependent municipality

Most Brazilian municipalities depend overwhelmingly on transfers rather
than own-source revenue. Small municipalities typically raise <10% of
total revenue locally; the rest comes from FPM, ICMS quota-parte, SUS,
FUNDEB, and other constitutional transfers. This is the fiscal reality
behind most municipal-level research designs.

### FPM — Fundo de Participação dos Municípios

The largest constitutional transfer to municípios.

- **Source**: 22.5% of IR + IPI (Art. 159 I b CF/88), with additional
  shares added by EC 55/2007 (+1%, July), EC 84/2014 (+1%, December),
  EC 112/2021 (more in Sept), bringing total by ~2026 to ~25.5% of
  IR+IPI.
- **Distribution**: by coefficient based on population tiers (Decreto-Lei
  1.881/1981 + LC 62/1989). **Capital cities** get 10% of the total;
  **interior municipalities** get 86.4%; the remainder goes to a reserve
  for larger interior municipalities (Lei 5.172/1966 Art. 91).
- **Interior coefficient structure**: 16 population-tier brackets. Small
  towns cluster in lower brackets; the coefficient is a step function of
  population, not continuous.
- **This step function is a canonical RD instrument** in the Brazilian
  empirical literature (Litschig & Morrison; Brollo et al.; many others).
  Population crosses into a higher bracket → discrete jump in FPM per
  capita.
- **Population estimates**: IBGE releases annual estimates; FPM
  coefficients for year t are set by TCU based on IBGE estimate published
  by August of year t−1. Rule changes in 2013 (LC 143/2013) altered the
  reclassification mechanics.

**Source**: [CF Art. 159](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm); [LC 62/1989](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp62.htm); [LC 143/2013](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp143.htm); Decreto-Lei 1.881/1981.

### FPE — Fundo de Participação dos Estados

- **Source**: 21.5% of IR + IPI (Art. 159 I a CF/88).
- **Distribution**: originally fixed coefficients from LC 62/1989 (declared
  unconstitutional by STF in ADI 875 et al., 2010, for perpetuating
  rigid shares). Replaced by **LC 143/2013**, which adopted a formula
  based on population and per-capita income, transitioning toward a
  more equalizing distribution.

### ICMS quota-parte (Art. 158 IV CF/88)

- States must transfer **25% of ICMS collected** to their municipalities.
- Distribution rule (Art. 158 §ú):
  - **At least 65%** proportional to the **value added** generated in
    the municipality (*valor adicionado fiscal*, VAF) — essentially
    commercial/industrial activity located there.
  - **Up to 35%** by state-defined criteria (typically population,
    environmental indicators, health/education outcomes).
- The VAF share creates strong incentives for municipalities to attract
  industrial activity and heavily shapes the geography of municipal
  finance.

### FUNDEB — Fundo de Manutenção e Desenvolvimento da Educação Básica

- Constitutional fund for basic education; states and municipalities
  contribute a share of specified taxes (20% of most state/municipal
  taxes); União tops up.
- Originally temporary (FUNDEF 1996, FUNDEB 2007) with sunset in 2020;
  made permanent by **EC 108/2020**.
- Federal complementation grew under EC 108 from 10% to 23% (phased).
- Distribution within each state is per-student-enrolled, weighted by
  education stage and modality.

**Source**: [CF Art. 212-A](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm) (post-EC 108); Lei 14.113/2020.

### SUS transfers

- **Constitutional minimum** (Art. 198 §2 CF/88, regulated by **LC 141/2012**):
  municipalities must spend **at least 15%** of own-source revenue on
  health; states **at least 12%**; União floor tied to nominal growth
  of receita corrente líquida (after EC 86/2015 and EC 95/2016).
- **Fundo-a-fundo transfers**: Ministério da Saúde transfers directly to
  municipal health funds based on population and pactuated programs.
  Components (pre-2017): PAB fixo + PAB variável + MAC + assistência
  farmacêutica. Restructured in 2017 (Portaria GM/MS 3.992/2017) into
  just two blocks: **Custeio** and **Investimento**.
- Relevant to the saude project and any municipal health-outcome design.

### Royalties (oil, mining, water)

- **Pre-sal royalties**: Lei 12.858/2013 dedicates 75% of União's pre-sal
  royalty share to education and 25% to health. Distribution formula
  among states/municipalities has been repeatedly litigated and changed
  (Lei 12.734/2012 was partially suspended by STF).
- **Mining (CFEM)**: Compensação Financeira pela Exploração de Recursos
  Minerais; distributed to municipalities where extraction occurs (60%),
  states (15%), União (10%), and affected/transportation municipalities
  (15%). Lei 13.540/2017 revised rates and distribution.
- **Royalty windfalls** have been used as natural experiments for
  spending responses (Caselli & Michaels; Monteiro & Ferraz).

### Convênios and transferências voluntárias

- Non-constitutional discretionary transfers from União (ministries) or
  estados to municipalities via signed agreements.
- Historically tracked in **SICONV / Plataforma +Brasil** (post-2019).
  Relevant to political-alignment research (mayor-governor /
  mayor-president alignment effects).
- **Lei 13.019/2014** regulates convênios with civil society entities.

---

## 3. Municipal own-source revenue

Small municipalities typically raise <10% of total revenue locally. The
key own-source taxes:

- **IPTU**: property tax on urban real estate. Collection effort varies
  enormously across municipalities; many small municípios under-collect
  due to outdated cadastros and political costs of reassessment. IPTU is
  a classic outcome in studies of fiscal effort.
- **ISS**: tax on services. Rate set by municipal law within federal
  floor/ceiling (2%–5%). Large municipalities earn substantial ISS;
  small ones minimal.
- **ITBI**: transfer tax on real estate transactions.
- **Taxas e contribuições**: fees for specific services, improvement
  contributions, public lighting contribution (COSIP, Art. 149-A CF/88).

### Fiscal effort vs. transfer dependence

Key stylized fact: municipalities that receive more in per-capita
transfers tend to exert **less** local fiscal effort. Analyzed extensively
in the Brazilian fiscal-federalism literature (Gadenne 2017 on Brazil
is the canonical empirical reference).

---

## 4. Lei de Responsabilidade Fiscal (LC 101/2000)

Foundational statute disciplining the fiscal behavior of all three
government levels. See also `contas-municipais.md` §5 for how LRF
violations feed into the TCE parecer and câmara judgment of mayoral
accounts.

### Personnel spending limits (Arts. 19–20)

Cap on **despesa total com pessoal** as a share of **receita corrente
líquida (RCL)**:

- **União**: 50% of RCL.
- **Estados**: 60% of RCL.
- **Municípios**: 60% of RCL, subdivided into:
  - **6%** for the câmara municipal (Legislativo);
  - **54%** for the Executivo.

**Alertas and sanctions**:
- **Limite de alerta** (90% of cap): TCE must warn.
- **Limite prudencial** (95% of cap): restrictions on new hiring, raises,
  overtime, contract creation.
- **Above 100%**: must be corrected within 2 quadrimestres (Art. 23);
  further non-compliance triggers transfer suspension, personal liability
  for the ordenador de despesas, and improbidade exposure.

### Debt limits (Arts. 29–30)

- Senado Federal sets debt ceilings by resolution for all levels.
- **Resolução SF 40/2001**: debt consolidated líquido cap of **120% of
  RCL** for municípios, **200% of RCL** for estados.

### Budget discipline

- **LDO / LOA / PPA** hierarchy (Arts. 165 CF/88): Plano Plurianual
  (4-year), Lei de Diretrizes Orçamentárias (annual guidelines), Lei
  Orçamentária Anual (annual budget).
- **Waiver of revenue** (*renúncia de receita*, Art. 14 LRF) requires
  compensating measures — constrains tax-break giveaways.
- **Geração de despesa obrigatória de caráter continuado** (Arts. 16–17)
  requires impact estimate and compensation.
- **Fiscal targets** (*metas fiscais*) set in annex to the LDO.

### Last-year-of-mandate restriction (Art. 42)

- Outgoing mayors/governors cannot incur spending obligations in the
  last two quadrimestres of their term that cannot be paid before the
  end of their mandate, unless there is sufficient cash.
- Common cause of improbidade prosecution (ordenador passing "restos a
  pagar" beyond available cash to successor).

**Source**: [LC 101/2000](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp101.htm).

### Receita corrente líquida (RCL) — the denominator

- Defined in Art. 2 IV LRF: sum of current revenue minus specified
  deductions (transfers to other federative levels, contribuições to
  social security, etc.), measured over the previous 12 months.
- The **relevant denominator** for all LRF percentage limits.
- Published by each federal entity on a bimonthly/quadrimestral basis in
  the Relatório Resumido de Execução Orçamentária (RREO) and Relatório
  de Gestão Fiscal (RGF).

---

## 5. Fiscal reporting and transparency

### Relatórios LRF

- **RREO** (Relatório Resumido de Execução Orçamentária): bimonthly;
  budgetary execution summary.
- **RGF** (Relatório de Gestão Fiscal): quadrimestral (annual for
  municipalities under 50k); fiscal limits compliance.
- Must be published electronically (LC 131/2009 — Lei da Transparência).

### SIOPS, SIOPE, FINBRA

- **SIOPS**: Sistema de Informações sobre Orçamentos Públicos em Saúde
  — standardized municipal health-spending reports. Data source for the
  saude project.
- **SIOPE**: analogous for education.
- **FINBRA** (Finanças do Brasil): STN's consolidated municipal fiscal
  database (now partially absorbed into **SICONFI** — Sistema de
  Informações Contábeis e Fiscais do Setor Público Brasileiro). Primary
  source for cross-municipal fiscal research.

**Source**: [LC 131/2009](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp131.htm).

---

## 6. Research design implications

- **FPM step function** → canonical RD for causal effects of municipal
  revenue (Litschig & Morrison; Brollo–Nannicini–Perotti–Tabellini on
  corruption).
- **ICMS VAF rule** → identification from industrial location shocks.
- **LRF personnel cap binding** → kink/threshold designs around the 60%
  limit.
- **Royalty windfalls** → time-varying instrument for spending.
- **Transfer vs. own-source composition** → drives political-economy
  research on accountability (Gadenne).

See also:
- `contas-municipais.md` — how LRF violations become TCE rejections and
  Ficha Limpa ineligibility.
- `tribunais-contas.md` — TCE audit of municipal accounts.
- `licitacoes.md` — procurement spending (the largest discretionary
  component of municipal budgets).
