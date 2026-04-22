# Dívida ativa e cobrança pré-judicial

O que acontece com o crédito tributário depois de definitivamente
constituído no contencioso administrativo — e **antes** de virar
execução fiscal judicial. Foco: inscrição em dívida ativa, Certidão de
Dívida Ativa (CDA), estrutura das procuradorias (PGFN/PGE/PGM),
cobrança extrajudicial (notificação, CADIN, protesto, averbação
pré-executória), e transação tributária.

Para a fase administrativa (PAF, DRJ, CARF), ver
`processo-administrativo-fiscal.md`. Para a execução judicial, ver
`execucao-fiscal.md`. Para a parte geral do direito tributário, ver
`direito-tributario.md`.

**Topics / keywords**: dívida ativa, inscrição em dívida ativa, CDA,
PGFN, PGE, PGM, CADIN, protesto de CDA, averbação pré-executória,
transação tributária, cobrança extrajudicial, certidão negativa, CND,
CPEN, tax debt registry, tax collection, extrajudicial tax enforcement.

**Snapshot as of 2026**: o rol de instrumentos pré-judiciais cresceu
bastante desde 2012 — protesto da CDA (`L12767/2012`, confirmado
constitucional pela STF ADI 5135 em 2016); averbação pré-executória
(`L13606`, parcialmente admitida pelo STF em 2020 nas ADIs 6.040 e
6.055, com ADI 7053 pendente); transação tributária (`LTT`, 2020 em
diante). A tendência estrutural é que a inscrição em dívida ativa
esteja gradualmente se tornando menos um *precedente* da EF e mais uma
alternativa a ela.

---

## 1. Inscrição em dívida ativa

### O ato e o efeito

**Inscrição em dívida ativa** é o ato administrativo da procuradoria
que atesta que o crédito é líquido e certo, e viabiliza sua cobrança
como título executivo extrajudicial. Regulada por `CTN.201`–`CTN.204`
e `LEF.2`–`LEF.3`.

Três efeitos imediatos da inscrição:

1. **Cria o título executivo** — a CDA (Certidão de Dívida Ativa) tem
   **presunção de liquidez e certeza** (`CTN.204`, `LEF.3`), ônus da
   prova invertido contra o devedor.
2. **Marca o início da presunção de fraude** — alienações posteriores
   presumem-se fraudulentas (`CTN.185`, após `LC118`). Antes de 2005
   o marco era a citação válida em EF; a antecipação é um dos
   principais endurecimentos da cobrança fiscal no século XXI.
3. **Cadastra o devedor no CADIN** (federal), com efeitos de
   restrição de acesso a crédito público e certificação.

### Quem pode inscrever

Inscrição é monopólio das procuradorias:

- **União** (tributária) — **PGFN** (Procuradoria-Geral da Fazenda
  Nacional), órgão da AGU por `LOAGU.12`.
- **União** (não-tributária) — PGF (Procuradoria-Geral Federal) para
  autarquias e fundações, também da AGU.
- **Estados** — **PGE** (Procuradoria-Geral do Estado), regulada por
  lei estadual.
- **Municípios** — **PGM** (Procuradoria-Geral do Município).

Esta estrutura importa para selecionar fontes de dados: cada
procuradoria publica separadamente seu estoque e fluxo de dívida
ativa. A PGFN publica dados consolidados anuais (Relatório PGFN em
Números); muitas PGEs publicam dados em portais próprios, com
qualidade variável.

### Dívida ativa tributária vs não-tributária

`LEF.2` abrange ambas:
- **Tributária**: impostos, taxas, contribuições, multas tributárias.
- **Não-tributária**: multas administrativas (Anvisa, Ibama, Anatel),
  ressarcimento ao erário por improbidade, FGTS não recolhido,
  contribuições sindicais, custas judiciais.

A distinção importa para competência e regime processual (não-tributária
não se beneficia das regras específicas do `CTN`, e.g., a presunção de
fraude do `CTN.185` pode ser lida mais restritivamente).

---

## 2. CDA — Certidão de Dívida Ativa

A CDA (`LEF.2.§5`, `CTN.202`) é um **título executivo extrajudicial**
com conteúdo mínimo legal: valor original, juros, multa, fundamento
legal, termo inicial, número do processo administrativo de origem,
identificação do devedor.

### Presunção de liquidez e certeza

`CTN.204` / `LEF.3`: a CDA goza de presunção *relativa* de liquidez e
certeza. O devedor pode desconstituir, mas precisa de **prova
inequívoca** — inverte o ônus comum de quem executa (que tem de
comprovar seu crédito).

Vícios formais da CDA (falta de fundamento legal, ausência de dados
essenciais) podem levar à **nulidade** em sede de embargos ou exceção
de pré-executividade. A jurisprudência do STJ é consistente em não
admitir "substituição" de CDA para sanar vícios materiais (Súmula 392
STJ: admite-se substituição até a prolação de sentença, para correção
de erro material ou formal, vedada modificação do sujeito passivo da
execução).

