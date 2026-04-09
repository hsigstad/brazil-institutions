# Jurisprudência STF — consolidated case file

Single source of truth for Supremo Tribunal Federal decisions cited
elsewhere in this directory. Where the same case appears in multiple
topical files, the substantive description lives here; the topical
files cite by name and link back.

**Topics / keywords**: STF, Supremo Tribunal Federal, jurisprudência,
Tema, repercussão geral, ADI, ADC, ADPF, RE, ARE, HC, súmula vinculante,
controle de constitucionalidade.

**Snapshot as of 2026**: STF jurisprudence is in continuous evolution.
Each entry below names the most recent decision known at the time of
writing. For high-stakes citation, verify the case has not been
modulated, overruled, or superseded by checking
[portal.stf.jus.br](https://portal.stf.jus.br/).

**Naming conventions** in this file:
- **Tema NNN** — repercussão geral (RE/ARE) thesis number assigned by
  STF after recognizing repercussão geral.
- **ADI / ADC / ADPF** — abstract control of constitutionality.
- **RE / ARE** — concrete control via recurso extraordinário / agravo
  em recurso extraordinário.
- **HC** — habeas corpus.

---

## 1. Improbidade administrativa

### Tema 897 — RE 852.475 — Imprescritibilidade do ressarcimento

- **Holding**: Ressarcimento ao erário arising from intentional
  (dolosa) improbidade administrativa is **imprescritível** — there
  is no statute of limitations on the reparation-of-damages claim. The
  declaratory and sanction components remain subject to ordinary
  prescription; only the reparation component is perpetual.
- **Significance**: A practical workaround for prescription defenses
  in old corruption cases — the state can always pursue restitution
  even when sanctions are time-barred.
- **Cited in**: [`topics/improbidade.md`](topics/improbidade.md) §1.

### Tema 1199 — ARE 843.989 — Retroatividade da Lei 14.230/2021

- **Decided**: 18 August 2022.
- **Rel.**: Min. Alexandre de Moraes.
- **Holdings**:
  1. The elimination of culposa improbidade by Lei 14.230/2021 is
     **irretroactive** for cases with final judgment (*trânsito em
     julgado*) — culposa convictions and ongoing enforcement are not
     undone.
  2. For **pending cases without final judgment**, the new dolo-only
     standard applies immediately: courts must re-examine intent and
     dismiss if only negligence is proven.
  3. The new 8-year absolute prescription regime is also irretroactive:
     for conduct predating the reform, the 8-year clock starts from
     the law's publication date (26 October 2021), not from the
     original act.
  4. The "lei mais benéfica" doctrine does not generally apply to
     improbidade because it is a civil regime, but the elimination of
     culposa is recognized as a substantive change with the limited
     retroactivity above.
- **Cited in**: [`topics/improbidade.md`](topics/improbidade.md) §2,
  [`topics/licitacoes.md`](topics/licitacoes.md) §"Related statutes".
- **Source**: <https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=1199>.

### Pet 3.240 AgR — Inexistência de foro por prerrogativa em improbidade

- **Decided**: 10 May 2018, Plenário (DJe 22 August 2018).
- **Rel.**: Min. Roberto Barroso (after redistribution from Min. Teori
  Zavascki).
- **Votação**: 10–1.
- **Holding**: Improbidade administrativa actions are *civil*, not
  criminal. The foro por prerrogativa de função established in CF
  Arts. 102 and 105 covers only "infrações penais comuns" and does
  not extend to civil improbidade actions. Even authorities with
  criminal foro privilegiado (ministros de Estado, governadores,
  parlamentares, including in principle the President) respond to
  improbidade actions in **first instance**, alongside ordinary
  defendants.
- **Doctrinal posture**: reaffirms **ADI 2797** (Plenário, decided
  15 September 2005, Rel. Sepúlveda Pertence), which had already
  declared unconstitutional the legislative attempt in Lei 10.628/2002
  to add § 2º to CPP Art. 84 and create a foro privilegiado for
  improbidade. Pet 3240 closes the door on revival of that argument.
  (ADI 2797 not yet in `jurisprudencia_index.yaml`; should be added.)
- **Why it matters for empirical work**: this is the case that lets
  researchers study improbidade caseloads at the first-instance level
  uniformly, without segregating defendants by political rank.
  Mayors, governors, and ministros all appear in TJ/TRF first-
  instance dockets; there's no parallel "STF improbidade" track to
  worry about.
- **Cited in**: [`topics/improbidade.md`](topics/improbidade.md) §3,
  [`topics/procedimentos-legais.md`](topics/procedimentos-legais.md) §"Foro privilegiado".
- **Source**: <https://portal.stf.jus.br/processos/detalhe.asp?incidente=2230342>.

---

## 2. Contas municipais e Ficha Limpa

### Tema 157 — RE 848.826 — Apreciação das contas de prefeito

- **Decided**: 10 August 2016. **Tese certified**: 18 October 2019.
- **Vote**: 6–5 (narrow majority).
- **Majority**: Lewandowski, Gilmar Mendes, Fachin, Cármen Lúcia,
  Marco Aurélio, Celso de Mello.
- **Dissent**: Barroso, Zavascki, Rosa Weber, Fux, Toffoli (would
  have allowed TCEs to independently judge contas de gestão).
- **Tese**: *"Para os fins do artigo 1º, inciso I, alínea g, da Lei
  Complementar 64/1990, a apreciação das contas de Prefeito, tanto as
  de governo quanto as de gestão, será exercida pelas Câmaras
  Municipais, com auxílio dos Tribunais de Contas competentes, cujo
  parecer prévio somente deixará de prevalecer por decisão de dois
  terços dos vereadores."*
- **Holding**: Both contas de governo and contas de gestão fall under
  câmara municipal jurisdiction for purposes of Ficha Limpa
  ineligibility (LC 64/1990 Art. 1 I "g"). A TCE parecer alone does
  not trigger ineligibility — the câmara must vote to reject. Omission
  by the câmara also does not generate ineligibility ("inadmissível o
  julgamento ficto das contas por decurso de prazo").
- **Cited in**: [`topics/contas-municipais.md`](topics/contas-municipais.md) §2,
  [`topics/partidos-e-sistema-eleitoral.md`](topics/partidos-e-sistema-eleitoral.md) §7.
- **Source**: <https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=157>.

### ADPF 982 — TCE / câmara boundary revisited

- **Decided**: ~2025.
- **Holdings**:
  1. Reaffirms that TCEs can independently judge contas de gestão and
     impose administrative sanctions (débitos, multas) on mayors
     acting as ordenadores de despesas.
  2. Clarifies that **electoral ineligibility** under Ficha Limpa
     arises only from câmara rejection of contas de governo, not from
     TCE decisions on contas de gestão.
  3. Complements rather than contradicts Tema 157.
- **Cited in**: [`topics/contas-municipais.md`](topics/contas-municipais.md) §2.
- **Source**: [Migalhas analysis](https://www.migalhas.com.br/depeso/433107/adpf-982-quem-julga-as-contas-do-prefeito-afinal).

### ADC 29/30 + ADI 4578 (2012) — Constitucionalidade da Ficha Limpa

- **Decided**: 16 February 2012.
- **Holding**: Upheld the constitutionality of LC 135/2010 (Lei da
  Ficha Limpa), including the provision that ineligibility attaches
  upon a **collegiate body** decision (not requiring trânsito em
  julgado). Rejected the *presunção de inocência* objection on the
  ground that ineligibility is a non-criminal restriction on
  candidacy, not a punishment.
- **Cited in**: [`topics/partidos-e-sistema-eleitoral.md`](topics/partidos-e-sistema-eleitoral.md) §7.

---

## 3. Justiça do Trabalho — reforma trabalhista

### ADI 5766 (October 2021) — Justiça gratuita pós-reforma trabalhista

- **Decided**: 20 October 2021.
- **Holdings**:
  1. **Art. 790-B caput and §4 CLT** (expert fees from credits
     obtained in the case) — **declared unconstitutional**. Justiça
     gratuita beneficiaries cannot be forced to pay perícia fees out
     of credits won in the action.
  2. **Art. 791-A §4 CLT** (deduction of honorários sucumbenciais
     from credits obtained in *other* proceedings) — **declared
     unconstitutional**. Obligation to pay is suspended for 2 years
     from trânsito em julgado; extinguished if economic situation does
     not change.
- **Significance**: Partially restored pre-reform regime for justiça
  gratuita beneficiaries. The 40% RGPS income threshold for automatic
  eligibility remains in force; non-beneficiaries still face the full
  cost regime.
- **Cited in**: [`topics/justica-trabalho.md`](topics/justica-trabalho.md)
  §"Filing costs".

---

## 4. Sistema eleitoral — financiamento de campanha

### ADI 4650 (September 2015) — Doações empresariais

- **Decided**: September 2015.
- **Rel.**: Min. Luiz Fux.
- **Holding**: Declared unconstitutional the provisions of Lei
  9.504/1997 and Lei 9.096/1995 that permitted corporate donations to
  campaigns and political parties. Rationale: corporate donations
  distort political equality and create systematic dependencies
  between donors and elected officials.
- **Effective from**: 2016 elections onward.
- **Significance**: Triggered creation of the FEFC (Lei 13.487/2017)
  as the public-funding replacement for corporate money. The
  pre-2016 vs. post-2016 campaign finance regimes are fundamentally
  different and any empirical work crossing the boundary must
  account for it.
- **Cited in**: [`topics/partidos-e-sistema-eleitoral.md`](topics/partidos-e-sistema-eleitoral.md) §6.
- **Source**: <https://portal.stf.jus.br/processos/detalhe.asp?incidente=4136819>.

---

## 5. Federalismo fiscal

### ADI 875 et al. (2010) — FPE coefficients

- **Decided**: 2010.
- **Holding**: Declared the rigid FPE distribution coefficients of
  LC 62/1989 unconstitutional for perpetuating fixed shares without
  meaningful update. Gave Congress a deadline to legislate a new
  formula.
- **Aftermath**: Congress responded with **LC 143/2013**, which
  introduced a population + per-capita-income formula transitioning
  toward more equalizing distribution.
- **Cited in**: [`topics/federalismo-fiscal.md`](topics/federalismo-fiscal.md) §2.

---

## 6. Anticorrupção penal — Lava Jato e Pacote Anticrime

### HC 126.292 (2016) — Execução provisória da pena

- **Decided**: 2016.
- **Holding**: Permitted execution of prison sentence after
  **second-instance** confirmation, before trânsito em julgado.
- **Significance**: Enabled the imprisonment of high-profile Lava
  Jato defendants while their extraordinary appeals remained pending.

### ADC 43/44/54 (November 2019) — Reversão de HC 126.292

- **Decided**: November 2019.
- **Holding**: Reversed HC 126.292; restored the requirement of
  **trânsito em julgado** before prison execution.
- **Significance**: Triggered release of high-profile defendants
  including former President Lula. Re-affirmed the *presunção de
  inocência* in its full procedural form.

### Lula vs. Moro cases (2021)

- **Decided**: 2021.
- **Holdings**:
  1. **Incompetência**: the 13ª Vara Federal Criminal de Curitiba was
     not the competent venue for non-Petrobras Lula cases.
  2. **Parcialidade**: former judge Sergio Moro (then Minister of
     Justice under Bolsonaro) was found to have lacked impartiality in
     the underlying convictions, vitiating the proceedings.
- **Significance**: Annulled multiple Lula convictions on procedural
  grounds; major institutional moment in the post-Lava Jato phase.
- **Cited in**: [`topics/anticorrupcao-penal.md`](topics/anticorrupcao-penal.md) §9.

### ADIs 6.298–6.305 (August 2023) — Juiz das garantias

- **Decided**: August 2023.
- **Holding**: The juiz das garantias institute introduced by Lei
  13.964/2019 (Pacote Anticrime, CPP Art. 3-A) is constitutional, with
  implementation guidelines set by the STF. Effective implementation
  from 2024.
- **Significance**: Mandates separation of investigatory and trial
  judges in criminal proceedings — a structural change to Brazilian
  criminal procedure.
- **Cited in**: [`topics/anticorrupcao-penal.md`](topics/anticorrupcao-penal.md) §6.

### HC 127.483 (Ulisses Ramos) and HC 164.493 (Bendine)

- **Holdings**: Defined the scope of judicial review over colaboração
  premiada agreements (Lei 12.850/2013 Art. 4) and the evidentiary
  standards for collaborator testimony. A colaboração alone cannot
  sustain a conviction (Art. 4 §16); corroboration is required.
- **Cited in**: [`topics/anticorrupcao-penal.md`](topics/anticorrupcao-penal.md) §3.

---

## 7. NTEP / acidentes de trabalho

### ADI 3.931 (April 2020) — Constitucionalidade do NTEP

- **Decided**: April 2020.
- **Holding**: Upheld the constitutionality of Art. 21-A of Lei
  8.213/1991 (added by Lei 11.430/2006), which established the **Nexo
  Técnico Epidemiológico Previdenciário** (NTEP). The presumption of
  occupational origin based on statistical CNAE × CID matching is
  constitutional and reversal of burden of proof is permitted in this
  context.
- **Significance**: Ratified the NTEP framework that shifts the burden
  of proof to the employer in workplace-injury social-security claims
  when the CNAE × CID pair is on the statistical risk list.

---

## 8. Transparência

### ARE 652.777 (2015, repercussão geral) — Salários de servidores públicos

- **Decided**: 23 April 2015 (repercussão geral).
- **Holding**: The disclosure of nominal salaries of individual
  public servants is constitutional and consistent with both the
  publicity principle (CF Art. 37) and the right to privacy. Servants
  do not have a privacy interest in concealing their compensation
  paid from public funds.
- **Significance**: Foundational ruling for the federal Portal da
  Transparência practice of publishing servant salaries by name. The
  LGPD (2018) does not override this — public salary disclosure
  remains lawful under the public-interest legal basis.
- **Cited in**: [`topics/transparencia-dados.md`](topics/transparencia-dados.md) §1.

---

## 9. Quick reference table

| Case | Theme | File |
|---|---|---|
| Tema 897 (RE 852.475) | Imprescritibilidade do ressarcimento | improbidade |
| Tema 1199 (ARE 843.989) | Retroatividade Lei 14.230/2021 | improbidade |
| Tema 157 (RE 848.826) | Câmara julga contas prefeito | contas-municipais |
| ADPF 982 | TCE × câmara × Ficha Limpa | contas-municipais |
| ADC 29/30 + ADI 4578 | Ficha Limpa constitucional | partidos-e-sistema-eleitoral |
| ADI 5766 | Justiça gratuita pós-reforma | justica-trabalho |
| ADI 4650 | Fim doações empresariais | partidos-e-sistema-eleitoral |
| ADI 875 et al. | FPE coefficients inconstitucionais | federalismo-fiscal |
| HC 126.292 | Execução provisória da pena | anticorrupcao-penal |
| ADC 43/44/54 | Reversão de HC 126.292 | anticorrupcao-penal |
| Lula vs. Moro | Incompetência + parcialidade | anticorrupcao-penal |
| ADIs 6.298–6.305 | Juiz das garantias | anticorrupcao-penal |
| HC 127.483 / HC 164.493 | Colaboração premiada | anticorrupcao-penal |
| ADI 3.931 | NTEP constitucional | (referenciado externamente) |
| ARE 652.777 | Salários de servidores públicos | transparencia-dados |

---

## Cross-references

- [`topics/improbidade.md`](topics/improbidade.md), [`topics/contas-municipais.md`](topics/contas-municipais.md),
  [`topics/partidos-e-sistema-eleitoral.md`](topics/partidos-e-sistema-eleitoral.md),
  [`topics/anticorrupcao-penal.md`](topics/anticorrupcao-penal.md),
  [`topics/justica-trabalho.md`](topics/justica-trabalho.md),
  [`topics/transparencia-dados.md`](topics/transparencia-dados.md),
  [`topics/federalismo-fiscal.md`](topics/federalismo-fiscal.md) — files where these
  cases are discussed in their substantive context.
- [`leis_index.yaml`](leis_index.yaml) — index of statutes whose
  interpretation these decisions shape.
