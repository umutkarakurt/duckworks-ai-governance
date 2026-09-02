# Duckworks AI Control Framework & Control Design Report

**DUCKWORKS**

**AI Control Framework &  
Control Design Report**

**Risk-to-control design for the 21 material Project W.I.N.G. AI risk scenarios**

| **Field**        | **Value**                                                                         |
|------------------|-----------------------------------------------------------------------------------|
| Organization     | Duckworks (fictional)                                                             |
| Program          | Project W.I.N.G.                                                                  |
| Document ID      | DW-WING-CTRL-01                                                                   |
| Version / status | 1.0 / Portfolio Baseline - Proposed Control Library                               |
| Scope            | AI-001 through AI-007; 21 material risk scenarios; 45 proposed/operating controls |
| Classification   | Fictional / Synthetic / Non-production                                            |

**Purpose**

Provide a defensible, auditable control design that links every material Duckworks AI risk to preventive, detective and/or corrective controls with named owners, frequency, evidence, testing procedures, automation opportunities, framework mappings and implementation status.

**Important boundary**

**Framework mappings in this report are governance/control design crosswalks. They do not establish legal compliance, regulatory conformity, ISO certification, or applicability of any law. Legal obligations remain a separate system-specific analysis.**

## 1. Executive Summary

Duckworks has 21 baseline material AI risk scenarios across seven inventory entries. The control design below creates a many-to-many risk/control model rather than inventing a separate control for every risk. Shared lifecycle, supplier, incident and evidence controls support system-specific safety, fairness, privacy, security, reliability and human-oversight controls.

The companion control library contains 45 controls: 26 preventive, 13 detective and 6 corrective. Current implementation posture is intentionally conservative: 2 controls are recorded as Implemented, 20 as Partially Implemented, 16 as Planned, 6 as Not Implemented and 1 as Weak / Ad Hoc. Those labels are design/portfolio status indicators, not independent audit opinions.

| **AI ID** | **System**               | **Current residual** | **Current gate**         | **Primary control focus**                                                                     |
|-----------|--------------------------|----------------------|--------------------------|-----------------------------------------------------------------------------------------------|
| AI-001    | DuckDesign AI            | High                 | Restricted pilot         | Safety validation, engineering human authority, IP/data boundary, regression testing          |
| AI-002    | QuackBot                 | High                 | Production blocked       | RAG grounding, escalation, prompt/RAG security testing, least privilege, monitoring           |
| AI-003    | FeatherForecast          | Moderate             | Continue with monitoring | Human planning approval, back-testing, drift alerts, supplier data controls                   |
| AI-004    | WingInspect Vision       | High                 | Restricted pilot         | Human final inspection, false-negative thresholds, QA sampling, fallback, revalidation        |
| AI-005    | DuckTalent AI            | Critical             | Do not deploy            | Job relevance, fairness testing, meaningful human review, data minimization, candidate remedy |
| AI-006    | PondGPT                  | High                 | Restricted pilot         | Permission-aware retrieval, permission regression, prompt/RAG tests, sandboxing, logging      |
| AI-007    | Unregistered GenAI Usage | Critical             | Immediate containment    | Acceptable use, approved tools, discovery/DLP, extension control, registration, remediation   |

## 2. Control Design Rules

- Evidence before credit: planned controls do not reduce current residual risk. An implementation label must be supported by evidence appropriate to the claimed state. Synthetic portfolio evidence may demonstrate design, workflow logic, or testability, but does not by itself establish production operating effectiveness.

- Risk and law remain separate: Duckworks internal High/Critical ratings are enterprise governance outcomes, not statutory AI classifications.

- One accountable owner: each control has one operating owner. Specialist reviewers can challenge, but ownership is not diffused across committees.

- Internal Audit independence: Internal Audit is deliberately excluded from first- and second-line control ownership and may later provide independent assurance.

- Material change invalidates stale assurance: changes to model/provider/data/permissions/purpose/autonomy/safety context trigger reassessment and re-testing.

- AI-007 is not a real system boundary: enterprise containment controls apply to shadow AI, but each material discovered use must be decomposed into its own inventory record and assessment.

## 3. Portfolio-Wide Controls

| **ID**    | **Control**                                   | **Type**   | **Owner**                                                    | **Frequency**                                                   | **Current design status**                                                                      |
|-----------|-----------------------------------------------|------------|--------------------------------------------------------------|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| AI-GOV-01 | Risk-Based Lifecycle Gate                     | Preventive | Eleanor Duckford - AI Governance Lead                        | At every lifecycle gate and material scope expansion            | Partially implemented - lifecycle gates exist; evidence workflow is still maturing             |
| AI-GOV-02 | Material Change & Reassessment Trigger        | Preventive | Eleanor Duckford - AI Governance Lead                        | On every material change; quarterly change-log reconciliation   | Partially implemented - triggers are defined; automated enforcement not evidenced              |
| AI-GOV-03 | Control Evidence Index                        | Detective  | Eleanor Duckford - AI Governance Lead                        | At each control execution; quarterly completeness review        | Planned - evidence repository/index is an open implementation priority                         |
| AI-TPR-01 | AI Supplier Due Diligence & Contract Controls | Preventive | Percival Duckworth - Director Procurement & Vendor Assurance | Before onboarding/renewal and on material supplier/model change | Partially implemented - templates exist; system-specific operating evidence is incomplete      |
| AI-INC-01 | AI Incident, Containment & Stop-Use           | Corrective | Cassandra Duckley - Chief Information Security Officer       | Event-driven; semiannual tabletop exercise for material AI      | Partially implemented - AI runbooks exist; sustained operating evidence is not yet established |

*These shared controls are not substitutes for system-specific safeguards. Their purpose is to ensure that release decisions, changes, suppliers, evidence and incidents are governed consistently across the portfolio.*

## 4. DuckDesign AI (AI-001)

