# Duckworks AI Ethical Impact Assessment

Portfolio assessment of Project W.I.N.G. AI systems against human-centred, fairness, transparency, safety, privacy, well-being and accountability principles

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Assessment purpose</strong></p>
<p>This document evaluates the ethical implications of Duckworks' seven baseline AI entries. It complements the existing AI Impact Assessments, enterprise risk assessments, privacy assessments, fundamental-rights analysis, security reviews and legal triage. It does not replace any of them and does not convert voluntary ethical guidance into legal requirements.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| **Field**          | **Value**                                          |
|--------------------|----------------------------------------------------|
| Document ID        | DW-WING-ETH-01                                     |
| Version            | 1.0                                                |
| Status             | Portfolio Baseline                                 |
| Organization       | Duckworks (fictional)                              |
| Assessment owner   | Eleanor Duckford — AI Governance Lead              |
| Governance sponsor | Reginald Duckman — Chief Risk & Compliance Officer |
| Scope              | AI-001 through AI-007                              |
| Classification     | Portfolio / Synthetic / Non-production             |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Ethical posture</strong></p>
<p>The assessment uses ethics as a decision discipline: identify who benefits, who bears risk, where power or information asymmetry exists, whether people retain meaningful agency, whether impacts can be challenged or remedied, and whether the organization can justify and evidence the trade-offs it accepts.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 1. Executive Determination

Duckworks' AI portfolio contains materially different ethical profiles. The most serious ethical concerns arise where AI can affect access to employment, physical/product safety, confidentiality, privacy, or consequential decisions; where affected people have limited ability to understand or challenge outcomes; or where ownership and accountability are missing.

| **ID** | **System**               | **Ethical priority** | **Current decision**                              | **Primary ethical focus**                                                                                         |
|--------|--------------------------|----------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| AI-001 | DuckDesign AI            | E3 — Significant     | Restricted pilot only                             | Product safety, engineer agency, over-reliance, IP/confidentiality, traceability                                  |
| AI-002 | QuackBot                 | E3 — Significant     | Production blocked pending gates                  | Customer reliance, safety-adjacent advice, transparency, privacy, accessibility, contestability                   |
| AI-003 | FeatherForecast          | E2 — Material        | Continue with monitoring                          | Operational dependence, supplier fairness, workforce effects, explainability, sustainability trade-offs           |
| AI-004 | WingInspect Vision       | E3 — Significant     | Restricted pilot; no safety-critical release      | Product safety, automation bias, inspector agency, worker-monitoring repurposing, waste                           |
| AI-005 | DuckTalent AI            | E4 — Severe          | Do not deploy                                     | Employment opportunity, discrimination, dignity, privacy, accessibility, opacity, contestability, power imbalance |
| AI-006 | PondGPT                  | E3 — Significant     | Restricted pilot; sensitive repositories excluded | Workforce autonomy, privacy, surveillance risk, information integrity, deskilling, security                       |
| AI-007 | Unregistered GenAI Usage | E4 — Severe          | Immediate containment and decomposition           | Unknown purpose/data/vendors, absent accountability, privacy/IP leakage, hidden consequential use                 |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Overall conclusion</strong></p>
<p>Ethical acceptability cannot be established by business benefit alone. DuckTalent and Unregistered GenAI Usage are unacceptable in their current states. DuckDesign, QuackBot, WingInspect and PondGPT require enhanced safeguards and evidence before broader deployment. FeatherForecast is ethically manageable within its current decision-support boundary, provided human planning authority, transparency and monitoring remain effective.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 2. Assessment Boundary and Relationship to Other Duckworks Assessments

| **Assessment**               | **Question it answers**                                                                                                           | **Boundary**                                |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| AI Ethical Impact Assessment | Values, fairness, agency, dignity, transparency, accountability, societal/workforce/environmental effects and ethical trade-offs. | This document                               |
| AI Impact Assessment         | Positive/adverse effects on people, groups, society and organization for each system.                                             | Existing seven-system AIA pack              |
| AI Risk Assessment           | Scenario likelihood/severity, controls, inherent/current/target residual risk.                                                    | Existing enterprise risk methodology/report |
| EU AI Act / legal triage     | Prohibited/high-risk/transparency and other legal obligations where applicable.                                                   | Legal/Compliance                            |
| GDPR DPIA                    | Risks to rights and freedoms from personal-data processing and privacy safeguards.                                                | Separate when Article 35 applies            |
| Fundamental Rights / HUDERIA | Rights-specific and human-rights-focused assessment.                                                                              | Separate companion assessments              |
| Security / safety validation | Threat, robustness, product safety and technical test evidence.                                                                   | Separate specialist review                  |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>No duplication rule</strong></p>
<p>Where an existing Duckworks AIA, DPIA, FRIA or risk assessment already establishes a fact, this ethical assessment reuses that evidence rather than inventing a new fact or a conflicting score. Ethical conclusions are recorded separately because an issue can be ethically significant even when its legal status or quantitative risk score is different.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 3. Ethical Assessment Basis

| **Source**                                            | **Classification**                     | **Use in this assessment**                                                                                                                                                                                        |
|-------------------------------------------------------|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| European Commission AI HLEG Ethics Guidelines / ALTAI | Voluntary ethical guidance             | Seven requirements: human agency and oversight; technical robustness and safety; privacy/data governance; transparency; diversity/non-discrimination/fairness; societal/environmental well-being; accountability. |
| OECD AI Principles                                    | Intergovernmental voluntary principles | Inclusive growth/well-being; human-centred values and fairness; transparency/explainability; robustness/security/safety; accountability.                                                                          |
| NIST AI RMF 1.0                                       | Voluntary risk-management framework    | Trustworthy characteristics: valid/reliable; safe; secure/resilient; accountable/transparent; explainable/interpretable; privacy-enhanced; fair with harmful bias managed.                                        |
| ISO/IEC 42005:2025                                    | Voluntary impact-assessment guidance   | Understand and document how AI systems and foreseeable applications may affect individuals, groups and society across the lifecycle.                                                                              |
| EU AI Act and other applicable law                    | Binding law where applicable           | Legal obligations are screened separately. Ethical guidance cannot override or substitute mandatory legal requirements.                                                                                           |
| Duckworks internal governance                         | Organizational practice                | Risk appetite, human oversight, auditability, proportionality, evidence, change management, whistleblowing and stop-use rules.                                                                                    |

