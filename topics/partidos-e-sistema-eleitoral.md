# Partidos e sistema eleitoral

Brazilian electoral system rules, party system, campaign finance, and
political eligibility. This file covers the *mechanics* of elections
and parties — who can run, how seats are allocated, how campaigns are
funded. For **electoral justice institutions** (TSE, TREs, electoral
procedure), see `justica-eleitoral.md` and `processo-eleitoral.md`. For
**campaign finance accounting specifically** (SPCE, filing rules, recibos),
see `prestacao-contas-eleitorais.md`.

**Topics / keywords**: sistema eleitoral, lista aberta, representação
proporcional, RP, majoritário, dois turnos, quociente eleitoral, sobras,
coligações, federações partidárias, cláusula de barreira, cláusula de
desempenho, fundo partidário, fundo eleitoral, FEFC, STF ADI 4650,
doação empresarial, Ficha Limpa, LC 64/90, inelegibilidade, EC 97/2017,
domicílio eleitoral, voto obrigatório, partidos políticos.

**Snapshot as of 2026**: major changes since 2015 have reshaped the party
system. (1) Corporate donations banned by `ADI4650` (September 2015).
(2) Coligações for proportional elections banned by `EC97-2017`, effective
from 2020 municipal elections onward. (3) Cláusula de desempenho phased
in from 2018; tighter thresholds apply each cycle through 2030 (`EC97-2017`).
(4) Federações partidárias introduced by Lei 14.208/2021, first used in 2022.
(5) Public Fundo Especial de Financiamento de Campanha (FEFC) created in
2017 to replace corporate money. Any pre-2018 research operates under a
fundamentally different party-system regime.

---

## 1. Offices and electoral cycles

### Elective offices (`CF.29`, `CF.45`, `CF.46`, `CF.77`)

| Office | Level | Term | Election type | Re-election |
|---|---|---|---|---|
| Presidente | Federal | 4 years | Majoritário, 2 turnos | 1× consecutive |
| Vice-presidente | Federal | 4 years | Chapa with Presidente | — |
| Senador | Federal (by state) | 8 years | Majoritário (1 or 2 per election, alternating) | Unlimited |
| Deputado federal | Federal (by state) | 4 years | Proporcional (open list) | Unlimited |
| Governador | Estadual | 4 years | Majoritário, 2 turnos | 1× consecutive |
| Vice-governador | Estadual | 4 years | Chapa with Governador | — |
| Deputado estadual / distrital | Estadual | 4 years | Proporcional (open list) | Unlimited |
| Prefeito | Municipal | 4 years | Majoritário (2 turnos only in munic. >200k) | 1× consecutive |
| Vice-prefeito | Municipal | 4 years | Chapa with Prefeito | — |
| Vereador | Municipal | 4 years | Proporcional (open list) | Unlimited |

### Eleições intercaladas (interleaved elections)

- **Federal/estadual cycle**: every 4 years, on the first Sunday of
  October. Second round (if needed) on the last Sunday of October.
  Presidente, governador, senador, deputado federal, deputado estadual
  elected together. **Last elections: 2022, 2026.**
- **Municipal cycle**: every 4 years, two years offset from
  federal/estadual. Prefeito and vereador. **Last elections: 2020, 2024.**
- This 2-year offset is a deliberate constitutional design feature
  meaning there is a major election in Brazil every 2 years.

### Two rounds (majoritário)

- **Presidente, governador**: second round if no candidate gets 50%+1
  of valid votes (excluding blanks and nulls) in the first round.
- **Prefeito**: second round applies **only** in municipalities with
  more than **200,000 registered voters** (`CF.29.II`).

### Senado — 1/3 + 2/3 alternation

- Each state elects 3 senadores (total 81).
- Elections alternate: in one cycle 1/3 of seats (1 per state) are
  renewed; in the next, 2/3 (2 per state) are renewed.
- 2022: 1 seat per state. 2026: 2 seats per state. Each senador serves 8
  years regardless.

---

## 2. Proportional representation (deputado/vereador)

