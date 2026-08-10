# Duckworks AI Governance Operational Playbook Pack

**DUCKWORKS**

AI Governance Operational Playbook Pack

Event-driven runbooks for intake, assessment, third parties, security, human oversight, release, incidents, monitoring, change, retirement and assurance

| **Document control** | **Value**                                                                              |
|----------------------|----------------------------------------------------------------------------------------|
| Document ID          | DW-WING-OPS-01                                                                         |
| Version              | 1.0                                                                                    |
| Status               | Portfolio Baseline - Draft for simulated approval                                      |
| Organization         | Duckworks (fictional)                                                                  |
| Document owner       | Eleanor Duckford - AI Governance Lead                                                  |
| Governance sponsor   | Reginald Duckman - Chief Risk & Compliance Officer                                     |
| Primary reviewers    | CISO; General Counsel; DPO; Head of Data & AI; HR; Procurement; Product Safety/Quality |
| Prepared date        | 9 August 2026                                                                          |
| Classification       | Portfolio / Synthetic / Non-production                                                 |

| **PURPOSE.** Turn Duckworks AI governance requirements into repeatable operational actions. The pack is designed to answer: what triggered action, who leads, what sequence is followed, what blocks progression, what evidence is retained, and when reassessment or escalation is required. |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **LEGAL / FRAMEWORK BOUNDARY.** These playbooks are Duckworks organizational procedures. They do not create legal obligations, determine regulatory classification, reproduce ISO clauses, or claim NIST/ISO conformity. Where a law may apply, the playbook routes the issue to Legal/Privacy and requires the applicable legal obligation to be recorded separately. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Duckworks operating principle:** No material AI without an owner, no owner without accountability, no material risk without treatment, and no control without evidence.

## 1. Scope and Operating Rules

This pack applies to internally developed AI, third-party AI services, AI-enabled SaaS, APIs, embedded AI, pilots, experiments, material changes to existing systems, and discovered shadow or unregistered AI. It supplements existing enterprise processes rather than replacing procurement, SDLC, information security, privacy, enterprise risk, business continuity, incident response or internal audit.

A playbook is an operational response to a trigger. A policy or standard establishes requirements; a playbook tells the responsible team what to do when an event occurs. Where a separate Duckworks policy, standard, assessment or contract exists, that artifact remains authoritative for its subject matter.

| **Rule**                           | **Duckworks operating position**                                                                                                                                     |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Intended purpose first             | Assess the actual use, affected persons, decision boundary, data, integrations and geography - not only the model type.                                              |
| Risk and law are separate          | Duckworks Low/Moderate/High/Critical ratings are enterprise risk ratings. They do not determine EU AI Act or other legal classification.                             |
| No evidence, no control credit     | Planned or asserted controls are not treated as implemented until operating evidence supports them.                                                                  |
| Proportionality                    | Governance intensity increases with material rights, safety, privacy, security, operational and third-party exposure.                                                |
| Human accountability               | Consequential employment, engineering, quality, procurement and customer decisions remain with authorized humans unless a formally approved design states otherwise. |
| Material change reopens governance | Changes to purpose, model, data, vendor, affected population, integrations, autonomy or legal context can invalidate prior approval.                                 |
| Independent assurance              | Internal Audit may observe and later test the framework but does not own or operate first- or second-line controls.                                                  |

### 1.1 Playbook selection

| **Playbook**                            | **Use when...**                                                                                                 | **Primary lead**                       |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------|----------------------------------------|
| PB-01 Intake & Registration             | A new, changed, purchased, embedded, experimental or discovered AI use case appears.                            | AI Governance Lead                     |
| PB-02 Risk, Impact & Legal Triage       | A registered use case needs governance classification, risk/impact scope and specialist gates.                  | Risk & Compliance / AI Governance      |
| PB-03 Enhanced Review                   | People, fundamental rights, safety, high/critical risk or other consequential impacts require deeper challenge. | AI Governance Committee / relevant SME |
| PB-04 Third-Party AI Acquisition        | An external AI provider, model, API or AI-enabled SaaS is being evaluated, renewed or materially changed.       | Procurement & Vendor Assurance         |
| PB-05 Shadow AI Discovery & Containment | Unapproved GenAI, browser extension, code assistant or external AI use is detected.                             | CISO + AI Governance                   |
| PB-06 AI Security Review                | AI-specific attack paths, permissions, integrations, model supply chain or GenAI security need review.          | CISO / Security                        |
| PB-07 Human Oversight                   | AI outputs influence employment, engineering, quality, customer, procurement or other material decisions.       | Business Owner                         |
| PB-08 Validation & Release Gate         | A pilot or system is proposed to enter production or expand materially.                                         | Business Owner + AI Governance         |
| PB-09 AI Incident & Escalation          | Harmful, discriminatory, unsafe, compromised, materially wrong or uncontrolled AI behavior occurs.              | CISO + AI Governance                   |
| PB-10 Monitoring & Drift                | A deployed/pilot system needs ongoing performance, risk and control monitoring.                                 | Technical Owner + Business Owner       |
| PB-11 Material Change & Reassessment    | Purpose, model, data, vendor, affected population, integration, geography or controls materially change.        | AI Governance Lead                     |
| PB-12 Suspension, Exit & Retirement     | A system must be paused, replaced, terminated or decommissioned.                                                | Business Owner + Technical Owner       |
| PB-13 Evidence & Assurance Readiness    | Controls and decisions need an auditable evidence trail or assurance preparation.                               | AI Governance Lead / Control Owners    |

### 1.2 Operating lifecycle

| **Lifecycle moment**               | **Primary playbook route**              | **Decision / evidence outcome**                                                          |
|------------------------------------|-----------------------------------------|------------------------------------------------------------------------------------------|
| Idea / experiment                  | PB-01 -\> PB-02                         | Known owner, purpose, data and initial governance route before material use.             |
| Consequential or higher-impact use | PB-03 + PB-07                           | Enhanced rights/safety/human-oversight safeguards and specialist challenge.              |
| External AI dependency             | PB-04 (+ PB-06 where security-relevant) | Due diligence, contract, change/incident cooperation and exit evidence.                  |
| Pilot / production release         | PB-08                                   | Recorded approve / conditional / block decision tied to evidence and monitoring.         |
| Operate and monitor                | PB-10 + PB-13                           | Current performance/control evidence and management visibility.                          |
| Incident or harmful behavior       | PB-09                                   | Containment, evidence, specialist/legal handoff, corrective action and restart decision. |
| Material change                    | PB-11 -\> affected playbooks -\> PB-08  | Prior approval reconfirmed or replaced before changed production use.                    |
| Suspend / retire                   | PB-12                                   | Safe fallback, access/data/vendor closure and preserved lifecycle evidence.              |

| **STATUS VOCABULARY.** Use controlled lifecycle terms consistently: Concept / Assessment; Restricted Pilot; Production Blocked Pending Gates; Production with Monitoring; Suspended; Retired/Terminated; or Immediate Containment for uncontrolled use. These are Duckworks governance states, not regulatory classifications. |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## 2. Roles, Decision Rights and Escalation

| **Role**                                            | **Operational responsibility in this pack**                                                                            |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Dr. Mallory Duckworth - CEO                         | Executive sponsor; resolves enterprise-level conflicts and exceptional risk matters within governance authority.       |
| Reginald Duckman - CRCO                             | Governance sponsor; chairs AI Governance Committee; owns risk methodology, policy and escalation model.                |
| Eleanor Duckford - AI Governance Lead               | Maintains QuackTrack inventory, coordinates assessments, playbooks, evidence and committee packs.                      |
| Cassandra Duckley - CISO                            | Owns AI security governance, threat-model expectations, security acceptance and incident/security challenge.           |
| Amelia Duckett - General Counsel                    | Provides legal interpretation, regulatory-role triage, contractual review and legal escalation.                        |
| Delia Duckham - DPO                                 | Provides privacy advice, DPIA guidance and data-protection challenge for personal-data AI.                             |
| Dr. Ada Duckfield - Head of Data & AI               | Owns AI/ML engineering practices, technical evidence, validation design, monitoring and model/service change evidence. |
| Beatrice Van Duck - CPO                             | Owns workforce governance and DuckTalent business outcomes; employment-domain reviewer.                                |
| Percival Duckworth - Procurement & Vendor Assurance | Owns AI supplier due diligence, contract route, renewal review and exit obligations.                                   |
| Quentin Duckwell - Product Safety & Quality         | Challenges AI that may affect product quality, reliability or safety.                                                  |
| System Business Owner                               | Owns intended purpose, business benefit, operating controls, treatment actions and first-line decisions.               |
| Technical Owner                                     | Owns implementation, configuration, testing, logging, monitoring, access and change evidence.                          |
| Penelope Duckins - Head of Internal Audit           | Provides independent assurance; may observe significant decisions but is not a control owner or approval substitute.   |

