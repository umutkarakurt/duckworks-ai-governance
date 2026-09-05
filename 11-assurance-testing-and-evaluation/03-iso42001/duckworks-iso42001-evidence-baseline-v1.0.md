# Duckworks — ISO/IEC 42001 Evidence Baseline

**Project:** W.I.N.G. — Workflows, Intelligence, Next-Generation Governance  
**Document ID:** DW-AIMS-EV-001  
**Version:** 1.0  
**Status:** Initial thematic mapping; proposed AIMS scope; review required  
**Maintainer:** AI Governance Lead, Eleanor Duckford (fictional role)  
**Proposed reviewer:** Chief Risk & Compliance Officer, Reginald Duckman  
**Approval:** Not recorded

Duckworks is fictional. This package assesses selected supplied portfolio documents and proposes the next evidence work. It does not demonstrate production operation, certification, independent assurance, or legal compliance. No signatures, approvals, test results, or organizational activities have been fabricated.

## 1. Executive assessment

The supplied baseline provides a documented organizational scenario, stakeholders, project boundaries, assessment method, acceptance criteria, and deliverables plan. Its strongest features are evidence-based control credit, separation of current and target residual risk, reassessment triggers, and separation of project acceptance from production approval.

The immediate priority is to connect those designs to inspectable execution records. A deliverables register marking an item “Complete” is a source assertion, not evidence that the referenced item was reviewed or its process operated. The supplied register also marks several foundational artifacts “Required” even though copies are available. Reconcile register status before using it as a management dashboard.

This is a **thematic evidence matrix**, not an exhaustive clause-by-clause assessment. Exact requirement and Annex A references remain unverified because the full standard was not supplied. No conformity percentage is calculated. Missing evidence means “not demonstrated in the reviewed source set,” not “absent from the entire portfolio.” The live GitHub repository and later DuckTalent execution artifacts were not inspected for this baseline.

## 2. Proposed AIMS overview

### Management-system boundary

Proposed scope: the governance of Duckworks' development, procurement, integration, and use of AI across engineering, manufacturing, customer operations, supply-chain planning, recruitment, and employee productivity. It includes intake, risk and impact assessment, treatment, decision gates, monitoring, change, incident handling, and retirement. Supplier dependencies remain subject to Duckworks oversight; suppliers' internal management systems are outside Duckworks' direct operational control.

This management-system boundary is distinct from the portfolio delivery boundary: the project demonstrates designs and synthetic exercises, while production deployment, real-data validation, certification, and formal conformity assessment remain outside the project scope (S03, section 3). The proposed AIMS scope does not establish that these organizational processes already operate.

Jurisdiction, sites, legal entities, outsourced interfaces, and system-specific developer/provider/user roles require confirmation before scope approval. EU/EEA operations remain an open project assumption (ASM-002). No additional geographic or legal facts are assumed here.

### Initial coverage and accountability

| Inventory coverage | Business responsibility from S11 | Boundary requiring evidence |
| --- | --- | --- |
| DuckDesign AI | VP Product & Engineering | Advisory output; competent engineering review |
| QuackBot | Director of Customer Operations | Customer-support boundaries and human escalation |
| FeatherForecast | Director of Supply Chain | Authorized approval of material commitments |
| WingInspect Vision | Director of Manufacturing | Qualified inspector retains final release authority |
| DuckTalent AI | Chief People Officer | Applicant recommendations; meaningful human decision authority |
| PondGPT | Head of IT & Cloud | Enterprise access, integrations, and information boundaries |
| Unregistered GenAI Usage | CISO / AI Governance Lead, per S12 AC-10 | Discovery and containment condition; decompose into individual use cases |

There are six named systems plus one aggregate inventory condition, not seven homogeneous systems. Inclusion does not mean approval. S12 records DuckTalent as “Do not deploy in current state”; this package does not alter that decision or other system gates.

### Management responsibilities and interfaces

The CEO sponsors the program. The CRCO chairs the AI Governance Committee. The AI Governance Lead maintains inventory and evidence coordination. Business owners own outcomes; technical owners supply implementation and monitoring evidence. Legal and privacy specialists provide domain review. Internal Audit assures independently and does not operate the controls it reviews (S11; S07 ASM-022).

| Existing process interface | Proposed AI-specific handoff | Record needed to demonstrate the handoff |
| --- | --- | --- |
| Information security | AI threats, access, logging and incident escalation | Security review tied to a system/version and gate |
| Privacy and HR | Applicant/employee impacts, human review, contestability | Domain assessment and unresolved conditions |
| Procurement | Provider changes, data use, obligations and exit | Supplier decision and tracked conditions |
| Engineering / change management | Material model, feature, data or purpose change | Change record and reassessment outcome |
| Enterprise risk | Residual risk and delegated decisions | Risk treatment and acceptance/rejection record |
| Internal Audit / management review | Findings, performance, resources and improvement | Workpapers, decisions and action follow-up |

