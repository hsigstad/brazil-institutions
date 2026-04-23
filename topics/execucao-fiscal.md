# Execução fiscal

Cobrança **judicial** do crédito tributário (e da dívida ativa não
tributária) — a fase em que a CDA vira processo. Governada pela
`LEF` (Lei 6.830/1980), com CPC subsidiário (`LEF.1`). Escopo: rito,
competência, penhora, defesa do executado, prescrição intercorrente,
medida cautelar fiscal, e implicações do volume — EFs dominam o
estoque processual no Brasil.

Para o crédito antes de virar EF (inscrição, CDA, protesto,
transação), ver `divida-ativa.md`. Para a parte geral (prescrição,
redirecionamento, responsabilidade tributária), ver
`direito-tributario.md`. Para o contencioso administrativo, ver
`processo-administrativo-fiscal.md`.

**Topics / keywords**: execução fiscal, LEF, Lei 6.830, CDA, embargos
à execução, exceção de pré-executividade, prescrição intercorrente,
redirecionamento, penhora, Sisbajud, Bacenjud, indisponibilidade,
medida cautelar fiscal, LCF, Tema 566, tax debt enforcement, tax
foreclosure, garantia do juízo, executive tax proceedings.

**Snapshot as of 2026**: `LEF` estrutura processual estável desde 1980
(reformas pontuais em 2014 — `L13043` — e 2018 — `L13606`). O ponto de
inflexão na última década foi jurisprudencial: o STJ fixou em 2018 a
tese operacional de prescrição intercorrente (`Tema566`, REsp
1.340.553), e o `LC118` (2005) antecipou marcos de prescrição e
presunção de fraude. O volume segue sendo o problema estrutural — EFs
são >50% do estoque da JF e >35% da JE (Justiça em Números 2024).

---

## 1. Onde a EF se encaixa

- **Título executivo**: CDA inscrita em dívida ativa (`LEF.2`–`LEF.3`,
  `CTN.201`–`CTN.204`), com presunção de liquidez e certeza.
- **Autor**: a Fazenda Pública — União via PGFN, estados via PGE,
  municípios via PGM, autarquias federais via PGF, conselhos de
  classe em parte dos casos.
- **Réu**: contribuinte originariamente inscrito; no curso, pode ser
  redirecionado a sócio-gerente ou sucessor.
- **Natureza**: processo de execução baseado em título extrajudicial
  (`CPC.784.IX`), com rito específico da `LEF`.

O ajuizamento **interrompe a prescrição** (regra do `CTN.174.I` após
`LC118` — é o despacho que ordena a citação que interrompe, mas o
efeito retroage à data de propositura quando a citação ocorre em
tempo razoável: STJ Súmula 106).

---

## 2. Competência — quem julga

- **Justiça Federal** (`CF.109.I`): tributos da União (IR, IPI,
  PIS/COFINS, CSLL, ITR), contribuições previdenciárias (transferidas
  à PGFN via `L11457.16`, em vigor desde 2007), FGTS, multas
  administrativas de autarquias e agências federais.
- **Justiça Estadual** (Vara da Fazenda Pública nos TJs maiores; Vara
  Cível ou comum nos demais): tributos estaduais (ICMS, IPVA, ITCMD) e
  **municipais** (IPTU, ISS, ITBI). Não há "justiça municipal"
  autônoma — as EFs de municípios tramitam na JE.
- **Justiça do Trabalho** (`CLT.876.§unico`): execução **de ofício** de
  contribuições previdenciárias sobre parcelas de sentenças
  trabalhistas (exceção ao fluxo normal, cuja execução pertence
  à PGFN na JF).

A transição de 2007 é relevante: antes do `L11457`, execuções fiscais
previdenciárias tramitavam em varas especializadas da Justiça
Estadual (Juizados Especiais Previdenciários) ou em varas previdenciárias.
Pós-reforma, foram todas absorvidas pela JF — parte do crescimento do
estoque da JF nos anos 2010 reflete essa migração, não só ajuizamentos
novos.

### Organização interna — varas especializadas em EF

