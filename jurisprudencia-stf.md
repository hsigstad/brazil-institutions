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

### `Tema1199` — ARE 843.989 — Retroatividade de `L14230`

- **Decided**: 18 August 2022.
- **Rel.**: Min. Alexandre de Moraes.
- **Holdings**:
  1. The elimination of culposa improbidade by `L14230` is
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

### `ADI2797` — Inconstitucionalidade de foro privilegiado para improbidade

- **Decided**: 15 September 2005, Plenário.
- **Rel.**: Min. Sepúlveda Pertence.
- **Votação**: maioria (julgada em conjunto com ADI 2860).
- **Holding**: Declared unconstitutional § 2º of `CPP.84`, introduced
  by `L10628`, which had extended foro por prerrogativa de função to
  ações de improbidade administrativa. The CF reserves foro especial
  to "infrações penais comuns"; improbidade has civil nature and must
  be adjudicated in first instance regardless of the defendant's
  office.
- **Why it matters for empirical work**: establishes that all
  improbidade defendants — mayors through ministers — appear in
  first-instance dockets. No parallel STF improbidade track to
  account for. Reaffirmed by `Pet3240` (2018, 10–1).
- **Cited in**: [`topics/improbidade.md`](topics/improbidade.md) §3,
  [`topics/procedimentos-legais.md`](topics/procedimentos-legais.md) §"Foro privilegiado".
- **Source**: <https://portal.stf.jus.br/processos/detalhe.asp?incidente=2093529>.

### `Pet3240` AgR — Inexistência de foro por prerrogativa em improbidade

- **Decided**: 10 May 2018, Plenário (DJe 22 August 2018).
- **Rel.**: Min. Roberto Barroso (after redistribution from Min. Teori
  Zavascki).
- **Votação**: 10–1.
- **Holding**: Improbidade administrativa actions are *civil*, not
  criminal. The foro por prerrogativa de função established in
  `CF.102` and `CF.105` covers only "infrações penais comuns" and
  does not extend to civil improbidade actions. Even authorities with
  criminal foro privilegiado (ministros de Estado, governadores,
  parlamentares, including in principle the President) respond to
  improbidade actions in **first instance**, alongside ordinary
  defendants.
- **Doctrinal posture**: reaffirms `ADI2797` (2005), which had already
  declared unconstitutional the legislative attempt in `L10628` to add
  § 2º to `CPP.84` and create a foro privilegiado for improbidade.
  `Pet3240` closes the door on revival of that argument.
- **Why it matters for empirical work**: this is the case that lets
  researchers study improbidade caseloads at the first-instance level
  uniformly, without segregating defendants by political rank.
  Mayors, governors, and ministros all appear in TJ/TRF first-
  instance dockets; there's no parallel "STF improbidade" track to
  worry about.
- **Cited in**: [`topics/improbidade.md`](topics/improbidade.md) §3,
  [`topics/procedimentos-legais.md`](topics/procedimentos-legais.md) §"Foro privilegiado".
- **Source**: <https://portal.stf.jus.br/processos/detalhe.asp?incidente=2230342>.

### `AP937` QO — Restrição do foro privilegiado criminal

- **Decided**: 3 May 2018, Plenário.
- **Rel.**: Min. Roberto Barroso.
- **Holding**: Criminal foro por prerrogativa de função applies only to
  crimes committed *during the exercise of the mandate* AND *related to
  the functions of the office held*. Crimes outside this scope —
  whether committed before the mandate or unconnected to office — are
  tried at first instance even if the defendant currently holds a
  foro-bearing position.
- **Companion to `Pet3240`**: decided one week before `Pet3240`
  (2018-05-10). `AP937` restricts the *criminal* foro; `Pet3240`
  confirms the *civil* (improbidade) foro never existed. Together they
  define the current scope of foro privilegiado.