## 4. Duckworks Ethical Assessment Method

The ethical priority is a qualitative governance judgment, not a probability model, legal classification or 5×5 risk score. It reflects the seriousness of foreseeable ethical effects after considering affected people, vulnerability, scale, reversibility, power asymmetry, dependency, ability to understand/challenge an outcome, and the maturity of safeguards.

| **Priority**     | **Meaning**                                                                                                                          | **Governance response**                                               |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| E1 — Limited     | Low ethical tension in current bounded use; impacts are readily reversible and affected people retain meaningful agency.             | Routine controls and monitoring.                                      |
| E2 — Material    | Meaningful trade-offs or indirect impacts require documented safeguards, transparency and monitoring.                                | Owner + AI Governance review.                                         |
| E3 — Significant | Potential serious effects on people, safety, privacy, workforce, customer reliance or accountability; enhanced evidence is needed.   | Enhanced review; restricted/conditional deployment where gaps remain. |
| E4 — Severe      | Current design or governance can materially impair rights/opportunity, cause serious harm, or lacks accountable/knowable boundaries. | Do not deploy / contain until blocking issues are treated.            |

### 4.1 Ethical dimensions

| **Dimension**                                     | **Assessment question**                                                                                                                     |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| D1 Human agency, autonomy & dignity               | Does AI empower or constrain people? Is human authority meaningful? Is manipulation or dehumanizing treatment avoided?                      |
| D2 Fairness, non-discrimination & inclusion       | Are criteria job/task relevant? Are groups treated fairly? Is accessibility designed in? Are vulnerable groups disproportionately burdened? |
| D3 Privacy, data dignity & information rights     | Is data use proportionate, expected, secure and limited? Are sensitive inferences or surveillance avoided?                                  |
| D4 Transparency, explainability & contestability  | Can users/affected people understand AI involvement, capabilities, limitations, basis of material outcomes and routes to challenge?         |
| D5 Robustness, safety & non-maleficence           | Can errors, adversarial abuse or unsafe reliance cause harm? Are fallbacks, validation and stop-use mechanisms effective?                   |
| D6 Accountability, auditability & remedy          | Is ownership clear? Can decisions and controls be evidenced? Can adverse outcomes be corrected or remedied?                                 |
| D7 Societal, workforce & environmental well-being | Does AI improve well-being without unacceptable deskilling, workload, exclusion, waste, environmental cost or harmful power concentration?  |

## 5. Stakeholder and Power-Asymmetry Analysis

| **Stakeholder**                            | **Relevant systems**                        | **Sensitivity**            | **Power / dependency observation**                                                                                               |
|--------------------------------------------|---------------------------------------------|----------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Job applicants / internal candidates       | DuckTalent                                  | High                       | Depend on Duckworks for access to employment; limited visibility into ranking and limited bargaining power.                      |
| Customers / product users                  | QuackBot; DuckDesign/WingInspect indirectly | Medium-High                | May rely on technical guidance or product quality without seeing underlying AI limitations.                                      |
| Employees                                  | PondGPT; shadow AI; workforce AI            | Medium                     | Can benefit from productivity but may face surveillance, deskilling, performance pressure or unclear acceptable-use boundaries.  |
| Recruiters / hiring managers               | DuckTalent                                  | High reliance risk         | May defer to rankings/summaries and unintentionally convert advisory AI into de facto decision-making.                           |
| Mechanical engineers                       | DuckDesign                                  | High professional reliance | Remain accountable for safety-relevant engineering decisions despite persuasive AI output.                                       |
| Quality inspectors                         | WingInspect                                 | High professional reliance | May experience automation bias, alert fatigue or deskilling while retaining formal final authority.                              |
| Suppliers / logistics partners             | FeatherForecast                             | Medium                     | Forecast-driven ordering may create volatility or unfair commercial pressure without visibility into model limitations.          |
| Data subjects in internal/customer records | PondGPT, QuackBot, DuckTalent, shadow AI    | High                       | May be affected by retrieval, summarization or disclosure without direct interaction with the AI.                                |
| Duckworks organization / shareholders      | All                                         | High influence             | Receive efficiency/value benefits and control deployment decisions; must not externalize ethical costs onto weaker stakeholders. |

### 5.1 Stakeholder engagement expectations

- DuckTalent: representative applicant/user input is required before any real pilot; accessibility and contestability must be tested, not merely documented.

- QuackBot: customer feedback, complaint patterns and escalation outcomes should inform release and monitoring.

- WingInspect and DuckDesign: inspectors/engineers must participate in validation so that oversight is operationally meaningful.

- PondGPT: employee feedback should include privacy/surveillance concerns, usefulness, accessibility, over-reliance and workload effects.

- FeatherForecast: supply-chain planners and manufacturing teams should review forecast dependency and override burdens; supplier impacts should be considered where material.

- AI-007: employee input should inform approved-tool design so controls do not simply drive shadow AI into less visible channels.

## 6. Portfolio Ethical Dimension Matrix

