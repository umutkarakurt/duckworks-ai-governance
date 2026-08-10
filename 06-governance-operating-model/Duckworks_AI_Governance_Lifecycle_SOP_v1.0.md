# Duckworks AI Governance Lifecycle Standard Operating Procedure (SOP)

**DUCKWORKS**

**AI Governance Lifecycle  
Standard Operating Procedure (SOP)**

Operational procedure for registering, assessing, approving, operating, reassessing, suspending, and retiring AI under Project W.I.N.G.

| **Control**                       | **Value**                                            |
|-----------------------------------|------------------------------------------------------|
| **Document ID**                   | DW-WING-SOP-01                                       |
| **Version**                       | 1.0                                                  |
| **Status**                        | Draft for Operational Approval                       |
| **Organization**                  | Duckworks                                            |
| **Program**                       | Project W.I.N.G.                                     |
| **Procedure Owner**               | Eleanor Duckford - AI Governance Lead                |
| **Governance Sponsor / Approver** | Reginald Duckman - Chief Risk & Compliance Officer   |
| **Effective Date**                | Upon approval                                        |
| **Review Cycle**                  | At least annually and after material trigger events  |
| **Classification**                | Internal Procedure / Fictional Portfolio / Synthetic |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Operating Rule</strong></p>
<p>No material AI moves to the next lifecycle stage unless the required owner, assessment, decision, controls, and evidence for the current gate are complete. Planned controls do not count as implemented controls.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

*Portfolio disclaimer. Duckworks, Project W.I.N.G., all personnel, AI systems, data, incidents, decisions, and controls referenced in this SOP are fictional and created solely for educational and professional portfolio purposes. This SOP is not legal advice, certification evidence, or a statement of regulatory conformity.*

## 1. Purpose

This Standard Operating Procedure operationalizes the Duckworks AI Governance Framework by defining the repeatable steps that must be followed when an AI use case is proposed, acquired, developed, piloted, deployed, materially changed, monitored, suspended, or retired.

The procedure is designed to preserve the Duckworks principle that every material AI use should be known, owned, assessed, controlled, monitored, and evidenced in proportion to its potential impact.

### 1.1 Procedure outcome

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Required traceability</strong></p>
<p>Business need -&gt; intended AI use -&gt; AI inventory -&gt; impact assessment -&gt; risk assessment -&gt; specialist reviews -&gt; controls and evidence -&gt; approval / lifecycle decision -&gt; monitoring -&gt; reassessment / retirement.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 1.2 What this SOP does not do

- It does not itself determine whether a particular law applies; Legal, Privacy, HR, Product Safety, or other qualified specialists make or support that determination as appropriate.

- It does not replace a formal GDPR Data Protection Impact Assessment, product conformity assessment, certification activity, penetration test, statistical fairness validation, or production engineering validation where those are separately required.

- It does not redesign Duckworks’ enterprise risk management, procurement, SDLC, information security, incident response, or internal-audit processes; it adds AI-specific governance checkpoints that integrate with them.

## 2. Scope

This SOP applies to Duckworks personnel and third parties acting on behalf of Duckworks when they propose, procure, build, configure, test, deploy, use, materially change, monitor, or retire AI-enabled capabilities.

- Internally developed AI and machine-learning systems.

- Third-party AI services, hosted models, APIs, and AI-enabled SaaS functionality.

- Generative AI, predictive machine learning, computer vision, coding assistants, browser extensions, embedded AI, and agentic or automated workflows.

- Production systems, restricted pilots, proofs of concept, controlled experiments, and material changes to existing AI.

- Discovered or unregistered “shadow AI” use involving Duckworks work, data, devices, credentials, code, processes, or customer-facing channels.

### 2.1 Material AI use

For this SOP, a use is treated as material when it can materially affect people, product or physical safety, confidential or personal data, significant financial or operational decisions, customer outcomes, legal obligations, product quality, or meaningful third-party/security dependency. This is a Duckworks internal governance definition, not a statutory classification.

## 3. Authority and Interpretation

