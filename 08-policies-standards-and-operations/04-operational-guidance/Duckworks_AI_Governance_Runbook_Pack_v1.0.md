# Duckworks AI Governance Runbook Pack

**DUCKWORKS**

**AI Governance Runbook Pack**

Executable response procedures for AI operations, incidents, change, safety, rights, vendors and evidence

| **Document control** | **Value**                                                                                |
|----------------------|------------------------------------------------------------------------------------------|
| Document ID          | DW-WING-RB-01                                                                            |
| Version              | 1.0                                                                                      |
| Status               | Portfolio Baseline - Draft for simulated approval                                        |
| Organization         | Duckworks (fictional)                                                                    |
| Document owner       | Eleanor Duckford - AI Governance Lead                                                    |
| Governance sponsor   | Reginald Duckman - Chief Risk & Compliance Officer                                       |
| Primary reviewers    | CISO; General Counsel; DPO; Head of Data & AI; HR; Procurement; Product Safety & Quality |
| Classification       | Portfolio / Synthetic / Non-production                                                   |
| Prepared             | 9 August 2026                                                                            |

| **OPERATING PRINCIPLE.** No material AI without an owner, no owner without accountability, no material risk without treatment, and no control without evidence. |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **PORTFOLIO BOUNDARY.** Duckworks, Project W.I.N.G., all personnel, AI systems, datasets, decisions, incidents and evidence in this pack are fictional. The runbooks demonstrate governance practice and are not legal advice, certification evidence, or production technical procedures. |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## **1. How to Use This Runbook Pack**

A runbook is the task-level execution layer beneath Duckworks policies, standards and operational playbooks. The playbook answers how Duckworks should handle a governance scenario; the runbook identifies the sequence of actions, responsible roles, evidence, decision points and stop conditions when a specific event occurs.

These runbooks are deliberately technology-neutral. Vendor-specific console clicks, CLI commands, API calls, SIEM queries, model rollback commands and infrastructure actions must be maintained in controlled local technical procedures. This avoids pretending that a generic governance document can safely substitute for implementation-specific operating knowledge.

| **IMPORTANT DISTINCTION.** Incident priority, Duckworks enterprise risk rating, and legal/regulatory classification are separate concepts. A P1 incident does not automatically make an AI system legally high-risk, and a Duckworks Critical risk rating is not a statutory classification. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### **1.1 Runbook selection matrix**

| **ID** | **Runbook**                                      | **Use when...**                                                                                       | **Primary lead**                     |
|--------|--------------------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------|
| RB-01  | Production Release / Deployment Gate             | A pilot or changed AI system is proposed for production or broader use.                               | AI Governance Lead + System Owner    |
| RB-02  | AI Incident Triage & Containment                 | Harmful behavior, control failure, compromise, data exposure or material AI incident is reported.     | CISO / AI Governance                 |
| RB-03  | Prompt Injection / RAG Compromise                | A GenAI/RAG system may be manipulated through prompts, retrieved content or tool use.                 | CISO / Security                      |
| RB-04  | Sensitive Data Leakage / Unauthorized Disclosure | AI may have exposed confidential, personal or restricted information.                                 | CISO + DPO                           |
| RB-05  | Shadow AI Discovery & Containment                | Unapproved public AI, extension, assistant, API or AI-enabled SaaS use is found.                      | CISO + AI Governance                 |
| RB-06  | Model Drift / Performance Degradation            | Performance, error distribution or operating assumptions materially deteriorate.                      | Head of Data & AI                    |
| RB-07  | Harmful / Incorrect Output                       | AI generates materially wrong, unsafe, misleading or policy-violating content.                        | Business Owner                       |
| RB-08  | Fairness / Discrimination Alert                  | A people-impacting AI system shows potential unequal treatment or discriminatory effect.              | HR + Legal + AI Governance           |
| RB-09  | Human Oversight Failure / Automation Bias        | Human review becomes ineffective, bypassed, rubber-stamped or unavailable.                            | Business Owner + AI Governance       |
| RB-10  | Product Safety / Quality AI Failure              | AI-assisted design or inspection may contribute to unsafe or defective product outcomes.              | Product Safety & Quality             |
| RB-11  | Third-Party AI Vendor Event                      | Vendor outage, incident, subprocessor/model change, material term change or degraded evidence occurs. | Procurement & Vendor Assurance       |
| RB-12  | Material Model / Data / Integration Change       | Purpose, model, data, provider, affected population, integration or autonomy changes materially.      | AI Governance Lead + Technical Owner |
| RB-13  | AI Access / Permission Misconfiguration          | AI can reach data, tools or actions beyond authorized user/system boundaries.                         | CISO + IT/Cloud                      |
| RB-14  | Emergency Suspension / Safe Fallback             | Immediate stopping, isolation, rollback or manual fallback is required.                               | System Owner + CISO                  |
| RB-15  | AI Retirement / Vendor Exit                      | System or service is decommissioned, replaced, contract terminated or abandoned.                      | System Owner + Procurement           |
| RB-16  | Evidence Preservation / Assurance Response       | Audit, legal review, investigation or governance challenge requires defensible evidence.              | AI Governance Lead                   |

### **1.2 Incident priority routing**

| **Priority**     | **Trigger examples**                                                                                                                                                       | **Initial response expectation**                                                  | **Governance route**                                    |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|---------------------------------------------------------|
| P1 - Emergency   | Potential serious physical harm; uncontrolled sensitive-data exposure; active compromise; discriminatory production outcome; loss of control over consequential decisions. | Immediate containment/suspension; notify required specialists; preserve evidence. | RB-02 + RB-14, then specialist runbook.                 |
| P2 - Major       | Material service/model failure; significant customer/employee impact; vendor incident; major control failure; severe performance degradation.                              | Prompt owner/security triage; restrict scope; initiate corrective action.         | RB-02 or relevant specialist runbook.                   |
| P3 - Significant | Localized harmful output; recurring monitoring breach; control evidence gap; non-critical vendor change.                                                                   | Record, investigate, remediate and reassess within normal governance cadence.     | Relevant specialist runbook + RB-12 if material change. |
| P4 - Routine     | Minor anomaly or low-impact deviation with no material harm and functioning controls.                                                                                      | Record and trend; resolve through normal operations.                              | Monitoring process; escalate if pattern develops.       |

### **1.3 Baseline system governance gates**

The current simulated governance gates below are inherited from the Duckworks acceptance criteria. A runbook does not silently override them; changes require a documented governance decision.

| **System**               | **Current gate**                 | **Key runbook implications**                                                                                                                          |
|--------------------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| DuckDesign AI            | Restricted pilot only            | RB-01 cannot approve production without competent engineer review, validation and IP/data controls. RB-10 applies to safety-relevant failure.         |
| QuackBot                 | Production blocked pending gates | RB-03, RB-07 and RB-01 are primary. Prompt/RAG security, escalation, content boundaries and monitoring remain release conditions.                     |
| FeatherForecast          | Continue with monitoring         | RB-06 and RB-12 are primary; manager approval remains required for material commitments.                                                              |
| WingInspect Vision       | Restricted pilot only            | RB-10 and RB-09 are primary; human inspector remains final authority and false-negative validation is essential.                                      |
| DuckTalent AI            | Do not deploy in current state   | RB-08 and RB-09 cannot be used to imply deployment approval. Enhanced legal/privacy/fairness analysis remains blocking.                               |
| PondGPT                  | Restricted pilot only            | RB-03, RB-04 and RB-13 are primary; enterprise access enforcement, sensitive-repository exclusions, logging and acceptable-use controls remain gates. |
| Unregistered GenAI Usage | Immediate containment            | RB-05 is the primary route; discovered material uses must be decomposed into individual inventory records.                                            |

## **2. Roles and Command Model**

| **Role**                                                     | **Command responsibility**                                                                                                        |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| AI Governance Lead - Eleanor Duckford                        | Maintains QuackTrack; initiates governance route; coordinates assessment, evidence and committee decisions.                       |
| CRCO - Reginald Duckman                                      | Governance sponsor; chairs AI Governance Committee; escalates risk acceptance and policy exceptions.                              |
| CISO - Cassandra Duckley                                     | Leads AI security triage, containment, threat assessment and security acceptance.                                                 |
| Head of Data & AI - Dr. Ada Duckfield                        | Leads model/service validation, performance analysis, monitoring design, rollback evidence and technical change review.           |
| General Counsel - Amelia Duckett                             | Determines legal review needs, contract/legal escalation and regulatory-role analysis.                                            |
| DPO - Delia Duckham                                          | Advises on personal-data incidents, DPIA implications and privacy safeguards.                                                     |
| Chief People Officer - Beatrice Van Duck                     | Owns workforce-domain impacts and DuckTalent business outcomes.                                                                   |
| Director Product Safety & Quality - Quentin Duckwell         | Leads safety/quality escalation and release challenge for product-impacting AI.                                                   |
| Director Procurement & Vendor Assurance - Percival Duckworth | Leads supplier notification, contract rights, vendor evidence, renewal and exit coordination.                                     |
| System Business Owner                                        | Owns intended purpose, business consequences, operational controls, safe fallback and business restart decision within authority. |
| Technical Owner                                              | Executes technical isolation, configuration, rollback, validation, monitoring and restoration actions.                            |
| Internal Audit - Penelope Duckins                            | May observe and later assure; does not operate incident, release, risk, or control activities.                                    |

### **2.1 Universal evidence rules**

- Use the unique AI system ID in every incident, change, assessment, approval and evidence record.

- Time-stamp material actions and preserve who performed them, what was changed, and why.

- Do not claim a control operated unless supporting evidence exists; planned controls receive no implementation credit.

- Preserve original logs, model/service version identifiers, prompts/outputs where lawful and appropriate, configuration snapshots, vendor notices and decision records.

- Separate factual evidence from assumptions, hypotheses and conclusions. Mark unresolved facts as open assumptions.

- Record who authorized restart, release, risk acceptance or closure; absence of a decision record is itself an evidence gap.

## **RB-01 — Production Release / Deployment Gate**

| **PURPOSE.** Provide an executable gate for moving an AI system from concept, assessment or restricted pilot into production or broader operational use without bypassing required risk, impact, security, privacy, vendor, human-oversight and monitoring decisions. |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Field**         | **Runbook position**                                                                                                                                              |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primary trigger   | A system owner requests production deployment, wider user access, external exposure, higher autonomy, product integration, or re-release after a material change. |
| Primary lead      | AI Governance Lead + Business Owner                                                                                                                               |
| Mandatory support | Technical Owner; CISO; Legal; DPO; relevant domain SME; Procurement where third-party; AI Governance Committee for High/Critical matters                          |
| Primary systems   | All governed AI; especially DuckDesign, QuackBot, WingInspect, DuckTalent and PondGPT                                                                             |
| Related playbooks | PB-02, PB-03, PB-04, PB-06, PB-07, PB-08, PB-13                                                                                                                   |
| Target response   | A recorded Approve / Approve with Conditions / Block / Return to Pilot / Retire decision tied to current evidence.                                                |

### **A. Entry conditions and immediate guardrails**

- A valid QuackTrack inventory record exists and intended purpose, users, affected persons, data, integrations, provider/model and human decision boundary are sufficiently defined.

- Required risk and impact assessments are current for the proposed deployment configuration.

- Open assumptions that could change legal classification, safety, affected persons or degree of automation are visible and assigned.

- The system owner has identified safe fallback, monitoring thresholds and accountable operations support.

| **DO NOT.** Treat target residual risk, planned controls, vendor marketing statements or an incomplete pilot as evidence of production readiness. |
|---------------------------------------------------------------------------------------------------------------------------------------------------|

### **B. Executable procedure**

