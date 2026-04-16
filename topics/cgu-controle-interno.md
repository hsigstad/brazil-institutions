# CGU — Controladoria-Geral da União

Federal internal-control body charged with auditing federal spending,
including the use of federal transfers by states and municipalities,
preventing corruption, and enforcing corporate anti-corruption rules.
CGU is an internal-control organ (*controle interno*), distinct from
TCU which is an external-control organ — both scrutinize federal
expenditure but from different constitutional positions.

This file is important for two lines of research: (1) the audit-based
literature that exploits the **CGU random municipal audit program**
(Ferraz–Finan, Avis–Ferraz–Finan, many others) for causal identification,
and (2) corporate liability under the **Lei Anticorrupção** (`LAC`).

**Topics / keywords**: CGU, Controladoria-Geral da União, municipal
audit, random audit, Programa de Fiscalização por Sorteios, PFS,
fiscalizações, lottery audit, Ferraz Finan, controle interno, PAD,
processo administrativo disciplinar, Lei Anticorrupção, acordo de
leniência, CEIS, CNEP, transparência, inabilitação.

**Snapshot as of 2026**: CGU's name and institutional position have
changed several times. Reformulated as **Ministério da Transparência,
Fiscalização e Controle (MTFC)** under Temer (2016), then renamed
**Ministério da Transparência e Controladoria-Geral da União** (Lei
13.341/2016). Restored to "CGU" under the 2019 Bolsonaro restructuring,
and continues as CGU through 2026. The random municipal audit program
ran under that name 2003–2015 (40 lotteries) before the program was
reformulated.

---

## 1. Constitutional and statutory basis

### Controle interno (`CF.74`)

The Constitution requires each branch (Legislativo, Executivo, Judiciário)
to maintain an integrated **sistema de controle interno** with four
explicit objectives:

1. Evaluate compliance with the goals of the PPA, LDO, LOA.
2. Verify the legality and evaluate the results of public management.
3. Exercise control over credit operations, guarantees, rights, and
   obligations.
4. Support external control (i.e., TCU).

CGU is the federal Executivo's internal control organ fulfilling these
obligations.

### Statutory basis

- **Lei 10.683/2003** created the CGU (earlier named *Corregedoria-Geral
  da União*, 2001). Structured CGU as the central internal-control body
  for federal Executivo.
- **Lei 13.341/2016**: reorganized the federal ministerial structure
  under Temer; CGU became *Ministério da Transparência, Fiscalização e
  CGU*. Preserved core competences.
- **Lei 13.844/2019**: further restructuring under Bolsonaro; CGU
  continues as a ministry-level body.
- **Decreto 11.331/2023** (Lula III): current CGU structure and
  competences (subject to further reorganization).

---

## 2. Core functions

CGU historically has four pillars:

### (a) Auditoria — auditing federal expenditure

- **Auditoria contábil, financeira, orçamentária, operacional,
  patrimonial** of federal agencies and federal funds transferred to
  states/municipalities.
- The main instrument for verifying how federal money is spent at the
  subnational level is the **municipal audit program** (next section).
- Audits produce relatórios made available to the MP, TCU, and (in
  redacted form) to the public.

### (b) Corregedoria — disciplinary oversight of federal servants

- **PAD — Processo Administrativo Disciplinar**: formal investigation
  and sanction of federal civil servants for administrative infractions.
  Legal basis: `L8112` (regime jurídico dos servidores federais),
  Arts. 143–182.
- **Sindicância**: lighter fact-finding procedure for minor allegations
  or preliminary investigation before PAD.
- Sanctions: advertência, suspensão, **demissão**, cassação de
  aposentadoria, destituição de cargo em comissão.
- CGU Corregedoria coordinates correcional action across federal
  agencies through the **Sistema de Correição do Poder Executivo Federal**
  (SISCOR), instituted by Decreto 5.480/2005.

### (c) Ouvidoria — complaint intake and citizen interface

- Central ouvidoria for federal government; coordinates the network of
  ouvidorias within federal agencies.
- Receives denúncias, which may feed into audits or PADs.

### (d) Transparência and prevention

- **Portal da Transparência** (*portaltransparencia.gov.br*): public
  database of federal expenditures, transfers, contracts, servant
  salaries. CGU operates it. See `transparencia-dados.md`.
- **Promoting integrity and ethics programs** within federal agencies.
- **Coordinating the federal response to `LAI`** (Lei de Acesso à
  Informação) — CGU is the recurso hierárquico
  authority for denied LAI requests within the federal Executivo.

---

## 3. The municipal audit program (PFS — Programa de Fiscalização por Sorteios)

### What it was

- Launched **2003** by the Lula government as a mechanism to audit
  municipal use of federal transfers (FPM, SUS, FUNDEF, programs).
- **Random lottery selection**: municipalities drawn by public lottery
  (sorteio público), held in Caixa Econômica Federal headquarters,
  sometimes broadcast, in the presence of civil society and MP
  observers.
- Audits performed by CGU field teams: examination of documents
  (empenhos, notas, contratos), site visits, interviews, physical
  verification of completed works.
- Reports produced a structured list of irregularities per municipality,
  classified by severity and subject area (procurement, health,
  education, social programs).

### Why it matters empirically

- **Quasi-random assignment** of audit to municipalities makes the
  program the canonical identification strategy for causal estimates of
  the effect of audits (and of audit-revealed corruption) on a variety
  of outcomes.
