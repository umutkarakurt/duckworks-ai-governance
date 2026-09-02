# Project W.I.N.G. — Operating Evidence Index

This register maps material AI risks to controls and the evidence available to demonstrate control design, implementation, operation, and effectiveness.

Synthetic portfolio evidence is explicitly distinguished from production operating evidence.

| Evidence ID | AI System | Risk | Control | Artifact | Evidence State | What It Demonstrates |
|---|---|---|---|---|---|---|
| EV-AI004-001 | AI-004 — WingInspect Vision | AI-004-R01 | WI-01 | Control Implementation Card | Designed | Control objective, owner, trigger, evidence requirements, and measurement approach |
| EV-AI004-002 | AI-004 — WingInspect Vision | AI-004-R01 | WI-01 | Synthetic Inspection Log | Synthetic execution demonstrated | Human decision workflow, override authority, timestamps, and final disposition trail |
| EV-AI004-003 | AI-004 — WingInspect Vision | AI-004-R01 | WI-01 | Human Release Gate Control Test | Synthetic operation tested | Control execution against the complete synthetic population |
| EV-AI004-004 | AI-004 — WingInspect Vision | AI-004-R01 | WI-01 | Production Inspection Records | Not available | Real-world operating evidence |
| EV-AI004-005 | AI-004 — WingInspect Vision | AI-004-R01 | WI-01 | Post-release Material Defect Trend | Not available | Outcome effectiveness / risk-reduction evidence |
| EV-AI005-001 | AI-005 — DuckTalent AI | AI-005-R01 | DT-01 / DT-02 | Control Implementation Card | Designed | Fairness-risk objective, owner, triggers, evidence, gate rule, metrics, and legal/evidence boundaries |
| EV-AI005-002 | AI-005 — DuckTalent AI | AI-005-R01 | DT-01 / DT-02 | Synthetic Applicant Fairness Test Dataset | Designed test input | Twenty-four synthetic applicants arranged as twelve matched pairs with approved job-related test features held equal within pairs |
| EV-AI005-003 | AI-005 — DuckTalent AI | AI-005-R01 | DT-02 | Executable Fairness & Adverse-Impact Test | Synthetic technical implementation demonstrated | Reproducible test logic for feature allow-list conformance, matched-pair analysis, disparity diagnostics, deployment gating, remediation, and retest |
| EV-AI005-004 | AI-005 — DuckTalent AI | AI-005-R01 | DT-02 | Fairness Test Results | Synthetic fairness execution demonstrated | Pre/post-remediation scores, shortlist outcomes, error types, and matched synthetic population results |
| EV-AI005-005 | AI-005 — DuckTalent AI | AI-005-R01 | DT-02 | Seeded Fairness / Proxy-Feature Exception | Synthetic failure detection / gate response demonstrated | Detection of the intentionally unapproved `Career_Gap_Months` penalty, measurable matched-pair effect, deployment block, remediation, and retest requirement |
| EV-AI005-006 | AI-005 — DuckTalent AI | AI-005-R01 | DT-02 | Fairness Control Test | Synthetic operation tested | Ten control assertions over the complete synthetic population and conclusion that DT-02 operated as designed within the portfolio scenario |
| EV-AI005-007 | AI-005 — DuckTalent AI | AI-005-R01 | DT-01 / DT-02 | Production Feature-Governance / Fairness Evidence | Not available | Real job-relevance approval, production feature inventory, lawful group-data method, representative validation, and actual model/version evidence |
| EV-AI005-008 | AI-005 — DuckTalent AI | AI-005-R01 | DT-02 / DT-07 | Real Applicant Outcome / Challenge Trend | Not available | Production fairness, contestability, error, complaint, and rights-impact outcome evidence |
| EV-AI005-009 | AI-005 — DuckTalent AI | AI-005-R01 | DT-01 / DT-02 / Governance Gate | Synthetic Pre-Deployment Governance Gate Decision Record | Synthetic lifecycle decision demonstrated | Risk, impact, rights/privacy, model-documentation and control-test evidence are consumed at a lifecycle gate; advancement to a real-applicant pilot is denied, blocking conditions are recorded, and a reassessment trigger is defined |
| EV-AI005-010 | AI-005 — DuckTalent AI | AI-005-R01 | Change / Monitoring | Synthetic Proposed Change Event `DT-CHG-001` | Synthetic material-change input | A proposed, unapproved feature/ranking configuration deliberately reintroduces `Career_Gap_Months` after prior remediation |
| EV-AI005-011 | AI-005 — DuckTalent AI | AI-005-R01 | DT-01 / DT-02 / Change Monitoring | Executable Change-Regression Check | Synthetic monitoring mechanism demonstrated | Canonical DT-02 allow-list and matched-pair dataset are reused to test the proposed change for unapproved features and recreated outcome effects |
| EV-AI005-012 | AI-005 — DuckTalent AI | AI-005-R01 | DT-01 / DT-02 / Reassessment Trigger | Change-Regression Result `DT-MON-001 / DT-TRG-001` | Synthetic reassessment trigger demonstrated | Seven monitoring assertions pass; the unapproved feature and recreated synthetic disparity are detected; the proposed configuration is rejected and `IR-001` is opened |
| EV-AI005-013 | AI-005 — DuckTalent AI | AI-005-R01 | Risk / Impact / Rights / Privacy / Model / Controls | Reassessment Record `IR-001` | Synthetic reassessment performed | Affected governance records are explicitly reopened; current Critical risk, DT-01/DT-02 status and DO NOT DEPLOY position are revalidated |
| EV-AI005-014 | AI-005 — DuckTalent AI | AI-005-R01 | Governance Gate / Change Control | Revised Governance Gate Decision | Synthetic revised lifecycle decision demonstrated | `DT-CHG-001` is rejected, the prior real-applicant block is preserved, and future material ranking/criteria/weight/feature changes are conditioned on version-diff and DT-02 regression evidence |
| EV-AI006-001 | AI-006 — PondGPT | AI-006-R01 | PG-01 / PG-02 | Control Implementation Card | Designed | Authorization-risk objective, owner, triggers, evidence, gate rule, and measurement approach |
| EV-AI006-002 | AI-006 — PondGPT | AI-006-R01 | PG-01 / PG-02 | Synthetic Authorization Matrix | Designed test input | Personas, source entitlements, repository exclusions, and DLP expectations |
| EV-AI006-003 | AI-006 — PondGPT | AI-006-R01 | PG-02 | Executable Permission Regression Control | Synthetic technical implementation demonstrated | Reproducible control logic that executes authorization, DLP, change, exception, gate, and retest assertions |
| EV-AI006-004 | AI-006 — PondGPT | AI-006-R01 | PG-02 | Permission Regression Test Log | Synthetic technical execution demonstrated | Twenty executed assertions across normal access, denials, exclusions, DLP, permission changes, seeded defect, remediation, and retest |
| EV-AI006-005 | AI-006 — PondGPT | AI-006-R01 | PG-02 | Seeded Authorization Exception | Synthetic failure detection / containment demonstrated | Detection of an intentionally misconfigured Finance connector ACL, alert generation, expansion blocking, and remediation tracking |
| EV-AI006-006 | AI-006 — PondGPT | AI-006-R01 | PG-02 | Permission Regression Control Test | Synthetic operation tested | Full-population control test and conclusion that PG-02 operated as designed within the synthetic population |
| EV-AI006-007 | AI-006 — PondGPT | AI-006-R01 | PG-01 / PG-02 | Production Permission / DLP / SIEM Records | Not available | Real operating evidence for authorization inheritance, DLP, alerting, and change-triggered regression |
| EV-AI006-008 | AI-006 — PondGPT | AI-006-R01 | PG-01 / PG-02 | Unauthorized Retrieval Escape Trend | Not available | Outcome effectiveness / actual cross-boundary data-exposure rate |