These are recommended organizational practices based on project objectives, not verified integrations or ISO/IEC 27001 conformity mappings.

## 3. Evidence classification and mapping rules

- **Design documented:** reviewed text describes the relevant process or responsibility; adequacy and approval may remain unverified.
- **Partial design:** related text exists, but the theme needs further specification or the referenced artifact was not inspected.
- **Not evidenced:** no sufficient design artifact was identified in the selected source set.
- **Operation not demonstrated:** execution records have not been inspected. This applies to every row in the initial matrix.
- **Synthetic operation demonstrated:** reserved for a later reproducible exercise with inspectable inputs, outputs and decisions. It does not mean production effectiveness.

All matrix themes are **candidate standards mappings**. Their precise requirement references and completeness must be checked against an authorized current standard, including applicable amendments. The “next evidence” column is a project recommendation, not quoted ISO text. Legal obligations require a separate applicability analysis. Proposed owners are workflow assignments for this package, not records of their acceptance.

## 4. Initial requirements-theme-to-evidence matrix

**Common status for all rows:** exact ISO reference = pending verification; operation = not demonstrated. Source references resolve in section 7. Row IDs are local portfolio identifiers, not ISO clause numbers.

| ID / candidate theme | Reviewed evidence and locator | Design assessment | Proposed operating owner | Next evidence / acceptance condition |
| --- | --- | --- | --- | --- |
| M01 Organizational context and AIMS scope | S03 §§1–3; S10 profile; S07 ASM-001–004 | Partial design: project scope exists; AIMS boundary proposed here | CRCO | Reviewed scope identifying entities, sites, AI roles, interfaces and rationale; resolve ASM-002 |
| M02 Interested parties and their needs | S11 stakeholder and affected-group tables | Design documented; consultation execution unverified | AI Governance Lead | Needs-to-process mapping and one synthetic feedback record with resulting action |
| M03 Leadership, accountability and AI policy | S11 S-01–S-17; S13 DEL-13–14 | Partial design: responsibilities exist; policy and authority operation unreviewed | CRCO | Inspect policy/charter; record authority, resources, approval and communication evidence |
| M04 Risks and opportunities affecting the AIMS | S06 §§2.8, 2.13; S07 ASM-003, ASM-021 | Partial design: system risks dominate; AIMS process risks need explicit treatment | CRCO | Assess governance capacity, competence and evidence failure; record one improvement opportunity and treatment |
| M05 AI risk assessment | S14 §§8–11, 14; S12 AC-04–05 | Design documented; method approval and completed assessments unverified | Relevant AI System Owner, supported by Risk | Inspect one assessment tied to inventory/version, assumptions and supporting control evidence |
| M06 AI impact assessment | S06 §2.5; S03 §2.6; S13 DEL-12 | Partial design: expectations present; completed AIA not inspected | Relevant AI System Owner | Inspect DuckTalent impact assessment, affected groups, benefits/harms and response decisions |
| M07 Risk treatment and control applicability | S14 §§11–12; S13 DEL-15 | Partial design: treatment method exists; applicability record not evidenced | CRCO, with control owners | Verified Statement of Applicability and treatment links, inclusion/exclusion rationale and implementation evidence |
| M08 AI objectives and plans | S06 §§2–3; S12 AC-01–20 | Partial design: project outcomes exist; ongoing AIMS targets not established | AI Governance Lead | Define objective, metric, source, target, owner, cadence and response to missed target |
| M09 Resources, competence and awareness | S03 §2.9; S11 A-04–05; S13 DEL-19 | Partial design: competence expected; demonstration not inspected | Relevant Business Owner | Role competence criteria, synthetic assessment record and authorization limits |
| M10 Communication and documented information | S12 Q-01, Q-04; S06 §2.12 | Partial design: versioning and evidence expected; full information control not evidenced | AI Governance Lead | Evidence index with version, reviewer, access, retention basis, retrieval and supersession rules |
| M11 Operational planning and lifecycle gates | S12 §5 and AC-08–09; S13 DEL-09 | Partial design: gate conditions recorded; workflow execution unverified | Relevant AI System Owner | Inspect a gate decision linked to exact assessment/test versions and outstanding conditions |
| M12 AI data and technical lifecycle controls | S03 §§2.8, 2.12; S07 ASM-009, ASM-013 | Partial design: expectations and assumptions only | Head of Data & AI | Inspect dataset/model or service version, data checks, access evidence and validation limits |
| M13 Third-party dependencies | S06 §2.9; S11 S-15; S13 DEL-17 | Partial design: due-diligence expectations; completed review not inspected | Director of Procurement & Vendor Assurance | Synthetic supplier review with decision, unresolved conditions and change-notification trigger |
| M14 Performance monitoring and evaluation | S06 §§2.11, 2.14; S13 DEL-20–21 | Partial design: metrics categories; populated measurements unreviewed | Head of Data & AI with Business Owner | Defined test period, denominator, thresholds, measured results and management response |
| M15 Change and reassessment | S14 §13; S12 AC-18 | Design documented; change execution unverified | Relevant Technical Owner | One versioned change triggering reassessment, gate decision and evidence update |
| M16 Internal audit | S11 S-08; S13 DEL-23 “Future phase” | Partial design: independence defined; program/workpapers not inspected | Head of Internal Audit | Simulated plan, criteria, sampling, workpapers and findings; disclose self-review limits |
| M17 Management review | S11 governance forums; S06 §2.14 | Partial design: meetings/reporting expected; AIMS review record not inspected | CEO, coordinated by CRCO | Simulated review of performance, findings, changes and resources with decisions and action owners |
| M18 Nonconformity, corrective action and improvement | S13 DEL-18; S14 §13 | Partial design: incident/reassessment triggers; corrective-action cycle not evidenced | Relevant Process Owner | Finding, correction, root cause, recurrence prevention, effectiveness check and closure decision |