| **System**             | **D1 Agency** | **D2 Fairness** | **D3 Privacy** | **D4 Transparency** | **D5 Safety** | **D6 Accountability** | **D7 Well-being** |
|------------------------|---------------|-----------------|----------------|---------------------|---------------|-----------------------|-------------------|
| AI-001 DuckDesign      | E3            | E1              | E2             | E2                  | E3            | E3                    | E2                |
| AI-002 QuackBot        | E3            | E2              | E3             | E3                  | E3            | E3                    | E2                |
| AI-003 FeatherForecast | E2            | E1              | E2             | E2                  | E2            | E2                    | E2                |
| AI-004 WingInspect     | E3            | E2              | E2             | E2                  | E3            | E3                    | E2                |
| AI-005 DuckTalent      | E4            | E4              | E4             | E4                  | E3            | E4                    | E3                |
| AI-006 PondGPT         | E3            | E2              | E3             | E2                  | E3            | E3                    | E3                |
| AI-007 Shadow GenAI    | E4            | E3              | E4             | E4                  | E3            | E4                    | E3                |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Interpretation</strong></p>
<p>The matrix shows ethical attention by dimension, not mathematical scoring. E4 in one dimension is not averaged down by lower concern elsewhere. For example, DuckTalent's employment-opportunity and fairness implications remain severe even if the system later demonstrates strong cybersecurity controls.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 7. AI-001 — DuckDesign AI

| **Field**                   | **Assessment**                                                                                                                                     |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Business owner              | Felix Duckson — VP Product & Engineering                                                                                                           |
| Ethical priority            | E3 — Significant                                                                                                                                   |
| Current governance decision | Restricted pilot only                                                                                                                              |
| Assessment boundary         | Current stated intended purpose and described controls only; material purpose, model, data, user, autonomy or vendor changes require reassessment. |

### 7.1 Positive ethical value

- Can reduce repetitive engineering work and expand the range of design alternatives considered by skilled engineers.

- May improve material efficiency, weight optimization and engineering iteration if benefits are validated rather than assumed.

- Can support knowledge reuse when outputs remain traceable to approved engineering sources.

### 7.2 Material ethical concerns

- Persuasive but incorrect recommendations can shift engineer judgment and indirectly affect product quality or physical safety.

- Formal human accountability can become nominal if schedule pressure or interface design causes routine deference to AI output.

- Use of proprietary CAD/specifications creates ethical duties around confidentiality, provenance and fair treatment of intellectual property.

- Opaque optimization objectives may privilege cost/speed over safety, maintainability or user well-being if trade-offs are not explicit.

### 7.3 Ethical tensions / trade-offs

- Innovation speed versus professional engineering independence and safety conservatism.

- Broader design exploration versus traceability and reproducibility of how a recommendation was produced.

- Potential material/resource savings versus computational and rework costs from poor suggestions.

### 7.4 Required safeguards and evidence

☐ Engineer remains accountable design authority and can reject/override AI output without adverse performance pressure.

☐ No direct release of AI-generated design to manufacturing; validated engineering checks remain mandatory.

☐ Model/output provenance and source/reference evidence are retained for material design decisions.

☐ Unsafe-recommendation, validation-failure and override patterns are monitored.

☐ Confidential IP is restricted to approved providers/tenants and contractual data-use terms.

☐ Product Safety & Quality review is mandatory before safety-critical expansion.

### 7.5 Ethical monitoring indicators

| **Indicator**                                   | **Why it matters**                                                                                                          |
|-------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Engineer override rate                          | Extremely low override can indicate automation bias or interface pressure; very high override can indicate poor usefulness. |
| Validation failure / unsafe recommendation rate | Shows whether AI suggestions create downstream rework or safety concern.                                                    |
| Source/provenance coverage                      | Supports traceability and informed professional judgment.                                                                   |
| Design-related incident / near miss             | Requires stop-use and reassessment where AI contribution is plausible.                                                      |

### 7.6 Reassessment triggers

- Removal/reduction of engineer review.

- Use on safety-critical products or functions.

- New model/provider or material optimization-objective change.

- New confidential data sources or external integrations.

- Material validation failure, product incident or near miss.

## 8. AI-002 — QuackBot

| **Field**                   | **Assessment**                                                                                                                                     |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Business owner              | Clara Duckley — Director Customer Operations                                                                                                       |
| Ethical priority            | E3 — Significant                                                                                                                                   |
| Current governance decision | Production blocked pending gates                                                                                                                   |
| Assessment boundary         | Current stated intended purpose and described controls only; material purpose, model, data, user, autonomy or vendor changes require reassessment. |

### 8.1 Positive ethical value

- Can improve availability and response time for routine customer support.

- May improve accessibility when users can interact in natural language and are offered alternative human channels.

- Can standardize retrieval of approved product and warranty information when grounding is effective.

### 8.2 Material ethical concerns

- Customers may reasonably treat confident technical or warranty statements as authoritative even when the model is uncertain.

- Safety-adjacent troubleshooting can expose users to harm if the system hallucinates, omits context or fails to escalate.

- Privacy and confidentiality can be compromised through customer input, retrieval errors or prompt-injection attacks.

- Users may not understand the limits of AI-generated advice, creating an information asymmetry.

- Accessibility can improve for some users while deteriorating for others if language, disability or digital-access needs are not tested.

### 8.3 Ethical tensions / trade-offs

- 24/7 automated service versus preserving meaningful access to human support.

- Fast resolution versus conservative escalation for uncertain or high-impact cases.

- Personalized support versus data minimization and privacy.

### 8.4 Required safeguards and evidence

☐ Clear AI disclosure and capability/limitation communication appropriate to the interaction.

☐ Human escalation for safety, legal, warranty-exception and other consequential cases.

☐ Grounding to approved knowledge; unsupported-answer detection and pre-release evaluation.

☐ Prompt/RAG injection testing, least-privilege retrieval and sensitive-data controls.

☐ Accessible human alternative and complaint/challenge route.

☐ No irreversible account/refund/product action without approved workflow and authorization.

### 8.5 Ethical monitoring indicators