| **Requirement type**         | **How this SOP treats it**                                                                                                                                                                                               |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Binding legal requirements   | Where applicable law creates an obligation, compliance is mandatory. Applicability and legal interpretation remain separate from this SOP and must be confirmed by the relevant legal/privacy specialist.                |
| Duckworks internal procedure | Once approved, “must”, “must not”, and “shall” statements in this SOP are mandatory Duckworks operating requirements. They are not automatically legal requirements.                                                     |
| Standards/framework guidance | NIST AI RMF, ISO/IEC 42001, ISO/IEC 23894, ISO/IEC 42005, ISO/IEC 27001, ENISA, MITRE ATLAS, and OWASP guidance may inform controls and evidence. Alignment does not itself establish legal compliance or certification. |
| Project assumptions          | Open assumptions about decision authority, model/provider, data, access, geography, safety role, and other implementation facts must be validated. A material assumption change may trigger reassessment.                |

## 4. Roles and Decision Rights

| **Role**                                    | **Primary procedural responsibility**                                                                                                                    |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| CEO / Executive Sponsor                     | Sets enterprise AI risk appetite and decides exceptional Critical residual-risk acceptance outside normal production tolerance.                          |
| Chief Risk & Compliance Officer (CRCO)      | Owns the governance framework and policy architecture, chairs the AI Governance Committee, and oversees risk escalation.                                 |
| AI Governance Lead                          | Operates this SOP, maintains QuackTrack inventory, coordinates assessments, records approvals, evidence, actions, and reassessments.                     |
| Business / AI System Owner                  | Owns intended purpose, business outcome, affected stakeholders, operating controls, treatment actions, monitoring, and use within the approved boundary. |
| Technical Owner / Data & AI                 | Owns technical architecture, model/service implementation, validation, technical controls, monitoring evidence, and material-change notification.        |
| CISO / Information Security                 | Owns AI security review, threat modelling, security acceptance criteria, and emergency security containment.                                             |
| General Counsel / DPO / HR / Product Safety | Provide specialist legal, privacy, employment/fairness, product-safety, and rights review where the domain is materially affected.                       |
| Procurement & Vendor Assurance              | Owns third-party AI due diligence, supplier change review, procurement controls, renewal checks, and exit obligations.                                   |
| AI Governance Committee                     | Cross-functional decision body for High residual risk, material exceptions, significant incidents, reassessments, and suspension decisions.              |
| Internal Audit                              | Provides independent assurance over design and operating effectiveness and does not own first- or second-line controls it may later audit.               |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>RACI rule</strong></p>
<p>Every procedure activity must have exactly one Accountable role. Business owners cannot self-approve High or Critical residual risk. Internal Audit remains independent from operational control ownership.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 5. Required Inputs, Systems, and Records

The procedure uses the Duckworks governance artifact chain below. A system may not require every artifact at the same depth; proportionality applies based on impact and risk.

| **Artifact / Record**      | **Minimum purpose**                                                                                                                                              |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Business Use Case          | Why the use exists, intended AI role, users, affected parties, human decision boundary, value hypothesis, and current governance boundary.                       |
| QuackTrack AI Inventory    | System identity, owners, lifecycle state, intended purpose, AI type, data, affected parties, provider/model, integrations, governance status, next review.       |
| AI Impact Assessment (AIA) | Positive/adverse impacts, affected persons, safeguards, human oversight, transparency, monitoring, current lifecycle decision.                                   |
| AI Risk Assessment         | Scenario-based inherent risk, implemented controls, evidence confidence, current residual risk, target residual risk, treatment, monitoring, approval authority. |
| Specialist review evidence | Security, privacy, legal, HR/fairness, product safety/quality, third-party due diligence, contractual review, as applicable.                                     |
| Release / approval record  | Decision, approver, conditions, exceptions, risk acceptance, action owners, due dates, evidence references.                                                      |
| Monitoring record          | KPIs/KRIs, drift/error trends, complaints, overrides, incidents, vendor/model changes, control failures, review dates.                                           |
| Change / closure record    | Material change evaluation, reassessment, suspension, retirement, access and integration closure, data disposition, retained evidence.                           |

## 6. Procedure Overview