| **ESCALATION TRIGGERS.** Escalate when residual risk is Critical or outside delegated authority; potential prohibited/high-risk legal classification requires specialist review; employment, fundamental-rights or safety impact is material; a significant AI/security/privacy incident occurs; unregistered production use is discovered; or a vendor/model change invalidates prior evidence or assumptions. |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## PB-01 — New AI Intake & Registration

| **Field**        | **Operational instruction**                                                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Trigger          | Any new AI use case, AI-enabled feature, vendor/model/API, employee experiment moving beyond a controlled sandbox, embedded AI capability, or discovered unregistered use. |
| Lead             | Eleanor Duckford - AI Governance Lead                                                                                                                                      |
| Support          | Business Owner; Technical Owner; Risk; Security; Legal/Privacy/HR/Product Safety/Procurement as triggered                                                                  |
| Required outcome | A unique AI record exists before material use proceeds, with purpose, ownership, data, affected parties, third parties, lifecycle and initial governance route documented. |

| **Step** | **Action**                       | **What to do**                                                                                                                                                           | **Primary owner**               | **Evidence / output**               |
|----------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|-------------------------------------|
| 1        | Open intake                      | Create or update the QuackTrack record; retain the same AI ID across assessments, approvals, monitoring and retirement.                                                  | AI Governance Lead              | Inventory record / intake ticket    |
| 2        | Define purpose                   | Record the business problem, intended purpose, users, affected persons, decisions supported, prohibited boundaries and expected benefit.                                 | Business Owner                  | Approved purpose statement          |
| 3        | Describe technology              | Record AI type, model/service/provider if known, hosting, integrations, APIs, data sources and whether the capability is internal or third-party. Unknowns stay TBD.     | Technical Owner                 | Architecture / dependency summary   |
| 4        | Classify data                    | Identify personal, sensitive, confidential and IP data; document expected storage/processing geography where known.                                                      | Data Owner / Privacy / Security | Data classification and flow notes  |
| 5        | Identify human decision boundary | State who can rely on, override, escalate and stop AI-supported decisions.                                                                                               | Business Owner                  | Human authority statement           |
| 6        | Screen specialist triggers       | Flag employment, product safety, customer interaction, personal data, GenAI, high privilege, third-party dependency, cross-border processing and other material factors. | AI Governance Lead              | Triage flags                        |
| 7        | Assign next playbooks            | Route to PB-02 and any additional playbook required before pilot or production.                                                                                          | AI Governance Lead              | Playbook routing / owner assignment |
| 8        | Record provisional gate          | Set lifecycle state such as concept, restricted pilot, blocked, production with monitoring, suspended or retired.                                                        | AI Governance Lead + Owner      | Lifecycle decision                  |

### Stop / escalate when

- No accountable business owner or technical owner can be identified for a material use case.

- The intended purpose or decision boundary is too vague to assess.

- Sensitive/confidential data is already being submitted to an unapproved external AI service - invoke PB-05 and PB-09 as appropriate.

- The requester wants production use before required risk, security, privacy, legal, vendor or human-oversight gates are complete.

### Minimum evidence pack

- QuackTrack inventory record

- Approved purpose and decision boundary

- Owner assignments

- Data classification / preliminary data flow

- Provider/model/dependency record or explicit TBD

- Triage decision and next playbooks

- Lifecycle gate / approval status

### Duckworks application examples

**DuckTalent AI** Register as AI-005; keep provider/model/version as TBD until evidence exists; current gate remains Do Not Deploy.

**FeatherForecast** AI-003 is already governed and can use the intake playbook only for material expansion/change.

**Unregistered GenAI** AI-007 is a discovery condition; each material discovered use must be decomposed into a separate governed intake record.

## PB-02 — Risk, Impact & Legal Triage

| **Field**        | **Operational instruction**                                                                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Trigger          | A valid AI inventory entry exists and requires classification, assessment depth, legal/privacy/security screening or re-assessment. |
| Lead             | Risk & Compliance + AI Governance                                                                                                   |
| Support          | Business/Technical Owner; CISO; General Counsel; DPO; HR; Product Safety; Procurement                                               |
| Required outcome | Documented risk scenarios, internal risk rating, impact scope, legal-review flags, control gaps, treatment and approval route.      |

| **Step** | **Action**                        | **What to do**                                                                                                                                                                                                                             | **Primary owner**            | **Evidence / output**              |
|----------|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|------------------------------------|
| 1        | Confirm assessment context        | Validate intended purpose, lifecycle, users, affected parties, data, provider/model, geography, integrations and decision authority.                                                                                                       | AI Governance + Owner        | Validated assessment context       |
| 2        | Perform legal triage              | Screen potential prohibited practices, high-risk/legal role questions, transparency, privacy, employment/equality, product/safety, cybersecurity and other applicable law. Do not convert internal risk scores into legal classifications. | General Counsel / DPO + SMEs | Legal applicability record / flags |
| 3        | Identify risk scenarios           | Write cause -\> event -\> impact scenarios across rights/fairness, safety, privacy/data, security/abuse, reliability, transparency, human oversight, third party, operational and compliance domains.                                      | Risk + Owner + SMEs          | Risk scenario register             |
| 4        | Score inherent risk               | Use Duckworks 5x5 Severity x Likelihood method before crediting specific mitigating controls.                                                                                                                                              | Risk & Compliance            | Inherent score/rating              |
| 5        | Assess controls                   | Credit only controls that are implemented and supported by evidence; rate control effectiveness and evidence confidence separately.                                                                                                        | Control Owners + Risk        | Control/evidence assessment        |
| 6        | Score current residual risk       | Reassess severity and likelihood after operating controls rather than mathematically discounting inherent risk.                                                                                                                            | Risk & Compliance            | Current residual rating            |
| 7        | Determine impact assessment depth | Identify affected individuals/groups, positive/adverse impacts, accessibility, contestability, autonomy, safety and other relevant impacts.                                                                                                | AI Governance + Domain SME   | Impact assessment scope            |
| 8        | Set treatment and target          | Define avoid/reduce/transfer-share/accept/retire actions; target residual risk is future-state only.                                                                                                                                       | Owner + Risk                 | Treatment plan / target risk       |
| 9        | Assign approval authority         | Low: owner/routine; Moderate: owner + AI Governance review; High: AI Governance Committee with enhanced evidence; Critical: normally block/escalate pending treatment or exceptional acceptance.                                           | AI Governance Lead           | Approval route and conditions      |

| **CONTROL CREDIT RULE.** A planned control does not reduce current residual risk. Evidence confidence must be recorded. High/Critical inherent-risk systems should not be represented as Low residual risk when the evidence supporting the reduction is weak or unverified. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Stop / escalate when

- A potentially unlawful or prohibited practice is identified - numeric risk scoring cannot authorize it.

- Critical current residual risk remains and production is proposed without treatment/exceptional escalation.

- Assessment facts are materially unverified in areas such as decision authority, provider/model, data or affected population.

### Minimum evidence pack

- Assessment context

- Legal/regulatory triage record

- Risk scenario register

- Inherent and residual scores

- Control effectiveness / evidence confidence

- Impact assessment

- Treatment plan

- Approval decision and review date

### Duckworks application examples

**DuckTalent AI** Current Critical residual risk and recruitment impacts require PB-03; legal/privacy/fairness work remains blocking.

**FeatherForecast** Moderate operational/financial profile supports proportionate governance, but data quality, drift and human planning approval remain required.

**DuckDesign / WingInspect** Safety and product consequences require enhanced review even where formal human decision authority remains.

## PB-03 — Enhanced Review for People, Rights and Safety AI

| **Field**        | **Operational instruction**                                                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Trigger          | High/Critical internal risk; employment/candidate impact; product/physical safety; fundamental-rights or vulnerable-person impact; significant autonomy; or specialist review requires enhanced governance. |
| Lead             | AI Governance Committee / relevant domain owner                                                                                                                                                             |
| Support          | General Counsel; DPO; CISO; HR; Product Safety; Data & AI; Business Owner                                                                                                                                   |
| Required outcome | A defensible go/conditional-go/no-go decision supported by deeper validation, rights/safety analysis, human oversight, specialist challenge and evidence.                                                   |