## Interpretation

A higher evidence state should not be inferred merely because a lower-state artifact exists.

For example:

- a control card demonstrates **design**;
- a synthetic execution log demonstrates **workflow or technical execution logic**;
- executable synthetic code can demonstrate **reproducible control implementation in the portfolio scenario**;
- a control test over synthetic data demonstrates **testable operation in a portfolio scenario**;
- only sustained production records could demonstrate **real operating effectiveness**; and
- validated effectiveness requires sufficiently rigorous or independent assurance over actual operation and outcomes.

## Current Evidence Conclusions

### WI-01 — Qualified Human Final Inspection

Project W.I.N.G. demonstrates:

**Designed → Synthetic execution demonstrated → Synthetic operation tested**

It does **not** claim:

**Production operating effectiveness → Validated effectiveness**

### DT-02 — Pre-Deployment Fairness & Adverse-Impact Testing

Project W.I.N.G. demonstrates:

**Designed → Synthetic technical implementation demonstrated → Synthetic fairness execution demonstrated → Synthetic operation tested**

The executable demonstration deliberately introduces an unapproved `Career_Gap_Months` scoring penalty into otherwise matched synthetic applicant pairs. The control succeeds because it detects the feature-governance violation, quantifies its effect, blocks the deployment gate, records an exception, removes the unapproved feature, and successfully retests the full synthetic population.