| **Step** | **Stage**          | **Required outcome**                                                                                                     |
|----------|--------------------|--------------------------------------------------------------------------------------------------------------------------|
| 1        | Identify & submit  | Business owner identifies new or materially changed AI use and submits it before material operational reliance.          |
| 2        | Register           | AI Governance creates/updates the QuackTrack inventory entry and confirms minimum ownership/context.                     |
| 3        | Define purpose     | Business owner defines intended purpose, AI role, human decision boundary, affected parties, and expected value.         |
| 4        | Triage             | Legal/regulatory and materiality screening determines which specialist reviews and assessment depth are required.        |
| 5        | Assess             | Impact and risk assessments are completed; security/privacy/HR/safety/vendor reviews are performed where applicable.     |
| 6        | Treat & test       | Controls, human oversight, evidence, testing, monitoring, and target residual risk are defined and evidenced.            |
| 7        | Approve & release  | Decision authority follows residual-risk thresholds; release occurs only within approved conditions.                     |
| 8        | Operate & monitor  | Owners monitor performance, risks, controls, complaints, overrides, incidents, and vendor/model changes.                 |
| 9        | Reassess / contain | Material change, significant event, or control failure triggers reassessment, suspension, or containment as appropriate. |
| 10       | Retire             | The system is decommissioned, dependencies closed, inventory updated, and closure evidence retained.                     |

### 6.1 Gate principle

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Gate rule</strong></p>
<p>A lifecycle stage is a permission boundary, not merely a project status. A pilot approval does not authorize production use; approval for one intended purpose does not authorize a materially different purpose; and target residual risk is not the current residual risk.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 7. Detailed Operating Procedure

### 7.1 Step 1 - Identify and submit the AI use case

Accountable: Business / AI System Owner. Responsible: Business owner and relevant technical lead.

1.  Identify the business problem or opportunity and whether AI is necessary or materially useful.

2.  Submit the use case before procurement, material production reliance, external release, or expansion beyond an approved experiment.

3.  Declare whether the capability is internally built, third-party, embedded in SaaS, API-based, model-based, browser/endpoint tooling, or public GenAI.

4.  Identify known data categories, affected persons, expected users, integrations, provider/model, deployment geography, and level of automation.

5.  If the use already exists outside governance, route it to the Shadow AI procedure in Section 12 rather than normalizing the unregistered use.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Exit criterion</strong></p>
<p>A named business sponsor exists and there is sufficient information to open an inventory record.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 7.2 Step 2 - Create or update the AI inventory record

Accountable/Responsible: AI Governance Lead.

6.  Assign or confirm a unique AI ID.

7.  Record intended purpose, lifecycle stage, business owner, technical owner, users, affected parties, AI type, provider/model, data categories, third parties, integrations, and geography.

8.  Record whether the use is new, materially changed, discovered shadow AI, or a renewal/extension of an existing system.

9.  Record the current governance gate, assessment status, approval status, monitoring requirement, and next review trigger/date when known.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Exit criterion</strong></p>
<p>QuackTrack contains a minimally complete, traceable record and ownership gaps are either resolved or formally escalated.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 7.3 Step 3 - Define intended purpose and decision/support boundary

Accountable: Business / AI System Owner.

10. Document the business process and intended AI-enabled activity.

11. State what the AI may generate, predict, rank, recommend, detect, summarize, or automate.

12. State what decisions remain with humans and who has authority to review, override, escalate, or stop the AI-supported process.

13. Document unsupported/prohibited uses within the current design.

14. Define business success measures to baseline; do not present unvalidated benefit hypotheses as realized ROI.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Material-change trigger</strong></p>
<p>A change in intended purpose, autonomy, decision authority, affected population, data, provider/model, integration, or geography can invalidate prior assessment and approval.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 7.4 Step 4 - Preliminary legal and regulatory triage

Accountable: General Counsel for legal triage. AI Governance Lead coordinates the record. DPO, HR, Product Safety, Security, and other specialists are consulted as relevant.

15. Identify Duckworks’ preliminary role in relation to the system and whether a legal classification or specific legal review may be required.

16. Screen for prohibited/unacceptable practices and other legal gating issues before relying on an internal risk score.

