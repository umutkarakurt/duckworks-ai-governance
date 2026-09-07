# Duckworks AI Control Framework Report

**Project:** W.I.N.G. — Workflows, Intelligence, Next-Generation Governance  
**Document ID:** DW-AICF-001  
**Version:** 1.1  
**Effective date:** 7 September 2026  
**Owner:** AI Governance Lead  
**Approval status:** Portfolio draft — fictional approval not recorded  
**Evidence reconciliation snapshot:** `e734ea64d6a9e5db35b59c4855e832aa433b43ad`  
**Supersedes:** Duckworks_AI_Control_Framework_Report_v1.0.md

> Status labels in this report describe the available portfolio evidence. They do not establish legal compliance, ISO/IEC 42001 conformity, certification, production effectiveness or independent assurance.

## 1. Evidence-aware status model

| Status | Minimum meaning | Permitted risk credit |
|---|---|---|
| Designed | Control objective, owner, trigger, procedure and required evidence are documented. | None |
| Implemented | The control mechanism exists for the defined system/version; implementation evidence is retrievable. | No effectiveness credit by itself |
| Operating | Execution records cover a defined population and period, including exceptions and review. | Possible only after authorized assessment |
| Effective | Operating evidence and outcomes show the control consistently achieves its objective for the defined scope and period. | May support an approved residual-risk reduction |
| Validated | Effectiveness has been challenged by a competent reviewer with sufficient independence and limitations recorded. | May support a sustained reduction within the approved methodology |
| Synthetic operation demonstrated | A bounded fictional/synthetic workflow or test was executed. | No production risk-reduction credit |

A source label such as Implemented or Partially implemented is retained for history, but the reconciled evidence-maturity field controls interpretation.

## 2. Control register

