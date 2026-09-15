# AI-001 DuckDesign AI — Technical Evidence Reconciliation Record

**Project:** Project W.I.N.G. — Phase II Technical AI Security Engineering & Adversarial Validation  
**Document ID:** DW-AI001-REC-SEC-01  
**Version:** 1.0  
**Effective date:** 15 September 2026  
**System:** AI-001 — DuckDesign AI  
**Business owner:** Felix Duckson — VP Product & Engineering  
**AI/ML owner:** Dr. Ada Duckfield — Head of Data & AI  
**Security owner:** Cassandra Duckley — Chief Information Security Officer  
**Product-safety challenger:** Quentin Duckwell — Director Product Safety & Quality  
**Governance owner:** Eleanor Duckford — AI Governance Lead  
**Current lifecycle gate:** **Restricted Pilot only**  
**Evidence classification:** Fictional / synthetic / non-production  
**Reconciliation status:** First DuckDesign Phase II executable-validation increment reconciled

> **Decision boundary:** This record reconciles synthetic technical-security evidence into the Duckworks governance evidence architecture. It does not establish production generated-code security, engineering-data confidentiality, dependency/build integrity, product safety, machinery/product conformity, supplier compliance, operating effectiveness, residual-risk reduction, audit-finding closure, or broader deployment readiness.

## 1. Reconciliation trigger

GitHub Actions **Evidence reproducibility run #166** (`34961107816`) completed successfully against commit:

`1c1fd170347dff466eb9d4a670e4355905119be2`

The DuckDesign step:

- executed under Python `3.12.14`;
- regenerated evidence from the committed lab;
- reproduced **12/12 deliberately vulnerable failures**;
- returned **12/12 hardened PASS**;
- passed **10/10 unit tests**;
- passed the DuckDesign semantic verifier;
- verified `source_commit == GITHUB_SHA`;
- retained `production_effectiveness_claim=false`;
- retained `product_safety_claim=false`;
- retained `legal_compliance_claim=false`;
- retained `risk_score_change_authorized=false`;
- retained `pilot_gate_change_authorized=false`;
- retained `evidence_id_allocation_authorized=false`;
- retained `iaf_2026_002_closure_authorized=false`;
- retained `assumption_closure_authorized=false`; and
- uploaded a retained DuckDesign evidence artifact.

| Field | Canonical value |
|---|---|
| Commit | `1c1fd170347dff466eb9d4a670e4355905119be2` |
| Workflow run | `#166` / `34961107816` |
| Job ID | `104354642158` |
| Python | `3.12.14` |
| Artifact | `duckdesign-security-evidence-1c1fd170347dff466eb9d4a670e4355905119be2` |
| Artifact ID | `10393790467` |
| Artifact digest | `sha256:fec7f78a7077d66890b9d00897eaf0bd21948a754912db77db89b7b1fa31edcb` |
| Artifact retention expiry | `15 October 2026` |
| Uploaded artifact files | `29` |
| Hash-manifest covered files | `28` excluding the manifest itself |

## 2. Source classification

### 2.1 Mandatory legal requirements

This reconciliation makes no new legal-compliance or product-conformity conclusion.

The separate DuckDesign applicability addendum preserves the following boundaries:

- DuckDesign is **not classified as a high-risk AI system** by this portfolio on the present advisory-design facts;
- EU AI Act classification must be reassessed if its intended role becomes a covered product/safety-component function;
- Machinery Regulation relevance remains product/context dependent;
- CRA applicability is not established for the internal assistant;
- Trade Secrets Directive relevance depends on whether engineering information meets the legal definition and national implementation;
- GDPR applies where personal data enter the workflow; and
- NIS2 remains organization/national-law dependent.

No `DDSEC-*` test is a legal-compliance, conformity-assessment, machinery-safety or product-safety test.

### 2.2 Standards / framework guidance

The technical design and validation are informed by the Duckworks baseline and DuckDesign addendum, including ISO/IEC 27001, ISO/IEC 42001, NIST CSF 2.0, NIST AI RMF, NIST AI 600-1, NIST SP 800-218/218A, NCSC secure-AI-development guidance, SLSA, OpenSSF, OWASP GenAI Security and MITRE ATLAS.

These sources support control/test structure. They do not independently establish compliance, conformity, certification or effectiveness.

### 2.3 Recommended organizational practices

The following are Duckworks portfolio practices:

- treat generated code, dependencies, imported instructions, tool commands and engineering claims as untrusted;
- isolate generated-code execution;
- deny arbitrary shell/file/network privilege;
- use approved dependency resolution and hash checks;
- separate engineering validation from model confidence;
- maintain an independent safety gate where required;
- bind engineer approval to the exact artifact hash reviewed;
- require provenance/SBOM completeness before promotion;
- trigger regression on material provider/model/config/tool/dependency changes;
- retain a known-good rollback state;
- bind evidence to a repository commit; and
- prevent synthetic PASS results from automatically changing risk, assumptions, audit findings or lifecycle gates.

### 2.4 Project assumptions

`ASM-007 — DuckDesign use`, `ASM-020 — Product scope`, and `ASM-025 — DuckDesign vendor architecture` remain open.

The lab validates a target synthetic design only. It does not establish actual generated-code use, production CAD/simulation tooling, real product/machinery classification, real AetherForge architecture, contractual data-use terms, or production engineering workflows.

## 3. New stable evidence IDs

The following IDs are authoritative for the first AI-001 Phase II executable-validation increment pending the next consolidated master evidence-index release.

| Evidence ID | Artifact | Evidence state | Primary control linkage | Primary risk linkage |
|---|---|---|---|---|
| `EV-AI001-001` | DuckDesign Technical Security Validation Plan v1.0 | Designed | DD-01–DD-05 | AI-001-R01; R02; R03 |
| `EV-AI001-002` | Executable DuckDesign Lab v0.1.0 | Synthetic technical implementation demonstrated | DD-01–DD-05 | AI-001-R01; R02; R03 |
| `EV-AI001-003` | Baseline Findings and Remediation v1.0 | Synthetic failure detection / remediation demonstrated | DD-01–DD-05 | AI-001-R01; R02; R03 |
| `EV-AI001-004` | Hardened Campaign + Technical Security Test Report v1.1 | Synthetic operation tested | DD-01–DD-05 | AI-001-R01; R02; R03 |
| `EV-AI001-005` | Detection and Control-Signal Validation v1.0 | Synthetic detection / control-signal validation demonstrated | DD-03; DD-04; DD-05; supporting DD-01; DD-02 | AI-001-R01; R02; R03 |
| `EV-AI001-006` | Commit-Bound GitHub Actions Replay + Retained Evidence Artifact | Synthetic commit-bound reproducibility demonstrated | DD-01–DD-05 | AI-001-R01; R02; R03 |
| `EV-AI001-007` | `DDSEC-T009` Exact-Artifact Engineer-Approval Binding Result | Synthetic approval-mechanism evidence demonstrated | DD-01; DD-05 | AI-001-R01; R03 |

No prior `EV-AI001-*` IDs existed in the master evidence index.

## 4. Control reconciliation

### DD-01 — Competent Engineer Approval

`DDSEC-T009` demonstrates exact-artifact approval binding in the synthetic lab: when the artifact changes after review, prior approval is invalidated and re-review is required.

**Decision:** bounded synthetic approval-mechanism evidence is now demonstrated and commit-bound.

**Important limit:** this does not establish defined-period production or production-equivalent operation of competent engineer approval. It does not provide the execution population, exceptions, metrics, owner review or independent validation required by `IAF-2026-002`.

The finding remains open.

### DD-02 — Independent Safety Validation Gate

`DDSEC-T008` demonstrates that required independent safety validation cannot be bypassed in the hardened synthetic workflow.

**Decision:** synthetic implementation/operation evidence is demonstrated.

**Not established:** real safety criteria, qualified validation, product-level safety outcomes, conformity assessment or production operation.

### DD-03 — Engineering Benchmark & Regression Suite

The campaign exercises generated-code containment, dependency/hash checks, engineering-value validation and material-change regression.

**Decision:** synthetic benchmark/regression mechanisms are implemented and exercised in the defined lab.

The historical source label `Planned` remains traceable until the authoritative control-library source is separately revised.

### DD-04 — Engineering Data Boundary & DLP

`DDSEC-T001` demonstrates defined engineering-IP/secret canaries absent from prohibited provider/log sinks in the hardened profile. `DDSEC-T002` demonstrates that imported engineering content cannot alter validation/tool authority.

**Decision:** bounded synthetic data-boundary and trust-boundary behavior is demonstrated.

**Not established:** production engineering-data classification, real DLP, real provider payloads/logs, or contractual provider controls.

### DD-05 — Design/Model Version Traceability

The campaign demonstrates dependency/hash integrity, exact-artifact approval binding, material-change detection, provenance/SBOM blocking and hash-verified rollback.

**Decision:** bounded synthetic version/integrity/provenance/rollback mechanisms are demonstrated and commit-bound.