Dentro de cada competência, a **especialização dos juízos** por matéria
varia por tribunal, porte da comarca/subseção, e volume. Três modelos
coexistem:

1. **Vara especializada em execução fiscal**. Usada em comarcas/subseções
   de grande volume. Exemplos:
   - **TJSP, comarca da Capital**: tem **Vara das Execuções Fiscais
     Estaduais** (ICMS, IPVA, ITCMD, multas estaduais) e **Vara das
     Execuções Fiscais Municipais** (IPTU, ISS, ITBI, taxas
     municipais). Esta última foi instalada em 10/11/2008 com
     aproximadamente 2 milhões de processos em tramitação — 95% IPTU.
     É um dos maiores juízos especializados do país em volume.
   - **Justiça Federal, 1ª Subseção SP**: várias varas especializadas
     em execução fiscal federal (10ª VEF, etc.); competência expandida
     em dezembro/2024 para absorver municípios de outras subseções
     (Sorocaba, Jundiaí, Osasco, Mauá, Barueri).
2. **Vara especializada em Fazenda Pública** (matéria fazendária geral,
   não apenas EF). Processa ações de improbidade, reintegração de posse,
   danos morais contra o poder público, concursos públicos, e **EFs
   também**. Modelo dominante em capitais de porte médio. Exemplos: TJMG
   (Varas da Fazenda Pública e Autarquias, com rotinas padronizadas
   desde 2013); TJRJ (Varas de Fazenda Pública).
3. **Vara cível comum**. Em comarcas menores sem especialização, a
   Fazenda Pública (incluindo EFs) tramita na vara cível única (ou
   juízo único) ao lado de qualquer outra matéria. É a regra geral fora
   das capitais e cidades grandes.

Pontos relevantes para desenho empírico:

- **Grau de especialização é heterogêneo intra-estado** — SP Capital
  tem duas varas exclusivas de EF; Santos tem vara fazendária geral;
  comarca pequena do interior tem juízo único. Comparações cross-vara
  dentro de um mesmo TJ misturam **três modelos organizacionais
  distintos**, não apenas variação de juiz.
- **Vara especializada ≠ maior velocidade**. As varas especializadas
  em EF (notadamente SP Capital) têm **estoques gigantes** acumulados;
  a especialização é consequência do volume, não solução para ele. Não
  é seguro assumir que "vara especializada" é proxy de throughput ou
  qualidade.
- **Redistribuição de competência** acontece por resoluções do TJ/TRF
  (em 2024 a 1ª Subseção SP redistribuiu competência para absorver
  outras subseções). Para séries temporais, atentar a resoluções que
  mudam o arranjo — afetam composição de casos por vara sem
  corresponder a mudanças substantivas.
- **Juizados Especiais da Fazenda Pública** (Lei 12.153/2009) têm
  competência para causas até 60 salários-mínimos em matéria
  fazendária estadual/municipal, mas **execução fiscal é explicitamente
  excluída** do JEFP (`L12153.2.§1.I`). EFs sempre tramitam na vara
  comum (ou especializada em EF), nunca em juizado especial.

**PROJECT-SPECIFIC — needs manual curation when used in study**:
mapear o arranjo de especialização na amostra (quais comarcas têm
vara exclusiva de EF vs. vara fazendária geral vs. vara cível) é
pré-requisito para qualquer análise cross-vara de outcomes de EF. A
informação vive em resoluções dos TJs/TRFs e em diretórios de varas
nos portais dos tribunais; não há mapa consolidado público.

---

## 3. Rito da LEF

### Petição inicial e citação

- **Inicial simplificada** (`LEF.6`): pode ser feita em termo, com
  CDA juntada. Distribuída ao juízo competente.
- **Despacho que ordena a citação** (`LEF.7`): interrompe a
  prescrição nos termos do `CTN.174.§unico.I` (após `LC118`).
- **Citação** — prazo e forma (`LEF.8`):
  - Primeiramente por **Correios** com AR. Se frustrada, oficial.
  - Se endereço desconhecido ou devedor não localizado, **citação por
    edital** (STJ Súmula 414: permitida após esgotamento das demais
    modalidades).
  - Executado tem **5 dias** para pagar ou **garantir a execução**.