17. Screen potentially relevant AI, privacy/data protection, employment/equality, product-safety, consumer, cybersecurity, intellectual-property, and sector-specific requirements.

18. Record applicability assumptions, uncertainties, required specialist advice, and legal-review flags.

19. Keep legal classification separate from the Duckworks Low/Moderate/High/Critical enterprise risk rating.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Important</strong></p>
<p>Regulatory triage is a gate, not a numerical risk multiplier. An unlawful use cannot be approved because its internal risk score is low.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 7.5 Step 5 - Complete AI impact assessment

Accountable: Business / AI System Owner. Responsible: AI Governance Lead and business owner.

20. Identify affected individuals, groups, operational teams, customers, applicants, suppliers, product users, and organizational interests.

21. Document intended benefits as well as plausible adverse impacts involving safety, privacy, fairness, accessibility, autonomy, transparency, security, customer outcomes, and operations.

22. Document meaningful human-oversight arrangements and contestability/escalation where relevant.

23. Define safeguards and monitoring indicators for material impacts.

24. State the current lifecycle decision or restriction resulting from the impact assessment.

### 7.6 Step 6 - Complete AI risk assessment

Accountable: Business / AI System Owner. AI Governance/Risk challenges the assessment.

25. Write material cause -\> event -\> impact scenarios across relevant Duckworks risk domains.

26. Score inherent severity and likelihood before crediting specific Duckworks mitigating controls.

27. Assess only controls that are actually implemented and supported by evidence.

28. Record control effectiveness and evidence confidence separately.

29. Re-score severity and likelihood after operating controls to determine current residual risk.

30. Define target controls and target residual risk without representing the target as the current state.

| **Internal rating** | **Score** | **Governance response**                                                                                  |
|---------------------|-----------|----------------------------------------------------------------------------------------------------------|
| Low                 | 1-4       | Owner acceptance; routine controls; at least annual review.                                              |
| Moderate            | 5-9       | Owner + AI Governance review; documented controls and monitoring.                                        |
| High                | 10-16     | AI Governance Committee approval/treatment; enhanced evidence; pre-production gate.                      |
| Critical            | 17-25     | Production normally blocked pending treatment or exceptional executive acceptance; immediate escalation. |

### 7.7 Step 7 - Perform specialist reviews

Specialist review depth depends on the intended purpose, data, affected parties, technology, supplier model, and impact. The following reviews are mandatory when the corresponding domain is material:

| **Review**                     | **Minimum review lens**                                                                                                                                                       |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Information Security           | Prompt injection, data leakage, insecure integration, excessive permissions, adversarial abuse, AI/model supply chain, logging, security testing, incident readiness.         |
| Privacy / DPO                  | Personal data, lawful processing questions, minimization, retention, data-subject impacts, processor/controller arrangements, and whether a formal DPIA workflow is required. |
| HR / Employment / Fairness     | Recruitment or workforce effects, discrimination/fairness, accessibility, criteria validity, automation bias, transparency, human review, contestability.                     |
| Product Safety & Quality       | Engineering validation, false negatives, quality acceptance, safety function, product reliability, human fallback, release criteria.                                          |
| Procurement / Vendor Assurance | Data use, model training, subprocessors, security, privacy, incident notification, service change, IP, continuity, exit, renewal.                                             |
| Legal / Contractual            | Applicable legal classification, contractual rights/obligations, transparency, liability, IP, product/customer commitments, other mandatory conditions.                       |

### 7.8 Step 8 - Define treatment, controls, evidence, and testing

Accountable: Business / AI System Owner for use-case treatment. Technical Owner, CISO, AI Governance, and specialists own/perform their assigned controls.

31. Select treatment: avoid/stop, reduce, transfer/share selected exposure, accept within delegated authority, or retire.

32. Assign each control a control owner, operating frequency/event trigger, required evidence, and testing approach.

33. Define technical and procedural controls for data access, security, human oversight, validation, third parties, monitoring, change, incident response, and retirement as applicable.

34. For higher-impact use, establish stronger evidence and pre-production testing before approval.

35. Do not reduce residual risk because a control is merely planned.

### 7.9 Step 9 - Validate model/service and human oversight

