# Duckworks Synthetic AI System Inventory

Six governed Project W.I.N.G. use cases - complete inventory and assumption traceability

| **Document version** | 1.0                                                                                                                                                                                             |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Status**           | Portfolio Baseline - Synthetic                                                                                                                                                                  |
| **Organization**     | Duckworks (fictional)                                                                                                                                                                           |
| **Scope**            | AI-001 through AI-006; AI-007 Unregistered GenAI Usage excluded from this six-system inventory                                                                                                  |
| **Data boundary**    | Fictional, synthetic, anonymized, or public information only                                                                                                                                    |
| **Purpose**          | Provide a CSV-ready, auditable AI system inventory with owners, vendors, data categories, lifecycle stages, risk indicators, monitoring requirements, governance decisions, and assumption IDs. |

**Portfolio use only. This report is not legal advice, certification evidence, or a statement of regulatory conformity.**

## 1. Executive Summary

This report creates a synthetic AI system inventory for the six registered Duckworks use cases AI-001 through AI-006. AI-007 Unregistered GenAI Usage is intentionally excluded because the Duckworks assumptions treat it as an organizational condition containing multiple uncontrolled use cases rather than one homogeneous approved AI system.

The inventory preserves the established Duckworks purposes, owners, lifecycle gates, internal impact indicators, and human-oversight boundaries. Fictional vendor names and implementation details were added only where the existing portfolio did not establish them; these additions are explicitly controlled through new Open assumptions ASM-025 through ASM-030.

Inclusion in this inventory does not mean unrestricted production approval. DuckDesign AI, WingInspect Vision, and PondGPT remain restricted pilots; QuackBot remains production-blocked pending governance gates; FeatherForecast may continue in production with monitoring; and DuckTalent AI must not be deployed in its current state.

The values Moderate, High, and Critical are Duckworks internal governance / impact indicators. They are not legal classifications and must not be interpreted as a determination that a system is or is not a high-risk AI system under the EU AI Act.

### 1.1 Portfolio Snapshot

| **Metric**                      | **Count** | **Interpretation**                         | **Governance significance**                                             |
|---------------------------------|-----------|--------------------------------------------|-------------------------------------------------------------------------|
| Registered systems              | 6         | AI-001 through AI-006                      | All six have named owners and traceable assumptions.                    |
| Restricted pilots               | 3         | DuckDesign; WingInspect; PondGPT           | Pilot use only until specified controls/evidence are validated.         |
| Production / operational        | 1         | FeatherForecast                            | Continue with manager approval and monitoring controls.                 |
| Production / deployment blocked | 2         | QuackBot; DuckTalent                       | Cannot proceed to unrestricted production in current state.             |
| High impact indicators          | 4         | DuckDesign; QuackBot; WingInspect; PondGPT | Enhanced governance, evidence, and pre-production gates.                |
| Critical impact indicators      | 1         | DuckTalent                                 | Deployment blocked pending material risk reduction and enhanced review. |

### 1.2 Inventory Design Principles

- Intended purpose first: records describe what each AI system is intended to do and the decision/support boundary around that use.

- Named accountability: every governed system has a business owner and technical owner drawn from the Duckworks stakeholder model.

- Human oversight is explicit: consequential employment, engineering, manufacturing quality, customer, and supply-chain decisions retain documented human authority.

- Third-party details are traceable: fictional vendors and platform arrangements are marked through Open assumptions rather than silently treated as established facts.

- Risk and legal classification are separate: Duckworks internal ratings support proportional governance but do not determine statutory classification.

- Evidence-driven change control: material changes in purpose, model, data, vendor, affected population, permissions, or decision authority should trigger reassessment.

## 2. Condensed Inventory

