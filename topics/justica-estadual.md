# Justica Estadual

The state court system (*Justica Comum Estadual*) handles the residual
mass of civil, criminal, and family litigation not assigned to federal,
labor, military, or electoral branches. Each state organizes its own
Tribunal de Justica (TJ) and first-instance courts (*comarcas*) under
federal constitutional constraints. This file covers TJ structure,
comarca organization, and state-level variation relevant to research
design. It does not cover judicial careers (promotion, removal,
guarantees) or CNJ oversight, which have their own files.

**Topics / keywords**: Justica Estadual, Tribunal de Justica, TJ,
comarca, entrancia, vara, foro, juiz de direito, orgao especial,
corregedor, state courts, judicial districts, case assignment

**Snapshot as of 2025**: structural rules stable since CF 1988; comarca
counts and entrancia classifications change via state complementary
laws every ~5 years.

For judicial career rules (promotion, removal, guarantees), see
[carreira-juizes.md](carreira-juizes.md). For CNJ administrative
oversight, see
[cnj-administracao-judicial.md](cnj-administracao-judicial.md). For
fiscal oversight of mayors (which generates TJ improbidade caseload),
see [contas-municipais.md](contas-municipais.md). For TCE structure
and relator assignment, see
[tribunais-contas.md](tribunais-contas.md). For procurement law often
at issue in TJ improbidade cases, see
[licitacoes.md](licitacoes.md).

---

## Constitutional and statutory basis

`CF.125` assigns each state the power to organize its own judiciary.
`CF.126` authorizes TJs to create *varas especializadas* for agrarian
conflicts. `CF.96` gives TJs the initiative to propose laws
establishing or altering territorial organization (comarca creation
and extinction).

The federal framework for state courts is `LOMAN` (Lei Complementar
35/1979), Arts. 95-113 (`LOMAN.95` through `LOMAN.113`). Key
provisions:

- **Comarca creation requirements**: `LOMAN.97` sets federal minimum
  criteria (population, voters, caseload, infrastructure). States add
  further requirements via their own *Codigos de Organizacao
  Judiciaria* (COJs).
- **Corregedor**: `LOMAN.103` — function described mostly in each
  TJ's *Regimento Interno*, not in LOMAN itself.
- **Conselho da Magistratura**: `LOMAN.104` — disciplinary body
  composed of the TJ president, vice-president, corregedor, and
  additional members chosen from the *orgao especial*.
- **Juiz de direito nomination**: `LOMAN.17`.

## TJ internal structure

Each TJ has broadly the same architecture, though nomenclature and
size vary:

- **Orgao Especial**: mandatory for TJs with >25 desembargadores
  (CF Art. 93 XI). Exercises plenary functions (administrative,
  disciplinary, constitutional control). Composed of 25 members: half
  by seniority, half by election.
- **Camaras / Turmas**: panels that hear appeals, typically grouped
  into *secoes* (criminal, civil/private, public law). Each camara
  usually has 5 desembargadores; cases decided by turma of 3.
- **Grupos de Camaras**: two consecutive camaras joined for
  *embargos infringentes* or uniform-jurisprudence functions.
- **Corregedor-Geral da Justica**: supervises first-instance judges
  and court staff; conducts *correicoes* (inspections).
- **Conselho da Magistratura**: disciplinary organ (see `LOMAN.104`).

### TJSP specifics

TJSP is the largest court in Latin America. Key structural facts for
research design:

- ~360 desembargadores (largest TJ by far; second is TJMG with ~140).
- Three *secoes*: Direito Criminal, Direito Privado, Direito Publico,
  each subdivided into numbered camaras (5 desembargadores per
  camara).
- Grupos de Camaras follow ordinal sequence: two consecutive camaras
  form one grupo (Art. 36 RITJSP).
- Cases decided by turma of 3 desembargadores; embargos infringentes
  and CPC Art. 942 cases go to full 5-member camara.
- Electronic system: ESAJ (*e-SAJ*), widely used for data extraction.

## Comarca organization

A *comarca* is the territorial unit of first-instance jurisdiction.
One comarca may cover one or several municipios. Each comarca has at
least one *vara* (judgeship); larger comarcas have multiple varas,
often specialized (civil, criminal, family, fazenda publica, JECCs).

### Creation requirements

`LOMAN.97` sets the federal floor. States add criteria via their COJs.
The table below summarizes selected states to illustrate the variation
that creates research-design opportunities (population/voter
thresholds as quasi-experimental cutoffs):

| State | Law / year | Pop. min | Voters min | Caseload min | Other |
|-------|-----------|----------|------------|-------------|-------|
| SP | DLC 3/1969 | — | — | — | Index-based system: sum of coefficients from voters (1 per 100), tax revenue, caseload (2 per 10 cases). Thresholds: 1a entrancia >= 100 pts; 2a >= 300; 3a >= 600. Capital = entrancia especial. |
| MG | LC 59/2001 | 18,000 | 13,000 | 400 | Also requires state-owned forum building and staffing concurso. |
| MG | LC 38/1995 | 15,000 | 8,000 | 200 | Tax revenue >= 2x municipal-creation threshold. |
| MG | L 7655/1965 | 30,000 | — | — | Tax revenue >= 600x minimum wage; 500 houses in seat. |
| RR | 2014 law | 8,000 | 4,000 | 200 | Forum building + judge's residence required. New vara if >800 annual filings. |
| BA | 2007 law | varies by entrancia | 40% of pop. | 300 (initial) / 600 (intermediate) | Initial: pop <= 50k, area <= 200 km^2. Intermediate: pop > 50k, area > 201 km^2. Salvador = entrancia final. |

