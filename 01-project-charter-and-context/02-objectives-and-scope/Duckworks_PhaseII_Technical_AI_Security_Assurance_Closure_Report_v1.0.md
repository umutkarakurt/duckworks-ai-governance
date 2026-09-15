# Project W.I.N.G. — Phase II Technical AI Security Assurance Closure Report

**Document ID:** DW-WING-SEC-CLOSE-01  
**Version:** 1.0  
**Effective date:** 15 September 2026  
**Project phase:** Phase II — Technical AI Security Engineering & Adversarial Validation  
**Owner:** Eleanor Duckford — AI Governance Lead  
**Security owner:** Cassandra Duckley — Chief Information Security Officer  
**Technical owner:** Dr. Ada Duckfield — Head of Data & AI  
**Closure status:** **CLOSED — first-wave synthetic / commit-bound technical-assurance build complete**  
**Residual evidence status:** **OPEN — production / production-equivalent effectiveness not established**

> Closure is a project-scope decision. It does not close system risks, internal-audit findings, legal questions, governance gates or production-evidence gaps.

## 1. Closure decision

The first-wave Phase II technical-security workstream is closed as **complete for portfolio publication and interview evaluation**.

The workstream achieved its intended portfolio purpose:

- selected governance risks were translated into technical system boundaries;
- five different AI system patterns received architecture/threat-model/validation chains;
- deliberately weak conditions were reproduced;
- hardening was implemented in controlled synthetic labs;
- identical tests were rerun;
- evidence was made machine-readable;
- detector/control signals were assessed separately from prevention;
- results were reproduced against exact GitHub commits;
- canonical evidence identifiers were allocated; and
- evidence was reconciled back into existing Duckworks controls, risks, assumptions, findings and governance positions without automatic maturity inflation.

No additional system-specific synthetic campaign is required for Phase II closure.

## 2. Original Phase II objectives — closure assessment

The original Technical AI & Cybersecurity Engineering Scope Addendum defined ten Phase II objectives.

| Original objective | Closure assessment | Evidence |
|---|---|---|
| 1. Define security architecture, assets, identities, data flows, trust boundaries and dependencies | **Complete for selected systems** | system-specific architectures for PondGPT, WingInspect, QuackBot, DuckDesign and FeatherForecast |
| 2. Distinguish conventional cyber threats from AI-specific attack mechanisms | **Complete** | system threat models combine authorization/API/supply-chain/access controls with prompt injection, RAG poisoning, adversarial CV, generated-code risk, poisoning/drift and related AI mechanisms |
| 3. Perform structured threat modelling using realistic attacker/failure objectives | **Complete** | five system-specific threat models and attack/failure paths |
| 4. Convert threats into explicit testable security requirements | **Complete** | system requirements and canonical campaign assertions |
| 5. Implement selected controls in a synthetic / controlled lab | **Complete** | five deterministic labs with vulnerable and hardened profiles |
| 6. Execute controlled adversarial tests against weak and remediated states | **Complete** | 52 canonical cases, executed in weak and hardened profiles |
| 7. Retain reproducible technical evidence | **Complete at synthetic / commit-bound level** | JSON/JSONL evidence, logs, hashes, reports, CI artifacts, evidence IDs |
| 8. Design detections / incident-response signals | **Complete for defined synthetic events** | system detection/control-signal validation reports |
| 9. Connect technical findings to existing risk/control architecture | **Complete** | canonical reconciliation records and overlays reuse existing risk/control IDs |
| 10. Preserve synthetic-versus-production evidence boundary | **Complete and explicitly enforced** | false claim flags, evidence-boundary sections, unchanged risk/gate/finding decisions unless separately justified |

**Closure conclusion:** all ten objectives are satisfied at the level authorized by the Phase II scope.

## 3. First-wave system completion

| Order | System | Differentiated assurance objective | Completion |
|---:|---|---|---|
| 1 | AI-006 PondGPT | Internal RAG, prompt injection, corpus poisoning, authorization/context boundary | **Closed / reconciled** |
| 2 | AI-004 WingInspect Vision | Adversarial computer vision, robustness containment, human release authority | **Closed / reconciled** |
| 3 | AI-002 QuackBot | Internet-facing RAG/API, session/authorization, customer-data and escalation boundaries | **Closed / reconciled** |
| 4 | AI-001 DuckDesign AI | Generated code, engineering data, dependencies, provenance, tool privilege and safety/approval boundaries | **Closed / reconciled** |
| 5 | AI-003 FeatherForecast | Forecast data integrity, poisoning/backfill, skew/drift, approval, access and operational resilience | **Closed / reconciled** |

“Closed / reconciled” means the first-wave synthetic technical increment is complete. It does not mean the system is production-approved or risk-accepted.

## 4. Consolidated assurance evidence

At closure, the programme contains:

- 5 system-specific technical-security architectures;
- 5 system-specific threat models;
- 5 validation-plan/lab chains;
- 52 canonical campaign cases;
- 104 weak/hardened case executions;
- 52 deliberately seeded unsafe outcomes reproduced;
- 52 hardened PASS outcomes;
- 40 supplemental automated unit tests;
- commit-bound replay for all five selected systems;
- detection/control-signal validation for all five systems;
- 33 canonical technical-validation evidence records; and
- governance reconciliation for every completed increment.

## 5. Scope acceptance criteria

