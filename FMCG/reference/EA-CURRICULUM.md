# Enterprise Applications & Information Systems (EA) — Curriculum (v1.0, 2026-10-26)
Teacher: Bilge · Student: Serkan Ok · Standard: /home/box/teaching-standard/lesson-notes-standard.md
Language: English, academic register (Turkish terms where the Turkish system is the object: e-fatura, SGK, KVKK). One lesson per sitting; read-gated: the next EA lesson is sent only after "EA okudum" (or a plain "okudum" when EA was the last stream sent).

**Total: 195 lessons** in 14 parts and 41 units. Tag balance: **BIZ 51 · TECH 52 · BOTH 92**. Counted by script (`grep -c '^| EA-'`; tags by `grep -c '^| EA-[0-9.]* | BIZ '` etc.) on 2026-10-26.

**Scope and seams.** A separate stream from FMCG (commercial theory) and ECO (economics, finance, accounting). EA teaches *systems*: the business domain each application family serves, its data model, process flows, architecture, vendor landscape and Turkish context, plus the IS theory and software/data/integration engineering underneath. It never re-teaches FMCG or ECO content; it cites it by ID (e.g. double-entry is ECO-33.2, the accounting engine that enforces it is EA-22.1; sales-force sizing is FMCG-8.4, the SFA system that supports it is EA-26.x). Tags: **[BIZ]** business/domain/management theory, **[TECH]** technology/architecture, **[BOTH]** a lesson that deliberately carries both (most application-family lessons).

**Honesty note.** The structure, ordering and granularity are **Bilge's synthesis**, benchmarked against the programmes and bodies of knowledge in §C at the level of course/certification pages fetched on 2026-10-26 (HTTP status and page title); syllabi were not read line by line, and no unit claims to replicate any programme. Vendor and market facts (product names, architecture claims, Turkish ERP market positions, e-document thresholds, payroll rates) change and are **verified at lesson time** from official sources; where they cannot be verified they are marked. Nothing in this curriculum states facts about Serkan's own products; Unit 40 teaches design problems that field-sales SaaS products generally face.

**Citation rule.** Every DOI below was resolved via the Crossref API on 2026-10-26 (first author, title, venue and year matched). **[book]** = standard textbook/monograph cited by author and title, no link claimed. HBR/SMR articles without DOIs are marked **[no DOI]**. **[check]** = source named but not yet verified; it is verified or dropped before the lesson that uses it is written (list in §E). If a lesson cannot be taught well in one sitting it is split (EA-x.ya/b) and this total is updated.

## A. Prerequisites assumed
Working knowledge of SQL and of building software (Serkan is a practising developer), and ~18 years of distribution operations. Assumed from sibling streams where a lesson cites them: ECO Unit 33 (double entry) before EA-22.x; ECO-31.1 (NPV) before EA-3.6/17.2; FMCG Units 6–8 and 11 before EA Units 26 and 29–31. No mathematics beyond school algebra and basic probability is needed, except EA-4.5 (Petri nets: sets and relations, stated in-line) and EA-31.2 (VRP: integer-programming formulation stated, not proved).

## B. Outline (part / unit / ID range / count / tag balance)
- **PART I — Information systems as a discipline** — 16 lessons (BIZ 12 · TECH 0 · BOTH 4)
  - Unit 1 — What enterprise information systems are: EA-1.1–EA-1.5 (5)
  - Unit 2 — IS research theories (adoption, success, structuration): EA-2.1–EA-2.5 (5)
  - Unit 3 — IT business value and strategy: EA-3.1–EA-3.6 (6)
- **PART II — Business process theory** — 9 lessons (BIZ 2 · TECH 1 · BOTH 6)
  - Unit 4 — Business processes and BPM: EA-4.1–EA-4.9 (9)
- **PART III — Enterprise architecture and IT governance** — 10 lessons (BIZ 4 · TECH 0 · BOTH 6)
  - Unit 5 — Enterprise architecture: EA-5.1–EA-5.5 (5)
  - Unit 6 — IT governance, risk, controls and service management: EA-6.1–EA-6.5 (5)
- **PART IV — Data and information management** — 18 lessons (BIZ 1 · TECH 10 · BOTH 7)
  - Unit 7 — Data modelling and databases: EA-7.1–EA-7.7 (7)
  - Unit 8 — Master data, quality and governance: EA-8.1–EA-8.5 (5)
  - Unit 9 — Analytics, warehousing and data platforms: EA-9.1–EA-9.6 (6)
- **PART V — Integration** — 11 lessons (BIZ 0 · TECH 7 · BOTH 4)
  - Unit 10 — Integration styles and patterns: EA-10.1–EA-10.5 (5)
  - Unit 11 — APIs and B2B integration: EA-11.1–EA-11.6 (6)
- **PART VI — Software architecture for enterprise applications** — 19 lessons (BIZ 0 · TECH 17 · BOTH 2)
  - Unit 12 — Architecture fundamentals: EA-12.1–EA-12.4 (4)
  - Unit 13 — Domain-driven design and data-intensive patterns: EA-13.1–EA-13.5 (5)
  - Unit 14 — Scale, reliability and operations: EA-14.1–EA-14.5 (5)
  - Unit 15 — Security, identity and privacy engineering: EA-15.1–EA-15.5 (5)
- **PART VII — Cloud and infrastructure** — 5 lessons (BIZ 1 · TECH 2 · BOTH 2)
  - Unit 16 — Cloud, SaaS and multi-tenancy: EA-16.1–EA-16.5 (5)
- **PART VIII — Acquiring, implementing and running enterprise systems** — 15 lessons (BIZ 13 · TECH 1 · BOTH 1)
  - Unit 17 — Build, buy, configure: EA-17.1–EA-17.4 (4)
  - Unit 18 — Implementation and why ERP projects fail: EA-18.1–EA-18.8 (8)
  - Unit 19 — Managing enterprise software work: EA-19.1–EA-19.3 (3)
- **PART IX — Core ERP and finance applications** — 24 lessons (BIZ 4 · TECH 1 · BOTH 19)
  - Unit 20 — ERP: concepts and core cycles: EA-20.1–EA-20.8 (8)
  - Unit 21 — ERP market and the Turkish landscape: EA-21.1–EA-21.4 (4)
  - Unit 22 — Accounting, consolidation and close systems: EA-22.1–EA-22.4 (4)
  - Unit 23 — Budgeting, planning and performance management (EPM/FP&A): EA-23.1–EA-23.5 (5)
  - Unit 24 — Treasury, cash and credit: EA-24.1–EA-24.3 (3)
- **PART X — Customer-facing and commercial systems** — 19 lessons (BIZ 3 · TECH 2 · BOTH 14)
  - Unit 25 — CRM: EA-25.1–EA-25.6 (6)
  - Unit 26 — Field-force automation and distributor systems: EA-26.1–EA-26.6 (6)
  - Unit 27 — Pricing, promotions and quoting: EA-27.1–EA-27.3 (3)
  - Unit 28 — Commerce, order management and retail: EA-28.1–EA-28.4 (4)
- **PART XI — Supply chain and operations systems** — 15 lessons (BIZ 4 · TECH 2 · BOTH 9)
  - Unit 29 — Planning systems: EA-29.1–EA-29.4 (4)
  - Unit 30 — Warehouse management: EA-30.1–EA-30.4 (4)
  - Unit 31 — Transport and routing: EA-31.1–EA-31.3 (3)
  - Unit 32 — Manufacturing, quality, product and asset systems: EA-32.1–EA-32.4 (4)
- **PART XII — Horizontal and support systems** — 11 lessons (BIZ 3 · TECH 0 · BOTH 8)
  - Unit 33 — Human capital management: EA-33.1–EA-33.3 (3)
  - Unit 34 — Procurement and supplier systems: EA-34.1–EA-34.2 (2)
  - Unit 35 — Content, documents, collaboration and workflow: EA-35.1–EA-35.3 (3)
  - Unit 36 — GRC, ITSM and portfolio systems: EA-36.1–EA-36.3 (3)
