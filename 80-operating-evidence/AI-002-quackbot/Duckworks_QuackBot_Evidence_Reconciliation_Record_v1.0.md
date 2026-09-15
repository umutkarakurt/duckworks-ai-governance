# AI-002 QuackBot — Technical Evidence Reconciliation Record

**Project:** Project W.I.N.G. — Phase II Technical AI Security Engineering & Adversarial Validation  
**Document ID:** DW-AI002-REC-SEC-01  
**Version:** 1.0  
**Effective date:** 15 September 2026  
**System:** AI-002 — QuackBot  
**Business owner:** Clara Duckley — Director Customer Operations  
**AI/ML owner:** Dr. Ada Duckfield — Head of Data & AI  
**Security owner:** Cassandra Duckley — Chief Information Security Officer  
**Governance owner:** Eleanor Duckford — AI Governance Lead  
**Privacy reviewer:** Delia Duckham — Data Protection Officer  
**Legal reviewer:** Amelia Duckett — General Counsel  
**Current lifecycle gate:** **Pre-Production / Production Blocked**  
**Evidence classification:** Fictional / synthetic / non-production  
**Reconciliation status:** First QuackBot Phase II validation increment reconciled

> **Decision boundary:** This record reconciles synthetic technical-security and interaction-disclosure evidence into the Duckworks governance evidence architecture. It does not establish production API/RAG security, customer-data protection, prompt-injection immunity, provider compliance, legal compliance, production operating effectiveness, residual-risk reduction, or deployment readiness.

## 1. Reconciliation trigger

GitHub Actions **Evidence reproducibility run #147** (`34946047428`) completed successfully against commit:

`25525cc2c09c6b6557ddb9e7706fdaf81ce1796f`

The QuackBot step:

- executed under Python `3.12.14`;
- regenerated evidence from the committed lab;
- reproduced **12/12 deliberately vulnerable failures**;
- returned **12/12 hardened PASS**;
- passed **8/8 unit tests**;
- passed the QuackBot semantic verifier;
- passed `QB-COMP-001`;
- verified `source_commit == GITHUB_SHA`;
- retained `production_effectiveness_claim=false`;
- retained `risk_score_change_authorized=false`;
- retained `production_gate_change_authorized=false`;
- retained `evidence_id_allocation_authorized=false`; and
- uploaded a retained QuackBot evidence artifact.

| Field | Canonical value |
|---|---|
| Commit | `25525cc2c09c6b6557ddb9e7706fdaf81ce1796f` |
| Workflow run | `#147` / `34946047428` |
| Job ID | `104305566534` |
| Python | `3.12.14` |
| Artifact | `quackbot-security-evidence-25525cc2c09c6b6557ddb9e7706fdaf81ce1796f` |
| Artifact ID | `10387591380` |
| Artifact digest | `sha256:a4f50c18553c5996e118b26fedbb4a7e976db703443f7516ec146d673e974391` |
| Artifact retention expiry | `15 October 2026` |

## 2. Source classification

### 2.1 Mandatory legal requirements

This reconciliation makes no new legal-compliance conclusion.

The separate QuackBot applicability addendum identifies GDPR applicability where personal-data processing is in scope and EU AI Act Article 50 direct-interaction transparency as a QuackBot-specific mandatory-law applicability item, subject to final legal-role/exception analysis. NIS2 remains scope/national-law dependent and CRA applicability remains unestablished.

`QB-COMP-001` demonstrates only that the **synthetic target interaction flow** contains the AI-interaction disclosure design requirement before or at first interaction. It does not establish full Article 50 compliance.

QuackBot remains **not classified as an EU AI Act high-risk AI system** by this portfolio evidence.

### 2.2 Standards / framework guidance

The technical design and validation are informed by the existing Duckworks baseline, including ISO/IEC 27001, ISO/IEC 42001, NIST CSF, NIST AI RMF, NIST AI 600-1, NIST SP 800-218A, ENISA, NCSC secure-AI-development guidance, OWASP GenAI Security, OWASP API Security and MITRE ATLAS.

These sources support test/control structure. They do not independently establish compliance, conformity or effectiveness.

### 2.3 Recommended organizational practices