**Current governance gate: Restricted pilot only. Priority: validate the open human-authority assumption and complete safety/benchmark/data-evidence gates before any production design reliance.**

### AI-001-R01 - Safety & physical harm

Incorrect or hallucinated engineering recommendation is accepted -\> unsafe design proceeds -\> product safety harm or costly rework.

| **Control ID** | **Control**                              | **Type**   | **Owner**                                              | **Status**            |
|----------------|------------------------------------------|------------|--------------------------------------------------------|-----------------------|
| AI-GOV-01      | Risk-Based Lifecycle Gate                | Preventive | Eleanor Duckford - AI Governance Lead                  | Partially implemented |
| AI-GOV-02      | Material Change & Reassessment Trigger   | Preventive | Eleanor Duckford - AI Governance Lead                  | Partially implemented |
| AI-INC-01      | AI Incident, Containment & Stop-Use      | Corrective | Cassandra Duckley - Chief Information Security Officer | Partially implemented |
| DD-01          | Competent Engineer Approval              | Preventive | Felix Duckson - VP Product & Engineering               | Implemented           |
| DD-02          | Independent Safety Validation Gate       | Preventive | Quentin Duckwell - Director Product Safety & Quality   | Planned               |
| DD-03          | Engineering Benchmark & Regression Suite | Detective  | Dr. Ada Duckfield - Head of Data & AI                  | Planned               |
| DD-05          | Design/Model Version Traceability        | Preventive | Dr. Ada Duckfield - Head of Data & AI                  | Partially implemented |

### AI-001-R02 - Privacy & data governance

Proprietary CAD/specifications are exposed to an external model/service -\> Duckworks IP is disclosed or reused.

| **Control ID** | **Control**                                   | **Type**   | **Owner**                                                    | **Status**            |
|----------------|-----------------------------------------------|------------|--------------------------------------------------------------|-----------------------|
| AI-GOV-02      | Material Change & Reassessment Trigger        | Preventive | Eleanor Duckford - AI Governance Lead                        | Partially implemented |
| AI-TPR-01      | AI Supplier Due Diligence & Contract Controls | Preventive | Percival Duckworth - Director Procurement & Vendor Assurance | Partially implemented |
| AI-INC-01      | AI Incident, Containment & Stop-Use           | Corrective | Cassandra Duckley - Chief Information Security Officer       | Partially implemented |
| DD-04          | Engineering Data Boundary & DLP               | Preventive | Cassandra Duckley - Chief Information Security Officer       | Partially implemented |

### AI-001-R03 - Reliability & robustness

Generated material/specification values are technically plausible but wrong -\> engineers use bad assumptions -\> design defects or rework occur.

| **Control ID** | **Control**                              | **Type**   | **Owner**                                | **Status**            |
|----------------|------------------------------------------|------------|------------------------------------------|-----------------------|
| AI-GOV-02      | Material Change & Reassessment Trigger   | Preventive | Eleanor Duckford - AI Governance Lead    | Partially implemented |
| DD-01          | Competent Engineer Approval              | Preventive | Felix Duckson - VP Product & Engineering | Implemented           |
| DD-03          | Engineering Benchmark & Regression Suite | Detective  | Dr. Ada Duckfield - Head of Data & AI    | Planned               |
| DD-05          | Design/Model Version Traceability        | Preventive | Dr. Ada Duckfield - Head of Data & AI    | Partially implemented |

## 5. QuackBot (AI-002)

**Current governance gate: Production blocked pending gates. Priority: keep customer production blocked until adversarial security testing, grounding/abstention and monitored escalation have operating evidence.**

### AI-002-R01 - Reliability & robustness

Chatbot hallucinates troubleshooting or warranty guidance -\> customer acts on incorrect advice -\> customer harm, complaint or liability.

| **Control ID** | **Control**                            | **Type**   | **Owner**                                              | **Status**            |
|----------------|----------------------------------------|------------|--------------------------------------------------------|-----------------------|
| AI-GOV-01      | Risk-Based Lifecycle Gate              | Preventive | Eleanor Duckford - AI Governance Lead                  | Partially implemented |
| QB-01          | Curated RAG Source Allowlist           | Preventive | Clara Duckley - Director Customer Operations           | Partially implemented |
| QB-02          | Grounding, Citation & Abstention Rules | Preventive | Dr. Ada Duckfield - Head of Data & AI                  | Planned               |
| QB-03          | Human Escalation SLA                   | Corrective | Clara Duckley - Director Customer Operations           | Partially implemented |
| QB-06          | GenAI Security & Harm Monitoring       | Detective  | Cassandra Duckley - Chief Information Security Officer | Planned               |

### AI-002-R02 - Security & adversarial manipulation

Prompt injection or malicious content manipulates retrieval/tool behavior -\> restricted information is exposed or unsafe actions are suggested.

| **Control ID** | **Control**                                   | **Type**   | **Owner**                                                    | **Status**            |
|----------------|-----------------------------------------------|------------|--------------------------------------------------------------|-----------------------|
| AI-TPR-01      | AI Supplier Due Diligence & Contract Controls | Preventive | Percival Duckworth - Director Procurement & Vendor Assurance | Partially implemented |
| AI-INC-01      | AI Incident, Containment & Stop-Use           | Corrective | Cassandra Duckley - Chief Information Security Officer       | Partially implemented |
| QB-04          | Prompt Injection & RAG Adversarial Testing    | Detective  | Cassandra Duckley - Chief Information Security Officer       | Planned               |
| QB-05          | Least-Privilege Retrieval & Tool Boundaries   | Preventive | Cassandra Duckley - Chief Information Security Officer       | Partially implemented |
| QB-06          | GenAI Security & Harm Monitoring              | Detective  | Cassandra Duckley - Chief Information Security Officer       | Planned               |

### AI-002-R03 - Legal / compliance

Chatbot gives incorrect warranty or consumer-rights statements -\> customers receive misleading information -\> legal, complaint or reputational consequences.