- **PART XIII — Turkish regulatory and financial infrastructure** — 7 lessons (BIZ 1 · TECH 3 · BOTH 3)
  - Unit 37 — Turkish e-document ecosystem: EA-37.1–EA-37.4 (4)
  - Unit 38 — Banking, payments and credit infrastructure: EA-38.1–EA-38.3 (3)
- **PART XIV — AI and automation, building your own, capstones** — 16 lessons (BIZ 3 · TECH 6 · BOTH 7)
  - Unit 39 — Automation and AI in enterprise systems: EA-39.1–EA-39.5 (5)
  - Unit 40 — Designing and building enterprise software yourself: EA-40.1–EA-40.6 (6)
  - Unit 41 — Capstones: EA-41.1–EA-41.5 (5)

**Recommended delivery order** (IDs are stable labels; the prerequisites column governs; the order below was checked by script so that every EA prerequisite precedes its lesson):
Unit 1 → Unit 2 → Unit 3 → EA-4.1–4.8 → Unit 7 → EA-10.1–10.3 → EA-4.9 → EA-5.1–5.4 → EA-6.1–6.4 → EA-8.1–8.2 → EA-6.5 → EA-8.3–8.5 → EA-10.4–10.5 → Unit 11 → Unit 9 → Units 12–16 → Unit 20 → EA-5.5 → Units 17–19 → EA-21.1–21.2 → Unit 22 → Unit 37 (Turkish e-documents) → EA-21.3–21.4 → Units 23–24 → Unit 38 → Units 25–36 → Unit 39 → Unit 40 → Unit 41.
Rationale: theory and vocabulary first (Part I), then the four engineering foundations every application family reuses (process, data, integration, architecture), then acquisition/implementation, then the families from the financial core outward (ERP → finance → commercial → supply chain → support), Turkish infrastructure where the families first need it, and the build-your-own unit and capstones last. Cross-stream prerequisites (ECO/FMCG IDs) are recommended, not blocking: if the cited ECO/FMCG lesson has not yet been delivered, the EA lesson restates the minimum in two or three sentences and points to the ID.

## Syllabus

## PART I — Information systems as a discipline

### Unit 1 — What enterprise information systems are
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-1.1 | BOTH | What an enterprise information system is: data vs information vs system; the socio-technical view (Leavitt diamond, Bostrom-Heinen); Anthony's levels (transaction, management control, strategic); the stack of layers; the taxonomy of enterprise application families; systems of record vs engagement vs insight | — | Bostrom & Heinen 1977; Sarker et al. 2019; Laudon & Laudon [book]; Anthony 1965 [book] |
| EA-1.2 | BIZ | The value chain and IT: Porter's value chain and how application families map onto primary and support activities; Porter-Millar "How information gives you competitive advantage" | 1.1, FMCG-1.1 | Porter 1985 [book]; Porter & Millar 1985 HBR [article, no DOI] |
| EA-1.3 | BOTH | Transaction processing systems, MIS, DSS, EIS and the Gorry-Scott Morton framework; structured vs semi-structured decisions | 1.1 | Gorry & Scott Morton 1971 SMR [article, no DOI; check]; Simon 1960 [book] |
| EA-1.4 | BIZ | History of enterprise computing: punched cards, MRP (Orlicky), MRP II, the ERP wave, client-server, Y2K, internet, SaaS, cloud ERP, AI; why each wave happened | 1.3 | Jacobs & Weston 2007 doi:10.1016/j.jom.2006.11.005; Klaus, Rosemann & Gable 2000 doi:10.1023/A:1026543906354 |
| EA-1.5 | BOTH | Enterprise software as an industry: vendor economics, licence vs subscription, ecosystems and partners, switching costs and lock-in; market-landscape sources and their limits (Gartner/Forrester as non-academic) | 1.4, ECO-8.1 | Shapiro & Varian *Information Rules* [book]; Cusumano *The Business of Software* [book] |

### Unit 2 — IS research theories (adoption, success, structuration)
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-2.1 | BIZ | IS as a research discipline: behavioural vs design science; the IT artifact; the socio-technical axis | 1.1 | Hevner et al. 2004 doi:10.2307/25148625; Sarker et al. 2019 doi:10.25300/MISQ/2019/13747 |
| EA-2.2 | BIZ | Technology acceptance: TAM (perceived usefulness, ease of use), TAM2, UTAUT; what the constructs predict and what they miss | 2.1 | Davis 1989 doi:10.2307/249008; Venkatesh et al. 2003 doi:10.2307/30036540 |
| EA-2.3 | BIZ | IS success: DeLone-McLean 1992 and the 2003 update (system, information, service quality; use; net benefits) | 2.2 | DeLone & McLean 1992 doi:10.1287/isre.3.1.60; 2003 doi:10.1080/07421222.2003.11045748 |
| EA-2.4 | BIZ | Technology and organisation: Orlikowski's duality of technology and practice lens; user coping and workarounds | 2.3 | Orlikowski 1992 doi:10.1287/orsc.3.3.398; 2000 doi:10.1287/orsc.11.4.404.14600; Beaudry & Pinsonneault 2005 doi:10.2307/25148693 |
| EA-2.5 | BOTH | Design science in practice: building an artifact as research; evaluation methods; how to read an IS paper | 2.1 | Hevner et al. 2004 (above) |

### Unit 3 — IT business value and strategy
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-3.1 | BIZ | The productivity paradox: Solow's quip, measurement explanations, Brynjolfsson 1993 and Brynjolfsson-Hitt 1996 | 1.4, ECO-14.1 | Brynjolfsson 1993 doi:10.1145/163298.163309; Brynjolfsson & Hitt 1996 doi:10.1287/mnsc.42.4.541 |
| EA-3.2 | BIZ | Complementarities: IT plus organisational capital; why the same ERP pays off in one firm and not another | 3.1 | Brynjolfsson & Hitt 2000 doi:10.1257/jep.14.4.23; Melville et al. 2004 doi:10.2307/25148636 |
| EA-3.3 | BIZ | Resource-based view of IT capability; information management capability | 3.2 | Bharadwaj 2000 doi:10.2307/3250983; Mithas et al. 2011 doi:10.2307/23043496 |
| EA-3.4 | BIZ | Strategic alignment: Henderson-Venkatraman model; business-IT alignment in practice | 3.3 | Henderson & Venkatraman 1993 doi:10.1147/sj.382.0472 |
| EA-3.5 | BIZ | "IT doesn't matter": the Carr debate, commoditisation vs differentiation; where custom software still creates advantage | 3.4 | Carr 2003 HBR [article, no DOI]; Carr *Does IT Matter?* [book] |
| EA-3.6 | BIZ | Measuring IT value in a business case: NPV/TCO/ROI of systems, real options in IT investment, benefits realisation | 3.5, ECO-31.1 | Synthesis; ECO capital-budgeting lessons |

## PART II — Business process theory

### Unit 4 — Business processes and BPM
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-4.1 | BIZ | What a business process is; functional vs process organisation; reengineering (Hammer, Hammer-Champy) and process innovation (Davenport, Davenport-Short) | 1.2 | Hammer 1990 HBR [no DOI]; Hammer & Champy 1993 [book]; Davenport 1993 *Process Innovation* [book] |
| EA-4.2 | BIZ | The BPM lifecycle: identification, discovery, analysis, redesign, implementation, monitoring; process architecture | 4.1 | Dumas, La Rosa, Mendling & Reijers *Fundamentals of BPM* [book] |
| EA-4.3 | BOTH | Process modelling I: BPMN 2.0 core (events, activities, gateways, pools/lanes, message flows) | 4.2 | OMG BPMN 2.0.2 https://www.omg.org/spec/BPMN/2.0.2/ |
| EA-4.4 | BOTH | Process modelling II: modelling quality (7PMG), EPCs (ARIS), value-stream maps; when each notation fits | 4.3 | Mendling, Reijers & van der Aalst 2010 doi:10.1016/j.infsof.2009.08.004; Scheer *ARIS* [book] |
| EA-4.5 | TECH | Formal foundations: Petri nets, workflow nets, soundness | 4.3 | van der Aalst 1998 doi:10.1142/S0218126698000043 |
| EA-4.6 | BOTH | Process analysis: cycle time, flow efficiency, Little's law, queues, cost per case, waste | 4.2 | Dumas et al. [book]; Hopp & Spearman *Factory Physics* [book] |
| EA-4.7 | BOTH | Process mining I: event logs, discovery (alpha algorithm), conformance checking | 4.5 | van der Aalst, Weijters & Maruster 2004 doi:10.1109/TKDE.2004.47; https://www.processmining.org/ |
| EA-4.8 | BOTH | Process mining II: enhancement, object-centric event logs, mining ERP order-to-cash data | 4.7 | van der Aalst *Process Mining* 2nd ed. [book] |
| EA-4.9 | BOTH | Workflow engines and process execution: BPMS, human tasks, case management; orchestration vs choreography | 4.3, 10.1 | Weske *Business Process Management* [book] |