| **\#** | **Action**                                                                                                                                                          | **Owner**                            | **Required evidence / record**                             | **Decision / hand-off**                                                             |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|------------------------------------------------------------|-------------------------------------------------------------------------------------|
| 1      | Confirm the exact release scope: version, provider/model, environment, users, geography, data sources, integrations, permissions, autonomy and affected population. | AI Governance Lead + Technical Owner | Release scope record / configuration baseline              | If scope differs materially from the assessed configuration, stop and invoke RB-12. |
| 2      | Verify current lifecycle gate and prior committee/owner restrictions.                                                                                               | AI Governance Lead                   | QuackTrack record; prior approval minutes                  | Existing Block / Do Not Deploy status remains effective until formally changed.     |
| 3      | Check assessment currency and confirm all blocking treatment actions are closed with evidence.                                                                      | Risk & Compliance + System Owner     | Risk/AIA action tracker; evidence links                    | Unverified critical controls remain blocking.                                       |
| 4      | Obtain specialist sign-off required by the use case: security, privacy, legal, HR, product safety/quality and vendor assurance as applicable.                       | AI Governance Lead                   | Signed review checklist / comments resolved                | Any mandatory specialist “not ready” decision sends the release back for treatment. |
| 5      | Verify human oversight design, named reviewers, competence, override authority, escalation and stop mechanism.                                                      | Business Owner                       | Human oversight procedure; training/authorization evidence | If meaningful review cannot operate, block release for consequential use.           |
| 6      | Verify technical validation against declared acceptance thresholds and known failure modes.                                                                         | Technical Owner / Head of Data & AI  | Validation report; test dataset/version; results           | Failed threshold or unexplained degradation blocks release.                         |
| 7      | Confirm production monitoring, alert ownership, evidence retention and reassessment triggers are configured.                                                        | Technical Owner + AI Governance      | Monitoring plan; alert routing; evidence schedule          | No unowned monitoring alert or undefined review cadence for material AI.            |
| 8      | Present the release pack to the correct approval authority based on current residual risk and internal delegation.                                                  | AI Governance Lead                   | Approval pack; risk rating; conditions                     | High/Critical matters use committee/executive escalation defined by methodology.    |
| 9      | Record decision, conditions, expiry/review date and any restricted-use boundary in QuackTrack.                                                                      | AI Governance Lead                   | Approval record; inventory update                          | No production activation before decision is recorded.                               |
| 10     | Authorize technical release and verify post-deployment smoke checks, logs and fallback readiness.                                                                   | Technical Owner + Business Owner     | Deployment record; smoke-test evidence                     | Unexpected behavior invokes RB-02 or RB-14.                                         |

### **C. Escalation and stop criteria**

- Critical current residual risk; unresolved potential unlawful/prohibited use; or request to bypass required human authority.

- Material safety, rights, privacy, or security evidence is missing or contradicted by test results.

- Vendor/model/version is not the same as the assessed dependency and the change could alter risk.

- No tested suspension, rollback or safe fallback exists where failure could cause serious harm.

### **D. Exit criteria**

- Formal release decision is recorded by authorized approver.

- All conditions have owners and due dates; blocking conditions are closed before activation.

- Monitoring and incident routes are active and assigned.

- QuackTrack reflects the released configuration and next review date.

### **E. Minimum evidence package**

- Release scope/configuration baseline

- Current risk and impact assessments

- Specialist sign-offs

- Validation results

- Human oversight evidence

- Monitoring/alert configuration

- Approval decision and conditions

- Deployment/smoke-test record

### **F. Duckworks system-specific notes**

**DuckTalent AI —** Current gate remains Do Not Deploy. This runbook can assemble a readiness pack but cannot convert that gate to approval without the required enhanced legal/privacy/fairness work and governance decision.

**QuackBot —** Production remains blocked pending prompt/RAG security testing, safe escalation, content boundaries, monitoring and customer-impact safeguards.

**FeatherForecast —** Proportionate release can continue where manager approval for material commitments, drift monitoring and data-quality controls remain effective.

| **TABLETOP PROMPT.** A business owner asks to move QuackBot from restricted testing to public customer use after a vendor model upgrade. What evidence proves the exact upgraded model was assessed, the RAG attack surface tested, and the release authority documented? |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## **RB-02 — AI Incident Triage & Containment**

| **PURPOSE.** Create a single, auditable first-response route for suspected AI incidents before specialized investigation, legal/privacy analysis, vendor action or system restart. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Field**         | **Runbook position**                                                                                                                                                                              |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primary trigger   | Any report of harmful AI output, security compromise, material data exposure, discriminatory outcome, unsafe decision, model failure, loss of oversight, vendor incident or unexplained behavior. |
| Primary lead      | CISO for security-led incidents; AI Governance Lead coordinates governance record                                                                                                                 |
| Mandatory support | Business Owner; Technical Owner; Legal; DPO; HR/Product Safety/Procurement as applicable                                                                                                          |
| Primary systems   | All AI systems and discovered shadow AI                                                                                                                                                           |
| Related playbooks | PB-09, PB-13; specialist PBs as applicable                                                                                                                                                        |
| Target response   | Incident prioritized, contained, assigned, evidenced, routed to specialist runbooks and closed only after a documented restart/closure decision.                                                  |

### **A. Entry conditions and immediate guardrails**

- Create a unique incident record linked to the affected AI system ID or temporary discovery ID.

- Treat the first report as unverified until facts are established; preserve the original observation.

- Use P1-P4 incident priority independently from Duckworks enterprise risk rating.

| **DO NOT.** Spend the first response window debating root cause while harmful processing continues. Containment and evidence preservation take priority over premature attribution. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### **B. Executable procedure**

| **\#** | **Action**                                                                                                                                                                      | **Owner**                             | **Required evidence / record**  | **Decision / hand-off**                                                                            |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|---------------------------------|----------------------------------------------------------------------------------------------------|
| 1      | Record reporter, timestamp, affected system, environment, observed behavior, affected users/data and immediate business impact.                                                 | Service Desk / AI Governance          | Incident ticket / intake record | If system identity is unknown, create temporary ID and invoke RB-05 if shadow AI.                  |
| 2      | Assign provisional P1-P4 incident priority using actual/credible impact and current exposure.                                                                                   | CISO + Business Owner                 | Priority rationale              | Potential serious harm or uncontrolled exposure = P1 pending contrary evidence.                    |
| 3      | Preserve volatile evidence: logs, prompts/outputs, model/service/version, configuration, retrieved content, user/session IDs, vendor notices and screenshots where appropriate. | Technical Owner / Security            | Evidence manifest               | Do not overwrite or “clean up” the environment before evidence capture unless required for safety. |
| 4      | Contain the affected capability proportionately: disable feature, revoke integration, restrict users, block external access, switch to manual fallback or suspend system.       | Technical Owner + Business Owner      | Containment record              | For P1 or uncontrolled harm, use RB-14.                                                            |
| 5      | Identify affected domains and notify mandatory specialists: privacy, legal, HR, product safety, procurement/vendor, customer operations.                                        | AI Governance Lead                    | Notification log                | Specialist notification is based on facts/credible exposure, not final root cause.                 |
| 6      | Determine whether data, people, product safety, security, contractual or legal obligations require separate incident processes.                                                 | Legal / DPO / CISO / Safety SME       | Specialist triage notes         | Use existing enterprise incident processes; this runbook does not replace statutory analysis.      |
| 7      | Select specialist runbook(s) for investigation and treatment.                                                                                                                   | AI Governance Lead                    | Runbook routing record          | Examples: RB-03 prompt injection, RB-08 fairness, RB-10 safety, RB-11 vendor.                      |
| 8      | Establish root cause, affected scope, control failures and whether prior risk/impact assumptions remain valid.                                                                  | Incident Lead + Technical Owner       | Investigation report            | Material invalidation invokes RB-12 and reassessment.                                              |
| 9      | Define corrective/preventive actions, owner, due date, validation test and residual risk impact.                                                                                | Business Owner + Risk                 | CAPA / treatment plan           | High/Critical unresolved risk follows governance escalation.                                       |
| 10     | Authorize restart or closure only after exit criteria and specialist approvals are satisfied.                                                                                   | Business Owner + appropriate approver | Restart/closure decision        | Restart after P1/P2 requires explicit documented authorization.                                    |

### **C. Escalation and stop criteria**

- Actual or credible serious physical harm, systemic rights harm, major confidential/personal-data exposure or active compromise.

- Incident affects multiple systems or shared AI dependency.

- Vendor cannot provide timely incident facts or preservation support.

- Root cause cannot be bounded and continued operation could worsen impact.

- Evidence indicates prior governance evidence or approvals were materially inaccurate.

### **D. Exit criteria**

- Harmful processing is contained or demonstrably bounded.

- Root cause and affected scope are sufficiently understood for a decision.

- Required specialist/legal/privacy/safety routes are complete or formally handed off.

- Corrective actions are assigned and reassessment completed where triggered.

- Restart/closure decision and evidence manifest are recorded.

### **E. Minimum evidence package**

- Incident intake/timeline

- Priority rationale

- Evidence manifest

- Containment actions

- Specialist notifications

- Root-cause analysis

- Affected-person/data/system scope

- Corrective action plan

- Reassessment/approval records

- Closure/restart decision

### **F. Duckworks system-specific notes**

**AI-007 Unregistered GenAI —** If the event began as discovery of an unapproved AI service, invoke RB-05 in parallel; if sensitive information may have been exposed, also invoke RB-04.

**WingInspect Vision —** Potential false negatives tied to released products or safety-relevant defects should route immediately to RB-10 and existing product-quality processes.

**DuckTalent AI —** A discriminatory outcome or applicant complaint routes to RB-08 and does not justify deploying the currently blocked system.

| **TABLETOP PROMPT.** A PondGPT user reports that another team’s confidential document appeared in an answer. What are the first five actions before anyone attempts to reproduce the issue? |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## **RB-03 — Prompt Injection / RAG Compromise**

| **PURPOSE.** Respond to suspected direct or indirect prompt injection, retrieval poisoning, malicious retrieved content, tool abuse, system-prompt disclosure or unauthorized action by a generative-AI application. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Field**         | **Runbook position**                                                                                                                                                                                        |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primary trigger   | Unexpected instruction following, suspicious retrieved content, abnormal tool execution, prompt/system leakage, data exfiltration behavior, or security test demonstrating exploitable prompt/RAG behavior. |
| Primary lead      | CISO / Security                                                                                                                                                                                             |
| Mandatory support | Technical Owner; Head of Data & AI; Business Owner; AI Governance; DPO/Legal if data or people are affected                                                                                                 |
| Primary systems   | QuackBot, PondGPT, DuckDesign AI and any GenAI/RAG system                                                                                                                                                   |
| Related playbooks | PB-06, PB-09, PB-10, PB-11                                                                                                                                                                                  |
| Target response   | Attack path contained, affected content/integration isolated, scope and exposure determined, controls corrected and retested before restart.                                                                |

### **A. Entry conditions and immediate guardrails**

- Capture the exact user input, retrieved content, tool call and output sequence when feasible and lawful.

- Identify whether the suspected manipulation is direct prompt input, indirect retrieved content, poisoned knowledge source, malicious tool response, or configuration weakness.

| **DO NOT.** Assume “the model ignored the prompt” proves security. The security objective is whether unauthorized disclosure, instruction priority failure, tool misuse or policy bypass was possible. |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### **B. Executable procedure**