| Control ID | Control | Type | Operating owner | Source status | Linked risks | Evidence IDs | Reconciled evidence maturity | Current risk credit | Next evidence required | Review status |
|---|---|---|---|---|---|---|---|---|---|---|
| AI-GOV-01 | Risk-Based Lifecycle Gate | Preventive | Eleanor Duckford - AI Governance Lead | Partially implemented | AI-001-R01; AI-002-R01; AI-002-R03; AI-004-R01; AI-005-R01; AI-005-R02; AI-007-R02 | EV-AI005-009; EV-AI005-014 | Synthetic implementation/operation demonstrated; production effectiveness unverified | No production risk-reduction credit | Add version-bound production operating and outcome evidence, including population, period, exceptions, review and approval. | Open |
| AI-GOV-02 | Material Change & Reassessment Trigger | Preventive | Eleanor Duckford - AI Governance Lead | Partially implemented | AI-001-R01; AI-001-R02; AI-001-R03; AI-003-R02; AI-004-R03 | EV-AI005-010; EV-AI005-011; EV-AI005-012; EV-AI005-013; EV-AI005-014 | Synthetic implementation/operation demonstrated; production effectiveness unverified | No production risk-reduction credit | Add version-bound production operating and outcome evidence, including population, period, exceptions, review and approval. | Open |
| AI-GOV-03 | Control Evidence Index | Detective | Eleanor Duckford - AI Governance Lead | Planned | Portfolio-wide evidence governance | None linked | Implemented at portfolio-document level; maintenance operation untested | Design/document implementation only | Assign a maintenance cadence; test retrieval, review, supersession and cross-document update operation. | Open |
| AI-INC-01 | AI Incident, Containment & Stop-Use | Corrective | Cassandra Duckley - Chief Information Security Officer | Partially implemented | AI-001-R01; AI-001-R02; AI-002-R02; AI-003-R03; AI-004-R01; AI-005-R03; AI-006-R01; AI-006-R02; AI-007-R01 | None linked | Design/status assertion — evidence ID absent | No additional credit | Provide implementation and operating evidence with a stable evidence ID. | Open |
| AI-TPR-01 | AI Supplier Due Diligence & Contract Controls | Preventive | Percival Duckworth - Director Procurement & Vendor Assurance | Partially implemented | AI-001-R02; AI-002-R02; AI-005-R01; AI-005-R03; AI-006-R01; AI-007-R03 | None linked | Design/status assertion — evidence ID absent | No additional credit | Provide implementation and operating evidence with a stable evidence ID. | Open |
| DD-01 | Competent Engineer Approval | Preventive | Felix Duckson - VP Product & Engineering | Implemented | AI-001-R01; AI-001-R03 | None linked | Unsupported implementation assertion — evidence ID absent | No additional credit until evidence is retrieved and reviewed | Provide execution records, population/period, exceptions, outcome metrics and owner review. | Open |
| DD-02 | Independent Safety Validation Gate | Preventive | Quentin Duckwell - Director Product Safety & Quality | Planned | AI-001-R01 | None linked | Planned | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| DD-03 | Engineering Benchmark & Regression Suite | Detective | Dr. Ada Duckfield - Head of Data & AI | Planned | AI-001-R01; AI-001-R03 | None linked | Planned | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| DD-04 | Engineering Data Boundary & DLP | Preventive | Cassandra Duckley - Chief Information Security Officer | Partially implemented | AI-001-R02 | None linked | Design/status assertion — evidence ID absent | No additional credit | Provide implementation and operating evidence with a stable evidence ID. | Open |
| DD-05 | Design/Model Version Traceability | Preventive | Dr. Ada Duckfield - Head of Data & AI | Partially implemented | AI-001-R01; AI-001-R03 | None linked | Design/status assertion — evidence ID absent | No additional credit | Provide implementation and operating evidence with a stable evidence ID. | Open |
| DT-01 | Job-Relevance Criteria & Proxy Feature Governance | Preventive | Beatrice Van Duck - Chief People Officer | Not implemented | AI-005-R01 | EV-AI005-001; EV-AI005-002; EV-AI005-009; EV-AI005-011; EV-AI005-012 | Not implemented; related synthetic evidence does not establish full implementation | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| DT-02 | Pre-Deployment Fairness & Adverse-Impact Testing | Detective | Beatrice Van Duck - Chief People Officer | Partially implemented | AI-005-R01 | EV-AI005-001; EV-AI005-002; EV-AI005-003; EV-AI005-004; EV-AI005-005; EV-AI005-006; EV-AI005-009; EV-AI005-011; EV-AI005-012 | Synthetic implementation/operation demonstrated; production effectiveness unverified | No production risk-reduction credit | Add version-bound production operating and outcome evidence, including population, period, exceptions, review and approval. | Open |
| DT-03 | Meaningful Human Review & No Automated Rejection | Preventive | Beatrice Van Duck - Chief People Officer | Not implemented | AI-005-R02 | None linked | Not implemented | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| DT-04 | Reviewer Rationale, Training & Override Monitoring | Preventive | Beatrice Van Duck - Chief People Officer | Not implemented | AI-005-R02 | None linked | Not implemented | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| DT-05 | Applicant Data Minimization, Field Exclusion & Retention | Preventive | Beatrice Van Duck - Chief People Officer | Not implemented | AI-005-R03 | None linked | Not implemented | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| DT-06 | Impact, Privacy & Legal Review Gate | Preventive | Eleanor Duckford - AI Governance Lead | Not implemented | AI-005-R03 | None linked | Not implemented | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| DT-07 | Candidate Notice, Challenge & Human Remedy | Corrective | Beatrice Van Duck - Chief People Officer | Not implemented | AI-005-R01; AI-005-R02 | None linked | Not implemented | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| FF-01 | Human Planning Approval & Override | Preventive | Tobias Duckman - Director Supply Chain | Implemented | AI-003-R01 | None linked | Unsupported implementation assertion — evidence ID absent | No additional credit until evidence is retrieved and reviewed | Provide execution records, population/period, exceptions, outcome metrics and owner review. | Open |
| FF-02 | Back-Testing, Stress Testing & Challenger Review | Detective | Dr. Ada Duckfield - Head of Data & AI | Partially implemented | AI-003-R01; AI-003-R02 | None linked | Design/status assertion — evidence ID absent | No additional credit | Provide implementation and operating evidence with a stable evidence ID. | Open |
| FF-03 | Automated Drift Alerts & Retraining Trigger | Detective | Dr. Ada Duckfield - Head of Data & AI | Planned | AI-003-R02 | None linked | Planned | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| FF-04 | Supplier/Planning Data Access & Logging | Preventive | Tobias Duckman - Director Supply Chain | Partially implemented | AI-003-R03 | None linked | Design/status assertion — evidence ID absent | No additional credit | Provide implementation and operating evidence with a stable evidence ID. | Open |
| PG-01 | Permission-Aware Retrieval | Preventive | Oliver Duckett - Head of IT & Cloud | Partially implemented | AI-006-R01 | EV-AI006-001; EV-AI006-002 | Synthetic implementation/operation demonstrated; production effectiveness unverified | No production risk-reduction credit | Add version-bound production operating and outcome evidence, including population, period, exceptions, review and approval. | Open |
| PG-02 | Automated Permission Regression & DLP Tests | Detective | Oliver Duckett - Head of IT & Cloud | Partially implemented | AI-006-R01 | EV-AI006-001; EV-AI006-002; EV-AI006-003; EV-AI006-004; EV-AI006-005; EV-AI006-006 | Synthetic implementation/operation demonstrated; production effectiveness unverified | No production risk-reduction credit | Add version-bound production operating and outcome evidence, including population, period, exceptions, review and approval. | Open |
| PG-03 | Prompt Injection & RAG Poisoning Test Suite | Detective | Cassandra Duckley - Chief Information Security Officer | Planned | AI-006-R02 | None linked | Planned | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| PG-04 | Tool Sandboxing & Allowlisted Actions | Preventive | Oliver Duckett - Head of IT & Cloud | Partially implemented | AI-006-R02 | None linked | Design/status assertion — evidence ID absent | No additional credit | Provide implementation and operating evidence with a stable evidence ID. | Open |
| PG-05 | GenAI Security Logging & Alerting | Detective | Cassandra Duckley - Chief Information Security Officer | Partially implemented | AI-006-R01; AI-006-R02; AI-006-R03 | None linked | Design/status assertion — evidence ID absent | No additional credit | Provide implementation and operating evidence with a stable evidence ID. | Open |
| PG-06 | Secure Output Verification & Code Scanning | Preventive | Dr. Ada Duckfield - Head of Data & AI | Partially implemented | AI-006-R03 | None linked | Design/status assertion — evidence ID absent | No additional credit | Provide implementation and operating evidence with a stable evidence ID. | Open |
| QB-01 | Curated RAG Source Allowlist | Preventive | Clara Duckley - Director Customer Operations | Partially implemented | AI-002-R01; AI-002-R03 | None linked | Design/status assertion — evidence ID absent | No additional credit | Provide implementation and operating evidence with a stable evidence ID. | Open |
| QB-02 | Grounding, Citation & Abstention Rules | Preventive | Dr. Ada Duckfield - Head of Data & AI | Planned | AI-002-R01; AI-002-R03 | None linked | Planned | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| QB-03 | Human Escalation SLA | Corrective | Clara Duckley - Director Customer Operations | Partially implemented | AI-002-R01; AI-002-R03 | None linked | Design/status assertion — evidence ID absent | No additional credit | Provide implementation and operating evidence with a stable evidence ID. | Open |
| QB-04 | Prompt Injection & RAG Adversarial Testing | Detective | Cassandra Duckley - Chief Information Security Officer | Planned | AI-002-R02 | None linked | Planned | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| QB-05 | Least-Privilege Retrieval & Tool Boundaries | Preventive | Cassandra Duckley - Chief Information Security Officer | Partially implemented | AI-002-R02 | None linked | Design/status assertion — evidence ID absent | No additional credit | Provide implementation and operating evidence with a stable evidence ID. | Open |
| QB-06 | GenAI Security & Harm Monitoring | Detective | Cassandra Duckley - Chief Information Security Officer | Planned | AI-002-R01; AI-002-R02 | None linked | Planned | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| SH-01 | AI Acceptable Use Standard | Preventive | Cassandra Duckley - Chief Information Security Officer | Planned | AI-007-R01; AI-007-R02 | None linked | Planned | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| SH-02 | Approved AI Tool Catalogue & Vendor Allowlist | Preventive | Percival Duckworth - Director Procurement & Vendor Assurance | Planned | AI-007-R01; AI-007-R03 | None linked | Planned | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| SH-03 | Shadow AI Discovery, DLP & Blocking | Detective | Cassandra Duckley - Chief Information Security Officer | Planned | AI-007-R01 | None linked | Planned | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| SH-04 | AI Browser Extension & Embedded-App Control | Preventive | Oliver Duckett - Head of IT & Cloud | Weak / ad hoc | AI-007-R01; AI-007-R03 | None linked | Design/status assertion — evidence ID absent | No additional credit | Provide implementation and operating evidence with a stable evidence ID. | Open |
| SH-05 | Employee Attestation, Manager Accountability & Mandatory Registration | Detective | Eleanor Duckford - AI Governance Lead | Planned | AI-007-R02 | None linked | Planned | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| SH-06 | Exposure Investigation, Decomposition & Remediation | Corrective | Eleanor Duckford - AI Governance Lead | Planned | AI-007-R01; AI-007-R02; AI-007-R03 | None linked | Planned | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| WI-01 | Qualified Human Final Inspection | Preventive | Henrietta Duckwell - Director Manufacturing | Partially implemented | AI-004-R01; AI-004-R02 | EV-AI004-001; EV-AI004-002; EV-AI004-003 | Synthetic implementation/operation demonstrated; production effectiveness unverified | No production risk-reduction credit | Add version-bound production operating and outcome evidence, including population, period, exceptions, review and approval. | Open |
| WI-02 | Minimum Sensitivity & Safety Validation | Preventive | Quentin Duckwell - Director Product Safety & Quality | Partially implemented | AI-004-R01 | None linked | Design/status assertion — evidence ID absent | No additional credit | Provide implementation and operating evidence with a stable evidence ID. | Open |
| WI-03 | Independent QA Sampling & Defect-Escape Monitoring | Detective | Quentin Duckwell - Director Product Safety & Quality | Planned | AI-004-R01; AI-004-R03 | None linked | Planned | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| WI-04 | Fail-Safe Manual Fallback & Stop Rule | Corrective | Henrietta Duckwell - Director Manufacturing | Planned | AI-004-R01 | None linked | Planned | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| WI-05 | False-Positive Tuning & QA Feedback Loop | Corrective | Dr. Ada Duckfield - Head of Data & AI | Planned | AI-004-R02 | None linked | Planned | No current risk-reduction credit | Implement the control, assign stable evidence IDs, operate it over a defined period and test it. | Open |
| WI-06 | Change-Triggered Revalidation & Locked Baseline | Preventive | Dr. Ada Duckfield - Head of Data & AI | Partially implemented | AI-004-R03 | None linked | Design/status assertion — evidence ID absent | No additional credit | Provide implementation and operating evidence with a stable evidence ID. | Open |