| **Indicator**                            | **Why it matters**                                                        |
|------------------------------------------|---------------------------------------------------------------------------|
| Unsupported-answer / hallucination rate  | Direct indicator of misleading customer guidance.                         |
| Correct escalation rate                  | Tests whether human oversight is available when ethically necessary.      |
| Customer complaint / challenge rate      | Surfaces confusion, harm and contested advice.                            |
| Sensitive-data exposure events           | Any confirmed event can require containment.                              |
| Human-channel availability / abandonment | Checks that automation does not make human help practically inaccessible. |

### 8.6 Reassessment triggers

- New safety-critical troubleshooting capability.

- Autonomous customer account/refund/product actions.

- New personal-data categories or high-sensitivity support context.

- Material model/RAG/provider change.

- Pattern of harmful output, complaints or security events.

## 9. AI-003 — FeatherForecast

| **Field**                   | **Assessment**                                                                                                                                     |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Business owner              | Tobias Duckman — Director Supply Chain                                                                                                             |
| Ethical priority            | E2 — Material                                                                                                                                      |
| Current governance decision | Continue with monitoring                                                                                                                           |
| Assessment boundary         | Current stated intended purpose and described controls only; material purpose, model, data, user, autonomy or vendor changes require reassessment. |

### 9.1 Positive ethical value

- Can reduce stockouts, excess inventory and operational waste when forecasts are accurate and appropriately used.

- May support more stable manufacturing planning and earlier identification of supply risks.

- Potentially reduces obsolete inventory and associated material waste.

### 9.2 Material ethical concerns

- Forecast opacity and automation bias can cause planners to defer to the system when local knowledge indicates otherwise.

- Bad forecasts can indirectly affect workforce schedules, overtime, supplier demand and customer availability.

- Supplier relationships can be strained if model-driven volatility is treated as objective rather than uncertain planning advice.

- Environmental benefits should not be claimed without measurement of actual waste/resource effects.

### 9.3 Ethical tensions / trade-offs

- Efficiency and inventory reduction versus resilience buffers and supplier stability.

- Consistent forecasting versus preserving professional judgment and local operational knowledge.

### 9.4 Required safeguards and evidence

☐ Authorized manager remains accountable for purchasing and production commitments.

☐ Forecast uncertainty/ranges and key drivers are understandable to planners where practical.

☐ Back-testing, drift monitoring and override documentation remain in place.

☐ Supplier/customer confidential data use remains purpose-limited.

☐ Workforce/supplier impacts are reviewed if automated planning scope expands.

### 9.5 Ethical monitoring indicators

| **Indicator**                                       | **Why it matters**                                               |
|-----------------------------------------------------|------------------------------------------------------------------|
| Forecast bias and error by product/supplier segment | Persistent directional error can systematically shift burdens.   |
| Planner override rate and rationale                 | Checks over-reliance and whether local expertise remains usable. |
| Stockout / excess inventory / obsolescence          | Measures promised operational and waste benefits.                |
| Supplier volatility / expedites                     | Can reveal downstream commercial burdens from poor forecasts.    |

### 9.6 Reassessment triggers

- Automatic purchasing or production commitments.

- Use for employment/performance decisions.

- New external/sensitive datasets.

- Major model or forecasting-objective change.

- Material persistent drift or unexplained segment bias.

## 10. AI-004 — WingInspect Vision

| **Field**                   | **Assessment**                                                                                                                                     |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Business owner              | Henrietta Duckwell — Director Manufacturing                                                                                                        |
| Ethical priority            | E3 — Significant                                                                                                                                   |
| Current governance decision | Restricted pilot; no safety-critical release                                                                                                       |
| Assessment boundary         | Current stated intended purpose and described controls only; material purpose, model, data, user, autonomy or vendor changes require reassessment. |

### 10.1 Positive ethical value

- Can improve consistency and focus human inspection on likely defect areas.

- May reduce defect escapes and provide earlier process-quality feedback.

- Potentially reduces rework if false-positive rates remain controlled.

### 10.2 Material ethical concerns

- False negatives can allow defects to progress and can create physical/product harm if human inspection becomes complacent.

- False positives can increase scrap and rework, creating environmental and workforce burdens.

- Inspectors can experience automation bias, alert fatigue or deskilling if the system becomes the de facto authority.

- Production imagery could be repurposed for worker monitoring, creating a new privacy/workplace power issue.

### 10.3 Ethical tensions / trade-offs

- Consistency through automation versus maintaining human vigilance and expertise.

- Higher detection sensitivity versus waste and alert burden from false positives.

- Quality analytics versus inappropriate surveillance of workers.

### 10.4 Required safeguards and evidence

☐ Qualified human inspector retains final pass/fail authority.

☐ No deployment to safety-critical lines without a separate safety case and reassessment.

☐ Performance is validated by defect class, product line and operating conditions.

☐ Worker imagery is not repurposed for performance/disciplinary monitoring without a new approved assessment.

☐ Inspectors receive training on limitations, override and escalation.

☐ Defect escape, false-positive/negative and override patterns are monitored.

### 10.5 Ethical monitoring indicators

| **Indicator**                            | **Why it matters**                               |
|------------------------------------------|--------------------------------------------------|
| False-negative / defect escape rate      | Primary product-safety ethical indicator.        |
| False-positive / scrap rate              | Captures unnecessary waste and burden.           |
| Inspector override and disagreement rate | Shows whether human authority remains active.    |
| Alert fatigue / workload signal          | Detects human-factors degradation.               |
| Use-of-imagery exceptions                | Identifies scope creep toward worker monitoring. |

### 10.6 Reassessment triggers

- Removal of mandatory human inspection.

- Use on new product line/camera without validation.

- Expansion to safety-critical components.

- Reuse of imagery for workforce monitoring.

- Significant model degradation or quality incident.

## 11. AI-005 — DuckTalent AI

| **Field**                   | **Assessment**                                                                                                                                     |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Business owner              | Beatrice Van Duck — Chief People Officer                                                                                                           |
| Ethical priority            | E4 — Severe                                                                                                                                        |
| Current governance decision | Do not deploy                                                                                                                                      |
| Assessment boundary         | Current stated intended purpose and described controls only; material purpose, model, data, user, autonomy or vendor changes require reassessment. |