### Ciclo de vida da CDA

- **Inscrita** mas não ajuizada: base para cobrança extrajudicial
  (notificação, protesto, CADIN). Fica no estoque de dívida ativa.
- **Ajuizada**: distribuída ao juízo competente (ver `execucao-fiscal.md`).
- **Extinta**: por pagamento, prescrição, transação, remissão, ou
  decisão judicial que anule o crédito.

---

## 3. CADIN — Cadastro Informativo de Créditos Federais (`L10522`)

Registro público de pessoas físicas e jurídicas com créditos não
quitados com órgãos federais. Principal efeito: **veda concessão de
crédito público** (`L10522.6`), **subvenções, incentivos fiscais** e
contratação com órgãos federais.

Relevante para pesquisa:
- É um dos canais pelos quais inadimplência tributária afeta
  comportamento econômico do devedor (empresas negativadas perdem
  acesso a linhas públicas).
- Permite ligação entre execução fiscal e restrição de crédito — uma
  variável de cost observável para análise de resposta à cobrança.

CADIN existe só para débitos **federais**. Estados e municípios mantêm
cadastros próprios (p. ex. CADIN estadual em SP, RJ).

---

## 4. Protesto da CDA

Introduzido por `L12767/2012` (alterou Lei 9.492/97). Permite que a
Fazenda leve a CDA a protesto em cartório, como qualquer título de
crédito, **sem ajuizar** execução fiscal.

**ADI 5135** (STF, 2016) — julgou o protesto de CDA **constitucional**
por maioria, rejeitando a tese de que protesto de crédito público
violaria devido processo legal. Argumento central: protesto é cobrança
extrajudicial legítima, não execução; preserva ampla defesa em sede
posterior.

Efeito operacional:
- Negativação do devedor em registros de crédito (Serasa, SPC, bureaus).
- Pressão reputacional sem os custos de EF judicial.
- **Dispensa o ajuizamento de EF** para créditos abaixo do limite
  (`L10522.20` e atos PGFN — ver abaixo). Para créditos médios
  (abaixo do limite de ajuizamento, acima do limite de dispensa total),
  o protesto é a ferramenta primária.

Virou **o instrumento principal** da PGFN para créditos "de baixo para
médio valor" — reduziu o volume ajuizado a partir de 2013–2014.

---

## 5. Averbação pré-executória (`L13606`, inserindo `L10522.20-B`–`L10522.20-E`)

Introduzida em 2018 pelo `L13606`. Permite que a PGFN, depois de
notificar o devedor e dar 5 dias para pagamento, **averbe a dívida
em registros de bens** (imóveis, veículos), tornando-os **inalienáveis**
**sem decisão judicial prévia**.

Crítica: sem contraditório prévio nem ordem judicial, a averbação
funciona como penhora administrativa.

**ADIs 6.040 e 6.055** (STF, 2020): reconheceram **constitucionalidade
parcial** do instituto, impondo salvaguardas — a averbação não pode
equivaler a indisponibilidade integral; só gera efeito de presunção
de fraude (análogo ao `CTN.185`) em relação a terceiros adquirentes.
**ADI 7053** sobre os atos normativos da PGFN que regulamentam a
averbação segue pendente em partes.

Efeito prático de curto prazo: a averbação é usada seletivamente, mais
como sinalização ao devedor e a terceiros do que como execução
administrativa plena. Cadastros cartorários (SERP, Sisbajud, Serasa)
recebem a averbação mesmo com os limites impostos pelo STF.

---

## 6. Transação tributária (`LTT`)

Principal inovação estrutural na cobrança da dívida ativa federal nos
anos 2020. Regulamenta `CTN.171` (transação como modalidade de extinção
do crédito), que existia no CTN desde 1966 mas nunca havia sido
efetivamente implementada.

Duas modalidades:

- **Transação por adesão a edital** (`LTT.2`) — a PGFN publica edital
  com termos (desconto, prazo, garantias) aplicáveis a uma classe de
  créditos (geralmente definidos por faixa de valor, situação
  econômica do devedor, matéria). Contribuinte adere no prazo.
- **Transação individual** (`LTT.2`) — para créditos de grande valor
  ou situações específicas, negociada caso a caso. Dependeu
  historicamente de limite de valor (`LTT.11`) ajustado por atos da
  PGFN.

Benefícios típicos: descontos de até 65% sobre multas e juros (nunca
sobre o tributo principal), prazos de até 120 meses, flexibilização
de garantias. Em contrapartida o contribuinte desiste de discussões
administrativas e judiciais e reconhece o débito.

Impacto no estoque de dívida ativa: a PGFN utiliza transações por
adesão como instrumento ativo de gestão — editais periódicos
liquidam grandes porções do estoque. Dados PGFN em Números mostram
que desde 2020 a transação é responsável pela saída de parte
significativa dos créditos, rivalizando com pagamento direto e
extinção por prescrição.

