# Duckworks AI Risk Scenario Register

System-specific cause -\> event -\> impact scenarios for the Project W.I.N.G. AI portfolio

| **Document ID**    | DW-WING-RSCN-01                                   |
|--------------------|---------------------------------------------------|
| **Version / date** | 1.0 / 9 August 2026                               |
| **Status**         | Portfolio Baseline - Risk Scenario Register       |
| **Organization**   | Duckworks (fictional)                             |
| **Program**        | Project W.I.N.G.                                  |
| **Owner**          | Risk & Compliance / AI Governance Lead            |
| **Coverage**       | AI-001 through AI-007; 21 baseline risk scenarios |
| **Classification** | Fictional / Synthetic / Non-production            |

> **Portfolio disclaimer.** Duckworks, Project W.I.N.G., all personnel, AI systems, data, incidents, controls, scores and evidence in this document are fictional or synthetic and created solely for educational and professional portfolio purposes. This register is not legal advice, certification evidence, a conformity assessment, or proof of regulatory compliance.

## 1. Purpose and Use

This register isolates and normalizes the material AI risk scenarios already assessed across the seven-entry Duckworks baseline. It is designed for use in risk workshops, control design, test planning, treatment tracking, AI Governance Committee review, internal assurance, and interview/portfolio demonstration.

**Scenario coverage.** The register contains three baseline scenarios for each of AI-001 through AI-007 (21 scenarios total). It is a controlled starting set, not an exhaustive threat model. New scenarios must be added when the intended purpose, model/provider, data, users, integrations, autonomy, geography, affected population, or operating environment changes materially.

| Duckworks scenario rule: Write concrete cause -\> event -\> impact scenarios. Do not score vague labels such as “bias risk” or “hallucination risk.” Planned controls receive no credit as implemented controls, and target residual risk must not be reported as current risk. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## 2. Method and Interpretation

Duckworks uses a 5x5 Severity x Likelihood matrix. Each scenario is scored inherently, then re-scored after controls that are actually implemented and evidenced. Target risk represents the planned state after additional treatment. The overall system rating is driven by the highest material scenario rather than an average that could dilute severe harm.

| **Rating** | **Score** | **Governance response**                                                                                                     | **Color**    |
|------------|-----------|-----------------------------------------------------------------------------------------------------------------------------|--------------|
| Low        | 1-4       | Owner acceptance; routine controls; at least annual review.                                                                 | **Low**      |
| Moderate   | 5-9       | Owner + AI Governance review; documented controls and monitoring.                                                           | **Moderate** |
| High       | 10-16     | AI Governance Committee approval/treatment; enhanced evidence; pre-production gate.                                         | **High**     |
| Critical   | 17-25     | Production/continued use normally blocked pending treatment or exceptional executive risk acceptance; immediate escalation. | **Critical** |

**Important separation.** Duckworks Low/Moderate/High/Critical ratings are internal enterprise-risk ratings. They are not statutory AI classifications. Legal/regulatory triage is a separate governance gate.

## 3. Risk Domains Used for Scenario Identification

| **Risk domain**                                   | **Assessment lens**                                                                     |
|---------------------------------------------------|-----------------------------------------------------------------------------------------|
| **Fundamental rights, fairness & discrimination** | Unequal treatment, accessibility, discrimination, exclusion, or adverse rights impacts. |
| **Safety & physical harm**                        | Physical injury, unsafe product outcomes, or hazardous operating decisions.             |
| **Privacy & data governance**                     | Personal data, confidentiality, IP, minimization, provenance, and retention.            |
| **Security, abuse & adversarial manipulation**    | Prompt injection, poisoning, model abuse, exfiltration, and insecure integrations.      |
| **Reliability, robustness & model performance**   | Hallucination, accuracy, drift, distribution shift, brittleness, and instability.       |
| **Transparency & explainability**                 | Disclosure, traceability, understandable outputs/limitations, and contestability.       |
| **Human oversight & automation bias**             | Over-reliance, ineffective review, inappropriate autonomy, and unclear accountability.  |
| **Third-party & supply chain**                    | Vendor/model dependencies, contractual terms, subprocessors, and service/model changes. |
| **Operational, financial & reputational**         | Service disruption, poor planning, cost, complaints, and brand impact.                  |
| **Legal, regulatory & compliance**                | Applicable legal duties, documentation, approval, recordkeeping, and control failure.   |

## 4. Portfolio Risk Position

| **AI ID**  | **System**                   | **Inherent**  | **Current**       | **Target**   | **Control status**  | **Gate**                                |
|------------|------------------------------|---------------|-------------------|--------------|---------------------|-----------------------------------------|
| **AI-001** | **DuckDesign AI**            | High (16)     | **High (10)**     | Moderate (8) | Partially Effective | Restricted pilot only                   |
| **AI-002** | **QuackBot**                 | High (16)     | **High (12)**     | Moderate (8) | Partially Effective | Production blocked pending gates        |
| **AI-003** | **FeatherForecast**          | Moderate (9)  | **Moderate (6)**  | Low (3)      | Effective           | Continue with monitoring                |
| **AI-004** | **WingInspect Vision**       | High (15)     | **High (10)**     | Moderate (5) | Partially Effective | Restricted pilot only                   |
| **AI-005** | **DuckTalent AI**            | Critical (20) | **Critical (20)** | High (10)    | Not Implemented     | Do not deploy in current state          |
| **AI-006** | **PondGPT**                  | High (16)     | **High (12)**     | Moderate (8) | Partially Effective | Restricted pilot only                   |
| **AI-007** | **Unregistered GenAI Usage** | Critical (20) | **Critical (20)** | High (10)    | Weak                | Immediate containment and decomposition |