### 11.1 Positive ethical value

- Could reduce administrative CV triage and make review criteria more structured if job relevance and fairness are demonstrably controlled.

- Could free recruiter time for substantive human review and candidate interaction.

- May improve consistency only if the criteria, data and operating process are demonstrably fair and accessible.

### 11.2 Material ethical concerns

- Ranking directly affects access to employment and operates in a strong power asymmetry between Duckworks and applicants.

- Historical or proxy features can reproduce or amplify discrimination at scale.

- Inaccurate parsing or ranking can deprive candidates of opportunity before a meaningful human assessment occurs.

- Opaque rankings can undermine dignity and procedural fairness when candidates cannot understand or challenge materially adverse treatment.

- Recruiters may defer to ranks/summaries, making nominal human review ineffective.

- Applicant data can expose or enable inference of sensitive/protected characteristics and unrelated personal information.

- Accessibility failures may disadvantage candidates with non-standard CVs, disabilities, language differences or career histories.

### 11.3 Ethical tensions / trade-offs

- Efficiency and standardization versus individualized, contextual and humane assessment.

- Consistency versus entrenching a flawed criterion consistently across every applicant.

- Data-rich prediction versus privacy, dignity and strict job relevance.

- Recruiter support versus the risk that ranking becomes a de facto automated gate.

### 11.4 Required safeguards and evidence

☐ No automated rejection or hiring; consequential decisions require documented, reasoned human review.

☐ Job-relevant criteria and prohibited/proxy features are defined and independently challenged before vendor/model selection.

☐ Fairness/proxy testing methodology and evidence are completed using lawful data and representative populations.

☐ Parsing/ranking accuracy and error distribution are validated, including accessibility/non-standard applicant cases.

☐ Candidate notice, accessible challenge/reconsideration route and meaningful remedy are implemented.

☐ Privacy/DPIA, vendor/DPA, retention, security and data-minimization evidence are complete.

☐ Recruiter training addresses automation bias, explanation limits and responsibility.

☐ Monitoring includes subgroup outcomes, overrides, challenges, ranking errors and adverse incidents.

### 11.5 Ethical monitoring indicators

| **Indicator**                                  | **Why it matters**                                                                                                   |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Selection-rate / outcome differences           | Can reveal disparate effects requiring investigation; interpretation needs lawful context and statistical expertise. |
| Parsing/ranking error by applicant type        | Detects systematic disadvantage from format, language or non-standard career histories.                              |
| Recruiter override rate and rationale          | Tests whether human review is meaningful rather than ceremonial.                                                     |
| Candidate challenge / reconsideration outcomes | Measures contestability and whether remedy changes decisions.                                                        |
| Accessibility failure / accommodation signal   | Identifies exclusion caused by process design.                                                                       |
| Use of prohibited/proxy features               | Any confirmed use is a blocking governance issue.                                                                    |

### 11.6 Reassessment triggers

- Any real-applicant pilot or procurement commitment.

- Change to ranking criteria, features, model/provider or intended employment use.

- Expansion to internal mobility, performance management or termination decisions.

- Material fairness, accessibility or privacy concern.

- Removal/weakening of human review or challenge route.

## 12. AI-006 — PondGPT

| **Field**                   | **Assessment**                                                                                                                                     |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Business owner              | Oliver Duckett — Head of IT & Cloud                                                                                                                |
| Ethical priority            | E3 — Significant                                                                                                                                   |
| Current governance decision | Restricted pilot; sensitive repositories excluded                                                                                                  |
| Assessment boundary         | Current stated intended purpose and described controls only; material purpose, model, data, user, autonomy or vendor changes require reassessment. |

### 12.1 Positive ethical value

- Can reduce repetitive drafting, search and summarization work and improve access to institutional knowledge.

- May support accessibility and language assistance for employees.

- Can assist developers and operational staff when outputs remain advisory and reviewed.

### 12.2 Material ethical concerns

- Broad enterprise access can create privacy/confidentiality harm if retrieval permissions fail or sensitive sources are connected.

- Employees may feel monitored if prompts, conversations or usage analytics are repurposed for performance scoring.

- Inaccurate answers or generated code can cause downstream harm when staff over-rely on fluent output.

- Persistent reliance can deskill employees or shift accountability away from competent professionals.

- Access to AI may benefit some functions more than others, creating uneven workload or capability effects.

- Agentic/tool capabilities could materially change employee autonomy and organizational power if added without reassessment.

### 12.3 Ethical tensions / trade-offs

- Productivity measurement versus privacy and freedom from covert performance surveillance.

- Centralized enterprise knowledge access versus contextual integrity and least privilege.

- Convenient generated answers versus maintaining professional competence and verification habits.

### 12.4 Required safeguards and evidence

☐ Permission-aware retrieval inherits source-system authorization and is regression-tested.

☐ Sensitive HR/legal/security repositories remain excluded until specifically assessed and approved.

☐ Purpose limitation prohibits covert employee performance scoring from prompt/usage data.

☐ Generated code and consequential professional advice require human review and relevant security/quality checks.

☐ Prompt injection, poisoned retrieval and excessive-permission scenarios are tested.

☐ Employees receive clear usage, privacy, logging and limitation information.

☐ Any agentic/action capability is treated as a material change requiring new assessment.

### 12.5 Ethical monitoring indicators

| **Indicator**                               | **Why it matters**                                                  |
|---------------------------------------------|---------------------------------------------------------------------|
| Unauthorized retrieval test failure         | Direct ethical and security indicator of cross-user data exposure.  |
| DLP / restricted-data event                 | Shows whether confidentiality boundaries are working.               |
| User complaint / reliance signal            | Captures harmful output, surveillance concern and usability issues. |
| Generated-code security defect trend        | Measures downstream harm potential.                                 |
| Sensitive-repository connector count        | Tracks expansion of ethical exposure.                               |
| Usage analytics access / purpose exceptions | Detects surveillance or purpose creep.                              |