Accountable: Technical Owner for technical validation; Business Owner for decision-use suitability.

36. Test performance against use-case-relevant criteria and baseline expected operating conditions.

37. Test fallback, escalation, override, and stop authority for consequential processes.

38. For generative AI, test relevant prompt/RAG security, hallucination/content boundaries, sensitive-data handling, and unsafe tool/code behavior.

39. For product/quality AI, test false negatives, error modes, safety/quality boundaries, and human acceptance/fallback.

40. For workforce AI, conduct the required fairness, criteria, explainability, human-review, and contestability evidence before any deployment decision.

41. Retain validation evidence sufficient to support the stated release conditions and later assurance.

### 7.10 Step 10 - Governance approval

Approval follows current residual risk, legal gates, and system-specific release conditions.

| **Residual risk** | **Decision authority**                                        | **Operating rule**                                                                                                                          |
|-------------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Low               | Business / AI System Owner                                    | May approve use within defined scope if routine controls and evidence are complete.                                                         |
| Moderate          | Business Owner + AI Governance review                         | Documented controls and monitoring required; approval record retained.                                                                      |
| High              | AI Governance Committee                                       | Treatment, enhanced evidence, specialist challenge, and pre-production gate required. Business owner cannot self-approve.                   |
| Critical          | Normally blocked; exceptional CEO / executive acceptance only | Requires explicit exceptional escalation with Legal, Risk, and Security challenge. Exceptional acceptance does not override applicable law. |

### 7.11 Step 11 - Production release / lifecycle authorization

Accountable: Business / AI System Owner for operational release within the approved purpose and conditions.

42. Confirm all mandatory approval conditions and blocking actions are satisfied.

43. Confirm technical deployment and access controls correspond to the approved architecture and data boundary.

44. Confirm human-oversight, fallback, logging, monitoring, incident, and support arrangements are operational.

45. Record model/provider/version and material configuration sufficient for later traceability.

46. Update QuackTrack to the authorized lifecycle stage and record the next review/reassessment trigger.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Release boundary</strong></p>
<p>Authorization applies only to the stated intended purpose, users, data, geography, integrations, provider/model, and decision role. Material expansion requires reassessment.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 7.12 Step 12 - Operate and monitor

Accountable: Business / AI System Owner. Technical Owner provides model/service monitoring evidence.

47. Monitor business outcome, system performance, drift, harmful/incorrect outputs, complaints, override rates, incidents, control failures, and relevant fairness/safety indicators.

48. Monitor vendor/model/service changes that could invalidate prior evidence or approval.

49. Review control evidence at the cadence defined in the approval record and risk treatment plan.

50. Record significant deviations, exceptions, and remediation actions with owners and due dates.

51. Escalate threshold breaches or material harm indicators rather than waiting for the next routine review.

### 7.13 Step 13 - Reassessment after material change or significant event

Accountable/Responsible: AI Governance Lead coordinates reassessment; Business and Technical Owners provide evidence.

52. Trigger reassessment for changes in intended purpose, autonomy, decision authority, model/provider/version, data, users, affected groups, permissions, integrations, geography, or material operating environment.

53. Trigger reassessment after significant incidents, near misses, complaints, performance threshold breaches, material drift, control failure, expired evidence, or relevant legal/regulatory change.

54. Determine which prior artifacts remain valid and which must be updated.

55. Re-run legal triage, impact, risk, specialist review, testing, and approval to the depth necessary for the changed context.

56. Do not continue operation beyond the approved boundary while a blocking reassessment condition remains unresolved.

### 7.14 Step 14 - Suspend, stop, or contain

The AI Governance Committee directs suspension for material governance failure. The CISO retains emergency authority for security containment. Business/Technical owners execute safe fallback.

- Suspected confidential or personal data leakage, unauthorized access, credential exposure, or cross-user disclosure.

- Successful or suspected prompt injection, retrieval poisoning, malicious tool execution, model/service compromise, or abnormal unauthorized behavior.

- Repeated or material hallucinations, unsafe recommendations, incorrect customer commitments, or unsafe engineering/manufacturing outputs.