Incident handling does not automatically demonstrate a corrective-action process. Committee meetings do not automatically demonstrate management review. A generic control library does not automatically demonstrate a justified applicability decision.

## 5. Prioritized evidence action register

All actions are open. Sequence is recommended, not an approved schedule. P1 blocks a defensible detailed mapping or operating claim; P2 develops the management cycle. No externally imposed deadlines are invented.

| Action | Priority / related rows | Proposed owner | Concrete closure evidence |
| --- | --- | --- | --- |
| A01 Validate standard references | P1 / all | AI Governance Lead | Record edition/amendment basis; verify requirement references; expand themes into complete requirement rows; second-person mapping review where available |
| A02 Reconcile current artifacts | P1 / all | AI Governance Lead | Inspect latest relevant repository files; capture commit and paths; reconcile S13 statuses; retain old versus new assessment basis |
| A03 Confirm AIMS scope | P1 / M01–02 | CRCO | Scope review and recorded fictional decision; explicitly resolve or carry jurisdiction and interface assumptions |
| A04 Inspect DuckTalent evidence | P1 / M05–07, M11, M15 | Chief People Officer + Head of Data & AI | Linked assessment, control specification, code/configuration, synthetic dataset, failure log, blocked gate, remediation and retest |
| A05 Establish applicability rationale | P1 / M07 | CRCO | Verified control references, risk/impact links, rationale, owner, implementation status and evidence pointers |
| A06 Demonstrate management cycle | P2 / M14, M16–18 | CRCO coordinates; Internal Audit retains its assurance role | Synthetic audit finding, root-cause action, effectiveness check and management decision with open actions |
| A07 Define ongoing objectives and support | P2 / M08–10 | AI Governance Lead + Business Owners | Measurable AIMS objectives, competence evidence and document/evidence handling rules |
| A08 Resolve acceptance ambiguity | P1 / M05, M11 | CRCO + General Counsel | Reconcile S14 §12 exceptional Critical-risk acceptance with S12 AC-08; document that an exception cannot waive applicable law or missing required gates |

S14 also contains time-sensitive legal references and application dates. Their correctness was not checked in this ISO mapping task. They are not imported as legal conclusions; review them against primary legislation before relying on them for a release decision.

## 6. DuckTalent evidence collection specification

The prior project narrative describes a failed fairness test, blocked deployment gate, remediation and successful retest. Those files were not supplied for this review, so the events receive no operating-effectiveness credit here. S12 independently records the baseline “Do not deploy in current state” decision.

For A04, collect the following as one versioned evidence bundle:

| Evidence item | Minimum content | Acceptance check |
| --- | --- | --- |
| Risk and impact | Stable IDs; intended purpose; affected groups; assumptions; owner | Same system and purpose as the tested configuration |
| Control specification | Risk link; feature restrictions; metric; threshold; gate behavior | Threshold justified before interpreting results |
| Reproduction inputs | Code/configuration version; synthetic data; dependencies; run instructions | Another reviewer can reproduce the bounded exercise |
| Failure and gate | Run ID; observed/expected results; blocked status | Failure demonstrably prevents progression in the test workflow |
| Remediation and retest | Cause; exact change; new run; comparative result | Same relevant test coverage; explain any changed data or thresholds |
| Governance decision | Decision authority; reviewed evidence versions; remaining gaps | Passing test does not erase privacy, oversight, security or other unresolved conditions |
| Reassessment | Material change event; impacted evidence; renewed decision | A changed feature/model invalidates stale acceptance where applicable |