**Portfolio interpretation.** DuckTalent AI and Unregistered GenAI Usage remain Critical current residual risk. DuckDesign AI, QuackBot, WingInspect Vision and PondGPT remain High. FeatherForecast is the only Moderate current residual system and is the current mature production baseline.

## 5. AI-001 - DuckDesign AI

*Generative engineering assistant for mechanical-arm design, optimization, simulation and CAD support.*

| **Lifecycle**             | Pilot               | **Risk owner**              | Felix Duckson - VP Product & Engineering |
|---------------------------|---------------------|-----------------------------|------------------------------------------|
| **Control effectiveness** | Partially Effective | **Evidence confidence**     | Medium                                   |
| **Overall inherent risk** | **High (16)**       | **Current residual risk**   | **High (10)**                            |
| **Target residual risk**  | **Moderate (8)**    | **Current governance gate** | **Restricted pilot only**                |

**Current decision:** Pilot may continue with restrictions; production is gated on validated safety criteria, independent engineering verification and formal change control.

### Baseline risk scenarios

| **AI-001-R01** | **Safety & physical harm** | **Scenario risk progression** |
|----------------|----------------------------|-------------------------------|

| **Cause**                       | AI generates an incorrect or hallucinated engineering recommendation.                                        |
|---------------------------------|--------------------------------------------------------------------------------------------------------------|
| **Event**                       | The recommendation is accepted and incorporated into a design.                                               |
| **Impact**                      | An unsafe design progresses toward prototyping or production, creating product-safety harm or costly rework. |
| **Inherent risk**               | **Severity 5 x Likelihood 3 = 15 High**                                                                      |
| **Existing controls credited**  | Mandatory engineer approval; pilot restrictions; output validation.                                          |
| **Current residual risk**       | **Severity 5 x Likelihood 2 = 10 High**                                                                      |
| **Target treatment / controls** | Independent validation criteria; safety test gates; version/change control; documented design traceability.  |
| **Target residual risk**        | **Severity 4 x Likelihood 2 = 8 Moderate**                                                                   |

| **AI-001-R02** | **Privacy & data governance** | **Scenario risk progression** |
|----------------|-------------------------------|-------------------------------|

| **Cause**                       | Proprietary CAD files or specifications are provided to an external model or service.              |
|---------------------------------|----------------------------------------------------------------------------------------------------|
| **Event**                       | The information is exposed, retained, reused, or accessed outside the approved Duckworks boundary. |
| **Impact**                      | Duckworks intellectual property or confidential engineering information is disclosed or reused.    |
| **Inherent risk**               | **Severity 4 x Likelihood 3 = 12 High**                                                            |
| **Existing controls credited**  | Tenant isolation; restricted access; approved data scope.                                          |
| **Current residual risk**       | **Severity 4 x Likelihood 2 = 8 Moderate**                                                         |
| **Target treatment / controls** | Contractual no-training terms; DLP; confidential-data controls; vendor evidence review.            |
| **Target residual risk**        | **Severity 4 x Likelihood 1 = 4 Low**                                                              |

| **AI-001-R03** | **Reliability & robustness** | **Scenario risk progression** |
|----------------|------------------------------|-------------------------------|

| **Cause**                       | AI generates technically plausible but incorrect material or specification values.                                             |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| **Event**                       | Engineers rely on the incorrect values as design assumptions.                                                                  |
| **Impact**                      | Design defects, failed validation, rework, or downstream quality issues occur.                                                 |
| **Inherent risk**               | **Severity 4 x Likelihood 4 = 16 High**                                                                                        |
| **Existing controls credited**  | Human review; simulation checks.                                                                                               |
| **Current residual risk**       | **Severity 4 x Likelihood 2 = 8 Moderate**                                                                                     |
| **Target treatment / controls** | Versioned benchmark suite; grounded engineering sources; fail-safe validation; monitoring of override and validation failures. |
| **Target residual risk**        | **Severity 4 x Likelihood 2 = 8 Moderate**                                                                                     |

**System-level rating note.** The system-level current and target ratings shown above are determined by the highest material scenario and the Duckworks governance rules; they are not averages of the scenario scores.

## 6. AI-002 - QuackBot

*Customer-service chatbot for product questions, troubleshooting, warranty guidance and escalation.*

| **Lifecycle**             | Development         | **Risk owner**              | Clara Duckley - Director Customer Operations |
|---------------------------|---------------------|-----------------------------|----------------------------------------------|
| **Control effectiveness** | Partially Effective | **Evidence confidence**     | Low-Medium                                   |
| **Overall inherent risk** | **High (16)**       | **Current residual risk**   | **High (12)**                                |
| **Target residual risk**  | **Moderate (8)**    | **Current governance gate** | **Production blocked pending gates**         |

**Current decision:** Customer-facing production is blocked until security testing, RAG validation, escalation controls and an AI impact assessment are complete.

### Baseline risk scenarios

| **AI-002-R01** | **Reliability & robustness** | **Scenario risk progression** |
|----------------|------------------------------|-------------------------------|