### 12.6 Reassessment triggers

- Addition of HR/legal/security or other sensitive repositories.

- Addition of agentic tools or external actions.

- Use of usage data for performance evaluation.

- New model/provider/connector with different data-use terms.

- Material data leakage, harmful output or systemic reliance issue.

## 13. AI-007 — Unregistered GenAI Usage

| **Field**                   | **Assessment**                                                                                                                                     |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Business owner              | Reginald Duckman — CRCO / business owners by discovered use                                                                                        |
| Ethical priority            | E4 — Severe                                                                                                                                        |
| Current governance decision | Immediate containment and decomposition                                                                                                            |
| Assessment boundary         | Current stated intended purpose and described controls only; material purpose, model, data, user, autonomy or vendor changes require reassessment. |

### 13.1 Positive ethical value

- Employee experimentation can reveal useful use cases and productivity opportunities.

- Low-friction experimentation may surface business needs that formal procurement has not yet addressed.

### 13.2 Material ethical concerns

- No stable intended purpose, owner, model/provider, data boundary, human-oversight design or evidence base exists for the aggregate condition.

- Confidential, personal or proprietary information may be submitted to services with unknown retention, training or transfer terms.

- Unregistered use can silently enter recruitment, customer, safety or other consequential processes without affected people knowing.

- Lack of logging and vendor visibility undermines accountability, remedy and incident response.

- Aggressive blocking without approved alternatives can drive use into less visible channels and weaken organizational trust.

### 13.3 Ethical tensions / trade-offs

- Rapid innovation versus the ethical requirement for accountable, knowable boundaries.

- Employee autonomy and experimentation versus confidentiality, data subject interests and organizational responsibility.

- Strict prohibition versus a proportionate approved-tool environment that people can realistically follow.

### 13.4 Required safeguards and evidence

☐ Contain restricted/sensitive uploads and identify material use cases.

☐ Provide approved enterprise alternatives for common low-risk tasks.

☐ Convert each material discovered use into its own inventory, owner, intended purpose and assessment.

☐ Publish clear acceptable-use boundaries and a low-friction exception/intake path.

☐ Use proportionate discovery/DLP controls with transparency and workforce/privacy review.

☐ Investigate known exposures and preserve evidence without treating all experimentation as misconduct.

☐ Stop any unregistered use in employment, safety, customer decisioning or other consequential context.

### 13.5 Ethical monitoring indicators

| **Indicator**                               | **Why it matters**                                                             |
|---------------------------------------------|--------------------------------------------------------------------------------|
| Unapproved-tool detections                  | Shows prevalence but must not be used alone as a workforce-performance metric. |
| Restricted-data DLP events                  | Any confirmed event may indicate real privacy/confidentiality harm.            |
| Material uses converted to governed pilots  | Measures whether governance enables legitimate innovation.                     |
| Repeat policy breaches / workaround signals | Can indicate poor behavior or poor control/process design.                     |
| Approved-tool adoption                      | Low adoption with persistent shadow use suggests usability/governance failure. |

### 13.6 Reassessment triggers

- Every newly discovered material use case.

- Confirmed restricted-data disclosure.

- New browser extension/agent with enterprise access.

- Evidence of consequential HR/customer/safety use.

- Control changes that cause users to migrate to harder-to-detect channels.

## 14. Cross-Cutting Ethical Issues

| **Issue**                      | **Systems**                                                             | **Ethical concern**                                                                                                         | **Duckworks response**                                                                         |
|--------------------------------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Automation bias                | DuckTalent, DuckDesign, WingInspect, FeatherForecast, QuackBot, PondGPT | Human review can be formally present but practically ineffective if UI/process incentives privilege AI output.              | Track overrides, disagreements, reviewer rationale, time pressure and ability to stop.         |
| Power asymmetry                | DuckTalent, workplace AI, customer AI                                   | Affected people may have little bargaining power or knowledge of how AI influences outcomes.                                | Notice, accessible alternatives, challenge, remedy and representative stakeholder input.       |
| Purpose creep                  | PondGPT, WingInspect imagery, shadow AI, DuckTalent data                | Data/AI built for one purpose can be quietly repurposed into monitoring or consequential decisions.                         | Purpose lock, change management, access logging, specialist review.                            |
| Opacity and provenance         | Generative AI and ranking systems                                       | Fluent output or scores can appear objective without adequate basis.                                                        | Source provenance, limitation statements, explanation appropriate to stakeholder.              |
| Accountability diffusion       | Third-party AI and shadow AI                                            | Vendor complexity can make responsibility appear external or unowned.                                                       | Named Duckworks owner, contractual evidence, change notice, incident/exit rights.              |
| Digital exclusion              | QuackBot, DuckTalent, PondGPT                                           | AI-first processes can disadvantage users who need human assistance, accessibility accommodations or non-standard channels. | Accessible human alternative and accommodation testing.                                        |
| Environmental/resource effects | All; especially compute-intensive GenAI                                 | Portfolio evidence lacks provider-specific energy/emissions/resource data.                                                  | Treat as an evidence gap; avoid unsupported sustainability claims; obtain data where material. |

## 15. Duckworks Ethical Red Lines

The following are internal ethical governance prohibitions/stop conditions. Some may also overlap with legal prohibitions or mandatory requirements, but this section does not claim that every item is independently required by law.

- No autonomous hiring or rejection through DuckTalent in the stated design.

- No deliberate discrimination or intentional use of protected/sensitive attributes for unrelated decision criteria.

- No removal of required human authority for product design release, manufacturing quality acceptance or other safety-relevant decisions without a new governance and legal/safety assessment.

- No covert employee performance scoring based on PondGPT prompts, conversations or usage analytics.