**Research-design note**: the population and voter thresholds are
sharp cutoffs that determine whether a municipality gets its own
judiciary. States revise these thresholds every ~5 years via *leis
quinquenais*. The MG series (1954-2001) shows thresholds falling over
time (30k -> 18k pop.), creating staggered adoption useful for
difference-in-differences or RD designs. SP's index-based system is
more complex but offers continuous variation.

### Installation requirements

Beyond the numerical thresholds, states require physical
infrastructure before a created comarca can be *installed*: a forum
building, public jail, police quarters, and (historically) a judge's
residence. These installation requirements create a second hurdle
that delays actual judicial presence after legal creation.

### Comarca extinction

`LOMAN.97` and state COJs require extinction when a comarca's
indicators fall below minimums — typically enforced in the quinquennial
review. In practice, extinctions are rare and politically costly.

## Entrancia system

Comarcas are classified into *entrancias* (tiers) that determine
judicial career progression. The number of tiers and classification
criteria vary by state:

- **SP**: 4 tiers (1a, 2a, 3a entrancia + entrancia especial for the
  Capital). Classification based on composite index (voters + tax
  revenue + caseload).
- **BA**: 3 tiers (initial, intermediate, final). Salvador is
  entrancia final by statute.
- **MG, most states**: 3 tiers (1a, 2a, 3a entrancia or
  inicial/intermediaria/final). Capital usually tops the hierarchy.

Entrancia determines which judges serve where and constrains
*promocao* (advancement) paths. For the full career-progression
mechanics (merecimento vs. antiguidade, quinto constitucional), see
[carreira-juizes.md](carreira-juizes.md).

## Foros and varas within a comarca

Larger comarcas subdivide into multiple *foros* (courthouse locations)
and *varas* (judgeships). Patterns relevant to case-assignment
research:

- **Single-foro comarcas**: most interior comarcas. One judge handles
  all matters (*vara unica*) or a small number of varas split
  civil/criminal.
- **Multi-foro comarcas**: large capitals split foros by geography
  (SP, Manaus) or by *materia* (Brasilia — different courthouse
  buildings for criminal, civil, family, fazenda publica, etc.).
- **Vara specialization**: large comarcas have specialized varas
  (family, fazenda publica, registros publicos, JECCs). Smaller
  comarcas bundle everything into one or two varas.

### Case assignment and randomization

Case assignment within a comarca uses the last digits of the NPU
(*Numero do Processo Unico*) to route cases to varas. Key caveats
for researchers using case-level data:

- **Multi-foro assignment**: in some cities (e.g., Teresina JECCs),
  physically separate foros share the same last-four-digit NPU
  routing, making geographic assignment look random when it may not
  be.
- **Vara-creation timing**: new varas absorb redistributed cases,
  creating non-random cohort effects at the transition boundary.
- **Specialization changes**: when a generalist vara is converted to
  a specialized vara, the case composition shifts discontinuously.

## Historical notes

Comarca creation in Brazil dates to the colonial period. Selected
benchmarks:

- **1832**: Codigo de Processo Criminal established the first
  systematic comarca division. SP had 6 comarcas.
- **1940**: SP had 126 comarcas.
- **Post-1988**: CF gave TJs initiative over comarca creation, leading
  to expansion waves in the 1990s-2000s as states lowered population
  thresholds.

The MG series of COJs (1954, 1959, 1965, 1979, 1995, 2001) provides
one of the longest continuous records of comarca-creation threshold
changes, useful for studying the expansion of judicial access.

### Cross-state comarca counts (current snapshot)

Source: `diarios` module comarca index (assembled from TJ websites
and COJs). DF not included (Justiça do DF is organized federally).

| State | Comarcas | State | Comarcas | State | Comarcas |
|-------|---------|-------|---------|-------|---------|
| SP | 315 | PE | 151 | MA | 103 |
| MG | 293 | PR | 146 | PI | 79 |
| BA | 275 | GO | 121 | MT | 78 |
| RS | 164 | CE | 111 | SE, PB | 75 |
| — | — | SC | 108 | ES | 68 |
| — | — | PA | 107 | RJ | 67 |

Smaller states: AM 60, AL 59, RN 53, MS 53, TO 41, RO 22, AC 22,
AP 12, RR 8. **Total: 2,666 comarcas across 26 states.**

### TJSP comarca count over time

Source: `justica` pipeline, assembled from ALESP legislative archive
(public decrees of comarca creation/installation). Coverage: 352
comarcas with creation dates from 1700 to 2016.

| Year | Cumulative comarcas | Notes |
|------|-------------------|-------|
| 1832 | 3 | Codigo de Processo Criminal |
| 1900 | 31 | |
| 1940 | 132 | |
| 1960 | 145 | |
| 1980 | 146 | Near-stagnation under military rule |
| 2000 | 230 | Post-CF 1988 expansion wave |
| 2010 | 342 | |
| 2016 | 352 | Last creation in dataset |

The 1988–2010 expansion (146 → 342) coincides with CF giving TJs
initiative over comarca creation (`CF.96`) and successive revisions
lowering population thresholds in SP's COJ.