| **Step** | **Action**                      | **What to do**                                                                                                                                                             | **Primary owner**                 | **Evidence / output**                           |
|----------|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|-------------------------------------------------|
| 1        | Confirm trigger                 | Document why enhanced review applies and which domain(s) make the system consequential.                                                                                    | AI Governance Lead                | Enhanced-review trigger record                  |
| 2        | Validate human authority        | Confirm who makes the consequential decision, their competence, override/stop authority, review burden and safeguards against automation bias.                             | Business Owner                    | Oversight design                                |
| 3        | Deepen impact assessment        | Assess affected people/groups, positive/adverse impacts, fairness, accessibility, contestability, privacy, autonomy and safety as applicable.                              | AI Governance + SMEs              | Enhanced AIA / impact record                    |
| 4        | Complete privacy route          | Where personal data creates likely high risk, route to DPO for DPIA determination and completion before processing as required.                                            | DPO / Privacy                     | DPIA or documented determination                |
| 5        | Complete legal classification   | Legal confirms relevant AI Act/other legal role and applicability questions; any mandatory conformity/documentation duties remain separate workstreams.                    | General Counsel                   | Legal classification memo/record                |
| 6        | Define validation plan          | Set accuracy, robustness, error-distribution, fairness, safety and human-factors testing appropriate to the intended use. Do not invent thresholds after results are seen. | Data & AI + Domain SME            | Validation plan and pre-set acceptance criteria |
| 7        | Review affected-user safeguards | Document notices, explanations, complaint/contest routes, accessibility accommodations and escalation where relevant.                                                      | Business Owner + Legal/Privacy/HR | Safeguard design                                |
| 8        | Committee decision              | Approve only when blocking evidence is complete and residual risk is within delegated appetite; otherwise condition, block or escalate.                                    | AI Governance Committee           | Decision record + conditions                    |

### Stop / escalate when

- No meaningful human review is feasible for a consequential decision that Duckworks assumes remains human-accountable.

- Fairness, safety, performance or rights-impact validation is absent for a system whose risk materially depends on that evidence.

- The legal role/classification remains unresolved where it affects deployment obligations.

- A Critical residual risk is being described as cleared for unrestricted production.

### Minimum evidence pack

- Enhanced impact assessment

- DPIA/FRIA/legal analysis where applicable or voluntarily adopted

- Human oversight procedure

- Validation protocol and results

- Fairness/accessibility evidence where relevant

- Specialist reviews

- Committee decision / conditions

- Monitoring and contestability plan

### Duckworks application examples

**DuckTalent AI** Primary example. Current gate: Do Not Deploy. Recruitment ranking, applicant privacy, fairness, accessibility, explainability, contestability and human review are blocking topics.

**DuckDesign AI** Enhanced engineering validation is required before AI-assisted output can influence production design.

**WingInspect Vision** False-negative performance, qualified human inspection and safe fallback are central acceptance conditions.

## PB-04 — Third-Party AI Acquisition, Renewal & Contracting

| **Field**        | **Operational instruction**                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Trigger          | A vendor, AI model, hosted service, API, AI-enabled SaaS, subprocessor or externally managed AI component is proposed, renewed or materially changed.                          |
| Lead             | Percival Duckworth - Procurement & Vendor Assurance                                                                                                                            |
| Support          | CISO; DPO; General Counsel; Data & AI; AI Governance; Business Owner                                                                                                           |
| Required outcome | No material AI supplier proceeds without due diligence, purpose/data boundaries, risk-proportionate contract controls, change/incident duties, evidence and exit arrangements. |

| **Step** | **Action**                        | **What to do**                                                                                                                                                                                             | **Primary owner**                  | **Evidence / output**                  |
|----------|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|----------------------------------------|
| 1        | Register before purchase          | Create/confirm AI ID and intended purpose before purchase, pilot beyond sandbox or acceptance of material click-through terms.                                                                             | AI Governance + Procurement        | Inventory/intake record                |
| 2        | Perform AI-specific due diligence | Assess security, privacy, data retention/use, model training use, subprocessors, service continuity, IP, testing, documentation, model/service change and exit.                                            | Procurement + SMEs                 | Due diligence questionnaire / evidence |
| 3        | Map data and access               | Identify Duckworks data categories, integrations, permissions, storage locations and whether vendor may train/fine-tune on Duckworks data.                                                                 | Technical Owner + Privacy/Security | Data/architecture record               |
| 4        | Assess vendor dependency          | Identify concentration, lock-in, model/cloud dependencies, fallback, portability and business continuity exposure.                                                                                         | Business Owner + Procurement       | Dependency/BCP assessment              |
| 5        | Set contract requirements         | Use the Duckworks AI Vendor Contract Template; apply CORE/ENHANCED/CONDITIONAL LEGAL modules based on facts and legal review.                                                                              | General Counsel + Procurement      | Executed contract / redline record     |
| 6        | Validate change notification      | Contract and operating process must make material model/service/data/subprocessor changes visible to Duckworks before they silently invalidate prior assessments.                                          | Procurement + AI Governance        | Change clause / notification route     |
| 7        | Validate incident cooperation     | Define vendor contact route, evidence sharing, containment cooperation and legal/privacy escalation. Contractual response targets are internal commercial requirements, not automatic statutory deadlines. | CISO + Legal                       | Incident clause / contact matrix       |
| 8        | Approve and schedule renewal      | Record approval conditions, evidence refresh dates and renewal/exit responsibilities.                                                                                                                      | Business Owner + AI Governance     | Approval + renewal calendar            |

### Stop / escalate when

- Vendor cannot explain material data use, training use, retention, subprocessors or model/service change practices.

- Vendor contract terms permit use of Duckworks confidential/personal data inconsistent with approved purpose or policy.

- Material supplier cannot provide evidence sufficient to support High/Critical risk conclusions.

- A material public AI service is being adopted through unmanaged individual click-through terms.

### Minimum evidence pack

- AI due diligence

- Security/privacy assessment

- Data-use and training-use terms

- Subprocessor/dependency record

- Contract / DPA / AI schedule as applicable

- Service/change/incident commitments

- Exit/portability plan

- Renewal review record

### Duckworks application examples

**DuckDesign AI** Third-party foundation/optimization services require IP/confidentiality, training-use and engineering-change controls.

**QuackBot / PondGPT** Hosted GenAI requires tenant isolation, permissions, RAG/data controls, vendor-change visibility and incident cooperation.

**DuckTalent AI** Vendor/model remains TBD; procurement cannot complete until technical selection and enhanced employment/privacy requirements are known.

## PB-05 — Shadow AI Discovery & Containment

| **Field**        | **Operational instruction**                                                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Trigger          | Unregistered public GenAI, AI browser extension, coding assistant, external chatbot, personal AI account or other AI use is discovered outside approved intake/governance. |
| Lead             | Cassandra Duckley - CISO + Eleanor Duckford - AI Governance Lead                                                                                                           |
| Support          | IT; Business Owner; Privacy; Legal; HR; Procurement; affected system owner                                                                                                 |
| Required outcome | Immediate unmanaged exposure is contained; data exposure is assessed; material uses are decomposed, registered and either approved with controls or stopped.               |

| **Step** | **Action**                 | **What to do**                                                                                                                                                        | **Primary owner**           | **Evidence / output**                     |
|----------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------|
| 1        | Preserve facts             | Record tool/service, user/team, dates, purpose, accounts, browser extensions, integrations and known data submitted. Do not alter evidence before basic fact capture. | Security / AI Governance    | Discovery record                          |
| 2        | Contain sensitive activity | Stop further upload of restricted, confidential, personal or other disallowed data; disable risky extensions/integrations where proportionate.                        | Security / IT               | Containment action                        |
| 3        | Assess exposure            | Determine whether confidential/IP, customer, employee, applicant or credentials/code were entered; identify vendor retention/training uncertainty.                    | Security + Privacy + Owner  | Exposure assessment                       |
| 4        | Decide incident route      | If actual or suspected disclosure, compromise, harmful output or unauthorized decision occurred, invoke PB-09 and enterprise privacy/security incident processes.     | CISO + DPO/Legal            | Incident case / decision                  |
| 5        | Decompose use cases        | Treat AI-007 as an organizational condition, not one homogeneous system. Create separate intake records for material recurring uses.                                  | AI Governance Lead          | New AI IDs / use-case records             |
| 6        | Assess business need       | Identify whether an approved enterprise alternative (e.g., PondGPT) can meet the need with lower unmanaged exposure.                                                  | Business Owner + IT         | Approved alternative / exception decision |
| 7        | Complete governance        | Run PB-01/PB-02 and PB-04 if a material external service is to continue.                                                                                              | AI Governance + Procurement | Assessment/contract route                 |
| 8        | Close and learn            | Record remediation, user guidance, policy/control gap, detection improvement and whether awareness content needs update.                                              | CISO + AI Governance        | Closure / lessons learned                 |

### Stop / escalate when

- Sensitive/confidential/personal data exposure cannot yet be bounded - treat as an incident candidate.

- The team proposes continued production use before the tool is registered and reviewed.

- A browser extension or public SaaS has excessive access to mail, files, code or credentials without approved architecture.

### Minimum evidence pack

