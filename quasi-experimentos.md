# Quasi-experimentos — natural experiments in Brazilian institutions

Index of identification strategies and natural experiments embedded in
Brazilian institutional features. Each entry: the institutional source,
the cutoff/threshold/event, what it identifies, and the canonical
paper(s) that exploited it.

This file is for **empirical researchers** designing causal studies on
Brazilian institutions. It complements the topical files by surfacing
the parts of those institutions that researchers have used as sources
of variation.

**Topics / keywords**: natural experiment, quasi-experiment,
identification strategy, regression discontinuity, RD, difference in
differences, event study, instrument, IV, cutoff, threshold, treatment
effect, causal inference, Brazilian empirical literature.

**Snapshot as of 2026**: a representative but not exhaustive list. Many
of these have multiple variations and active replication / extension
work in the literature.

---

## Cross-references

For institutional context behind each entry, follow the cited file:
- [`topics/cgu-controle-interno.md`](topics/cgu-controle-interno.md) — CGU random audits
- [`topics/federalismo-fiscal.md`](topics/federalismo-fiscal.md) — FPM, FPE, royalties, LRF kinks
- [`topics/partidos-e-sistema-eleitoral.md`](topics/partidos-e-sistema-eleitoral.md) — electoral cutoffs and reforms
- [`topics/justica-trabalho.md`](topics/justica-trabalho.md) — labor reform shocks
- [`topics/improbidade.md`](topics/improbidade.md) — improbidade reform
- [`topics/contas-municipais.md`](topics/contas-municipais.md) — Ficha Limpa, voto secreto reforms
- [`topics/tribunais-contas.md`](topics/tribunais-contas.md) — TCE relator random assignment
- [`topics/anticorrupcao-penal.md`](topics/anticorrupcao-penal.md) — Lava Jato structural breaks
- [`jurisprudencia-stf.md`](jurisprudencia-stf.md) — STF rulings as cutoffs

---

## 1. CGU random municipal audits — the canonical Brazilian RD

**Institutional source**: Controladoria-Geral da União (CGU), *Programa
de Fiscalização por Sorteios* (PFS), 2003–2015.

**Mechanism**: ~40 lotteries held in Caixa Econômica Federal
headquarters, each randomly drawing ~60 municipalities for federal
audit. Audits produced detailed reports of irregularities classified by
type (procurement, health, education, social programs).

**Identifies**: causal effects of audit exposure (and audit-revealed
corruption) on a wide variety of outcomes: voting, future spending,
firm-level outcomes, future corruption, etc.

**Population restriction**: municipalities above certain population
thresholds (initially ~500k, later lifted) were excluded from the random
pool and audited on different criteria.

**Canonical papers**:
- Ferraz & Finan (2008, *QJE*) — electoral punishment of corruption
  revealed by audit.
- Ferraz & Finan (2011, *AER*) — re-election incentives and corruption.
- Avis, Ferraz & Finan (2018, *JPE*) — deterrence effects of audits on
  future corruption.
- Many extensions in the broader Ferraz–Finan–Monteiro literature.

**Caveat**: random assignment applies **strictly to 2003–2015**. After
2015, the program was reformulated as risk-based selection
(*Programa de Fiscalização em Entes Federativos*). Post-2015 audits are
not randomly assigned and require different identification assumptions.

**See**: [`topics/cgu-controle-interno.md`](topics/cgu-controle-interno.md) §3.

---

## 2. FPM step function — RD on municipal revenue

**Institutional source**: Fundo de Participação dos Municípios (FPM)
distribution rules under Decreto-Lei 1.881/1981 + LC 62/1989.

**Mechanism**: FPM coefficients for interior municipalities follow a
**step function** of population — 16 brackets, with discrete jumps in
per-capita FPM as a municipality crosses a bracket boundary. Population
estimates are published annually by IBGE; coefficients are set by TCU
for year *t* based on the IBGE estimate published by August of year *t−1*.

**Identifies**: effects of marginal increases in municipal revenue on
spending, public goods provision, electoral outcomes, corruption,
political competition, etc.

**Threshold detail**: bracket boundaries depend on population tier;
small towns cluster in lower brackets where the absolute jumps are
smaller but per-capita effects are larger.

