# Fluxo do crédito tributário — from fato gerador to execução fiscal

Cross-cutting narrative tracing how a tax obligation becomes an
enforceable debt and how each institutional layer generates observable
data for research design. This file connects stages covered in depth
by sibling files; it does not duplicate their substance.

**Topics / keywords**: fluxo do crédito tributário, ciclo do crédito,
lançamento, auto de infração, PAF, DRJ, CARF, inscrição em dívida ativa,
CDA, cobrança extrajudicial, protesto, transação, execução fiscal, LEF,
extinção do crédito, tax lifecycle, tax assessment pipeline, tax
collection flow, pipeline institucional.

**Snapshot as of 2026**: institutional pipeline is stable in structure
but layered by incremental reforms that changed the *composition* of
flows at each stage. Key inflection points: `LC118` (2005) antecipou a
presunção de fraude e alterou a interrupção da prescrição;
`L11457/2007` (Super-Receita) transferiu previdenciárias à PGFN;
`L12767/2012` introduziu protesto da CDA (STF ADI 5135, 2016);
`L13606/2018` introduziu averbação pré-executória (STF ADIs 6.040/6.055,
2020); STJ `Tema566` (2018) fixou o rito da prescrição intercorrente em
EF; Lei 13.988/2020 (LTT) ativou a transação tributária. Reforma
tributária (`EC132-2023`) começa transição em 2026 e pleno em 2033 — não
altera o rito, mas muda a *composição* dos créditos no estoque.

For the general framework (lançamento, prescrição, responsabilidade),
see `direito-tributario.md`. For the administrative contencioso stage,
see `processo-administrativo-fiscal.md`. For the pre-judicial collection
stage, see `divida-ativa.md`. For the judicial enforcement stage, see
`execucao-fiscal.md`. For the procuradorias that act as exequentes,
see `funcoes-essenciais.md`.

---

## 1. Fato gerador — the obligation is born

The obligation to pay tax arises at the moment defined by statute as
the *fato gerador* (`CTN.114`–`CTN.115`). Two distinctions matter
throughout the flow:

- **Obrigação vs. crédito** (`CTN.113`, `CTN.139`): obligation exists
  from the fato gerador; **crédito** only after lançamento. Only the
  crédito is exigível and can be inscribed in dívida ativa.
- **Obrigação principal vs. acessória**: principal is paying; acessória
  is declaring, scripting, issuing NFe. Non-compliance with acessórias
  converts into principal via multa.

Detail in `direito-tributario.md` sec. 2.

## 2. Lançamento — crédito tributário is constituted

`CTN.142` defines **lançamento** as the administrative act that
verifies the fato gerador, identifies the sujeito passivo, calculates
the amount, and applies penalties. Three modalities:

- **De ofício** (`CTN.149`) — Fazenda apura and notifies. Typical for
  IPTU, IPVA, and for the **auto de infração** after fiscalização.
- **Por declaração** (`CTN.147`) — contribuinte declares; Fazenda
  apura and notifies. Typical for ITBI, ITCMD.
- **Por homologação** (`CTN.150`) — contribuinte apura e paga; Fazenda
  homologates (tácita em 5 anos). **Dominates the federal system**
  (IR, ICMS, ISS, IPI, PIS/COFINS, contribuições previdenciárias).

**Operational consequence**: the large majority of federal contencioso
nasce de **lançamento de ofício revendo homologação tácita** — auto de
infração da RFB após fiscalização detecta subdeclaração. Amostras of
federal EFs therefore reflect the RFB's fiscalization policy as much
as contribuinte behavior — the selection into the pipeline is not
random. Detail in `direito-tributario.md` sec. 2.

**Decadência** — 5-year prazo to constitute the crédito
(`CTN.173.I` regra geral; `CTN.150.§4` em homologação com pagamento
antecipado). Passes this prazo sem lançamento → crédito decai and can
no longer be constituted.

## 3. Fase administrativa — PAF, DRJ, CARF

Once lançamento is notified to the contribuinte, the contestation
channel is the processo administrativo fiscal (PAF federal: Decreto
70.235/1972; estadual/municipal: leis próprias).