- Discriminatory or materially unfair outcomes, or loss of meaningful human review in consequential decisions.

- Significant drift, sudden performance degradation, vendor/model change, expired evidence, or control failure that invalidates the approved risk assessment.

- Production AI discovered without the required owner, registration, assessment, approval, or controls.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Safety caveat</strong></p>
<p>If immediate shutdown would itself create safety or material operational risk, the responsible owner must use the approved fallback and escalation procedure rather than an unsafe abrupt stop.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 7.15 Step 15 - Retire or decommission

Accountable: Business / AI System Owner. Responsible: Technical Owner and AI Governance Lead.

57. Confirm the retirement decision and business/system owner authorization.

58. Remove or disable user access, credentials, connectors, APIs, integrations, scheduled jobs, and production dependencies.

59. Complete vendor exit/termination actions and data disposition in accordance with applicable contracts, policy, retention schedules, and law.

60. Close monitoring and incident obligations that are no longer applicable while preserving required historical evidence.

61. Update QuackTrack to Retired/Decommissioned and retain closure evidence explaining why and when the system was retired.

## 8. Evidence and Auditability

Duckworks must be able to reconstruct how a material AI decision was made and demonstrate that claimed controls were operating at the relevant time. Evidence depth increases with impact and risk.

| **Evidence area**      | **Examples**                                                                                                                                                    |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Purpose & ownership    | AI ID; business/technical owner; intended purpose; decision boundary; lifecycle; users; affected parties; provider/model; data; integrations.                   |
| Assessment             | Impact assessment; risk scenarios; inherent/current/target risk; legal/privacy/security/HR/safety/vendor reviews as applicable.                                 |
| Control implementation | Configuration, procedures, access records, test results, monitoring records, supplier evidence, training/competence evidence, human oversight procedure.        |
| Approval & treatment   | Decision, decision authority, conditions, exceptions, accepted risk, actions, owners, due dates, meeting/committee record.                                      |
| Operation & monitoring | KPIs/KRIs; drift/error trends; complaints; overrides; incidents; control failures; vendor/model changes; reassessment dates.                                    |
| Change & closure       | Material-change assessment, reassessment decision, suspension/containment, retirement record, access/integration closure, data disposition, evidence retention. |

Record retention periods are governed by the applicable Duckworks corporate retention schedule, contractual requirements, and applicable law. This SOP does not invent a universal retention period.

## 9. Current Portfolio Governance Gates

The following positions are portfolio baseline decisions. They are not permanent classifications and must be reassessed when material facts change.

| **ID** | **System**               | **Current gate**                  | **Minimum procedural condition**                                                                                                   |
|--------|--------------------------|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| AI-001 | DuckDesign AI            | Restricted pilot only             | Competent engineer review; design validation; IP/data controls; no autonomous production design release.                           |
| AI-002 | QuackBot                 | Production blocked pending gates  | Prompt/RAG security testing; safe escalation; content boundaries; monitoring; customer-impact safeguards.                          |
| AI-003 | FeatherForecast          | Continue with monitoring          | Manager approval for material commitments; drift/performance monitoring; data-quality controls.                                    |
| AI-004 | WingInspect Vision       | Restricted pilot only             | Human inspector remains final authority; false-negative testing; no unvalidated safety-critical reliance.                          |
| AI-005 | DuckTalent AI            | Do not deploy in current state    | Enhanced legal/privacy/fairness review; meaningful human review; bias testing; transparency/contestability; Critical risk reduced. |
| AI-006 | PondGPT                  | Restricted pilot only             | Enterprise access enforcement; sensitive repository exclusions; prompt/RAG security; logging; acceptable-use controls.             |
| AI-007 | Unregistered GenAI Usage | Immediate containment / decompose | Discover individual uses; prevent sensitive uploads; approve tools; register material uses; investigate potential exposure.        |

## 10. Shadow AI / Unregistered Use Procedure

AI-007 is not treated as one homogeneous AI system. It is an organizational condition containing multiple unknown use cases that must be discovered and decomposed.