## PART III — Enterprise architecture and IT governance

### Unit 5 — Enterprise architecture
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-5.1 | BOTH | Why EA: Zachman framework; architecture as decision structure; operating models (Ross-Weill-Robertson) | 1.1, 3.4 | Zachman 1987 doi:10.1147/sj.263.0276; Ross, Weill & Robertson *Enterprise Architecture as Strategy* [book] |
| EA-5.2 | BOTH | TOGAF: ADM phases, architecture domains (business, data, application, technology), repository | 5.1 | The Open Group TOGAF https://www.opengroup.org/togaf |
| EA-5.3 | BOTH | ArchiMate: layers, aspects, viewpoints; modelling an application landscape | 5.2 | ArchiMate https://www.opengroup.org/archimate-forum/archimate-overview |
| EA-5.4 | BIZ | Business capability maps, value streams, application portfolio management (TIME), rationalisation | 5.3 | Synthesis; TOGAF Series Guides [check] |
| EA-5.5 | BOTH | Reference architectures and the application landscape: ERP core vs best-of-breed vs suite; "clean core"; the two-tier ERP pattern | 5.4, 20.1 | Synthesis; vendor docs [check at lesson time] |

### Unit 6 — IT governance, risk, controls and service management
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-6.1 | BIZ | IT governance: decision rights archetypes (Weill-Ross); COBIT 2019 governance and management objectives | 5.1 | Weill & Ross *IT Governance* [book]; COBIT https://www.isaca.org/resources/cobit |
| EA-6.2 | BIZ | IT service management: ITIL 4 service value system, practices; SLAs, incident/problem/change | 6.1 | ITIL 4 https://www.axelos.com/certifications/itil-service-management |
| EA-6.3 | BOTH | Information security management: ISO/IEC 27001 ISMS, Annex A controls, risk treatment | 6.1 | ISO/IEC 27001:2022 [standard; iso.org blocks fetch] |
| EA-6.4 | BOTH | Internal controls and ITGC: COSO, SOX 404, segregation of duties, access reviews, change control; the auditor's view of an ERP (CISA domains) | 6.3, ECO-33.7 | COSO 2013 [check]; ISACA CISA https://www.isaca.org/credentialing/cisa |
| EA-6.5 | BIZ | Data governance: decision rights over data, roles (owner, steward), policies | 6.1, 7.1 | Khatri & Brown 2010 doi:10.1145/1629175.1629210; DAMA-DMBOK2 [book] |

## PART IV — Data and information management

### Unit 7 — Data modelling and databases
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-7.1 | TECH | Conceptual modelling: entities, relationships, cardinality; Chen's ER model | 1.1 | Chen 1976 doi:10.1145/320434.320440 |
| EA-7.2 | TECH | The relational model: relations, keys, relational algebra, SQL as its practical form | 7.1 | Codd 1970 doi:10.1145/362384.362685; Date [book] |
| EA-7.3 | TECH | Normalisation: functional dependencies, 1NF-3NF, BCNF; when enterprise systems denormalise | 7.2 | Elmasri & Navathe [book] |
| EA-7.4 | TECH | Enterprise data model patterns: party/role, product/item, document header-line, ledger, temporal (effective-dated) data | 7.3 | Hay *Data Model Patterns* [book]; Silverston *Data Model Resource Book* [book] |
| EA-7.5 | TECH | Transactions and ACID; isolation levels and anomalies; recovery (logging) | 7.2 | Haerder & Reuter 1983 doi:10.1145/289.291; Gray & Reuter [book] |
| EA-7.6 | TECH | Beyond relational: document, key-value, column, graph, time-series stores; "one size fits all" | 7.5 | Stonebraker & Çetintemel 2005 doi:10.1109/ICDE.2005.1; Kleppmann *DDIA* [book] |
| EA-7.7 | TECH | Indexing, query planning and performance for transactional workloads | 7.5 | Ramakrishnan & Gehrke [book]; PostgreSQL docs |

### Unit 8 — Master data, quality and governance
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-8.1 | BOTH | Master vs transactional vs reference vs metadata; DAMA-DMBOK knowledge areas | 7.4 | DAMA-DMBOK2 [book] |
| EA-8.2 | BOTH | Data quality: dimensions (Wang-Strong), measurement, root causes in field and ERP data | 8.1 | Wang & Strong 1996 doi:10.1080/07421222.1996.11518099 |
| EA-8.3 | BOTH | MDM architectures: registry, consolidation, coexistence, centralised; matching and survivorship (customer/outlet master) | 8.2 | Loshin *Master Data Management* [book] |
| EA-8.4 | BOTH | Product information management (PIM) and GS1 identification (GTIN, GLN, SSCC, GDSN) | 8.3 | GS1 General Specifications [check; gs1.org blocks fetch] |
| EA-8.5 | BOTH | Metadata, lineage, data catalogues | 8.3, 6.5 | DAMA-DMBOK2 [book] |

### Unit 9 — Analytics, warehousing and data platforms
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-9.1 | BOTH | OLTP vs OLAP; data warehousing concepts; Inmon vs Kimball | 7.5 | Chaudhuri & Dayal 1997 doi:10.1145/248603.248616; Inmon [book]; Kimball & Ross [book] |
| EA-9.2 | TECH | Dimensional modelling: facts, dimensions, grain, SCDs; star schema for sell-in/sell-out | 9.1 | Kimball & Ross *The Data Warehouse Toolkit* [book] |
| EA-9.3 | TECH | ETL/ELT, CDC, orchestration, data contracts | 9.2, 10.3 | Kleppmann [book] |
| EA-9.4 | TECH | Columnar storage, MPP, MapReduce to Spark, data lakes and the lakehouse | 9.3 | Dean & Ghemawat 2008 doi:10.1145/1327452.1327492; Armbrust et al. CIDR 2021 https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf |
| EA-9.5 | BOTH | Data mesh and data products: domain ownership, federated governance; critique | 9.4, 6.5 | Dehghani [book]; https://martinfowler.com/articles/data-mesh-principles.html |
| EA-9.6 | BIZ | BI and analytics: descriptive-diagnostic-predictive-prescriptive; KPI design, semantic layers, dashboards | 9.2 | Chen, Chiang & Storey 2012 doi:10.2307/41703503; Watson & Wixom 2007 doi:10.1109/MC.2007.331 |

## PART V — Integration

### Unit 10 — Integration styles and patterns
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-10.1 | TECH | Why integration is hard: heterogeneity, semantics, federated databases; four integration styles (file, shared DB, RPC, messaging) | 7.2 | Sheth & Larson 1990 doi:10.1145/96602.96604; Hohpe & Woolf *EIP* [book] |
| EA-10.2 | TECH | Messaging patterns: channels, routers, translators, endpoints; idempotent receiver, dead-letter | 10.1 | Hohpe & Woolf [book]; https://www.enterpriseintegrationpatterns.com/ |
| EA-10.3 | TECH | Message brokers and event streaming: queues vs logs (RabbitMQ-style vs Kafka-style), ordering, delivery semantics | 10.2 | Kleppmann [book] |
| EA-10.4 | TECH | EAI, ESB, SOA and iPaaS: hub-and-spoke to smart-endpoints; what went wrong with ESBs | 10.2 | Hohpe & Woolf [book]; synthesis |
| EA-10.5 | BOTH | Canonical data models, mapping and semantic integration; master-data synchronisation | 10.4, 8.3 | Hohpe & Woolf [book] |