### Garantia do juízo

Modalidades (`LEF.9`):
- Depósito em dinheiro.
- Fiança bancária ou seguro-garantia — equiparados ao dinheiro para
  fins de ordem de penhora por `CPC.835.§2` (desde que o valor supere
  em 30% o débito).
- Nomeação de bens à penhora.

A garantia do juízo é **pressuposto dos embargos à execução** (`LEF.16`).
Sem garantia, o executado só pode apresentar **exceção de
pré-executividade**.

### Penhora e avaliação

Ordem preferencial (`LEF.11`):

1. Dinheiro (inclusive via Sisbajud/Bacenjud).
2. Títulos da dívida pública.
3. Pedras e metais preciosos.
4. Imóveis.
5. Navios e aeronaves.
6. Veículos.
7. Móveis.
8. Direitos e ações.

**Sisbajud** (sucessor do Bacenjud) é o instrumento mais usado — permite
bloqueio online de contas bancárias e de investimentos vinculados ao
CPF/CNPJ executado em todas as instituições financeiras. Combina com
`CTN.185-A` (indisponibilidade judicial de bens) quando citado não
paga nem indica bens.

### Sistemas eletrônicos de descoberta e constrição — rollout e timeline

Ao longo de 2001–2022 o Judiciário construiu uma pilha progressivamente
mais densa de sistemas eletrônicos para localizar e constringir ativos
do executado. Para pesquisa empírica, **o rollout destes sistemas é
uma das principais fontes de variação temporal (e, para alguns, de
variação entre tribunais) na tecnologia de cobrança** — independente
de reformas legais. Timeline:

- **Bacenjud 1.0 — 2001**. Sistema inicial de convênio do BCB com o
  STJ/CJF, voltado à transmissão eletrônica de ordens de bloqueio para
  instituições financeiras. Operação manual; adesão gradual entre
  tribunais; inicialmente concentrada na Justiça do Trabalho.
- **Bacenjud 2.0 — 2005**. Convênio BCB–STJ–CJF reformula o sistema
  com cobertura bancária mais ampla e interface aperfeiçoada. Base
  legal processual posteriormente consolidada em `CPC.854` (CPC 2015).
  Usa-se também para `CTN.185-A` (indisponibilidade judicial de bens e
  direitos) quando o devedor citado não paga nem indica bens.
- **Renajud — 2006–2008**. Convênio CNJ / Secretaria de Reforma do
  Judiciário / Denatran celebrado em 2006; projeto piloto no TRT-10
  em maio de 2008; lançamento formal em 28/08/2008. Desenvolvido pelo
  Serpro. Permite consulta e gravação de restrições (bloqueio de
  transferência, penhora) sobre veículos registrados no Renavam, em
  tempo real.
- **Infojud — 2007–2010**. Convênio CNJ–RFB para acesso do Judiciário
  a dados da Receita Federal (DIRPF, DIRF, DITR, cadastros) via
  certificação digital. Adoção progressiva ao longo do final dos anos
  2000; coberta por Termo de Adesão ao Convênio assinado por cada
  tribunal.
- **Sisbajud — agosto/setembro 2020**. Substituto do Bacenjud,
  resultante de **Acordo de Cooperação Técnica CNJ–BCB–PGFN de
  dezembro de 2019**. Lançado em 25/08/2020; migração concluída em
  08/09/2020 (Bacenjud desligado em 04/09/2020). Inovações principais:
  (i) **"teimosinha"** — reiteração automática das ordens de bloqueio
  (o sistema recalcula e reenvia ordens residuais até a satisfação do
  valor); (ii) requisição de extratos bancários detalhados no formato
  SIMBA/MPF; (iii) cópias de contratos de abertura de conta, extratos
  de cartão, contratos de câmbio, cheques, extratos PIS/FGTS; (iv)
  integração direta com a PGFN. A inclusão da PGFN no acordo reflete
  o interesse da Fazenda Federal em usar o sistema para créditos em
  EF de grande volume.