- No use of WingInspect production imagery for worker disciplinary monitoring without a new approved purpose and assessment.

- No knowingly unapproved public AI use with restricted/confidential/personal data.

- No suppression or falsification of AI incidents, validation failures, fairness results, audit evidence or material model limitations.

- No customer-facing AI design that makes a human channel practically unavailable for consequential or contested matters.

- No release where a Severe (E4) ethical concern remains untreated and the current system state lacks adequate remedy or governance evidence.

## 16. Ethical Treatment and Action Plan

| **ID** | **Scope**       | **Required action**                                                                                                                      | **Owner**                              | **Priority**                   |
|--------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|--------------------------------|
| ETH-01 | DuckTalent      | Maintain Do Not Deploy; complete fairness/job-relevance, accessibility, DPIA/legal, human oversight, contestability and vendor evidence. | CPO + AI Governance + Legal/DPO        | Blocking                       |
| ETH-02 | QuackBot        | Complete customer transparency, safe escalation, grounded-answer, prompt/RAG security, complaint/remedy and accessibility controls.      | Customer Ops + Data & AI + CISO        | Blocking for production        |
| ETH-03 | DuckDesign      | Formalize engineering validation and provenance; test unsafe recommendation and automation-bias indicators.                              | Product & Engineering + Product Safety | Before production expansion    |
| ETH-04 | WingInspect     | Validate defect performance by class/line; preserve human final authority; prohibit worker-monitoring repurposing.                       | Manufacturing + Product Safety         | Before expanded pilot          |
| ETH-05 | PondGPT         | Verify permission-aware retrieval, DLP, restricted-source exclusions, anti-surveillance purpose limits and adversarial testing.          | IT + CISO + DPO/CPO                    | Before corpus/action expansion |
| ETH-06 | FeatherForecast | Maintain human planning authority; review supplier/workforce effects and evidence claimed waste benefits.                                | Supply Chain                           | Ongoing                        |
| ETH-07 | AI-007          | Contain, discover, provide approved alternatives and decompose material uses into separate governed records.                             | CISO + AI Governance + IT              | Immediate                      |
| ETH-08 | Portfolio       | Add stakeholder-engagement evidence and ethical monitoring fields to QuackTrack/control records.                                         | AI Governance Lead                     | Program action                 |
| ETH-09 | Portfolio       | Request material third-party AI environmental/resource evidence and label unknowns.                                                      | Procurement + AI Governance            | Program action                 |

## 17. Ethical Approval Decision Rules

| **Ethical priority** | **Decision rule**                                                                                            | **Governance**                                                       |
|----------------------|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| E1 — Limited         | Routine owner acceptance if other governance gates are satisfied.                                            | Standard monitoring.                                                 |
| E2 — Material        | Owner + AI Governance review; document trade-offs and safeguards.                                            | Periodic review and stakeholder signals.                             |
| E3 — Significant     | Enhanced specialist review; production only where blocking gaps are closed and evidence supports safeguards. | AI Governance Committee where linked risk/gate requires it.          |
| E4 — Severe          | Do not deploy / contain current state. Redesign, treatment and re-assessment required.                       | Executive/committee visibility; legal/specialist review as relevant. |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Non-offset rule</strong></p>
<p>A claimed benefit does not cancel an adverse ethical impact. Faster hiring does not offset discrimination; lower inspection time does not offset safety failure; productivity does not offset covert surveillance. Benefits and harms are evidenced separately, and severe harm must be treated on its own merits.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 18. Portfolio Ethical Monitoring

| **Dimension**                 | **Portfolio indicators**                                                                          | **Owner**                                   |
|-------------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------|
| Agency / oversight            | Override/disagreement rate; human escalation; stop-use events; reviewer burden                    | System owner + AI Governance                |
| Fairness / inclusion          | Outcome differences, accessibility failures, complaints/challenges, excluded user groups          | HR / Business Owner + Legal/DPO as relevant |
| Privacy / dignity             | Sensitive-data events, unauthorized retrieval, purpose exceptions, surveillance complaints        | DPO + CISO                                  |
| Transparency / contestability | AI disclosure effectiveness, explanation requests, challenge outcomes, human-channel availability | Business Owner                              |
| Safety / robustness           | Harmful outputs, defect escapes, unsafe recommendations, incidents/near misses                    | CISO / Product Safety / Business Owner      |
| Accountability                | Unowned AI, overdue assessments, evidence gaps, vendor-change notices, unresolved actions         | AI Governance + Procurement                 |
| Well-being / workforce        | Workload, deskilling, user trust, shadow-AI workarounds, benefit distribution                     | CPO + Business Owners                       |
| Environmental                 | Provider energy/resource disclosures where material; waste/rework/obsolescence indicators         | Procurement + Operations                    |

### 18.1 Reassessment triggers

- Change in intended purpose, autonomy or formal decision authority.

- New model/provider/version or material configuration change.

- New data categories, sensitive sources, features, RAG repositories, connectors or permissions.

- Expansion to new users, affected groups, countries, languages or product lines.

- Material incident, near miss, complaint, whistleblowing report, rights challenge or evidence of discriminatory outcome.

- Drift, error-distribution change, performance threshold breach or control failure.

- Change in legal/regulatory context or internal risk appetite.

- Evidence that a mitigation creates a new burden, exclusion, workaround or ethical harm.

## 19. Minimum Ethical Evidence Pack

