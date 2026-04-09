# Licitações — public procurement

Brazilian public procurement law, procurement-related corruption, and
bid-rigging typology. Focus on statutes governing municipal and federal
procurement and the CADE framework for cartel enforcement in auctions.

**Topics / keywords**: public procurement, bid rigging, cartel, pregão,
reverse auction, Lei 8.666, Lei 14.133, CADE, dispensa, inexigibilidade,
bid rotation, cover bidding, cartel typology, procurement fraud,
improbidade, compras governamentais.

**Snapshot as of 2026**: statutory numbers are static, but monetary
thresholds under Lei 14.133 are updated annually via Decree — verify
current values before using specific R$ figures for post-2023 work.

Sourced in part from `projects/procure/docs/institutions.md`.

---

## Lei 8.666/1993 — Lei Geral de Licitações

Governed virtually all Brazilian public procurement for nearly three decades.
Still the relevant statute for historical (pre-2021) analysis.

### Modalities (Art. 22)

Five modalities, each defined by value thresholds and procedural requirements:

- **Convite** (Art. 23, I a / II a): engineering up to R$150,000; goods/services
  up to R$80,000. Minimum 3 invited firms (Art. 22 §3).
- **Tomada de preços** (Art. 23, I b / II b): engineering up to R$1,500,000;
  goods/services up to R$650,000. Requires prior cadastro.
- **Concorrência**: above tomada de preços thresholds; open to all.
- **Concurso**: for technical/artistic/scientific work.
- **Leilão**: for sale of public goods.

Thresholds updated by Decreto 9.412/2018.