| **ID** | **System**         | **Function**                          | **Business owner**                              | **Lifecycle**                       | **Impact** | **Approval / gate**                                                                                                                                      |
|--------|--------------------|---------------------------------------|-------------------------------------------------|-------------------------------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| AI-001 | DuckDesign AI      | Product & Engineering                 | Felix Duckson - VP Product & Engineering        | Restricted Pilot                    | High       | Conditionally approved for restricted pilot only; production design use prohibited without required validation gates                                     |
| AI-002 | QuackBot           | Customer Operations                   | Clara Duckley - Director of Customer Operations | Pre-Production / Production Blocked | High       | Production not approved pending prompt/RAG security testing, escalation controls, content boundaries, and monitoring                                     |
| AI-003 | FeatherForecast    | Supply Chain & Manufacturing Planning | Tobias Duckman - Director of Supply Chain       | Production / Operational            | Moderate   | Approved to continue in production with documented monitoring and manager approval for material commitments                                              |
| AI-004 | WingInspect Vision | Manufacturing & Quality               | Henrietta Duckwell - Director of Manufacturing  | Restricted Pilot                    | High       | Conditionally approved for restricted pilot only; no unvalidated safety-critical reliance                                                                |
| AI-005 | DuckTalent AI      | Human Resources                       | Beatrice Van Duck - Chief People Officer        | Pre-Deployment / Deployment Blocked | Critical   | Do not deploy in current state; deployment blocked until critical risk is reduced and enhanced governance gates are satisfied                            |
| AI-006 | PondGPT            | Enterprise IT & Employee Productivity | Oliver Duckett - Head of IT & Cloud             | Restricted Pilot                    | High       | Conditionally approved for restricted pilot only; broader rollout blocked until access, logging, RAG security, and acceptable-use controls are validated |

Note: the condensed table is a management view. The system profiles below contain the complete CSV-ready field set.

## 3.1 AI-001 - DuckDesign AI

**Restricted Pilot \| Internal impact indicator: High**

| **AI ID**                    | AI-001                                                                                                                                                                       |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **System name**              | DuckDesign AI                                                                                                                                                                |
| **Business function**        | Product & Engineering                                                                                                                                                        |
| **Intended purpose**         | Assist engineers with design generation; component optimization; material selection; CAD workflows; simulation support; and comparison of alternative mechanical-arm designs |
| **Business owner**           | Felix Duckson - VP Product & Engineering                                                                                                                                     |
| **Technical owner**          | Dr. Ada Duckfield - Head of Data & AI                                                                                                                                        |
| **AI technology**            | Generative AI; engineering decision-support; computational design                                                                                                            |
| **Development model**        | Duckworks-developed engineering workflow using third-party foundation-model services                                                                                         |
| **Vendor**                   | AetherForge AI GmbH (fictional)                                                                                                                                              |
| **Lifecycle stage**          | Restricted Pilot                                                                                                                                                             |
| **Primary users**            | Mechanical engineers; product-design teams                                                                                                                                   |
| **Affected parties**         | Mechanical engineers; product users indirectly through downstream design decisions                                                                                           |
| **Data categories**          | Confidential engineering IP; CAD files; technical specifications; materials data; simulation data; supplier component information                                            |
| **Human oversight**          | Competent engineer must review and validate outputs before prototyping or production; AI cannot authorize production design                                                  |
| **Third-party involvement**  | Yes - hosted foundation-model/API capability integrated into Duckworks engineering workflow                                                                                  |
| **Current impact indicator** | High                                                                                                                                                                         |
| **Primary risk indicators**  | Unsafe or invalid design recommendations; hallucinated engineering information; IP leakage; automation bias; model/service change; third-party dependency                    |
| **Assessment status**        | Baseline risk and impact assessment completed; control-validation actions remain                                                                                             |
| **Approval status**          | Conditionally approved for restricted pilot only; production design use prohibited without required validation gates                                                         |
| **Monitoring requirements**  | Design-validation failures; override/rejection rate; unsafe recommendation events; model/version changes; security events; IP/data-control exceptions                        |
| **Assumption IDs**           | ASM-005; ASM-007; ASM-012; ASM-013; ASM-025                                                                                                                                  |

### Control and monitoring interpretation

The monitoring requirements listed above are governance indicators for the synthetic portfolio. They should be converted into measurable thresholds, ownership, evidence sources, and escalation rules in the later AI Monitoring & Reassessment Standard.

### Assumption traceability

Material implementation details and governance boundaries for this system are traceable through: ASM-005; ASM-007; ASM-012; ASM-013; ASM-025.

## 3.2 AI-002 - QuackBot

**Pre-Production / Production Blocked \| Internal impact indicator: High**

