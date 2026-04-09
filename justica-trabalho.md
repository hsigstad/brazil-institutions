# Justiça do Trabalho

Specialized federal judiciary branch for employment disputes. Three tiers:
Varas do Trabalho (first instance) → TRTs (24 regional appellate courts) →
TST (national superior court). TRT2 covers the São Paulo metropolitan area.

**Topics / keywords**: labor court, employment disputes, CLT, TRT, TST,
vara do trabalho, 2017 labor reform, Lei 13.467, filing costs, justiça
gratuita, honorários de sucumbência, conciliation, settlement, judicial
homologation, direitos indisponíveis, overtime, horas extras, impedimento,
case assignment, ADI 5766.

**Snapshot as of 2026**: 2017 reform provisions reflect STF ADI 5766
(October 2021). Filing-volume figures are from CNJ *Justiça em Números*
and TST reports through ~2024. Monetary thresholds (RGPS ceiling, minimum
wage) update annually.

Labor courts handle over 1 million new filings per year and have the
highest conciliation rate in the Brazilian judiciary. They also offer a
relatively rare empirical feature: **nearly all settlements are
judicially mediated and observable in the data**.

For the 2017 reform as a quasi-experiment (Lei 13.467/17 + STF ADI
5766), see [`quasi-experimentos.md`](quasi-experimentos.md) §§5–6. For
the date timeline of related events, see [`timeline.md`](timeline.md).
For common confusions (pre-2017 vs post-2017 cost regimes), see
[`pitfalls.md`](pitfalls.md) "Labor courts".

Compiled from personal research notes on Brazilian labor courts, with
citations to published CNJ and TST reports where relevant.

---

## Constitutional and statutory basis

- **TST**: [LOMAN Art. 12](lei/loman.org::*Art.%2012).
- **TRTs**: [LOMAN Art. 13](lei/loman.org::*Art.%2013).
- Substantive law: **CLT** (Consolidação das Leis do Trabalho, DL 5.452/1943).
- Procedure governed by CLT (Arts. 763 onward) supplemented by CPC.

---

## Case assignment and judge composition

- Each court unit (**vara**) has one chief judge (*juiz titular*) and
  typically one substitute (*juiz substituto*).
- Cases are randomly distributed to varas within a foro trabalhista.
- **Exception** (*dependência / prevenção*): cases connected to a prior
  case (same litigants, same issue) are assigned to the same vara.
- Quasi-random assignment enables judge fixed-effect estimation.

---

## Recusal — impedimento

- Judge must recuse if a lawyer for any party is a relative up to the
  third degree (includes in-laws, excludes cousins).
- If recused: case goes to the substitute judge in the same vara, or to
  the next vara if no substitute.
- **Legal basis**: CPC 2016 Arts. 144 and 146; CNJ Resolution of March 2,
  2015.
- **Pre-2015**: impedimento only when the lawyer was actively acting in
  the case (not merely a member of the firm).
- **2015 CNJ Resolution**: extended to cases where the relative is sócio,
  associado, colaborador, or empregado of the law firm, or maintains any
  professional link.
- **NCPC Art. 144 III §3 (2016)**: formalized the extension to members of
  the same law firm "even if they do not directly intervene in the case".
- Impedimento is *matéria de ordem pública*: judge can recognize ex
  officio. Suspeição (bias) is not — must be raised by a party.

### Compliance notes

- Compliance with formal impedimento rules is high when the lawyer is a
  direct relative of the judge.
- Compliance is substantially weaker for looser connections (e.g.,
  relatives of colleagues in the same law firm), even after the 2015
  CPC reform explicitly extended the rule to members of the firm.
- Cousins (not covered by the rule) generate no observable change in
  case assignment.

---

## Filing costs

### Pre-2017 regime

- **Zero filing costs** for workers. No fees to file or appeal. Workers
  bore no financial risk from filing.
- **No honorários de sucumbência** (loser-pays attorney fees) — each
  party bore its own attorney costs regardless of outcome.
- Workers earning up to 2× minimum wage automatically entitled to
  *justiça gratuita*; above that, a simple *declaração de hipossuficiência*
  sufficed. In practice, nearly all workers obtained free access.

### Post-2017 regime (Lei 13.467/17, effective 11 Nov 2017)

Workers now face financial risk from filing (Arts. 789, 790, 790-B, 791-A,
844 §2, CLT):

- **Custas processuais**: 2% of claim value, min R$10.64, max 4× RGPS
  ceiling. At the 2018 RGPS ceiling (R$5,645.80), max ≈ R$22,583. Ceiling
  is updated annually — verify current value before using the R$22k figure
  for post-2018 work. Charged to the losing party.
- **Honorários de sucumbência**: 5%–15% of judgment value (or economic
  benefit, or updated claim value if neither is measurable). Assessed
  against the losing party **on each claim** — a plaintiff who wins some
  but loses others pays honorários on the lost claims.