| **Cause**                       | QuackBot hallucinates troubleshooting, warranty, or product-support information.                                      |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| **Event**                       | A customer receives and acts on the incorrect guidance.                                                               |
| **Impact**                      | Customer harm, complaints, warranty disputes, liability, or loss of trust may result.                                 |
| **Inherent risk**               | **Severity 4 x Likelihood 4 = 16 High**                                                                               |
| **Existing controls credited**  | Escalation rules; source allowlist; draft safety filters.                                                             |
| **Current residual risk**       | **Severity 4 x Likelihood 3 = 12 High**                                                                               |
| **Target treatment / controls** | Pre-release evaluations; grounding/citation checks; constrained answers for high-impact topics; human escalation SLA. |
| **Target residual risk**        | **Severity 4 x Likelihood 2 = 8 Moderate**                                                                            |

| **AI-002-R02** | **Security & adversarial manipulation** | **Scenario risk progression** |
|----------------|-----------------------------------------|-------------------------------|

| **Cause**                       | A malicious prompt or poisoned source content manipulates retrieval or tool behavior.                                |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------|
| **Event**                       | QuackBot retrieves restricted information, follows malicious instructions, or produces unsafe guidance.              |
| **Impact**                      | Sensitive data may be exposed and customers or systems may be adversely affected.                                    |
| **Inherent risk**               | **Severity 4 x Likelihood 4 = 16 High**                                                                              |
| **Existing controls credited**  | Least-privilege retrieval design; authentication; draft filters.                                                     |
| **Current residual risk**       | **Severity 4 x Likelihood 3 = 12 High**                                                                              |
| **Target treatment / controls** | Adversarial testing; content isolation; tool-permission boundaries; injection monitoring; red-team regression suite. |
| **Target residual risk**        | **Severity 4 x Likelihood 2 = 8 Moderate**                                                                           |

| **AI-002-R03** | **Legal / compliance** | **Scenario risk progression** |
|----------------|------------------------|-------------------------------|

| **Cause**                       | The chatbot generates incorrect warranty or consumer-rights statements.                                         |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------|
| **Event**                       | The incorrect statement is presented to a customer as authoritative Duckworks guidance.                         |
| **Impact**                      | Customers receive misleading information, creating legal, contractual, complaint, or reputational consequences. |
| **Inherent risk**               | **Severity 3 x Likelihood 4 = 12 High**                                                                         |
| **Existing controls credited**  | Knowledge-base allowlist; escalation.                                                                           |
| **Current residual risk**       | **Severity 3 x Likelihood 3 = 9 Moderate**                                                                      |
| **Target treatment / controls** | Approved legal content; response templates for regulated topics; confidence/abstention rules.                   |
| **Target residual risk**        | **Severity 3 x Likelihood 2 = 6 Moderate**                                                                      |

**System-level rating note.** The system-level current and target ratings shown above are determined by the highest material scenario and the Duckworks governance rules; they are not averages of the scenario scores.

## 7. AI-003 - FeatherForecast

*Predictive analytics for demand, inventory, production-volume and supply-chain forecasting.*

| **Lifecycle**             | Production       | **Risk owner**              | Tobias Duckman - Director Supply Chain |
|---------------------------|------------------|-----------------------------|----------------------------------------|
| **Control effectiveness** | Effective        | **Evidence confidence**     | High                                   |
| **Overall inherent risk** | **Moderate (9)** | **Current residual risk**   | **Moderate (6)**                       |
| **Target residual risk**  | **Low (3)**      | **Current governance gate** | **Continue with monitoring**           |

**Current decision:** Production use may continue with routine monitoring, manager approval for material commitments, data-quality controls and drift/performance oversight.

### Baseline risk scenarios

| **AI-003-R01** | **Operational / financial** | **Scenario risk progression** |
|----------------|-----------------------------|-------------------------------|

| **Cause**                       | The forecasting model materially underestimates or overestimates demand.                                       |
|---------------------------------|----------------------------------------------------------------------------------------------------------------|
| **Event**                       | Procurement, inventory, or production planning decisions are made using the inaccurate forecast.               |
| **Impact**                      | Duckworks experiences stockouts, excess inventory, production inefficiency, service impact, or avoidable cost. |
| **Inherent risk**               | **Severity 3 x Likelihood 3 = 9 Moderate**                                                                     |
| **Existing controls credited**  | Human planning approval; back-testing; overrides.                                                              |
| **Current residual risk**       | **Severity 3 x Likelihood 2 = 6 Moderate**                                                                     |
| **Target treatment / controls** | Stress testing; scenario ranges; exception thresholds; periodic recalibration.                                 |
| **Target residual risk**        | **Severity 3 x Likelihood 1 = 3 Low**                                                                          |

| **AI-003-R02** | **Reliability & robustness** | **Scenario risk progression** |
|----------------|------------------------------|-------------------------------|

| **Cause**                       | Market or supplier conditions change materially from the model's historical operating context. |
|---------------------------------|------------------------------------------------------------------------------------------------|
| **Event**                       | Model drift is not detected or addressed promptly.                                             |
| **Impact**                      | Degraded forecasts persist and repeatedly influence planning decisions.                        |
| **Inherent risk**               | **Severity 3 x Likelihood 3 = 9 Moderate**                                                     |
| **Existing controls credited**  | Monthly drift review; performance monitoring.                                                  |
| **Current residual risk**       | **Severity 3 x Likelihood 2 = 6 Moderate**                                                     |
| **Target treatment / controls** | Automated drift alerts; challenger model; defined retraining trigger.                          |
| **Target residual risk**        | **Severity 3 x Likelihood 1 = 3 Low**                                                          |

| **AI-003-R03** | **Privacy & data governance** | **Scenario risk progression** |
|----------------|-------------------------------|-------------------------------|