The following are Duckworks portfolio practices: system boundaries enforced outside model refusal behavior; vulnerable-versus-hardened replay; deterministic synthetic identities/data/canaries; object authorization before private retrieval; RAG source provenance/integrity validation; safe abstention/escalation for unsupported material guidance; provider/log minimization; version/change-triggered regression; source-commit binding; retained evidence artifacts; and no automatic risk/gate change from synthetic PASS results.

### 2.4 Project assumptions

`ASM-010 — QuackBot escalation` remains open.

`ASM-026 — QuackBot vendor architecture` remains open.

The lab validates a target synthetic design only; it does not establish actual escalation SLA operation, production provider architecture, provider retention/no-training terms, or production customer-data flows.

## 3. New stable evidence IDs

The following IDs are authoritative for the first AI-002 Phase II validation increment pending the next consolidated master evidence-index release.

| Evidence ID | Artifact | Evidence state | Primary control linkage | Primary risk linkage |
|---|---|---|---|---|
| `EV-AI002-001` | QuackBot Public-Facing RAG/API Technical Security Validation Plan v1.0 | Designed | QB-01–QB-06 | AI-002-R01; R02; R03 |
| `EV-AI002-002` | Executable QuackBot Lab v0.1.0 | Synthetic technical implementation demonstrated | QB-01–QB-06 | AI-002-R01; R02; R03 |
| `EV-AI002-003` | Baseline Findings and Remediation v1.0 | Synthetic failure detection / remediation demonstrated | QB-01–QB-06 | AI-002-R01; R02; R03 |
| `EV-AI002-004` | Hardened Campaign + Technical Security Test Report v1.1 | Synthetic operation tested | QB-01–QB-06 | AI-002-R01; R02; R03 |
| `EV-AI002-005` | Detection and Control-Signal Validation v1.0 | Synthetic detection / control-signal validation demonstrated | QB-04; QB-05; QB-06; supporting QB-01–QB-03 | AI-002-R01; R02; R03 |
| `EV-AI002-006` | Commit-Bound GitHub Actions Replay + Retained Evidence Artifact | Synthetic commit-bound reproducibility demonstrated | QB-01–QB-06 | AI-002-R01; R02; R03 |
| `EV-AI002-007` | AI Interaction Disclosure Design Assertion v1.0 | Synthetic legal-design assertion demonstrated | Governance / interaction-transparency design | AI-002-R03 |

No prior `EV-AI002-*` IDs existed in the master evidence index.

## 4. Control reconciliation

### QB-01 — Curated RAG Source Allowlist

The lab demonstrates source approval/provenance/integrity behavior, including quarantine of an unapproved/integrity-failed source.

**Decision:** evidence maturity increases from design/status assertion to bounded synthetic technical implementation, failure/remediation, operation testing and commit-bound reproducibility.

**Not established:** production corpus governance, real ingestion operation, actual source-owner approval, sustained integrity, stale-content management.

### QB-02 — Grounding, Citation & Abstention Rules

The lab demonstrates that unsupported material guidance can abstain/escalate and that fabricated citation behavior is rejected in the hardened case.

**Decision:** synthetic implementation/operation demonstrated.

**Not established:** production answer quality, citation correctness over real corpora, real customer safety/warranty outcomes.

### QB-03 — Human Escalation SLA

`QBSEC-T007` demonstrates a correlated synthetic escalation record when grounding is insufficient.

**Decision:** synthetic escalation **trigger/handoff behavior** demonstrated.

**Important limit:** the lab does **not** demonstrate SLA timing, staffing, completion, quality or production follow-through. The historical source status remains Partially implemented.

### QB-04 — Prompt Injection & RAG Adversarial Testing

The twelve-case campaign directly implements the planned adversarial-testing capability and replays direct/indirect injection and related RAG/API abuse scenarios.

**Decision:** synthetic technical implementation, operation testing and commit-bound reproducibility demonstrated.

The historical source label `Planned` should remain traceable until the authoritative control-library source is separately revised.

### QB-05 — Least-Privilege Retrieval & Tool Boundaries

The lab demonstrates anonymous/public versus private retrieval separation, server-side cross-customer object authorization, session isolation, tool/egress denial by default, and provider-context minimization.

**Decision:** bounded synthetic implementation/operation and commit-bound replay demonstrated.

**Not established:** real authentication/session/object authorization, actual connector/tool inventory, real egress enforcement.

### QB-06 — GenAI Security & Harm Monitoring