- **Honorários periciais**: the losing party on the technical issue pays
  the expert (Art. 790-B) — relevant for *insalubridade* and other
  expert-dependent claims.
- **No-show penalty** (Art. 844 §2): if plaintiff fails to attend the
  hearing, the case is archived and the plaintiff must pay court costs
  to refile, even if a *justiça gratuita* beneficiary.
- **Justiça gratuita threshold tightened** (Art. 790 §3): automatic only
  for those earning up to 40% of RGPS ceiling (≈ R$2,258 in 2018, ~2.4×
  minimum wage at that time — both the ceiling and the minimum wage are
  updated annually). Above that: must affirmatively prove economic
  insufficiency (Art. 790 §4).

### STF — ADI 5766 (October 2021)

Declared unconstitutional two key provisions restricting access to justice
for *justiça gratuita* beneficiaries:

- **Art. 790-B caput and §4**: provision requiring beneficiaries to pay
  expert fees from credits obtained in the case — struck down.
- **Art. 791-A §4**: provision allowing deduction of honorários de
  sucumbência from credits in other proceedings — struck down. Obligation
  now suspended for 2 years from *trânsito em julgado*; extinguished if
  the economic situation does not change.

**Implication**: November 2017 – October 2021 is the period of maximum
filing cost deterrence. The 40% RGPS threshold for automatic eligibility
remains in force; non-beneficiaries still face the full cost regime.

### Impact on filing volumes

| Year | New cases (1st instance) | Change |
|---|---|---|
| 2015 | ~2.6M | — |
| 2016 | ~2.7M (peak) | +4% |
| 2017 | ~2.6M (Nov spike ~207k in one month) | −3% |
| 2018 | ~1.7M | **−34%** |
| 2019 | ~1.5M | −12% |

- **November 2017 spike**: monthly filings nearly doubled as workers
  rushed to file under the old rules (~207k vs. typical ~100k–120k).
- **Immediate collapse**: Jan–Sep 2018 vs. same period 2017: 1.29M vs.
  2.01M (−36%).
- **Sustained reduction** through 2019; gradual recovery from 2020,
  approaching pre-reform levels by 2023–2024 (as of 2026 data).
- **Composition change**: speculative/low-probability claims
  (*pedidos aventureiros*) appear to have dropped disproportionately.

**Sources:** TST *Relatório Geral da Justiça do Trabalho*;
TST, "Primeiro ano da reforma trabalhista: efeitos" (2018);
CNJ *Justiça em Números*.

---

## Hearing procedure

The CLT prescribes an *audiência una* (single unified hearing) in which
conciliation attempt, defense, evidence, and judgment occur in one session
(Arts. 849–850 CLT). In practice, most courts fractionate into 2–3 sessions.

1. **Audiência inaugural / de conciliação**: mandatory conciliation
   proposal (Art. 846). If both parties agree, settlement is homologated
   and the case ends. Otherwise, the defendant presents *contestação*
   orally (20 min) or in writing. Judge may take *depoimento pessoal* and
   schedule the next hearing.
2. **Audiência de instrução e julgamento**: evidence (witness testimony,
   documentary, expert reports); *razões finais* (10 min each, Art. 850);
   renewed conciliation proposal (Art. 850); judgment immediately or
   within a reserved period.
3. **Rito sumaríssimo** (claims up to 40 minimum wages, Art. 852-C):
   hearing within 15 days of filing; designed for a single session.

- If interrupted, continuation must be scheduled within 30 days (Art. 849).
- After the hearing, judgment must be rendered within 15 days.

---

## Conciliation

Labor courts have the highest conciliation rate in the Brazilian judiciary.

- Overall rate across the *Justiça do Trabalho*: ~24% of cases resolved
  (CNJ *Justiça em Números* 2019).
- At first instance (*Varas do Trabalho*): **42.9% of cases resolved by
  agreement in 2019** — >853,000 settlements totaling >R$14.4 billion
  paid to workers (TST *Relatório da Conciliação* 2019).
- CNJ target for 2025: ≥38% conciliation in the *fase de conhecimento*.
- TST's *Cejusc/TST* (created 2023): >68% conciliation in referred cases.

---

## Settlement observability — a data advantage

**Nearly all labor court settlements are judicially mediated and observable
in the data**, unlike most US/European settings where settlements are
private and unobserved.

Institutional reasons:

1. **Pre-2017**: out-of-court settlements were **unenforceable** against
   indisposable rights — a worker who signed a private release could
   still file a lawsuit. Employers therefore had no incentive to settle
   out of court, pushing virtually all settlement activity into the
   mandatory conciliation hearing (recorded in the case file).