| **Cause**                       | Supplier or confidential planning data is made accessible through analytics integrations or overly broad access. |
|---------------------------------|------------------------------------------------------------------------------------------------------------------|
| **Event**                       | An unauthorized person or system obtains commercially sensitive information.                                     |
| **Impact**                      | Supplier confidentiality, commercial position, or Duckworks internal planning information is compromised.        |
| **Inherent risk**               | **Severity 3 x Likelihood 2 = 6 Moderate**                                                                       |
| **Existing controls credited**  | Private cloud; role-based access.                                                                                |
| **Current residual risk**       | **Severity 3 x Likelihood 1 = 3 Low**                                                                            |
| **Target treatment / controls** | Periodic access review; encryption; logging; supplier-data minimization.                                         |
| **Target residual risk**        | **Severity 3 x Likelihood 1 = 3 Low**                                                                            |

**System-level rating note.** The system-level current and target ratings shown above are determined by the highest material scenario and the Duckworks governance rules; they are not averages of the scenario scores.

## 8. AI-004 - WingInspect Vision

*Computer-vision system that flags potential manufacturing defects for quality-control review.*

| **Lifecycle**             | Pilot               | **Risk owner**              | Henrietta Duckwell - Director Manufacturing |
|---------------------------|---------------------|-----------------------------|---------------------------------------------|
| **Control effectiveness** | Partially Effective | **Evidence confidence**     | Medium                                      |
| **Overall inherent risk** | **High (15)**       | **Current residual risk**   | **High (10)**                               |
| **Target residual risk**  | **Moderate (5)**    | **Current governance gate** | **Restricted pilot only**                   |

**Current decision:** Pilot may continue only on the approved non-safety-critical product line with mandatory human final inspection.

### Baseline risk scenarios

| **AI-004-R01** | **Safety & physical harm** | **Scenario risk progression** |
|----------------|----------------------------|-------------------------------|

| **Cause**                       | The vision model fails to detect a true product defect.                                                 |
|---------------------------------|---------------------------------------------------------------------------------------------------------|
| **Event**                       | A defective component is not flagged and progresses through the quality process.                        |
| **Impact**                      | An unsafe or defective product could progress toward release, creating physical or product-safety harm. |
| **Inherent risk**               | **Severity 5 x Likelihood 3 = 15 High**                                                                 |
| **Existing controls credited**  | Mandatory human final inspection; pilot limited to non-safety-critical line.                            |
| **Current residual risk**       | **Severity 5 x Likelihood 2 = 10 High**                                                                 |
| **Target treatment / controls** | Validated minimum sensitivity; safety case; independent QA sampling; fail-safe/manual fallback.         |
| **Target residual risk**        | **Severity 5 x Likelihood 1 = 5 Moderate**                                                              |

#### Implementation evidence — AI-004-R01 / WI-01

A worked implementation demonstration for the canonical control **`WI-01 — Qualified Human Final Inspection`** is available at:

[`../80-operating-evidence/AI-004-winginspect/`](../80-operating-evidence/AI-004-winginspect/)

The evidence package operationalizes `WI-01` through a **Mandatory Human Release Gate** and demonstrates, using synthetic portfolio records:

- control design and decision boundaries;
- a qualified manufacturing inspector as the control performer;
- final release authorization only after recorded human review;
- human accept/reject authority independent of the AI output;
- documented AI overrides and rationale;
- timestamped traceability from AI output to human decision and final disposition; and
- a control-test workpaper over the complete synthetic inspection population.

**Evidence state:** **Designed → Synthetic execution demonstrated → Synthetic operation tested.**

**Assurance boundary:** This package does not establish real production operating effectiveness, actual WingInspect defect-detection performance, sustained inspector behavior under throughput pressure, or validated reduction of product-safety risk. The underlying real-world human-authority assumption therefore remains subject to operational validation.

Accordingly, this synthetic evidence package does **not** provide additional residual-risk reduction credit. The current `AI-004-R01` residual risk, system-level **High (10)** rating, **Partially Effective** control status, and **Medium** evidence confidence remain unchanged by this portfolio demonstration.

| **AI-004-R02** | **Operational / financial** | **Scenario risk progression** |
|----------------|-----------------------------|-------------------------------|

| **Cause**                       | The model produces excessive false-positive defect alerts.               |
|---------------------------------|--------------------------------------------------------------------------|
| **Event**                       | Good components are incorrectly flagged and held, scrapped, or reworked. |
| **Impact**                      | Manufacturing cost, waste, delay, and inspector workload increase.       |
| **Inherent risk**               | **Severity 3 x Likelihood 4 = 12 High**                                  |
| **Existing controls credited**  | Human inspector confirmation.                                            |
| **Current residual risk**       | **Severity 3 x Likelihood 2 = 6 Moderate**                               |
| **Target treatment / controls** | Threshold tuning; cost-weighted evaluation; feedback loop with QA.       |
| **Target residual risk**        | **Severity 3 x Likelihood 1 = 3 Low**                                    |

| **AI-004-R03** | **Reliability & robustness** | **Scenario risk progression** |
|----------------|------------------------------|-------------------------------|