- **Sniper — agosto/2022**. Sistema Nacional de Investigação
  Patrimonial e Recuperação de Ativos, lançado pelo CNJ em 16/08/2022
  no âmbito do **Programa Justiça 4.0** (CNJ–PNUD, desde 2020).
  Agrega e cruza bases de dados (Sisbajud, Infojud, Renajud, Juntas
  Comerciais, Receita Federal, Serasajud) para **identificar vínculos
  patrimoniais, societários e financeiros** entre PFs e PJs em
  segundos — usado sobretudo para mapear redes de grupo econômico e
  para redirecionamento. Menos uma ferramenta de bloqueio e mais uma
  de investigação cruzada. Nova versão do Sniper com funcionalidades
  de constrição lançada em 23/09/2025.
- **Serasajud** — sistema que integra base da Serasa Experian ao
  Judiciário; permite consulta a dívidas de PFs/PJs e negativação
  (quando cabível) em tempo real. Coexiste com os anteriores.

**Base legal principal**: `CPC.854` (penhora de dinheiro em depósito ou
aplicação financeira por sistema eletrônico da autoridade supervisora
do SFN); `CTN.185-A` (indisponibilidade judicial de bens e direitos).
A obrigatoriedade do uso foi ampliada pela Resolução CNJ que tornou
obrigatório o uso dos sistemas eletrônicos para bloqueio patrimonial
antes de diligências físicas de menor eficácia.

**Implicações empíricas do rollout**:

- **Variação temporal exógena na tecnologia de cobrança** entre 2001 e
  2022. Para projetos que medem efetividade da EF sobre horizonte
  longo, o rollout destes sistemas é uma das fontes de mudança na
  probabilidade de localização de ativos — separadamente de reformas
  legais como `LC118` (2005), `Tema566` (2018), ou Lei 13.988 (2020).
- **Adoção não-uniforme entre tribunais** na fase inicial de cada
  sistema (Bacenjud 1.0, Renajud pré-2010, Infojud pré-2012). A
  interação rollout × tribunal gera potencial para *event-study* com
  corte por TJ/TRT/TRF, embora dados precisos de adoção por vara não
  sejam públicos.
- **Sisbajud "teimosinha" como quebra pós-2020**: a reiteração
  automática de ordens altera a distribuição de valores efetivamente
  bloqueados vis-à-vis Bacenjud (onde a reiteração exigia novo
  despacho). Em séries de outcome (valor recuperado / tempo até
  constrição), 2020–2021 é quebra estrutural.
- **Sniper e redirecionamento**: para desenhos que estudam phoenix
  firms, a chegada do Sniper (2022) muda a capacidade do sistema de
  mapear grupos econômicos e redes societárias em segundos — afeta a
  probabilidade observada de redirecionamento após 2022, e pode
  alterar o perfil dos sócios alcançados (ver `Tema981`,
  `direito-tributario.md` §3).
- **Dados quantitativos do CNJ** sobre taxas de bloqueio (valor
  bloqueado / valor solicitado) existem para alguns cortes (ex.:
  relatório "Um ano de Sisbajud", 2021), mas não são
  sistematicamente publicados por tribunal/vara. **NEEDS PRIMARY
  SOURCE**: confirmar séries de hit-rate ao usar quantitativamente.

---

## 4. Defesa do executado

### Embargos à execução (`LEF.16`)

- Prazo: **30 dias** da intimação da penhora ou garantia.
- **Requer garantia do juízo** (a garantia pode ser insuficiente, mas
  deve existir).
- Matéria: qualquer questão de fato ou direito, inclusive nulidade
  da CDA, pagamento, compensação, prescrição.
- **Não suspendem automaticamente** a execução (após reforma do CPC
  2015). A atribuição de efeito suspensivo depende de decisão
  judicial, com requisitos de relevância da fundamentação e risco
  de dano (análogos aos da tutela provisória).

### Exceção de pré-executividade

Não prevista na `LEF`, construída pela jurisprudência (Pontes de
Miranda → Galeno Lacerda → STJ).