New evidence records should include: evidence ID, linked matrix/risk/control IDs, system, artifact path and version or commit, execution period, producer, reviewer, review outcome, limitations, and next review trigger. Hashes support file identity; they do not prove truth or effectiveness. Proposed IDs must be reconciled with existing IDs before adoption.

## 7. Reviewed source index

Source IDs below are local to this package. Original filenames identify the supplied baseline; locators identify sections or register rows, not live repository paths. No source content has been changed.

| Source ID | Supplied artifact | Use in this review |
| --- | --- | --- |
| S03 | Duckworks AI Governance Project — In-Scope and Out-of-Scope Items.md | Project boundaries, governance expectations, exclusions |
| S06 | Duckworks AI Governance Project — Project Objectives.md | Intended outcomes and evidence expectations |
| S07 | Duckworks_Project_Assumptions_Register_v1.0.docx | Assumptions and validation limits |
| S10 | Duckworks — Fictional Organization Profile.md | Organization, use cases, executive responsibilities |
| S11 | Duckworks_Project_Stakeholders_v1.0.docx | Owners, affected groups, forums and independence |
| S12 | Duckworks_Project_Acceptance_Criteria_v1.0.docx | Acceptance rules, system gates, evidence standards |
| S13 | Duckworks_Project_Required_Deliverables_v1.0.docx | Baseline delivery status and expected artifacts |
| S14 | Duckworks_AI_Risk_Classification_Assessment_Methodology_v1.0.docx | Risk method, treatment, evidence credit and reassessment |

The remaining supplied files, including the readiness PDF and diagram, were not used as evidence for this matrix. “Validated” in the assumptions register is a fictional baseline label; it does not establish real-world validation or verify every referenced artifact.

### Official standards sources

- [ISO/IEC 42001:2023 official overview](https://www.iso.org/standard/42001): confirms the AIMS purpose and lifecycle of establishment, implementation, maintenance and improvement.
- [ISO/IEC 42001 explained](https://www.iso.org/home/insights-news/resources/iso-42001-explained-what-it-is.html): supports high-level themes including context, leadership, policy, risk, lifecycle, evaluation and improvement; distinguishes the management standard from law.

These public pages were checked for this package. They are not a substitute for the normative text and do not substantiate an exhaustive clause mapping. The matrix is original project analysis, not reproduced standard text.

## 8. Repository integration and maintenance

Recommended destination: `10-assurance/iso42001/duckworks-iso42001-evidence-baseline-v1.0.md`, consistent with S13's proposed structure. Verify the actual repository layout before adding it. This task has not modified or published the repository.

Suggested README entry when placed at that location:

`[ISO/IEC 42001 evidence baseline](10-assurance/iso42001/duckworks-iso42001-evidence-baseline-v1.0.md) — Proposed AIMS scope, initial thematic evidence matrix, and prioritized evidence gaps. Fictional case study; no certification claim.`

Maintain the matrix when a referenced artifact changes, an exercise produces evidence, scope changes, or a mapping is verified. Preserve the prior assessment basis. A change from “operation not demonstrated” must identify the actual reviewed evidence and its limitations. Do not replace this with “compliant” merely because a document was added.

Step-one output is complete as a source-bounded baseline. Detailed normative mapping remains explicitly pending A01; demonstrated operation remains pending evidence inspection. The next implementation task is A02/A04: reconcile the current repository and connect one complete DuckTalent evidence trail before creating further policy documents.

### Source identity fingerprints

SHA-256 of the inspected local copies; these identify the baseline bytes only.

| Source | SHA-256 |
| --- | --- |
| S03 | `1ea4a0e98f4ee6cbfcf1593cf310774f7bda10149efcebe09c889e92ffcf4b4a` |
| S06 | `bbdc130899cb0629d501c86b3fd0be77a262aeabd754799eac024c226e29f30b` |
| S07 | `0459c8e33e6640e0b16cf147b724c5afc10b8326f6d76dfa9c4d63a9eb1507ed` |
| S10 | `90439e1a33ea6c6d14ce94090f26ba6cd3a05304b9af51dc9442c88a62ed9988` |
| S11 | `5517920bd55a077b55fe0e5476007bcf3a075d530a4fd72dde8bb707269fa907` |
| S12 | `37fdf715daade474fc74d08b679bbd4ceabb94d76b5fda5ed0939818b7724af7` |
| S13 | `923def50949b2003a1e0c2f6e3d28d37569dbc608fbc3736e70655e37894dc2d` |
| S14 | `31a0ef59d390d39fd049cb549db89416c8643ed5b0d1f4f03c0c88b7fbe09930` |