| **AI ID**                    | AI-002                                                                                                                                                                        |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **System name**              | QuackBot                                                                                                                                                                      |
| **Business function**        | Customer Operations                                                                                                                                                           |
| **Intended purpose**         | Answer common customer questions; retrieve technical product information; provide troubleshooting and warranty guidance; and escalate complex or sensitive cases              |
| **Business owner**           | Clara Duckley - Director of Customer Operations                                                                                                                               |
| **Technical owner**          | Dr. Ada Duckfield - Head of Data & AI                                                                                                                                         |
| **AI technology**            | Generative AI; conversational AI; retrieval-augmented generation                                                                                                              |
| **Development model**        | Duckworks-managed customer chatbot and RAG layer using third-party hosted LLM services                                                                                        |
| **Vendor**                   | HelixRiver AI Services S.A. (fictional)                                                                                                                                       |
| **Lifecycle stage**          | Pre-Production / Production Blocked                                                                                                                                           |
| **Primary users**            | Customers; product users; customer-support personnel                                                                                                                          |
| **Affected parties**         | Customers; product users; customer-service employees                                                                                                                          |
| **Data categories**          | Customer contact and account information; support history; warranty information; chat transcripts; product documentation; troubleshooting knowledge                           |
| **Human oversight**          | Uncertain, sensitive, safety-related, or out-of-scope interactions must be escalated to human customer-support staff                                                          |
| **Third-party involvement**  | Yes - hosted LLM/model service; Duckworks manages application, knowledge retrieval, escalation, and monitoring                                                                |
| **Current impact indicator** | High                                                                                                                                                                          |
| **Primary risk indicators**  | Prompt injection; retrieval poisoning; hallucinated technical advice; customer misinformation; confidential-data leakage; excessive data retrieval; service dependency        |
| **Assessment status**        | Baseline risk and impact assessment completed; security and customer-impact gates remain open                                                                                 |
| **Approval status**          | Production not approved pending prompt/RAG security testing, escalation controls, content boundaries, and monitoring                                                          |
| **Monitoring requirements**  | Hallucination/error rate; escalation rate; unresolved customer complaints; prompt-injection events; sensitive-data exposure; retrieval-quality failures; vendor/model changes |
| **Assumption IDs**           | ASM-005; ASM-010; ASM-012; ASM-013; ASM-026                                                                                                                                   |

### Control and monitoring interpretation

The monitoring requirements listed above are governance indicators for the synthetic portfolio. They should be converted into measurable thresholds, ownership, evidence sources, and escalation rules in the later AI Monitoring & Reassessment Standard.

### Assumption traceability

Material implementation details and governance boundaries for this system are traceable through: ASM-005; ASM-010; ASM-012; ASM-013; ASM-026.

## 3.3 AI-003 - FeatherForecast

**Production / Operational \| Internal impact indicator: Moderate**

| **AI ID**                    | AI-003                                                                                                                                                      |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **System name**              | FeatherForecast                                                                                                                                             |
| **Business function**        | Supply Chain & Manufacturing Planning                                                                                                                       |
| **Intended purpose**         | Forecast product demand; inventory requirements; manufacturing volumes; component shortages; and supplier demand                                            |
| **Business owner**           | Tobias Duckman - Director of Supply Chain                                                                                                                   |
| **Technical owner**          | Dr. Ada Duckfield - Head of Data & AI                                                                                                                       |
| **AI technology**            | Predictive machine learning; time-series forecasting; demand analytics                                                                                      |
| **Development model**        | Duckworks-configured forecasting models operating on a third-party analytics platform                                                                       |
| **Vendor**                   | Northstar Planning Analytics GmbH (fictional)                                                                                                               |
| **Lifecycle stage**          | Production / Operational                                                                                                                                    |
| **Primary users**            | Supply-chain planners; procurement personnel; manufacturing planners                                                                                        |
| **Affected parties**         | Duckworks operations; suppliers and logistics partners indirectly                                                                                           |
| **Data categories**          | Demand history; inventory levels; purchase-order data; production schedules; supplier lead times; component availability; aggregated order information      |
| **Human oversight**          | Forecasts support decisions only; authorized managers approve purchasing and production commitments                                                         |
| **Third-party involvement**  | Yes - third-party analytics/ML platform with Duckworks-owned configuration and business rules                                                               |
| **Current impact indicator** | Moderate                                                                                                                                                    |
| **Primary risk indicators**  | Forecast drift; inaccurate demand prediction; poor data quality; inventory imbalance; supplier disruption; over-reliance on forecasts; vendor availability  |
| **Assessment status**        | Baseline risk and impact assessment completed                                                                                                               |
| **Approval status**          | Approved to continue in production with documented monitoring and manager approval for material commitments                                                 |
| **Monitoring requirements**  | Forecast accuracy; forecast error by product family; drift; shortage prediction accuracy; inventory variance; manual override rate; data-quality exceptions |
| **Assumption IDs**           | ASM-005; ASM-011; ASM-012; ASM-013; ASM-027                                                                                                                 |