| **Control ID** | **Control**                            | **Type**   | **Owner**                                    | **Status**            |
|----------------|----------------------------------------|------------|----------------------------------------------|-----------------------|
| AI-GOV-01      | Risk-Based Lifecycle Gate              | Preventive | Eleanor Duckford - AI Governance Lead        | Partially implemented |
| QB-01          | Curated RAG Source Allowlist           | Preventive | Clara Duckley - Director Customer Operations | Partially implemented |
| QB-02          | Grounding, Citation & Abstention Rules | Preventive | Dr. Ada Duckfield - Head of Data & AI        | Planned               |
| QB-03          | Human Escalation SLA                   | Corrective | Clara Duckley - Director Customer Operations | Partially implemented |

## 6. FeatherForecast (AI-003)

**Current governance gate: Continue with monitoring. Priority: retain the mature human planning boundary and improve automated drift/challenger evidence rather than over-engineering governance.**

### AI-003-R01 - Operational / financial

Forecast error materially under- or over-estimates demand -\> poor procurement/production decisions -\> stockout, excess inventory or service impact.

| **Control ID** | **Control**                                      | **Type**   | **Owner**                              | **Status**            |
|----------------|--------------------------------------------------|------------|----------------------------------------|-----------------------|
| FF-01          | Human Planning Approval & Override               | Preventive | Tobias Duckman - Director Supply Chain | Implemented           |
| FF-02          | Back-Testing, Stress Testing & Challenger Review | Detective  | Dr. Ada Duckfield - Head of Data & AI  | Partially implemented |

### AI-003-R02 - Reliability & robustness

Market or supplier conditions shift -\> model drift is not detected promptly -\> degraded forecasts persist.

| **Control ID** | **Control**                                      | **Type**   | **Owner**                             | **Status**            |
|----------------|--------------------------------------------------|------------|---------------------------------------|-----------------------|
| AI-GOV-02      | Material Change & Reassessment Trigger           | Preventive | Eleanor Duckford - AI Governance Lead | Partially implemented |
| FF-02          | Back-Testing, Stress Testing & Challenger Review | Detective  | Dr. Ada Duckfield - Head of Data & AI | Partially implemented |
| FF-03          | Automated Drift Alerts & Retraining Trigger      | Detective  | Dr. Ada Duckfield - Head of Data & AI | Planned               |

### AI-003-R03 - Privacy & data governance

Supplier or confidential planning data is exposed through analytics access or integration -\> commercial information leakage.

| **Control ID** | **Control**                             | **Type**   | **Owner**                                              | **Status**            |
|----------------|-----------------------------------------|------------|--------------------------------------------------------|-----------------------|
| FF-04          | Supplier/Planning Data Access & Logging | Preventive | Tobias Duckman - Director Supply Chain                 | Partially implemented |
| AI-INC-01      | AI Incident, Containment & Stop-Use     | Corrective | Cassandra Duckley - Chief Information Security Officer | Partially implemented |

## 7. WingInspect Vision (AI-004)

**Current governance gate: Restricted pilot only. Priority: false-negative risk dominates. Safety sensitivity and human final authority must not be traded away to reduce false positives or inspection cost.**

### AI-004-R01 - Safety & physical harm

Model misses a true defect -\> defective component is not flagged -\> unsafe product could progress toward release.

| **Control ID** | **Control**                                        | **Type**   | **Owner**                                              | **Status**            |
|----------------|----------------------------------------------------|------------|--------------------------------------------------------|-----------------------|
| AI-GOV-01      | Risk-Based Lifecycle Gate                          | Preventive | Eleanor Duckford - AI Governance Lead                  | Partially implemented |
| AI-INC-01      | AI Incident, Containment & Stop-Use                | Corrective | Cassandra Duckley - Chief Information Security Officer | Partially implemented |
| WI-01          | Qualified Human Final Inspection                   | Preventive | Henrietta Duckwell - Director Manufacturing            | Partially implemented |
| WI-02          | Minimum Sensitivity & Safety Validation            | Preventive | Quentin Duckwell - Director Product Safety & Quality   | Partially implemented |
| WI-03          | Independent QA Sampling & Defect-Escape Monitoring | Detective  | Quentin Duckwell - Director Product Safety & Quality   | Planned               |
| WI-04          | Fail-Safe Manual Fallback & Stop Rule              | Corrective | Henrietta Duckwell - Director Manufacturing            | Planned               |

#### WI-01 implementation / evidence note

`WI-01 — Qualified Human Final Inspection` is operationalized in the portfolio as a **Mandatory Human Release Gate**.

The worked evidence package at [`../80-operating-evidence/AI-004-winginspect/`](../80-operating-evidence/AI-004-winginspect/) demonstrates the intended control workflow using synthetic records, including:

- qualified-inspector review before final disposition;
- independent accept/reject authority;
- four documented AI/human disagreements with override rationale;
- timestamped traceability from AI output to human decision and release/block disposition; and
- a synthetic control-test workpaper.

The control remains **Partially implemented** for portfolio-status purposes because the evidence demonstrates design, workflow logic and synthetic testability rather than real production authority, sustained operation or operating effectiveness. `ASM-008` therefore remains Open / Critical, and this evidence does not provide additional residual-risk reduction credit.

### AI-004-R02 - Operational / financial

False positives incorrectly flag good components -\> unnecessary scrap/rework -\> manufacturing cost and delay.

| **Control ID** | **Control**                              | **Type**   | **Owner**                                   | **Status**            |
|----------------|------------------------------------------|------------|---------------------------------------------|-----------------------|
| WI-01          | Qualified Human Final Inspection         | Preventive | Henrietta Duckwell - Director Manufacturing | Partially implemented |
| WI-05          | False-Positive Tuning & QA Feedback Loop | Corrective | Dr. Ada Duckfield - Head of Data & AI       | Planned               |

