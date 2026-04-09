# Improbidade administrativa

Civil prosecution of public-administration misconduct. The core statute
is [[LIA]] (Lei 8.429/1992), substantially reformed by [[L14230-2021]].
This is not a criminal proceeding but a civil action with quasi-criminal
sanctions (loss of office, suspension of political rights, fines,
prohibition from contracting with the public administration).

**Topics / keywords**: improbidade administrativa, civil corruption, LIA,
Lei 8.429, Lei 14.230, dolo, culpa, enriquecimento ilícito, prejuízo ao
erário, violação de princípios, ação civil pública, Ministério Público,
Ficha Limpa, STF Tema 1199, ressarcimento, imprescritível.

**Snapshot as of 2026**: post-reform jurisprudence is still settling.
STF Tema 1199 (ARE 843989, Aug 2022) governs retroactivity of the
dolo-only standard. ADPF 982 (~2025) clarifies the TCE / câmara boundary
for the ineligibility consequence (see `contas-municipais.md`).

For procurement-specific fact patterns most often prosecuted as
improbidade, see `licitacoes.md`. For the Ficha Limpa eligibility
consequence and the câmara procedure that converts a rejected account
into ineligibility, see `contas-municipais.md`. For criminal statutes
that may run in parallel (lavagem, organização criminosa, Lei
Anticorrupção), see `anticorrupcao-penal.md`.

This file does not paraphrase statutory text. For the verbatim wording
of any LIA article — current, original, or as amended by a specific
law — resolve the bracketed citations against `tools/leis_artigos/`.
The text below characterizes what's in the statute and explains why
it matters.

Compiled from personal research notes on civil corruption prosecution
in Brazil.

---

## 1. Structure of the LIA

### Scope ([[LIA.1]])

The LIA reaches any agent — public servant or not — who acts against
the direct, indirect, or foundational administration of any branch of
the União, estados, DF, municípios, territórios, state-owned
enterprises, or entities receiving public benefit. The breadth of the
subject pool is deliberate: improbidade is meant to follow the public
money, not the formal employment status of the actor.

### Three categories ([[LIA.9]]–[[LIA.11]])

The LIA classifies improbidade into three escalating categories. Each
article opens with a *caput* defining the category, followed by a
non-exhaustive list of incisos giving canonical examples.

- **[[LIA.9]] — Enriquecimento ilícito.** Personal patrimonial gain
  through the office. Most severe category and the narrowest factually:
  the official has to have *taken something*. The incisos cover bribes,
  gifts from interested parties, use of public labor for private gain,
  and kickbacks on contracts.
- **[[LIA.10]] — Prejuízo ao erário.** Conduct causing loss to the
  public treasury, whether the official benefited personally or not.
  By far the most common category in TJSP improbidade caseloads
  because it captures procurement irregularities, dispensações
  irregulares, overpricing, and failure-to-collect fact patterns.
  Pre-reform [[LIA.10:original]] reached both intentional and
  negligent conduct; [[LIA.10 from:L14230-2021]] restricted it to
  dolo only.
- **[[LIA.11]] — Violação de princípios administrativos.** The
  catch-all: conduct violating legality, impessoalidade, moralidade,
  publicidade, etc. Pre-reform this was a true open-textured standard;
  [[LIA.11 from:L14230-2021]] narrowed it to a *taxative* list of
  conduct types in [[LIA.11.§1 from:L14230-2021]]. The reform's
  intent was to stop Art. 11 from absorbing procedural irregularities
  that didn't fit Art. 9 or 10.

### Sanctions ([[LIA.12]])

[[LIA.12]] sets the sanction menu by category. Every conviction can
combine loss of public function, full ressarcimento, asset forfeiture,
and prohibition from contracting with the public administration; what
differs across categories is the scale of the fine and the length of
the political-rights suspension. Post-reform structural shape:

| Category | Suspensão de direitos políticos | Proibição de contratar | Multa |
|---|---|---|---|
| [[LIA.9]]  | up to 14 years | up to 14 years | ≤ value of patrimonial increment |
| [[LIA.10]] | up to 12 years | up to 12 years | ≤ 2× the loss |
| [[LIA.11]] | up to 4 years  | up to 4 years  | ≤ 24× monthly remuneration |