| **Cause**                       | Camera, lighting, product-line, or component characteristics change from the validated baseline. |
|---------------------------------|--------------------------------------------------------------------------------------------------|
| **Event**                       | Distribution shift degrades model detection performance without timely revalidation.             |
| **Impact**                      | Defect escape rates increase and confidence in the inspection control becomes unreliable.        |
| **Inherent risk**               | **Severity 4 x Likelihood 3 = 12 High**                                                          |
| **Existing controls credited**  | Performance by product line; camera monitoring.                                                  |
| **Current residual risk**       | **Severity 4 x Likelihood 2 = 8 Moderate**                                                       |
| **Target treatment / controls** | Change-triggered revalidation; automated drift detection; locked deployment baselines.           |
| **Target residual risk**        | **Severity 4 x Likelihood 1 = 4 Low**                                                            |

**System-level rating note.** The system-level current and target ratings shown above are determined by the highest material scenario and the Duckworks governance rules; they are not averages of the scenario scores.

## 9. AI-005 - DuckTalent AI

*AI-supported CV parsing, candidate comparison, ranking, summarization and interview recommendation.*

| **Lifecycle**             | Concept           | **Risk owner**              | Beatrice Van Duck - Chief People Officer |
|---------------------------|-------------------|-----------------------------|------------------------------------------|
| **Control effectiveness** | Not Implemented   | **Evidence confidence**     | Low                                      |
| **Overall inherent risk** | **Critical (20)** | **Current residual risk**   | **Critical (20)**                        |
| **Target residual risk**  | **High (10)**     | **Current governance gate** | **Do not deploy in current state**       |

**Current decision:** Do not deploy. Legal assessment, impact/privacy assessment, fairness testing, meaningful human-oversight design, vendor due diligence and AI Governance Committee approval are mandatory preconditions.

### Baseline risk scenarios

| **AI-005-R01** | **Fundamental rights & fairness** | **Scenario risk progression** |
|----------------|-----------------------------------|-------------------------------|

| **Cause**                       | Training data, features, criteria, or proxy variables encode historical or structural bias.                                      |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| **Event**                       | DuckTalent systematically ranks members of a protected or otherwise disadvantaged group lower.                                   |
| **Impact**                      | Applicants experience discriminatory or unfair restriction of access to employment, with associated legal and reputational harm. |
| **Inherent risk**               | **Severity 5 x Likelihood 4 = 20 Critical**                                                                                      |
| **Existing controls credited**  | No implemented control; concept-stage principles only.                                                                           |
| **Current residual risk**       | **Severity 5 x Likelihood 4 = 20 Critical**                                                                                      |
| **Target treatment / controls** | Legal review; job-relevance controls; representative testing; fairness metrics; adverse-impact investigation; challenge process. |
| **Target residual risk**        | **Severity 5 x Likelihood 2 = 10 High**                                                                                          |

#### Implementation evidence — AI-005-R01 / DT-01 / DT-02

A worked pre-deployment fairness-control demonstration is available at:

[`../80-operating-evidence/AI-005-ducktalent/`](../80-operating-evidence/AI-005-ducktalent/)

The evidence chain links the preventive dependency **`DT-01 — Job-Relevance Criteria & Proxy Feature Governance`** to the detective control **`DT-02 — Pre-Deployment Fairness & Adverse-Impact Testing`** and demonstrates, using synthetic portfolio data:

- a synthetic approved-feature allow-list;
- 24 synthetic applicants arranged as 12 matched pairs;
- an executable fairness/adverse-impact test;
- a deliberately seeded unapproved `Career_Gap_Months` scoring penalty;
- matched-pair score comparisons;
- selection-rate, true-positive-rate and false-negative-rate diagnostics;
- detection of the unapproved feature and its measurable effect;
- a pre-deployment `BLOCK` result;
- generated exception evidence;
- remediation by removing the unapproved feature;
- full-population retesting; and
- a control-test conclusion that a passing synthetic retest results only in **Eligible for further governance review**.

**Evidence state:** **Designed → Synthetic technical implementation demonstrated → Synthetic fairness execution demonstrated → Synthetic operation tested.**

**Assurance boundary:** The package does not use real applicants or real protected-characteristic data and does not establish production job relevance, real applicant fairness, lawful fairness-data processing, legal non-discrimination compliance, accessibility performance, candidate remedy effectiveness, or actual DuckTalent model behavior.

Accordingly, `DT-02` may be classified as **Partially implemented within the synthetic portfolio boundary**, while `DT-01` remains **Not implemented**. This evidence does **not** provide current residual-risk reduction credit. DuckTalent remains system-level **Critical (20)**, **Not Implemented**, **Low evidence confidence**, and **Do not deploy in current state**.

| **AI-005-R02** | **Human oversight & automation bias** | **Scenario risk progression** |
|----------------|---------------------------------------|-------------------------------|

| **Cause**                       | Recruiters place excessive trust in AI rankings or summaries.                                                           |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| **Event**                       | A flawed recommendation becomes the de facto screening or selection decision despite nominal human review.              |
| **Impact**                      | Qualified candidates are unfairly screened out and human accountability becomes ineffective.                            |
| **Inherent risk**               | **Severity 4 x Likelihood 4 = 16 High**                                                                                 |
| **Existing controls credited**  | Planned human review; no-automated-rejection principle not yet implemented.                                             |
| **Current residual risk**       | **Severity 4 x Likelihood 4 = 16 High**                                                                                 |
| **Target treatment / controls** | Human-oversight procedure; forced rationale; no automated rejection; reviewer training; override and appeal monitoring. |
| **Target residual risk**        | **Severity 4 x Likelihood 2 = 8 Moderate**                                                                              |

| **AI-005-R03** | **Privacy & data governance** | **Scenario risk progression** |
|----------------|-------------------------------|-------------------------------|