### AI-004-R03 - Reliability & robustness

Camera or product-line changes create distribution shift -\> detection performance degrades unnoticed -\> defect escape rate rises.

| **Control ID** | **Control**                                        | **Type**   | **Owner**                                            | **Status**            |
|----------------|----------------------------------------------------|------------|------------------------------------------------------|-----------------------|
| AI-GOV-02      | Material Change & Reassessment Trigger             | Preventive | Eleanor Duckford - AI Governance Lead                | Partially implemented |
| WI-03          | Independent QA Sampling & Defect-Escape Monitoring | Detective  | Quentin Duckwell - Director Product Safety & Quality | Planned               |
| WI-06          | Change-Triggered Revalidation & Locked Baseline    | Preventive | Dr. Ada Duckfield - Head of Data & AI                | Partially implemented |

## 8. DuckTalent AI (AI-005)

**Current governance gate: Do not deploy in current state. Priority: deployment remains blocked. Fairness cannot be reduced to one metric; job relevance, data governance, human decision quality, contestability and vendor evidence all need closure.**

### AI-005-R01 - Fundamental rights & fairness

Training data or features encode historical/proxy bias -\> ranking disadvantages a protected group -\> discriminatory access to employment.

| **Control ID** | **Control**                                       | **Type**   | **Owner**                                                    | **Status**            |
|----------------|---------------------------------------------------|------------|--------------------------------------------------------------|-----------------------|
| AI-GOV-01      | Risk-Based Lifecycle Gate                         | Preventive | Eleanor Duckford - AI Governance Lead                        | Partially implemented |
| AI-TPR-01      | AI Supplier Due Diligence & Contract Controls     | Preventive | Percival Duckworth - Director Procurement & Vendor Assurance | Partially implemented |
| DT-01          | Job-Relevance Criteria & Proxy Feature Governance | Preventive | Beatrice Van Duck - Chief People Officer                     | Not implemented       |
| DT-02          | Pre-Deployment Fairness & Adverse-Impact Testing  | Detective  | Beatrice Van Duck - Chief People Officer                     | Partially implemented |
| DT-07          | Candidate Notice, Challenge & Human Remedy        | Corrective | Beatrice Van Duck - Chief People Officer                     | Not implemented       |

#### DT-02 implementation / evidence note

A worked executable evidence package is available at [`../80-operating-evidence/AI-005-ducktalent/`](../80-operating-evidence/AI-005-ducktalent/).

The package implements a deterministic synthetic `DT-02` test harness over 24 synthetic applicants arranged as 12 matched pairs. Approved job-related test features are held equal within each pair while a deliberately unapproved `Career_Gap_Months` penalty is introduced into the pre-remediation scoring configuration.

The synthetic execution demonstrates:

- feature allow-list conformance testing;
- matched-pair score comparison;
- selection-rate and error diagnostics;
- detection of the seeded unapproved feature;
- pre-deployment gate blocking;
- generated exception evidence;
- removal of the unapproved feature;
- full-population retesting; and
- a final state of **Eligible for further governance review**, not deployment approval.

`DT-02` is therefore classified as **Partially implemented** for portfolio-status purposes because a reproducible synthetic testing mechanism and evidence-generation workflow exist. `DT-01` remains **Not implemented** because the synthetic allow-list is only a test fixture and does not establish real DuckTalent job-criteria or feature governance.

The defensible evidence state is **Designed → Synthetic technical implementation demonstrated → Synthetic fairness execution demonstrated → Synthetic operation tested**.

This package uses no real applicants or real protected-characteristic data and does not establish legal discrimination, legal compliance, production fairness, lawful fairness-data processing, accessibility performance, or real DuckTalent model behavior. DuckTalent therefore remains **Critical**, **Do not deploy**, and system-level control effectiveness remains **Not Implemented**.

### AI-005-R02 - Human oversight & automation bias

Recruiters over-rely on rankings/summaries -\> flawed AI recommendation becomes the de facto decision -\> qualified candidates are unfairly screened out.

| **Control ID** | **Control**                                        | **Type**   | **Owner**                                | **Status**            |
|----------------|----------------------------------------------------|------------|------------------------------------------|-----------------------|
| AI-GOV-01      | Risk-Based Lifecycle Gate                          | Preventive | Eleanor Duckford - AI Governance Lead    | Partially implemented |
| DT-03          | Meaningful Human Review & No Automated Rejection   | Preventive | Beatrice Van Duck - Chief People Officer | Not implemented       |
| DT-04          | Reviewer Rationale, Training & Override Monitoring | Preventive | Beatrice Van Duck - Chief People Officer | Not implemented       |
| DT-07          | Candidate Notice, Challenge & Human Remedy         | Corrective | Beatrice Van Duck - Chief People Officer | Not implemented       |

### AI-005-R03 - Privacy & data governance

CV/application data contains sensitive attributes or proxies -\> unnecessary inference or use occurs -\> privacy and discrimination exposure.

| **Control ID** | **Control**                                              | **Type**   | **Owner**                                                    | **Status**            |
|----------------|----------------------------------------------------------|------------|--------------------------------------------------------------|-----------------------|
| AI-TPR-01      | AI Supplier Due Diligence & Contract Controls            | Preventive | Percival Duckworth - Director Procurement & Vendor Assurance | Partially implemented |
| AI-INC-01      | AI Incident, Containment & Stop-Use                      | Corrective | Cassandra Duckley - Chief Information Security Officer       | Partially implemented |
| DT-05          | Applicant Data Minimization, Field Exclusion & Retention | Preventive | Beatrice Van Duck - Chief People Officer                     | Not implemented       |
| DT-06          | Impact, Privacy & Legal Review Gate                      | Preventive | Eleanor Duckford - AI Governance Lead                        | Not implemented       |

## 9. PondGPT (AI-006)

**Current governance gate: Restricted pilot only. Priority: permission inheritance is a critical assumption. Sensitive repositories should remain excluded until regression tests, DLP, attack testing and logging are verified.**