- Discovery record

- Containment actions

- Exposure/data assessment

- Incident determination

- Decomposed AI inventory records

- Approved/blocked use decision

- Remediation evidence

- Lessons-learned actions

### Duckworks application examples

**AI-007 Unregistered GenAI Usage** Current gate is Immediate Containment. This playbook is the primary operating response.

**PondGPT** Can serve as a controlled enterprise alternative where architecture, access and data boundaries are validated; it is not automatically safe merely because it is enterprise-hosted.

## PB-06 — AI Security Review & Abuse Resistance

| **Field**        | **Operational instruction**                                                                                                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Trigger          | A GenAI/RAG system, external AI integration, model supply chain, privileged AI capability, code generation, computer vision, or other AI-specific attack surface requires security challenge. |
| Lead             | Cassandra Duckley - CISO / Security                                                                                                                                                           |
| Support          | Technical Owner; Data & AI; AI Governance; Vendor; Business Owner                                                                                                                             |
| Required outcome | Documented AI threat model, test plan/results, access controls, logging, unresolved findings and security acceptance conditions before release.                                               |

| **Step** | **Action**                          | **What to do**                                                                                                                                                                                                                      | **Primary owner**          | **Evidence / output**         |
|----------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|-------------------------------|
| 1        | Define trust boundaries             | Map users, model/service, system prompts, RAG/retrieval sources, plugins/tools, APIs, identities, secrets, data stores and downstream actions.                                                                                      | Security + Technical Owner | Threat-model architecture     |
| 2        | Identify AI-specific threats        | Consider prompt/indirect injection, retrieval poisoning, sensitive-data leakage, excessive agency/permissions, insecure output handling, model supply-chain compromise, adversarial inputs, unsafe generated code and abuse/misuse. | Security                   | Threat register               |
| 3        | Review identity and least privilege | Confirm AI cannot access or act beyond the user/service account authorization boundary; test privilege amplification and cross-user leakage scenarios.                                                                              | Security + IT              | Access review / test evidence |
| 4        | Review data boundaries              | Confirm prompts, logs, embeddings, retrieval stores and vendor telemetry follow approved data classification, retention and training-use rules.                                                                                     | Security + Privacy         | Data-security assessment      |
| 5        | Define proportionate testing        | Set tests for the specific architecture and intended use. Full penetration testing/red teaming may be outside this portfolio, but production criteria must state what real testing is required.                                     | Security + Data & AI       | Security test plan            |
| 6        | Execute / capture available tests   | Record prompt-injection, retrieval, leakage, unsafe-code, abuse, authentication/authorization and resilience tests available in the project or require them as a blocking evidence item.                                            | Security / Engineering     | Test results or blocking gap  |
| 7        | Assess monitoring                   | Confirm logs can detect abuse, anomalous requests, high-risk tool calls, permission failures, unsafe output patterns and vendor incidents as relevant.                                                                              | Security + Technical Owner | Logging/alert design          |
| 8        | Issue security decision             | Accept, conditionally accept, block or escalate; unresolved critical security findings remain visible in the risk treatment plan.                                                                                                   | CISO                       | Security acceptance record    |

### Stop / escalate when

- The AI can retrieve data a user is not otherwise authorized to access.

- A GenAI system can invoke high-impact actions without appropriate authorization, validation or rollback.

- Known prompt/RAG or data-leakage vulnerabilities remain open for a use case handling sensitive data or consequential decisions.

- Security test evidence is claimed but cannot be produced.

### Minimum evidence pack

- Threat model

- Architecture/trust boundary diagram

- Access-control review

- Security test plan/results

- Open findings and treatment

- Logging/monitoring design

- Security approval/conditions

### Duckworks application examples

**QuackBot** Prompt injection, retrieval poisoning, customer-data leakage, hallucinated technical advice and escalation boundaries are priority threats.

**PondGPT** Cross-user retrieval, document permissions, code generation, prompt/RAG injection and sensitive repository exclusions are key.

**DuckDesign AI** Confidential CAD/IP leakage, model/service supply chain and unsafe generated engineering suggestions require security + engineering review.

**WingInspect Vision** Adversarial/abnormal images, data integrity and model/version integrity matter where defect detection influences quality decisions.

## PB-07 — Human Oversight & Decision Control

| **Field**        | **Operational instruction**                                                                                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Trigger          | AI outputs influence a consequential business, employment, engineering, quality, procurement, customer or safety decision, or prior approval assumes meaningful human accountability. |
| Lead             | System Business Owner                                                                                                                                                                 |
| Support          | Domain SME; AI Governance; HR/Product Safety/Customer Ops; Technical Owner                                                                                                            |
| Required outcome | Human reviewers have authority, competence, time, information, override/stop capability and evidence that review is meaningful rather than ceremonial.                                |

| **Step** | **Action**                             | **What to do**                                                                                                                                      | **Primary owner**                      | **Evidence / output**             |
|----------|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|-----------------------------------|
| 1        | Define decision owner                  | Name the human role accountable for the final decision and specify which actions the AI may and may not take.                                       | Business Owner                         | Decision-authority matrix         |
| 2        | Define reviewer competence             | Specify domain knowledge, training and system limitations reviewers must understand.                                                                | Business Owner + HR/Domain SME         | Competence requirements           |
| 3        | Design review information              | Provide the AI output, relevant source/context, uncertainty/limitations and comparison evidence needed for independent judgment.                    | Technical Owner + Domain SME           | Reviewer interface / instructions |
| 4        | Enable override and stop               | Reviewer must be able to reject/override the output, choose an alternative process, escalate and stop AI-supported processing when needed.          | Technical Owner + Business Owner       | Override/stop procedure           |
| 5        | Control automation bias                | Use sampling, second review, disagreement prompts, mandatory rationale or other proportionate safeguards where risk of rubber-stamping is material. | Business Owner + AI Governance         | Oversight control design          |
| 6        | Document exceptions and contestability | Record how affected persons/users can raise concerns and how contested or harmful decisions are re-reviewed where relevant.                         | Business Owner + Legal/HR/Customer Ops | Escalation/contest route          |
| 7        | Monitor oversight effectiveness        | Track override/disagreement rates, review time, errors discovered by humans, escalation patterns and signs of over-reliance.                        | Business Owner + Data & AI             | Oversight metrics                 |
| 8        | Reassess if authority changes          | Any move toward autonomous decision-making or reduced human review invokes PB-11 before implementation.                                             | AI Governance Lead                     | Reassessment record               |

### Stop / escalate when

- The named reviewer lacks authority to override or stop the AI-supported decision.

- Reviewers are expected to approve outputs faster than they can reasonably evaluate them.

- The system withholds information necessary for meaningful review or makes the human step functionally automatic.

- A proposed automation change contradicts an assessment assumption that humans retain formal accountability.

### Minimum evidence pack

- Human oversight procedure

- Role/authority matrix

- Training/competence records

- Override/stop test evidence

- Decision/override logs

- Escalation/contest procedure

- Oversight monitoring metrics

### Duckworks application examples

**DuckTalent AI** Recruiters/hiring managers retain final authority; autonomous rejection/hiring is prohibited under current design assumptions.

**WingInspect Vision** Qualified human inspectors remain final acceptance/rejection authority.

**DuckDesign AI** Competent engineers review and validate outputs before prototype/production design use.

**FeatherForecast** Authorized managers approve material purchasing/production commitments.

**QuackBot** Human escalation is required for uncertain, sensitive or safety-relevant interactions.

## PB-08 — Validation & Release Gate

| **Field**        | **Operational instruction**                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Trigger          | A system is proposed to move from concept to pilot, restricted pilot to production, or to materially expand users, data, autonomy, geography or business dependency. |
| Lead             | System Business Owner + AI Governance Lead                                                                                                                           |
| Support          | Technical Owner; Risk; Security; Legal/Privacy/HR/Product Safety/Procurement as triggered; AI Governance Committee for High/Critical                                 |
| Required outcome | A written release decision tied to evidence, unresolved risk, operating controls, monitoring and rollback/stop capability.                                           |