### Unit 11 — APIs and B2B integration
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-11.1 | TECH | REST: Fielding's constraints, resources, HTTP semantics, idempotency, pagination, versioning | 10.1 | Fielding & Taylor 2002 doi:10.1145/514183.514185 |
| EA-11.2 | TECH | RPC and query APIs: gRPC/protobuf, GraphQL, webhooks, OpenAPI; choosing among them | 11.1 | gRPC, GraphQL, OpenAPI specs [check URLs] |
| EA-11.3 | TECH | Event-driven architecture: events vs commands, outbox pattern, schema evolution | 11.1, 10.3 | Kleppmann [book]; Richardson *Microservices Patterns* [book] |
| EA-11.4 | BOTH | B2B/EDI: EDIFACT/X12, AS2, EANCOM, GS1 XML; retailer-supplier integration | 10.5, 8.4 | GS1 EANCOM [check] |
| EA-11.5 | BOTH | UBL and UBL-TR: the document model behind Turkish e-documents (bridges Unit 37) | 11.4 | OASIS UBL 2.1 [check]; GİB e-belge technical guides [check; site unreachable from box] |
| EA-11.6 | BOTH | API management and API economy: gateways, rate limits, developer portals, partner APIs | 11.2 | Synthesis |

## PART VI — Software architecture for enterprise applications

### Unit 12 — Architecture fundamentals
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-12.1 | TECH | Software architecture: quality attributes, tactics, views; architecture decision records | 7.2 | Bass, Clements & Kazman *Software Architecture in Practice* [book] |
| EA-12.2 | TECH | Modularity: Parnas information hiding, coupling/cohesion, Conway's law | 12.1 | Parnas 1972 doi:10.1145/361598.361623; Conway 1968 [Datamation, no DOI] |
| EA-12.3 | TECH | Enterprise application patterns: layers, transaction script vs domain model, unit of work, repository | 12.2 | Fowler *Patterns of Enterprise Application Architecture* [book] |
| EA-12.4 | TECH | Monolith, modular monolith, microservices: trade-offs, migration evidence | 12.3 | Balalaie et al. 2016 doi:10.1109/MS.2016.64; Newman *Building Microservices* [book] |

### Unit 13 — Domain-driven design and data-intensive patterns
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-13.1 | BOTH | DDD strategic design: ubiquitous language, bounded contexts, context maps (sales vs finance "customer") | 12.3 | Evans *Domain-Driven Design* [book] |
| EA-13.2 | TECH | DDD tactical design: entities, value objects, aggregates, domain events | 13.1 | Evans [book]; Vernon *Implementing DDD* [book] |
| EA-13.3 | TECH | CQRS and event sourcing; the ledger as an event-sourced system | 13.2 | Fowler bliki [check]; Kleppmann [book] |
| EA-13.4 | TECH | Distributed transactions: 2PC, sagas, compensation; life beyond distributed transactions | 7.5, 11.3 | Garcia-Molina & Salem 1987 doi:10.1145/38713.38742; Helland 2016 doi:10.1145/3012426.3025012 |
| EA-13.5 | TECH | Consistency: CAP, BASE, eventual consistency, ordering and clocks | 13.4 | Gilbert & Lynch 2002 doi:10.1145/564585.564601; Vogels 2009 doi:10.1145/1435417.1435432; Lamport 1978 doi:10.1145/359545.359563 |

### Unit 14 — Scale, reliability and operations
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-14.1 | TECH | Performance and scalability: load, latency percentiles, tail latency, capacity estimation | 12.1 | Dean & Barroso 2013 doi:10.1145/2408776.2408794 |
| EA-14.2 | TECH | Caching, queues and back-pressure; batch vs stream jobs (period-end closing, MRP runs) | 14.1, 10.3 | Kleppmann [book] |
| EA-14.3 | TECH | Observability: logs, metrics, traces; SLOs and error budgets | 14.1, 6.2 | Beyer et al. *Site Reliability Engineering* [book] |
| EA-14.4 | TECH | High availability and disaster recovery: RPO/RTO, replication, backups, failover drills | 14.3 | Beyer et al. [book] |
| EA-14.5 | TECH | Testing and release of enterprise software: test pyramid, migration tests, CI/CD, feature flags | 12.4 | Humble & Farley *Continuous Delivery* [book] |

### Unit 15 — Security, identity and privacy engineering
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-15.1 | TECH | Security principles: Saltzer-Schroeder; threat modelling; OWASP top risks | 12.1 | Saltzer & Schroeder 1975 doi:10.1109/PROC.1975.9939 |
| EA-15.2 | TECH | Authorisation: RBAC, ABAC, row-level security, SoD in ERP roles | 15.1, 6.4 | Sandhu et al. 1996 doi:10.1109/2.485845 |
| EA-15.3 | TECH | Identity federation: SSO, SAML, OAuth 2.0, OpenID Connect, SCIM | 15.2 | RFC 6749 https://www.rfc-editor.org/rfc/rfc6749; OIDC Core https://openid.net/specs/openid-connect-core-1_0.html |
| EA-15.4 | TECH | Audit trails and tamper evidence: immutable logs, who-did-what, legal retention | 15.2, 13.3 | Synthesis; VUK retention rules [check at lesson time] |
| EA-15.5 | BOTH | Privacy engineering: KVKK (6698) and GDPR principles, lawful bases, data subject rights, VERBİS, cross-border transfer; privacy by design, k-anonymity | 15.4 | KVKK https://www.kvkk.gov.tr/; Sweeney 2002 doi:10.1142/S0218488502001648; GDPR text [check URL] |

## PART VII — Cloud and infrastructure

### Unit 16 — Cloud, SaaS and multi-tenancy
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-16.1 | BOTH | Cloud computing: NIST definition; IaaS/PaaS/SaaS; economics of elasticity | 1.5, 14.1 | Mell & Grance 2011 doi:10.6028/NIST.SP.800-145; Armbrust et al. 2010 doi:10.1145/1721654.1721672 |
| EA-16.2 | TECH | Containers and Kubernetes at concept level: Borg lineage, declarative state, scheduling | 16.1 | Burns et al. 2016 doi:10.1145/2890784 |
| EA-16.3 | TECH | Multi-tenant SaaS architecture: shared DB/shared schema vs schema-per-tenant vs DB-per-tenant; tenant isolation, noisy neighbours, customisation | 16.1, 7.4 | Bezemer & Zaidman 2010 doi:10.1145/1862372.1862393 |
| EA-16.4 | BIZ | SaaS business model: unit economics, churn, ARR/NRR, pricing tiers; implications for architecture | 16.3, ECO-31.1 | Synthesis |
| EA-16.5 | BOTH | FinOps and cloud cost; multi-cloud and data residency (Turkish public-sector/BDDK constraints flagged for checking) | 16.4 | FinOps Foundation [check]; BDDK regulation [check] |

## PART VIII — Acquiring, implementing and running enterprise systems

### Unit 17 — Build, buy, configure
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-17.1 | BIZ | Build vs buy vs configure vs compose; fit-gap; customisation debt | 5.5, 3.6 | Synthesis; Soh et al. 2000 doi:10.1145/332051.332070 |
| EA-17.2 | BIZ | Total cost of ownership: licence/subscription, implementation, integration, run, exit; a worked TCO model | 17.1, ECO-25.2 | Synthesis (illustrative numbers) |
| EA-17.3 | BIZ | Requirements and business analysis: BABOK knowledge areas, user stories vs specifications | 17.1 | IIBA BABOK v3 [book]; https://www.iiba.org/business-analysis-certifications/cbap/ |
| EA-17.4 | BIZ | Vendor selection: RFI/RFP, scoring, demos/scripts, reference checks, contracts and SLAs | 17.3 | Synthesis |