| **\#** | **Action**                                                                                                                                                                                                            | **Owner**                      | **Required evidence / record**   | **Decision / hand-off**                                                                          |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------|
| 1      | Create/attach incident record and preserve prompt, retrieved chunks, system context, tool traces, model/service/version and session metadata.                                                                         | Security + Technical Owner     | Evidence bundle                  | If sensitive data was exposed, invoke RB-04.                                                     |
| 2      | Disable or isolate the affected retrieval source, tool, plugin, connector or public endpoint as appropriate.                                                                                                          | Technical Owner                | Containment/configuration record | If isolation is not reliable, invoke RB-14.                                                      |
| 3      | Determine whether the exploit can cross user/tenant/access boundaries or trigger privileged actions.                                                                                                                  | Security                       | Threat assessment                | Cross-boundary access or privileged action = P1/P2 escalation.                                   |
| 4      | Identify the malicious instruction source and propagation path through retrieval, prompt assembly, memory or tool chain.                                                                                              | Security + Data & AI           | Attack-path analysis             | If source integrity is compromised, quarantine the corpus/index and rebuild from trusted source. |
| 5      | Review authorization enforcement outside the model: identity, ACLs, tool permissions, API scopes and data filtering.                                                                                                  | CISO + IT/Cloud                | Access-control evidence          | Model prompting alone is not accepted as an authorization control.                               |
| 6      | Apply corrective controls appropriate to the architecture: source filtering, least privilege, tool allowlists, content segmentation, output controls, context isolation, retrieval integrity, validation or redesign. | Technical Owner                | Change record                    | Material architecture change invokes RB-12.                                                      |
| 7      | Retest using original exploit and variant attack cases; document pass/fail and residual limitations.                                                                                                                  | Security / Validation          | Security test report             | A single successful test is insufficient if the original attack class remains plausible.         |
| 8      | Assess whether monitoring can detect recurrence and add event patterns/alerts where feasible.                                                                                                                         | Security Operations            | Detection/monitoring update      | Unmonitored high-impact attack path remains an approval concern.                                 |
| 9      | Reassess risk and approve restricted restart only within validated scope.                                                                                                                                             | AI Governance + Business Owner | Reassessment / restart decision  | Use RB-01 for production gate if scope materially changed.                                       |

### **C. Escalation and stop criteria**

- Unauthorized access to restricted information or cross-user data.

- Tool execution could alter external systems, code, customer records or business transactions.

- Poisoned content exists in a trusted enterprise knowledge source.

- Attack remains reproducible after attempted remediation.

- Provider behavior or platform architecture prevents Duckworks from applying adequate controls.

### **D. Exit criteria**

- Attack path is contained and no uncontrolled malicious source remains active.

- Authorization boundaries are enforced outside model behavior.

- Corrective controls have repeatable test evidence.

- Monitoring and residual limitations are documented.

- Restart/release is explicitly approved.

### **E. Minimum evidence package**

- Prompt/retrieval/tool traces

- Affected source/index record

- Threat model update

- Access-control review

- Remediation changes

- Security test cases/results

- Monitoring rule/update

- Risk reassessment

- Restart approval

### **F. Duckworks system-specific notes**

**QuackBot —** Prioritize indirect prompt injection through product-support content, customer-provided text and knowledge retrieval. Customer-facing exposure increases the need for safe escalation and constrained tool use.

**PondGPT —** Prioritize cross-user retrieval authorization and privilege amplification. The project assumption is that users should not retrieve documents they could not otherwise access.

**DuckDesign AI —** Protect engineering IP and prevent untrusted external content from influencing design recommendations without validation.

| **TABLETOP PROMPT.** A QuackBot troubleshooting document contains hidden instructions telling the chatbot to reveal internal warranty rules and ignore escalation policy. How do you isolate the source and prove the control fix works? |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## **RB-04 — Sensitive Data Leakage / Unauthorized Disclosure**

| **PURPOSE.** Contain and investigate actual or suspected disclosure of confidential information, personal data, credentials, intellectual property or restricted content through an AI system or AI vendor. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Field**         | **Runbook position**                                                                                                                                                           |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primary trigger   | Sensitive data appears in AI input/output/logs, is sent to an unapproved provider, crosses access boundaries, or may have been retained/trained on contrary to approved terms. |
| Primary lead      | CISO + DPO for personal data                                                                                                                                                   |
| Mandatory support | Legal; AI Governance; Business Owner; Technical Owner; Procurement/Vendor Assurance                                                                                            |
| Primary systems   | PondGPT, QuackBot, DuckDesign AI, DuckTalent AI, shadow AI and any vendor-hosted AI                                                                                            |
| Related playbooks | PB-04, PB-05, PB-09                                                                                                                                                            |
| Target response   | Exposure bounded, further disclosure stopped, provider/data path understood, required privacy/legal/contract routes initiated, and control weakness corrected.                 |

### **A. Entry conditions and immediate guardrails**

- Identify data classification and whether the data is personal, confidential, credential material, engineering IP, customer information or other restricted content.

- Preserve evidence of what was submitted, exposed, retained or returned without unnecessarily replicating sensitive data.

| **DO NOT.** Upload the exposed data into additional AI tools to “analyze” the incident or copy it into uncontrolled collaboration channels. |
|---------------------------------------------------------------------------------------------------------------------------------------------|

### **B. Executable procedure**

| **\#** | **Action**                                                                                                                                                             | **Owner**                  | **Required evidence / record**       | **Decision / hand-off**                                                     |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|--------------------------------------|-----------------------------------------------------------------------------|
| 1      | Open incident and classify the information involved using Duckworks data classification.                                                                               | CISO / DPO                 | Incident record; data classification | Unknown sensitivity is treated conservatively until verified.               |
| 2      | Stop the data path: disable connector/upload feature, revoke token, restrict users, quarantine content or block vendor access as appropriate.                          | Technical Owner            | Containment record                   | Use RB-14 if continued processing cannot be bounded.                        |
| 3      | Identify what data left which boundary, when, through which user/service/account, and whether recipients/subprocessors are known.                                      | Security + Technical Owner | Data-flow / access log analysis      | If vendor facts are required, invoke RB-11.                                 |
| 4      | Determine whether the service terms permit retention, training, human review or onward processing and whether actual behavior matches approved terms.                  | Procurement + Legal + DPO  | Contract/DPA/vendor evidence         | Any contradiction becomes a vendor risk and potential contractual incident. |
| 5      | Assess affected individuals, systems and business assets; avoid unsupported assumptions about deletion or model memorization.                                          | DPO / Business Owner       | Scope assessment                     | Where facts are unavailable, record limitation and request vendor evidence. |
| 6      | Initiate applicable enterprise privacy, security, legal and notification processes.                                                                                    | DPO / Legal / CISO         | Specialist handoff record            | This runbook does not determine statutory notification obligations.         |
| 7      | Correct the control failure: access boundaries, DLP, data exclusions, approved-use restrictions, retention settings, connector scopes or user training as appropriate. | Control Owner              | Remediation evidence                 | Material design/config change invokes RB-12.                                |
| 8      | Validate that the data is no longer accessible through unauthorized AI queries or integrations.                                                                        | Security + Technical Owner | Validation test results              | Test using safe synthetic equivalents where possible.                       |
| 9      | Reassess residual risk and approve restart/continued use.                                                                                                              | AI Governance + Risk       | Reassessment / decision              | Unverified deletion/retention can remain an explicit residual risk.         |

### **C. Escalation and stop criteria**

- Personal data or confidential IP exposure cannot be bounded.

- Credentials, secrets or privileged tokens were included in AI inputs/outputs.

- Vendor cannot confirm retention/deletion/subprocessor handling.

- Leakage crosses employee/customer/applicant boundaries or affects vulnerable/consequential use.

- Repeated leakage indicates systemic access-control or architecture weakness.

### **D. Exit criteria**

- Further disclosure has stopped.

- Affected data types, systems and likely recipients are sufficiently bounded.

- Required legal/privacy/security/vendor routes are complete or owned.

- Corrective controls have evidence and validation.

- Residual uncertainty is documented and accepted by appropriate authority.

### **E. Minimum evidence package**

- Data classification

- Input/output/log evidence

- Data-flow map

- Vendor terms/DPA evidence

- Access logs

- Specialist assessments

- Remediation record

- Validation tests

- Reassessment/closure decision

### **F. Duckworks system-specific notes**

**PondGPT —** Cross-user retrieval is a critical assumption in the project; any violation invalidates the assumption and should trigger immediate reassessment.

**AI-007 —** Unregistered public GenAI use involving internal correspondence, code, HR documentation or customer communications should invoke RB-05 and this runbook in parallel.

**DuckDesign AI —** Engineering designs, CAD content and proprietary material selections may constitute sensitive IP even where no personal data is involved.

| **TABLETOP PROMPT.** An engineer pasted an unreleased CAD design into a public GenAI service whose training/retention settings are unknown. Which evidence must Procurement request from the provider, and what can Duckworks conclude if the provider cannot answer? |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## **RB-05 — Shadow AI Discovery & Containment**

| **PURPOSE.** Turn detection of unregistered AI use into a controlled discovery, containment, decomposition and governance intake process instead of treating “shadow AI” as one homogeneous system. |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Field**         | **Runbook position**                                                                                                                                                                 |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primary trigger   | Discovery of unapproved public GenAI, browser extension, code assistant, API, AI-enabled SaaS feature, personal account or other AI use outside Duckworks registration and approval. |
| Primary lead      | CISO + AI Governance Lead                                                                                                                                                            |
| Mandatory support | IT/Cloud; Business Manager; DPO; Legal; Procurement; HR as appropriate                                                                                                               |
| Primary systems   | AI-007 and any newly discovered use case                                                                                                                                             |
| Related playbooks | PB-01, PB-05, PB-09                                                                                                                                                                  |
| Target response   | Exposure contained, each material use decomposed and registered, data/permission exposure assessed, and the tool either prohibited, approved with controls or removed.               |

### **A. Entry conditions and immediate guardrails**

- Capture the tool/service name, account type, users, business purpose, data types, browser/application permissions, integrations and observed usage.

- Do not assume all users of the same public AI service represent one use case; material uses must be separately assessed.

| **DO NOT.** Normalize continued production use simply because the tool is popular, low-cost, personally licensed or already embedded in another SaaS product. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|

### **B. Executable procedure**

| **\#** | **Action**                                                                                                                                                                   | **Owner**                        | **Required evidence / record** | **Decision / hand-off**                                              |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|--------------------------------|----------------------------------------------------------------------|
| 1      | Create a shadow-AI discovery record and temporary use-case identifiers.                                                                                                      | AI Governance Lead               | Discovery record               | Group only genuinely equivalent uses.                                |
| 2      | Determine whether sensitive/confidential/personal data or privileged integrations are involved.                                                                              | CISO + DPO                       | Exposure triage                | Potential exposure invokes RB-04/RB-02.                              |
| 3      | Apply proportionate containment: block service, disable extension, revoke OAuth/API permissions, stop sensitive uploads or restrict to synthetic/public data pending review. | IT/Cloud + CISO                  | Containment evidence           | High uncertainty with broad permissions favors temporary suspension. |
| 4      | Interview business users to establish actual intended purpose, frequency, decisions supported and business dependency.                                                       | AI Governance + Business Manager | Use-case statement             | Usage purpose must be documented before risk assessment.             |
| 5      | Decompose material uses into individual QuackTrack records with owners.                                                                                                      | AI Governance Lead               | Inventory entries              | No owner = no authorized material use.                               |
| 6      | Assess provider terms, data use, retention, training, subprocessors, security and contractual status.                                                                        | Procurement + DPO + Security     | Due diligence record           | Unmanaged click-through terms may be unacceptable for material use.  |
| 7      | Route each use through proportionate intake/risk/security/privacy review.                                                                                                    | AI Governance Lead               | Triage decisions               | Consequential people/safety use receives enhanced review.            |
| 8      | Decide disposition: prohibit/remove, allow limited experimentation, approve controlled use, or replace with enterprise-approved capability.                                  | Business Owner + AI Governance   | Disposition decision           | Record allowed data/use boundaries explicitly.                       |
| 9      | Remediate past exposure and educate affected users; document recurrence controls.                                                                                            | CISO + Business Manager          | Remediation/training evidence  | Repeated bypass may require management escalation.                   |

### **C. Escalation and stop criteria**

- Unknown or excessive permissions to mail, files, source code, credentials or enterprise repositories.

- Evidence of sensitive data submission or external retention.

- Tool influences employment, product safety, quality or other consequential decisions.

- Business team refuses registration or attempts to bypass controls.

- Service cannot be technically disabled while exposure remains material.

### **D. Exit criteria**

- Each material discovered use is registered or formally prohibited.

- Sensitive-data and permission exposure is assessed.

- Unauthorized integrations/accounts are revoked or approved.

