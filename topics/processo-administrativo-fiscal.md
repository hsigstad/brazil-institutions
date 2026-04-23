# Processo administrativo fiscal

Contencioso **administrativo** em matéria tributária: o que acontece
entre o **lançamento** (auto de infração ou notificação) e a
**inscrição em dívida ativa**. Escopo principal: o PAF federal
(`PAF` = Decreto 70.235/1972), as DRJs, o CARF, e a Câmara Superior.
PATs estaduais e municipais são citados em contorno — cada unidade
federativa tem legislação própria, fora do escopo deste repositório.

**Importante**: este é o file da fase administrativa. Para o crédito
que sai do PAF em direção à cobrança, ver `divida-ativa.md`. Para
execução judicial, ver `execucao-fiscal.md`. Para a parte geral do
direito tributário (lançamento como ato, decadência, prescrição), ver
`direito-tributario.md`.

**Topics / keywords**: processo administrativo fiscal, PAF, CARF, DRJ,
CSRF, auto de infração, impugnação, recurso voluntário, recurso
especial, voto de qualidade, representação fiscal para fins penais,
contencioso tributário administrativo, tax administrative procedure,
tax court administrative, administrative tax challenge.

**Snapshot as of 2026**: estrutura PAF estável. Voto de qualidade no
CARF mudou duas vezes em 4 anos — `LTT` (2020) extinguiu o voto
pró-Fazenda; Lei 14.689/2023 restaurou com contrapartidas
(perdão de multas e juros quando o empate prevalece). Prazo de 360
dias (`L11457.24`) foi consolidado como direito subjetivo pelo STJ
em Tema 1.115 (2022).

---

## 1. Onde o PAF se encaixa no ciclo do crédito

Sequência típica de um crédito tributário federal em disputa:

1. **Fato gerador** → obrigação tributária (`CTN.113`).
2. **Lançamento** (de ofício, por declaração, ou por homologação) →
   constitui o crédito (`CTN.142`).
3. Se homologação e o contribuinte pagou o que declarou: encerra.
4. Se a RFB discorda (auto de infração) ou se o lançamento foi de
   ofício: contribuinte recebe notificação, abrindo **30 dias** para
   impugnar (`PAF.15`).
5. **Impugnação** → **DRJ** julga em 1ª instância.
6. **Recurso voluntário** → **CARF** julga em 2ª instância (turma
   paritária Fazenda-contribuinte).
7. **Recurso especial** (cabível em caso de divergência entre câmaras)
   → **CSRF** (Câmara Superior de Recursos Fiscais).
8. Decisão administrativa definitiva (`PAF.42`):
   - Favorável ao contribuinte → extingue o crédito.
   - Favorável à Fazenda → encaminhamento à PGFN para **inscrição em
     dívida ativa** e eventual **execução fiscal**.

O PAF é assim um **filtro** — só uma fração dos autos de infração
lavrados pela RFB chega à cobrança. Os percentuais variam ao longo do
tempo e por tema, mas o volume de reversões nas DRJs e no CARF é
material para qualquer projeto que use processos tributários
judiciais como base amostral.

---

## 2. Decreto 70.235/1972 — o PAF federal

Embora formalmente um **decreto**, o `PAF` tem **força de lei** por ter
sido recepcionado sob o DL 822/1969 que autorizava o Executivo a
disciplinar o processo administrativo fiscal. Alterações ao `PAF`
normalmente ocorrem por MP ou lei ordinária.

### Ritos fundamentais

- **Início do procedimento** (`PAF.7`–`PAF.9`) — auto de infração,
  notificação de lançamento, ou termo de início de fiscalização.
  Do lançamento nasce o contencioso administrativo.
- **Impugnação** (`PAF.15`–`PAF.17`) — 30 dias do recebimento da
  notificação. A impugnação **suspende a exigibilidade** do crédito
  (`CTN.151.III`) — durante o PAF, a Fazenda não pode cobrar nem
  inscrever em dívida ativa.