**Not established:** real model/provider/tool/dependency/build/design traceability or sustained production operation.

### Supporting controls not upgraded

`AI-GOV-02`, `AI-TPR-01` and `AI-INC-01` receive supporting system-specific evidence only. The campaign does not demonstrate enterprise-wide change governance, actual AetherForge supplier governance or enterprise incident-response operation.

## 5. Risk reconciliation

### AI-001-R01 — Safety & physical harm

Recorded values remain:

- inherent: **Severity 5 × Likelihood 3 = 15 High**
- current residual: **Severity 5 × Likelihood 2 = 10 High**
- target residual: **Severity 4 × Likelihood 2 = 8 Moderate**

**Score-support status:** **Provisional reduction — synthetic evidence only.**

The new evidence supports bounded generated-code containment, engineering validation, independent safety-gate enforcement, approval integrity, version/change control and rollback. It does not establish product safety or real engineering outcomes.

### AI-001-R02 — Privacy & data governance / engineering confidentiality

Recorded values remain:

- inherent: **Severity 4 × Likelihood 3 = 12 High**
- current residual: **Severity 4 × Likelihood 2 = 8 Moderate**
- target residual: **Severity 4 × Likelihood 1 = 4 Low**

**Score-support status:** **Provisional reduction — synthetic evidence only.**

The new evidence supports bounded engineering-IP/secret minimization and provider/log boundary behavior. It does not establish actual AetherForge architecture/contract or production DLP/data-flow protection.

### AI-001-R03 — Reliability & robustness

Recorded values remain:

- inherent: **Severity 4 × Likelihood 4 = 16 High**
- current residual: **Severity 4 × Likelihood 2 = 8 Moderate**
- target residual: **Severity 4 × Likelihood 2 = 8 Moderate**

**Score-support status:** **Provisional reduction — synthetic evidence only.**

The new evidence supports bounded engineering-value validation, dependency/hash checks, change regression, provenance and approval integrity. It does not establish target residual achievement, real benchmark performance or production design outcomes.

## 6. Internal-audit finding

`IAF-2026-002 — Competent Engineer Approval implementation claim is unsupported` remains:

> **OPEN — MANAGEMENT RESPONSE REQUIRED**

The synthetic `DDSEC-T009` result narrows uncertainty about the technical approval mechanism, but the finding requires retrievable, version-bound implementation and operating evidence, including population/execution samples, exceptions, metrics, owner review and independent validation.

No closure is authorized.

## 7. Lifecycle decision

No score changes.

No target residual is treated as achieved.

No risk acceptance is created.

No assumption is closed.

No product-safety or conformity conclusion is created.

No audit finding is closed.

No broader-use authorization is created.

The lifecycle gate remains:

> **RESTRICTED PILOT ONLY**

## 8. Production / production-equivalent evidence still required

Before a broader-use recommendation can rely on these controls, Duckworks would require at minimum:

1. version-bound real or production-equivalent engineer-approval population and period;
2. exact artifact/version approval records, rejections, overrides and exceptions;
3. independently validated safety-gate criteria and execution records where required;
4. approved engineering benchmark/regression suite with real representative fixtures and failure outcomes;
5. real engineering-data classification/DLP/provider payload/log evidence;
6. actual AetherForge contract, retention, no-training, hosting/subprocessor and security evidence;
7. approved package/dependency source, lock/hash and build/provenance records;
8. actual sandbox/tool privilege and egress configuration plus allow/deny evidence;
9. model/provider/prompt/config/tool/dependency change/revalidation records;
10. known-good rollback exercises and incident linkage;
11. defined-period engineering/safety/outcome metrics; and
12. independent assurance and authorized risk-owner/governance review before any gate expansion.

## 9. Controlled-document precedence

Until the next consolidated portfolio baseline:

- `Duckworks_AI_Control_Evidence_Index_v1.8.md` remains the master base evidence index;
- the AI-004 reconciliation addendum remains authoritative for `EV-AI004-006–011`;
- the AI-002 reconciliation addendum remains authoritative for `EV-AI002-001–007`;
- `Duckworks_AI_Control_Evidence_Index_AI001_Reconciliation_v1.0.md` governs `EV-AI001-001–007`;
- `Duckworks_AI_Control_Framework_Report_v1.6.md` remains the master base control report, supplemented by the AI-001 control reconciliation addendum;
- `Duckworks_AI_Risk_Scenarios_v1.4.md` remains the master base risk register, supplemented by the AI-001 risk reconciliation addendum; and
- no score, assumption, audit-finding or lifecycle-gate field is changed by implication.