- **Sem garantia do juízo**.
- Prazo: qualquer momento do processo.
- **Matéria restrita** (STJ Súmula 393): matérias de **ordem pública**
  (ex.: prescrição, decadência, ilegitimidade, nulidade da CDA) e que
  **dispensem dilação probatória** (prova pré-constituída).

Em execução fiscal, é o principal instrumento defensivo do executado
sem patrimônio (ou sem vontade de oferecer garantia). Na prática, a
maior parte é rejeitada por extrapolar a matéria admitida, mas a
alegação de prescrição intercorrente cabe.

---

## 5. Prescrição intercorrente — `Tema566`

**O problema**: EF aberta, devedor não localizado, bens não
encontrados. O processo fica em arquivamento indefinido. O STJ fixou
o rito operacional em **REsp 1.340.553** (`Tema566`, 2018):

1. Não-localização do devedor ou de bens → juiz **suspende** a
   execução por **1 ano** (`LEF.40`).
2. Findo o ano sem manifestação útil → **arquivamento sem baixa**.
3. Do arquivamento começa a contagem da **prescrição intercorrente
   de 5 anos** (`CTN.174` + `LEF.40.§4`).
4. Decorridos 5 anos sem movimentação que represente diligência útil
   do credor → juiz reconhece a prescrição **de ofício**, após
   intimar a Fazenda.
5. Diligências **meramente protelatórias** (petições genéricas, pedidos
   de vista) **não interrompem** nem suspendem.

Antes do `Tema566`, era comum que EFs ficassem "vivas" por décadas
sob diligências formais da Fazenda. A tese fixada destrava o
reconhecimento massivo de prescrição intercorrente — efeito esperado:
reduz o estoque historicamente empilhado.

---

## 6. Medida cautelar fiscal (`LCF`)

Instrumento de tutela **preventiva** à cobrança, pré- ou paralela à EF.

- **Cabimento** (`LCF.1`): antes ou durante a EF, quando há crédito
  constituído.
- **Hipóteses** (`LCF.2`): devedor não tem domicílio certo, aliena ou
  tenta alienar bens, põe-se em estado de insolvência, etc.
- **Efeito** (`LCF.4`): **indisponibilidade de bens** até o limite da
  dívida.
- **Liminar** (`LCF.7`): concedida sem ouvir o devedor.
- **Caducidade** (`LCF.15`): se a EF não for ajuizada em 60 dias da
  concessão da medida.

Na prática, usada seletivamente para grandes devedores em manobras de
ocultação patrimonial. Volume baixo comparado à EF ordinária, mas
valor agregado relevante — especialmente em casos de fraude fiscal ou
dissolução irregular iminente.

---

## 7. Recursos e recursos especiais

O sistema recursal em EF é o do CPC (aplicação subsidiária via
`LEF.1`), com adaptações:

- **Agravo de instrumento** (`CPC.1015`): contra decisões
  interlocutórias arroladas na lei — em EF, inclui decisões sobre
  penhora, impugnação de avaliação, arrematação.
- **Apelação**: contra sentença (p. ex., julgamento de embargos,
  extinção da EF por pagamento ou prescrição).
- **Recurso especial e recurso extraordinário**: contra acórdãos do
  TRF ou TJ, em matéria de lei federal (REsp) ou constitucional (RE).
  EF gera volume desproporcional de REsp em matéria tributária — o
  STJ tem diversas teses repetitivas fixadas em temas de EF (ver
  `Tema566`, Súmulas 393, 414, 435, 436, 437).

---

## 8. EF no estoque do Judiciário — o problema estrutural

Dados do CNJ (Justiça em Números, série histórica até 2024):

- EF compõe **~52% do estoque** da Justiça Federal e **~36% do
  estoque** da Justiça Estadual.
- **Taxa de congestionamento** em EFs fica historicamente **>90%**
  (de 100 processos em andamento, <10 saem por ano).
- **Tempo médio** de EF: >8 anos na JE; 5–6 anos na JF.
- Taxa de recuperação efetiva (valor cobrado / valor ajuizado):
  extremamente baixa, na casa de poucos pontos percentuais
  dependendo da fonte e do ano.