### AI-006-R01 - Privacy & data governance

Permission or retrieval configuration failure exposes restricted internal information -\> an unauthorized employee receives sensitive, IP or customer data.

| **Control ID** | **Control**                                   | **Type**   | **Owner**                                                    | **Status**            |
|----------------|-----------------------------------------------|------------|--------------------------------------------------------------|-----------------------|
| AI-TPR-01      | AI Supplier Due Diligence & Contract Controls | Preventive | Percival Duckworth - Director Procurement & Vendor Assurance | Partially implemented |
| AI-INC-01      | AI Incident, Containment & Stop-Use           | Corrective | Cassandra Duckley - Chief Information Security Officer       | Partially implemented |
| PG-01          | Permission-Aware Retrieval                    | Preventive | Oliver Duckett - Head of IT & Cloud                          | Partially implemented |
| PG-02          | Automated Permission Regression & DLP Tests   | Detective  | Oliver Duckett - Head of IT & Cloud                          | Partially implemented |
| PG-05          | GenAI Security Logging & Alerting             | Detective  | Cassandra Duckley - Chief Information Security Officer       | Partially implemented |

#### PG-02 implementation / evidence note

A worked executable evidence package is available at [`../80-operating-evidence/AI-006-pondgpt/`](../80-operating-evidence/AI-006-pondgpt/).

The package implements the `PG-02` control logic in a deterministic Python test harness using a synthetic authorization matrix, synthetic personas, source entitlements, DLP/exclusion assertions, permission-change cases, a deliberately seeded connector ACL defect, exception/gate handling, remediation, and retesting.

The synthetic execution performs 20 control assertions. The seeded Finance authorization defect is intentionally allowed to occur in the test environment so that PG-02 can demonstrate detection, alert generation, connector/corpus expansion blocking, remediation, and successful retest.

`PG-02` is therefore classified as **Partially implemented** for portfolio-status purposes: a reproducible synthetic technical mechanism and evidence-generation workflow exist, but production identity/connector/DLP/SIEM integration, scheduled operating history, and production operating effectiveness are not evidenced.

This synthetic implementation does **not** validate `ASM-009` or `ASM-030` as production facts and does not provide additional current residual-risk reduction credit.

### AI-006-R02 - Security & adversarial manipulation

Prompt injection or poisoned retrieved content manipulates the assistant -\> unsafe output, data exfiltration or tool misuse occurs.

| **Control ID** | **Control**                                 | **Type**   | **Owner**                                              | **Status**            |
|----------------|---------------------------------------------|------------|--------------------------------------------------------|-----------------------|
| AI-INC-01      | AI Incident, Containment & Stop-Use         | Corrective | Cassandra Duckley - Chief Information Security Officer | Partially implemented |
| PG-03          | Prompt Injection & RAG Poisoning Test Suite | Detective  | Cassandra Duckley - Chief Information Security Officer | Planned               |
| PG-04          | Tool Sandboxing & Allowlisted Actions       | Preventive | Oliver Duckett - Head of IT & Cloud                    | Partially implemented |
| PG-05          | GenAI Security Logging & Alerting           | Detective  | Cassandra Duckley - Chief Information Security Officer | Partially implemented |

### AI-006-R03 - Reliability & robustness

Employee uses hallucinated code or operational guidance without verification -\> vulnerable code or an incorrect business action is introduced.

| **Control ID** | **Control**                                | **Type**   | **Owner**                                              | **Status**            |
|----------------|--------------------------------------------|------------|--------------------------------------------------------|-----------------------|
| PG-05          | GenAI Security Logging & Alerting          | Detective  | Cassandra Duckley - Chief Information Security Officer | Partially implemented |
| PG-06          | Secure Output Verification & Code Scanning | Preventive | Dr. Ada Duckfield - Head of Data & AI                  | Partially implemented |

## 10. Unregistered GenAI Usage (AI-007)

**Current governance gate: Immediate containment and decomposition. Priority: contain first, then decompose. A single organization-wide shadow-AI record cannot support a defensible legal classification, risk score or control conclusion for every discovered use.**

### AI-007-R01 - Privacy & data governance

Employee uploads confidential, IP or personal data to unapproved public AI -\> provider retention/training or unauthorized access causes disclosure.

| **Control ID** | **Control**                                         | **Type**   | **Owner**                                                    | **Status**            |
|----------------|-----------------------------------------------------|------------|--------------------------------------------------------------|-----------------------|
| AI-INC-01      | AI Incident, Containment & Stop-Use                 | Corrective | Cassandra Duckley - Chief Information Security Officer       | Partially implemented |
| SH-01          | AI Acceptable Use Standard                          | Preventive | Cassandra Duckley - Chief Information Security Officer       | Planned               |
| SH-02          | Approved AI Tool Catalogue & Vendor Allowlist       | Preventive | Percival Duckworth - Director Procurement & Vendor Assurance | Planned               |
| SH-03          | Shadow AI Discovery, DLP & Blocking                 | Detective  | Cassandra Duckley - Chief Information Security Officer       | Planned               |
| SH-04          | AI Browser Extension & Embedded-App Control         | Preventive | Oliver Duckett - Head of IT & Cloud                          | Weak / ad hoc         |
| SH-06          | Exposure Investigation, Decomposition & Remediation | Corrective | Eleanor Duckford - AI Governance Lead                        | Planned               |

### AI-007-R02 - Legal / compliance

Unregistered AI is used in HR, customer or another consequential process -\> applicable requirements are not identified -\> unlawful or uncontrolled decision support.