- **Instrução e julgamento em 1ª instância** — pelas DRJs.
- **Recurso voluntário** — ao CARF (em 30 dias da intimação da decisão
  da DRJ). Recurso de ofício pela DRJ se a decisão exonerar valor
  acima do limite fixado em regulamento.
- **Recurso especial à CSRF** (`PAF.37`) — admissível em caso de
  divergência entre câmaras ou turmas do CARF; fundamento análogo ao
  recurso especial ao STJ por divergência jurisprudencial.
- **Decisão definitiva** (`PAF.42`) — encerra o contencioso
  administrativo e abre o prazo prescricional de 5 anos para a PGFN
  inscrever em dívida ativa e ajuizar a EF.

### Representação fiscal para fins penais

`L9430.83`: ocorrendo crime tributário (`LCOT.1`, `LCOT.2`) no auto de
infração, a RFB formaliza **representação fiscal para fins penais**,
que fica **sobrestada** enquanto pendente o contencioso administrativo
e só é encaminhada ao MPF **após a decisão definitiva**.

Esta regra é a face operacional da `SV24` (tipicidade de crime material
tributário exige lançamento definitivo). O PAF, portanto, **posterga
qualquer persecução penal** — e o parcelamento do débito durante o PAF
**suspende a pretensão punitiva** (Lei 9.964/2000, Lei 10.684/2003).

---

## 3. Delegacias de Julgamento (DRJ) — 1ª instância

Órgãos da RFB, não independentes. Julgadores são auditores da Receita.
Competência: impugnações contra lançamentos de ofício (auto de
infração e notificação de lançamento) e contra não-homologação de
compensações.

Estrutura:
- **17 DRJs** distribuídas pelo território nacional (número varia
  conforme reorganizações).
- **Turmas de julgamento** compostas por auditores.
- Decisões colegiadas, sem paridade com contribuinte — é a RFB se
  autotutelando.

Taxa de reversão nas DRJs é significativa, mas substancialmente menor
do que no CARF (a composição paritária do CARF, quando combinada com
voto de qualidade pró-contribuinte entre 2020 e 2023, resultou em
desfechos mais favoráveis ao contribuinte nessa fase).

---

## 4. CARF — 2ª instância

**Conselho Administrativo de Recursos Fiscais**. Órgão colegiado
vinculado ao Ministério da Fazenda, **paritário**: metade dos
conselheiros são representantes da Fazenda Nacional (auditores e
procuradores), metade são representantes dos contribuintes (indicados
por entidades de classe). Decisões não são bindingly apeláveis pela
Fazenda em juízo — decisão do CARF em favor do contribuinte **extingue
o crédito tributário** (`CTN.156`).

### Estrutura

- **3 Seções**, cada uma especializada em temas (IR/CSLL, IPI/PIS/COFINS,
  ICMS-ST/previdenciárias/multas).
- Cada Seção tem **4 Câmaras** com **turmas ordinárias** paritárias.
- Em cima das Seções fica a **Câmara Superior de Recursos Fiscais**
  (CSRF), também paritária, com competência para recurso especial por
  divergência.

### Voto de qualidade — a alternância 2020–2023

Em votações empatadas (frequentes dada a paridade), o **voto de
qualidade** era tradicionalmente do **presidente** (sempre um
representante da Fazenda). Portanto empate = Fazenda vence.

- **`LTT` (2020), Art. 28** introduziu no `PAF` o princípio de que,
  em caso de empate, prevalece a interpretação **favorável ao
  contribuinte** — inverteu décadas de prática.
- **Lei 14.689/2023** restaurou o voto de qualidade pró-Fazenda, **mas**
  com contrapartidas: quando o empate prevalece, há perdão de multas
  e juros de mora, limites à exigibilidade e facilidades de
  parcelamento (cobra-se só o tributo principal).

Efeito empírico: a decisão final depende do ano em que o processo foi
julgado. Projetos que usam desfechos do CARF como outcome precisam
identificar o regime de voto de qualidade vigente na data do
julgamento — a virada de 2020 e o retorno de 2023 produzem **dois
breaks estruturais**.

### CSRF — recurso especial