### Control and monitoring interpretation

The monitoring requirements listed above are governance indicators for the synthetic portfolio. They should be converted into measurable thresholds, ownership, evidence sources, and escalation rules in the later AI Monitoring & Reassessment Standard.

### Assumption traceability

Material implementation details and governance boundaries for this system are traceable through: ASM-005; ASM-011; ASM-012; ASM-013; ASM-027.

## 3.4 AI-004 - WingInspect Vision

**Restricted Pilot \| Internal impact indicator: High**

| **AI ID**                    | AI-004                                                                                                                                                          |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **System name**              | WingInspect Vision                                                                                                                                              |
| **Business function**        | Manufacturing & Quality                                                                                                                                         |
| **Intended purpose**         | Analyze production-line images to identify missing components; assembly problems; cracks; surface defects; and other potential quality issues                   |
| **Business owner**           | Henrietta Duckwell - Director of Manufacturing                                                                                                                  |
| **Technical owner**          | Dr. Ada Duckfield - Head of Data & AI                                                                                                                           |
| **AI technology**            | Computer vision; image classification; defect detection                                                                                                         |
| **Development model**        | Duckworks manufacturing-quality workflow using third-party computer-vision components                                                                           |
| **Vendor**                   | VisiCore Industrial AI GmbH (fictional)                                                                                                                         |
| **Lifecycle stage**          | Restricted Pilot                                                                                                                                                |
| **Primary users**            | Manufacturing inspectors; quality engineers                                                                                                                     |
| **Affected parties**         | Manufacturing inspectors; production teams; downstream product users                                                                                            |
| **Data categories**          | Manufacturing-line images; component images; product identifiers; batch records; defect labels; quality-inspection results                                      |
| **Human oversight**          | Qualified human inspectors retain final acceptance/rejection authority; AI flags potential defects but cannot independently release products                    |
| **Third-party involvement**  | Yes - third-party computer-vision runtime/model components integrated into Duckworks quality systems                                                            |
| **Current impact indicator** | High                                                                                                                                                            |
| **Primary risk indicators**  | False negatives; missed safety-relevant defects; false positives; performance drift; image-quality sensitivity; automation bias; adversarial or abnormal inputs |
| **Assessment status**        | Baseline risk and impact assessment completed; validation actions remain                                                                                        |
| **Approval status**          | Conditionally approved for restricted pilot only; no unvalidated safety-critical reliance                                                                       |
| **Monitoring requirements**  | False-negative rate; false-positive rate; defect recall; inspector override rate; image-quality failures; drift; missed-defect incidents; model/version changes |
| **Assumption IDs**           | ASM-005; ASM-008; ASM-012; ASM-013; ASM-028                                                                                                                     |

### Control and monitoring interpretation

The monitoring requirements listed above are governance indicators for the synthetic portfolio. They should be converted into measurable thresholds, ownership, evidence sources, and escalation rules in the later AI Monitoring & Reassessment Standard.

### Assumption traceability

Material implementation details and governance boundaries for this system are traceable through: ASM-005; ASM-008; ASM-012; ASM-013; ASM-028.

## 3.5 AI-005 - DuckTalent AI

**Pre-Deployment / Deployment Blocked \| Internal impact indicator: Critical**