- **Movement of cases**: when a defendant takes office, qualifying
  criminal cases move *up* to the higher court; when they leave, cases
  move back *down*. STF flagged that downward movement near
  prescription may constitute abuse.
- **Cited in**: [`topics/procedimentos-legais.md`](topics/procedimentos-legais.md) §"Foro privilegiado".
- **Source**: <https://portal.stf.jus.br/processos/detalhe.asp?incidente=4776682>.

---

## 2. Contas municipais e Ficha Limpa

### `Tema157` — RE 848.826 — Apreciação das contas de prefeito

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
  ineligibility (`LI.1.I.g`). A TCE parecer alone does not trigger
  ineligibility — the câmara must vote to reject. Omission
  by the câmara also does not generate ineligibility ("inadmissível o
  julgamento ficto das contas por decurso de prazo").
- **Cited in**: [`topics/contas-municipais.md`](topics/contas-municipais.md) §2,
  [`topics/partidos-e-sistema-eleitoral.md`](topics/partidos-e-sistema-eleitoral.md) §7.
- **Source**: <https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=157>.

### `ADPF982` — TCE / câmara boundary revisited

- **Decided**: ~2025.
- **Holdings**:
  1. Reaffirms that TCEs can independently judge contas de gestão and
     impose administrative sanctions (débitos, multas) on mayors
     acting as ordenadores de despesas.
  2. Clarifies that **electoral ineligibility** under Ficha Limpa
     arises only from câmara rejection of contas de governo, not from
     TCE decisions on contas de gestão.
  3. Complements rather than contradicts `Tema157`.
- **Cited in**: [`topics/contas-municipais.md`](topics/contas-municipais.md) §2.
- **Source**: [Migalhas analysis](https://www.migalhas.com.br/depeso/433107/adpf-982-quem-julga-as-contas-do-prefeito-afinal).

### `ADC29` / ADC 30 + ADI 4578 (2012) — Constitucionalidade da Ficha Limpa

- **Decided**: 16 February 2012.
- **Holding**: Upheld the constitutionality of `LFL` (LC 135/2010,
  Lei da Ficha Limpa), including the provision that ineligibility
  attaches upon a **collegiate body** decision (not requiring trânsito
  em julgado). Rejected the *presunção de inocência* objection on the
  ground that ineligibility is a non-criminal restriction on
  candidacy, not a punishment.
- **Cited in**: [`topics/partidos-e-sistema-eleitoral.md`](topics/partidos-e-sistema-eleitoral.md) §7.

---

## 3. Justiça do Trabalho — reforma trabalhista

### `ADI5766` (October 2021) — Justiça gratuita pós-reforma trabalhista

- **Decided**: 20 October 2021.
- **Holdings**:
  1. `CLT.790-B` caput and §4 (expert fees from credits obtained in
     the case) — **declared unconstitutional**. Justiça gratuita
     beneficiaries cannot be forced to pay perícia fees out of credits
     won in the action.
  2. `CLT.791-A` §4 (deduction of honorários sucumbenciais from
     credits obtained in *other* proceedings) — **declared
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

### `ADI4650` (September 2015) — Doações empresariais

- **Decided**: September 2015.
- **Rel.**: Min. Luiz Fux.
- **Holding**: Declared unconstitutional the provisions of `LE` and
  `LPP` that permitted corporate donations to campaigns and political
  parties. Rationale: corporate donations distort political equality
  and create systematic dependencies between donors and elected
  officials.
- **Effective from**: 2016 elections onward.
- **Significance**: Triggered creation of the FEFC (`L13487`) as the
  public-funding replacement for corporate money. The
  pre-2016 vs. post-2016 campaign finance regimes are fundamentally
  different and any empirical work crossing the boundary must
  account for it.
- **Cited in**: [`topics/partidos-e-sistema-eleitoral.md`](topics/partidos-e-sistema-eleitoral.md) §6.
- **Source**: <https://portal.stf.jus.br/processos/detalhe.asp?incidente=4136819>.

---

## 5. Federalismo fiscal

### `ADI875` et al. (2010) — FPE coefficients

- **Decided**: 2010.
- **Holding**: Declared the rigid FPE distribution coefficients of
  `LC62` (LC 62/1989) unconstitutional for perpetuating fixed shares
  without meaningful update. Gave Congress a deadline to legislate a
  new formula.
- **Aftermath**: Congress responded with `LC143` (LC 143/2013), which
  introduced a population + per-capita-income formula transitioning
  toward more equalizing distribution.
- **Cited in**: [`topics/federalismo-fiscal.md`](topics/federalismo-fiscal.md) §2.

---

## 6. Anticorrupção penal — Lava Jato e Pacote Anticrime

### `HC126292` (2016) — Execução provisória da pena

- **Decided**: 2016.
- **Holding**: Permitted execution of prison sentence after
  **second-instance** confirmation, before trânsito em julgado.
- **Significance**: Enabled the imprisonment of high-profile Lava
  Jato defendants while their extraordinary appeals remained pending.

### `ADC43` / ADC 44 / ADC 54 (November 2019) — Reversão de `HC126292`

- **Decided**: November 2019.
- **Holding**: Reversed `HC126292`; restored the requirement of
  **trânsito em julgado** before prison execution.
- **Significance**: Triggered release of high-profile defendants
  including former President Lula. Re-affirmed the *presunção de
  inocência* in its full procedural form.

### `LulaMoro2021` — Lula vs. Moro cases

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

### `ADI6298` et al. (August 2023) — Juiz das garantias

- **Decided**: August 2023.
- **Holding**: The juiz das garantias institute introduced by `LPC`
  (`CPP.3-A`) is constitutional, with implementation guidelines set by
  the STF. Effective implementation from 2024.
- **Significance**: Mandates separation of investigatory and trial
  judges in criminal proceedings — a structural change to Brazilian
  criminal procedure.
- **Cited in**: [`topics/anticorrupcao-penal.md`](topics/anticorrupcao-penal.md) §6.

### `HC127483` (Ulisses Ramos) and HC 164.493 (Bendine)

- **Holdings**: Defined the scope of judicial review over colaboração
  premiada agreements (`LCO.4`) and the evidentiary standards for
  collaborator testimony. A colaboração alone cannot sustain a
  conviction (Art. 4 §16); corroboration is required.
- **Cited in**: [`topics/anticorrupcao-penal.md`](topics/anticorrupcao-penal.md) §3.

### `RE593727` — Tema 184 — Poder de investigação criminal do MP

- **Decided**: 14 May 2015.
- **Relator**: Min. Cezar Peluso (vencido na parte vencedora);
  acórdão redigido por Min. Gilmar Mendes.
- **Holding**: O MP tem legitimidade para promover, por autoridade
  própria, investigações de natureza penal, desde que respeitados os
  direitos e garantias constitucionais dos investigados e observada a
  reserva de jurisdição para medidas restritivas.
- **Significance**: Ended a long-running institutional dispute (the
  delegados' lobby had argued investigation was exclusive to the
  polícia judiciária). Operationalized by **CNMP Resolução 181/2017**
  via the PIC (Procedimento Investigatório Criminal). Creates a
  partial substitute for PF-led inquérito policial; MP can conduct
  criminal investigation directly when strategic or when PF is slow
  or conflicted.
- **Cited in**: [`topics/ministerio-publico.md`](topics/ministerio-publico.md) §5,
  [`topics/policia-federal.md`](topics/policia-federal.md) §1.

---

## 7. NTEP / acidentes de trabalho

### `ADI3931` (April 2020) — Constitucionalidade do NTEP

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

### `ARE652777` (2015, repercussão geral) — Salários de servidores públicos

- **Decided**: 23 April 2015 (repercussão geral).
- **Holding**: The disclosure of nominal salaries of individual
  public servants is constitutional and consistent with both the
  publicity principle (`CF.37`) and the right to privacy. Servants
  do not have a privacy interest in concealing their compensation
  paid from public funds.
- **Significance**: Foundational ruling for the federal Portal da
  Transparência practice of publishing servant salaries by name. The
  LGPD (2018) does not override this — public salary disclosure
  remains lawful under the public-interest legal basis.
- **Cited in**: [`topics/transparencia-dados.md`](topics/transparencia-dados.md) §1.

---

## 9. Matéria tributária

Case law on the ICMS/PIS/COFINS base, prescription in tax matters, and
extrajudicial collection instruments (protesto, averbação). Includes
selected STJ repetitivos that operate alongside the STF jurisprudence
in shaping execução fiscal practice.

### `Tema69` — RE 574.706 — ICMS fora da base do PIS/COFINS

- **Decided**: 15 March 2017, Plenário.
- **Rel.**: Min. Cármen Lúcia.
- **Votação**: 6×4.
- **Holding**: O ICMS não compõe a base de cálculo das contribuições
  PIS e COFINS. O imposto destacado na nota fiscal representa receita
  transitória do sujeito passivo, que apenas a arrecada em favor do
  Estado; não é faturamento/receita bruta para fins das contribuições
  sociais do `CF.195.I.b`.
- **Significance**: um dos julgamentos de maior impacto fiscal do
  STF. Gerou passivo estimado em centenas de bilhões de reais em
  compensações e repetições de indébito. Reverberou em múltiplas
  "teses filhotes" — exclusão do ICMS-ST, do ISS, do próprio PIS/COFINS
  de suas próprias bases, etc. — nem todas acolhidas pelo STF.
- **Modulação**: ver `Tema881` abaixo.
- **Cited in**: [`topics/direito-tributario.md`](topics/direito-tributario.md) §5.

### `Tema881` — RE 574.706 ED — Modulação do Tema 69

- **Decided**: 13 May 2021.
- **Holding**: Os efeitos do `Tema69` produzem-se a partir de
  **15/03/2017** (data do julgamento de mérito), ressalvadas as ações
  judiciais e os procedimentos administrativos **protocolados até
  15/03/2017**, que podem recuperar indébitos desde o quinquênio
  anterior. Confirmada a tese de que o ICMS excluído da base é o
  **destacado na nota fiscal**, não o efetivamente recolhido.
- **Significance**: resolveu a disputa central sobre os efeitos
  temporais — contribuintes que haviam ajuizado antes do julgamento
  preservaram o direito integral à repetição; os que ajuizaram depois
  ficaram restritos ao período pós-2017.
- **Cited in**: [`topics/direito-tributario.md`](topics/direito-tributario.md) §5.

### `Tema4` — RE 566.621 — Retroatividade da LC 118

- **Decided**: 4 August 2011.
- **Rel.**: Min. Ellen Gracie.
- **Holding**: A nova regra introduzida por `LC118.3` — segundo a qual
  a extinção do crédito em lançamento por homologação ocorre no
  momento do pagamento antecipado, reduzindo o prazo para pleitear
  repetição de indébito de "5+5" para 5 anos — **tem caráter
  inovador, não interpretativo**. Sua aplicação vale apenas para
  ações ajuizadas **após o término da vacatio legis (09/06/2005)**.
  Para ações protocoladas antes dessa data, aplica-se a regra antiga
  (5 anos do fato gerador + 5 anos da extinção do crédito =
  efetivamente 10 anos).
- **Significance**: fixa o marco temporal da prescrição para recuperar
  tributos pagos indevidamente — ponto operacional para qualquer
  litígio de repetição de indébito. Diretamente relacionado à
  prescrição em execução fiscal, uma vez que antecipou o marco de
  presunção de fraude à execução (`CTN.185`) para a inscrição em
  dívida ativa, via `LC118.2`–`LC118.3`.
- **Cited in**: [`topics/direito-tributario.md`](topics/direito-tributario.md) §5,
  [`topics/divida-ativa.md`](topics/divida-ativa.md).

### `ADI5135` — Protesto de CDA constitucional

- **Decided**: 9 November 2016, Plenário.
- **Rel.**: Min. Roberto Barroso.
- **Votação**: maioria.
- **Holding**: Declarada **constitucional** a inclusão das certidões
  de dívida ativa no rol de títulos passíveis de protesto
  extrajudicial (Lei 9.492/1997 Art. 1º, §único, incluído pela
  `L12767/2012`). Protesto de CDA é forma legítima de cobrança
  extrajudicial, não viola devido processo legal nem é sanção
  política, e preserva ampla defesa em ação anulatória posterior.
- **Significance**: validou o instrumento extrajudicial que hoje é
  central à estratégia de cobrança da PGFN para créditos de baixo
  para médio valor — desloca pressão de cobrança para fora do
  Judiciário, sem formalização de execução fiscal. Também
  constitucionalizou a prática de negativação do devedor em registros
  de crédito via protesto.
- **Cited in**: [`topics/divida-ativa.md`](topics/divida-ativa.md) §4.

### `ADI6040` / `ADI6055` — Averbação pré-executória parcialmente constitucional

- **Decided**: 9 December 2020, Plenário (julgadas conjuntamente).
- **Rel.**: Min. Marco Aurélio (redator p/ acórdão Min. Roberto Barroso).
- **Holding**: Parcial procedência. Os Arts. 20-B a 20-E da `L10522`
  (incluídos por `L13606.25`) foram mantidos na sua maior parte, **com
  interpretação conforme** para limitar o alcance da averbação
  pré-executória. A averbação pode ser realizada administrativamente
  pela PGFN mas **não pode equivaler a indisponibilidade integral
  sem ordem judicial** — seu efeito primário é o de tornar a
  alienação posterior presumidamente fraudulenta, análogo ao
  `CTN.185`. Notificação prévia do devedor, protesto da CDA, e
  regulamentação permaneceram íntegros.
- **Significance**: definiu os limites do instituto. Desde o
  julgamento, a PGFN opera a averbação com ressalvas — o instrumento
  funciona mais como sinalização patrimonial a terceiros do que
  como penhora administrativa plena.
- **Cited in**: [`topics/divida-ativa.md`](topics/divida-ativa.md) §5.

### `ADI7053` — Atos normativos da PGFN sobre averbação (pendente)

- **Status (2026)**: pendente de julgamento definitivo ou parcialmente
  decidida; objeto são as Portarias PGFN que regulamentaram os
  Arts. 20-B a 20-E da `L10522` depois das `ADI6040` / `ADI6055`.
  Contestação central: os atos normativos excederam a interpretação
  conforme fixada pelo STF em 2020, reintroduzindo efeitos de
  indisponibilidade que a Corte havia afastado.
- **Why it matters**: desfecho define se a PGFN pode efetivamente
  operar a averbação como instrumento de constrição patrimonial ou
  apenas como registro de fraude presumida. Verificar portal STF antes
  de citar como resolvida.
- **Cited in**: [`topics/divida-ativa.md`](topics/divida-ativa.md) §5.

### `Tema566` (STJ, repetitivo) — REsp 1.340.553 — Prescrição intercorrente em EF

- **Tribunal**: Superior Tribunal de Justiça, Primeira Seção.
- **Decided**: 12 September 2018.
- **Rel.**: Min. Mauro Campbell Marques.
- **Holding operacional** (`LEF.40`):
  1. Não localizado o devedor ou bens, o juiz **suspende** a
     execução por 1 ano. O termo inicial é a ciência inequívoca do
     exequente.
  2. Findo o prazo de 1 ano sem manifestação útil, segue **arquivamento
     sem baixa** — e daí se inicia a prescrição intercorrente de
     5 anos (`CTN.174`).
  3. Diligências protelatórias ou genéricas **não interrompem** o
     curso do prazo; apenas atos concretos capazes de resultar em
     constrição patrimonial preservam a execução.
  4. O juiz deve reconhecer a prescrição de ofício, após intimar a
     Fazenda para se manifestar.
- **Significance**: destravou o reconhecimento massivo de prescrição
  intercorrente em estoque acumulado, sobretudo em EFs antigas da
  Justiça Federal. Efeito material sobre a composição do estoque
  histórico do CNJ e na série de extinções de EF pós-2018.
- **Cited in**: [`topics/execucao-fiscal.md`](topics/execucao-fiscal.md) §5,
  [`topics/direito-tributario.md`](topics/direito-tributario.md) §5.

### `Tema1115` (STJ, repetitivo) — Prazo de 360 dias para decisão administrativa

- **Tribunal**: Superior Tribunal de Justiça, Primeira Seção.
- **Decided**: 2022.
- **Holding**: O prazo de **360 dias** do `L11457.24` para decisão
  administrativa em matéria tributária é **direito subjetivo do
  contribuinte** e tem caráter cogente. Seu descumprimento
  autoriza impetração de mandado de segurança para compelir a
  Administração a decidir, sem que isso cause extinção do crédito.
- **Significance**: consolidou o mandado de segurança como
  ferramenta rotineira contra a demora do CARF e das DRJs. Não altera
  a suspensão da exigibilidade durante o PAF, mas limita o uso da
  demora administrativa como forma de postergação.
- **Cited in**: [`topics/processo-administrativo-fiscal.md`](topics/processo-administrativo-fiscal.md) §6.

---

## 10. Quick reference table

| Case | Theme | File |
|---|---|---|
| `Tema897` (RE 852.475) | Imprescritibilidade do ressarcimento | improbidade |
| `Tema1199` (ARE 843.989) | Retroatividade `L14230` | improbidade |
| `Tema157` (RE 848.826) | Câmara julga contas prefeito | contas-municipais |
| `ADPF982` | TCE × câmara × Ficha Limpa | contas-municipais |
| `ADC29` / ADC 30 + ADI 4578 | Ficha Limpa constitucional | partidos-e-sistema-eleitoral |
| `ADI5766` | Justiça gratuita pós-reforma | justica-trabalho |
| `ADI4650` | Fim doações empresariais | partidos-e-sistema-eleitoral |
| `ADI875` et al. | FPE coefficients inconstitucionais | federalismo-fiscal |
| `HC126292` | Execução provisória da pena | anticorrupcao-penal |
| `ADC43` / ADC 44 / ADC 54 | Reversão de `HC126292` | anticorrupcao-penal |
| `LulaMoro2021` | Incompetência + parcialidade | anticorrupcao-penal |
| `ADI6298` et al. | Juiz das garantias | anticorrupcao-penal |
| `HC127483` / HC 164.493 | Colaboração premiada | anticorrupcao-penal |
| `ADI3931` | NTEP constitucional | (referenciado externamente) |
| `ARE652777` | Salários de servidores públicos | transparencia-dados |
| `Tema69` (RE 574.706) | ICMS fora da base do PIS/COFINS | direito-tributario |
| `Tema881` (RE 574.706 ED) | Modulação do Tema 69 | direito-tributario |
| `Tema4` (RE 566.621) | Retroatividade da LC 118 | direito-tributario, divida-ativa |
| `ADI5135` | Protesto de CDA constitucional | divida-ativa |
| `ADI6040` / `ADI6055` | Averbação pré-executória parcial | divida-ativa |
| `ADI7053` | Atos PGFN sobre averbação (pendente) | divida-ativa |
| `Tema566` (STJ, REsp 1.340.553) | Prescrição intercorrente em EF | execucao-fiscal |
| `Tema1115` (STJ) | 360 dias para decisão administrativa | processo-administrativo-fiscal |

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