Função análoga ao recurso especial ao STJ no processo civil: uniformiza
jurisprudência administrativa. Admissibilidade por **divergência**
entre câmaras/turmas. Ritos equivalentes (paridade, voto de qualidade
sob o mesmo regime da Câmara).

---

## 5. Lei 9.784/1999 — base subsidiária

`LPA` é a lei geral do processo administrativo federal. Aplica-se
subsidiariamente ao PAF (`LPA.69`) — quando o Decreto 70.235/72 for
silente, recorre-se aos princípios e regras da `LPA`. Relevantes na
prática:

- **Motivação obrigatória** (`LPA.50`) — decisões administrativas,
  inclusive da DRJ e do CARF, precisam de fundamentação explícita.
- **Autotutela com decadência quinquenal** (`LPA.54`) — a
  Administração pode anular seus atos ilegais, mas decai em 5 anos
  o poder de anular atos que beneficiem administrado de boa-fé. Relevante
  em casos de revisão tardia de isenções, compensações, ou benefícios
  concedidos.
- **Recursos administrativos** (`LPA.56`–`LPA.65`) — regra geral de
  recorribilidade a três instâncias, salvo disposição em contrário (o
  PAF impõe estrutura própria, que prevalece).

---

## 6. Prazo de 360 dias — STJ Tema 1.115

`L11457.24` estabelece prazo de **360 dias** para decisão administrativa
em matéria tributária, a contar do protocolo da petição. Em 2022, no
Tema 1.115, o STJ fixou a tese: **o prazo é obrigatório** e o
contribuinte pode impetrar **mandado de segurança** para compelir a
Fazenda a decidir.

Efeito prático: embora o prazo não extinga o crédito nem altere a
suspensão da exigibilidade, cria alavancagem processual contra o
uso de instrução administrativa como instrumento de postergação.
Operacionalmente, o CARF tem estoque acumulado significativo e o prazo
é frequentemente descumprido; MS para forçar julgamento tornou-se
rotineiro pós-Tema 1.115.

---

## 7. PATs estaduais e municipais — ver arquivo dedicado

O contencioso administrativo tributário estadual (TIT-SP, CCMG,
Conselho de Contribuintes do RJ, TARF-RS, CCRF-PR, etc.) e municipal
(CMT-SP, CCM-Rio, estruturas menores) é tratado em arquivo próprio:
[`tribunais-administrativos-fiscais.md`](tribunais-administrativos-fiscais.md).

**Caveat**: PATs estaduais e municipais variam enormemente em
estrutura, paridade, prazo de recursos e duração do contencioso.
Qualquer projeto comparativo entre estados/municípios precisa
caracterizar cada sistema separadamente — o PAF federal **não** é um
bom proxy para o PAT estadual.

---

## 8. Implicações para desenho empírico

- **PAF como filtro**: amostras de execuções fiscais federais não são
  amostras de autos de infração. O que chega à EF passou por DRJ e
  (frequentemente) CARF. Taxas de reversão nas duas instâncias
  administrativas moldam a composição da amostra de EFs em termos de
  valor, matéria e perfil do contribuinte.
- **Voto de qualidade** (2020 e 2023): dois *structural breaks* em
  estoque e composição de crédito no CARF. Qualquer desfecho CARF
  usado como outcome exige identificação do regime vigente.
- **Tempo entre lançamento e ajuizamento**: 5–10 anos é típico.
  Relevante para interpretar "idade" do crédito em EFs e para
  calibrar desenhos com variação temporal no recebimento do auto.
- **Simultaneidade PAF/penal**: crimes tributários ficam dormentes
  até definitividade administrativa (`L9430.83`, `SV24`). Projetos
  que estudam denúncias por crime tributário têm lag endógeno
  determinado pelo PAF.

See also:
- `direito-tributario.md` — parte geral (lançamento, decadência,
  prescrição).
- `divida-ativa.md` — o que acontece com o crédito depois do PAF.
- `execucao-fiscal.md` — cobrança judicial.
- `anticorrupcao-penal.md` — crimes tributários (`LCOT`) e relação
  com o PAF.