| **AI ID**                    | AI-005                                                                                                                                                                                                            |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **System name**              | DuckTalent AI                                                                                                                                                                                                     |
| **Business function**        | Human Resources                                                                                                                                                                                                   |
| **Intended purpose**         | Parse CVs; extract qualifications and experience; compare applicants with predefined job criteria; summarize applications; rank candidates; and recommend candidates for human review                             |
| **Business owner**           | Beatrice Van Duck - Chief People Officer                                                                                                                                                                          |
| **Technical owner**          | Dr. Ada Duckfield - Head of Data & AI                                                                                                                                                                             |
| **AI technology**            | Machine learning; NLP; ranking and recommendation; recruitment decision-support                                                                                                                                   |
| **Development model**        | Third-party recruitment AI SaaS configured using Duckworks job criteria and workflow rules                                                                                                                        |
| **Vendor**                   | MeritPath HR Technologies S.A. (fictional)                                                                                                                                                                        |
| **Lifecycle stage**          | Pre-Deployment / Deployment Blocked                                                                                                                                                                               |
| **Primary users**            | Recruiters; hiring managers; HR personnel                                                                                                                                                                         |
| **Affected parties**         | Job applicants; recruiters; hiring managers                                                                                                                                                                       |
| **Data categories**          | Applicant identity and contact data; CVs; employment history; qualifications; education; skills; application metadata; recruiter annotations; job criteria                                                        |
| **Human oversight**          | AI may rank and recommend candidates but cannot autonomously reject, shortlist, hire, or issue final employment decisions; meaningful recruiter review required                                                   |
| **Third-party involvement**  | Yes - externally hosted recruitment AI SaaS handling applicant personal data                                                                                                                                      |
| **Current impact indicator** | Critical                                                                                                                                                                                                          |
| **Primary risk indicators**  | Discrimination; disparate candidate outcomes; inappropriate proxy variables; privacy; ranking errors; explainability limitations; automation bias; lack of contestability; employment impact; regulatory exposure |
| **Assessment status**        | Baseline risk and impact assessment completed; enhanced legal, privacy, fairness, and control validation remains required                                                                                         |
| **Approval status**          | Do not deploy in current state; deployment blocked until critical risk is reduced and enhanced governance gates are satisfied                                                                                     |
| **Monitoring requirements**  | Selection-rate disparities; ranking consistency; human override rate; candidate complaints; contested decisions; model drift; data-quality issues; unexplained recommendation rate; vendor/model changes          |
| **Assumption IDs**           | ASM-005; ASM-006; ASM-012; ASM-013; ASM-029                                                                                                                                                                       |

### Control and monitoring interpretation

The monitoring requirements listed above are governance indicators for the synthetic portfolio. They should be converted into measurable thresholds, ownership, evidence sources, and escalation rules in the later AI Monitoring & Reassessment Standard.

### Assumption traceability

Material implementation details and governance boundaries for this system are traceable through: ASM-005; ASM-006; ASM-012; ASM-013; ASM-029.

## 3.6 AI-006 - PondGPT

**Restricted Pilot \| Internal impact indicator: High**

| **AI ID**                    | AI-006                                                                                                                                                                                                    |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **System name**              | PondGPT                                                                                                                                                                                                   |
| **Business function**        | Enterprise IT & Employee Productivity                                                                                                                                                                     |
| **Intended purpose**         | Provide employees with drafting; summarization; research; knowledge retrieval; coding assistance; meeting summaries; and answers to internal process questions                                            |
| **Business owner**           | Oliver Duckett - Head of IT & Cloud                                                                                                                                                                       |
| **Technical owner**          | Oliver Duckett - Head of IT & Cloud                                                                                                                                                                       |
| **AI technology**            | Generative AI; enterprise LLM assistant; retrieval-augmented generation                                                                                                                                   |
| **Development model**        | Duckworks enterprise AI application using a third-party hosted LLM with Duckworks-controlled identity, retrieval, and access enforcement                                                                  |
| **Vendor**                   | LanternMind Enterprise AI Ltd. (fictional)                                                                                                                                                                |
| **Lifecycle stage**          | Restricted Pilot                                                                                                                                                                                          |
| **Primary users**            | Duckworks employees                                                                                                                                                                                       |
| **Affected parties**         | Employees; internal data owners; customers or other individuals indirectly where their information is contained in permitted source material                                                              |
| **Data categories**          | Internal documents; policies; procedures; source code; meeting content; employee identity and access metadata; permitted customer and operational information                                             |
| **Human oversight**          | Users remain responsible for outputs; source-system permissions must be enforced; privileged or excluded repositories cannot be made accessible through AI retrieval                                      |
| **Third-party involvement**  | Yes - hosted enterprise LLM service integrated with Duckworks identity and internal knowledge sources                                                                                                     |
| **Current impact indicator** | High                                                                                                                                                                                                      |
| **Primary risk indicators**  | Prompt injection; indirect prompt injection; retrieval poisoning; cross-user data leakage; excessive permissions; sensitive-data disclosure; unsafe generated code; hallucination; third-party dependency |
| **Assessment status**        | Baseline risk and impact assessment completed; architecture and security controls require further validation                                                                                              |
| **Approval status**          | Conditionally approved for restricted pilot only; broader rollout blocked until access, logging, RAG security, and acceptable-use controls are validated                                                  |
| **Monitoring requirements**  | Prompt-injection detections; unauthorized retrieval attempts; sensitive-data events; hallucination/user-feedback rate; unsafe code findings; access-control failures; vendor/model changes                |
| **Assumption IDs**           | ASM-009; ASM-012; ASM-013; ASM-030                                                                                                                                                                        |