### Unit 18 — Implementation and why ERP projects fail
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-18.1 | BIZ | Putting the enterprise into the enterprise system; integration benefits vs imposed logic | 17.1 | Davenport 1998 HBR [article, no DOI] |
| EA-18.2 | BIZ | The ERP experience cycle (Markus-Tanis) and adopter problems | 18.1 | Markus et al. 2000 doi:10.1080/02683960010008944 |
| EA-18.3 | BIZ | Critical success factors and risk factors | 18.2 | Holland & Light 1999 doi:10.1109/52.765784; Sumner 2000 doi:10.1080/02683960010009079; Nah et al. 2001 doi:10.1108/14637150110392782 |
| EA-18.4 | BIZ | Post-implementation: stabilisation dip, learning, interdependence; "surviving vs thriving" | 18.3 | Ross & Vitale 2000 doi:10.1023/A:1026500224101; Robey et al. 2002 doi:10.1080/07421222.2002.11045713; Gattiker & Goodhue 2005 doi:10.2307/25148695 |
| EA-18.5 | BOTH | Implementation methodology: phases, SAP Activate-style fit-to-standard, waterfall vs agile vs hybrid, cutover | 18.3 | Parr & Shanks 2000 doi:10.1080/02683960010009051; Boehm 1988 doi:10.1109/2.59 |
| EA-18.6 | TECH | Data migration: profiling, cleansing, mapping, mock loads, reconciliation, opening balances | 18.5, 8.2 | Synthesis |
| EA-18.7 | BIZ | Change management and training: Kotter, Lewin, user resistance, key-user networks | 18.4, 2.4 | Kotter 1995 HBR [no DOI]; Beaudry & Pinsonneault 2005 (above) |
| EA-18.8 | BIZ | Evidence on ERP payoff: firm performance studies | 18.4, 3.2 | Hitt, Wu & Zhou 2002 doi:10.1080/07421222.2002.11045716 |

### Unit 19 — Managing enterprise software work
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-19.1 | BIZ | Project management: PMBOK performance domains, scope-time-cost, risk registers, earned value | 17.4 | PMI PMBOK 7 [book]; PMI site [403 to fetch] |
| EA-19.2 | BIZ | Agile and product management for enterprise software: Scrum, roadmaps, discovery, B2B product-market fit | 19.1 | Agile Manifesto [check URL]; Cagan *Inspired* [book] |
| EA-19.3 | BIZ | Outsourcing, offshoring and partner ecosystems; running an AMS contract | 19.1 | Synthesis |

## PART IX — Core ERP and finance applications

### Unit 20 — ERP: concepts and core cycles
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-20.1 | BOTH | What ERP is: single database, integrated modules, organisational structures (company code, plant, sales org), configuration vs code | 1.4, 7.4 | Klaus et al. 2000; Kumar & van Hillegersberg 2000 doi:10.1145/332051.332063; Magal & Word *Integrated Business Processes with ERP Systems* [book] |
| EA-20.2 | BOTH | Order-to-cash in depth: inquiry, order, ATP, delivery, goods issue, billing, receivables, cash application; documents and postings | 20.1, ECO-33.3 | Magal & Word [book] |
| EA-20.3 | BOTH | Procure-to-pay: requisition, PO, goods receipt, invoice receipt, three-way match, GR/IR, payment | 20.2 | Magal & Word [book] |
| EA-20.4 | BOTH | Record-to-report: GL, subledgers, period close, intercompany, reporting | 20.3, ECO-33.7 | Magal & Word [book] |
| EA-20.5 | BOTH | Inventory management in ERP: movement types, valuation (moving average vs standard), batches, serials, expiry | 20.3, ECO-34.1 | Magal & Word [book] |
| EA-20.6 | BOTH | Plan-to-produce I: BOM, routings, work centres; MRP logic (netting, lot sizing, offsetting) | 20.5, FMCG-11.3 | Orlicky *MRP* [book]; Vollmann et al. *MPC Systems* [book] |
| EA-20.7 | BOTH | Plan-to-produce II: MRP II, capacity planning, APS and finite scheduling; limits of MRP | 20.6 | Stadtler 2005 doi:10.1016/j.ejor.2004.03.001 |
| EA-20.8 | BOTH | ERP and the supply chain: evidence on ERP's supply-chain impact | 20.7 | Akkermans et al. 2003 doi:10.1016/S0377-2217(02)00550-7 |

### Unit 21 — ERP market and the Turkish landscape
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-21.1 | BOTH | Tier-1 suites: SAP S/4HANA (in-memory, Universal Journal, clean core), Oracle (Fusion/NetSuite), Microsoft Dynamics 365; architecture and positioning | 20.4 | Vendor documentation [check at lesson time] |
| EA-21.2 | BOTH | Open-source and mid-market: Odoo, ERPNext; modular architecture and extension models | 21.1 | Odoo docs https://www.odoo.com/documentation/ |
| EA-21.3 | BOTH | Turkish ERP market: Logo (Tiger/j-Platform/Netsis), Mikro, Nebim (retail), Canias, others; localisation (Tekdüzen, e-documents, payroll); market facts only from verifiable sources | 21.2, 37.1 | https://www.logo.com.tr/; https://www.mikro.com.tr/; others [check] |
| EA-21.4 | BOTH | ERP data model study: reading an open-source ERP schema (documents, lines, ledger) | 21.2, 7.4 | Odoo source/docs |

### Unit 22 — Accounting, consolidation and close systems
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-22.1 | BOTH | The accounting engine: chart of accounts (Tekdüzen), account determination, subledger-to-GL, double-entry invariants as constraints | 20.4, ECO-33.2 | ECO-33.2; synthesis |
| EA-22.2 | BOTH | Multi-currency, multi-GAAP, parallel ledgers; inflation adjustment (TMS 29 / VUK) in systems | 22.1, ECO-35.3 | Synthesis; ECO-35.x |
| EA-22.3 | BOTH | Consolidation and close systems: intercompany elimination, ownership, close management, disclosure management | 22.2, ECO-34.9 | Synthesis |
| EA-22.4 | BOTH | Fixed assets, leases and revenue-recognition subsystems (IFRS 15/16 engines) | 22.1, ECO-34.5 | Synthesis |

### Unit 23 — Budgeting, planning and performance management (EPM/FP&A)
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-23.1 | BIZ | Management control and budgeting theory: purposes, games, Beyond Budgeting critique | 1.3, ECO-39.4 | Anthony & Govindarajan [book]; Hope & Fraser *Beyond Budgeting* [book] |
| EA-23.2 | BIZ | Driver-based planning, rolling forecasts, zero-based budgeting; Turkish practice under high inflation | 23.1, ECO-37.2 | Synthesis |
| EA-23.3 | BIZ | Strategic performance management: balanced scorecard, strategy maps, OKRs | 23.1 | Kaplan & Norton 1992 HBR [no DOI]; *The Balanced Scorecard* [book] |
| EA-23.4 | TECH | EPM architecture: multidimensional (OLAP) cubes, sparse/dense dimensions, write-back, versions; Hyperion/Essbase, Anaplan, Board, SAP BPC/SAC as archetypes | 23.2, 9.1 | Vendor docs [check] |
| EA-23.5 | BOTH | Profitability and cost management systems: allocations, ABC engines, customer/channel profitability | 23.4, ECO-39.3 | Kaplan & Cooper *Cost & Effect* [book] |

### Unit 24 — Treasury, cash and credit
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-24.1 | BIZ | Treasury management: cash positioning, forecasting, FX/interest risk, bank relationships | 22.1, ECO-32.2, ECO-32.3 | Synthesis |
| EA-24.2 | BOTH | Bank connectivity: statements (MT940/camt.053), payment files (ISO 20022 pain.001), host-to-host; Turkish bank integration | 24.1, 11.4 | ISO 20022 [check] |
| EA-24.3 | BOTH | Credit management and collections systems: limits, scoring, dunning, DBS (doğrudan borçlandırma) | 24.2, FMCG-7.3, ECO-38.3 | Synthesis |

## PART X — Customer-facing and commercial systems