- **Impugnação**: 30 days after notificação to contest before the
  **DRJ** (Delegacia de Julgamento — 1ª instância administrativa).
- **Recurso voluntário**: against DRJ decision to the **CARF**
  (Conselho Administrativo de Recursos Fiscais — 2ª instância, turma
  paritária Fazenda–contribuinte).
- **Recurso especial**: divergência entre câmaras → **CSRF** (Câmara
  Superior de Recursos Fiscais).
- **Decisão administrativa definitiva**:
  - Favorável ao contribuinte → extingue o crédito.
  - Favorável à Fazenda → encaminhamento para inscrição em dívida ativa.

Two structural shifts in recent years:

- **Voto de qualidade no CARF** — Lei 13.988/2020 (LTT) extinguiu o
  voto pró-Fazenda em empates; Lei 14.689/2023 restaurou com
  contrapartidas (perdão de multas/juros quando o empate prevalece).
  Affects the reversal rate of federal autos de infração at CARF —
  a structural break for empirical work on tax contencioso.
- **Prazo de julgamento** — 360 dias (Lei 11.457/2007 Art. 24); STJ
  Tema 1.115 (2022) consolidated it as direito subjetivo. Non-compliance
  now triggers judicial remedies.

While the crédito is in PAF (impugnação, recurso), its exigibilidade
is **suspended** (`CTN.151.III`): prescrição does not run and the
contribuinte retains direito à certidão positiva com efeitos de
negativa (`CTN.206`). The pendency window can be long — years.

Detail in `processo-administrativo-fiscal.md`.

## 4. Inscrição em dívida ativa

After the crédito is definitively constituted (no PAF, or PAF
exhausted with Fazenda favorável), the procuradoria (PGFN for União
tributária; PGF for União não-tributária; PGE/PGM for
estados/municípios) performs the **inscrição em dívida ativa**
(`CTN.201`–`CTN.204`, `LEF.2`). Three immediate effects:

1. **Creates the título executivo** — the CDA (Certidão de Dívida
   Ativa) carries presunção relativa de liquidez e certeza
   (`CTN.204`, `LEF.3`), with ônus da prova inverted against the
   debtor.
2. **Presumption of fraud** — alienações posteriores presume-se
   fraudulentas (`CTN.185`). Antes de `LC118` (2005) the marker was
   valid citation in EF; antecipation is one of the central 21st-century
   tightenings of fiscal collection.
3. **CADIN registration** (federal) — restricts access to public
   credit, subventions, incentives, and public-sector contracting.

The split between **tributária** (impostos, taxas, contribuições) and
**não-tributária** (multas administrativas, ressarcimento, FGTS,
contribuições sindicais, custas) matters for procedural regime — the
`CTN` regime applies strictly only to tributária. Detail in
`divida-ativa.md` secs. 1–2.

## 5. Cobrança extrajudicial — before (or instead of) EF

Inscrição is a **fork**, not a gate to EF. Several parallel channels:

- **Notificação e pagamento em 5 dias** (`L10522.20-B`) — federal; added by
  `L13606/2018`. Baseline for federal dívida ativa.
- **Protesto da CDA** — introduced by Lei 12.767/2012 (altera Lei
  9.492/1997); constitutionality confirmed by STF ADI 5135 (2016). The
  PGFN takes the CDA to cartório, as with any credit title; negativação
  of the devedor in credit bureaus. **Virou o principal canal da PGFN
  para créditos de baixo-médio valor a partir de 2013–2014** — reduced
  EF ajuizamento volume.
- **Averbação pré-executória** (`L10522.20-B`–`L10522.20-E`,
  introduced by `L13606/2018`) — PGFN averbs the debt in registries of
  goods (imóveis, veículos), making them inalienáveis sem decisão
  judicial prévia. STF ADIs 6.040 e 6.055 (2020) reconheceram
  constitucionalidade parcial — averbação gera presunção de fraude
  perante terceiros (análoga ao `CTN.185`), mas não indisponibilidade
  integral. ADI 7053 pendente em parte.