- Disposition and owner are recorded.

- Recurrence controls and user communication are completed.

### **E. Minimum evidence package**

- Discovery record

- User/tool inventory

- Permissions/OAuth/API evidence

- Data exposure assessment

- QuackTrack entries

- Vendor terms/due diligence

- Disposition decision

- Remediation/training record

### **F. Duckworks system-specific notes**

**AI-007 —** The project explicitly treats AI-007 as an organizational condition, not one AI system. This runbook operationalizes decomposition into individual governed records.

**PondGPT —** Where a shadow use has a valid business purpose, controlled migration to PondGPT may be considered only within PondGPT’s current restricted-pilot boundaries.

**DuckTalent-related shadow AI —** Use of public AI to rank CVs or draft consequential HR judgments requires immediate HR/Legal/Privacy review; it should not be normalized as “productivity use.”

| **TABLETOP PROMPT.** Security discovers a browser extension with access to corporate mail and files that several teams use for summarization. How do you separate harmless experimentation from material, governed use cases? |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## **RB-06 — Model Drift / Performance Degradation**

| **PURPOSE.** Respond when model/service performance, error distribution, data quality or operating conditions no longer support the approved risk and impact assumptions. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Field**         | **Runbook position**                                                                                                                                                                      |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primary trigger   | KPI/KRI breach, model drift alert, rising false positives/negatives, accuracy decline, distribution shift, unexplained output change, or complaint trend indicating degraded performance. |
| Primary lead      | Head of Data & AI / Technical Owner                                                                                                                                                       |
| Mandatory support | Business Owner; AI Governance; Risk; relevant HR/Safety/Customer SME                                                                                                                      |
| Primary systems   | FeatherForecast, WingInspect Vision, DuckTalent AI if ever deployed, QuackBot and other monitored AI                                                                                      |
| Related playbooks | PB-10, PB-11, PB-08                                                                                                                                                                       |
| Target response   | Performance issue bounded, operational reliance adjusted, cause identified, model/data/control changes validated, and reassessment completed before full restoration.                     |

### **A. Entry conditions and immediate guardrails**

- Confirm the metric breach is measured against the approved production/pilot baseline and not an instrumentation error.

- Identify which users, decisions, product lines, sites or populations are affected.

| **DO NOT.** Retrain, swap models or silently change thresholds before preserving the failing baseline and determining whether the change is material. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|

### **B. Executable procedure**

| **\#** | **Action**                                                                                                                                             | **Owner**                        | **Required evidence / record**             | **Decision / hand-off**                                                         |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|--------------------------------------------|---------------------------------------------------------------------------------|
| 1      | Validate alert integrity and reproduce the degradation using current monitoring data.                                                                  | Technical Owner                  | Monitoring records / reproducibility check | If instrumentation is faulty, correct monitoring and record the false alert.    |
| 2      | Quantify the change by metric, time, segment, data source and affected decision/output.                                                                | Data & AI                        | Performance analysis                       | Segment-level harm can matter even when aggregate performance looks acceptable. |
| 3      | Reduce operational reliance where thresholds linked to safety, rights or material business decisions are breached.                                     | Business Owner                   | Restriction/fallback record                | Use RB-14 for serious/uncontrolled consequences.                                |
| 4      | Check upstream data quality, pipeline changes, source drift, label definition, feature availability, provider/model version and configuration changes. | Technical Owner                  | Root-cause dataset/config review           | Unapproved material change invokes RB-12.                                       |
| 5      | Assess whether error distribution disproportionately affects a group, safety condition or critical scenario.                                           | Relevant SME + AI Governance     | Impact analysis                            | People-impacting disparity routes to RB-08; safety to RB-10.                    |
| 6      | Select treatment: recalibration, data correction, rollback, threshold change, retraining, model replacement, process control or reduced use.           | Data & AI + Business Owner       | Treatment plan                             | Any material model/data/config change requires controlled validation.           |
| 7      | Validate treatment against original acceptance criteria plus newly observed failure mode.                                                              | Validation Owner                 | Validation report                          | Do not validate only on the previously successful dataset.                      |
| 8      | Update risk/impact assessment if severity, likelihood, affected population or control effectiveness changed.                                           | AI Governance + Risk             | Reassessment                               | High/Critical residual risk escalates.                                          |
| 9      | Restore scope gradually and confirm post-change monitoring stability.                                                                                  | Business Owner + Technical Owner | Restoration record / monitoring results    | Use RB-01 if the remediation constitutes a new production release gate.         |

### **C. Escalation and stop criteria**

- Safety-related false negatives or performance breach tied to released product.

- Fairness or group disparity signal in a people-impacting system.

- Large unexplained shift after vendor/model update.

- Business dependency prevents fallback despite failed acceptance threshold.

- Monitoring cannot reliably measure the key failure mode.

### **D. Exit criteria**

- Root cause is understood or explicitly bounded.

- Reliance is proportionate to verified performance.

- Treatment has validation evidence.

- Risk/impact assumptions and monitoring thresholds are updated.

- Restoration/release is approved and recorded.

### **E. Minimum evidence package**

- Monitoring alert

- Baseline and degraded metrics

- Segment analysis

- Data/config/version evidence

- Fallback record

- Root-cause analysis

- Treatment/validation

- Reassessment

- Restoration approval

### **F. Duckworks system-specific notes**

**FeatherForecast —** Operational and financial impact is primary; authorized managers retain approval for material purchasing/production commitments.

**WingInspect Vision —** False-negative performance is more important than aggregate accuracy where missed defects can affect quality/safety.

**QuackBot —** Monitor harmful/incorrect answer rates, escalation effectiveness and complaint trends in addition to generic language-model metrics.

| **TABLETOP PROMPT.** WingInspect’s overall accuracy is stable, but false negatives increase for a newly introduced component finish. What makes this a material governance issue even if the headline accuracy barely changes? |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## **RB-07 — Harmful / Incorrect Output**

| **PURPOSE.** Handle AI outputs that are materially wrong, misleading, unsafe, offensive, out of scope, or otherwise inconsistent with the approved intended purpose and safeguards. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Field**         | **Runbook position**                                                                                                                           |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Primary trigger   | User complaint, QA review, monitoring alert or staff observation of a harmful/incorrect AI output that is not primarily a security compromise. |
| Primary lead      | Business Owner                                                                                                                                 |
| Mandatory support | Technical Owner; AI Governance; CISO; Legal/DPO/HR/Safety depending on impact                                                                  |
| Primary systems   | QuackBot, PondGPT, DuckDesign AI and other generative/predictive systems                                                                       |
| Related playbooks | PB-07, PB-09, PB-10                                                                                                                            |
| Target response   | Harm contained, affected users/decisions identified, output failure classified, corrective control validated and recurrence monitored.         |

### **A. Entry conditions and immediate guardrails**

- Capture the exact output and input/context where appropriate.

- Determine whether a human acted on the output and whether downstream harm occurred.

| **DO NOT.** Dismiss an incorrect output as “just hallucination” when the system is used in a context where users may reasonably rely on it. |
|---------------------------------------------------------------------------------------------------------------------------------------------|

### **B. Executable procedure**

| **\#** | **Action**                                                                                                                                                                               | **Owner**                        | **Required evidence / record** | **Decision / hand-off**                                    |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|--------------------------------|------------------------------------------------------------|
| 1      | Record the output, input, context, model/service/version, user, time and downstream action.                                                                                              | Business Owner / Technical Owner | Output incident record         | If security manipulation is suspected, invoke RB-03.       |
| 2      | Assess impact: informational nuisance, customer harm, employment consequence, engineering/safety risk, privacy issue or policy violation.                                                | Business Owner + AI Governance   | Impact triage                  | Consequential impact invokes appropriate specialist route. |
| 3      | Correct or retract the output where users/customers may rely on it and provide human support if needed.                                                                                  | Business Owner                   | Correction/escalation record   | Do not wait for root cause before preventing reliance.     |
| 4      | Determine failure class: knowledge gap, stale source, retrieval error, instruction failure, reasoning/accuracy issue, unsupported claim, unsafe recommendation or UX disclosure problem. | Technical Owner + SME            | Failure classification         | Security or poisoning routes to RB-03.                     |
| 5      | Review whether the use case asks AI to perform beyond approved decision/support boundary.                                                                                                | AI Governance + Business Owner   | Purpose-boundary review        | Scope creep invokes RB-12.                                 |
| 6      | Apply treatment: source correction, prompt/workflow change, escalation threshold, answer abstention, validation rule, human review, restricted content or service/model change.          | Technical Owner + Business Owner | Change/treatment record        | Material change invokes RB-12.                             |
| 7      | Retest the specific case and a representative set of nearby cases; assess regressions.                                                                                                   | Validation Owner                 | Test report                    | Do not accept one corrected example as sufficient.         |
| 8      | Update monitoring and user guidance for the observed failure mode.                                                                                                                       | Business Owner + AI Governance   | Monitoring/guidance update     | Repeated pattern can elevate incident priority.            |

### **C. Escalation and stop criteria**

- Incorrect output created or could create serious physical harm, discriminatory treatment, privacy breach or material financial/contractual action.

- Repeated similar failures indicate systemic unreliability.

- Human reviewers routinely fail to catch known failure modes.

- Output correction requires changing intended purpose or model/provider.

### **D. Exit criteria**

- Affected output is corrected/contained.

- Downstream decisions/users are identified and remediated where needed.

- Failure mode is understood and treated.

- Validation demonstrates acceptable operation within approved scope.

- Monitoring tracks recurrence.

### **E. Minimum evidence package**

- Input/output/context

- Impact assessment

- Correction record

- Failure classification

- Purpose review

- Treatment change

- Validation tests

- Monitoring update

### **F. Duckworks system-specific notes**

**QuackBot —** Incorrect warranty or troubleshooting guidance requires customer correction and safe escalation; safety-relevant troubleshooting should not rely on unverified generated advice.

**DuckDesign AI —** Engineering recommendations remain advisory and require competent engineer validation; harmful output may indicate ineffective human oversight as well as model failure.

**PondGPT —** Internal productivity use still needs safeguards where outputs influence code, HR documentation or operational procedures.

| **TABLETOP PROMPT.** QuackBot confidently gives an incorrect warranty condition to several customers. The answer is not malicious. What distinguishes a content correction from a governance incident? |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## **RB-08 — Fairness / Discrimination Alert**

| **PURPOSE.** Provide a controlled response to evidence or credible concern that an AI-supported people decision may create unjustified unequal treatment, discriminatory outcomes, accessibility barriers or materially different error rates. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Field**         | **Runbook position**                                                                                                                                                                    |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primary trigger   | Complaint, fairness test, monitoring result, audit finding or staff observation indicating potential disparate treatment or proxy discrimination.                                       |
| Primary lead      | Chief People Officer + AI Governance                                                                                                                                                    |
| Mandatory support | General Counsel; DPO; HR; Data & AI; Business Owner; affected-stakeholder representative as appropriate                                                                                 |
| Primary systems   | DuckTalent AI primarily; other workforce/people-impacting AI                                                                                                                            |
| Related playbooks | PB-03, PB-07, PB-09, PB-10                                                                                                                                                              |
| Target response   | Potential discriminatory effect contained, affected decision process reviewed, evidence preserved, analysis completed, safeguards/treatment validated and legal/HR decision documented. |

### **A. Entry conditions and immediate guardrails**

- Treat the allegation as a material impact signal, not proof of discrimination.

- Preserve model/version, scoring logic, input features, decision records and human overrides for the affected period using synthetic or lawfully processed data as appropriate.

| **DO NOT.** Continue consequential automated ranking merely to collect more production evidence when credible harmful disparity has been identified and safer evaluation routes exist. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### **B. Executable procedure**