| **Control ID** | **Control**                                                           | **Type**   | **Owner**                                              | **Status**            |
|----------------|-----------------------------------------------------------------------|------------|--------------------------------------------------------|-----------------------|
| AI-GOV-01      | Risk-Based Lifecycle Gate                                             | Preventive | Eleanor Duckford - AI Governance Lead                  | Partially implemented |
| SH-01          | AI Acceptable Use Standard                                            | Preventive | Cassandra Duckley - Chief Information Security Officer | Planned               |
| SH-05          | Employee Attestation, Manager Accountability & Mandatory Registration | Detective  | Eleanor Duckford - AI Governance Lead                  | Planned               |
| SH-06          | Exposure Investigation, Decomposition & Remediation                   | Corrective | Eleanor Duckford - AI Governance Lead                  | Planned               |

### AI-007-R03 - Third-party & supply chain

Unknown vendors, extensions or plugins process company data under unknown retention/security/service-change terms -\> unmanaged third-party exposure persists.

| **Control ID** | **Control**                                         | **Type**   | **Owner**                                                    | **Status**            |
|----------------|-----------------------------------------------------|------------|--------------------------------------------------------------|-----------------------|
| AI-TPR-01      | AI Supplier Due Diligence & Contract Controls       | Preventive | Percival Duckworth - Director Procurement & Vendor Assurance | Partially implemented |
| SH-02          | Approved AI Tool Catalogue & Vendor Allowlist       | Preventive | Percival Duckworth - Director Procurement & Vendor Assurance | Planned               |
| SH-04          | AI Browser Extension & Embedded-App Control         | Preventive | Oliver Duckett - Head of IT & Cloud                          | Weak / ad hoc         |
| SH-06          | Exposure Investigation, Decomposition & Remediation | Corrective | Eleanor Duckford - AI Governance Lead                        | Planned               |

## 11. Control Evidence and Testing Model

The library is designed so that a GRC reviewer or Internal Audit team can later test both control design and operation without reconstructing the entire AI project. Every control records expected evidence and a practical testing procedure in the companion workbook.

| **Assurance dimension** | **Question**                                                                                                             | **Example evidence**                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| Design effectiveness    | Does the control, if performed as written, address the stated risk scenario and preserve the approved decision boundary? | Control description, procedure/configuration, ownership, scope, design walkthrough          |
| Operating effectiveness | Did the control operate consistently for the selected period/population?                                                 | Execution records, logs, approvals, alerts, test results, tickets, exceptions               |
| Evidence confidence     | Is evidence current, complete, version-specific and independently reproducible where appropriate?                        | Evidence index, timestamps, model/config identifiers, reviewer identity, source-system logs |
| Change resilience       | Would a model/data/permission/provider/purpose change bypass or invalidate the control?                                  | Change register, version history, reassessment records, regression evidence                 |
| Exception governance    | Are deviations time/event bound and approved at the correct authority with compensating controls?                        | Exception request, residual risk, approver, expiry trigger, closure evidence                |

**Internal Audit should not operate or design these controls. A future audit program can use the library testing procedures as an auditable starting point after controls have sufficient operating history.**

## 12. Automation Opportunities

- Governance workflow automation: release gates, mandatory fields, approval routing, evidence ageing and reassessment triggers in QuackTrack/GRC tooling.

- MLOps/CI controls: model/version stamping, benchmark and adversarial regression suites, change detection and blocked release on failed thresholds.

- Security automation: DLP/SSE/CASB discovery, permission regression, SIEM/SOAR case creation, connector/tool allowlists and endpoint/browser enforcement.

- Monitoring automation: drift alerts, false-negative/false-positive thresholds, unsupported-answer metrics, permission violations and reviewer/override trend analytics.

- Evidence automation: automatically attach versioned logs/test results/approvals to the relevant AI ID and control ID rather than relying on manual screenshots.

## 13. Implementation Priorities

| **Priority** | **Scope**              | **Required outcome**                                                                                                                                          | **Primary owners**                            |
|--------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| P0           | AI-005 DuckTalent      | Keep blocked; implement DT-01 through DT-07, supplier review and governance gate before any real-applicant use.                                               | CPO / AI Governance / Data & AI               |
| P0           | AI-007 Shadow AI       | Publish acceptable-use rules; establish approved tools; enable discovery/DLP; control extensions; attest/register; investigate and decompose discovered uses. | CISO / AI Governance / Procurement            |
| P1           | AI-002 QuackBot        | Close grounding, escalation, adversarial testing, least-privilege and monitoring gates before customer production.                                            | Customer Operations / CISO / Data & AI        |
| P1           | AI-006 PondGPT         | Verify source permission inheritance, regression tests, DLP, injection tests, sandboxing and logging before sensitive repository expansion.                   | IT & Cloud / CISO / Data & AI                 |
| P1           | AI-001 DuckDesign      | Validate human engineering approval, independent safety tests, engineering benchmark suite, DLP/vendor evidence and traceability.                             | Product & Engineering / Product Safety / CISO |
| P1           | AI-004 WingInspect     | Establish false-negative acceptance thresholds, independent QA sampling, fallback and locked-baseline revalidation.                                           | Manufacturing / Product Safety / Data & AI    |
| P2           | AI-003 FeatherForecast | Preserve human planning approval while automating drift alerts, stress/challenger evidence and access assurance.                                              | Supply Chain / Data & AI                      |

*Priority labels are Duckworks implementation priorities only; they are not legal classifications or statutory deadlines.*

## 14. Assumptions and Gaps That Must Be Challenged

- Meaningful human oversight is repeatedly assumed across DuckDesign, WingInspect, FeatherForecast and DuckTalent. A named human is not enough: workflow evidence must show sufficient information, time, authority and ability to override. For WingInspect specifically, the synthetic `WI-01` evidence package demonstrates the intended workflow and override logic, but `ASM-008` remains Open / Critical until real manufacturing authority and operating evidence are validated.

- PondGPT source-authorization inheritance and third-party tenant/data-use controls are material assumptions. The synthetic PG-02 package now demonstrates executable permission-regression logic, seeded-defect detection, gating and retest, but `ASM-009` / `ASM-030` remain unverified production assumptions until real architecture, access tests, supplier evidence and operating records are obtained.