- **Dispensa de ajuizamento por valor** (`L10522.20`) — federal créditos
  abaixo de limite fixado por portaria PGFN (R$ 20k → R$ 30k em anos
  recentes) **não são ajuizados**. Permanecem inscritos e passíveis de
  protesto, CADIN, transação. Estados e municípios têm políticas
  análogas, muito variáveis.
- **Transação tributária** — Lei 13.988/2020 (LTT) ativou o `CTN.171`
  (que existia desde 1966 mas sem regulamentação efetiva). Duas
  modalidades: por adesão a edital (classes de créditos, descontos de
  até 65% sobre multa/juros, prazos de até 120 meses) e individual
  (grandes créditos). Desde 2020 rivaliza com pagamento direto e
  prescrição nas estatísticas de saída de dívida ativa federal. **Key
  structural break in the composition of EF stock post-2020**: créditos
  com perfil "transacionável" saem; EFs remanescentes são o hard core.
- **Parcelamentos ordinários** (`L10522.10`–`L10522.14`) e **Refis**
  especiais (Refis/2000, PAES/2003, PAEX/2006, Refis da Crise/2009,
  PERT/2017, programas pós-2020). Suspendem exigibilidade
  (`CTN.151.VI`) — processos podem sair do estoque ativo sem extinção e
  retornar em caso de descumprimento. Cada Refis é ruído em séries
  temporais.

Detail in `divida-ativa.md` secs. 3–9.

## 6. Execução fiscal — the judicial stage

If the crédito chega ao ajuizamento (it survived PAF, dispensa por
valor, protesto-only, transação), the PGFN/PGE/PGM files EF under the
`LEF` (Lei 6.830/1980), with CPC subsidiário (`LEF.1`).

- **Título executivo extrajudicial** — a CDA inscrita (`CPC.784.IX`).
- **Competência** — `CF.109.I` for União; JE para estados/municípios;
  exceção na Justiça do Trabalho (`CLT.876.§unico`) para previdenciárias
  sobre sentenças trabalhistas (executadas de ofício pela JT, não pela
  PGFN na JF).
- **Citação e garantia** (`LEF.8`, `LEF.9`) — 5 days to pay or offer
  garantia (depósito, fiança bancária, seguro-garantia, nomeação de bens).
- **Penhora** (`LEF.11`) — ordem preferencial com dinheiro no topo
  (Sisbajud), depois títulos, pedras e metais, imóveis, veículos, móveis,
  direitos. Integrações: Sisbajud (`CPC.854` + `CTN.185-A`), Renajud,
  Infojud, JUCEB.
- **Defesa**: **embargos à execução** (`LEF.16`) em 30 dias, com garantia
  do juízo; **exceção de pré-executividade** (construção jurisprudencial,
  STJ Súmula 393) sem garantia, matéria restrita a ordem pública com
  prova pré-constituída.
- **Prescrição intercorrente** (`LEF.40` + STJ `Tema566`, REsp
  1.340.553, 2018) — 1 ano de suspensão + 5 anos de arquivamento sem
  diligência útil → juiz reconhece de ofício. **Tema566 é quebra
  estrutural a partir de 2018**: destrava reconhecimento massivo de
  prescrição intercorrente.

Detail in `execucao-fiscal.md`.

## 7. Extinção do crédito

`CTN.156` lists 11 modalidades. In EF contexto, the relevant exits:

- **Pagamento** (integral ou via acordo em garantia).
- **Compensação** (`L9430.74` para créditos federais).
- **Transação** (`CTN.171` + Lei 13.988/2020 no federal).
- **Prescrição** — direta ou intercorrente.
- **Decadência** — bloqueia constituição; se lançamento já ocorreu,
  não se aplica.
- **Conversão em renda do depósito**; **consignação em pagamento**.
- **Decisão judicial irreformável** (procedência de embargos, nulidade
  da CDA).
- **Dação em pagamento** em imóveis (incluída pelo LC 104/2001).
- **Remissão** (`CTN.172`) — administrative forgiveness by statute.

Survival analysis of EF requires distinguishing these exit modes —
payment and prescrição have very different fiscal meaning even when
observationally both close the case.