**Reform**: LC 143/2013 altered the reclassification mechanics — verify
which regime applies for the period of interest.

**Canonical papers**:
- Litschig & Morrison (2013, *AEJ Applied*) — public spending and
  political effects.
- Brollo, Nannicini, Perotti & Tabellini (2013, *AER*) — corruption and
  political selection.
- Many extensions on health, education, infrastructure outcomes.

**See**: [`topics/federalismo-fiscal.md`](topics/federalismo-fiscal.md) §2 ("FPM").

---

## 3. 200k voter threshold for second-round mayoral elections

**Institutional source**: CF Art. 29 II.

**Mechanism**: in municipalities with **more than 200,000 registered
voters**, prefeito elections require a second round if no candidate
gets 50%+1 in the first round. In smaller municipalities, the
first-round plurality wins outright.

**Identifies**: effects of two-round elections vs single-round on
political competition, candidate selection, ideological positioning,
corruption, policy outcomes.

**Caveat**: the 200k threshold is on **registered voters**, not
population. The two are correlated but not identical (electorate
expansion or contraction can move a municipality across the threshold
without population change).

**Canonical papers**:
- Bordignon, Nannicini & Tabellini (2016, *AER*) — moderation effects.
- Multiple Brazilian replication / extension papers on corruption and
  selection.

**See**: [`topics/partidos-e-sistema-eleitoral.md`](topics/partidos-e-sistema-eleitoral.md) §1.

---

## 4. Ficha Limpa (LC 135/2010) — introduction shock

**Institutional source**: Lei Complementar 135/2010, amending LC 64/1990
Art. 1 I "g" (Ficha Limpa).

**Mechanism**: pre-2010, ineligibility for past convictions required
**trânsito em julgado** (final, unappealable conviction). Post-2010, a
**collegiate body decision** (não unipessoal) suffices, vastly
expanding the pool of ineligible candidates.

**Identifies**: effects of stricter eligibility rules on candidate
quality, political competition, voter behavior, and turnover. Also
within-politician variation: a politician convicted at first instance
in 2009 was eligible for the 2010 election; the same conviction
post-Ficha-Limpa ruling regime would render them ineligible.

**Constitutional confirmation**: STF ADC 29/30 + ADI 4578 (2012) upheld
the constitutionality despite presunção de inocência objections.

**Canonical papers**:
- Avis, Ferraz, Finan & Varjão (2022, *AEJ Applied*) and others on
  Ficha Limpa effects on electoral selection.

**See**: [`topics/partidos-e-sistema-eleitoral.md`](topics/partidos-e-sistema-eleitoral.md) §7,
[`topics/contas-municipais.md`](topics/contas-municipais.md) §3.

---

## 5. Reforma trabalhista (Lei 13.467/2017) — sharp filing-cost shock

**Institutional source**: Lei 13.467/2017, effective 11 November 2017.

**Mechanism**: pre-reform, Brazilian labor courts had **zero filing
costs** for workers and **no honorários de sucumbência** (loser-pays
attorney fees). The 2017 reform introduced custas (2% of claim value),
honorários (5–15%), no-show penalties, and tightened *justiça gratuita*
eligibility (40% RGPS ceiling, down from 2× minimum wage).

**Identifies**: effects of filing costs on litigation volume and
composition. The November 2017 cutoff produces:
- A **mass-filing spike** in November 2017 (workers rushing under old
  rules) — ~207k filings vs ~120k typical monthly volume.
- **34% drop** in 2018 vs 2017 filings.
- **Composition change**: speculative claims (*pedidos aventureiros*)
  dropped disproportionately.

**Partial reversal**: STF ADI 5766 (October 2021) struck down the
harshest cost provisions for *justiça gratuita* beneficiaries —
introduces a second discontinuity around October 2021.

**See**: [`topics/justica-trabalho.md`](topics/justica-trabalho.md) §"Filing costs"
and §"Impact on filing volumes".

---

## 6. STF ADI 5766 (October 2021) — partial reversal of reforma trabalhista

**Institutional source**: STF ADI 5766, decided 20 October 2021.