## 3. Portfolio-wide control clarifications

- **AI-GOV-01 — Risk-Based Lifecycle Gate:** EV-AI005-009 and EV-AI005-014 demonstrate bounded synthetic DuckTalent gate decisions. They do not establish enterprise-wide operation.
- **AI-GOV-02 — Material Change & Reassessment Trigger:** EV-AI005-010 through EV-AI005-014 demonstrate one synthetic DuckTalent material-change and reassessment cycle.
- **AI-GOV-03 — Control Evidence Index:** the index exists and is implemented at the portfolio-document level. Its maintenance, retrieval and supersession process has not yet been tested.
- **AI-INC-01 — AI Incident, Containment & Stop-Use:** seeded exceptions demonstrate related detection, gating and containment behavior. They do not demonstrate the complete incident lifecycle.

## 4. Evidence acceptance requirements

Before a control can be rated Operating, Effective or Validated for a production context, the reviewer must record:

1. Exact AI system, model/service, data, configuration and control version.
2. Defined population and operating period.
3. Control owner and actual performer.
4. Expected and observed execution frequency.
5. Exceptions, overrides, failures and remediation.
6. Outcome or effectiveness metric and threshold.
7. Reviewer competence, independence and limitations.
8. Approval and resulting lifecycle/risk decision.

A screenshot, folder reference, policy statement or implementation label alone is insufficient evidence of operation or effectiveness.

## 5. Testing approach

| Evidence stage | Minimum test |
|---|---|
| Designed | Inspect whether objective, owner, trigger, procedure, evidence and metric are complete and aligned to the mapped risk. |
| Implemented | Inspect configuration or implementation artifact and verify it applies to the scoped version and boundary. |
| Operating | Select or evaluate the full defined-period population; verify execution, timeliness, completeness, exceptions and review. |
| Effective | Evaluate whether outcomes remain within approved thresholds and whether failures were detected and corrected. |
| Validated | Repeat or independently challenge the test, data, sampling, conclusion and decision linkage. |

## 6. Governance and maintenance

The AI Governance Lead maintains the framework. Control owners supply evidence and explain exceptions. Risk owners approve any credit used in risk scoring. Material changes or control failures trigger reassessment. Control status changes must be reflected simultaneously in the risk register, evidence index, AIMS crosswalk and management reporting.