It does **not** claim:

**Production fairness validated → Real-applicant operating effectiveness → Legal compliance/non-discrimination → Validated rights-risk reduction → Independent assurance**

### AI-005 — Synthetic Governance Gate Decision

Project W.I.N.G. additionally demonstrates:

**Synthetic control evidence available → Governance evidence pack reviewed → Synthetic lifecycle decision demonstrated**

The gate record asks whether DuckTalent may advance to a pilot using real applicants. It consumes the current Critical-risk conclusion, AIA/FRIA/DPIA position, model-documentation gaps, DT-02 implementation evidence, run summary, and control-test result.

The decision is:

**DENIED — maintain DO NOT DEPLOY with real applicants**

The record therefore demonstrates that a successful synthetic control test does not override unresolved system-level risk, rights, privacy, model, human-oversight, security, accessibility, transparency, contestability, vendor, or monitoring conditions.

It does **not** claim:

**Real committee meeting → Real executive approval/non-approval → Real pilot authorization → Production operation → Validated risk reduction**

### AI-005 — Synthetic Monitoring, Reassessment & Revised Decision

Project W.I.N.G. now demonstrates:

**Prior synthetic gate decision → Synthetic material-change event → Synthetic change-monitor execution → Synthetic reassessment trigger → Synthetic reassessment performed → Synthetic revised lifecycle decision**

`DT-CHG-001` deliberately reintroduces `Career_Gap_Months` after the earlier DT-02 remediation. The executable regression monitor compares the proposed configuration with the existing synthetic approved-feature boundary, detects the unapproved feature and recreated matched-pair/group effect, and opens `IR-001`.

The reassessment reopens the relevant risk, control, AIA, FRIA/HUDERIA, DPIA, model-documentation, and gate-decision records. It does **not** lower the system risk score.

The revised decision is:

**DENIED — reject `DT-CHG-001` and maintain DO NOT DEPLOY with real applicants**

It does **not** claim:

**Continuous production monitoring → Real telemetry/event signal → Real committee reassessment → Real production suspension/authorization → Validated operating effectiveness**

### PG-02 — Automated Permission Regression & DLP Tests

Project W.I.N.G. demonstrates:

**Designed → Synthetic technical implementation demonstrated → Synthetic technical execution demonstrated → Synthetic operation tested**

The executable demonstration includes one seeded authorization defect that is detected, alerted, gated, remediated, and successfully retested. The control therefore does not pass because the synthetic environment contains no defects; it passes because the detective process identifies and contains the seeded defect as designed.

It does **not** claim:

**Production authorization validated → Sustained operating effectiveness → Validated risk reduction → Independent assurance**