**Mechanism**: declared unconstitutional CLT Arts. 790-B caput/§4
(expert fees from credits) and 791-A §4 (honorários from credits in
other proceedings) for **justiça gratuita beneficiaries**. The ruling
restored partial pre-reform protection for low-income workers.

**Identifies**: heterogeneous effects of cost-regime reversal —
treatment effect differs by *justiça gratuita* status. The November
2017 to October 2021 window is the period of maximum filing-cost
deterrence; post-October 2021 is a partial restoration.

**See**: [`topics/justica-trabalho.md`](topics/justica-trabalho.md) §"STF ADI 5766",
[`jurisprudencia-stf.md`](jurisprudencia-stf.md) §3.

---

## 7. Lei 14.230/2021 — improbidade reform

**Institutional source**: Lei 14.230/2021, published 26 October 2021;
STF Tema 1199 (ARE 843.989, 18 August 2022) governs retroactivity.

**Mechanism**: eliminated culposa improbidade entirely; only **dolosa**
(intentional) conduct is now actionable. Centralized standing in MP
exclusively. New 8-year absolute prescription regime.

**Identifies**: effects of narrowing the improbidade standard on:
- Filing volume
- Conviction rates
- Type of conduct prosecuted
- Selection of cases pursued by MP

**Retroactivity nuance** (per STF Tema 1199):
- Cases with **trânsito em julgado** before the reform: irretroactive,
  past convictions stand.
- **Pending cases without final judgment**: new law applies; courts
  must re-examine intent.
- This creates a within-state-court pre/post comparison conditional on
  case status.

**See**: [`topics/improbidade.md`](topics/improbidade.md) §2,
[`jurisprudencia-stf.md`](jurisprudencia-stf.md) §1.

---

## 8. STF ADI 4650 (September 2015) — corporate donation ban

**Institutional source**: STF ADI 4650, decided September 2015,
Rel. Min. Luiz Fux. Effective from the **2016 elections** onward.

**Mechanism**: declared unconstitutional the provisions of Lei
9.504/1997 and Lei 9.096/1995 that permitted corporate donations to
campaigns and political parties. Corporate money was abruptly
prohibited; FEFC (public campaign fund, Lei 13.487/2017) was created
to partially replace it.

**Identifies**: effects of the campaign finance regime on:
- Candidate selection (especially incumbents who relied on corporate
  donations)
- Political competition
- Pork-barrel allocation
- Public-policy outcomes
- Connection between donor firms and policy

**Caveat**: the 2016 elections were the **first** affected — the
campaign finance regime has been unstable since (FEFC introduced,
expenditure caps changed, allocation rules altered).

**See**: [`topics/partidos-e-sistema-eleitoral.md`](topics/partidos-e-sistema-eleitoral.md) §6,
[`jurisprudencia-stf.md`](jurisprudencia-stf.md) §4.

---

## 9. EC 97/2017 — fim das coligações proporcionais

**Institutional source**: Emenda Constitucional 97/2017, promulgated
October 2017, effective from **2020** elections (proportional ban),
2018 elections (cláusula de desempenho phase-in).

**Mechanism**: prohibits coligações in proportional elections
(deputado federal, deputado estadual, vereador). Replaced by
**federações partidárias** (Lei 14.208/2021), which require multi-year
commitments.

**Identifies**: effects of removing vote-pooling on:
- Party fragmentation / consolidation
- Candidate selection within parties
- Vote-buying and brokerage networks
- Cross-party transfers (popular candidates "carrying" weak slate-mates)

**Cláusula de desempenho** (separate but related): tightening thresholds
2018 → 2022 → 2026 → 2030 generate within-party variation.

**See**: [`topics/partidos-e-sistema-eleitoral.md`](topics/partidos-e-sistema-eleitoral.md) §§3–4.

---

## 10. EC 76/2013 — voto aberto in Congress

**Institutional source**: Emenda Constitucional 76/2013, promulgated
28 November 2013.

**Mechanism**: abolished secret voting in Congress for cassação de
mandatos and appreciation of presidential vetoes. Triggered by the
**Natan Donadon case** (August 2013), where deputies in secret ballot
upheld the mandate of a congressman sentenced to 13 years for
embezzlement.

**Identifies**: effects of vote transparency on legislator behavior.
Within-Congress comparison: same legislators voting on similar matters
under different transparency regimes.