### Unit 25 — CRM
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-25.1 | BIZ | CRM as strategy: Payne-Frow framework; operational, analytical, collaborative CRM | 1.2 | Payne & Frow 2005 doi:10.1509/jmkg.2005.69.4.167 |
| EA-25.2 | BIZ | Customer value: CLV models (retention, migration, probabilistic) | 25.1, ECO-25.2 | Gupta et al. 2006 doi:10.1177/1094670506293810 |
| EA-25.3 | BOTH | Sales force automation in B2B: leads, opportunities, pipeline, forecasting; data model | 25.1, FMCG-13.8 | Synthesis; FMCG-8.10 |
| EA-25.4 | BOTH | Marketing automation and customer data platforms; consent under KVKK / İYS | 25.3, 15.5 | İYS [check] |
| EA-25.5 | BOTH | Service management: cases, SLAs, omnichannel contact centre, knowledge bases | 25.3 | Synthesis |
| EA-25.6 | BOTH | CRM platforms and architecture: metadata-driven multi-tenant platforms (Salesforce archetype), Dynamics, HubSpot; extension models | 25.5, 16.3 | Vendor docs [check] |

### Unit 26 — Field-force automation and distributor systems
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-26.1 | BIZ | Retail-execution SFA in FMCG: visit planning, journey plans, perfect store, order capture, surveys; what the business needs | 25.3, FMCG-8.10 | FMCG-8.10, 8.13; synthesis |
| EA-26.2 | BOTH | Field-force data model: outlet, route, visit, order, audit, photo, GPS check-in | 26.1, 7.4 | Synthesis |
| EA-26.3 | TECH | Mobile offline-first architecture I: local store, sync protocols, conflict detection | 26.2, 13.5 | Terry et al. 1995 doi:10.1145/224056.224070; Kleppmann et al. 2019 doi:10.1145/3359591.3359737 |
| EA-26.4 | TECH | Mobile offline-first II: CRDTs vs server-authoritative merges; delta sync; device management, security of lost devices | 26.3 | Shapiro et al. 2011 doi:10.1007/978-3-642-24550-3_29 |
| EA-26.5 | BOTH | Van sales and pre-sales: on-device invoicing, stock on truck, cash collection, end-of-day reconciliation; e-invoice/e-arşiv on the road | 26.2, 37.2 | Synthesis |
| EA-26.6 | BOTH | Distributor management systems (DMS): manufacturer-distributor data sharing, secondary sales visibility, claims | 26.5, FMCG-7.4 | Synthesis |

### Unit 27 — Pricing, promotions and quoting
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-27.1 | BOTH | Pricing engines: condition technique (price lists, discounts, scales, access sequences), price waterfall | 20.2, FMCG-5.1 | Nagle & Müller *Strategy and Tactics of Pricing* [book] |
| EA-27.2 | BOTH | Trade promotion management and optimisation (TPM/TPO), accruals and settlement; revenue growth management systems | 27.1, FMCG-5.x | Synthesis; FMCG Unit 5 |
| EA-27.3 | BOTH | CPQ: configuration rules, quote approval, guided selling | 27.1 | Synthesis |

### Unit 28 — Commerce, order management and retail
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-28.1 | BOTH | Order management systems: distributed order orchestration, ATP across nodes, order lifecycle | 20.2 | Synthesis |
| EA-28.2 | BOTH | E-commerce and B2B portals: catalog, cart, checkout, headless commerce; marketplace integration (Trendyol/Hepsiburada-type, facts checked at lesson time) | 28.1, 11.1 | Synthesis |
| EA-28.3 | BOTH | POS and retail systems: store systems, ÖKC/yeni nesil ÖKC (Turkish fiscal POS), loyalty, merchandising; Nebim-type retail ERP | 28.2, 37.1 | GİB ÖKC rules [check] |
| EA-28.4 | BOTH | Payments in commerce: card acquiring, 3-D Secure, virtual POS, tokenisation, PCI DSS | 28.3, 15.1 | PCI DSS [check] |

## PART XI — Supply chain and operations systems

### Unit 29 — Planning systems
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-29.1 | BIZ | SCM software map: planning vs execution; APS architecture | 20.7, FMCG-11.1 | Stadtler 2005 (above); Chopra & Meindl [book] |
| EA-29.2 | BOTH | Demand planning systems: statistical forecasting, consensus, forecast value added; bullwhip and information sharing | 29.1, FMCG-11.2 | Lee, Padmanabhan & Whang 1997 doi:10.1287/mnsc.43.4.546 |
| EA-29.3 | BOTH | Supply and inventory planning: DRP, multi-echelon inventory optimisation | 29.2, FMCG-11.4 | Silver, Pyke & Thomas [book] |
| EA-29.4 | BIZ | S&OP/IBP process and its system support | 29.3, FMCG-11.6 | Synthesis |

### Unit 30 — Warehouse management
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-30.1 | BIZ | Warehouse operations: receiving, putaway, storage, picking, packing, shipping; KPIs | 20.5, FMCG-11.7 | Gu et al. 2007 doi:10.1016/j.ejor.2006.02.025; Bartholdi & Hackman https://www.warehouse-science.com/ |
| EA-30.2 | BOTH | Slotting and storage assignment; picking strategies (discrete, batch, zone, wave), routing | 30.1 | de Koster et al. 2007 doi:10.1016/j.ejor.2006.07.009 |
| EA-30.3 | TECH | WMS architecture: locations, handling units, tasks; WMS vs WES vs WCS; automation interfaces | 30.2 | Synthesis |
| EA-30.4 | BOTH | Identification and capture: barcodes (EAN-13, GS1-128, DataMatrix), SSCC, RFID/EPC; Turkish track-and-trace contexts | 30.3, 8.4 | GS1 [check] |

### Unit 31 — Transport and routing
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-31.1 | BIZ | TMS: planning, tendering, execution, freight audit; fleet management and telematics | 30.1 | Synthesis |
| EA-31.2 | TECH | Vehicle routing at concept level: VRP, CVRP, VRPTW; Clarke-Wright savings; metaheuristics | 31.1, FMCG-8.5 | Dantzig & Ramser 1959 doi:10.1287/mnsc.6.1.80; Clarke & Wright 1964 doi:10.1287/opre.12.4.568; Laporte 2009 doi:10.1287/trsc.1090.0301 |
| EA-31.3 | BOTH | Route planning for field sales vs delivery; geocoding, distance matrices, e-irsaliye on dispatch | 31.2, 37.2 | Synthesis |

### Unit 32 — Manufacturing, quality, product and asset systems
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-32.1 | BOTH | MES and ISA-95 levels; shop-floor integration, OEE | 20.7 | ISA-95 / IEC 62264 [check] |
| EA-32.2 | BOTH | QMS: inspection, CAPA, HACCP/ISO 22000 traceability in food | 32.1 | ISO 9001 / ISO 22000 [check] |
| EA-32.3 | BOTH | PLM: product structures, engineering change, BOM transfer to ERP | 32.1 | Stark *Product Lifecycle Management* [book] |
| EA-32.4 | BOTH | EAM/CMMS: asset registers, preventive and predictive maintenance | 32.1 | ISO 55000 [check] |

## PART XII — Horizontal and support systems

### Unit 33 — Human capital management
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-33.1 | BIZ | HCM/HRIS scope: core HR, org management, recruiting, performance, learning | 20.1 | Synthesis |
| EA-33.2 | BOTH | Payroll engines: gross-to-net, time evaluation; Turkish context (SGK premiums, gelir vergisi, damga vergisi, asgari ücret, kıdem) verified at lesson time | 33.1, ECO-43.2 | SGK https://www.sgk.gov.tr/; mevzuat https://www.mevzuat.gov.tr/ |
| EA-33.3 | BOTH | Workforce management and sales-incentive compensation systems | 33.2, FMCG-8.8 | Synthesis |

### Unit 34 — Procurement and supplier systems
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-34.1 | BIZ | Strategic sourcing, SRM, spend analysis, contract management | 20.3 | Monczka et al. *Purchasing and SCM* [book] |
| EA-34.2 | BOTH | e-procurement: catalogues, punch-out, supplier networks, e-auctions; public procurement (EKAP) | 34.1 | EKAP [check] |