| **Action**        | **Required procedure**                                                                                                                                      |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Discover          | Identify tool/service, users, business purpose, data used, model/provider, integration, and whether the use has become operationally relied upon.           |
| Contain           | Prevent further sensitive uploads or uncontrolled integration where exposure is plausible; preserve relevant evidence; use proportionate security controls. |
| Assess exposure   | Determine whether confidential, personal, customer, HR, code, IP, credentials, or other sensitive information may have been disclosed or processed.         |
| Decompose         | Create separate inventory records for each materially distinct use case rather than one AI-007 record.                                                      |
| Assign owners     | Name a business owner and technical owner for each material use.                                                                                            |
| Assess and decide | Run normal intake, triage, impact, risk, specialist review, treatment, and approval.                                                                        |
| Remediate         | Stop, replace with an approved enterprise tool, restrict, or formally authorize the use based on the decision.                                              |
| Learn             | Update awareness, approved-tool guidance, discovery controls, and policy where systemic patterns are identified.                                            |

## 11. Exceptions and Risk Acceptance

An exception permits a controlled deviation from a Duckworks internal requirement; it does not waive applicable law, contract, or safety obligation.

62. The requester documents the requirement, reason for deviation, duration or review trigger, affected systems/data/people, compensating controls, and residual risk.

63. AI Governance and relevant specialists review the request.

64. Approval authority follows the residual-risk and policy authority applicable to the exception.

65. Exceptions are time-bound or event-bound and expire when material assumptions, purpose, provider/model, data, controls, or operating context change.

66. Expired or violated exceptions trigger reassessment or stop/suspension action.

## 12. Mandatory Escalation Triggers

- Critical residual risk or a proposed risk acceptance outside delegated authority.

- Potential prohibited practice or material legal classification issue requiring specialist review.

- Material impact on employment, fundamental rights, safety, vulnerable individuals, or product quality.

- Significant AI incident, confidential/personal data leakage, discriminatory outcome, unsafe recommendation, model compromise, or loss of human oversight.

- Unregistered production AI use or a de facto production dependency outside the approved intake process.

- Material vendor/model/service change that invalidates prior evidence or assumptions.

- Persistent control failure, overdue blocking remediation, or evidence insufficiency that undermines a High/Critical system decision.

## 13. Procedure Performance and Management Reporting

The AI Governance Lead maintains management reporting that supports prioritization rather than raw technical reporting. The current source set does not define numeric performance targets; targets should be approved separately after baselining.

| **Metric family**     | **Management view**                                                                            |
|-----------------------|------------------------------------------------------------------------------------------------|
| Inventory coverage    | Number/percentage of material AI uses registered; discovered shadow AI awaiting decomposition. |
| Ownership             | Records missing business or technical owner.                                                   |
| Assessment completion | AIA/risk/specialist reviews complete vs required.                                              |
| Risk distribution     | Low/Moderate/High/Critical current residual risk; target risk shown separately.                |
| Approval status       | Approved, conditionally approved, blocked, restricted pilot, suspended, retired.               |
| Remediation           | Open/overdue treatment actions; blocking actions by owner.                                     |
| Monitoring            | Overdue reviews; threshold breaches; drift/performance exceptions; complaints; overrides.      |
| Incidents             | Significant AI incidents, containment actions, unresolved investigations.                      |
| Third-party exposure  | Material AI vendors, upcoming renewals, unresolved due-diligence/change issues.                |
| Evidence health       | Expired, missing, or low-confidence evidence supporting material control claims.               |

## 14. Procedure Quality Checklist

| **Quality area**       | **Pass condition**                                                                                                |
|------------------------|-------------------------------------------------------------------------------------------------------------------|
| Ownership              | Exactly one accountable role is identifiable for each key activity; High/Critical self-approval is prevented.     |
| Purpose                | Intended purpose and AI decision/support boundary are documented and consistent across artifacts.                 |
| Legal separation       | Legal/regulatory classification is not inferred from Duckworks internal risk rating.                              |
| Control credit         | Only implemented controls supported by evidence reduce current residual risk.                                     |
| Current vs target risk | Target residual risk is not presented as current state.                                                           |
| Human oversight        | Reviewer competence, override, escalation, stop authority, and accountability are explicit where consequential.   |
| Traceability           | Inventory -\> impact -\> risk -\> treatment/decision -\> monitoring is traceable through the AI ID.               |
| Proportionality        | Governance depth reflects impact/risk rather than applying identical review to every system.                      |
| Independence           | Internal Audit has not been assigned operational control ownership.                                               |
| Assumptions            | Material unknowns are labelled and have validation/evidence requirements.                                         |
| Evidence               | Material approval and control claims are supported by current evidence or clearly labelled planned/not validated. |
| Lifecycle decision     | Every assessment states the current allowed, restricted, blocked, suspended, or retired status.                   |