| **Step** | **Action**                       | **What to do**                                                                                                                                           | **Primary owner**                | **Evidence / output**            |
|----------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|----------------------------------|
| 1        | Confirm gate requested           | State exactly what change is being approved: pilot, production, new population, new country, new automation, new model or other expansion.               | Business Owner                   | Release request                  |
| 2        | Check mandatory predecessors     | Verify inventory, risk/impact assessment, specialist reviews, vendor review, human oversight and required legal/privacy work are complete for this gate. | AI Governance Lead               | Gate checklist                   |
| 3        | Validate performance             | Use intended-purpose-specific performance and robustness evidence; record data/sample limits and conditions.                                             | Data & AI + Domain SME           | Validation report                |
| 4        | Validate controls                | Confirm security, data, access, logging, human oversight, fallback, incident and change controls are implemented and evidenced.                          | Control Owners                   | Control evidence pack            |
| 5        | Confirm monitoring thresholds    | Before release, define metrics, thresholds/decision rules, owners, review cadence and what triggers containment/reassessment.                            | Technical + Business Owner       | Monitoring plan                  |
| 6        | Confirm rollback / safe fallback | Demonstrate how the AI can be disabled or bypassed without unacceptable operational or safety consequences.                                              | Technical Owner + Business Owner | Rollback/fallback evidence       |
| 7        | Resolve open risks               | All blocking actions must be closed; non-blocking actions need owners/dates and accepted residual risk within authority.                                 | Risk + Owner                     | Action tracker / risk acceptance |
| 8        | Record release decision          | Approve, conditionally approve, block, suspend or escalate. The decision must identify evidence and conditions.                                          | Authorized approver              | Signed/recorded gate decision    |

| **System**               | **Current Duckworks gate**       | **Minimum current acceptance conditions**                                                                                            |
|--------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| DuckDesign AI            | Restricted pilot only            | Competent engineer review; design validation; IP/data controls; no autonomous release to production design.                          |
| QuackBot                 | Production blocked pending gates | Prompt/RAG security testing; safe escalation; content boundaries; monitoring; customer-impact safeguards.                            |
| FeatherForecast          | Continue with monitoring         | Manager approval for material commitments; drift/performance monitoring; data-quality controls.                                      |
| WingInspect Vision       | Restricted pilot only            | Human inspector final authority; false-negative testing; no unvalidated safety-critical reliance.                                    |
| DuckTalent AI            | Do not deploy in current state   | Enhanced legal/privacy/fairness analysis; meaningful human review; bias testing; transparency/contestability; Critical risk reduced. |
| PondGPT                  | Restricted pilot only            | Enterprise access enforcement; sensitive repository exclusions; prompt/RAG security; logging; acceptable-use controls.               |
| Unregistered GenAI Usage | Immediate containment            | Discover uses; prevent sensitive uploads; approve tools; register material uses; investigate exposure.                               |

### Stop / escalate when

- Blocking evidence is missing or only planned.

- Critical residual risk remains without exceptional escalation.

- The requested release expands purpose/autonomy/data/affected persons beyond the assessed boundary.

- No reliable rollback, fallback or monitoring path exists for a safety-, rights- or business-critical use.

### Minimum evidence pack

- Release checklist

- Validation reports

- Control evidence

- Open action tracker

- Monitoring/rollback plan

- Specialist approvals

- Final gate decision

## PB-09 — AI Incident & Escalation

| **Field**        | **Operational instruction**                                                                                                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Trigger          | Harmful/unsafe output, discriminatory outcome, confidential-data disclosure, security compromise, inappropriate automated decision, major drift, vendor incident, loss of human oversight, product-safety concern or other governance-significant AI event. |
| Lead             | CISO + AI Governance Lead                                                                                                                                                                                                                                   |
| Support          | Business Owner; Technical Owner; Legal; DPO; HR; Product Safety; Procurement/Vendor; Communications as appropriate                                                                                                                                          |
| Required outcome | Contain harm, preserve evidence, restore safe operation, complete legal/privacy/safety handoff, identify root cause/control failures and require reapproval where the incident invalidates prior assumptions.                                               |

| **Step** | **Action**                               | **What to do**                                                                                                                                                                                         | **Primary owner**                             | **Evidence / output**            |
|----------|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|----------------------------------|
| 1        | Triage event                             | Record what happened, system/AI ID, model/version, users/affected persons, decision/output, data involved, time detected and whether harm is ongoing.                                                  | CISO + AI Governance                          | Incident intake record           |
| 2        | Protect people / operations              | Stop or constrain harmful outputs, unsafe automation, affected workflows or exposed integrations; use manual fallback when required.                                                                   | Business/Technical Owner                      | Containment action               |
| 3        | Preserve evidence                        | Retain relevant logs, prompts, outputs, model/version/configuration, retrieval sources, access events, vendor notices, decisions and screenshots consistent with existing incident procedures.         | Security + Technical Owner                    | Evidence package                 |
| 4        | Classify parallel obligations            | Determine whether the event is also a cybersecurity incident, personal-data breach, product-safety issue, employment/rights complaint, contractual/vendor incident or potential statutory AI incident. | Legal/DPO/CISO/Product Safety                 | Parallel incident classification |
| 5        | Engage vendor if relevant                | Obtain containment, model/service status, affected versions, IOCs/known failure mechanism, data impact and change history.                                                                             | Procurement + CISO                            | Vendor incident record           |
| 6        | Assess affected decisions                | Identify decisions/outputs that may need review, correction, customer/candidate/user remediation or product containment.                                                                               | Business Owner + Domain SME                   | Impact review                    |
| 7        | Determine legal notifications separately | Legal/DPO determines any statutory notification/reporting requirement and deadline. This playbook does not invent or substitute those deadlines.                                                       | General Counsel / DPO                         | Legal notification decision      |
| 8        | Root cause and treatment                 | Identify technical, process, vendor, data, human-oversight and governance control failures; assign corrective actions.                                                                                 | CISO + Risk + Owner                           | RCA / action plan                |
| 9        | Reapproval decision                      | Invoke PB-11 and PB-08 before resuming where the incident changes assumptions, controls, model confidence, risk or intended operating boundary.                                                        | AI Governance Committee / authorized approver | Reassessment / restart decision  |
| 10       | Lessons learned                          | Update playbooks, risk scenarios, controls, vendor terms, monitoring and training as appropriate.                                                                                                      | AI Governance Lead                            | Lessons-learned record           |

| **Incident category**     | **Examples**                                                                                           | **Immediate governance concern**                                                      |
|---------------------------|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Safety / physical         | Unsafe engineering recommendation; defect missed; AI contributes to hazardous product outcome.         | Stop affected reliance; Product Safety escalation; preserve model/output evidence.    |
| Fairness / rights         | Systematic candidate ranking disparity; inaccessible process; inappropriate employment recommendation. | Suspend affected decision path; HR/Legal/Privacy review; identify affected decisions. |
| Security / abuse          | Prompt injection; retrieval poisoning; credential/data exfiltration; compromised model/component.      | Contain access/integration; Security incident route; vendor coordination.             |
| Privacy / confidentiality | Personal/confidential data exposed through prompts, outputs, logs, retrieval or vendor.                | DPO/Security route; bound data and affected persons; preserve evidence.               |
| Reliability / drift       | Material accuracy degradation; hallucination pattern; false-negative spike.                            | Reduce/stop reliance; validate scope; monitor affected outputs.                       |
| Oversight failure         | Human review bypassed, rubber-stamped or technically impossible.                                       | Restore human authority; review affected decisions; reassess autonomy.                |
| Vendor / change           | Unnotified model replacement; material subprocessor or data-use change.                                | Freeze/limit use where necessary; vendor escalation; reassess evidence.               |

### Stop / escalate when

- Ongoing risk to people, product safety or confidential information exists.

- The system cannot be placed into a safe/manual fallback state.

- A material incident is being handled only as a technical defect with no business, rights, privacy, legal or governance review.

### Minimum evidence pack

- Incident record

- Containment log

- Prompt/output/model/version/log evidence

- Affected decision review

- Legal/privacy/safety classification

- Vendor correspondence

- RCA and corrective actions

- Restart/reapproval decision

- Lessons learned

### Restart gate after a material AI incident

| **Restart question**                         | **Minimum answer before resumption**                                                                                                              |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Is ongoing harm contained?                   | Yes; affected workflow is stable or operating on a validated manual/replacement fallback.                                                         |
| Is the affected scope known?                 | System/model/version, data, users/affected persons, time window and affected decisions are sufficiently bounded.                                  |
| Is the failure mechanism understood enough?  | Root cause or credible causal hypothesis exists and corrective controls target the actual failure path.                                           |
| Are legal/privacy/safety decisions recorded? | Relevant specialists have recorded whether notifications, remediation, product/employment/customer actions or further investigation are required. |
| Have controls been validated?                | Corrective controls are implemented and evidenced; planned controls alone do not justify restart.                                                 |
| Is monitoring strengthened?                  | Post-incident metrics/alerts and review frequency are updated for the observed failure mode.                                                      |
| Has authority approved restart?              | PB-11/PB-08 decision is recorded where prior assumptions, risk or controls were invalidated.                                                      |

| **NOTIFICATION TIMING PRINCIPLE.** Use existing statutory, regulatory, contractual and enterprise incident processes to determine deadlines. The playbook requires immediate internal escalation to Legal/DPO/Security when a reporting trigger may exist, but it deliberately does not invent a universal AI notification deadline. |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## PB-10 — AI Monitoring, Drift & Performance Degradation