## 8. Research design implications

Each stage of the pipeline generates observable data and, in some
cases, structural breaks or quasi-random variation:

| Stage | Data source | Selection / structural break |
|---|---|---|
| Fiscalização and auto de infração | RFB/SEFAZ internal; DataJud for federal admin MS | RFB auditing policy is endogenous to contribuinte size, sector, risk scoring. |
| PAF (DRJ/CARF) | CARF public database (federal); state/municipal PATs vary | **Voto de qualidade reform (2020/2023)** — reversal rate at CARF shifts. |
| Inscrição em dívida ativa | PGFN em Números (federal); PGE/PGM portals variável | **`LC118` (2005)** antecipou marcos de prescrição e presunção de fraude. |
| Dispensa por valor | PGFN portarias; `L10522.20` | **Limite de ajuizamento se move ao longo do tempo** — truncamento à esquerda na distribuição de valores ajuizados. |
| Protesto da CDA | Cartórios (CENPROT); PGFN relatórios | **Lei 12.767/2012 + ADI 5135 (2016)** — canal alternativo reduz volume ajuizado pós-2013. |
| Averbação pré-executória | PGFN, SERP | **`L13606/2018` + ADIs 6.040/6.055 (2020)** — instrumento recente, uso seletivo. |
| Transação | PGFN em Números, editais | **Lei 13.988/2020** — introduz seleção endógena; EFs remanescentes são hard core. |
| Parcelamentos/Refis | PGFN, SIAFI; leis instituidoras | **Cada Refis = quebra estrutural** no estoque ativo. |
| Execução fiscal | DataJud, diários de justiça, consulta processual | **Tema566 (2018)** — massive reconhecimento de prescrição intercorrente; `L11457/2007` migrou previdenciárias à JF. |
| Garantia e penhora | Movimentos no processo, Sisbajud logs (restritos) | Rollout de Sisbajud, Renajud, Infojud: variação temporal na tecnologia de descoberta. |
| Extinção | Movimentos terminais no processo | **Competing risks** (pagamento vs. prescrição vs. transação). |

**Key empirical considerations**:

- **The EF sample is the residual of a long filter**. Only créditos that
  (a) survived fiscalização, (b) were not extinguished at PAF, (c) were
  not dispensed by value, (d) were not paid in cobrança extrajudicial,
  (e) were not transacted, (f) the Fazenda chose to ajuizar rather than
  only protestar, reach the judicial stage. Generalizing from EF
  microdata to "tax enforcement" without modeling the filter is a
  common mistake.
- **Three temporal markers are routinely confused**: fato gerador,
  constituição definitiva (fim do PAF), inscrição em dívida ativa.
  Prescrição runs from constituição; presumption of fraud from
  inscrição. Models of "tempo do débito" must pick the coherent marker.
- **Structural breaks cluster**: `LC118` (2005), `L11457` (2007), Lei
  12.767 (2012), `L13606` (2018), `Tema566` (2018), Lei 13.988 (2020)
  all land in a 15-year span and interact. Empirical work on EF stock
  or flow over 2005–2024 must track them.
- **Reform heterogeneity across federations**: the shared reference here
  is dominated by federal institutions (PGFN, CARF, RFB). Estados and
  municípios replicate the structure with huge variation in data
  quality, dispensa thresholds, protesto/transação adoption, and
  CARF-equivalents. JE-based EF studies require per-UF characterization.

See also:

- `direito-tributario.md` — parte geral (lançamento, decadência,
  prescrição, responsabilidade, reforma tributária).
- `processo-administrativo-fiscal.md` — detail on PAF/DRJ/CARF.
- `divida-ativa.md` — detail on inscrição, CDA, protesto, averbação,
  transação.
- `execucao-fiscal.md` — detail on the judicial stage.
- `funcoes-essenciais.md` — PGFN/PGE/PGM (exequentes).
- `justica-federal.md` / `justica-estadual.md` — estrutura das varas.
- `federalismo-fiscal.md` — divisão de competências por ente; which
  tributos é de quem.