- **Canonical papers**:
  - Ferraz & Finan (2008, *QJE*): electoral punishment of corrupt
    mayors revealed by audit.
  - Ferraz & Finan (2011, *AER*): effects of re-election incentives on
    corruption.
  - Avis, Ferraz & Finan (2018, *JPE*): deterrence effect of audits on
    future corruption.
  - The Ferraz–Finan–Monteiro line of work remains the canonical
    reference.

### Operational details

- **Lotteries ran 2003–2015**, ~40 rounds. Each lottery typically
  sampled ~60 municipalities (varied across rounds).
- **Population cap**: municipalities over some population threshold
  (initially ~500,000, later lifted) were excluded from the random
  pool and audited on a different basis.
- **Reports** published on CGU website with varying degrees of detail;
  canonical datasets used by researchers are constructed from these
  reports.

### What changed after 2015

- The program was **reformulated** under the name *Programa de
  Fiscalização em Entes Federativos* around 2015. The explicit random
  lottery was replaced by a risk-based / thematic selection model.
- **Implication for research**: the random-assignment property applies
  strictly to the 2003–2015 lotteries. Post-2015 audits are not
  randomly assigned and require different identification assumptions.

### Distinction from TCU audits

- **CGU** audits federal money wherever it flows (including to
  municipalities); CGU is **controle interno** of the Executivo.
- **TCU** audits federal expenditure from an **external** constitutional
  position; it reports to Congress and has its own jurisdiction over
  administrators of federal funds (`CF.71`). TCU does not focus on
  random municipal audits.
- A given municipal irregularity involving federal funds can be pursued
  by both CGU (internal control, referral to MP) and TCU (external
  control, direct sanction).

---

## 4. Lei Anticorrupção (`LAC`) — corporate liability

CGU is the federal authority for administrative enforcement of the
corporate anti-corruption statute. See `anticorrupcao-penal.md` for
full treatment; highlights here:

- **Objective liability** of legal entities for acts against national
  or foreign public administration (`LAC.1`).
- **Administrative sanctions** (`LAC.6`): fines (0.1% to 20% of gross
  revenue of the year before the filing of the administrative
  proceeding), publication of the sanction.
- **Judicial sanctions** (`LAC.19`): dissolution, asset freezing,
  prohibition from receiving public benefits.
- **Acordo de leniência** (`LAC.16`–`LAC.17`): firms can cooperate with CGU
  in exchange for reduced sanctions and immunity from certain
  additional liabilities. CGU's leniency authority is a significant
  lever in corporate anti-corruption enforcement.
- **CEIS — Cadastro Nacional de Empresas Inidôneas e Suspensas**
  (`LAC.23`): public list of firms barred from contracting with the
  public administration due to sanctions under `L8666`, `L14133`, or
  other statutes. Maintained by CGU.
- **CNEP — Cadastro Nacional de Empresas Punidas**: public list of
  firms sanctioned under `LAC` specifically.

**Source**: `LAC`; Decreto 8.420/2015 (regulamenta a `LAC`).

---

## 5. Interaction with other anti-corruption institutions

| Actor | Role | Competence | Relationship with CGU |
|---|---|---|---|
| **CGU** | Controle interno, Executivo federal | PAD servants, audit federal funds, `LAC`, `LAI` recourse | Self |
| **TCU** | Controle externo, Legislativo | Julga contas of administrators, `LOTCU` | Shares audit information; parallel jurisdiction |
| **MPF** | Prosecution, federal | Criminal + civil action on federal matters | CGU reports feed MPF inquéritos; joint action in acordos de leniência |
| **Polícia Federal** | Investigation | Criminal investigation | CGU triggers PF action via denúncia |
| **TCE / TCM** | Controle externo estadual/municipal | Julga contas municipais | CGU focuses on federal money; TCE on state/municipal money |
| **MPE** | Prosecution, state | Improbidade estadual | Parallel; CGU findings may trigger MPE action |

### Leniency agreement coordination

- A common procedural complication: firms under investigation may face
  parallel exposure under CGU (`LAC`), MPF (criminal), CADE
  (cartel), and TCU (audit). Historically, these agencies negotiated
  separately.
- **Post-2020 practice**: joint/coordinated leniency agreements are
  preferred, sometimes formalized by inter-institutional agreements (MoUs).
- CGU historically leads on `LAC` leniency; MPF typically
  leads on parallel criminal leniency.

---

## 6. Data and transparency infrastructure run by CGU

- **Portal da Transparência** — federal expenditures, transfers, contracts,
  servant salaries. Most used research source for federal spending data.
- **e-SIC / Fala.BR** — LAI request intake system for federal Executivo.
- **CEIS / CNEP** — sanctioned-firms registries.
- **Painel de Corregedoria** — aggregated PAD statistics.
- **Reports and manuals**: CGU publishes methodological guides,
  integrity-program templates, and audit reports.

See `transparencia-dados.md` for broader transparency infrastructure.

---

## 7. Research design implications

- **Pre-2015 CGU lotteries**: as-good-as-random municipal audits — the
  single most-used identification strategy in the Brazilian corruption
  literature. Any project that needs credible causal estimates of
  "the effect of audit exposure" should start here.
- **Post-2015**: non-random selection; need to model risk-based
  assignment or use other designs.
- **PAD records**: under LAI, sanctioned servants' decisions are
  publishable. Useful as an outcome or treatment in studies of
  disciplinary enforcement.
- **Leniency agreements (`LAC`)**: a small-N but high-salience dataset
  for corporate liability research.
- **Caveat on federal focus**: CGU is federal. State-level equivalents
  (controladorias estaduais, e.g., CGE-SP) exist but are less powerful
  and less studied.