| **Field**        | **Operational instruction**                                                                                                                                   |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Trigger          | An AI system is in pilot or production and requires ongoing monitoring, or a KPI/KRI/control threshold is breached.                                           |
| Lead             | Technical Owner + Business Owner                                                                                                                              |
| Support          | Data & AI; AI Governance; Security; Privacy; Domain SMEs                                                                                                      |
| Required outcome | Ongoing evidence shows whether the AI remains within approved purpose, performance, risk and control boundaries, with clear escalation/reassessment triggers. |

| **Step** | **Action**                        | **What to do**                                                                                                                                                                             | **Primary owner**             | **Evidence / output**      |
|----------|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|----------------------------|
| 1        | Establish baseline                | Before release, record approved version/configuration, validation results, risk assumptions and expected operating range.                                                                  | Technical Owner               | Baseline record            |
| 2        | Set metrics and owners            | Choose measures relevant to the use case: performance, drift, harmful outputs, fairness, override, complaints, security/privacy events, vendor changes, availability and control failures. | Business + Technical Owner    | Monitoring plan            |
| 3        | Set thresholds before use         | Define decision rules for investigate, restrict, suspend or reassess before relying on live results. Avoid retrofitting thresholds to justify observed performance.                        | Owner + Risk + Domain SME     | Threshold/decision table   |
| 4        | Collect operating evidence        | Retain monitoring data at the cadence appropriate to risk and existing records requirements.                                                                                               | Technical Owner               | Monitoring records         |
| 5        | Review human/system interaction   | Evaluate override rates, complaints, escalations, manual corrections, user over-reliance and workload where relevant.                                                                      | Business Owner                | Human/feedback metrics     |
| 6        | Review changes and vendor notices | Check model/service version, provider changes, data sources, integrations, permissions and dependencies.                                                                                   | Technical Owner + Procurement | Change/dependency review   |
| 7        | Investigate deviations            | Determine whether a threshold breach is noise, data quality issue, drift, misuse, security event, model change, rights/safety issue or control failure.                                    | Data & AI + SMEs              | Investigation record       |
| 8        | Escalate appropriately            | Use PB-09 for incidents, PB-11 for material changes, PB-08 for re-release, or corrective action within delegated authority for non-material deviations.                                    | AI Governance Lead            | Escalation / action record |

| **System**         | **Example monitoring dimensions - targets remain TBD until baselined**                                                                                             |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DuckDesign AI      | Engineering rejection/override rate; validation failures; unsafe/invalid suggestion patterns; IP/data events; model/version changes.                               |
| QuackBot           | Escalation rate; unresolved/inaccurate answer rate; harmful/safety-relevant responses; customer complaints; prompt/RAG security events.                            |
| FeatherForecast    | Forecast error; drift; manual adjustment rate; shortage/excess inventory outcomes; data quality; availability.                                                     |
| WingInspect Vision | False-negative/false-positive performance; defect escape; human override; camera/data drift; model/version integrity.                                              |
| DuckTalent AI      | If ever approved: selection/ranking outcomes; fairness indicators; override/disagreement; complaints/contestability; model/data drift; human-review effectiveness. |
| PondGPT            | Sensitive-data events; access-control failures; retrieval leakage; unsafe-code incidents; prompt/RAG abuse; user complaints; model/service change.                 |

### Stop / escalate when

- A safety-, rights- or confidentiality-relevant threshold is breached and impact is not bounded.

- Monitoring data cannot be trusted or the system version/configuration cannot be tied to results.

- Repeated human overrides or complaints suggest the AI is no longer fit for intended purpose.

### Minimum evidence pack

- Monitoring plan

- Baseline/version record

- Metric results

- Threshold breaches/investigations

- Override/complaint records

- Vendor/model change notices

- Corrective action / reassessment decisions

## PB-11 — Material Change & Reassessment

| **Field**        | **Operational instruction**                                                                                                                                                                                                                                |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Trigger          | A change occurs or is proposed to intended purpose, autonomy, model/provider/version, training/reference data, affected persons, users, geography, integrations, permissions, vendor/subprocessor, legal context, control design or operating environment. |
| Lead             | Eleanor Duckford - AI Governance Lead                                                                                                                                                                                                                      |
| Support          | Business/Technical Owner; Risk; Legal/Privacy/Security/HR/Product Safety/Procurement as triggered                                                                                                                                                          |
| Required outcome | Prior approval is either confirmed as still valid or replaced with an updated assessment, controls and release decision before materially changed use proceeds.                                                                                            |

| **Step** | **Action**                       | **What to do**                                                                                                                                    | **Primary owner**               | **Evidence / output**                   |
|----------|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|-----------------------------------------|
| 1        | Log the change                   | Record proposed/observed change, date, initiator, systems/AI IDs and why it may be material.                                                      | Technical Owner / AI Governance | Change record                           |
| 2        | Compare with approved baseline   | Identify which purpose, risk, data, people, model, vendor, integration, geography, autonomy, controls or evidence assumptions differ.             | AI Governance + Owner           | Baseline comparison                     |
| 3        | Classify materiality             | If change can alter rights/safety impact, legal role, risk, performance, security, data use or human oversight, treat as material until assessed. | Risk + AI Governance            | Materiality decision                    |
| 4        | Freeze unapproved expansion      | Do not move the material change into production solely because the previous version/use was approved.                                             | Business/Technical Owner        | Change hold / controlled pilot boundary |
| 5        | Re-run affected assessments      | Repeat PB-02 and any specialist playbooks only to the depth needed for changed facts; do not duplicate unchanged evidence.                        | AI Governance + SMEs            | Updated assessment pack                 |
| 6        | Refresh vendor/contract evidence | For third parties, determine whether notification, due diligence or contract remedies/approval are triggered.                                     | Procurement + Legal             | Vendor change review                    |
| 7        | Update monitoring / fallback     | Revise baseline, thresholds, runbooks and rollback process for the changed configuration.                                                         | Technical + Business Owner      | Updated operating plan                  |
| 8        | Reapprove                        | Use PB-08 to record the new lifecycle gate and conditions.                                                                                        | Authorized approver             | Reapproval record                       |

| **CRITICAL ASSUMPTION RULE.** If a critical assumption becomes false, materially changes, or cannot be validated, update the inventory and trigger the relevant impact, risk, legal and approval reviews. Examples include human decision authority, PondGPT access boundaries, safety-function use, vendor/model data use and deployment geography. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Stop / escalate when

- A material vendor/model change occurred without enough information to assess impact.

- Human review is being reduced or autonomy increased without reassessment.

- New data categories or affected populations are added without privacy/impact review.

- A changed system is operating under an approval decision that refers to a materially different version or intended purpose.

### Minimum evidence pack

- Change request/notification

- Baseline comparison

- Materiality decision

- Updated risk/impact/legal/vendor/security records

- Updated validation/monitoring

- Reapproval decision

- Version/configuration traceability

## PB-12 — Suspension, Exit & Retirement

| **Field**        | **Operational instruction**                                                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Trigger          | Risk is outside tolerance; incident or control failure requires pause; vendor/service is terminated; business value no longer justifies exposure; system is replaced; legal/operating conditions change; or planned end-of-life is reached. |
| Lead             | Business Owner + Technical Owner                                                                                                                                                                                                            |
| Support          | AI Governance; Security; Privacy; Procurement; Legal; Records; Domain SME                                                                                                                                                                   |
| Required outcome | AI reliance stops safely, data/access/integrations are handled, vendor obligations are closed, affected processes transition, and evidence/inventory records preserve the lifecycle history.                                                |

| **Step** | **Action**                   | **What to do**                                                                                                                            | **Primary owner**              | **Evidence / output**                |
|----------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------------|
| 1        | Choose action                | Distinguish temporary restriction/suspension from permanent retirement/termination and document why.                                      | Business Owner + AI Governance | Suspension/retirement decision       |
| 2        | Move to safe operating state | Disable affected automation, integrations, model endpoint or user access; activate manual/replacement fallback.                           | Technical Owner                | Change/disable evidence              |
| 3        | Protect affected decisions   | Identify pending or recent outputs that require review, reprocessing, customer/candidate communication or product action.                 | Business Owner                 | Decision remediation record          |
| 4        | Handle vendor exit           | Export agreed data/artifacts/logs; revoke vendor access/API keys; disable connectors; invoke deletion/return and portability obligations. | Procurement + Technical Owner  | Exit checklist / vendor attestations |
| 5        | Handle data and records      | Apply approved retention, legal hold, deletion and evidence-preservation requirements. Do not invent retention periods in the playbook.   | Privacy/Legal/Records          | Retention/deletion record            |
| 6        | Close security credentials   | Revoke service accounts, secrets, tokens, keys, SSO assignments and privileged roles.                                                     | Security / IT                  | Access revocation evidence           |
| 7        | Update inventory             | Set lifecycle to Suspended/Retired/Terminated; record final version, date, reason and successor/fallback if any.                          | AI Governance Lead             | QuackTrack update                    |
| 8        | Close residual actions       | Resolve incidents, vendor claims, open remediation or formally transfer actions to successor system/program.                              | Risk + Owner                   | Closure record                       |
| 9        | Preserve assurance trail     | Archive approval, monitoring, incidents, risk acceptance and retirement evidence according to applicable records rules.                   | AI Governance + Control Owners | Final evidence pack                  |