## 15. Source Basis and Framework Position

This SOP is an internal Duckworks operating procedure derived from the controlled project artifact set. It does not reproduce or claim conformity with any external standard.

| **Project source**                                             | **SOP contribution**                                                                                                                                                                      |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Duckworks AI Governance Project - Business Scenario            | Defines the seven-entry portfolio, governance problem, controlled-innovation objective, and enterprise governance mandate.                                                                |
| Duckworks AI Responsible Use Policy v1.0                       | Defines mandatory internal responsible-use expectations, material-change triggers, evidence, incident/stop-use criteria, and role responsibilities.                                       |
| Duckworks AI RACI Chart v1.0                                   | Provides activity-level accountability across governance, intake, assessment, development/acquisition, approval, operation, retirement, and assurance.                                    |
| Duckworks AI Risk Classification & Assessment Methodology v1.0 | Provides intended-purpose-first risk assessment, 5x5 scoring, control evidence rules, residual/target risk, approval thresholds, and reassessment triggers.                               |
| Duckworks AI Business Use Case Portfolio v1.0                  | Defines the business process, intended use, human decision boundary, value measures, and current gate for six governed use cases; AI-007 is treated as a discovery/containment condition. |
| Duckworks Project Acceptance Criteria v1.0                     | Defines evidence-based acceptance criteria, current system-specific governance gates, legal separation, auditability, proportionality, and Internal Audit independence.                   |
| Duckworks Project Stakeholder Register v1.0                    | Defines executive, first-line, second-line, third-line, specialist, affected-party, and committee responsibilities.                                                                       |
| Duckworks Public Frameworks, Legislation & Guidance            | Maintains the authoritative-source hierarchy and distinction between binding law, official guidance, standards/frameworks, technical guidance, and internal requirements.                 |

### 15.1 External framework position

The project source set uses NIST AI RMF, ISO/IEC 42001, ISO/IEC 23894, ISO/IEC 42005, ISO/IEC 27001, ENISA guidance, MITRE ATLAS, OWASP GenAI guidance, and applicable European legislation as reference sources. These sources inform governance design but do not independently make this SOP a legal requirement or prove compliance/certification.

## 16. Document Control

| **Control**                   | **Value**                                                                                                                                                                                                                                                              |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Procedure owner               | AI Governance Lead - Eleanor Duckford                                                                                                                                                                                                                                  |
| Governance sponsor / approver | Chief Risk & Compliance Officer - Reginald Duckman                                                                                                                                                                                                                     |
| Required reviewers            | CISO; General Counsel; DPO; Head of Data & AI; HR; Procurement; Product Safety & Quality, as relevant                                                                                                                                                                  |
| Approval status               | Draft for simulated operational approval within the fictional portfolio                                                                                                                                                                                                |
| Effective date                | Upon approval                                                                                                                                                                                                                                                          |
| Review frequency              | At least annually and after material trigger events                                                                                                                                                                                                                    |
| Related artifacts             | AI Responsible Use Policy; AI RACI Chart; QuackTrack inventory; AI Business Use Case Portfolio; AI Risk Methodology; AIA/Risk Assessment packs; future Control Library, Monitoring Standard, Incident Playbook, Third-Party AI Questionnaire, Human Oversight Standard |

*Portfolio disclaimer. Duckworks, Project W.I.N.G., all named individuals, systems, risks, decisions, data, and evidence in this SOP are fictional and created exclusively for educational and professional portfolio purposes. This SOP is not legal advice, certification evidence, or a determination that any particular law applies to a real organization.*