### Control and monitoring interpretation

The monitoring requirements listed above are governance indicators for the synthetic portfolio. They should be converted into measurable thresholds, ownership, evidence sources, and escalation rules in the later AI Monitoring & Reassessment Standard.

### Assumption traceability

Material implementation details and governance boundaries for this system are traceable through: ASM-009; ASM-012; ASM-013; ASM-030.

## 4. Assumption Traceability

The table below combines the existing assumptions directly referenced by the six inventory records with six new implementation/vendor assumptions. New assumptions are intentionally Open. They must not be represented as validated facts until the listed evidence is obtained.

| **ID**  | **Category**                            | **Assumption**                                                                                                                                                                                                                                | **Status** | **Materiality** | **Why it matters**                                                                                         | **Validation / evidence**                                                      | **Origin**                         |
|---------|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|-----------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|------------------------------------|
| ASM-005 | Human accountability                    | Humans retain formal accountability for employment, product release, quality, procurement, and material customer decisions.                                                                                                                   | Open       | Critical        | Human oversight affects impact, regulatory, and residual-risk conclusions.                                 | Validate per system                                                            | Existing Assumptions Register      |
| ASM-006 | DuckTalent purpose                      | DuckTalent parses, compares, ranks, and recommends job applicants but does not autonomously issue final rejection or hiring decisions.                                                                                                        | Validated  | Critical        | Materially affects employment impact and legal classification analysis.                                    | DuckTalent AIA                                                                 | Existing Assumptions Register      |
| ASM-007 | DuckDesign use                          | DuckDesign outputs are advisory and require competent engineer review before prototyping or production.                                                                                                                                       | Open       | Critical        | Safety and product risk depend on meaningful engineering validation.                                       | Pilot operating procedure                                                      | Existing Assumptions Register      |
| ASM-008 | WingInspect use                         | WingInspect flags defects but qualified human inspectors retain final acceptance/rejection authority.                                                                                                                                         | Open       | Critical        | Quality/safety exposure changes if the model becomes autonomous.                                           | Manufacturing procedure                                                        | Existing Assumptions Register      |
| ASM-009 | PondGPT access                          | PondGPT uses enterprise access controls and should not grant users access to documents they could not otherwise access.                                                                                                                       | Open       | Critical        | Controls cross-user leakage and privilege amplification.                                                   | Architecture evidence                                                          | Existing Assumptions Register      |
| ASM-010 | QuackBot escalation                     | QuackBot can escalate uncertain, sensitive, or safety-relevant interactions to human support staff.                                                                                                                                           | Open       | High            | Reduces customer harm and supports oversight.                                                              | Release design                                                                 | Existing Assumptions Register      |
| ASM-011 | FeatherForecast decisions               | FeatherForecast is decision support; purchasing and production commitments require authorized manager approval.                                                                                                                               | Open       | Medium          | Limits direct automation risk.                                                                             | Supply chain SOP                                                               | Existing Assumptions Register      |
| ASM-012 | Third-party mix                         | Duckworks uses a combination of internally developed AI components and third-party models/services.                                                                                                                                           | Validated  | High            | Requires both development governance and supplier risk controls.                                           | Architecture scenario                                                          | Existing Assumptions Register      |
| ASM-013 | Data                                    | AI systems may process confidential IP and, for selected systems, customer, employee, or applicant personal data.                                                                                                                             | Validated  | High            | Drives privacy, security, and data governance controls.                                                    | Inventory                                                                      | Existing Assumptions Register      |
| ASM-025 | DuckDesign vendor architecture          | DuckDesign AI uses a Duckworks-developed engineering workflow integrated with the fictional AetherForge AI GmbH hosted model service; Duckworks engineering data is contractually excluded from provider model training.                      | Open       | High            | Determines third-party, IP, confidentiality, training-data-use, and supplier-control requirements.         | Vendor contract; architecture diagram; data-use terms                          | New synthetic inventory assumption |
| ASM-026 | QuackBot vendor architecture            | QuackBot uses the fictional HelixRiver AI Services S.A. hosted LLM, while Duckworks controls the RAG knowledge base, customer-support workflow, and escalation logic; provider reuse of Duckworks prompts/content for training is prohibited. | Open       | High            | Determines customer-data exposure, supplier controls, RAG accountability, and data-use restrictions.       | Vendor contract; solution architecture; retention/training terms               | New synthetic inventory assumption |
| ASM-027 | FeatherForecast platform                | FeatherForecast uses the fictional Northstar Planning Analytics GmbH ML platform, with Duckworks controlling datasets, forecasting configuration, thresholds, and operational decisions.                                                      | Open       | Medium          | Clarifies provider dependency while retaining Duckworks accountability for data and operational decisions. | Platform architecture; configuration record; supplier agreement                | New synthetic inventory assumption |
| ASM-028 | WingInspect imaging scope               | WingInspect Vision uses fictional VisiCore Industrial AI components; production cameras are intended to capture products/components rather than perform employee surveillance or biometric identification.                                    | Open       | High            | Materially affects privacy, workforce-impact, security, and regulatory screening.                          | Camera field-of-view review; system design; privacy assessment                 | New synthetic inventory assumption |
| ASM-029 | DuckTalent vendor and decision boundary | DuckTalent AI is provided by fictional MeritPath HR Technologies S.A.; special-category attributes are not intended ranking features, and the system cannot autonomously reject or hire an applicant.                                         | Open       | Critical        | Affects fairness testing, privacy, legal classification, human oversight, and deployment decision.         | Vendor documentation; feature inventory; workflow configuration; HR procedure  | New synthetic inventory assumption |
| ASM-030 | PondGPT enterprise controls             | PondGPT uses fictional LanternMind Enterprise AI Ltd. under an enterprise arrangement providing tenant isolation and no provider training on Duckworks content; retrieval permissions inherit authorization from source systems.              | Open       | Critical        | Controls cross-user leakage, privilege amplification, third-party data use, and deployment scope.          | Contract; architecture evidence; access-control tests; retrieval security test | New synthetic inventory assumption |

