# Processo civil

Civil procedure under the Código de Processo Civil (`CPC`,
Lei 13.105/2015, effective 18 Mar 2016). This file covers the
procedural framework: judge decisions, competência, procedimento
comum, recursos, tutela provisória, execução. For **criminal
procedure**, see `processo-penal.md`. For **judicial reform history**
(including the CPC 2015 transition), see `reformas-judiciais.md`.
For **court administration and case-flow management**, see
`cnj-administracao-judicial.md`.

**Topics / keywords**: processo civil, CPC, procedimento comum,
sentença, decisão interlocutória, acórdão, competência, prevenção,
conexão, litispendência, coisa julgada, recursos, apelação, agravo,
embargos de declaração, recurso especial, recurso extraordinário,
ação rescisória, execução, cumprimento de sentença, tutela provisória,
honorários, custas.

**Snapshot as of 2026**: CPC 2015 is the governing statute. The
revoked CPC 1973 (Lei 5.869/1973) governs cases filed before
18 Mar 2016 under `CPC.1046` transitional rules.

For **ação civil pública**, see `ministerio-publico.md`. For
**improbidade administrativa**, see `improbidade.md`. For **execução
fiscal**, see `contas-municipais.md`.

---

## 1. CPC structure

The CPC 2015 is organized in five Books:

| Book | Subject | Articles |
|------|---------|----------|
| I | Normas processuais civis | 1–15 |
| II | Função jurisdicional (competência, juiz, partes) | 16–187 |
| III | Sujeitos do processo | 70–187 |
| IV | Atos processuais | 188–293 |
| V | Tutela provisória | 294–311 |
| VI | Formação, suspensão e extinção do processo | 312–317 |
| Especial | Procedimento comum + especial | 318–770 |
| Execução | Processo de execução | 771–925 |
| Recursos | Processos nos tribunais e recursos | 926–1044 |

`CPC.14`: procedural norms apply immediately to pending cases
(tempus regit actum), but do not retroactively alter completed acts.

## 2. Judge decisions (`CPC.203`–`CPC.205`)

| Type | Definition | Challengeable by |
|------|-----------|-----------------|
| **Sentença** | Terminates the *fase cognitiva* or extinguishes *execução* (`CPC.203.§1`) | Apelação |
| **Decisão interlocutória** | Any non-final decision during the proceeding (`CPC.203.§2`) | Agravo de instrumento (taxative list `CPC.1015`) or apelação (others) |
| **Despacho** | Procedural dispatch with no decisory content (`CPC.203.§3`) | Not appealable |
| **Acórdão** | Collegial judgment by a tribunal (`CPC.204`) | Embargos de declaração, RE, REsp, embargos de divergência |

All decisions published in the DJe; acórdãos must include ementa
(`CPC.205`).

**Research implication**: case-duration studies must distinguish
sentença (merit disposition) from decisão interlocutória (interim
ruling) and despacho (no decisory content). Court datasets often
classify by *movimentação* code; map to CPC categories before
measuring duration.

## 3. Competência

### Absoluta vs. relativa

- **Absoluta** (matéria, pessoa, função): cannot be waived; court
  must recognize *ex officio* at any stage (`CPC.64`). Violation →
  nullity.
- **Relativa** (territorial, valor da causa): waivable if not raised
  in preliminary contestação (`CPC.65`). Raised as preliminar de
  contestação, not by exceção (CPC 2015 eliminated the standalone
  exceção de incompetência).

### Prevenção and conexão

- **Conexão** (`CPC.55`): two actions share pedido or causa de pedir
  → reunião for joint judgment. Prevents contradictory decisions.
- **Continência** (`CPC.56`): one action's pedido encompasses the
  other's.
- **Prevenção** (`CPC.59`): the court that first registered
  (*registrou ou distribuiu*) the action is prevento.

### Litispendência and coisa julgada

- **Litispendência** (`CPC.337.§1`–`§3`): identity of parties,
  causa de pedir, and pedido between two pending actions → later
  action extinguished.
- **Coisa julgada** (`CPC.502`–`CPC.508`): final decision on the
  merits binds the parties. Material coisa julgada attaches to the
  dispositivo.

## 4. Impedimento and suspeição

- **Impedimento** (`CPC.144`): objective grounds (judge was witness,
  relative of party/lawyer up to 3rd degree, etc.) — recognized
  *ex officio*, nullity if violated. CNJ Resolução 200/2015 extends
  to indirect kinship via hidden arrangements.
- **Suspeição** (`CPC.145`): subjective grounds (friendship/enmity,
  gifts, financial interest). Must be raised by the parties.