### Unit 35 — Content, documents, collaboration and workflow
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-35.1 | BOTH | ECM/DMS: capture, metadata, versioning, retention, records management | 8.5 | ISO 15489 [check] |
| EA-35.2 | BOTH | e-signature and KEP: e-imza (Law 5070), mali mühür, KEP, eIDAS comparison | 35.1 | Law 5070 mevzuat [check] |
| EA-35.3 | BOTH | Collaboration, intranet and workflow/approval suites; low-code BPM | 35.1, 4.9 | Synthesis |

### Unit 36 — GRC, ITSM and portfolio systems
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-36.1 | BOTH | GRC platforms: risk registers, control testing, policy management, audit management | 6.4 | Synthesis |
| EA-36.2 | BOTH | ITSM/ESM platforms: CMDB, service catalogue, workflow; ServiceNow archetype | 6.2 | Vendor docs [check] |
| EA-36.3 | BIZ | Project and portfolio management (PPM): portfolio selection, resource management, professional services automation | 19.1 | Synthesis |

## PART XIII — Turkish regulatory and financial infrastructure

### Unit 37 — Turkish e-document ecosystem
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-37.1 | BOTH | The e-belge system map: e-fatura, e-arşiv, e-irsaliye, e-defter, e-SMM, e-müstahsil, e-adisyon; who is obliged (thresholds checked at lesson time); legal basis (VUK 213, tebliğler) | 11.5, ECO-43.6 | GİB e-belge portal [check; unreachable from box 2026-10-26]; mevzuat https://www.mevzuat.gov.tr/ |
| EA-37.2 | TECH | e-fatura technically: UBL-TR document, profiles (TEMELFATURA, TICARIFATURA), envelopes, application responses, ETTN/UUID, XSLT views, mali mühür signing | 37.1 | GİB UBL-TR guides [check] |
| EA-37.3 | TECH | Integration routes: GİB portal vs direct integration vs özel entegratör; integrator APIs; error handling, retries and idempotency | 37.2, 11.3 | GİB özel entegratör list [check] |
| EA-37.4 | BOTH | e-defter and e-arşiv: berat, archive obligations, reconciliation with ERP ledgers | 37.3, 22.1 | GİB [check] |

### Unit 38 — Banking, payments and credit infrastructure
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-38.1 | BIZ | Turkish payment system map: EFT, FAST, BKM, card schemes, TR Karekod; TCMB as operator and regulator (Law 6493) | 24.2, ECO-50.1 | TCMB [check]; BKM https://bkm.com.tr/ |
| EA-38.2 | TECH | Open banking: PSD2 concepts, Turkish ÖHVPS/account-information and payment-initiation APIs (BKM GEÇİT) | 38.1, 15.3 | BKM https://bkm.com.tr/ [GEÇİT page check] |
| EA-38.3 | BOTH | Credit bureaus and risk data: KKB, Findeks; using bureau data in credit workflows | 38.1, 24.3 | KKB https://www.kkb.com.tr/ |

## PART XIV — AI and automation, building your own, capstones

### Unit 39 — Automation and AI in enterprise systems
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-39.1 | BOTH | Low-code/no-code platforms: citizen development, governance, limits | 35.3 | Synthesis |
| EA-39.2 | BOTH | Robotic process automation: definition, where it fits (lightweight IT), risks | 39.1, 4.6 | van der Aalst, Bichler & Heinzl 2018 doi:10.1007/s12599-018-0542-4 |
| EA-39.3 | BIZ | Generative AI and work: experimental evidence and exposure studies | 39.2, 3.2 | Noy & Zhang 2023 doi:10.1126/science.adh2586; Brynjolfsson, Li & Raymond 2025 doi:10.1093/qje/qjae044; Eloundou et al. 2024 doi:10.1126/science.adj0998 |
| EA-39.4 | TECH | LLMs inside enterprise systems: retrieval-augmented generation over ERP/CRM data, tool use, permissions, hallucination and evaluation | 39.3, 15.2 | Lewis et al. 2020 arXiv:2005.11401; Ji et al. 2023 doi:10.1145/3571730 |
| EA-39.5 | BOTH | ML in enterprise apps: forecasting, recommendation (next-best-action in SFA), anomaly detection; MLOps and governance | 39.4, 29.2 | Synthesis |

### Unit 40 — Designing and building enterprise software yourself
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-40.1 | BOTH | From domain to product: domain discovery with practitioners, event storming, scoping an MVP for a B2B vertical SaaS | 13.1, 19.2 | Evans [book]; Brandolini *Introducing EventStorming* [book] |
| EA-40.2 | TECH | Multi-tenant data model for a field-sales SaaS: tenant keys, row-level security, per-tenant configuration, reference data | 40.1, 16.3, 26.2 | Synthesis; PostgreSQL RLS docs [check] |
| EA-40.3 | TECH | Offline sync design for field apps: change tracking, versioning, conflict policy per entity, idempotent order submission | 40.2, 26.4 | Synthesis on 26.3–26.4 sources |
| EA-40.4 | TECH | Integrating with customers' ERPs (Logo/Mikro/SAP-type) and with e-document integrators: adapters, mapping, reconciliation | 40.3, 37.3, 21.3 | Synthesis |
| EA-40.5 | BOTH | Security, KVKK compliance, audit and operations for a small SaaS team; SLAs and support | 40.4, 15.5, 14.3 | Synthesis |
| EA-40.6 | BIZ | Go-to-market and economics of a vertical B2B SaaS in Turkey: pricing, onboarding/implementation as product, partner channels | 40.5, 16.4 | Synthesis |

### Unit 41 — Capstones
| ID | Tag | Title and scope | Prerequisites | Core sources |
|---|---|---|---|---|
| EA-41.1 | BOTH | Capstone 1: application landscape of an FMCG distributor (capability map → systems → ArchiMate view) | 5.3, Units 20–31 | Synthesis |
| EA-41.2 | BIZ | Capstone 2: build vs buy decision case with TCO and risk | 41.1, 17.2 | Synthesis (illustrative numbers) |
| EA-41.3 | TECH | Capstone 3: canonical data model for customer, product, order, invoice across ERP/SFA/WMS | 41.1, 10.5 | Synthesis |
| EA-41.4 | TECH | Capstone 4: integration design (APIs, events, e-documents, bank) with failure modes | 41.3, 37.3 | Synthesis |
| EA-41.5 | BOTH | Capstone 5: migration and cutover plan from legacy to new ERP/SFA; governance and change plan | 41.4, 18.6 | Synthesis |