Principais causas estruturais:
- Baixa probabilidade de localização de bens do devedor (especialmente
  em créditos pequenos contra PJs inativas).
- Revelia elevadíssima (STJ Súmula 414 autoriza citação por edital,
  mas capacidade real de defesa é mínima).
- Redirecionamento contra sócios é lento e burocrático.
- Falta de incentivo para extinguir EFs "mortas" — reconhecimento de
  prescrição intercorrente antes do `Tema566` era demorado.

Há políticas explícitas para reduzir o estoque: desjudicialização
(protesto, transação), dispensa de ajuizamento por valor, Meta 7 do
CNJ (priorização de baixa de EFs antigas), e iniciativas de
conciliação (Semana Nacional da Execução Fiscal).

---

## 9. Jurisprudência operacional

- **`Tema566`** (STJ, REsp 1.340.553) — prescrição intercorrente:
  ritmo operacional da `LEF.40` (acima).
- **STJ Súmula 106** — proposta a ação no prazo, demora de citação
  imputável ao Judiciário não prejudica a prescrição.
- **STJ Súmula 392** — admite substituição de CDA até a sentença para
  correção de erro material/formal; vedada modificação do sujeito
  passivo.
- **STJ Súmula 393** — matéria da exceção de pré-executividade.
- **STJ Súmula 414** — citação por edital em EF.
- **STJ Súmula 430 e 435** — redirecionamento ao sócio-gerente (ver
  `direito-tributario.md` §3).
- **`Tema444` / `Tema962` / `Tema981`** — cluster operacional do
  redirecionamento: termo inicial da prescrição (444), exclusão do
  sócio retirado regularmente antes da dissolução (962), inclusão do
  administrador à época da dissolução ainda que não fosse gerente no
  fato gerador (981). Detalhe em `direito-tributario.md` §3.
- **STJ Súmula 436** — entrega de declaração pelo contribuinte
  reconhece débito e dispensa procedimento administrativo para cobrar
  o saldo declarado não pago.
- **STJ Súmula 555** — decadência em lançamento por homologação sem
  pagamento antecipado segue `CTN.173.I`, não `CTN.150.§4`.

---

## 10. Implicações para desenho empírico

- **Ponto amostral** da EF: cuidado com seleção múltipla prévia —
  apenas créditos que (a) não foram extintos no PAF, (b) não foram
  dispensados por valor, (c) não foram pagos ou parcelados, (d) não
  foram objeto de transação, chegam ao ajuizamento.
- **Duração altamente censurada**: muitas EFs vivem o tempo máximo
  amostral sem desfecho. Análise de tempo-até-extinção requer modelos
  de sobrevivência, não OLS em duração.
- **Taxa de recuperação vs valor ajuizado**: valor bruto ajuizado é má
  proxy para recuperação — desconto implícito nos juros, multas,
  prescrições. Para efeito fiscal real, usar valor liquidado.
- **Reforma pós-`Tema566`**: em dados de EF pós-2018, há aumento
  observado na extinção por prescrição intercorrente, com efeito sobre
  duração média e estoque. Tratar como *structural break*.
- **Heterogeneidade de competência**: EFs estaduais/municipais
  (JE) têm rito, tempo, taxa de recuperação e perfil de devedor
  muito distintos das federais (JF). Não combinar sem cautela.
- **Reforma tributária (`EC132-2023`)**: não altera o rito da EF, mas
  vai mudar o mix de créditos — a partir de 2027–2033, IBS/CBS vão
  progressivamente substituir ICMS/ISS/PIS/COFINS como base do estoque.

See also:
- `divida-ativa.md` — a fase pré-judicial.
- `direito-tributario.md` — parte geral (prescrição, redirecionamento,
  responsabilidade).
- `processo-administrativo-fiscal.md` — a fase administrativa que
  precede a EF.
- `processo-civil.md` — CPC subsidiário (recursos, penhora,
  arrematação).
- `justica-federal.md` / `justica-estadual.md` — estrutura das varas
  competentes.
- `funcoes-essenciais.md` — procuraturas da Fazenda.