| **\#** | **Action**                                                                                                                                                                                | **Owner**                          | **Required evidence / record** | **Decision / hand-off**                                                                    |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|--------------------------------|--------------------------------------------------------------------------------------------|
| 1      | Open case linked to system and affected decision process; record allegation/metric without prejudging cause.                                                                              | HR + AI Governance                 | Case record                    | If system is not approved for production, investigate unauthorized use.                    |
| 2      | Pause or restrict the affected ranking/recommendation process where continued use could compound harm.                                                                                    | Chief People Officer               | Restriction record             | DuckTalent remains Do Not Deploy under current baseline.                                   |
| 3      | Preserve relevant model/data/version, criteria, job configuration, human review and decision evidence.                                                                                    | Data & AI + HR                     | Evidence manifest              | Protect applicant/employee privacy during analysis.                                        |
| 4      | Identify affected groups, decision points, error/disparity patterns and plausible proxy features.                                                                                         | HR + Data & AI + DPO               | Fairness analysis plan/results | Do not infer protected attributes without lawful basis and governance review.              |
| 5      | Review job-related criteria, feature relevance, accessibility and potential historical-data effects.                                                                                      | HR + Legal                         | Criteria review                | Unjustified criteria are treated as process/control defects, not just model tuning issues. |
| 6      | Assess effectiveness of human review: override behavior, rubber-stamping, explanation quality and contestability.                                                                         | AI Governance + HR                 | Oversight analysis             | Ineffective oversight invokes RB-09.                                                       |
| 7      | Determine corrective treatment: data/feature change, decision boundary, threshold, reviewer procedure, transparency, accessibility, contestability, model replacement or discontinuation. | HR + AI Governance + Data & AI     | Treatment plan                 | Material changes invoke RB-12 and enhanced reassessment.                                   |
| 8      | Validate treatment using an approved fairness/testing methodology before any consequential use.                                                                                           | Validation Owner + HR/Legal review | Validation report              | No production release from this runbook alone; use RB-01 after all gates.                  |
| 9      | Communicate/remediate affected decisions where Legal/HR determines appropriate.                                                                                                           | HR + Legal                         | Remediation record             | Record rationale and affected-person process.                                              |

### **C. Escalation and stop criteria**

- Potential systemic discrimination or broad affected population.

- Protected or sensitive data handling raises privacy/legal questions.

- Human review cannot meaningfully detect/correct ranking errors.

- Vendor refuses sufficient documentation/testing support.

- Management proposes production despite unresolved Critical residual risk.

### **D. Exit criteria**

- Potential harm is contained.

- Relevant decision/data/model evidence is preserved.

- Fairness/criteria/oversight analysis is complete or limitations are explicit.

- Corrective treatment is validated.

- Legal/HR/governance decision is recorded before any restart.

### **E. Minimum evidence package**

- Complaint/alert record

- Decision/model/data baseline

- Fairness analysis

- Job-criteria review

- Oversight/override analysis

- Treatment plan

- Validation evidence

- Affected-person remediation record

- Governance decision

### **F. Duckworks system-specific notes**

**DuckTalent AI —** The project baseline already treats DuckTalent as Critical current residual risk and Do Not Deploy. This runbook is for investigation/readiness and must not be interpreted as production authorization.

**Affected applicants —** Transparency, accessibility, contestability and meaningful human review are part of the impact lens in the Duckworks scenario.

**Legal boundary —** Any statutory employment/equality or AI-law conclusion remains for qualified legal review; this runbook is an internal governance procedure.

| **TABLETOP PROMPT.** A synthetic pre-deployment fairness test shows materially lower recommendation rates for a group after adding a new proxy-like feature. What gets frozen, who reviews the job-relatedness, and what evidence is needed before retesting? |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## **RB-09 — Human Oversight Failure / Automation Bias**

| **PURPOSE.** Respond when required human review is bypassed, unavailable, unqualified, routinely rubber-stamped, or unable to override AI outputs effectively. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Field**         | **Runbook position**                                                                                                                                                                        |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primary trigger   | Override rate anomaly, audit finding, complaint, workflow bypass, reviewer vacancy, time pressure, UI design issue or evidence that humans are deferring to AI without meaningful judgment. |
| Primary lead      | Business Owner + AI Governance                                                                                                                                                              |
| Mandatory support | HR/Training; Technical Owner; Risk; Legal/Safety SMEs depending on domain                                                                                                                   |
| Primary systems   | DuckTalent, DuckDesign, WingInspect, QuackBot escalation, FeatherForecast                                                                                                                   |
| Related playbooks | PB-03, PB-07, PB-09, PB-10                                                                                                                                                                  |
| Target response   | Consequential AI reliance reduced until competent human authority, override capability, escalation and evidence are demonstrably functioning.                                               |

### **A. Entry conditions and immediate guardrails**

- Identify which decisions require human authority under the approved system boundary.

- Determine whether the issue is individual behavior, staffing/competence, UI/workflow design, permissions, performance pressure or ambiguous accountability.

| **DO NOT.** Treat a nominal “human in the loop” checkbox as effective oversight when reviewers lack time, competence, information or practical authority to disagree. |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### **B. Executable procedure**

| **\#** | **Action**                                                                                                                                           | **Owner**                         | **Required evidence / record** | **Decision / hand-off**                                       |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|--------------------------------|---------------------------------------------------------------|
| 1      | Record the affected decision workflow, required human role and observed oversight failure.                                                           | AI Governance + Business Owner    | Oversight incident record      | If serious harm occurred, invoke RB-02.                       |
| 2      | Restrict AI-supported consequential decisions until minimum human authority is restored.                                                             | Business Owner                    | Restriction/fallback record    | Use manual process where available.                           |
| 3      | Verify reviewer identity, authorization, competence, training and actual access to supporting information.                                           | Business Manager / HR             | Authorization/training record  | Unqualified reviewer cannot satisfy oversight requirement.    |
| 4      | Test whether the reviewer can inspect relevant rationale/input, override output, document reason, escalate and stop the process.                     | AI Governance + Technical Owner   | Oversight functional test      | Technical inability to override is a control failure.         |
| 5      | Analyze override/acceptance patterns, review times, disagreement rates and known error catches for automation-bias signals.                          | Risk + Business Owner             | Oversight metrics              | Near-zero override can be a warning, not proof of quality.    |
| 6      | Identify pressure points: throughput targets, interface defaults, alert fatigue, unexplained scores, lack of alternatives or unclear accountability. | Business Owner + HR/Human Factors | Root-cause analysis            | Treat process incentives as controls, not only user training. |
| 7      | Remediate workflow, staffing, competence, UI, escalation, documentation or AI decision boundary.                                                     | Business Owner + Technical Owner  | Remediation record             | Material autonomy/purpose change invokes RB-12.               |
| 8      | Revalidate oversight using scenario testing and observed operation.                                                                                  | AI Governance / Quality           | Oversight validation           | Consequential use remains restricted until effective.         |
| 9      | Update risk/impact and approval status if prior residual-risk assumptions relied on ineffective human oversight.                                     | Risk + AI Governance              | Reassessment / decision        | Potential Critical residual risk escalates.                   |

### **C. Escalation and stop criteria**

- No competent human can currently exercise final authority for a consequential decision.

- System technically prevents override or obscures information necessary for review.

- Reviewers systematically accept outputs despite known errors.

- Staffing/throughput conditions make meaningful review impracticable.

- Failure affects employment, safety or other rights-impacting decisions.

### **D. Exit criteria**

- Named competent reviewers are available and authorized.

- Override/escalation/stop mechanisms work in practice.

- Reviewers have sufficient information and time.

- Monitoring tracks oversight effectiveness.

- Risk/impact/approval records reflect actual oversight design.

### **E. Minimum evidence package**

- Decision workflow

- Reviewer authorization/training

- Functional oversight tests

- Override metrics

- Root-cause analysis

- Workflow/UI changes

- Validation evidence

- Reassessment/approval

### **F. Duckworks system-specific notes**

**WingInspect Vision —** Qualified human inspectors retain final acceptance/rejection authority under the project assumption; loss of that authority changes safety and risk conclusions.

**DuckDesign AI —** Competent engineer review before prototyping/production is a critical open assumption requiring validation.

**FeatherForecast —** Authorized managers remain responsible for material purchasing/production commitments; blind auto-execution would be a material change.

| **TABLETOP PROMPT.** Managers begin accepting FeatherForecast purchase recommendations automatically because “it has been right for months.” No formal automation setting changed. Why can this still be an oversight control failure? |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## **RB-10 — Product Safety / Quality AI Failure**

| **PURPOSE.** Provide a rapid governance route when AI-assisted engineering, inspection or other product-related AI may contribute to unsafe design, missed defects, defective release or loss of validated quality controls. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Field**         | **Runbook position**                                                                                                                                                         |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primary trigger   | Safety concern, defect escape, false-negative spike, unsafe design recommendation, field complaint, near miss, quality audit finding or evidence of unvalidated AI reliance. |
| Primary lead      | Director Product Safety & Quality                                                                                                                                            |
| Mandatory support | Business Owner; Engineering/Manufacturing; CISO if security-related; AI Governance; Legal; Data & AI                                                                         |
| Primary systems   | DuckDesign AI, WingInspect Vision, product-integrated AI                                                                                                                     |
| Related playbooks | PB-03, PB-07, PB-09, PB-10                                                                                                                                                   |
| Target response   | Affected product/process isolated, human authority restored, safety/quality scope bounded, AI contribution analyzed, validation repeated and release decision re-approved.   |

### **A. Entry conditions and immediate guardrails**

- Activate existing product quality/safety processes in parallel where applicable; this AI runbook supplements rather than replaces them.

- Preserve the AI recommendation/detection, model/version, input/image/design, human review and product/batch identifiers.

| **DO NOT.** Use the absence of confirmed injury as evidence that the AI failure is low risk. Near misses and defect escapes can invalidate safety assumptions. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|

### **B. Executable procedure**

| **\#** | **Action**                                                                                                                                                         | **Owner**                                    | **Required evidence / record** | **Decision / hand-off**                                                           |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|--------------------------------|-----------------------------------------------------------------------------------|
| 1      | Identify affected product, batch, design, inspection step and AI contribution.                                                                                     | Product Safety & Quality                     | Safety/quality incident record | If field product may be unsafe, follow enterprise product escalation immediately. |
| 2      | Suspend AI reliance for the affected decision and restore qualified human/manual process.                                                                          | Manufacturing/Engineering Owner              | Fallback record                | Use RB-14 where necessary.                                                        |
| 3      | Preserve design/image/input, AI output, model/service/version, threshold, human review and release records.                                                        | Technical Owner + Quality                    | Evidence manifest              | Maintain product traceability.                                                    |
| 4      | Bound affected production/design scope by time, version, line/site/component and downstream product.                                                               | Quality + Engineering                        | Scope analysis                 | Unknown scope requires conservative containment.                                  |
| 5      | Analyze AI failure: false negative/positive, unsafe recommendation, dataset shift, configuration, integration, security manipulation or human-oversight breakdown. | Engineering + Data & AI + Quality            | Failure analysis               | Security manipulation routes to RB-03; oversight to RB-09.                        |
| 6      | Assess whether released product or safety-related decision requires additional legal/product actions.                                                              | Legal + Product Safety                       | Specialist review              | This document does not determine statutory product obligations.                   |
| 7      | Correct model/data/process/validation/oversight control and document change.                                                                                       | Control Owner                                | CAPA / change record           | Material model/data/integration change invokes RB-12.                             |
| 8      | Repeat safety/quality validation with emphasis on observed failure class and worst credible conditions.                                                            | Quality Validation Owner                     | Validation report              | No return to AI reliance without acceptable evidence.                             |
| 9      | Reassess residual risk and authorize constrained restart/release.                                                                                                  | AI Governance Committee / delegated approver | Reassessment / approval        | High/Critical matters follow risk methodology.                                    |

### **C. Escalation and stop criteria**

- Potential serious physical harm or unsafe released product.

- AI performs or effectively becomes a safety function beyond prior assumptions.

- False-negative performance cannot be bounded.

- Human final authority was bypassed or ineffective.

- Product architecture changes may alter regulatory applicability assumptions.

### **D. Exit criteria**

- Affected product/process scope is bounded and handled through quality/safety process.