### 4.1 New Assumption Change-Control Rule

Any new assumption that proves false, materially changes, or cannot be validated should trigger an inventory update and, where appropriate, a new impact assessment, risk assessment, legal triage, third-party review, security/privacy review, or governance approval. This follows the existing Duckworks assumption-management approach.

## 5. Governance Gates and Current Decisions

These decisions reproduce the current Duckworks portfolio position. They are governance / lifecycle gates, not legal-compliance conclusions.

| **AI ID** | **System**         | **Current gate**                 | **Impact** | **Minimum acceptance conditions**                                                                                                    |
|-----------|--------------------|----------------------------------|------------|--------------------------------------------------------------------------------------------------------------------------------------|
| AI-001    | DuckDesign AI      | Restricted pilot only            | High       | Competent engineer review; design validation; IP/data controls; no autonomous release to production design.                          |
| AI-002    | QuackBot           | Production blocked pending gates | High       | Prompt/RAG security testing; safe escalation; content boundaries; monitoring; customer-impact safeguards.                            |
| AI-003    | FeatherForecast    | Continue with monitoring         | Moderate   | Manager approval for material commitments; drift/performance monitoring; data-quality controls.                                      |
| AI-004    | WingInspect Vision | Restricted pilot only            | High       | Human inspector remains final authority; false-negative testing; no unvalidated safety-critical reliance.                            |
| AI-005    | DuckTalent AI      | Do not deploy in current state   | Critical   | Enhanced legal/privacy/fairness analysis; meaningful human review; bias testing; transparency/contestability; critical risk reduced. |
| AI-006    | PondGPT            | Restricted pilot only            | High       | Enterprise access enforcement; sensitive repository exclusions; prompt/RAG security; logging; acceptable-use controls.               |