## C. Benchmarks (URLs fetched 2026-10-26 with curl; "200" = HTTP 200; title matched where stated)
**Verified to exist (course/certification page reached):**
- MIT OCW 15.571 *Generating Business Value from Information Technology* (Spring 2009) — https://ocw.mit.edu/courses/15-571-generating-business-value-from-information-technology-spring-2009/ (200, title matched) → Units 3, 17.
- MIT OCW 15.565J *Integrating eSystems & Global Information Systems* (Spring 2002) — https://ocw.mit.edu/courses/15-565j-integrating-esystems-global-information-systems-spring-2002/ (200, title matched) → Units 10–11.
- MIT OCW 15.561 *Information Technology Essentials* — https://ocw.mit.edu/courses/15-561-information-technology-essentials-spring-2005/ (200) → Units 1, 7, 16.
- MIT OCW 15.566 *IT as an Integrating Force in Manufacturing* — https://ocw.mit.edu/courses/15-566-information-technology-as-an-integrating-force-in-manufacturing-spring-2003/ (200) → Units 20, 32.
- MIT OCW 6.033 *Computer System Engineering* (Spring 2018) — https://ocw.mit.edu/courses/6-033-computer-system-engineering-spring-2018/ (200) → Units 12–14.
- MIT OCW 6.5660 *Computer Systems Security* (Spring 2024) — https://ocw.mit.edu/courses/6-5660-computer-systems-security-spring-2024/ (200) and 6.858 (Fall 2014) → Unit 15.
- MIT OCW 6.830 *Database Systems* — https://ocw.mit.edu/courses/6-830-database-systems-fall-2010/ (200) → Units 7, 9.
- MIT OCW 15.763J *Manufacturing System and Supply Chain Design* — https://ocw.mit.edu/courses/15-763j-manufacturing-system-and-supply-chain-design-spring-2005/ (200); 15.762J *Supply Chain Planning* (200) → Units 29–32.
- CMU 17-214 *Principles of Software Construction* — https://cmu-17-214.github.io/ (200) → Units 12–13; UC Berkeley CS 169 *Software Engineering* — https://cs169.org/ (200) → Units 14, 19.
- Boğaziçi University Department of Management Information Systems — https://mis.bogazici.edu.tr/ (200, title matched) → Parts I–VIII overall. METU Informatics Institute — https://ii.metu.edu.tr/ (200; the IS programme sub-page I tried returned 404, so the IS programme's course list was **not** inspected). İTÜ — https://www.itu.edu.tr/ (200; no specific programme page inspected).
- AIS/ACM **IS2020** model curriculum (PDF) — https://www.acm.org/binaries/content/assets/education/curricula-recommendations/is2020.pdf (200) → competency areas mapped in §D. ACM/IEEE **SE2014** — https://www.acm.org/binaries/content/assets/education/se2014.pdf (200). ACM/IEEE/AAAI **CS2023** — https://csed.acm.org/ (200).
- ASCM **CPIM** — https://www.ascm.org/learning-development/certifications-credentials/cpim/ (200); **CSCP** — …/cscp/ (200) → Units 20, 29–31.
- ISACA **CISA** — https://www.isaca.org/credentialing/cisa (200); **COBIT** — https://www.isaca.org/resources/cobit (200) → Unit 6, 36.1.
- The Open Group **TOGAF** — https://www.opengroup.org/togaf (200); **ArchiMate** — https://www.opengroup.org/archimate-forum/archimate-overview (200) → Unit 5.
- IIBA **CBAP/BABOK** — https://www.iiba.org/business-analysis-certifications/cbap/ (200) → 17.3.
- DAMA **CDMP** — https://www.dama.org/cpages/cdmp-information (200) → Unit 8, 6.5.
- AXELOS **ITIL 4** — https://www.axelos.com/certifications/itil-service-management (200) → 6.2, 36.2.
- OMG **BPMN 2.0.2** — https://www.omg.org/spec/BPMN/2.0.2/ (200) → Unit 4.

**Not verified (page blocked or not found):** PMI PMP page (403 to automated fetch; existence not in doubt, content not inspected); SAP University Alliances (403; curriculum not inspected — the ERP cycle lessons follow Magal & Word, a textbook used in SAP-UA-style courses, but that link is not claimed); ISO 27001 page (403); GS1 (403); GİB e-belge portal and gib.gov.tr (connection timed out from the box — likely network/geo restriction); MIT 15.575/15.567 (*Economics of Information*) — the URLs I tried returned 404, so not claimed; a Stanford "software architecture" course page (404 at the URL tried; not claimed); Gartner/Forrester taxonomies (paywalled; used only as non-academic context in EA-1.5, never as a source of fact).

## D. Coverage-gap check (benchmark domain → lessons)
| Benchmark domain (source) | Where covered |
|---|---|
| IS foundations, IS in organisations, IS strategy (IS2020; MIT 15.571; Boğaziçi MIS) | Units 1–3 |
| Business process management and modelling (IS2020; BPMN; BABOK) | Unit 4, 17.3 |
| Enterprise architecture (TOGAF, ArchiMate; IS2020) | Unit 5 |
| IT governance, audit, controls (COBIT, CISA), service management (ITIL 4) | Unit 6, 36.1–36.2 |
| Data and information management (DAMA-DMBOK/CDMP; MIT 6.830; IS2020) | Units 7–9 |
| Integration, APIs, B2B (MIT 15.565J; EIP) | Units 10–11, 37 |
| Software architecture and design (CMU 17-214; SE2014; CS2023 SE/SDF) | Units 12–14 |
| Security, identity, privacy (MIT 6.5660; CS2023 security; CISA; ISO 27001) | Unit 15 |
| Cloud and SaaS (CS2023 parallel/distributed; NIST) | Unit 16 |
| IS acquisition, project and change management (IS2020; PMI; BABOK) | Units 17–19 |
| ERP cycles, MRP/MRP II (CPIM; MIT 15.566) | Units 20–22 |
| Planning and control, budgeting, EPM | Unit 23 (theory delegated to ECO-39.4) |
| Treasury, banking, payments | Units 24, 38 |
| CRM, SFA, commerce, pricing | Units 25–28 (sales theory delegated to FMCG Units 8, 13) |
| Supply chain planning and execution (CSCP; MIT 15.762J/15.763J) | Units 29–31 (inventory theory delegated to FMCG Unit 11) |
| Manufacturing, quality, PLM, EAM | Unit 32 |
| HCM/payroll, procurement, ECM, GRC, ITSM, PPM | Units 33–36 |
| Turkish regulatory systems (e-belge, KVKK, SGK, payments) | 15.5, 33.2, Units 37–38 (tax law delegated to ECO Unit 43) |
| Emerging: low-code, RPA, AI/LLMs | Unit 39 |
| Practice: design and build (IS2020 capstone; SE2014 project) | Units 40–41 |
**Known thin spots (honest gaps):** quantum/blockchain are deliberately excluded (no enterprise evidence base worth a lesson; can be added on request); public-sector/e-government systems beyond EKAP and e-belge are only touched; industry-specific vertical systems (banking core, insurance, healthcare, telecom billing) are out of scope except where they meet a distributor (bank connectivity, payments); operations-research depth for VRP/APS is concept-level only; Unit 32 (manufacturing) is lighter than an industrial-engineering programme because his domain is distribution.

## E. Unverified / to verify before use
- **Standards and regulators, pages not fetched or blocked:** GİB e-belge portal and UBL-TR technical guides, özel entegratör list, e-fatura/e-arşiv/e-irsaliye obligation thresholds (37.x, 11.5, 26.5, 31.3); ÖKC rules (28.3); TCMB FAST page (URL tried returned 404; 38.1); BKM GEÇİT page (38.2); İYS (25.4); EKAP (34.2); Law 5070 text (35.2); BDDK cloud/outsourcing rules (16.5); GDPR text URL (15.5); ISO 27001/9001/22000/55000/15489, ISA-95/IEC 62264, ISO 20022, PCI DSS, OASIS UBL 2.1, GS1 General Specifications/EANCOM, COSO 2013, FinOps Foundation, Agile Manifesto, gRPC/GraphQL/OpenAPI specs, PostgreSQL RLS docs, TOGAF Series Guides, Fowler bliki CQRS page.
- **Articles without DOIs (exist, but no DOI to resolve):** Gorry & Scott Morton 1971 (SMR); Porter & Millar 1985, Hammer 1990, Davenport 1998, Carr 2003, Kotter 1995, Kaplan & Norton 1992 (HBR); Conway 1968 (Datamation).
- **Vendor documentation** (SAP, Oracle, Microsoft, Salesforce, ServiceNow, Anaplan, Logo, Mikro, Nebim, Canias): only logo.com.tr, mikro.com.tr and Odoo docs returned 200; sap.com returned 403. Market-share or ranking claims will not be made without a citable source.
- **Not found and therefore not used:** a DOI for Ross & Vitale under the title "The ERP journey" (the verified item is Ross & Vitale 2000, "The ERP Revolution: Surviving vs. Thriving", ISF, doi:10.1023/A:1026500224101); one DOI I first tried for Holland & Light resolved to a different IEEE Software paper and one for Gattiker & Goodhue to a different MISQ paper; both were replaced by the correct DOIs found by Crossref search (10.1109/52.765784, 10.2307/25148695). The DOI first assumed for Markus et al. 2000 resolved to Parr & Shanks 2000 (kept, under Parr & Shanks, in 18.5); Markus et al. is doi:10.1080/02683960010008944.