The 14/12/4 ratio is the load-bearing fact for research design — it
governs which category the MP prefers to charge, since [[LIA.9]]
charges trigger the heaviest political consequences but require
proving personal enrichment.

### Standing to sue ([[LIA.17]])

The most consequential procedural change of the 2021 reform.

- **Pre-reform** ([[LIA.17:original]]): MP **or** the affected public
  entity (*pessoa jurídica interessada*) could initiate the action.
- **Post-reform** ([[LIA.17 from:L14230-2021]]): only the MP can
  initiate. Public entities participate only as intervenientes.

The shift centralizes prosecutorial discretion in the MP and removes
self-prosecution by victim entities. For empirical work this is a
clean before/after design point: filing rates by entity type drop to
zero after October 2021.

### Prescription

- **Pre-reform**: 5 years from the end of term (elected officials)
  or from knowledge of the act (other servants).
- **Post-reform** ([[LIA.23 from:L14230-2021]]): 8 years from the act,
  with intermediate prescription rules attached to procedural phases.
- **STF Tema 897 (RE 852475)**: ressarcimento ao erário for *dolosa*
  improbidade is **imprescritível**. The declaratory and sanction
  components remain subject to prescription; only the reparation of
  damages is perpetual.

---

## 2. The 2021 reform ([[L14230-2021]])

Published 26 October 2021. Six structural changes that, taken together,
narrow the regime to its most serious cases:

1. **Elimination of culposa improbidade.** Only **dolosa** conduct is
   actionable. [[LIA.1.§1 from:L14230-2021]] introduces an explicit
   dolo definition (conscious will to achieve the illicit result).
   Mere negligence, missed deadlines, and failure to supervise no
   longer suffice.
2. **Exclusive MP standing** ([[LIA.17 from:L14230-2021]]).
3. **New 8-year absolute prescription** ([[LIA.23 from:L14230-2021]]).
4. **Narrowed [[LIA.11]]** via the taxative list in
   [[LIA.11.§1 from:L14230-2021]].
5. **Acordo de não persecução cível** ([[LIA.17-B from:L14230-2021]]):
   formal MP-defendant settlement with judicial homologação.
6. **Procedural tightening**: heightened evidentiary standards,
   expanded defense opportunities, stricter standards for interim
   measures (bloqueio de bens).

### STF Tema 1199 — retroactivity (ARE 843989, 18 Aug 2022, Rel. Alexandre de Moraes)

Central jurisprudence on whether and how the reform reaches pre-existing
cases. STF held:

1. The elimination of culposa improbidade is **irretroactive in bonam
   partem** for acts already subject to *trânsito em julgado* — past
   convictions stand.
2. For **pending cases** without final judgment at the reform date, the
   new standard applies immediately: courts must re-examine for dolo
   and dismiss if only negligence is proven.
3. The new 8-year prescription is also **irretroactive** in clock terms:
   the 8-year period begins running from 26 Oct 2021, not from the
   underlying act, for pre-reform conduct.