The campaign generates structured synthetic control signals for injection, provenance, authorization, sessions, grounding/escalation, output handling, tool/egress denial, resource limits, data minimization and version change.

**Decision:** bounded synthetic telemetry/detection behavior and commit-bound replay demonstrated.

**Not established:** production SIEM integration, responder workflow, alert quality, missed-event rates or sustained monitoring effectiveness.

### Supporting controls not upgraded

`AI-GOV-02` and `AI-TPR-01` receive supporting technical evidence only. The QuackBot lab does not demonstrate enterprise-wide change governance or actual supplier due diligence/contract operation. `AI-INC-01` receives no maturity upgrade from this campaign.

## 5. Risk reconciliation

### AI-002-R01 — Reliability & robustness

Recorded values remain:

- inherent: **Severity 4 × Likelihood 4 = 16 High**
- current residual: **Severity 4 × Likelihood 3 = 12 High**
- target residual: **Severity 4 × Likelihood 2 = 8 Moderate**

The new synthetic evidence supports bounded grounding, abstention/escalation and fail-safe response behavior.

**Score-support status:** **Provisional reduction — synthetic evidence only.**

No production answer-quality, customer-harm, complaint, warranty-dispute or outcome evidence exists.

### AI-002-R02 — Security & adversarial manipulation

Recorded values remain:

- inherent: **Severity 4 × Likelihood 4 = 16 High**
- current residual: **Severity 4 × Likelihood 3 = 12 High**
- target residual: **Severity 4 × Likelihood 2 = 8 Moderate**

The new technical campaign is directly relevant to this risk and demonstrates bounded synthetic authorization, RAG-integrity, injection, session, output, tool/egress, resource, data-minimization and change controls.

**Score-support status:** **Provisional reduction — synthetic evidence only.**

No production attack resistance, customer-data isolation, provider security or incident outcome is established.

### AI-002-R03 — Legal / compliance

Recorded values remain:

- inherent: **Severity 3 × Likelihood 4 = 12 High**
- current residual: **Severity 3 × Likelihood 3 = 9 Moderate**
- target residual: **Severity 3 × Likelihood 2 = 6 Moderate**

The lab demonstrates bounded synthetic handling of unsupported warranty/legal-sensitive guidance and separately demonstrates the AI-interaction disclosure design assertion.

**Score-support status:** **Provisional reduction — synthetic evidence only.**

No legal-content accuracy study, jurisdiction-specific consumer-law review, production notice implementation or legal-compliance conclusion is established.

## 6. Lifecycle decision

No score changes. No target residual is treated as achieved. No risk acceptance is created. No assumption is closed. No production-effectiveness conclusion is created. No production authorization is created.

The lifecycle gate remains:

> **PRE-PRODUCTION / PRODUCTION BLOCKED**

## 7. Production evidence still required

Before any broader deployment recommendation can rely on these controls, Duckworks would require at minimum:

1. version-bound production-equivalent authentication/session architecture;
2. real customer/object authorization tests and access evidence;
3. approved RAG source/provenance records and stale-content controls;
4. production-equivalent prompt/RAG regression evidence;
5. defined-period grounding/citation/abstention quality evidence;
6. real escalation SLA operation and completion records;
7. actual WAF/API/resource-limit configuration and outcomes;
8. provider contract/security/privacy/data-use/retention evidence;
9. production logging/redaction/SIEM/response evidence;
10. material-change/revalidation records;
11. actual Article 50 notice implementation review where applicable; and
12. competent governance/legal/privacy/security challenge before production approval.

## 8. Controlled-document precedence

Until the next consolidated portfolio baseline:

- `Duckworks_AI_Control_Evidence_Index_v1.8.md` remains the master base evidence index;
- the AI-004 reconciliation addendum remains authoritative for `EV-AI004-006–011`;
- `Duckworks_AI_Control_Evidence_Index_AI002_Reconciliation_v1.0.md` governs `EV-AI002-001–007`;
- `Duckworks_AI_Control_Framework_Report_v1.6.md` remains the master base control report, supplemented by the AI-002 control reconciliation addendum;
- `Duckworks_AI_Risk_Scenarios_v1.4.md` remains the master base risk register, supplemented by the AI-002 risk reconciliation addendum; and
- no score, assumption or lifecycle-gate field is changed by implication.