| **Evidence ID** | **Minimum record**                                                                        |
|-----------------|-------------------------------------------------------------------------------------------|
| ETH-EV-01       | Validated intended purpose and decision/support boundary                                  |
| ETH-EV-02       | Affected-stakeholder map and power/dependency analysis                                    |
| ETH-EV-03       | System-specific AIA and linked risk assessment                                            |
| ETH-EV-04       | Human oversight procedure, training and override evidence                                 |
| ETH-EV-05       | Fairness/accessibility evidence where people/opportunity may be affected                  |
| ETH-EV-06       | Privacy/data-use and security review evidence where data is material                      |
| ETH-EV-07       | Transparency, explanation, notice, complaint/challenge/remedy artifacts                   |
| ETH-EV-08       | Technical validation / safety / robustness test evidence as applicable                    |
| ETH-EV-09       | Vendor model/data-use/retention/change and assurance evidence                             |
| ETH-EV-10       | Stakeholder-engagement evidence or documented reason why simulated/no engagement was used |
| ETH-EV-11       | Monitoring thresholds and post-deployment ethical indicators                              |
| ETH-EV-12       | Governance decision, conditions, exceptions and treatment closure                         |

## 20. Material Assumptions and Evidence Gaps

| **Gap**    | **Evidence limitation**                                                                                                              | **Materiality**         |
|------------|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| GAP-ETH-01 | Several human-authority arrangements remain project assumptions and must be validated in operating procedures.                       | Critical                |
| GAP-ETH-02 | DuckTalent vendor/model, production data, fairness and accessibility evidence are not verified.                                      | Critical                |
| GAP-ETH-03 | PondGPT permission architecture and future connector/agent scope require evidence.                                                   | High                    |
| GAP-ETH-04 | Provider-specific environmental/energy/resource data is not available for material third-party GenAI services.                       | Medium                  |
| GAP-ETH-05 | No real stakeholder engagement or real affected-person evidence is claimed in this portfolio.                                        | High                    |
| GAP-ETH-06 | No real protected-class or applicant data is used; fairness conclusions are governance hypotheses, not validated production results. | Critical for DuckTalent |
| GAP-ETH-07 | AI-007 contains multiple unknown uses and cannot receive one stable ethical conclusion beyond containment/decomposition.             | Critical                |
| GAP-ETH-08 | Exact jurisdictions and national employment/equality/privacy implementation details require separate Legal review.                   | High                    |

## 21. Source and Framework Map

| **Source**                                                                     | **Use**                                                                                                               | **Classification**                     |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| European Commission — Ethics Guidelines for Trustworthy AI / ALTAI             | Seven ethical/trustworthy-AI requirements used as the primary ethical structure.                                      | Voluntary guidance                     |
| OECD AI Principles (updated 2024)                                              | Human-centred values/fairness; transparency; robustness/security/safety; accountability; inclusive growth/well-being. | Voluntary intergovernmental principles |
| NIST AI RMF 1.0                                                                | Trustworthy AI characteristics and Govern-Map-Measure-Manage thinking.                                                | Voluntary framework                    |
| ISO/IEC 42005:2025 public description                                          | Lifecycle impact assessment focused on individuals, groups and society.                                               | Voluntary standard guidance            |
| EU AI Act — current consolidated text                                          | Separate legal screening for applicable mandatory duties; not used as an ethics score.                                | Binding law where applicable           |
| Duckworks AI Impact Assessment Pack                                            | System-specific positive/adverse impacts, stakeholders, safeguards and current decisions.                             | Project evidence                       |
| Duckworks AI Risk Methodology / Risk Report                                    | Risk scenarios, evidence confidence, control effectiveness, risk appetite and approval rules.                         | Internal governance methodology        |
| Duckworks Stakeholder Register / RACI / Responsible Use Policy                 | Ownership, affected stakeholders, specialist review, human oversight, evidence and escalation.                        | Internal governance                    |
| Duckworks FRIA / DPIA / HUDERIA / Algorithmic Impact Assessment for DuckTalent | Specialist rights/privacy/human-rights/algorithmic evidence reused without duplication.                               | Companion assessments                  |

### 21.1 Official public references

| **Reference**                                            | **Official URL**                                                                                                           |
|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| European Commission Ethics Guidelines for Trustworthy AI | https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai                                          |
| European Commission ALTAI                                | https://digital-strategy.ec.europa.eu/en/library/assessment-list-trustworthy-artificial-intelligence-altai-self-assessment |
| OECD AI Principles                                       | https://oecd.ai/en/ai-principles                                                                                           |
| NIST AI RMF                                              | https://www.nist.gov/itl/ai-risk-management-framework                                                                      |
| NIST trustworthy AI characteristics                      | https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/                                                         |
| ISO/IEC 42005:2025                                       | https://www.iso.org/standard/42005                                                                                         |
| EU AI Act consolidated working text                      | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R1689-20260727                                         |

## 22. Final Portfolio Position

Duckworks can pursue controlled AI adoption, but ethical governance must remain proportionate to the consequences of the use case rather than the novelty of the technology. The portfolio's central ethical control is not a generic 'human in the loop' statement; it is demonstrable human agency, contestability, evidence, and accountability at the points where AI can materially affect people, safety or organizational decisions.

The highest priority is DuckTalent: access to employment, discrimination risk, applicant dignity, accessibility and contestability make the current concept ethically unacceptable for real deployment until the blocking evidence and safeguards are complete. AI-007 presents a different but equally severe problem: ethical accountability cannot operate where the organization does not know what AI is being used, for what purpose, with what data or by which provider.

For the remaining systems, ethical acceptability depends on preserving current boundaries: competent engineer/inspector/manager authority, safe escalation to people, permission-aware data access, transparent AI use, proportional monitoring, and the ability to stop or reassess the system when context changes.

## Portfolio Disclaimer

Duckworks, Project W.I.N.G., all personnel, AI systems, datasets, stakeholders, incidents, findings, controls, scores and decisions in this assessment are fictional and created solely for educational and professional portfolio purposes. No real individual, employer, candidate, customer, supplier or production data is assessed.

This document is not legal advice, a regulatory conformity assessment, a GDPR DPIA, a mandatory EU AI Act fundamental-rights impact assessment, ISO certification evidence or independent assurance. Its ethical priorities are Duckworks internal governance judgments informed by public voluntary guidance and the stated fictional project evidence.