**Spillover**: served as a federal **precedent** for municipal câmara
reforms abolishing secret voting on contas de prefeito. Many municipal
reforms cite EC 76/2013 explicitly. This generates a *municipal-level*
diffusion process from ~2014 onward, with reforms staggered across
municipalities.

**See**: [`topics/contas-municipais.md`](topics/contas-municipais.md) §4
("EC 76/2013 — federal precedent" and "Municipal reform examples").

---

## 11. Municipal câmara voting modality reforms (~2004–2025)

**Institutional source**: each municipality's Lei Orgânica Municipal,
amended over time; no federal mandate.

**Mechanism**: pre-reform, many small municipalities used **secret
ballot** to vote on contas de prefeito. Reforms by câmara (often
prompted by MP recommendations or civil-society campaigns) amended the
Lei Orgânica to require **open nominal roll call**. The reform wave
diffused over two decades, accelerating after EC 76/2013.

**Identifies**: effects of voting transparency on:
- Whether câmara follows TCE recommendations
- Mayor accountability
- Selection of councilors
- Re-election rates

**Identification challenges**: reform timing is endogenous (politically
motivated), so DiD requires careful parallel-trends checks. Municipality
fixed effects + state-year FE help.

**See**: [`topics/contas-municipais.md`](topics/contas-municipais.md) §4 ("Municipal
reform examples").

---

## 12. TCE-SP relator random assignment

**Institutional source**: TCE-SP Regimento Interno (compilado, com
Resolução 16/2024), Art. 36 (random electronic draw) + Art. 38 (annual
contas with two-year exclusion rule).

**Mechanism**: each TCE-SP processo is assigned a relator (rapporteur
conselheiro) by **random electronic draw**. For mayoral contas, the
draw excludes the conselheiro who was relator in either of the two
preceding fiscal years. Once assigned, the relator becomes the
"julgador certo" for all subsequent acts in the same processo
(prevenção, Art. 40 IV).

**Identifies**: effects of relator characteristics
(harshness, ideology, career trajectory) on:
- Outcome of contas judgments
- Mayoral political careers
- Subsequent municipal behavior

**Caveat**: random assignment applies to the **initial** relator. Once
fixed, prevenção persists across appeals.

**See**: [`topics/tribunais-contas.md`](topics/tribunais-contas.md).

---

## 13. STF Tema 157 (RE 848.826) — câmara competence on mayoral accounts

**Institutional source**: STF, decided 10 August 2016, certified
18 October 2019. Vote 6–5.

**Mechanism**: clarified that the câmara municipal — not the TCE — is
the competent body for judging contas de prefeito for purposes of
Ficha Limpa ineligibility. After Tema 157, the câmara vote became the
single decision point for inelegibilidade under `LI.1.I.g`.

**Identifies**: effects of legal salience on câmara behavior. Pre-Tema
157, the câmara vote was politically meaningful but the legal stakes
were ambiguous. Post-Tema 157, the legal stakes are unambiguous —
câmara behavior may have shifted in response.

**Caveat**: the Tese was certified in October 2019, three years after
the decision. The "effective" date depends on whether you treat the
2016 decision or the 2019 certification as the cutoff.

**See**: [`topics/contas-municipais.md`](topics/contas-municipais.md) §2,
[`jurisprudencia-stf.md`](jurisprudencia-stf.md) §2.

---

## 14. Pre-sal royalty distribution shocks

**Institutional source**: Lei 12.858/2013, dedicating 75% of União's
pre-sal royalty share to education and 25% to health. Lei 12.734/2012
(partially suspended by STF) attempted to redistribute royalties more
broadly.

**Mechanism**: time-varying royalty windfalls to producing
municipalities (and earmark to specific spending categories). Multiple
court rulings altered the distribution rules across time.

**Identifies**: effects of windfall revenue on:
- Public spending composition
- Education and health outcomes
- Political behavior (re-election, corruption, accountability)

**Compare with**: mining royalties (CFEM, Lei 13.540/2017) which use a
different base and distribution formula.

**See**: [`topics/federalismo-fiscal.md`](topics/federalismo-fiscal.md) §2 ("Royalties").

---

## 15. LRF personnel-spending limit (Arts. 19–20)

**Institutional source**: LC 101/2000 (Lei de Responsabilidade Fiscal).

**Mechanism**: cap on personnel spending as a share of *receita
corrente líquida* (RCL): 60% for municipalities (54% Executivo + 6%
Legislativo). Three thresholds:
- **Limite de alerta** (90% of cap): TCE warning.
- **Limite prudencial** (95%): restrictions on new hiring/raises.
- **Above 100%**: must correct within 2 quadrimestres; further
  non-compliance triggers transfer suspension and personal liability.

**Identifies**: kink/threshold designs around the 60% limit. Effects of
binding LRF constraints on:
- Hiring decisions
- Wage policy
- Service delivery
- Audit/sanction outcomes

**Caveat**: RCL is itself endogenous to local economic conditions. The
kink works best when combined with other revenue shocks.

**See**: [`topics/federalismo-fiscal.md`](topics/federalismo-fiscal.md) §4.

---

## 16. Lava Jato as institutional shock

**Institutional source**: not a legal cutoff but an **operational
phenomenon** (2014–2021) that changed prosecutorial practice across
Brazilian institutions.

**Mechanism**: the Operação Lava Jato model (force-task with MPF + PF +
COAF + Receita Federal; aggressive use of colaboração premiada, leniency
agreements with corporations, prison execution after second-instance
conviction) became the template for subsequent corruption
investigations.

**Identifies**: effects of prosecutorial intensity on:
- Corporate investment behavior
- Political donation patterns
- Politician selection
- Electoral outcomes

**Cutoffs** (multiple, with different identifying variations):
- **2014**: operation begins.
- **HC 126.292 (2016)**: prison execution after second-instance
  conviction permitted. Imprisonment of high-profile defendants begins.
- **ADC 43/44/54 (Nov 2019)**: prison execution requirement reversed.
  High-profile defendants released.
- **STF Lula vs Moro (2021)**: incompetência da 13ª Vara Federal +
  parcialidade. Multiple convictions annulled.
- **Lei 13.964/2019 Pacote Anticrime**: tightens colaboração premiada
  formalities.
- **2021**: Lava Jato force task formally dissolved.

Each of these is its own quasi-experiment within the broader Lava Jato
era.

**See**: [`topics/anticorrupcao-penal.md`](topics/anticorrupcao-penal.md) §§7–9,
[`jurisprudencia-stf.md`](jurisprudencia-stf.md) §6.

---

## 17. Reforma tributária (EC 132/2023) — phase-in 2026–2033

**Institutional source**: Emenda Constitucional 132/2023, December 2023.
Phase-in begins 2026, full effect by 2033.

**Mechanism**: replaces ICMS, ISS, IPI, PIS, COFINS with a dual VAT
(CBS federal + IBS state/municipal) plus an excise (IS). The transition
period sees the old and new systems coexisting at different proportions.

**Identifies**: effects of tax-system changes on:
- Sectoral price levels
- Inter-state trade
- Firm location decisions
- Municipal fiscal position (especially services-heavy municipalities
  losing ISS base)
- Compliance costs

**Caveat**: as of 2026, the reform is **just beginning** — empirical
analysis will need data from 2026 onward.

**See**: [`topics/federalismo-fiscal.md`](topics/federalismo-fiscal.md) §1
("Reforma tributária").

---

## 18. CNJ Resolução 547/2024 — execução fiscal mass extinction

**Institutional source**: CNJ Res. 547/2024.

**Mechanism**: authorized judges to extinguish low-value execuções
fiscais (≤R$10,000) on economic-unviability grounds. Resulted in
>10 million case extinctions in <2 years; the stock fell from 26.9M
(Dec 2023) to ~16.5M (Dec 2025), a ~37% reduction.

**Identifies**: effects of administrative case-clearing on:
- Court congestion measures
- Judge workload
- Other case durations (does clearing congestion help non-tax cases
  move faster?)

**Caveat**: the extinction is **not** randomly assigned across cases —
it targets low-value cases below a sharp threshold. RD on the value
threshold could work for cases just above/below R$10,000.

**See**: [`topics/cnj-administracao-judicial.md`](topics/cnj-administracao-judicial.md)
§7.

---

## 19. FUNDEB complementação — federal top-up threshold

- **Source**: FUNDEB (EC 108/2020, Lei 14.113/2020). Federal government
  tops up state-level FUNDEB funds when per-student spending falls
  below a national minimum.
- **Mechanism**: states whose FUNDEB per-student value falls below the
  national complementação threshold receive federal top-up. Creates a
  kink/notch at the threshold.
- **Identifies**: effect of incremental education funding on student
  outcomes, teacher salaries, school infrastructure.
- **Caveats**: threshold moves annually; state-level sorting around the
  cutoff is possible via enrollment manipulation.
- **Canonical papers**: Gordon & Vegas (2005); Kosec (2014 *JDE*).
- **See**: [`topics/federalismo-fiscal.md`](topics/federalismo-fiscal.md) §2.

---

## 20. Judicial random case assignment — judge fixed effects

- **Source**: CNJ case-assignment rules. Cases distributed by electronic
  *sorteio* within groups of varas of the same competence.
- **Mechanism**: quasi-random assignment of cases to judges within the
  same vara-group. Prevenção creates persistence within a case but
  does not affect initial assignment.
- **Identifies**: effect of judge identity/characteristics on case
  outcomes (duration, settlement rates, sentencing).
- **Caveats**: specialization structures (cível vs. criminal, fazenda
  pública) create non-random sorting by subject matter. Must document
  the specialization structure when claiming random assignment.
  Titular/substituto splits (by case-number parity) add a second
  layer of quasi-randomness within a single vara.
- **Canonical papers**: Abrams et al. (2012); for Brazil: various TJSP
  studies exploiting vara-level random assignment.
- **See**: [`topics/cnj-administracao-judicial.md`](topics/cnj-administracao-judicial.md) §5,
  [`topics/justica-federal.md`](topics/justica-federal.md) §1,
  [`topics/justica-trabalho.md`](topics/justica-trabalho.md) §2.

---

## 21. Quinto constitucional — OAB/MP vs career judges

- **Source**: `CF.94`. 1/5 of seats in TJs, TRFs, and TRTs reserved
  for lawyers (OAB) and MP members.
- **Mechanism**: within the same tribunal, some judges entered via
  concurso (career track) and others via quinto (OAB/MP track).
  Different professional formation, age at appointment, and career
  incentives.
- **Identifies**: effect of judge background (career vs. external
  appointment) on judicial behavior, voting patterns, case outcomes.
- **Caveats**: quinto judges are selected (not random); need to account
  for selection on observables. Chambers/turmas may not be randomly
  composed.
- **See**: [`topics/carreira-juizes.md`](topics/carreira-juizes.md) §2,
  [`topics/juizes.md`](topics/juizes.md) §3.

---

## 22. Municipal emancipation wave (1988–2000)

- **Source**: CF/88 Art. 18 §4 (original) gave states authority to
  create new municipalities by state law. ~1,438 new municípios
  created between 1988 and 2000 before EC 15/1996 tightened the rules.
- **Mechanism**: creation of new municipalities in response to state-
  level legislative incentives (typically FPM capture — smaller
  municipalities get higher per-capita FPM due to the step function).
- **Identifies**: effects of government fragmentation on public goods,
  fiscal outcomes, political competition.
- **Caveats**: municipality creation is endogenous to local political
  interests; need instruments or boundary-based designs.
- **Canonical papers**: Litschig (2012 *JDE*); Arvate et al.
- **See**: [`topics/federalismo-fiscal.md`](topics/federalismo-fiscal.md) §2.

---

## How to add an entry

When you find or use a new natural experiment in Brazilian institutions,
add an entry to this file with:

1. **Institutional source**: the statute, regulation, or decision that
   creates the variation.
2. **Mechanism**: the precise rule that generates the assignment /
   threshold / event.
3. **Identifies**: what causal effect you can recover with this variation.
4. **Caveats**: known threats to identification (selection, anticipation,
   spillover, etc.).
5. **Canonical paper(s)**: the seminal use(s) of the variation in the
   literature.
6. **Cross-reference**: link to the topical file(s) where the
   institutional details are explained.