- DuckTalent vendor/model/feature design is not finalized. The synthetic DT-02 package now demonstrates executable pre-deployment fairness-test logic, seeded unapproved-feature detection, deployment blocking and remediation/retest, but this does not validate production features, real applicant outcomes, lawful fairness-data processing or legal compliance. Fairness, privacy, explainability, human-oversight and candidate-remedy controls remain blocking requirements.

- Current baseline control-effectiveness labels are assessment inputs, not independent assurance conclusions. This report does not upgrade Partially Effective or Weak controls merely by documenting them.

- AI-007 cannot be scored or legally classified as one stable system after discovery. Its controls must drive decomposition into distinct use cases, each with its own owner, data, purpose and treatment.

## 15. Framework Mapping Boundary and Sources

**Framework mappings are deliberately maintained at function/topic level. The project uses public descriptions and recognized guidance; it does not reproduce copyrighted ISO clauses or claim clause-level conformity without authorized standard text. Mapping a control to NIST, ISO, ENISA or OWASP means the control is conceptually relevant to that framework/guidance, not that Duckworks is legally compliant or certified.**

| **Framework / guidance**                                             | **Classification**                                           | **Use in this control framework**                                                                                                 |
|----------------------------------------------------------------------|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| NIST AI Risk Management Framework (AI RMF 1.0)                       | Voluntary framework                                          | Governance, context, measurement and risk management functions (GOVERN, MAP, MEASURE, MANAGE)                                     |
| NIST AI 600-1 - Generative AI Profile                                | Voluntary NIST profile                                       | GenAI-specific risk analysis and treatments for systems such as QuackBot, PondGPT, DuckDesign and shadow GenAI                    |
| ISO/IEC 42001:2023                                                   | Management-system requirements standard                      | AI management-system governance, accountability, lifecycle controls and continual improvement; mappings are topic-level only      |
| ISO/IEC 23894:2023                                                   | Voluntary guidance standard                                  | AI risk identification, analysis, treatment and monitoring                                                                        |
| ISO/IEC 42005:2025                                                   | Voluntary guidance standard                                  | AI system impact assessment and affected-person/stakeholder impact thinking                                                       |
| ISO/IEC 27001:2022                                                   | Information security management-system requirements standard | Information-security governance, access control, supplier security, logging, secure development and incident management around AI |
| ISO 31000:2018                                                       | Voluntary risk-management guidance                           | Enterprise/operational risk principles used for proportional treatment and monitoring                                             |
| ENISA - Multilayer Framework for Good Cybersecurity Practices for AI | Official EU agency guidance                                  | AI cybersecurity threat/control design across lifecycle layers                                                                    |
| OWASP GenAI Security Project                                         | Recognized technical guidance                                | Practical GenAI security design/testing for injection, sensitive information, excessive agency and related application risks      |

## 16. Reference URLs

NIST AI Risk Management Framework (AI RMF 1.0): https://www.nist.gov/itl/ai-risk-management-framework

NIST AI 600-1 - Generative AI Profile: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf

ISO/IEC 42001:2023: https://www.iso.org/standard/42001

ISO/IEC 23894:2023: https://www.iso.org/standard/77304.html

ISO/IEC 42005:2025: https://www.iso.org/standard/42005

ISO/IEC 27001:2022: https://www.iso.org/standard/27001

ISO 31000:2018: https://www.iso.org/standard/65694.html

ENISA - Multilayer Framework for Good Cybersecurity Practices for AI: https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai

OWASP GenAI Security Project: https://genai.owasp.org/

## 17. Source-Basis and Portfolio Disclaimer

The risk coverage in this report is based on the Duckworks AI Risk Scenario Register v1.0 and the risk-assessed AI inventory. Control ownership is aligned to the Duckworks stakeholder model. Evidence and no-false-compliance rules are aligned to the project acceptance criteria and assumptions register. Legal/framework source taxonomy is drawn from the Duckworks public frameworks/legislation register.

**Duckworks, Project W.I.N.G., all personnel, AI systems, vendors, data, risks, controls, incidents and evidence in this report are fictional or synthetic. This artifact is designed solely for educational and professional portfolio demonstration. It is not legal advice, certification evidence, an audit opinion, an EU AI Act conformity assessment, a GDPR compliance determination, or proof that any external framework has been implemented.**

## Appendix A - Control Index