4. The "lei mais benéfica" doctrine does not generally extend to
   improbidade (it's civil, not criminal), but the elimination of
   culposa is recognized as a substantive change with the
   retroactivity limits above.

For the canonical description of this case, see `jurisprudencia-stf.md`
(Tema 1199).

### Practical effect on caseloads

- Cases originally filed under the broader pre-reform standard had to
  be re-pleaded to allege dolo, or dismissed.
- The most affected category: **procedural and documentary
  irregularities in procurement**, previously prosecuted under culposa
  [[LIA.10:original]]. After the reform these require proof that the
  official *intended* the illicit outcome, not merely that they were
  careless.
- A selection shift in post-October 2021 sentenças is the natural
  empirical prediction: more egregious cases reaching judgment, fewer
  routine procedural-error prosecutions.

---

## 3. Procedural framework (Ação Civil Pública de Improbidade)

### Investigation and filing

- **Notícia de Fato (NF)**: initial intake at the MP. 120 days
  (extendable) to triage.
- **Inquérito Civil (IC)**: formal investigation by the MP. Should
  conclude in 1 year, frequently extended.
- **Ação Civil Pública (ACP)**: filed before the competent court (TJ
  state-level for state/municipal officials; TRF federal for federal
  officials or federal funds).

### Jurisdiction

- **State-level** (TJ) for state/municipal officials and state/municipal
  funds — the bulk of the caseload.
- **Federal** (TRFs) when federal funds are involved (convênios, SUS
  transfers, FPM, etc.) or when the defendant is a federal official.
- **Foro por prerrogativa**: improbidade actions do **not** carry
  foro-privilegiado status in general — they follow ordinary
  first-instance rules regardless of the defendant's political office.
  See `procedimentos-legais.md` for the broader foro discussion.

### Case flow and timing

- Filing → *notificação prévia* of the accused (60 days for preliminary
  response, post-2021) → judicial decision whether to receive the
  petition → contestação → instrução → sentença → appeal.
- **Typical duration**: 7–8 years from filing to first-instance
  sentença in TJSP is common in observed cases.
- CNJ study cited in MPSP Manual: average time to judgment in state
  courts ~1,586 days (~4.3 years).

### Outcomes

- **Procedente**: conviction (full or partial).
- **Improcedente**: acquittal on the merits.
- **Extinta**: dismissed on procedural or legal grounds (prescription,
  standing, res judicata, etc.).

### Appeals

- Appeal to the TJ chambers (apelação).
- Further recourse to STJ (recurso especial) and STF (recurso
  extraordinário) on federal-law / constitutional questions.

---

## 4. Interaction with other proceedings

The same underlying conduct can be prosecuted in parallel under multiple
regimes:

| Regime | Statute | Competent authority | Sanction type |
|---|---|---|---|
| Improbidade | [[LIA]] | MP → TJ/TRF | Civil sanctions (loss of office, political rights, fines, ressarcimento) |
| Criminal corruption | [[CP]] + Lei 8.137/90 + [[L8666]] Arts. 89–98 | MP → criminal court | Criminal penalties (imprisonment, fines) |
| Cartel / competition | Lei 12.529/11 | CADE (admin) | Administrative fines up to 20% of revenue |
| Corporate liability | Lei 12.846/13 (Anticorrupção) | CGU / MP | Administrative + judicial sanctions on firms |
| Fiscal / audit | LC 101/00 (LRF), TC statutes | TCU / TCE / TCM | Débitos, multas, inabilitação |
| Electoral ineligibility | [[LI.1.I.g]] | Câmara → TSE | 8-year ineligibility (Ficha Limpa) |

Parallel prosecution is expressly permitted. A TCE finding of
irregularity is **not** itself a judicial finding of improbidade, but
can trigger MP investigation. A cartel prosecuted at CADE can also
generate an improbidade action against the public officials who
facilitated it.

**Source**: CADE, *Guia de Combate a Cartéis em Licitação* (2019),
Part IV, p. 58 (summary table).

---

## 5. Ministério Público's role

MP-SP (Ministério Público do Estado de São Paulo) is the dominant actor
in state-level improbidade prosecution. Federal cases (involving
federal funds or entities) go to MPF.

- **~2,000 active promotores** in São Paulo state.
- Organized by **entrância** (tier): Inicial → Intermediária → Final.
  Small comarcas = inicial; São Paulo capital = final.
- **Specialized positions in the capital**: Promotor de Justiça do
  Patrimônio Público (corruption-specific); GAECO (organized crime);
  Promotor de Justiça Criminal.
- **Small comarcas**: single prosecutor handles all case types,
  including improbidade.
- **Selection discretion**: MP exercises broad discretion in which
  investigations to pursue. This is a major source of sample selection
  for researchers — not all alleged irregularities become ACPs.

For general MP structure (career, guarantees, CNMP oversight), see
`ministerio-publico.md`.

---

## 6. Key empirical facts

| Fact | Value | Source |
|---|---|---|
| Average state-court judgment time | ~1,586 days (~4.3 years) | CNJ study cited in MPSP Manual |
| Typical improbidade duration (TJSP) | 7–8 years filing → sentença | Observed in sampled TJSP cases |