Transação de contencioso de relevante controvérsia (`LTT.14`) atinge
litígios judiciais e administrativos de temas repetitivos — é o
canal pelo qual a Fazenda resolve teses-PGFN quando derrota judicial
aparentemente inevitável torna desejável capitalizar com recuperação
parcial.

Para detalhe sobre o voto de qualidade no CARF (também alterado pelo
`LTT.28` e depois pela Lei 14.689/2023), ver
`processo-administrativo-fiscal.md`.

---

## 7. Dispensa de ajuizamento por valor

`L10522.20` autoriza o Ministro da Fazenda a dispensar o ajuizamento
de execuções fiscais federais **abaixo de um limite** (R$ 10 mil no
texto original; ajustado posteriormente por portaria — atualmente
R$ 20 mil na esfera federal).

Créditos abaixo do limite:
- Continuam inscritos em dívida ativa.
- Permanecem passíveis de cobrança extrajudicial (notificação, CADIN,
  protesto).
- Não geram execução fiscal judicial.

Implicação amostral: universos de execuções fiscais federais têm
**censura de valor mínimo** — a distribuição de valores ajuizados é
truncada à esquerda pelo limite vigente. Projetos que comparam
distribuições de valor ao longo do tempo precisam rastrear alterações
no limite.

Estados e municípios têm políticas análogas, com limites muito
variáveis (alguns municípios ajuízam débitos de qualquer valor;
outros têm limites de dispensa altos).

---

## 8. Certidões (CTN.205–206)

Prova documental da situação do devedor perante a Fazenda:

- **CND** — Certidão Negativa de Débitos: emitida quando não há
  débitos registrados.
- **CPEN / Positiva com Efeitos de Negativa** (`CTN.206`): emitida
  quando há débito, mas ele está **suspenso** (`CTN.151` — parcelamento,
  depósito, liminar, impugnação administrativa) ou **com penhora
  garantindo** a execução. Equivale à CND para efeitos de contratação,
  crédito, licitação.
- **CP** — Certidão Positiva: indica débitos em aberto.

Certidões são instrumento de pressão: débito não garantido impede
contratar com o Poder Público (`L8666.29` e `L14133.68`), obter
financiamento público, participar de leilões de bens.

---

## 9. Parcelamentos — breve histórico

Além da transação (`LTT`), a Fazenda oferece **parcelamentos ordinários**
(`L10522.10`–`L10522.14`) e **parcelamentos especiais** (Refis),
periodicamente instituídos por lei:

- **Refis original** — Lei 9.964/2000.
- **PAES** — Lei 10.684/2003.
- **PAEX** — MP 303/2006.
- **Refis da Crise** — Lei 11.941/2009.
- **PERT** — Lei 13.496/2017.
- **Programas pós-Covid e pós-2020** — várias leis federais e
  programas PGFN específicos.

Cada Refis cria uma discontinuidade: grandes volumes de débitos
migram do estoque ativo (em cobrança/EF) para o estoque parcelado
(suspenso). **Ao usar o estoque de EFs como variável, cada Refis é
uma fonte de ruído** — processos "desaparecem" do ativo sem extinção,
e podem retornar se o parcelamento for descumprido.

Combinados com a `LTT` (vigor desde 2020), os parcelamentos
especiais tendem a perder relevância — a transação torna-se o canal
estrutural de resolução em massa.

---

## 10. Implicações para desenho empírico

- **Inscrição em dívida ativa ≠ ajuizamento em EF**. Boa parte do
  estoque de dívida ativa nunca vira EF: dispensa por valor, protesto
  sem ajuizamento, transação, prescrição no curso da cobrança
  administrativa. Para estudar "cobrança tributária", EFs captam só
  uma fatia — e uma fatia selecionada por valor, idade e capacidade
  de localizar devedor e bens.
- **Três marcos temporais** costumam ser confundidos: fato gerador,
  constituição definitiva (fim do PAF), inscrição em dívida ativa.
  A prescrição corre entre constituição e cobrança; a presunção de
  fraude nasce com a inscrição. Projetos que modelam "tempo do débito"
  devem escolher o marco coerente com a pergunta.
- **Transação (pós-2020)** introduz seleção endógena: débitos com
  característica X (tamanho, tipo, devedor) são mais prováveis de
  serem objeto de transação e saírem do estoque executado. EFs
  remanescentes representam o *hard core* mais resistente a
  negociação.
- **Heterogeneidade federativa**: PGFN é centralizada e bem
  documentada; PGEs e PGMs variam enormemente em estrutura, dados
  publicados, políticas de cobrança. Comparações entre estados ou
  entre municípios requerem caracterização caso a caso.

See also:
- `direito-tributario.md` — parte geral (obrigação, crédito,
  prescrição, responsabilidade).
- `processo-administrativo-fiscal.md` — o contencioso antes da
  inscrição.
- `execucao-fiscal.md` — a fase judicial.
- `funcoes-essenciais.md` — procuraturas da Fazenda (AGU/PGFN, PGE,
  PGM) e seu papel institucional.