- `CPC.144.§2`: parties may not engineer impediment by substituting
  counsel after distribution.

## 5. Procedimento comum (`CPC.318`–`CPC.512`)

### Phases

1. **Petição inicial** (`CPC.319`–`CPC.331`): must contain parties,
   facts, legal basis, pedido, valor da causa, evidence, and
   conciliation preference. Judge may order amendment within 15 days
   (`CPC.321`); indeferimento if defects uncured (`CPC.330`).

2. **Liminar improcedência** (`CPC.332`): judge may dismiss outright
   if claim contradicts súmula, acórdão in recursos repetitivos, or
   if prescription/decadência is evident.

3. **Audiência de conciliação/mediação** (`CPC.334`): mandatory
   unless both parties opt out or the claim does not admit
   autocomposição.

4. **Contestação** (`CPC.335`–`CPC.342`): 15-day deadline. All
   defenses raised here; new allegations barred after (`CPC.342`).
   Failure to contest → revelia (`CPC.344`, facts presumed true).

5. **Saneamento** (`CPC.357`): judge resolves preliminary issues,
   fixes controverted facts, organizes proof. May grant partial
   summary judgment.

6. **Instrução** (`CPC.358`–`CPC.368`): witness testimony, expert
   evidence. Judge may attempt conciliation (`CPC.359`).

7. **Sentença**: in hearing or within 30 days (`CPC.366`).

### Sentença classification

| Outcome | CPC | Effect |
|---------|-----|--------|
| **Com resolução de mérito** | `CPC.487` | Coisa julgada material |
| **Sem resolução de mérito** | `CPC.485` | No coisa julgada; may refile (except litispendência, coisa julgada, perempção) |

Grounds for *sem resolução*: indeferimento of initial petition,
abandonment (>1 year), perempção (3 abandonments), litispendência,
coisa julgada, lack of standing or interest.

### Sentença elements (`CPC.489`)

- **Relatório**: summary of parties, claims, defense
- **Fundamentação**: must address all arguments; must explain
  precedent application; must not use indeterminate legal concepts
  without justification
- **Dispositivo**: operative holding

## 6. Recursos (`CPC.994`–`CPC.1044`)

### Overview table

| Recurso | Against | Prazo | Effect | CPC |
|---------|---------|-------|--------|-----|
| Apelação | Sentença | 15 days | Suspensivo + devolutivo | `CPC.1009`–`CPC.1014` |
| Agravo de instrumento | Decisão interlocutória (taxative list) | 15 days | Devolutivo only (suspensivo by request) | `CPC.1015`–`CPC.1020` |
| Agravo interno | Decisão monocrática do relator | 15 days | — | `CPC.1021` |
| Embargos de declaração | Obscuridade, contradição, omissão | 5 days | Interrupts other prazos | `CPC.1022`–`CPC.1026` |
| Recurso ordinário | Decisions in mandado de segurança / habeas data by tribunais | 15 days | — | `CPC.1027`–`CPC.1028` |
| Recurso especial (REsp) | Violação de lei federal by tribunal | 15 days | Devolutivo | `CPC.1029`–`CPC.1041` |
| Recurso extraordinário (RE) | Violação da CF by tribunal | 15 days | Devolutivo | `CPC.1029`–`CPC.1041` |
| Embargos de divergência | Divergência interna no STF/STJ | 15 days | — | `CPC.1043`–`CPC.1044` |

### Key procedural points

- **Prequestionamento**: REsp/RE require the constitutional/legal
  question to have been raised and decided below. Embargos de
  declaração are the standard vehicle for prequestionamento.
- **Repercussão geral** (`CPC.1035`): threshold filter for RE —
  STF must recognize the question's general repercussion before
  admitting.
- **Recursos repetitivos** (`CPC.1036`–`CPC.1041`): when multiple
  RE/REsp raise the same legal question, STF/STJ selects
  representative cases and suspends the rest. Binding on lower courts.
- **Efeito suspensivo**: apelação has it by default; agravo de
  instrumento does not (can be requested). Embargos de declaração
  interrupt (not suspend) the prazo for other recursos.

### Acórdão mechanics

Judgment session (`CPC.937`–`CPC.942`): relator presents → parties
speak (15 min each) → preliminary questions → voting. If not
unanimous, the *técnica de julgamento ampliado* (`CPC.942`) adds
more judges for a new session. Acórdão drafted by the relator if
in the majority; otherwise by the first vote in the majority.

## 7. Ação rescisória (`CPC.966`–`CPC.975`)