| **Cause**                       | CV or application data contains sensitive attributes or proxy information beyond what is necessary for recruitment.                            |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **Event**                       | The system infers, processes, or uses those attributes in ranking, summarization, or recommendations.                                          |
| **Impact**                      | Applicants face privacy intrusion, inappropriate profiling, discrimination exposure, or inability to understand/correct the use of their data. |
| **Inherent risk**               | **Severity 4 x Likelihood 3 = 12 High**                                                                                                        |
| **Existing controls credited**  | No production data; vendor not selected.                                                                                                       |
| **Current residual risk**       | **Severity 4 x Likelihood 3 = 12 High**                                                                                                        |
| **Target treatment / controls** | Data minimization; field exclusion; DPIA/privacy review; vendor restrictions; retention controls.                                              |
| **Target residual risk**        | **Severity 4 x Likelihood 2 = 8 Moderate**                                                                                                     |

**System-level rating note.** The system-level current and target ratings shown above are determined by the highest material scenario and the Duckworks governance rules; they are not averages of the scenario scores.

## 10. AI-006 - PondGPT

*Internal generative-AI assistant for drafting, research, knowledge retrieval, meeting summaries and coding support.*

| **Lifecycle**             | Pilot               | **Risk owner**              | Oliver Duckett - Head of IT & Cloud |
|---------------------------|---------------------|-----------------------------|-------------------------------------|
| **Control effectiveness** | Partially Effective | **Evidence confidence**     | Medium                              |
| **Overall inherent risk** | **High (16)**       | **Current residual risk**   | **High (12)**                       |
| **Target residual risk**  | **Moderate (8)**    | **Current governance gate** | **Restricted pilot only**           |

**Current decision:** Continue the restricted pilot; sensitive repositories remain excluded until permission inheritance, DLP, prompt-injection and logging controls are verified.

### Baseline risk scenarios

| **AI-006-R01** | **Privacy & data governance** | **Scenario risk progression** |
|----------------|-------------------------------|-------------------------------|

| **Cause**                       | Retrieval permissions or connector authorization are configured incorrectly.                                            |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| **Event**                       | PondGPT returns restricted internal information to a user who is not authorized to access the underlying source.        |
| **Impact**                      | Sensitive IP, customer data, employee information, or other confidential content is disclosed across access boundaries. |
| **Inherent risk**               | **Severity 4 x Likelihood 4 = 16 High**                                                                                 |
| **Existing controls credited**  | SSO; source authorization inheritance; restricted pilot repositories.                                                   |
| **Current residual risk**       | **Severity 4 x Likelihood 3 = 12 High**                                                                                 |
| **Target treatment / controls** | Automated permission-regression tests; DLP; sensitive-source denylist; logging and alerting.                            |
| **Target residual risk**        | **Severity 4 x Likelihood 2 = 8 Moderate**                                                                              |

#### Implementation evidence — AI-006-R01 / PG-01 / PG-02

A worked technical-control demonstration for the PondGPT authorization boundary is available at:

[`../80-operating-evidence/AI-006-pondgpt/`](../80-operating-evidence/AI-006-pondgpt/)

The evidence chain links the preventive control **`PG-01 — Permission-Aware Retrieval`** to the detective control **`PG-02 — Automated Permission Regression & DLP Tests`** and demonstrates, using synthetic portfolio data:

- a versioned authorization matrix with permitted and denied source access;
- an executable Python regression control using synthetic personas and repositories;
- positive and negative permission assertions;
- pilot-source exclusions and DLP assertions;
- entitlement removal/addition regression;
- one deliberately seeded Finance connector ACL defect;
- detection of the resulting unauthorized retrieval condition;
- alert and exception generation;
- connector/corpus expansion blocking;
- remediation and successful retesting; and
- a full-population control-test workpaper over 20 synthetic assertions.

**Evidence state:** **Designed → Synthetic technical implementation demonstrated → Synthetic technical execution demonstrated → Synthetic operation tested.**

**Assurance boundary:** The package does not establish actual PondGPT source-system authorization inheritance, real connector ACL configuration, production identity synchronization, real DLP/SSE/CASB enforcement, actual SIEM alerting, sustained weekly execution, or a measured unauthorized-retrieval escape rate.

Accordingly, this synthetic evidence package does **not** provide additional residual-risk reduction credit. The current `AI-006-R01` residual risk, system-level **High (12)** rating, **Partially Effective** control status, **Medium** evidence confidence, and **Restricted pilot only** gate remain unchanged by this portfolio demonstration.

| **AI-006-R02** | **Security & adversarial manipulation** | **Scenario risk progression** |
|----------------|-----------------------------------------|-------------------------------|

| **Cause**                       | A malicious prompt or poisoned retrieved document contains instructions intended to manipulate the assistant.         |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| **Event**                       | The assistant follows the malicious instruction, exposes data, produces unsafe output, or misuses an integrated tool. |
| **Impact**                      | Confidentiality, integrity, code security, or business operations are compromised.                                    |
| **Inherent risk**               | **Severity 4 x Likelihood 4 = 16 High**                                                                               |
| **Existing controls credited**  | Restricted connectors; logging; pilot controls.                                                                       |
| **Current residual risk**       | **Severity 4 x Likelihood 3 = 12 High**                                                                               |
| **Target treatment / controls** | Injection testing; content provenance; tool sandboxing; allowlisted actions; response monitoring.                     |
| **Target residual risk**        | **Severity 4 x Likelihood 2 = 8 Moderate**                                                                            |

| **AI-006-R03** | **Reliability & robustness** | **Scenario risk progression** |
|----------------|------------------------------|-------------------------------|