2. **Post-2017 (Arts. 855-B – 855-E CLT, added by Lei 13.467/17)**:
   formal procedure for judicial homologation of extrajudicial agreements.
   Both parties must be represented by **separate** attorneys. The agreement
   is submitted to a labor judge. Once homologated, it gains *título
   executivo judicial* force. Even these "extrajudicial" settlements flow
   through the court system and appear in records.
3. **Direitos indisponíveis doctrine**: many worker protections cannot be
   waived even voluntarily; judges verify this during homologation. Further
   channels settlement through the courts.

**Contrast with civil courts**: under CPC Art. 784, private agreements
signed by parties + 2 witnesses are directly enforceable as *título
executivo extrajudicial*; judicial homologation is optional. Civil
settlements are therefore largely unobservable, creating the standard
selection problem. The observability advantage is **specific to labor
courts**.

---

## Direitos indisponíveis

Brazilian labor law distinguishes *direitos disponíveis* (waivable) from
*direitos indisponíveis* (non-waivable, considered protections of *ordem
pública*). Grounded in CF Art. 7.

The 2017 reform clarified the boundary through two CLT articles:

- **Art. 611-A — negotiable via collective bargaining**: work schedules,
  banco de horas, intervalo interjornada, telework, time-tracking methods,
  and others.
- **Art. 611-B — non-negotiable (direitos indisponíveis)**, cannot be
  reduced even by collective agreement:
  - Salário mínimo and irredutibilidade salarial
  - FGTS deposits and the 40% multa rescisória
  - 13º salário
  - Adicional de horas extras (min 50% above regular rate, CF Art. 7 XVI)
  - Adicional noturno
  - Adicional de insalubridade/periculosidade
  - Repouso semanal remunerado
  - Férias anuais + 1/3 de férias
  - Maternity/paternity leave
  - Aviso prévio proporcional
  - Normas de saúde, higiene e segurança

### Interaction with settlement

- **In-court settlement**: judges accept discounts on disputed amounts
  (e.g., 60% of claimed overtime) because existence/quantum are genuinely
  disputed, but will not approve waivers of rights proven to exist.
- **Extrajudicial settlement (Art. 855-B)**: same principle; judge may
  reject if it appears to waive indisposable rights.
- **Private release pre-2017**: essentially no legal force regarding
  indisposable rights.

### Quitação anual (Art. 507-B, added by Lei 13.467/17)

- Employer and employee appear before the employee's union and sign a
  statement itemizing all labor obligations fulfilled for the year.
- Must be **item-by-item**; generic "quitação geral" is invalid.
- Has *eficácia liberatória* for listed items.
- Limitations: (a) constitutional access to justice preserved — worker can
  still file, but *termo* is a defense; (b) union participation required;
  (c) TST jurisprudence not yet consolidated.
- **Practical uptake limited**: unions reluctant to participate; employers
  uncertain about legal strength.

---

## Overtime disputes (horas extras) — evidentiary rules

Overtime disputes are consistently the most frequent category of labor
cases; exact share varies by sample and period.

Key legal standards:

- **CLT Art. 74 §2**: employers with >20 employees must record working
  hours.
- **TST Súmula 338**: if timecards are not presented, burden shifts to
  the employee — plaintiff's allegations presumed true.
- **CLT Art. 71**: meal and rest breaks.
- **NR-17**: ergonomic breaks for specific occupations.
- **CLT Art. 818** (amended by Lei 13.467/17): burden of proof rules.
- **Portaria 1.510/2009**: timecards with variable entry/exit times and no
  other irregularity are presumed valid; absence of signature does not
  invalidate.

### Other evidentiary rules relevant to empirical work

- Employer absence from hearing: claimant's allegations typically taken
  as true (**deemed confession**).
- Witness credibility: contradictions between claimant and witness
  undermine credibility.

---

## Union representation

- Workers may be represented by union attorneys (*sindicato*) at no cost.
- Common in labor courts; affects both filing rates and litigation strategy.
- Unions are institutional repeat players on the plaintiff side.

---

## Contingency fees and lawyer incentives

- Plaintiff lawyers: typically **20–30% contingency fee** (share of value
  awarded).
- Defendant lawyers: typically on **fixed-wage** contracts independent of
  case outcome.
- This asymmetry shapes incentives differently on the two sides of a
  case.

---

## Typical timeline (first instance)

Based on aggregated CNJ and TRT data:

- **Filing → first hearing**: ~135 days (~4.5 months).
- **First hearing → continuation hearing**: ~300–450 days (high variance).
- **Continuation → sentença**: ~60 days.
- **Fase de conhecimento (total)**: ~1–2 years average.
- **Fase de execução**: ~4 years 11 months (CNJ 2015 data).
- **Overall average duration**: ~2 years 4 months (CNJ) with enormous
  variance by court, complexity, and early settlement.

---

## Peritos (court experts)

Notes on judicial expert appointment in labor courts:
<https://sentenca.com.br/pdf/palavra-perito/A_NOMEA%C3%87%C3%83O_DO_PERITO.pdf>