- AI reliance is suspended or safely restored with validated controls.

- Failure root cause/treatment is documented.

- Human authority and traceability are effective.

- Reassessment and release decision are recorded.

### **E. Minimum evidence package**

- Product/batch/design trace

- AI input/output/model version

- Human review/release record

- Scope analysis

- Failure/CAPA report

- Safety/legal review

- Validation results

- Reassessment/release approval

### **F. Duckworks system-specific notes**

**WingInspect Vision —** Current gate is Restricted Pilot; final acceptance remains with qualified human inspectors and false-negative testing is a minimum condition.

**DuckDesign AI —** Outputs are advisory under a critical open assumption; competent engineer validation must be demonstrable before production design reliance.

**Product scope —** The assumptions register states exact machinery/product/cybersecurity applicability remains product-specific and must be assessed before real conformity claims.

| **TABLETOP PROMPT.** A component that WingInspect marked “pass” later shows a crack during downstream testing. Which records let Duckworks determine whether the problem is model performance, image quality, threshold configuration or ineffective human inspection? |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## **RB-11 — Third-Party AI Vendor Event**

| **PURPOSE.** Respond to a material supplier event affecting an AI service, model, API or AI-enabled SaaS, including outage, security/privacy incident, model change, subprocessor change, data-use change, degraded evidence or contract change. |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Field**         | **Runbook position**                                                                                                                                                           |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primary trigger   | Vendor notification, service degradation, model/version change, subprocessor/data-use update, incident, contractual term change, deprecation or evidence expiry.               |
| Primary lead      | Procurement & Vendor Assurance                                                                                                                                                 |
| Mandatory support | CISO; DPO; Legal; Technical Owner; Business Owner; AI Governance                                                                                                               |
| Primary systems   | Any third-party AI or dependency                                                                                                                                               |
| Related playbooks | PB-04, PB-09, PB-11, PB-12                                                                                                                                                     |
| Target response   | Vendor event classified, affected systems identified, contractual/evidence rights exercised, operational exposure controlled, and reassessment/exit triggered where necessary. |

### **A. Entry conditions and immediate guardrails**

- Maintain dependency mapping so Duckworks can identify which AI systems use the affected vendor/model/service.

- Preserve the vendor notice and current/previous contract, DPA, AI schedule, security evidence and technical version information.

| **DO NOT.** Treat “no action required” in a vendor email as Duckworks’ risk decision. Duckworks must assess the event against its own intended purpose, data, controls and risk. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### **B. Executable procedure**

| **\#** | **Action**                                                                                                                                                       | **Owner**                                    | **Required evidence / record**       | **Decision / hand-off**                                      |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|--------------------------------------|--------------------------------------------------------------|
| 1      | Log vendor event and identify affected Duckworks systems, environments, data and business owners.                                                                | Procurement + AI Governance                  | Vendor event record / dependency map | Unknown dependency scope escalates until bounded.            |
| 2      | Classify event type: outage, incident, security/privacy change, model/version change, subprocessor/data use, contract/terms, deprecation or evidence gap.        | Procurement                                  | Event classification                 | Security/privacy incident invokes RB-02/RB-04 as applicable. |
| 3      | Exercise contractual notification/cooperation rights and request evidence needed to assess impact.                                                               | Procurement + Legal                          | Vendor request / response            | Failure to cooperate becomes a supplier risk.                |
| 4      | Assess technical and business impact, including changed outputs, performance, availability, retention, training use, access, subprocessors and exit constraints. | Technical Owner + SMEs                       | Impact assessment                    | Material change invokes RB-12.                               |
| 5      | Apply operational containment/fallback if service reliability or control assumptions are no longer acceptable.                                                   | Business Owner + Technical Owner             | Fallback/restriction record          | Use RB-14 if urgent.                                         |
| 6      | Review whether existing due diligence and contract protections remain sufficient.                                                                                | Procurement + CISO + DPO + Legal             | Updated due diligence                | Record evidence confidence.                                  |
| 7      | Decide treatment: accept with monitoring, require remediation, restrict use, change configuration, move provider, suspend, or initiate exit.                     | Business Owner + Procurement + AI Governance | Supplier treatment decision          | High/Critical residual risk escalates.                       |
| 8      | Update inventory, assessments, vendor register, monitoring and renewal/exit plan.                                                                                | AI Governance + Procurement                  | Updated records                      | Use RB-15 if exit chosen.                                    |

### **C. Escalation and stop criteria**

- Vendor incident may expose Duckworks confidential/personal data.

- Model/service change invalidates validation or changes intended-purpose capability.

- Vendor starts using customer data for training contrary to approved basis/terms.

- Critical provider refuses material evidence or timely cooperation.

- Deprecation creates unsafe/uncontrolled business continuity risk.

### **D. Exit criteria**

- Affected systems and event scope are known.

- Required vendor evidence has been obtained or absence is explicitly treated as risk.

- Operational decision is recorded.

- Assessments/contracts/monitoring are updated.

- Exit or remediation actions are owned and tracked.

### **E. Minimum evidence package**

- Vendor notice

- Dependency map

- Contract/DPA/AI schedule

- Vendor questions/responses

- Technical impact analysis

- Updated due diligence

- Risk/treatment decision

- Inventory/reassessment update

- Exit plan if applicable

### **F. Duckworks system-specific notes**

**Third-party mix —** Duckworks assumes a combination of internal and third-party AI; supplier events can therefore affect multiple systems at once.

**DuckTalent AI —** Provider/model is TBD in the current project; procurement cannot claim vendor controls until a specific supplier and evidence exist.

**QuackBot/PondGPT —** Hosted GenAI requires attention to tenant isolation, permissions, RAG/data handling, service changes and incident cooperation.

| **TABLETOP PROMPT.** A vendor silently changes the foundation model behind PondGPT but says API compatibility is unchanged. What evidence would make this a material governance change even if there is no outage? |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## **RB-12 — Material Model / Data / Integration Change**

| **PURPOSE.** Determine whether a proposed or discovered change invalidates prior risk, impact, legal, security, privacy, validation or approval evidence and route the system through proportionate reassessment. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Field**         | **Runbook position**                                                                                                                                                                          |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primary trigger   | Change to intended purpose, autonomy, provider/model/version, training/reference data, affected population, geography, integrations, permissions, user group, decision role or legal context. |
| Primary lead      | AI Governance Lead + Technical Owner                                                                                                                                                          |
| Mandatory support | Business Owner; Risk; CISO; Legal; DPO; HR/Safety/Procurement as applicable                                                                                                                   |
| Primary systems   | All governed AI                                                                                                                                                                               |
| Related playbooks | PB-11, PB-02, PB-03, PB-04, PB-08                                                                                                                                                             |
| Target response   | Change classified, affected evidence identified, necessary reassessment/testing completed, and prior approval reaffirmed or replaced before changed production use.                           |

### **A. Entry conditions and immediate guardrails**

- Describe the “before” and “after” state precisely enough to identify affected assumptions and controls.

- Treat undocumented vendor/model change as a change event, not routine maintenance, until materiality is assessed.

| **DO NOT.** Use semantic version labels such as “minor upgrade” as proof of low governance impact. Materiality depends on capability, data, behavior, affected persons and controls. |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### **B. Executable procedure**

| **\#** | **Action**                                                                                                                                                              | **Owner**                        | **Required evidence / record** | **Decision / hand-off**                                                   |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|--------------------------------|---------------------------------------------------------------------------|
| 1      | Record change request/event with before/after purpose, model/service, data, integrations, permissions, users, geography, autonomy and affected decisions.               | Technical Owner + Business Owner | Change record                  | Insufficient description blocks approval.                                 |
| 2      | Map the change to critical assumptions and prior assessment evidence.                                                                                                   | AI Governance Lead               | Assumption/evidence impact map | Critical assumption change triggers reassessment.                         |
| 3      | Classify change as non-material, material-limited, or material-major using risk/impact consequences rather than technical effort.                                       | AI Governance + Risk             | Materiality decision           | Rights/safety/autonomy changes are presumptively material pending review. |
| 4      | Identify required specialist reassessments: legal classification, privacy/DPIA, security threat model, vendor due diligence, fairness, product safety, human oversight. | AI Governance Lead               | Reassessment plan              | No specialist can be skipped solely to meet release deadline.             |
| 5      | Update risk scenarios, inherent/current residual risk and control evidence for affected domains.                                                                        | Risk + System Owner              | Updated assessment             | Planned post-change controls receive no current credit.                   |
| 6      | Perform required validation/security/performance/fairness/safety testing against changed configuration.                                                                 | Technical Owner / SMEs           | Test evidence                  | Tests must identify exact changed version/configuration.                  |
| 7      | Update monitoring thresholds and safe fallback if failure modes or dependency changed.                                                                                  | Technical Owner + Business Owner | Monitoring/fallback update     | Unowned new failure mode blocks release.                                  |
| 8      | Obtain approval at the appropriate lifecycle/risk authority before changed production use.                                                                              | AI Governance Lead               | Approval decision              | Use RB-01 for release gate.                                               |
| 9      | Update QuackTrack, evidence links, next review date and superseded artifacts.                                                                                           | AI Governance Lead               | Inventory/version history      | Prior evidence remains traceable, not overwritten.                        |

### **C. Escalation and stop criteria**

- Change increases autonomy or removes human final authority.

- New affected population/geography or consequential decision use.

- New personal/sensitive data or privileged integration.

- Provider/model change invalidates validation or vendor evidence.

- Change affects product safety or legal classification assumptions.

### **D. Exit criteria**

- Materiality decision is recorded.

- Required reassessments/tests are complete.

- Updated controls and monitoring have evidence.

- Approval for changed configuration is recorded.

- Inventory and version/evidence history are current.

### **E. Minimum evidence package**

- Change request

- Before/after baseline

- Assumption impact map

- Materiality decision

- Updated risk/AIA/legal/security/privacy/vendor reviews

- Validation results

- Monitoring update

- Approval

- QuackTrack history

### **F. Duckworks system-specific notes**

**Assumptions register —** Duckworks explicitly treats changes to intended purpose, affected persons, legal role, safety impact, data category or degree of automation as potentially assessment-changing.

**Vendor changes —** Use RB-11 in parallel where the change originates from a third party.

**Lifecycle gate —** A material change can return a production system to restricted or blocked status pending reassessment.

| **TABLETOP PROMPT.** FeatherForecast gains an automated purchase-order integration. The predictive model is unchanged. Why is this still a potentially major change? |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## **RB-13 — AI Access / Permission Misconfiguration**

| **PURPOSE.** Contain AI systems, agents, assistants or integrations that can access data, repositories, tools or actions beyond approved user/system authorization boundaries. |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Field**         | **Runbook position**                                                                                                                                                            |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primary trigger   | Unexpected cross-user retrieval, excessive OAuth/API scope, overprivileged service account, unauthorized tool call, connector misconfiguration or access-control audit finding. |
| Primary lead      | CISO + Head of IT/Cloud                                                                                                                                                         |
| Mandatory support | Technical Owner; AI Governance; DPO; Business Owner; Data Owner                                                                                                                 |
| Primary systems   | PondGPT, QuackBot, AI agents/tools, browser extensions and integrated AI services                                                                                               |
| Related playbooks | PB-06, PB-09, PB-11                                                                                                                                                             |
| Target response   | Excess access revoked, data exposure bounded, authorization architecture corrected, validation proves least-privilege behavior, and prior risk assumptions reassessed.          |

### **A. Entry conditions and immediate guardrails**

- Identify the identity context: end user, service account, API token, plugin, agent, connector or vendor tenant.

- Determine whether the AI is enforcing access itself or relying on upstream/downstream systems; authorization should not depend solely on model behavior.

| **DO NOT.** Fix only the prompt or system instruction when the actual problem is excessive technical permission. |
|------------------------------------------------------------------------------------------------------------------|

### **B. Executable procedure**