## 6. Data Dictionary

| **Inventory field**          | **Definition**                                                                               |
|------------------------------|----------------------------------------------------------------------------------------------|
| **AI_ID**                    | Unique Duckworks AI inventory identifier.                                                    |
| **System_Name**              | Approved fictional name of the AI system/use case.                                           |
| **Business_Function**        | Primary business area accountable for the use case.                                          |
| **Intended_Purpose**         | Documented purpose and functional boundary of the AI system.                                 |
| **Business_Owner**           | Named first-line owner accountable for business outcomes and use-case controls.              |
| **Technical_Owner**          | Named owner accountable for architecture, implementation, operation, and technical evidence. |
| **AI_Technology**            | Primary AI/ML technology used by the system.                                                 |
| **Development_Model**        | Synthetic description of build/buy/integration approach.                                     |
| **Vendor**                   | Fictional third-party AI/model/platform provider introduced for portfolio realism.           |
| **Lifecycle_Stage**          | Current system lifecycle / governance-gate state.                                            |
| **Primary_Users**            | People or teams directly using/interacting with the system.                                  |
| **Affected_Parties**         | People/groups who may be materially affected directly or indirectly.                         |
| **Data_Categories**          | Primary categories of business, technical, and personal data processed.                      |
| **Human_Oversight**          | Required human review, decision authority, override, escalation, or accountability boundary. |
| **Third_Party_Involvement**  | Nature of external model, platform, SaaS, or API involvement.                                |
| **Current_Impact_Indicator** | Duckworks internal portfolio impact/risk indicator; not an EU AI Act legal classification.   |
| **Primary_Risk_Indicators**  | Material risk themes that drive governance and monitoring.                                   |
| **Assessment_Status**        | Status of baseline impact/risk assessment and remaining validation activity.                 |
| **Approval_Status**          | Current governance decision or production restriction.                                       |
| **Monitoring_Requirements**  | Key performance, security, rights, safety, and change indicators to monitor.                 |
| **Assumption_IDs**           | Traceability to controlled assumptions supporting material facts or unknowns.                |

## 7. Source Basis

The inventory is grounded in the existing Duckworks portfolio artifacts. The source list below identifies how each provided document was used. Fictional vendors and new implementation details are not source-derived facts; they are controlled synthetic assumptions recorded separately.

| **Source area**      | **Duckworks artifact**                                            | **Use in this inventory**                                                                                            |
|----------------------|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Business Scenario    | Duckworks AI Governance Project - Business Scenario               | Defines the six registered use cases, purposes, portfolio IDs, governance problem, and system-level context.         |
| Organization Profile | Duckworks - Fictional Organization Profile                        | Defines the fictional organization, AI environment, and named executives/system context.                             |
| Stakeholder Register | Duckworks AI Governance Project - Stakeholder Register            | Defines named business/technical owners and affected stakeholder groups.                                             |
| Assumptions Register | Duckworks AI Governance Project - Assumptions Register            | Defines existing controlled assumptions ASM-001 through ASM-024 and change-control rules.                            |
| Acceptance Criteria  | Duckworks AI Governance Project - Acceptance Criteria             | Defines lifecycle/release gates and impact levels for the seven baseline entries.                                    |
| Risk Methodology     | Duckworks AI Risk Classification & Assessment Methodology v1.0    | Defines internal Low/Moderate/High/Critical ratings and separates enterprise risk ratings from legal classification. |
| Project Objectives   | Duckworks AI Governance Project - Project Objectives              | Defines minimum inventory fields, traceability, monitoring, ownership, and evidence expectations.                    |
| Scope                | Duckworks AI Governance Project - In-Scope and Out-of-Scope Items | Defines inventory scope and portfolio boundaries, including synthetic-data-only requirement.                         |

## 8. Portfolio Disclaimer

Duckworks, Project W.I.N.G., all personnel, vendors, AI systems, datasets, risks, decisions, controls, and evidence referenced in this report are fictional and were created solely for educational and professional portfolio purposes. This inventory uses only synthetic/project information and public or fictional source material. It does not constitute legal advice, certification evidence, a conformity assessment, or a determination of regulatory applicability.