### Stop / escalate when

- The system is retired technically but accounts, integrations, vendor data or access remain active without an approved reason.

- A safety-/rights-relevant process is shut down without a validated fallback.

- Evidence required for incident, legal, audit or contractual purposes would be destroyed by routine deletion.

### Minimum evidence pack

- Suspension/retirement approval

- Disable/access-revocation evidence

- Fallback/transition plan

- Vendor export/deletion attestations

- Final inventory status

- Open-risk closure

- Final evidence archive index

## PB-13 — Evidence & Assurance Readiness

| **Field**        | **Operational instruction**                                                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Trigger          | A material governance decision, control claim, release gate, monitoring cycle, incident or audit/assurance preparation requires proof that controls were designed and operated. |
| Lead             | Eleanor Duckford - AI Governance Lead + Control Owners                                                                                                                          |
| Support          | Risk; Security; Privacy; Technology; Business Owners; Procurement; Internal Audit as independent observer                                                                       |
| Required outcome | A traceable evidence chain links AI ID -\> purpose -\> impact/risk -\> controls -\> approval -\> monitoring/incidents/changes -\> current lifecycle state.                      |

| **Step** | **Action**                        | **What to do**                                                                                                                                     | **Primary owner**             | **Evidence / output**          |
|----------|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|--------------------------------|
| 1        | Define evidence requirement       | For each material control, specify what evidence proves design and what evidence proves operation.                                                 | Control Owner + AI Governance | Evidence requirement           |
| 2        | Use stable identifiers            | Use AI ID, risk/control/action IDs, model/version and date/time so evidence can be traced across artifacts.                                        | AI Governance Lead            | Cross-reference convention     |
| 3        | Capture source evidence           | Prefer system-generated logs, signed approvals, test results, tickets, reports, vendor artifacts and controlled records over narrative assertions. | Control Owner                 | Primary evidence               |
| 4        | Assess evidence confidence        | Rate whether evidence is current, complete, attributable, repeatable and relevant to the assessed control.                                         | Risk / Second line            | Evidence-confidence assessment |
| 5        | Separate planned from implemented | Planned controls remain action items and do not support current control effectiveness until operating evidence exists.                             | Risk + Owner                  | Updated control status         |
| 6        | Maintain decision traceability    | Approval records should state the evidence considered, unresolved assumptions, conditions, risk accepted and next review trigger/date.             | Approver / AI Governance      | Decision record                |
| 7        | Refresh evidence                  | Update evidence after material change, incident, control modification, vendor/model change or scheduled review.                                    | Control Owners                | Refreshed evidence             |
| 8        | Prepare assurance view            | Provide Internal Audit with read-only evidence and clear ownership without transferring control responsibility to audit.                           | AI Governance Lead            | Evidence index / audit pack    |

| **Evidence domain**   | **Examples**                                                                       | **Weak evidence warning**                                                    |
|-----------------------|------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| Inventory / ownership | QuackTrack record; owner acceptance; lifecycle state.                              | Owner name copied into a document with no accountability/approval record.    |
| Risk / impact         | Scenario register; AIA/DPIA where relevant; risk scores; treatment actions.        | Generic "bias/security risk" statements with no scenario, owner or evidence. |
| Technical validation  | Test protocol/results; model/version; data/sample description; limitations.        | Accuracy claim with no version, dataset context or test result.              |
| Security              | Threat model; access review; test results; log configuration; remediation tickets. | Policy statement alone proves technical control operation.                   |
| Human oversight       | Role matrix; override tests; decision/override logs; training evidence.            | "Human in the loop" with no authority, time, competence or evidence.         |
| Third party           | Due diligence; contract; DPA; vendor evidence; change notices; exit tests.         | Marketing/security page without scope or current validity.                   |
| Monitoring / incident | Metric records; threshold investigations; incident/RCA; restart decision.          | Dashboard screenshot disconnected from version, threshold or owner.          |

### Stop / escalate when

- A control is represented as effective solely because a procedure says it should exist.

- Evidence cannot be tied to the current model/version/configuration or use case.

- High/Critical residual-risk reduction depends on weak, stale or unverified evidence.

- Internal Audit is asked to design or operate the control it will later assure.

### Minimum evidence pack

- Evidence index

- Control-to-evidence mapping

- Approval records

- Current test/validation evidence

- Monitoring and incident records

- Vendor/change evidence

- Action closure evidence

- Assurance handoff record

## 3. System-Specific Quick Action Cards

| **HOW TO READ THESE CARDS.** They do not replace risk or legal assessment. They summarize the current fictional portfolio state and identify the playbooks that should be activated first based on existing Duckworks evidence. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### AI-001 DuckDesign AI

| **Current gate**      | **Context**                                                                                          | **Priority playbooks**                   | **Immediate decision rule**                                                                                                |
|-----------------------|------------------------------------------------------------------------------------------------------|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Restricted pilot only | Generative engineering design assistance; highly confidential CAD/IP; third-party component assumed. | PB-04, PB-06, PB-07, PB-08, PB-10, PB-11 | Do not permit autonomous production design release. Require competent engineer review, validation and IP/data protections. |

### AI-002 QuackBot

| **Current gate**                 | **Context**                                                                          | **Priority playbooks**                   | **Immediate decision rule**                                                                                                   |
|----------------------------------|--------------------------------------------------------------------------------------|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Production blocked pending gates | Customer-facing GenAI/RAG; customer queries and support knowledge; third-party SaaS. | PB-04, PB-06, PB-07, PB-08, PB-09, PB-10 | Block production until prompt/RAG security, escalation, content boundaries, monitoring and customer safeguards are evidenced. |

### AI-003 FeatherForecast

| **Current gate**         | **Context**                                                                   | **Priority playbooks**     | **Immediate decision rule**                                                                        |
|--------------------------|-------------------------------------------------------------------------------|----------------------------|----------------------------------------------------------------------------------------------------|
| Continue with monitoring | Internal predictive ML for demand/inventory; operational/financial decisions. | PB-07, PB-10, PB-11, PB-13 | Managers retain approval for material commitments; monitor forecast error, drift and data quality. |

### AI-004 WingInspect Vision

| **Current gate**      | **Context**                                                                             | **Priority playbooks**                   | **Immediate decision rule**                                                                            |
|-----------------------|-----------------------------------------------------------------------------------------|------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Restricted pilot only | Computer vision for defect detection; product quality/safety relevance; internal model. | PB-03, PB-06, PB-07, PB-08, PB-09, PB-10 | Human inspector remains final authority; validate false-negative risk before safety-critical reliance. |

### AI-005 DuckTalent AI

| **Current gate**               | **Context**                                                                                                   | **Priority playbooks**                                 | **Immediate decision rule**                                                                                                                             |
|--------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Do not deploy in current state | Recruitment screening/ranking; applicant personal data; provider/model TBD; internal risk currently Critical. | PB-02, PB-03, PB-04, PB-06, PB-07, PB-08, PB-10, PB-13 | No real-applicant deployment until legal/privacy/fairness/human-oversight/vendor/validation evidence closes blocking gaps and Critical risk is treated. |

### AI-006 PondGPT

| **Current gate**      | **Context**                                                                                           | **Priority playbooks**                   | **Immediate decision rule**                                                                                                                |
|-----------------------|-------------------------------------------------------------------------------------------------------|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Restricted pilot only | Enterprise GenAI/RAG/code assistant; mixed internal/personal/confidential data; third-party provider. | PB-04, PB-06, PB-07, PB-08, PB-09, PB-10 | Validate enterprise access boundaries, repository exclusions, logging and prompt/RAG security; prevent cross-user privilege amplification. |

### AI-007 Unregistered GenAI Usage

| **Current gate**      | **Context**                                                                                                         | **Priority playbooks**                                | **Immediate decision rule**                                                                                               |
|-----------------------|---------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Immediate containment | Multiple unknown public AI services, browser extensions and individual uses; data/vendors/geography may be unknown. | PB-05 first; then PB-01, PB-02, PB-04/PB-09 as needed | Contain sensitive uploads, investigate exposure, decompose into material use cases, register, assess and approve or stop. |