Extraordinary action to rescind a decision with coisa julgada.
Grounds include: prevaricação/concussão/corrupção of the judge,
judge impeded, dolo of the winning party, violation of *norma
jurídica*, false evidence. Prazo: 2 years from trânsito em julgado
(`CPC.975`). Competência: tribunal that rendered or would have
reviewed the decision.

## 8. Tutela provisória (`CPC.294`–`CPC.311`)

| Type | Basis | Reversibility |
|------|-------|--------------|
| **Tutela de urgência — antecipada** (`CPC.300`–`CPC.304`) | Probability of right + danger of damage or risk to useful result | Respondent may post bond |
| **Tutela de urgência — cautelar** (`CPC.305`–`CPC.310`) | Same basis; preserves status quo rather than granting the right | — |
| **Tutela da evidência** (`CPC.311`) | No urgency required; right is evidently provable (e.g., súmula, prova documental, abuso de direito de defesa) | — |

Tutela provisória can be granted *antecedente* (before the main
action) or *incidental* (during). If granted antecedente, plaintiff
must file the main action within 30 days (urgência) or the tutela
stabilizes after 2 years if not challenged (`CPC.304`).

## 9. Execução and cumprimento de sentença

### Cumprimento de sentença (`CPC.513`–`CPC.538`)

Enforcement of judicial titles (sentenças, acórdãos, homologated
agreements). Debtor intimated to pay within 15 days; failure →
10% fine + 10% honorários (`CPC.523`).

### Processo de execução (`CPC.771`–`CPC.925`)

Enforcement of extrajudicial titles (promissory notes, debentures,
contracts with specific enforceability). Debtor cited to pay within
3 days (`CPC.829`).

### Execução fiscal

Governed by LEF (Lei 6.830/1980), not the CPC, with CPC as
subsidiary. See `contas-municipais.md` for TCE/execução fiscal
interaction. Key features:

- Filed by municipal, state, or federal fazenda for dívida ativa
  (tax and non-tax debts already administratively constituted)
- Debtor cited to pay or offer garantia within 5 days (LEF Art. 8)
- Embargos à execução (30 days) require garantia unless debtor is
  hipossuficiente
- Penhora order: cash → bonds → precious metals → real property →
  vehicles → other assets → rights (LEF Art. 11)
- Suspension if debtor/assets not found; arquivamento after 1 year
  suspended; prescrição intercorrente after 5 years archived
  (LEF Art. 40, `CTN.174`)

## 10. Honorários and custas

- **Honorários sucumbenciais** (`CPC.85`): 10–20% of the condenação
  value (fazenda pública: `CPC.85.§3`, tiered scale). Set in the
  sentença; belong to the lawyer, not the party (`CPC.85.§14`).
- **Custas**: court fees vary by state (each TJ has its own fee
  schedule). Federal courts follow Lei 9.289/1996.
- **Gratuidade de justiça** (`CPC.98`–`CPC.102`): available to
  natural or legal persons who cannot afford custas without prejudice
  to subsistence. Presumed for natural persons who declare
  insufficiency (`CPC.99.§3`). Covers custas, honorários periciais,
  and sucumbenciais (suspended for 5 years if beneficiary loses).

## 11. Research-design implications

- **Case classification**: court databases classify cases by *classe
  processual* (CNJ Resolução 46/2007 taxonomy). Map these to CPC
  categories (conhecimento, execução, cautelar/tutela) before
  analyzing outcomes.
- **Duration measurement**: "case duration" should distinguish
  fase de conhecimento (petição inicial → sentença) from execução
  (início do cumprimento → satisfação). Many cases in *cumprimento
  de sentença* or *execução fiscal* stay open for years in
  suspension/arquivamento, distorting unconditional duration stats.
- **Settlement vs. judgment**: CPC 2015 made conciliation/mediation
  hearings mandatory (`CPC.334`). Post-2016 settlement rates may
  show a structural break. Identify settlements via *movimentação*
  codes for homologação de acordo.
- **Revelia**: defendant no-show rate is a signal of case quality
  and defendant awareness. High revelia in execução fiscal is
  structural (debtors not found), not informative about legal merit.
- **Recursos repetitivos**: STJ/STF decisions under `CPC.1036`
  bind lower courts. Cases suspended pending a repetitivo are not
  "inactive" — they are awaiting a system-wide resolution. Exclude
  or flag these in duration analyses.
- **Chronological-order rule** (`CPC.12`): CPC 2015 introduced
  mandatory chronological judgment order (with broad exceptions).
  In practice, compliance is uneven — see `cnj-administracao-judicial.md`.