**Sources:** [Lei 8.666/1993 Art. 22–23](https://www.planalto.gov.br/ccivil_03/leis/l8666cons.htm); Decreto 9.412/2018.

### Award criteria (Art. 45)

- **Menor preço** (lowest price) — default.
- Melhor técnica; técnica e preço; maior lance (for leilões).

### Publication requirements (Art. 21)

Diário Oficial, newspapers; varies by modality and value. Creates the paper
trail exploited in Audesp / TCE-SP datasets.

### Contract amendments (Art. 65)

Permitted up to **25% of original value** (50% for construction renovations,
Art. 65 §1). Frequent vehicle for ex-post price adjustments.

### Dispensa de licitação (Art. 24)

Enumerated exceptions where competitive bidding is not required:

- Art. 24, I: works/engineering below R$15,000 (original threshold).
- Art. 24, II: purchases/services below R$8,000 (original threshold).
- Art. 24, IV: emergency situations.
- Art. 24, V: no bidders appeared (*deserto*).

Dispensations and inexigibilidade are frequently cited in improbidade cases
as mechanisms for directing contracts without competition.

### Inexigibilidade (Art. 25)

When competition is objectively infeasible: sole source, artistic services,
specialized professionals.

### Anti-fracionamento rule (Art. 23 §5)

Prohibits splitting works or services of the same nature that could be
performed simultaneously or successively to circumvent modality thresholds.
Lei 14.133/2021 Art. 75 §1 strengthens this by requiring agencies to sum
all expenditures for objects of the same nature within a fiscal year.

### Criminal provisions (Arts. 89–98)

Crimes specific to procurement: fraud in bidding (Art. 90), unlawful
dispensation (Art. 89), obstruction of competition (Art. 95).

---

## Lei 10.520/2002 — Pregão

- Introduced the **pregão** modality: an open descending-price reverse auction.
- Initially for goods and standard services; expanded in practice.
- **Pregão eletrônico** mandatory for the federal government from Decreto
  10.024/2019; widely adopted by municipalities.
- Most common modality in municipal procurement during the 8.666 era.

**Source:** [Lei 10.520/2002](https://www.planalto.gov.br/ccivil_03/leis/2002/l10520.htm); Decreto 10.024/2019.

---

## Lei 14.133/2021 — Nova Lei de Licitações

- Replaces Lei 8.666/1993, Lei 10.520/2002, and the RDC (Lei 12.462/2011).
- **Transition period:** municipalities could choose old or new regime until
  December 30, 2023 (Art. 191). After that date, Lei 14.133 is mandatory.
- New modality: **diálogo competitivo** added.
- **Dispensa thresholds (Art. 75):** works/engineering up to R$100,000 (I);
  goods/other services up to R$50,000 (II). Values updated annually via
  Decree. Significantly higher than Lei 8.666 thresholds.
- Strengthened integrity requirements: compliance programs, risk matrices.

**Source:** [Lei 14.133/2021](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm).

---

## CADE and cartel enforcement in procurement

### Lei 12.529/2011 — Competition law

- Established **CADE** (Conselho Administrativo de Defesa Econômica) as an
  autarquia with adjudicatory powers.
- **Cartel prohibition** (Art. 36 §3, I): agreements between competitors to
  fix prices, divide markets, or rig bids are administrative infractions.
- **Sanctions** (Art. 37): fines of 0.1% to 20% of gross revenue.
- **Leniency program** (Arts. 86–87): first confessor receives full or
  partial immunity; key source of information on cartel mechanics.

**Source:** [Lei 12.529/2011](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12529.htm).

### CADE typology of collusive strategies

From the CADE *Guia de Combate a Cartéis em Licitação* (December 2019, 58 pp),
Part II, Section II.3:

- **Cover bidding** (*propostas fictícias ou de cobertura*): competitors
  submit deliberately high bids to make the designated winner's bid appear
  competitive. Most common form of collusion in procurement.
- **Bid suppression / withdrawal** (*supressão/retirada de propostas*):
  firms refrain from bidding or withdraw bids to ensure the designated
  winner prevails.
- **Blocking in pregão presencial** (*bloqueio em pregão presencial*):
  cartel members submit bids within the 10% threshold of the lowest bid to
  block non-aligned firms from the verbal bidding phase. Does not apply to
  pregão eletrônico (footnote 36, p. 39).
- **Bid rotation** (*propostas rotativas / rodízio*): firms take turns
  winning across auctions or lots — by equal number of lots, market share,
  or production capacity.
- **Market division** (*divisão de mercado*): geographic or client-based
  allocation among cartel members. Often combined with cover bidding or
  bid suppression.
- **Other**: abuse of consórcios (Art. 33, Lei 8.666) and subcontracting
  to implement agreements and split cartel profits.

### Red flags for collusion

CADE guide Section II.4 (pp. 47–49) lists indicators at four stages:

- (I) **Bid submission**: few bids, unexplained withdrawals, bids with
  identical errors or formatting.
- (II) **Bidder declarations**: references to "industry prices".
- (III) **Bidder behavior**: winners subcontracting losers, periodic wins of
  similar quantities.
- (IV) **Outcomes**: rotation patterns, geographic concentration, disparate
  prices for similar objects.

### Intersection of cartel, fraud, and corruption

CADE guide Part IV (pp. 52–58):

- **Cartel** (agreement between competitors) and **fraud** (fake firms
  pretending to compete) are legally distinct but often coincide (p. 54).
- **Corruption** (public officials involved) and cartel can coexist and
  reinforce each other: officials may direct specifications or leak
  information to facilitate the cartel (p. 55).
- The same conduct can be prosecuted in parallel:
  - Administrative infraction by CADE (Lei 12.529/2011 Art. 36).
  - Criminal offense under Lei 8.137/1990 Art. 4 and Lei 8.666/1993 Art. 90.
  - Improbidade administrativa by MP (Lei 8.429/1992).
  - Corporate liability under Lei Anticorrupção 12.846/2013 Art. 5.
- Summary table on p. 58 maps sanctions, agreement types, and competent
  authorities across CADE, CGU, and MP/Police.

### Procurement as share of GDP

- OECD member countries: ~15% of GDP (CADE guide p. 12, citing OECD 2009).
- Brazil federal government (2018): 100,000+ procurement processes totaling
  ~R$48 billion (CADE guide p. 12, citing Painel de Compras).
- Cartel overpricing estimate: 10–20% (conservative; CADE guide p. 14; OECD).

### Notable CADE cases (from guide)

- **Cartel de Portas de Segurança Giratórias** (PA 08012.009611/2008-51):
  bid rotation + cover bidding, ~25% overpricing, 4 firms + 10 individuals
  convicted (2014). (p. 41)
- **Cartel em Licitação para Aquisição de Tintas** (PA 08012.006199/2009-07):
  blocking in pregão presencial, Prefeitura de Lages/SC, 3 firms convicted
  (2014). (p. 40)
- **Cartel do Transporte Aéreo Postal** (PA 08012.010362/2007-66):
  subcontracting to implement market division, ECT procurement, all
  investigated convicted (2014). (p. 46)

**Source:** CADE, *Guia de Combate a Cartéis em Licitação*, December 2019.

---

## Related statutes (cross-reference)

- **Lei 8.429/1992** — improbidade administrativa (civil corruption
  prosecution; see `contas-municipais.md` §3 for the Ficha Limpa interaction).
- **Lei 8.137/1990** — crimes contra a ordem econômica (Art. 4 criminalizes
  cartel conduct).
- **Lei 12.846/2013** — Lei Anticorrupção (corporate liability).
- **Lei 14.230/2021** — reform of improbidade (eliminated culposa conduct;
  STF Tema 1199 on retroactive application).