## 4. Legal, Framework, Practice and Assumption Classification

| **Category**                                  | **Source / basis**                                                                                                                                 | **How this pack uses it**                                                                                                                         | **Boundary**                                                                                                       |
|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Mandatory legal requirement - conditional     | EU Artificial Intelligence Act (Regulation (EU) 2024/1689, current consolidated text identified in Duckworks reference file)                       | Routes systems for legal role/classification, high-risk/prohibited/transparency and other applicable obligations.                                 | Applicability depends on facts, role, jurisdiction and dates. Playbooks do not create or replace statutory duties. |
| Mandatory legal requirement - conditional     | GDPR (Regulation (EU) 2016/679)                                                                                                                    | Routes personal-data AI to privacy review, DPIA determination, processor/vendor requirements, rights/security/incident analysis where applicable. | Controller/processor roles, lawful basis, DPIA and other duties require factual/legal determination.               |
| Mandatory legal requirement - conditional     | Employment/equality, product-safety, machinery, cybersecurity and other EU/national law listed in project reference file                           | Triggers HR, Product Safety, Legal, Security and other specialist review.                                                                         | National implementing law and product/sector facts must be assessed separately.                                    |
| Voluntary framework guidance                  | NIST AI RMF 1.0 and NIST GenAI Profile                                                                                                             | Supports Govern/Map/Measure/Manage thinking, lifecycle risk, monitoring and GenAI risk treatment.                                                 | Voluntary guidance; not proof of legal compliance.                                                                 |
| Voluntary standards / guidance                | ISO/IEC 42001, ISO/IEC 23894, ISO/IEC 42005, ISO/IEC 27001 public descriptions                                                                     | Supports management-system governance, risk, impact, security, lifecycle evidence and continual improvement concepts.                             | Pack does not reproduce ISO clauses or claim certification/conformity.                                             |
| Recognized cybersecurity guidance             | ENISA AI cybersecurity guidance; MITRE ATLAS; OWASP GenAI Security Project                                                                         | Supports threat modelling and AI-specific security review.                                                                                        | Good-practice/technical references, not universal legal requirements.                                              |
| Duckworks recommended organizational practice | Project W.I.N.G. governance baseline, risk methodology, acceptance criteria, vendor contract, responsible-use policy and this pack                 | Defines intake gates, evidence rules, enhanced review, incident/change response, human oversight, vendor and monitoring practices.                | Internal control choices; may be refined through governance approval.                                              |
| Project assumptions                           | EU/EEA focus; mixed internal/third-party AI; humans retain formal accountability for consequential decisions; portfolio uses synthetic/public data | Shapes examples and priority gates.                                                                                                               | Critical assumptions must be validated per system; if false, invoke PB-11.                                         |

### 4.1 Framework orientation - high level only

| **Playbook cluster**          | **NIST AI RMF orientation**                           | **ISO/public-standard orientation**                                          |
|-------------------------------|-------------------------------------------------------|------------------------------------------------------------------------------|
| PB-01 / PB-02                 | GOVERN + MAP; MEASURE/MANAGE as assessment progresses | AI management-system context, roles, lifecycle risk and impact concepts.     |
| PB-03 / PB-07 / PB-08         | GOVERN + MAP + MEASURE + MANAGE                       | Impact assessment, human oversight, validation and controlled deployment.    |
| PB-04 / PB-06                 | GOVERN + MAP + MANAGE                                 | Supplier/security governance, technical risk and lifecycle controls.         |
| PB-09 / PB-10 / PB-11 / PB-12 | MEASURE + MANAGE with GOVERN oversight                | Monitoring, incident response, change, continual improvement and retirement. |
| PB-13                         | GOVERN across the lifecycle                           | Documented information, evidence, accountability and assurance readiness.    |

## Appendix A - Playbook Execution Record Template

| **Field**                     | **Record**                                                    |
|-------------------------------|---------------------------------------------------------------|
| Playbook ID / version         | \[PB-\_\_ / v\_\_\]                                           |
| AI ID / system                | \[AI-\_\_\_ / name\]                                          |
| Trigger date/time             | \[Insert\]                                                    |
| Trigger description           | \[Insert\]                                                    |
| Business owner                | \[Insert\]                                                    |
| Technical owner               | \[Insert\]                                                    |
| Playbook lead                 | \[Insert\]                                                    |
| Specialist reviewers          | \[Insert\]                                                    |
| Current lifecycle gate        | \[Insert\]                                                    |
| Current internal risk rating  | \[Insert - not legal classification\]                         |
| Legal/privacy flags           | \[Insert / N/A / pending legal confirmation\]                 |
| Actions taken                 | \[Insert\]                                                    |
| Evidence locations            | \[Links / repository IDs\]                                    |
| Open actions / owners / dates | \[Insert\]                                                    |
| Decision                      | \[Approve / condition / block / suspend / retire / escalate\] |
| Approver / committee          | \[Insert\]                                                    |
| Next review / trigger         | \[Insert\]                                                    |

## Appendix B - Minimum Evidence Naming Convention

| **Element**       | **Recommended format**        | **Example**                                      |
|-------------------|-------------------------------|--------------------------------------------------|
| AI identifier     | AI-###                        | AI-005                                           |
| Evidence date     | YYYY-MM-DD                    | 2026-08-09                                       |
| Artifact type     | Short controlled label        | SEC-TEST / AIA / DPIA / VEND-DD / APPROVAL / MON |
| Version/component | v# or model/config identifier | v1.0 / model-TBD                                 |
| Evidence file     | AIID_DATE_TYPE_DESCRIPTION    | AI-005_2026-08-09_AIA_DuckTalent.docx            |
| Action ID         | AIID-ACT-###                  | AI-005-ACT-014                                   |
| Incident ID       | AIID-INC-YYYY-###             | AI-002-INC-2026-001                              |

| **RECORDS RULE.** This naming convention is a recommended Duckworks practice. Retention periods, legal holds, deletion requirements and statutory records duties must be set through the applicable records, legal, privacy and contractual requirements rather than invented in this pack. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Appendix C - Source Register

**1.** Duckworks AI Governance Project - Business Scenario (Project W.I.N.G. governance problem, seven-system portfolio and desired operating principle).

**2.** Duckworks AI Governance Readiness Assessment - Executive Case Study (portfolio findings, risk priorities and recommended governance response).

**3.** Duckworks AI Governance Project - In-Scope and Out-of-Scope Items (intake, risk, human oversight, third-party, GenAI/shadow AI, security, monitoring, incident, evidence and assurance scope).

**4.** Duckworks Project Objectives (risk-based approval, third-party governance, monitoring, evidence, management reporting and assurance objectives).

**5.** Duckworks Project Stakeholder Register v1.0 (named first/second/third-line roles and escalation triggers).

**6.** Duckworks Project Assumptions Register v1.0 (critical assumptions and reassessment/change-control rule).

**7.** Duckworks Project Acceptance Criteria v1.0 (current system release/governance gates and auditability requirements).

**8.** Duckworks AI Risk Classification & Assessment Methodology v1.0 (5x5 scoring, risk thresholds, control credit, evidence confidence, treatment and reassessment triggers).

**9.** Duckworks AI Asset Inventory v1.0 (technology, provider, hosting, data categories, personal/confidential data and third-party dependency context).

**10.** Duckworks AI Vendor Contract Template v1.0 (third-party AI due diligence/contract, model/service change, incident cooperation and exit controls).

**11.** Duckworks AI Responsible Use Policy v1.0 (related policy/standard hierarchy and operating expectations).

**12.** Duckworks Public Frameworks, Legislation & Guidance reference file (official-source catalogue; last verified 9 August 2026).

### Public authoritative sources maintained by Duckworks

- EU Artificial Intelligence Act: https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng

- GDPR: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng

- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework

- NIST AI RMF Playbook: https://airc.nist.gov/airmf-resources/playbook/

- NIST Generative AI Profile: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf

- ISO/IEC 42001 public description: https://www.iso.org/standard/42001

- ISO/IEC 23894 public description: https://www.iso.org/standard/77304.html

- ISO/IEC 42005 public description: https://www.iso.org/standard/42005

- ISO/IEC 27001 public description: https://www.iso.org/standard/27001

- ENISA AI cybersecurity framework: https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai

- MITRE ATLAS: https://atlas.mitre.org/

- OWASP GenAI Security Project: https://genai.owasp.org/

| **PORTFOLIO DISCLAIMER.** Duckworks, Project W.I.N.G., all named personnel, AI systems, vendors, data, risks, incidents, decisions and evidence in this document are fictional and created solely for educational and professional portfolio purposes. This pack is not legal advice, certification evidence, a production incident-response procedure, or a determination that any particular law applies to a real organization. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