| **Cause**                       | PondGPT generates hallucinated code or incorrect operational guidance.                                        |
|---------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Event**                       | An employee uses the output without adequate verification.                                                    |
| **Impact**                      | Vulnerable code, erroneous configuration, incorrect business action, or operational disruption is introduced. |
| **Inherent risk**               | **Severity 4 x Likelihood 3 = 12 High**                                                                       |
| **Existing controls credited**  | Mandatory user responsibility; pilot guidance.                                                                |
| **Current residual risk**       | **Severity 4 x Likelihood 3 = 12 High**                                                                       |
| **Target treatment / controls** | Secure-code scanning; human review for consequential outputs; source grounding; user training.                |
| **Target residual risk**        | **Severity 4 x Likelihood 2 = 8 Moderate**                                                                    |

**System-level rating note.** The system-level current and target ratings shown above are determined by the highest material scenario and the Duckworks governance rules; they are not averages of the scenario scores.

## 11. AI-007 - Unregistered GenAI Usage

*Discovered employee use of public or unapproved generative-AI services across multiple business processes.*

| **Lifecycle**             | Discovered / uncontrolled | **Risk owner**              | Reginald Duckman - CRCO / business owners by discovered use |
|---------------------------|---------------------------|-----------------------------|-------------------------------------------------------------|
| **Control effectiveness** | Weak                      | **Evidence confidence**     | Low                                                         |
| **Overall inherent risk** | **Critical (20)**         | **Current residual risk**   | **Critical (20)**                                           |
| **Target residual risk**  | **High (10)**             | **Current governance gate** | **Immediate containment and decomposition**                 |

**Current decision:** Immediate treatment: contain exposure, provide approved alternatives, discover individual use cases, assign owners, and run each material use through normal intake, legal triage, impact/risk assessment and approval.

### Baseline risk scenarios

| **AI-007-R01** | **Privacy & data governance** | **Scenario risk progression** |
|----------------|-------------------------------|-------------------------------|

| **Cause**                       | An employee uploads confidential, IP, customer, HR, source-code, or personal data to an unapproved public AI service.          |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| **Event**                       | The provider retains, trains on, transfers, or otherwise exposes the information outside Duckworks' approved control boundary. |
| **Impact**                      | Confidentiality, privacy, intellectual-property, contractual, or incident-response consequences arise.                         |
| **Inherent risk**               | **Severity 5 x Likelihood 4 = 20 Critical**                                                                                    |
| **Existing controls credited**  | Limited awareness; no consistent technical enforcement.                                                                        |
| **Current residual risk**       | **Severity 5 x Likelihood 4 = 20 Critical**                                                                                    |
| **Target treatment / controls** | Approved-tool catalogue; DLP/CASB/SSE discovery; blocking; awareness; exception workflow.                                      |
| **Target residual risk**        | **Severity 5 x Likelihood 2 = 10 High**                                                                                        |

| **AI-007-R02** | **Legal / compliance** | **Scenario risk progression** |
|----------------|------------------------|-------------------------------|

| **Cause**                       | Unregistered AI is introduced into HR, customer, engineering, or another consequential process without governance intake.             |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| **Event**                       | Applicable legal, regulatory, contractual, policy, or human-oversight requirements are not identified before outputs are relied upon. |
| **Impact**                      | Duckworks operates unlawful or uncontrolled decision support and cannot demonstrate appropriate accountability or evidence.           |
| **Inherent risk**               | **Severity 5 x Likelihood 3 = 15 High**                                                                                               |
| **Existing controls credited**  | No centralized inventory or control over the individual use cases.                                                                    |
| **Current residual risk**       | **Severity 5 x Likelihood 3 = 15 High**                                                                                               |
| **Target treatment / controls** | Mandatory registration; periodic attestations; manager accountability; risk-based approval before consequential use.                  |
| **Target residual risk**        | **Severity 5 x Likelihood 2 = 10 High**                                                                                               |

| **AI-007-R03** | **Third-party & supply chain** | **Scenario risk progression** |
|----------------|--------------------------------|-------------------------------|

| **Cause**                       | Employees use unknown public AI vendors, browser extensions, plugins, or embedded AI features with unreviewed terms.                         |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| **Event**                       | Company data is processed under unknown retention, training, security, subprocessor, or service-change conditions.                           |
| **Impact**                      | Unmanaged third-party exposure persists and Duckworks lacks contractual leverage, assurance evidence, incident visibility, or exit controls. |
| **Inherent risk**               | **Severity 4 x Likelihood 4 = 16 High**                                                                                                      |
| **Existing controls credited**  | Ad hoc browser/security controls.                                                                                                            |
| **Current residual risk**       | **Severity 4 x Likelihood 4 = 16 High**                                                                                                      |
| **Target treatment / controls** | Vendor allowlist; extension controls; procurement gate; contractual, privacy, and security review.                                           |
| **Target residual risk**        | **Severity 4 x Likelihood 2 = 8 Moderate**                                                                                                   |

**System-level rating note.** The system-level current and target ratings shown above are determined by the highest material scenario and the Duckworks governance rules; they are not averages of the scenario scores.

## 12. Cross-Portfolio Risk Themes

The following themes consolidate the baseline scenarios without creating new risk scores. They are useful for control-library design and assurance planning.