The original scope addendum's first-increment acceptance criteria are generalized below for programme closure.

| Acceptance criterion | Closure result |
|---|---|
| Architecture separates verified portfolio facts from design assumptions | **Met** |
| Security-relevant data flows / trust boundaries are identifiable | **Met** |
| Threat models include conventional cyber and AI-specific attack/failure paths | **Met** |
| Material technical threats have testable requirements or explicit gaps | **Met** |
| Existing risk/control IDs are reused where applicable | **Met** |
| Technical requirements are not falsely represented as production controls | **Met** |
| Reproducible technical test suites exist | **Met** |
| Intentionally vulnerable conditions are demonstrated, remediated and retested | **Met** |
| Telemetry/detection is separately evaluated | **Met** |
| Raw evidence is traceable to stable evidence identifiers | **Met** |
| Synthetic evidence is not represented as production effectiveness | **Met** |
| External/real third-party systems are not attacked | **Met** |
| Limitations and unresolved risks remain visible | **Met** |

## 6. Mandatory legal requirements

This closure report creates **no new legal requirement** and makes no new determination of compliance.

System-specific applicability analyses remain controlling for legal questions.

The technical programme must not be used to infer:

- EU AI Act high-risk classification where not separately established;
- GDPR compliance;
- NIS2 compliance;
- Cyber Resilience Act applicability/compliance;
- product/machinery conformity;
- trade-secret status;
- contractual supplier compliance; or
- any other legal conclusion not separately supported.

## 7. Standards / framework guidance

Phase II is informed by the project's adopted standards/framework references and public technical guidance, including ISO/IEC 27001, ISO/IEC 42001, NIST CSF 2.0, NIST AI RMF and system-specific technical references.

The existence of architecture, tests, evidence or mappings does not itself establish:

- ISO certification;
- ISO conformity;
- regulatory compliance; or
- independent assurance.

## 8. Recommended organizational practices established by Phase II

The programme establishes the following reusable Duckworks practices:

1. define the system boundary before testing;
2. write security invariants that do not depend on model cooperation;
3. test deliberately weak conditions before hardening;
4. rerun identical cases after remediation;
5. use machine-readable evidence;
6. separate prevention from detection;
7. bind evidence to exact repository state;
8. assign stable evidence identifiers only after commit-bound replay;
9. reconcile technical evidence to existing governance structures;
10. prevent test PASS from automatically changing risk/gate/finding/assumption status;
11. preserve known-good rollback/fail-safe behavior where relevant; and
12. make future work trigger-driven rather than artifact-count-driven.

These are organizational practices, not mandatory external requirements.

## 9. Open items intentionally carried forward

### 9.1 Production effectiveness

No Phase II technical increment reaches defined-period production operating effectiveness.

This is the largest evidence gap and is intentionally visible.

### 9.2 Internal-audit findings

The following remain open:

- `IAF-2026-002` — DuckDesign Competent Engineer Approval;
- `IAF-2026-003` — FeatherForecast Human Planning Approval & Override.

Their synthetic technical mechanisms are demonstrated, but their production or production-equivalent operating populations are not.

### 9.3 System-specific gates

Phase II closure does not change existing governance positions, including:

- DuckDesign — Restricted Pilot only;
- QuackBot — Pre-Production / Production Blocked;
- FeatherForecast — Continue with monitoring;
- WingInspect — Restricted pilot only; and
- PondGPT — Restricted pilot only.

### 9.4 Supplier/platform assurance

Synthetic provider/platform boundaries do not establish actual supplier:

- security;
- architecture;
- contract operation;
- retention behavior;
- subprocessor posture;
- hosting controls; or
- incident performance.

### 9.5 Independent assurance

No broad claim of independent technical assurance is created by Phase II closure.

## 10. Residual technical coverage gaps

The first-wave programme is deliberately not exhaustive.

Potential future technical scope includes, where justified:

- AI-007 shadow-GenAI discovery / endpoint / network containment;
- model extraction / stealing;
- membership inference / model inversion;
- multi-agent trust;
- autonomous external-action safety;
- production MLOps/cloud/IaC hardening;
- runtime/container/GPU isolation;
- cryptographic model/artifact signing in a real pipeline;
- full container/software-composition assurance;
- authorized production red-team exercises; and
- real performance/safety evaluation.

These are **future candidates**, not Phase II closure blockers.

## 11. Closure criteria for reopening the workstream

Phase II technical work should be reopened or extended when one of the following occurs:

- a new AI system introduces a materially new threat class;
- a selected system undergoes material architecture/model/provider/data/tool/use change;
- production or production-equivalent evidence becomes available;
- an open audit finding requires technical validation;
- an incident/control failure creates a new hypothesis;
- a regulatory classification materially changes the assurance objective;
- evaluator/hiring feedback identifies a genuine technical credibility gap; or
- an independent reviewer requests additional evidence.

“More documents” by itself is not a reopening trigger.

## 12. Final closure position

**Phase II first-wave technical-assurance build: CLOSED.**

**Synthetic / commit-bound technical evidence: COMPLETE for selected first-wave systems.**

**Production operating effectiveness: OPEN / NOT ESTABLISHED.**

**Independent assurance: NOT ESTABLISHED.**

**Open audit findings: PRESERVED.**

**System governance gates: UNCHANGED unless separately decided.**

The next portfolio-development decision should be based on evidence value, not artifact volume.