| **\#** | **Action**                                                                                                                                                                        | **Owner**                  | **Required evidence / record**      | **Decision / hand-off**                                          |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|-------------------------------------|------------------------------------------------------------------|
| 1      | Open incident/change record and identify excessive permission, identity, resource and affected system.                                                                            | CISO / IT                  | Access incident record              | If actual disclosure occurred, invoke RB-04.                     |
| 2      | Revoke or reduce the excessive permission and isolate affected connector/account.                                                                                                 | IT/Cloud                   | IAM/config evidence                 | Use RB-14 if safe operation cannot continue.                     |
| 3      | Review access logs to identify what resources were actually queried/read/modified and by whom.                                                                                    | Security                   | Access-log analysis                 | Unknown scope escalates.                                         |
| 4      | Map intended authorization model and identify where enforcement failed: identity propagation, ACL filter, service account scope, tool policy, caching/indexing or vendor tenancy. | Security + Technical Owner | Authorization architecture analysis | Architecture defect may require material change review.          |
| 5      | Correct permissions using least privilege, per-user authorization, scoped service identities, tool allowlists and repository exclusions as appropriate.                           | IT/Cloud + Technical Owner | Remediation/configuration record    | Avoid broad shared credentials for user-specific retrieval.      |
| 6      | Test positive and negative authorization cases across users/groups/resources.                                                                                                     | Security / QA              | Authorization test report           | Include deny cases; “can access own data” alone is insufficient. |
| 7      | Review cached/indexed/vectorized content to ensure revocation is reflected in retrieval layer.                                                                                    | Technical Owner            | Index/cache validation              | Rebuild/quarantine if stale permissions remain.                  |
| 8      | Update threat model, risk assessment and monitoring for privilege anomalies.                                                                                                      | CISO + AI Governance       | Updated assessment/monitoring       | Critical assumption changes trigger RB-12.                       |

### **C. Escalation and stop criteria**

- Cross-user or cross-tenant confidential/personal-data access.

- AI can execute privileged changes, transactions or code beyond approved scope.

- Permission model cannot enforce per-user access.

- Shared index/cache retains content after source access is revoked.

- Vendor architecture prevents Duckworks from verifying isolation.

### **D. Exit criteria**

- Excess access is revoked.

- Actual access/exposure is bounded.

- Authorization architecture is corrected.

- Positive/negative access tests pass.

- Risk/monitoring and restart decision are updated.

### **E. Minimum evidence package**

- IAM/permission snapshot

- Access logs

- Architecture analysis

- Remediation config

- Positive/negative tests

- Index/cache evidence

- Threat/risk update

- Restart decision

### **F. Duckworks system-specific notes**

**PondGPT —** The assumptions register treats enterprise access enforcement as critical: users should not obtain documents they could not otherwise access.

**QuackBot —** External users must not gain internal knowledge-source or tool permissions through chatbot context.

**Shadow extensions —** Browser extensions with broad mail/file scopes should route through RB-05 in addition to this access-control runbook.

| **TABLETOP PROMPT.** PondGPT correctly enforces SharePoint permissions at query time, but its vector index was built using a service account with access to everything. What must the team test before claiming user-level authorization is effective? |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## **RB-14 — Emergency Suspension / Safe Fallback**

| **PURPOSE.** Provide the controlled “stop” mechanism when continued AI operation creates unacceptable immediate uncertainty or harm and normal corrective change is too slow. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Field**         | **Runbook position**                                                                                                                                                               |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primary trigger   | P1 incident, serious safety/rights/privacy/security concern, uncontrolled output, active compromise, loss of human authority, or governance decision to block continued operation. |
| Primary lead      | System Business Owner + CISO for security emergencies                                                                                                                              |
| Mandatory support | Technical Owner; AI Governance; relevant Legal/DPO/HR/Safety/Procurement                                                                                                           |
| Primary systems   | All AI systems; especially consequential or externally exposed systems                                                                                                             |
| Related playbooks | PB-09, PB-12                                                                                                                                                                       |
| Target response   | AI capability safely stopped or isolated, business fallback activated, evidence preserved, stakeholder communication controlled, and restart prevented until authorized.           |

### **A. Entry conditions and immediate guardrails**

- Each material AI system should have a pre-defined stop/fallback mechanism proportionate to impact; if none exists, this is a control gap.

- Emergency action should minimize further harm while preserving critical evidence where feasible.

| **DO NOT.** Keep a harmful AI service online solely to preserve availability KPIs. Safety, rights, confidentiality and control take precedence over AI convenience. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### **B. Executable procedure**

| **\#** | **Action**                                                                                                                                                                                | **Owner**                              | **Required evidence / record**             | **Decision / hand-off**                                              |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|--------------------------------------------|----------------------------------------------------------------------|
| 1      | Confirm suspension authority and incident priority; for urgent P1 conditions, act within delegated emergency authority and document immediately.                                          | Business Owner / CISO                  | Suspension authorization / incident record | Do not wait for committee meeting where delay could worsen harm.     |
| 2      | Select safest stop action: disable feature, remove external route, revoke credential, isolate model/service, disable tool, roll back version, restrict users or switch to manual process. | Technical Owner                        | Stop plan                                  | Avoid actions that destroy evidence unless required for safety.      |
| 3      | Execute stop and verify it actually prevents affected processing/action.                                                                                                                  | Technical Owner + Independent verifier | Execution/verification record              | If stop fails, escalate infrastructure/vendor support.               |
| 4      | Activate documented business fallback/manual process and communicate affected operating teams.                                                                                            | Business Owner                         | Fallback activation / communication        | Fallback itself must have clear authority and capacity.              |
| 5      | Preserve logs, configuration, model/version and pre-stop state needed for investigation.                                                                                                  | Security / Technical Owner             | Evidence manifest                          | Follow chain-of-custody/evidence rules where investigation requires. |
| 6      | Notify relevant governance specialists and vendor if external dependency is involved.                                                                                                     | AI Governance Lead                     | Notification log                           | Legal/DPO/Safety review based on impact.                             |
| 7      | Prevent unauthorized restart by restricting deployment/configuration authority or flagging blocked status in governance tooling.                                                          | IT/Cloud + AI Governance               | Access restriction / QuackTrack status     | No informal “temporary re-enable.”                                   |
| 8      | Route root cause to relevant runbook and define restart criteria.                                                                                                                         | Incident Lead                          | Investigation route / restart checklist    | Restart uses RB-01 when production approval must be re-established.  |

### **C. Escalation and stop criteria**

- Stop mechanism fails or vendor prevents isolation.

- Fallback cannot support critical business/safety process.

- Suspension itself creates material safety or legal risk.

- Multiple systems share affected dependency.

- Unauthorized restart is attempted.

### **D. Exit criteria**

- Affected AI processing is stopped or tightly isolated.

- Fallback is operating or business decision accepts controlled outage.

- Evidence is preserved.

- Blocked status and restart authority are recorded.

- Specific restart criteria and owners are defined.

### **E. Minimum evidence package**

- Suspension authorization

- Stop execution logs

- Verification

- Fallback activation

- Evidence manifest

- Notifications

- Blocked-status/access record

- Restart criteria

### **F. Duckworks system-specific notes**

**DuckTalent AI —** Current baseline is already Do Not Deploy; any discovered production instance should be suspended and investigated as unauthorized use.

**WingInspect Vision —** Fallback is qualified human inspection; capacity and traceability must be sufficient.

**QuackBot —** Fallback may be human customer support and a clear service notice rather than an unvalidated AI substitute.

| **TABLETOP PROMPT.** A vendor-hosted AI cannot be fully disabled from Duckworks’ admin console during an active incident. What alternative containment options should already exist in the architecture and contract? |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## **RB-15 — AI Retirement / Vendor Exit**

| **PURPOSE.** Decommission an AI system or third-party service without leaving orphaned data, credentials, integrations, models, indexes, logs, contractual obligations or unmanaged business dependency. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Field**         | **Runbook position**                                                                                                                                                       |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primary trigger   | Business decision to retire/replace system, vendor termination/deprecation, unacceptable residual risk, failed remediation, end of pilot, or lifecycle completion.         |
| Primary lead      | System Owner + Procurement for third-party services                                                                                                                        |
| Mandatory support | Technical Owner; AI Governance; CISO; DPO; Legal; Records/Data Owners; Business Continuity                                                                                 |
| Primary systems   | All AI systems and vendor services                                                                                                                                         |
| Related playbooks | PB-12, PB-04, PB-13                                                                                                                                                        |
| Target response   | Capability removed, data/credentials/integrations handled, evidence retained appropriately, vendor obligations closed, users migrated and inventory status set to Retired. |

### **A. Entry conditions and immediate guardrails**

- Define retirement scope: system, models, endpoints, datasets, indexes, credentials, integrations, users, downstream dependencies, vendor contracts and retained evidence.

- Identify replacement/fallback where business process still requires the function.

| **DO NOT.** Mark a system “retired” merely because users stopped opening the application. Hidden APIs, scheduled jobs, extensions, indexes and vendor data can persist. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### **B. Executable procedure**

| **\#** | **Action**                                                                                                                                                          | **Owner**                       | **Required evidence / record**        | **Decision / hand-off**                                     |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|---------------------------------------|-------------------------------------------------------------|
| 1      | Approve retirement decision and effective date; identify business continuity/replacement needs.                                                                     | Business Owner                  | Retirement decision                   | Critical dependency requires transition plan.               |
| 2      | Inventory technical assets and dependencies: endpoints, models, repositories, vector stores, connectors, API keys, service accounts, pipelines and scheduled tasks. | Technical Owner                 | Retirement asset checklist            | Unknown dependency blocks final closure.                    |
| 3      | Plan data disposition: return, archive, delete, anonymize or retain according to approved legal/records/privacy requirements.                                       | Data Owner + DPO/Legal          | Data disposition plan                 | Do not invent retention periods in this runbook.            |
| 4      | Exercise vendor exit rights, obtain data/export where needed and request deletion/termination evidence where contractually available.                               | Procurement + Legal             | Vendor exit record                    | Unverified vendor deletion remains explicit residual issue. |
| 5      | Disable integrations, revoke credentials/tokens, terminate accounts and remove network/application access.                                                          | IT/Cloud + Technical Owner      | Decommission logs                     | Validate no orphaned credentials remain.                    |
| 6      | Remove or quarantine model/data/index artifacts and document what is retained for evidence or reproducibility.                                                      | Technical Owner + Records Owner | Artifact disposition record           | Preserve evidence needed for audits/incidents/legal holds.  |
| 7      | Notify users and update procedures so the retired system is no longer referenced or reintroduced informally.                                                        | Business Owner                  | User communication / procedure update | Shadow re-adoption risk may require RB-05 controls.         |
| 8      | Close monitoring, alerts and support only after confirming no production calls remain.                                                                              | Technical Owner                 | Traffic/log verification              | Unexpected calls indicate hidden dependency.                |
| 9      | Update QuackTrack to Retired with final evidence location, exit issues and retention owner.                                                                         | AI Governance Lead              | Inventory closure record              | Retired status must remain auditable.                       |

### **C. Escalation and stop criteria**

- Vendor refuses data export/deletion/cooperation expected under contract.

- Hidden dependency means retirement would disrupt safety/critical operations.

- Legal hold or investigation requires preserving data/artifacts.

- Users continue using personal accounts or replacement shadow AI after retirement.

### **D. Exit criteria**

- No authorized production use remains.

- Credentials/integrations/endpoints are disabled.

- Data/model/index disposition is completed or formally tracked.

- Vendor exit obligations are closed or residual issues documented.

- Inventory is Retired with evidence and owner.

### **E. Minimum evidence package**

- Retirement approval

- Asset/dependency checklist

- Data disposition

- Vendor exit/deletion evidence

- Credential/integration revocation

- Traffic verification

- User communication

- QuackTrack closure

### **F. Duckworks system-specific notes**

**Vendor-neutrality —** Exit requirements should be designed before purchase; retirement is not only a technical uninstall.

**Evidence —** Some artifacts may need retention for governance/audit even when production data is deleted; retention decisions require records/legal/privacy input.