| **ID**    | **Control**                                                           | **Type**   | **Owner**                                                    | **Design status**     |
|-----------|-----------------------------------------------------------------------|------------|--------------------------------------------------------------|-----------------------|
| AI-GOV-01 | Risk-Based Lifecycle Gate                                             | Preventive | Eleanor Duckford - AI Governance Lead                        | Partially implemented |
| AI-GOV-02 | Material Change & Reassessment Trigger                                | Preventive | Eleanor Duckford - AI Governance Lead                        | Partially implemented |
| AI-GOV-03 | Control Evidence Index                                                | Detective  | Eleanor Duckford - AI Governance Lead                        | Planned               |
| AI-TPR-01 | AI Supplier Due Diligence & Contract Controls                         | Preventive | Percival Duckworth - Director Procurement & Vendor Assurance | Partially implemented |
| AI-INC-01 | AI Incident, Containment & Stop-Use                                   | Corrective | Cassandra Duckley - Chief Information Security Officer       | Partially implemented |
| DD-01     | Competent Engineer Approval                                           | Preventive | Felix Duckson - VP Product & Engineering                     | Implemented           |
| DD-02     | Independent Safety Validation Gate                                    | Preventive | Quentin Duckwell - Director Product Safety & Quality         | Planned               |
| DD-03     | Engineering Benchmark & Regression Suite                              | Detective  | Dr. Ada Duckfield - Head of Data & AI                        | Planned               |
| DD-04     | Engineering Data Boundary & DLP                                       | Preventive | Cassandra Duckley - Chief Information Security Officer       | Partially implemented |
| DD-05     | Design/Model Version Traceability                                     | Preventive | Dr. Ada Duckfield - Head of Data & AI                        | Partially implemented |
| QB-01     | Curated RAG Source Allowlist                                          | Preventive | Clara Duckley - Director Customer Operations                 | Partially implemented |
| QB-02     | Grounding, Citation & Abstention Rules                                | Preventive | Dr. Ada Duckfield - Head of Data & AI                        | Planned               |
| QB-03     | Human Escalation SLA                                                  | Corrective | Clara Duckley - Director Customer Operations                 | Partially implemented |
| QB-04     | Prompt Injection & RAG Adversarial Testing                            | Detective  | Cassandra Duckley - Chief Information Security Officer       | Planned               |
| QB-05     | Least-Privilege Retrieval & Tool Boundaries                           | Preventive | Cassandra Duckley - Chief Information Security Officer       | Partially implemented |
| QB-06     | GenAI Security & Harm Monitoring                                      | Detective  | Cassandra Duckley - Chief Information Security Officer       | Planned               |
| FF-01     | Human Planning Approval & Override                                    | Preventive | Tobias Duckman - Director Supply Chain                       | Implemented           |
| FF-02     | Back-Testing, Stress Testing & Challenger Review                      | Detective  | Dr. Ada Duckfield - Head of Data & AI                        | Partially implemented |
| FF-03     | Automated Drift Alerts & Retraining Trigger                           | Detective  | Dr. Ada Duckfield - Head of Data & AI                        | Planned               |
| FF-04     | Supplier/Planning Data Access & Logging                               | Preventive | Tobias Duckman - Director Supply Chain                       | Partially implemented |
| WI-01     | Qualified Human Final Inspection                                      | Preventive | Henrietta Duckwell - Director Manufacturing                  | Partially implemented |
| WI-02     | Minimum Sensitivity & Safety Validation                               | Preventive | Quentin Duckwell - Director Product Safety & Quality         | Partially implemented |
| WI-03     | Independent QA Sampling & Defect-Escape Monitoring                    | Detective  | Quentin Duckwell - Director Product Safety & Quality         | Planned               |
| WI-04     | Fail-Safe Manual Fallback & Stop Rule                                 | Corrective | Henrietta Duckwell - Director Manufacturing                  | Planned               |
| WI-05     | False-Positive Tuning & QA Feedback Loop                              | Corrective | Dr. Ada Duckfield - Head of Data & AI                        | Planned               |
| WI-06     | Change-Triggered Revalidation & Locked Baseline                       | Preventive | Dr. Ada Duckfield - Head of Data & AI                        | Partially implemented |
| DT-01     | Job-Relevance Criteria & Proxy Feature Governance                     | Preventive | Beatrice Van Duck - Chief People Officer                     | Not implemented       |
| DT-02     | Pre-Deployment Fairness & Adverse-Impact Testing                      | Detective  | Beatrice Van Duck - Chief People Officer                     | Partially implemented |
| DT-03     | Meaningful Human Review & No Automated Rejection                      | Preventive | Beatrice Van Duck - Chief People Officer                     | Not implemented       |
| DT-04     | Reviewer Rationale, Training & Override Monitoring                    | Preventive | Beatrice Van Duck - Chief People Officer                     | Not implemented       |
| DT-05     | Applicant Data Minimization, Field Exclusion & Retention              | Preventive | Beatrice Van Duck - Chief People Officer                     | Not implemented       |
| DT-06     | Impact, Privacy & Legal Review Gate                                   | Preventive | Eleanor Duckford - AI Governance Lead                        | Not implemented       |
| DT-07     | Candidate Notice, Challenge & Human Remedy                            | Corrective | Beatrice Van Duck - Chief People Officer                     | Not implemented       |
| PG-01     | Permission-Aware Retrieval                                            | Preventive | Oliver Duckett - Head of IT & Cloud                          | Partially implemented |
| PG-02     | Automated Permission Regression & DLP Tests                           | Detective  | Oliver Duckett - Head of IT & Cloud                          | Partially implemented |
| PG-03     | Prompt Injection & RAG Poisoning Test Suite                           | Detective  | Cassandra Duckley - Chief Information Security Officer       | Planned               |
| PG-04     | Tool Sandboxing & Allowlisted Actions                                 | Preventive | Oliver Duckett - Head of IT & Cloud                          | Partially implemented |
| PG-05     | GenAI Security Logging & Alerting                                     | Detective  | Cassandra Duckley - Chief Information Security Officer       | Partially implemented |
| PG-06     | Secure Output Verification & Code Scanning                            | Preventive | Dr. Ada Duckfield - Head of Data & AI                        | Partially implemented |
| SH-01     | AI Acceptable Use Standard                                            | Preventive | Cassandra Duckley - Chief Information Security Officer       | Planned               |
| SH-02     | Approved AI Tool Catalogue & Vendor Allowlist                         | Preventive | Percival Duckworth - Director Procurement & Vendor Assurance | Planned               |
| SH-03     | Shadow AI Discovery, DLP & Blocking                                   | Detective  | Cassandra Duckley - Chief Information Security Officer       | Planned               |
| SH-04     | AI Browser Extension & Embedded-App Control                           | Preventive | Oliver Duckett - Head of IT & Cloud                          | Weak / ad hoc         |
| SH-05     | Employee Attestation, Manager Accountability & Mandatory Registration | Detective  | Eleanor Duckford - AI Governance Lead                        | Planned               |
| SH-06     | Exposure Investigation, Decomposition & Remediation                   | Corrective | Eleanor Duckford - AI Governance Lead                        | Planned               |

*For full objective, description, frequency, evidence, testing procedure, automation opportunity, related risks, framework mapping and implementation-status basis, use the companion Duckworks_AI_Control_Library_v1.0.xlsx.*