| **Theme**                                        | **Systems represented**                                       | **Governance implication**                                                                                                                                                   |
|--------------------------------------------------|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Product safety and quality**                   | DuckDesign; WingInspect                                       | Human final authority, validation criteria, change-triggered revalidation, safety evidence, and fail-safe/manual fallback must be explicit.                                  |
| **Generative-AI reliability and hallucination**  | DuckDesign; QuackBot; PondGPT                                 | Grounding, benchmark/evaluation suites, human verification, abstention/escalation, and monitoring are recurring controls.                                                    |
| **Prompt injection and adversarial content**     | QuackBot; PondGPT; shadow AI                                  | Least privilege, content isolation, connector/tool boundaries, adversarial testing, provenance, logging, and response monitoring are required where relevant.                |
| **Confidentiality, privacy and IP**              | DuckDesign; FeatherForecast; DuckTalent; PondGPT; shadow AI   | Data minimization, approved data scope, access controls, DLP, vendor terms, privacy review, and evidence of authorization are recurring requirements.                        |
| **Automation bias and ineffective human review** | DuckDesign; FeatherForecast; WingInspect; DuckTalent; PondGPT | Human involvement must be competent, informed and empowered to override, reject, pause, or escalate rather than nominal.                                                     |
| **Drift and change risk**                        | FeatherForecast; WingInspect; DuckDesign; PondGPT             | Model, data, product-line, camera, connector and version changes must be treated as reassessment triggers with regression/revalidation evidence.                             |
| **Third-party and shadow AI exposure**           | QuackBot; PondGPT; DuckDesign; AI-007                         | Vendor/model due diligence, data-use terms, provider-change monitoring, extension controls, approved-tool catalogues and exit arrangements are material governance controls. |

## 13. Scenario Maintenance and Reassessment

A scenario must be reviewed or a new scenario added when a material change alters the risk context. Duckworks baseline triggers include:

- change in intended purpose, autonomy, or decision authority;

- new model, provider, model version, or substantial configuration change;

- new data categories, sensitive sources, connectors, APIs, or permissions;

- expansion to new users, affected groups, countries, product lines, or safety-relevant functions;

- material incident, near miss, complaint, security event, rights challenge, or loss of human oversight;

- drift, performance threshold breach, change in error distribution, or evidence expiry;

- control failure or a material change in control effectiveness; or

- new or amended legal, regulatory, contractual, or internal policy requirement.

**AI-007 special rule.** Unregistered GenAI Usage is an organizational discovery condition, not a single homogeneous AI system. Each materially distinct discovered use must be decomposed into its own inventory record, owner, intended purpose, risk scenarios, legal triage, assessment, controls, approval and monitoring.

## 14. Source Basis and Evidence Boundary

This register is derived from the existing Duckworks Project W.I.N.G. source set. It does not introduce real incidents, measured production performance, or new legal conclusions. Where synthetic worked evidence is created for portfolio demonstration, it is cross-referenced explicitly and must not be interpreted as production operating-effectiveness evidence or as justification for additional residual-risk credit.

| **Source artifact**                                                | **Use in this register**                                                                                                                |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **Duckworks AI Risk Assessment Report v1.0**                       | Primary source for the 21 baseline scenarios, scenario scores, credited controls, target treatments, owners and lifecycle decisions.    |
| **Duckworks AI System Inventory - Risk Assessed**                  | Structured scenario rows and system-level inherent/current/target risk, control effectiveness, evidence confidence and review context.  |
| **Duckworks AI Risk Classification & Assessment Methodology v1.0** | Cause -\> event -\> impact formulation, 5x5 severity/likelihood method, thresholds, control-evidence rules and reassessment principles. |
| **Duckworks AI Asset Inventory v1.0**                              | Current system identity, owners, lifecycle, data context, key risks, controls, KPIs/KRIs and governance gates.                          |
| **Duckworks AI Business Use Case Portfolio v1.0**                  | Business purpose, human decision boundaries and current use constraints.                                                                |
| **Duckworks Project Assumptions Register v1.0**                    | Open/critical assumptions, evidence boundaries and change triggers.                                                                     |
| **Duckworks AI RACI Chart v1.0**                                   | System owner map, specialist challenge roles, committee approval and Internal Audit independence.                                       |
| **Duckworks Responsible Use Policy and Governance Lifecycle SOP**  | Operational release gates, stop-use criteria, shadow-AI handling and evidence expectations.                                             |
| **AI-004 WingInspect Operating Evidence Package**                  | Synthetic worked example linking AI-004-R01 to canonical control `WI-01`, inspection execution records, human override evidence and a control-test workpaper; not production operating-effectiveness evidence. |
| **AI-005 DuckTalent DT-02 Operating Evidence Package**             | Synthetic executable worked example linking AI-005-R01 to `DT-01` / `DT-02`, matched applicant pairs, seeded unapproved feature, diagnostic fairness metrics, deployment blocking, remediation and retest; not real-applicant fairness, legal discrimination analysis, or production operating-effectiveness evidence. |
| **AI-006 PondGPT PG-02 Operating Evidence Package**                | Synthetic executable worked example linking AI-006-R01 to `PG-01` / `PG-02`, an authorization matrix, permission-regression code, seeded authorization defect, exception/gate evidence, remediation retest and control-test workpaper; not production operating-effectiveness evidence. |

**Evidence discipline.** Existing controls shown in this register are those credited in the baseline assessment. Their presence in the document does not independently prove operating effectiveness. Target treatments are planned states and must not be represented as current controls until implementation and evidence are verified. Synthetic execution or test artifacts may demonstrate control design and workflow logic, but they must not be represented as production operating-effectiveness evidence unless supported by sustained real operational data and appropriate assurance.