Brazil uses **open-list proportional representation** (lista aberta) with
D'Hondt/largest-remainder seat allocation. The rules are in the
**Código Eleitoral** (`CE`), heavily modified over time.

### Quociente eleitoral (QE) and quociente partidário (QP)

- **Quociente eleitoral**: valid votes ÷ seats in the district.
- Parties (or federations) that reach the QE threshold win seats equal
  to the integer part of (party's valid votes ÷ QE) = quociente partidário.
- **Cláusula de desempenho individual** (`L13165`, amended by
  Lei 14.211/2021): a candidate must personally receive at least **10%
  of the quociente eleitoral** to take a seat under the QP. Candidates
  below this threshold do not take seats even if their party has QP slots.
- **Sobras** (remaining seats): distributed among parties that met the QE,
  by successive quotient (largest average). Post-2017 reforms allow
  parties that did *not* meet the QE to participate in the sobras under
  certain conditions.

### Open list

- Voters cast ballots for an individual candidate *or* a party (*voto
  de legenda*). Votes for individuals are counted toward the party total
  and also used to rank candidates within the party.
- Seats are filled in order of **individual vote count** within the
  party's candidate list.
- The **order of candidates on the ballot** has no effect: it is the
  individual vote count that decides.

### Districts

- For deputado federal / estadual: the **state** is the single district.
- For vereador: the **municipality** is the single district.
- Magnitude: varies from 8 (small states, minimum deputados federais) to
  70 (São Paulo). Median state magnitude ~10.

---

## 3. Coligações and federações partidárias

### Coligações (abolished for proportional, 2020)

- **Pre-2020**: parties could form electoral coalitions (*coligações*)
  that pooled votes for seat allocation purposes. In proportional
  elections, the coligação was treated as a single list for the QE
  calculation, generating notorious vote-transfer effects (a popular
  candidate from party A could "carry" weak candidates from party B
  into office).
- **Coligações for majoritário offices remain legal** (President,
  Governor, Prefeito, Senador).

### `EC97-2017` — ban on proportional coligações

- Constitutional amendment promulgated October 2017.
- **Prohibits coligações in proportional elections** (deputado federal,
  deputado estadual, vereador) starting from the **2020 elections**.
- Also introduced the *cláusula de desempenho* (§4 below).

### Federações partidárias (Lei 14.208/2021)

- To partially offset the loss of coligações, parties can form
  **federações** that behave as a single party for electoral and
  legislative purposes (for at least 4 years).
- Introduced by **Lei 14.208/2021** (amending `LPP`).
- Unlike coligações, a federação is a multi-year commitment: parties
  must remain federated for the full legislative term; dissolving
  carries sanctions.
- **First used in 2022**: Federação Brasil da Esperança (PT + PC do B +
  PV); Federação PSOL-REDE; Federação PSDB-Cidadania.

---

## 4. Cláusula de desempenho (cláusula de barreira)

Constitutional filter introduced by `EC97-2017`, tightening over
successive elections. Parties that fail to meet the threshold lose
access to the fundo partidário, TV/radio free airtime, and cannot
constitute a parliamentary bloc.

### Thresholds (deputado federal votes)

Applied to valid votes distributed over at least **9 states** with at
least **2% in each** — OR elect a minimum number of deputados federais
distributed over 9+ states.

| Election | Vote threshold | Deputado alternative |
|---|---|---|
| 2018 | 1.5% over 9 states (2% each) | Elect 9 dep fed over 9 states |
| 2022 | 2% over 9 states (2% each) | Elect 11 dep fed over 9 states |
| 2026 | 2.5% over 9 states (2.5% each) | Elect 13 dep fed over 9 states |
| 2030+ | 3% over 9 states (2% each) | Elect 15 dep fed over 9 states |

**Consequence of the cláusula**: several small parties have merged or
dissolved since 2018. The party system is slowly consolidating compared
to the pre-2018 fragmentation.

### Effect on federações

- Parties in a federação are evaluated **collectively** against the
  cláusula. This is the major institutional incentive for small parties
  to enter federations.

---

## 5. Party creation and discipline

### Forming a party

Governed by `LPP` (Lei dos Partidos Políticos).

- Registration at the TSE requires:
  1. An **organizing act** signed by minimum 101 founders from at
     least 9 different states.
  2. **Apoiamento de eleitores**: signatures from at least 0.5% of the
     votes cast in the last federal deputy election (excluding blanks/nulls),
     distributed across at least 1/3 of states with at least 0.1% in each.
- The TSE verifies the signatures and grants provisional/final registration.
- Brazil has historically had **30+ parties**; the number has been
  declining post-cláusula de desempenho.

### Janela partidária (party-switching window)

- Elected officials generally **lose their mandate** if they switch
  parties (TSE Res. 22.610/2007; later constitutionalized). The mandate
  belongs to the party, not the individual.
- **Exceptions** (TSE Res. 22.610/2007 as updated):
  - Creation of a new party.
  - Party merger or incorporation.
  - Grave personal discrimination within the party.
  - "Mudança substancial" in party program.
- **Janelas partidárias**: statutory windows (typically 30 days, 6
  months before elections) in which officials can switch parties
  without losing mandate. Most switches now happen in these windows.
- **Restrictions**: officials who switch outside the window without a
  valid cause lose the mandate via action filed by the party in the
  TSE.

### Discipline and expulsion

- Parties can expel members under internal rules (estatuto), but
  expulsion does not automatically cost the mandate.

---

## 6. Campaign finance

### Pre-2015 regime

- **Corporate donations allowed**, capped at 2% of gross revenue of the
  prior year.
- **Individual donations** capped at 10% of declarant's income.
- Campaigns dominated by corporate money; especially in federal and
  gubernatorial races, corporate donations represented the majority of
  campaign receipts for most candidates.

### `ADI4650` (decided September 2015)

- **Declared unconstitutional** the provisions of `LE` and
  `LPP` that permitted corporate donations to campaigns and
  parties.
- Effective from the **2016 elections** onward.
- Rationale: corporate donations distort political equality and create
  systematic dependencies between donors and elected officials.
- **Rel. Min. Luiz Fux**; approved by majority.

Canonical case entry: `ADI4650`.

### Post-2015 funding sources

1. **Fundo Partidário** (Fundo Especial de Assistência Financeira aos
   Partidos Políticos): public fund for party maintenance, predating
   ADI 4650. Funded by federal budget + fines + reserves. Distributed
   by TSE to parties (5% split equally among all registered parties;
   95% in proportion to votes received at last federal deputy election).
   Legal basis: `LPP.38`–`LPP.44`.
2. **FEFC — Fundo Especial de Financiamento de Campanha**: created by
   `L13487` specifically to replace corporate donations for
   campaign financing. Much larger than the fundo partidário.
   Distribution rules have changed multiple times; currently tied to
   party size in Congress and to self-declared candidate demographic
   criteria (women, Black candidates).
3. **Individual donations**: limited to 10% of declarant's gross income
   the year before (`LE.23`).
4. **Self-financing**: candidates can finance their own campaigns from
   their own resources, capped by the total expenditure limit for the
   office.

### Expenditure limits

- Set by `L13488` and adjusted by TSE resolutions per election.
- **Prefeito** (2016 cycle): max was 70% of the maximum spent in 2012
  elections for the same position in the same municipality (`L13165`
  Art. 5).
- Post-2018 reforms introduced inflation-adjusted monetary caps by
  election type and municipal/state size.

### Candidate accounting (SPCE)

- All donations received must be logged within **72 hours** in the
  Sistema de Prestação de Contas Eleitorais (SPCE).
- Recibo eleitoral required for donations above R$4,000 (pre-2018; check
  current thresholds).
- Expenditures by check or bank transfer except for very small amounts
  (<R$300 pre-2018; check current).
- See `prestacao-contas-eleitorais.md` for detailed filing mechanics.

### Enforcement

- The TSE rules on the *prestação de contas* of each candidate: **aprovação**,
  **aprovação com ressalvas**, **desaprovação**, or **não prestação**.
- **Não prestação**: candidate loses position; party loses fundo.
- **Desaprovação** may trigger ineligibility if it meets Ficha Limpa
  thresholds.

---

## 7. Ficha Limpa — inelegibilidade

Constitutional framework in `CF.14.§9`; regulated by
`LI` (Lei Complementar das Inelegibilidades), substantially
reformed by `LFL` (Lei da Ficha Limpa).

### Hypotheses of inelegibility (`LI.1`)

Not exhaustive, but the most consequential:

- `LI.1.I.e`: conviction for specified crimes (against public
  administration, crimes hediondos, racism, drug trafficking,
  electoral crimes) by a **collegiate body** (not just first-instance)
  — 8-year ineligibility from the completion of the sentence.
- `LI.1.I.g`: rejection of accounts related to public office by
  the competent organ, when the rejection (i) is due to insanable
  irregularity, (ii) constitutes ato doloso de improbidade, (iii) is
  by irrevocable decision — 8 years. **This is the improbidade /
  municipal accounts pathway**, see `contas-municipais.md`.
- `LI.1.I.h`: loss of office via cassação — 8 years.
- `LI.1.I.j`: conviction for electoral abuse or improper use of
  administrative/media power by electoral justice — 8 years.
- `LI.1.I.l`: conviction for improbidade administrativa that
  results in suspension of political rights — for the duration of the
  suspension + 8 years afterward.

### Key feature of `LFL`

- **Collegiate body sufficient**: pre-2010 inelegibility required a
  *final, unappealable* conviction; Ficha Limpa lowered this to a
  decision by a collegiate body, dramatically expanding the pool of
  ineligible candidates.
- The STF upheld constitutionality (ADC 29/30, ADI 4578, 2012) despite
  the *presunção de inocência* objection, on the ground that
  inelegibility is not a criminal sanction.

### Duration

- Typically **8 years** from the triggering event (conclusion of
  sentence, end of mandate, irrevocable decision, etc.).

Primary statutes: `LI`, `LFL`. STF ADC 29/30, ADI 4578 (constitutionality upheld, 2012).

---

## 8. Voting

### Obligations

- **Voto obrigatório** for citizens aged 18–69 (`CF.14.§1`).
- **Voto facultativo** for those 16–17, 70+, and illiterate.
- Penalty for abstention without justification: small fine + temporary
  loss of ability to obtain passport, renew ID, participate in public
  concursos, etc. (`CE.7`).

### Domicílio eleitoral

- Voters must register in a specific electoral district (domicílio
  eleitoral) where they habitually reside.
- Candidates must have electoral domicile in the district where they
  run for at least 6 months before the election (`LE.9`,
  post-reform period reduced from 1 year).

### Electronic voting

- Brazil uses **urnas eletrônicas** (electronic voting machines)
  introduced in 1996 and universal since 2000.
- Operated by the TSE; votes counted and totaled within hours of poll
  closure.

---

## 9. Research design implications

- **Pre-2015 vs. post-2015 campaign finance regime** is a sharp break:
  any study of donor effects, political alignment, or corruption
  exposure must distinguish regimes.
- **Ban on proportional coligações (from 2020)** changes the mapping
  from votes to seats — affects any study comparing pre-2020 and
  post-2020 legislative outcomes.
- **Cláusula de desempenho (from 2018)** alters the party system over
  time, making period-specific comparisons fraught.
- **Municipal second-round threshold (>200k voters)** is used as an RD
  in mayoral-reelection and political-competition studies (Brollo et al.,
  Ferraz & Finan, others).
- **Ficha Limpa as quasi-experiment**: the 2010 introduction and
  subsequent enforcement generated within-politician variation in
  eligibility.

See also:
- `justica-eleitoral.md` — TSE/TRE organization, electoral procedure.
- `processo-eleitoral.md` — AIJE, AIME, AIPRC, RCED, recursos.
- `prestacao-contas-eleitorais.md` — detailed campaign finance filing.
- `contas-municipais.md` — Ficha Limpa pathway for mayoral accounts.
- `improbidade.md` — `LI.1.I.l` ineligibility from improbidade
  convictions.

Primary statutes: `CE`, `LE`, `LPP`, `EC97-2017`, Lei 14.208/2021.