**Shadow AI —** If users replace a retired service with unapproved public AI, route discovery through RB-05.

| **TABLETOP PROMPT.** Duckworks retires a hosted GenAI service but discovers an old API key is still used by a nightly script. What evidence is needed before the inventory can legitimately show “Retired”? |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## **RB-16 — Evidence Preservation / Assurance Response**

| **PURPOSE.** Produce a defensible, traceable evidence package for governance challenge, Internal Audit, incident investigation, management review or legal/regulatory assessment without rewriting history or overstating control operation. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Field**         | **Runbook position**                                                                                                                                                                             |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primary trigger   | Audit request, governance committee challenge, incident investigation, legal/privacy review, certification/readiness exercise or management request to prove a material AI control/decision.     |
| Primary lead      | AI Governance Lead                                                                                                                                                                               |
| Mandatory support | Control Owner; Technical Owner; CISO; DPO/Legal; Procurement; Internal Audit as independent requester                                                                                            |
| Primary systems   | All governed AI and governance processes                                                                                                                                                         |
| Related playbooks | PB-13 and all source playbooks/runbooks                                                                                                                                                          |
| Target response   | Evidence request mapped to controls/decisions, original records preserved, gaps disclosed, evidence packaged with provenance and ownership, and remediation initiated for missing/weak evidence. |

### **A. Entry conditions and immediate guardrails**

- Clarify the question being evidenced: design, implementation, operating effectiveness, decision rationale, legal screening, incident response, monitoring or change control.

- Internal Audit remains independent and does not become the owner of evidence-producing controls.

| **DO NOT.** Backfill, recreate or date documents to make a control appear to have operated when contemporaneous evidence does not exist. Mark retrospective reconstruction explicitly. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### **B. Executable procedure**

| **\#** | **Action**                                                                                                                           | **Owner**                         | **Required evidence / record** | **Decision / hand-off**                                                          |
|--------|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|--------------------------------|----------------------------------------------------------------------------------|
| 1      | Record evidence request, requester, scope, system/control IDs, period and due date.                                                  | AI Governance Lead                | Evidence request log           | Ambiguous request is clarified before bulk collection.                           |
| 2      | Map each requested assertion to the expected evidence source and control owner.                                                      | AI Governance Lead                | Evidence map                   | One artifact may support multiple assertions, but relevance must be explicit.    |
| 3      | Collect original/current records from authoritative systems or controlled repositories.                                              | Control Owners                    | Evidence files/exports         | Preserve metadata where useful.                                                  |
| 4      | Validate provenance: creator/system, timestamp, version, completeness, environment and link to AI ID.                                | AI Governance + Control Owner     | Provenance checklist           | Screenshots without context may be weak evidence.                                |
| 5      | Separate evidence of design from evidence of operation; identify sample period/frequency where operating effectiveness is requested. | AI Governance / Assurance Liaison | Evidence classification        | A policy alone does not prove operation.                                         |
| 6      | Identify gaps, expired evidence, contradictory records and assumptions; do not conceal them.                                         | AI Governance + Risk              | Gap log                        | Material gaps can affect residual risk/control effectiveness.                    |
| 7      | Package evidence with index, concise explanation, confidentiality classification and unresolved limitations.                         | AI Governance Lead                | Evidence pack/index            | Avoid unnecessary personal/confidential data in portfolio copies.                |
| 8      | Provide pack to requester through approved channel; record questions and supplemental evidence.                                      | AI Governance Lead                | Submission record              | Internal Audit evaluates independently.                                          |
| 9      | Route material control/evidence gaps to remediation and reassessment.                                                                | Control Owner + Risk              | Remediation plan               | If prior approval relied on unsupported control, reassess current residual risk. |

### **C. Escalation and stop criteria**

- Requested evidence suggests a control was claimed but not actually implemented.

- Records conflict with approved purpose, release scope or legal/risk classification.

- Evidence contains sensitive personal/confidential information requiring restricted handling.

- Critical/High decision cannot be traced from inventory to assessment, treatment, approval and monitoring.

- Request may be associated with legal hold, regulator or investigation; engage Legal before altering or deleting records.

### **D. Exit criteria**

- Evidence request is fully indexed and responded to.

- Provenance and limitations are documented.

- Gaps have owners and due dates.

- Any risk/approval implications are reassessed.

- Evidence location and access are recorded.

### **E. Minimum evidence package**

- Evidence request log

- Control-to-evidence map

- Original source records

- Provenance checklist

- Evidence index

- Gap log

- Submission record

- Remediation/reassessment actions

### **F. Duckworks system-specific notes**

**Acceptance criteria —** Duckworks’ acceptance principle is: if a reviewer cannot point to the evidence, the criterion is not met.

**Internal Audit —** Penelope Duckins may independently test design and operating effectiveness but should not create or operate first/second-line controls.

**Portfolio boundary —** Externally shareable portfolio evidence should remain fictional/synthetic and should not contain real employer, customer, applicant or government confidential data.

| **TABLETOP PROMPT.** Internal Audit asks for proof that PondGPT access controls operated for the previous quarter. Which evidence shows design, which shows operation, and what happens if only a current configuration screenshot exists? |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## **3. Cross-Runbook Quick Response Checklists**

### **3.1 First 15 minutes of a material AI event**

- Create an incident/change record and identify the AI system or temporary discovery ID.

- Stop or bound ongoing harm before attempting a complete root-cause analysis.

- Preserve original evidence: logs, model/service/version, configuration, prompt/output, data source and decision context.

- Identify affected domains: security, privacy, people/rights, product safety, customer, vendor, legal/contract.

- Assign P1-P4 incident priority separately from enterprise risk rating.

- Notify the business owner and correct specialist lead; record the notification.

- Select the specialist runbook and define who has restart/closure authority.

### **3.2 Restart authorization checklist**

| **Question**                                        | **Required answer before restart**                                                 |
|-----------------------------------------------------|------------------------------------------------------------------------------------|
| Is the harmful condition contained?                 | Yes, with evidence of technical/operational containment.                           |
| Is affected scope sufficiently bounded?             | Yes, or remaining uncertainty is explicitly accepted by authorized decision-maker. |
| Are required specialists complete?                  | Security/privacy/legal/HR/safety/vendor reviews complete where triggered.          |
| Were critical assumptions invalidated?              | If yes, RB-12 reassessment completed.                                              |
| Are corrective controls implemented?                | Implemented and evidenced; not merely planned.                                     |
| Has validation addressed the observed failure mode? | Yes, with exact post-change configuration/version identified.                      |
| Is safe fallback available?                         | Yes for material/consequential use.                                                |
| Is monitoring ready to detect recurrence?           | Yes, with named alert owner.                                                       |
| Who authorized restart?                             | Named authorized person/committee and timestamp recorded.                          |

### **3.3 Minimum incident evidence manifest**

- System ID and environment

- Reporter and timeline

- Model/provider/version/configuration

- Relevant inputs/prompts/retrieved content and outputs

- User/session/service identity

- Data classifications and affected records where applicable

- Logs/tool calls/integration events

- Containment actions and who executed them

- Specialist notifications and decisions

- Root-cause analysis

- Corrective action and validation

- Risk reassessment

- Restart/closure approval

## **4. Runbook Governance and Maintenance**

| **Control**                | **Duckworks rule**                                                                                                                                                |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Owner                      | AI Governance Lead maintains the pack; each specialist function owns the accuracy of its operational steps.                                                       |
| Review cadence             | At least annual review and event-driven review after material incident, control failure, architecture change, vendor/model change or governance framework update. |
| Local technical procedures | Vendor-/platform-specific commands, console actions and automation scripts must be maintained by the Technical Owner and tested in the relevant environment.      |
| Tabletop testing           | P1/P2 runbooks and safety/rights/data scenarios should be exercised periodically with evidence of participants, decisions, gaps and corrective actions.           |
| Version control            | Changes must record version, date, approver, affected runbooks and reason. Superseded versions remain traceable.                                                  |
| Evidence quality           | A runbook is not considered operational merely because it exists. Duckworks needs training, ownership, tooling, tested fallback and execution evidence.           |

### **4.1 Suggested tabletop exercise schedule**

| **Quarter** | **Scenario**                                            | **Primary runbooks**       | **Success evidence**                                                    |
|-------------|---------------------------------------------------------|----------------------------|-------------------------------------------------------------------------|
| Q1          | PondGPT cross-user confidential data retrieval          | RB-02, RB-04, RB-13, RB-14 | Containment time, access scope, evidence quality, restart decision.     |
| Q2          | WingInspect false-negative defect escape                | RB-10, RB-06, RB-09, RB-14 | Human fallback, product traceability, validation and safety escalation. |
| Q3          | QuackBot indirect prompt injection via knowledge source | RB-03, RB-02, RB-07        | Source isolation, tool/data boundary test, retest evidence.             |
| Q4          | Vendor model change + outage + changed data-use terms   | RB-11, RB-12, RB-15        | Dependency mapping, contractual evidence, fallback and exit readiness.  |

## **5. Traceability to Duckworks Project Artifacts**

| **Source artifact**                          | **How this pack uses it**                                                                                                                                  |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Business Scenario                            | Uses the seven-system baseline, governance mandate, material risk themes and controlled-innovation objective.                                              |
| In-Scope / Out-of-Scope                      | Keeps runbooks at governance/operational-procedure level and avoids claiming production technical testing, legal opinions or certification.                |
| Project Objectives                           | Implements intake, risk/impact, third-party, shadow AI, monitoring, reassessment, evidence and independent assurance objectives.                           |
| Stakeholder Register                         | Uses named governance roles, first/second/third-line responsibilities and system/domain owners.                                                            |
| Assumptions Register                         | Treats critical assumptions as reassessment triggers; does not convert assumptions into facts.                                                             |
| Acceptance Criteria                          | Preserves current system gates, evidence principle, legal/risk separation, traceability and Internal Audit independence.                                   |
| Risk Classification & Assessment Methodology | Uses intended-purpose-first, scenario-based risk, evidence-based control credit, separate legal triage, residual-risk and reassessment rules.              |
| Public Frameworks, Legislation & Guidance    | Recognizes binding law vs regulatory guidance vs voluntary standards/frameworks; runbooks use “where applicable” and route legal conclusions to Legal/DPO. |
| Operational Playbook Pack                    | Runbooks sit beneath the playbooks and provide task-level execution for recurring operational events.                                                      |

## **6. References and Classification of Requirements**

The following sources inform the Duckworks governance design. Their role is intentionally separated so the runbooks do not imply that voluntary framework alignment equals legal compliance.

| **Category**                                           | **Source / role in this pack**                                                                                                                                                                                             |
|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mandatory legal requirements - applicability dependent | EU Artificial Intelligence Act; GDPR; applicable employment/equality, product safety, cybersecurity and national implementing law. Applicability and duties require system-specific legal analysis.                        |
| Standards / framework guidance                         | ISO/IEC 42001, ISO/IEC 23894, ISO/IEC 42005, ISO/IEC 27001/27005 and NIST AI RMF inform governance, risk, lifecycle, control and evidence practices.                                                                       |
| Technical guidance                                     | ENISA AI cybersecurity guidance, MITRE ATLAS and OWASP GenAI guidance inform AI security threat/response considerations.                                                                                                   |
| Duckworks organizational practice                      | Incident priority, release gates, runbook steps, evidence rules, escalation, suspension, restart and tabletop expectations are internal portfolio design choices unless separately required by applicable law or contract. |
| Project assumptions                                    | Human final authority, specific system architecture, vendor behavior and geographic/product applicability remain assumptions where not validated.                                                                          |

## **7. Portfolio Disclaimer**

Duckworks, Project W.I.N.G., all personnel, committees, systems, datasets, incidents, decisions and evidence referenced in this document are fictional and were created solely for educational and professional portfolio purposes. This runbook pack demonstrates an auditable operational AI governance design. It is not legal advice, a regulatory determination, a production incident-response procedure, a certification claim, or evidence that any named control operates in a real organization.
