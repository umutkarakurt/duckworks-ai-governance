# Duckworks AI Change Management Process Documentation Pack

**DUCKWORKS**

AI Change Management Process  
Documentation Pack

Project W.I.N.G. — controlled change, reassessment, release and evidence management for AI systems

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Purpose</strong></p>
<p>Establish a repeatable and auditable process for changing AI systems without silently invalidating prior risk, impact, legal, privacy, security, safety, human-oversight or approval conclusions. The process applies to internally developed AI, third-party AI services, AI-enabled SaaS, model/API changes, data/retrieval changes, configuration changes and material changes in intended use.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| **Field**          | **Value**                                          |
|--------------------|----------------------------------------------------|
| Organization       | Duckworks (fictional)                              |
| Program            | Project W.I.N.G.                                   |
| Document ID        | DW-WING-CM-00                                      |
| Version            | 1.0                                                |
| Status             | Portfolio Baseline                                 |
| Classification     | Portfolio / Synthetic / Non-production             |
| Owner              | AI Governance Lead — Eleanor Duckford              |
| Governance Sponsor | Chief Risk & Compliance Officer — Reginald Duckman |

**Duckworks change principle**

*“No material AI change without impact screening, no changed control without evidence, and no release without an accountable decision.”*

## 1. Document Set and Operating Position

This pack converts Duckworks’ existing reassessment triggers, governance gates and evidence expectations into an operational change-management process. It is intentionally integrated with the existing AI inventory, risk assessment, impact assessment, security, privacy, procurement, incident, human-oversight and monitoring processes.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Important terminology</strong></p>
<p>“Material AI change” and the change classes in this pack are Duckworks internal governance terms. They are not substitutes for statutory concepts such as “substantial modification” or other legal classifications. Where a change may alter legal role, intended purpose, regulatory classification or obligations, Legal/Compliance must perform a separate applicability review.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| **ID** | **Document**                                | **Purpose**                                                                    |
|--------|---------------------------------------------|--------------------------------------------------------------------------------|
| CM-01  | AI Change Management Standard & Process     | Policy-level process, scope, change classes, workflow, approvals and evidence. |
| CM-02  | AI Change Request Form                      | Standard request for planned changes.                                          |
| CM-03  | Change Classification & Impact Screen       | Determine change class, affected domains and required reassessment.            |
| CM-04  | AI Reassessment & Control Impact Checklist  | Identify artifacts, controls and tests invalidated or requiring update.        |
| CM-05  | Change Approval & Release Gate Record       | Document specialist review, approval, conditions and release decision.         |
| CM-06  | Emergency AI Change Procedure               | Controlled fast path for incidents, severe failures and urgent containment.    |
| CM-07  | Third-Party Model / Vendor Change Procedure | Handle vendor model, service, terms, subprocessor and infrastructure changes.  |
| CM-08  | Rollback, Suspension & Recovery Plan        | Define safe rollback, stop-use authority, fallback and restoration.            |
| CM-09  | AI Change Log & Evidence Register           | Maintain auditable change history and evidence traceability.                   |

### 1.1 Governance classification

| **Category**                      | **How this pack treats it**                                                                                                              |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Mandatory legal requirement       | Only where separately determined applicable from verified facts. This process does not convert a legal duty into an internal assumption. |
| Standards/framework guidance      | NIST/ISO and similar sources inform governance design but do not independently create legal obligations or certification.                |
| Duckworks organizational practice | Change classes, workflow, approval gates, evidence fields, internal timelines and escalation rules defined in this pack.                 |
| Project assumption                | Fictional systems, people, technologies and operating details that require validation in a real organization.                            |

## 2. Scope

### 2.1 In scope

- Model/provider/version changes, including hosted foundation-model substitutions.

- Fine-tuning, retraining, parameter, threshold, prompt, system-instruction or guardrail changes.

- Training, validation, reference, retrieval, vector-store, knowledge-base or feature-data changes.

- New connectors, tools, APIs, agents, plugins, permissions or external integrations.

- Changes to intended purpose, user population, affected population, geography, language, business process or decision authority.

- Changes to human review, override, escalation, fallback or stop-use arrangements.

- Changes to monitoring thresholds, logging, content filtering, moderation or security controls.

- Vendor terms, data-use, retention, training, hosting, subprocessor, service-availability or exit changes.

- Changes made in response to incidents, drift, complaints, control failures or regulatory developments.

- Retirement, replacement, rollback and reactivation of AI systems.

### 2.2 Out of scope

- Purely administrative updates that do not affect AI behavior, controls, processing or governance conclusions, except for logging as CM-C0 where appropriate.

- Routine enterprise infrastructure changes already managed under another approved process, unless they change the AI system’s risk, security, privacy, safety, data or availability characteristics.

- Unregistered AI use. Shadow AI must first be discovered, contained and registered before it can enter normal change governance.

- Formal legal opinions, certification, conformity assessment or production penetration testing.

## 3. Change Management Principles

| **Principle**                                 | **Duckworks rule**                                                                                                                              |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Inventory first                               | No material change is processed against an unidentified AI asset. AI ID and current baseline must be known.                                     |
| Intended purpose is a primary trigger         | Changing what the AI is used for may invalidate prior legal, impact and risk conclusions even when the model does not change.                   |
| Control credit requires evidence              | Planned controls cannot justify reduced residual risk. Updated controls must be implemented and evidenced.                                      |
| No silent control degradation                 | Removal, weakening or bypass of security, privacy, human-oversight or safety controls requires explicit review.                                 |
| Reassessment is targeted but complete         | Only affected artifacts need to be reopened, but the screen must consider all material domains.                                                 |
| Risk and legal classification remain separate | A change can be internally Major without creating a statutory high-risk classification, and the reverse can also occur.                         |
| Rollback is part of release readiness         | Material changes require a viable fallback, suspension or recovery path before approval.                                                        |
| Evidence survives the change                  | The organization must be able to reconstruct what changed, why, who approved it, what testing occurred and which prior evidence was superseded. |

## 4. Duckworks AI Change Classification

The change class determines minimum governance intensity. It is not a risk score. Risk is assessed separately using the Duckworks AI Risk Classification & Assessment Methodology.

| **Class**                       | **Definition**                                                                                                                                                                | **Examples**                                                                                                                       | **Minimum approval**                                                                   | **Minimum evidence**                                                                    |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| CM-C0 — Administrative          | No functional or control effect.                                                                                                                                              | Document wording, contact detail, non-functional metadata.                                                                         | System/record owner; log change.                                                       | No reassessment unless screen identifies hidden impact.                                 |
| CM-C1 — Standard                | Limited functional change with no credible material impact on purpose, affected people, safety, rights, sensitive data, autonomy or key controls.                             | UI wording; low-risk configuration change; monitoring dashboard display change.                                                    | Business + Technical Owner; AI Governance notified where relevant.                     | Targeted regression test; update record/evidence.                                       |
| CM-C2 — Material                | Could change model behavior, data processing, security posture, performance, third-party dependency or prior control evidence.                                                | Model version; RAG source; connector; fine-tune; prompt/guardrail; threshold; vendor hosting change.                               | Business + Technical Owner; AI Governance; relevant SMEs; committee if residual High.  | Impact screen; targeted reassessment; testing; approval gate; post-change verification. |
| CM-C3 — Major Governance Change | Changes intended purpose, autonomy, decision authority, materially affected people, safety/employment/rights impact, legal role/classification, or removes critical controls. | DuckTalent ranking logic/features; WingInspect autonomous rejection; FeatherForecast auto-purchasing; QuackBot safety decisioning. | AI Governance Committee + CRCO; specialist review; executive escalation when required. | Full reassessment of affected artifacts; production blocked until approved.             |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Emergency flag</strong></p>
<p>Emergency is not a fifth change class. An urgent containment or restoration change is assigned the normal CM-C0–CM-C3 class plus an “Emergency” flag. The emergency procedure accelerates authorization but does not eliminate logging, post-implementation verification or retrospective governance review.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 4.1 Automatic CM-C3 triggers

- Change in intended purpose or material business decision supported by the AI.

- Increase in autonomy or removal/reduction of human review, override or stop-use authority.

- Use of the AI in employment, applicant ranking, product safety, quality release or other consequential decision where prior approval did not cover the new use.

- Expansion to materially new affected populations, jurisdictions or vulnerable groups.

- Change reasonably capable of altering legal classification or Duckworks’ role in the AI value chain.

- Replacement of a critical model/provider where prior validation, assurance or contractual conclusions no longer apply.

- Removal or material weakening of a critical security, privacy, fairness, safety or human-oversight control.

- Reactivation of a system previously suspended for Critical residual risk or a severe incident.

## 5. End-to-End AI Change Process

| **Step** | **Stage**              | **Required activity**                                                                                           | **Artifact**                      |
|----------|------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------|
| 1        | Initiate               | Raise change request before implementation; identify AI ID and baseline.                                        | CM-02                             |
| 2        | Screen & classify      | Determine CM-C0–C3 and Emergency flag; identify affected domains.                                               | CM-03                             |
| 3        | Determine reassessment | Identify which risk, impact, legal, privacy, security, vendor, safety and oversight artifacts must be reopened. | CM-04                             |
| 4        | Design & plan          | Define implementation, testing, rollback, evidence, owners and monitoring changes.                              | CM-02 / CM-08                     |
| 5        | Specialist review      | Obtain Security, Privacy, Legal, HR, Product Safety, Procurement or other review as triggered.                  | CM-04                             |
| 6        | Test & validate        | Execute risk-proportionate technical, functional, security, fairness, safety, performance and oversight tests.  | Evidence register                 |
| 7        | Approve                | Record formal release decision and conditions at the required authority level.                                  | CM-05                             |
| 8        | Deploy                 | Implement within approved window and configuration.                                                             | Change ticket / deployment record |
| 9        | Verify                 | Confirm production behavior, controls, monitoring and rollback readiness.                                       | CM-05 / CM-09                     |
| 10       | Close & monitor        | Update inventory/version, supersede evidence, track actions, monitor and schedule reassessment.                 | CM-09                             |

### 5.1 Stop conditions

☐ The change differs materially from the approved request.

☐ Required testing fails or evidence is incomplete.

☐ Residual risk becomes Critical or outside delegated appetite.

☐ Human oversight is not available or cannot operate as designed.

☐ A legal/privacy/security/safety reviewer identifies a blocking issue.

☐ Rollback/fallback is unavailable for a change requiring it.

☐ A third-party change invalidates a material contractual or assurance assumption.

☐ Production behavior after release materially deviates from validated behavior.

## 6. Roles, Decision Rights and Segregation

| **Role**                                            | **Responsibility**                                                                                             | **Independence / rule**                                     |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Business / AI System Owner                          | Owns business rationale, intended purpose, operational impact, change request and treatment actions.           | Cannot self-approve High/Critical residual risk.            |
| Technical Owner / Data & AI                         | Owns technical design, versioning, implementation, test evidence, monitoring and rollback.                     | Cannot determine legal classification alone.                |
| AI Governance Lead — Eleanor Duckford               | Runs classification, coordinates reassessment, maintains change log/evidence and prepares committee decisions. | Second-line coordination/challenge.                         |
| CRCO — Reginald Duckman                             | Governance sponsor; approves/escalates material risk decisions according to authority.                         | Cannot replace specialist Legal/Privacy/Security judgments. |
| CISO — Cassandra Duckley                            | Reviews AI security, access, integration, prompt/RAG, supply-chain and incident implications.                  | Mandatory where security trigger is present.                |
| General Counsel — Amelia Duckett                    | Reviews contractual/legal implications, legal role/classification and material regulatory changes.             | Legal interpretation separate from risk score.              |
| DPO — Delia Duckham                                 | Advises on personal-data processing, DPIA need, retention, rights and transfer implications.                   | Independent privacy role preserved.                         |
| Head of Data & AI — Dr. Ada Duckfield               | Provides model/data architecture and validation evidence.                                                      | Technical SME.                                              |
| Procurement & Vendor Assurance — Percival Duckworth | Coordinates supplier change notices, due diligence, contract and exit impacts.                                 | Required for third-party AI changes.                        |
| HR / CPO — Beatrice Van Duck                        | Mandatory domain review for workforce/recruitment changes.                                                     | Enhanced review for DuckTalent.                             |
| Product Safety & Quality — Quentin Duckwell         | Mandatory review where product quality/safety may change.                                                      | Required for relevant DuckDesign/WingInspect changes.       |
| Internal Audit — Penelope Duckins                   | May independently assess the process and evidence.                                                             | Does not own or approve first/second-line controls.         |

### 6.1 Minimum approval matrix

| **Change class** | **Minimum approver(s)**                          | **Specialist review**                                                              | **Committee**                                             |
|------------------|--------------------------------------------------|------------------------------------------------------------------------------------|-----------------------------------------------------------|
| CM-C0            | Record owner / Technical Owner                   | None unless screen indicates hidden impact                                         | No                                                        |
| CM-C1            | Business Owner + Technical Owner                 | AI Governance as needed                                                            | Only if risk or gate changes                              |
| CM-C2            | Business Owner + Technical Owner + AI Governance | Security/Privacy/Legal/HR/Safety/Procurement as triggered                          | Yes where residual High, gate changes, or policy requires |
| CM-C3            | AI Governance Committee + CRCO                   | All triggered specialists; executive escalation where Critical or outside appetite | Yes                                                       |

## 7. Reassessment Trigger Matrix

| **Trigger**                                         | **Default class** | **Artifacts/domains to reopen**                                                                | **Reassessment**               |
|-----------------------------------------------------|-------------------|------------------------------------------------------------------------------------------------|--------------------------------|
| Intended purpose / business decision                | CM-C3             | Inventory, legal triage, AIA, risk assessment, human oversight, approval gate                  | Mandatory                      |
| Autonomy / decision authority                       | CM-C3             | AIA, risk, human oversight, legal, safety/HR as applicable                                     | Mandatory                      |
| Model/provider/version                              | CM-C2 or C3       | Technical validation, risk, security, vendor evidence; legal if role/classification may change | Risk-based                     |
| Training/fine-tuning data                           | CM-C2 or C3       | Data governance, privacy, fairness, security, model validation                                 | Risk-based                     |
| RAG / knowledge source                              | CM-C2             | Data access, privacy, security, prompt/RAG testing, content quality                            | Mandatory for material sources |
| Connector/API/tool/agent                            | CM-C2 or C3       | Security, permissions, data flow, third party, human oversight                                 | Mandatory                      |
| Threshold / decision rule                           | CM-C2 or C3       | Performance, false positive/negative, fairness/safety, operational impacts                     | Mandatory                      |
| User / affected population                          | CM-C2 or C3       | AIA, privacy, accessibility, legal, human oversight                                            | Mandatory                      |
| Geography / jurisdiction                            | CM-C2 or C3       | Legal/privacy applicability, notices, transfers, language performance                          | Mandatory                      |
| Guardrail / filter / system prompt                  | CM-C2             | Security, harmful-output, red-team/regression tests                                            | Mandatory                      |
| Human oversight / fallback                          | CM-C3             | Oversight standard, training, approval, risk                                                   | Mandatory                      |
| Monitoring / logging                                | CM-C1 to C3       | Monitoring standard, privacy/security, incident detection                                      | Risk-based                     |
| Vendor terms / retention / training / subprocessors | CM-C2 or C3       | Procurement, Legal, Privacy, Security, DPA/contract, exit                                      | Mandatory                      |
| Incident / drift / complaint / control failure      | CM-C2 or C3       | Risk assessment, incident record, relevant specialist review                                   | Mandatory                      |
| Legal/regulatory change                             | CM-C2 or C3       | Applicability review and affected governance artifacts                                         | Mandatory when relevant        |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Evidence rule</strong></p>
<p>A prior approval does not automatically transfer to the changed system. The change owner must identify which prior evidence remains valid, which evidence is superseded, and which controls require new operating evidence before release.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 8. Risk-Proportionate Change Validation

| **Validation**        | **When required**                                                         | **Minimum focus**                                                                        | **Evidence**                               |
|-----------------------|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------|
| Functional/regression | All functional changes                                                    | Expected behavior, prohibited behavior, error paths, integration regression              | Test results + defects                     |
| Model/performance     | Model/version/retrain/threshold changes                                   | Accuracy, robustness, drift baseline, error distribution, edge cases                     | Validation report                          |
| Security              | LLM/RAG/connectors/permissions/vendor model changes                       | Prompt injection, data leakage, access boundaries, abuse resistance, supply chain        | Security assessment                        |
| Privacy/data          | New personal/sensitive data, retention, training, transfers, data sources | Minimization, purpose, access, retention, rights, transfer path                          | Privacy review / DPIA update if applicable |
| Fairness / rights     | People-impacting changes                                                  | Feature/criterion changes, group impacts, accessibility, contestability, automation bias | Fairness/impact evidence                   |
| Safety / quality      | Product/quality-impacting changes                                         | False negative/positive, unsafe output, failure modes, human fallback                    | Safety/quality validation                  |
| Human oversight       | Any change to recommendation/decision role                                | Reviewer competence, visibility, override, escalation, stop authority                    | Oversight test / sign-off                  |
| Resilience / rollback | CM-C2/C3                                                                  | Fallback, recovery, provider outage, version rollback, data restoration                  | Rollback test / BCP evidence               |

## 9. CM-02 — AI Change Request Form

**Change request ID:** DW-CHG-\[AI ID\]-\[NNNN\]

**AI system / AI ID:** \[Complete\]

**Requester:** \[Complete\]

**Business Owner:** \[Complete\]

**Technical Owner:** \[Complete\]

**Requested deployment window:** \[Complete\]

**Related vendor / model / service:** \[Complete\]

**Current approved version / baseline:** \[Complete\]

**Proposed version / baseline:** \[Complete\]

**Emergency flag:** Yes / No

### 9.1 Change description

**Business reason / expected value:** \[Describe why the change is needed\]

**Technical description:** \[Describe exactly what will change\]

**Components affected:** \[Model / prompt / data / RAG / integration / access / UI / monitoring / vendor / other\]

**Intended purpose changing?:** Yes / No — explain

**Human decision authority changing?:** Yes / No — explain

**Affected people / users changing?:** Yes / No — explain

**Data categories changing?:** Yes / No — explain

**Third-party relationship changing?:** Yes / No — explain

### 9.2 Implementation plan

☐ Implementation steps defined

☐ Configuration/version identifiers recorded

☐ Test environment identified

☐ Production deployment steps defined

☐ Rollback / suspension steps defined

☐ Post-release monitoring window defined

☐ Evidence owners assigned

### 9.3 Requested governance outcome

☐ Approve for implementation

☐ Approve restricted pilot only

☐ Approve with conditions

☐ Hold pending evidence

☐ Reject / redesign

☐ Emergency containment only

## 10. CM-03 — Change Classification & Impact Screen

| **\#** | **Screening question**                                                                                   | **Classification rule**                                                   |
|--------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| 1      | Does the change alter intended purpose, autonomy or formal decision authority?                           | If Yes → CM-C3                                                            |
| 2      | Could it materially affect employment, fundamental rights, product safety/quality or a vulnerable group? | If Yes → normally CM-C3                                                   |
| 3      | Does it replace the model/provider or materially change model behavior?                                  | If Yes → CM-C2; CM-C3 if prior legal/safety/rights conclusions may change |
| 4      | Does it introduce/retrain/fine-tune using new data, features or knowledge sources?                       | If Yes → CM-C2/C3                                                         |
| 5      | Does it add a connector, tool, agent, API, permission or data-access path?                               | If Yes → CM-C2/C3                                                         |
| 6      | Does it change human review, escalation, override or fallback?                                           | If Yes → CM-C3                                                            |
| 7      | Does it change security, privacy, moderation, guardrail or monitoring controls?                          | If Yes → CM-C2/C3                                                         |
| 8      | Does it expand users, affected groups, countries, languages or business processes?                       | If Yes → CM-C2/C3                                                         |
| 9      | Does it alter vendor data use, retention, training, hosting, subprocessors, terms or resilience?         | If Yes → CM-C2/C3                                                         |
| 10     | Does it respond to a material incident, drift, complaint or control failure?                             | If Yes → CM-C2/C3 and link incident                                       |
| 11     | Could it alter legal/regulatory applicability or Duckworks’ legal role?                                  | If Yes → Legal review + CM-C3 unless Legal determines otherwise           |
| 12     | Is the change demonstrably non-functional and unable to alter prior control/risk conclusions?            | If Yes and all above No → CM-C0/C1                                        |

### 10.1 Domain impact flags

☐ Security

☐ Privacy / personal data

☐ Data governance / IP

☐ Fairness / discrimination

☐ Fundamental rights

☐ Human oversight

☐ Safety / physical harm

☐ Reliability / robustness

☐ Transparency / explainability

☐ Third-party / supply chain

☐ Operational / financial

☐ Legal / regulatory

☐ Business continuity

☐ Monitoring / evidence

**Assigned change class:** CM-C0 / CM-C1 / CM-C2 / CM-C3

**Classification rationale:** \[Complete\]

**Emergency flag:** Yes / No

**AI Governance reviewer:** \[Complete\]

**Required specialists:** \[Complete\]

## 11. CM-04 — AI Reassessment & Control Impact Checklist

| **Artifact / control area**     | **Questions to reassess**                                                                                |
|---------------------------------|----------------------------------------------------------------------------------------------------------|
| AI inventory record             | Purpose, lifecycle, model/provider, version, users, affected people, data, integrations, approvals       |
| Risk assessment                 | New scenarios, severity/likelihood, controls, residual/target risk, appetite and treatment               |
| AI impact assessment            | Affected parties, benefits/adverse impacts, autonomy, fairness, accessibility, safety, contestability    |
| Legal/regulatory triage         | Intended purpose, legal role/classification, transparency, applicable law, national/jurisdictional scope |
| Privacy / DPIA                  | Purpose, lawful basis, processor/controller roles, personal data, retention, rights, transfers           |
| Security assessment             | Threat model, prompt/RAG risks, permissions, integrations, model supply chain, logging                   |
| Model/system documentation      | Model card/system card, limitations, data, performance, configuration, version                           |
| Human oversight record          | Reviewer role, authority, competence, override, escalation, stop-use, automation-bias safeguards         |
| Vendor due diligence / contract | Security, privacy, data use, training, retention, subprocessors, change notice, resilience, exit         |
| Safety / quality validation     | Failure modes, false negatives/positives, acceptance criteria, fallback                                  |
| Monitoring plan                 | KPIs/KRIs, drift, incidents, complaints, overrides, thresholds, alert routing                            |
| Incident / problem record       | Link cause, remediation, lessons learned and recurrence controls where applicable                        |
| Business continuity / rollback  | Fallback, provider outage, model rollback, restoration dependencies                                      |

### 11.1 Evidence disposition

| **Existing evidence ID** | **Status**                           | **Reason** | **Replacement / new evidence** | **Owner** |
|--------------------------|--------------------------------------|------------|--------------------------------|-----------|
| \[EV-001\]               | Valid / Partially valid / Superseded | \[why\]    | \[new EV\]                     | \[owner\] |
| \[EV-002\]               | Valid / Partially valid / Superseded | \[why\]    | \[new EV\]                     | \[owner\] |
| \[EV-003\]               | Valid / Partially valid / Superseded | \[why\]    | \[new EV\]                     | \[owner\] |

## 12. CM-05 — Change Approval & Release Gate Record

**Change request ID:** \[Complete\]

**AI system / AI ID:** \[Complete\]

**Change class:** \[Complete\]

**Emergency flag:** \[Complete\]

**Target environment:** Pilot / Production / Other

**Current governance gate:** \[Complete\]

**Requested governance gate:** \[Complete\]

**Current residual risk:** \[Complete\]

**Post-change residual risk:** \[Complete\]

**Target residual risk:** \[Complete\]

### 12.1 Gate readiness

☐ Change matches approved design and scope.

☐ Required risk/impact/legal/privacy/security/safety reassessments are complete.

☐ Required tests passed or exceptions are explicitly approved.

☐ Human oversight remains effective and trained/authorized personnel are available.

☐ Rollback / suspension route is validated.

☐ Monitoring and alert thresholds reflect the changed system.

☐ Documentation and inventory fields are updated.

☐ Vendor/contract/DPA changes are approved where applicable.

☐ Evidence package is complete and traceable.

☐ No unresolved Critical residual risk is being treated as routine approval.

### 12.2 Specialist sign-off

| **Function**                   | **Required?**     | **Decision**         | **Reviewer** | **Conditions / evidence** |
|--------------------------------|-------------------|----------------------|--------------|---------------------------|
| AI Governance                  | Yes for CM-C2/C3  | Approve / Hold / N/A | \[name\]     | \[details\]               |
| Security                       | As triggered      | Approve / Hold / N/A | \[name\]     | \[details\]               |
| Privacy / DPO                  | As triggered      | Approve / Hold / N/A | \[name\]     | \[details\]               |
| Legal                          | As triggered      | Approve / Hold / N/A | \[name\]     | \[details\]               |
| HR                             | People AI         | Approve / Hold / N/A | \[name\]     | \[details\]               |
| Product Safety & Quality       | Safety/quality AI | Approve / Hold / N/A | \[name\]     | \[details\]               |
| Procurement / Vendor Assurance | Third-party AI    | Approve / Hold / N/A | \[name\]     | \[details\]               |

### 12.3 Release decision

☐ Approved

☐ Approved with conditions

☐ Restricted pilot only

☐ Held pending evidence

☐ Rejected / redesign required

☐ Emergency containment implemented; retrospective review required

**Approver / authority:** \[Complete\]

**Approval conditions:** \[Complete\]

**Post-release verification owner:** \[Complete\]

**Verification due:** \[Complete\]

**Next reassessment trigger/date:** \[trigger or scheduled review\]

## 13. CM-06 — Emergency AI Change Procedure

Emergency changes are permitted only to contain, restore or prevent material harm when the normal lead time is not practical. This is a Duckworks internal operating rule and does not waive any applicable legal notification, safety, privacy or other obligations.

| **Step**                 | **Emergency action**                                                                                                                                                                |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1\. Declare              | Incident Commander / CISO / authorized service owner identifies urgent need; link incident or outage.                                                                               |
| 2\. Classify             | Assign normal CM-C class plus Emergency flag; document what normal evidence cannot be completed pre-change.                                                                         |
| 3\. Authorize            | Obtain minimum emergency authority: service/business owner + relevant incident authority; for rights/safety implications, include CRCO/Legal/appropriate specialist where feasible. |
| 4\. Protect              | Prefer reversible containment: disable feature, block connector, revert model, restrict access, route to human fallback.                                                            |
| 5\. Implement            | Deploy the minimum necessary change; preserve before/after configuration and logs.                                                                                                  |
| 6\. Verify               | Confirm containment/restoration and monitor for adverse side effects.                                                                                                               |
| 7\. Record               | Create/complete change record no later than the next business day.                                                                                                                  |
| 8\. Retrospective review | Complete normal reassessment, evidence and approval within five business days or before permanent retention of the change, whichever occurs first.                                  |
| 9\. Close or revert      | Either convert to approved permanent change or rollback/remove emergency configuration.                                                                                             |

### 13.1 Emergency change minimum record

☐ Incident / trigger and severity

☐ AI system and version before change

☐ Reason normal process could not be completed

☐ Change made and exact configuration/version

☐ Authority approving emergency action

☐ Data/security/privacy/safety impact considered

☐ Rollback/fallback

☐ Verification evidence

☐ Temporary controls

☐ Retrospective-review owner and due date

## 14. CM-07 — Third-Party Model / Vendor Change Procedure

Vendor-driven changes can alter Duckworks risk without a traditional internal deployment. Procurement and system owners must therefore treat material vendor notices as change triggers rather than passive communications.

| **Vendor change**                  | **Potential impact**                                         | **Required response**                       |
|------------------------------------|--------------------------------------------------------------|---------------------------------------------|
| Model/service version              | Behavior, capability, guardrails, performance, compatibility | Technical validation + risk/security review |
| Hosting location / architecture    | Data transfer, resilience, access, compliance, latency       | Privacy/Legal/Security + BCP review         |
| Data use / training terms          | Confidentiality, IP, personal data, model improvement        | Legal/Privacy/Procurement review            |
| Retention / deletion               | Data minimization, deletion evidence, incident exposure      | Privacy/Security review                     |
| Subprocessor / model provider      | Supply-chain risk, data flow, contractual coverage           | Vendor assurance + Legal/Privacy/Security   |
| Security controls / certifications | Assurance basis may become stale or weaker                   | Security/vendor re-assessment               |
| API/tool capability                | New actions, permissions, autonomy, data exposure            | CM-C2/C3 technical + governance review      |
| Terms / SLA / support              | Availability, incident response, exit, audit rights          | Procurement/Legal/BCP                       |
| End-of-life / deprecation          | Forced migration, availability, evidence expiry              | Replacement plan + reassessment             |

### 14.1 Vendor notice workflow

1.  Register notice against each affected AI ID.

2.  Determine whether vendor change is administrative, standard, material or major.

3.  Freeze/extend prior version where commercially and technically possible if review is incomplete.

4.  Reassess contract/DPA, vendor due diligence and data-flow assumptions where affected.

5.  Obtain updated security/privacy/assurance evidence.

6.  Retest critical application scenarios before migration when behavior may change.

7.  Update exit/rollback plan if vendor support or version availability changes.

8.  Record final decision and superseded evidence.

## 15. CM-08 — Rollback, Suspension & Recovery Plan

**AI system / AI ID:** \[Complete\]

**Change request ID:** \[Complete\]

**Current baseline / version:** \[Complete\]

**Target baseline / version:** \[Complete\]

**Rollback owner:** \[Complete\]

**Business fallback owner:** \[Complete\]

**Maximum acceptable service disruption:** \[internal target\]

**Data restoration dependency:** \[Complete\]

**Vendor dependency:** \[Complete\]

**Human/manual fallback:** \[Complete\]

### 15.1 Rollback triggers

☐ Critical or unanticipated safety/rights/privacy/security issue.

☐ Material degradation in accuracy, reliability or error distribution.

☐ Loss of expected human review, escalation or access-control behavior.

☐ Unexpected vendor/model behavior outside validated boundaries.

☐ Monitoring or logging failure preventing adequate oversight.

☐ Deployment defect, integration failure or data corruption.

☐ Governance condition breached or required approval invalidated.

### 15.2 Rollback sequence

| **\#** | **Recovery action**                                                             |
|--------|---------------------------------------------------------------------------------|
| 1      | Stop or restrict the affected capability.                                       |
| 2      | Preserve relevant logs, prompts/outputs, configuration and monitoring evidence. |
| 3      | Notify business owner, technical owner and triggered specialist functions.      |
| 4      | Restore approved prior version or activate manual/human fallback.               |
| 5      | Validate data integrity, access controls and service function.                  |
| 6      | Confirm user/customer communication requirements if service behavior changed.   |
| 7      | Open incident/problem record where failure is material.                         |
| 8      | Determine whether re-release requires CM-C2/C3 reassessment.                    |

## 16. CM-09 — AI Change Log & Evidence Register

| **Change ID** | **AI ID**         | **Class** | **Type**               | **Summary** | **Version** | **Decision** | **Owner** | **Evidence** |
|---------------|-------------------|-----------|------------------------|-------------|-------------|--------------|-----------|--------------|
| CHG-0001      | AI-002 QuackBot   | CM-C2     | Model / RAG            | \[summary\] | \[version\] | \[decision\] | \[owner\] | \[EV IDs\]   |
| CHG-0002      | AI-006 PondGPT    | CM-C2     | Connector / access     | \[summary\] | \[version\] | \[decision\] | \[owner\] | \[EV IDs\]   |
| CHG-0003      | AI-005 DuckTalent | CM-C3     | Ranking / intended use | \[summary\] | \[version\] | \[decision\] | \[owner\] | \[EV IDs\]   |

### 16.1 Evidence package minimum

| **Evidence ID** | **Required record**                                                   |
|-----------------|-----------------------------------------------------------------------|
| EV-CM-01        | Approved change request                                               |
| EV-CM-02        | Classification & impact screen                                        |
| EV-CM-03        | Updated/revalidated risk and impact artifacts                         |
| EV-CM-04        | Legal/privacy/security/safety/vendor specialist reviews as applicable |
| EV-CM-05        | Technical design/version/configuration manifest                       |
| EV-CM-06        | Test and validation results                                           |
| EV-CM-07        | Rollback/suspension plan and test evidence                            |
| EV-CM-08        | Release approval and conditions                                       |
| EV-CM-09        | Deployment record                                                     |
| EV-CM-10        | Post-change verification and monitoring                               |
| EV-CM-11        | Superseded evidence references                                        |
| EV-CM-12        | Closure / action completion record                                    |

## 17. System-Specific Change Examples

| **System**         | **Example change**                                                                | **Default class**      | **Required focus**                                                                                                  |
|--------------------|-----------------------------------------------------------------------------------|------------------------|---------------------------------------------------------------------------------------------------------------------|
| DuckDesign AI      | Update hosted generative model while engineer review remains unchanged            | CM-C2                  | Model validation, IP/data, security, regression; engineer review still effective                                    |
| DuckDesign AI      | Allow generated design to flow directly into production without engineer sign-off | CM-C3                  | Purpose/autonomy/safety/human oversight/legal-product review                                                        |
| QuackBot           | Add a new product-support RAG repository                                          | CM-C2                  | Content quality, access, privacy, prompt injection/RAG security, customer safeguards                                |
| QuackBot           | Permit chatbot to give unreviewed safety-critical repair instructions             | CM-C3                  | Safety, intended purpose, human escalation, legal/product impact                                                    |
| FeatherForecast    | Routine retraining with approved data and same decision-support boundary          | CM-C2                  | Data quality, performance/drift, manager approval remains                                                           |
| FeatherForecast    | Automatically issue purchase commitments                                          | CM-C3                  | Autonomy/decision authority, operational/financial controls, oversight                                              |
| WingInspect Vision | Adjust defect-confidence threshold                                                | CM-C2 or C3            | False negatives/positives, quality/safety; C3 if acceptance authority materially changes                            |
| WingInspect Vision | Remove human inspector final acceptance                                           | CM-C3                  | Safety/quality, human oversight, legal/product assessment                                                           |
| DuckTalent AI      | Change ranking features or scoring weights                                        | CM-C3                  | Fairness, discrimination, legal/privacy, explainability, human review                                               |
| DuckTalent AI      | Replace underlying recruitment model/vendor                                       | CM-C3                  | Enhanced fairness/legal/privacy/vendor revalidation; current 'Do Not Deploy' gate remains unless separately changed |
| PondGPT            | Connect a new internal document repository                                        | CM-C2 or C3            | Authorization boundaries, sensitive data, privacy, RAG security; C3 if materially new restricted data/users         |
| PondGPT            | Enable agent to execute administrative actions                                    | CM-C3                  | Autonomy, permissions, security, oversight, audit logs                                                              |
| Unregistered GenAI | Employee switches from one public AI tool to another                              | Not normal change path | Discover, contain and register each material use before approval                                                    |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Current gate preservation</strong></p>
<p>A change request cannot implicitly override an existing Duckworks release restriction. For example, DuckTalent remains “Do Not Deploy,” QuackBot remains blocked pending release gates, and restricted-pilot systems remain restricted until the appropriate governance authority explicitly changes that decision.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 18. Change Management Metrics and KRIs

| **Metric / KRI**                | **Definition**                                        | **Cadence**                      | **Owner**             |
|---------------------------------|-------------------------------------------------------|----------------------------------|-----------------------|
| Change volume                   | Number of AI changes by CM-C0–C3 and system           | Monthly                          | AI Governance Lead    |
| Material-change rate            | % of changes classified CM-C2/C3                      | Monthly                          | AI Governance Lead    |
| Unapproved change rate          | Changes detected without prior approval               | Monthly / immediate for material | CISO + AI Governance  |
| Reassessment completion         | % of triggered reassessments completed before release | Monthly                          | Risk & Compliance     |
| Evidence completeness           | % of CM-C2/C3 changes with complete evidence package  | Monthly                          | AI Governance Lead    |
| Rollback success                | % of tested rollbacks completed successfully          | Quarterly                        | Technical Owners      |
| Emergency change rate           | Emergency changes as % of all changes                 | Monthly                          | Technology + Risk     |
| Emergency retrospective overdue | Count beyond five-business-day internal target        | Weekly                           | AI Governance Lead    |
| Post-change incidents           | Material incidents within defined post-release window | Monthly                          | CISO / Business Owner |
| Vendor notice coverage          | % of material vendor notices registered and assessed  | Quarterly                        | Procurement           |
| Change-related control failures | Count of controls invalidated or failed after change  | Monthly                          | Control Owners        |

## 19. Process Acceptance Criteria

| **ID**   | **Acceptance criterion**                                                                                       |
|----------|----------------------------------------------------------------------------------------------------------------|
| CM-AC-01 | Every material AI change is linked to an AI inventory record and current baseline.                             |
| CM-AC-02 | CM-C2/C3 changes have a completed impact screen before production release.                                     |
| CM-AC-03 | Reassessment scope identifies which prior artifacts/evidence remain valid or are superseded.                   |
| CM-AC-04 | Required specialist reviews are evidenced.                                                                     |
| CM-AC-05 | No CM-C3 change is released through a CM-C0/C1 approval path.                                                  |
| CM-AC-06 | High/Critical residual-risk decisions follow the existing Duckworks governance authority and escalation rules. |
| CM-AC-07 | Human-oversight changes are explicitly assessed rather than treated as ordinary configuration changes.         |
| CM-AC-08 | Third-party material changes trigger vendor/contract/security/privacy review where relevant.                   |
| CM-AC-09 | Rollback or suspension is documented for CM-C2/C3 changes where service risk requires it.                      |
| CM-AC-10 | Post-change verification confirms expected controls and monitoring operate.                                    |
| CM-AC-11 | Emergency changes receive retrospective review within the internal target or are escalated.                    |
| CM-AC-12 | The change log provides traceability from request → assessment → evidence → approval → release → verification. |

## 20. Integration with Existing Duckworks Artifacts

| **Artifact**                                    | **Change-management integration**                                                                                          |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| QuackTrack AI System Inventory                  | Baseline system identity, version, owners, lifecycle and governance state are updated after change.                        |
| AI Risk Classification & Assessment Methodology | Reassessment triggers, residual-risk rules, control evidence and High/Critical approval requirements remain authoritative. |
| AI Impact Assessments                           | Reopened when affected people, rights, safety, autonomy, fairness, transparency or material impacts may change.            |
| AI Governance Operational Playbooks             | Provide scenario-level operating guidance; this process supplies the formal change control path.                           |
| AI Governance Runbooks                          | Incident/runbook actions can trigger emergency changes; permanent fixes return to normal change governance.                |
| AI Vendor Contract / AI DPA                     | Vendor/model, data-use, retention, subprocessor and service changes are reviewed against contract/DPA obligations.         |
| Human Oversight Standard                        | Any changed decision authority, override or fallback must remain compliant with Duckworks oversight expectations.          |
| Monitoring & Reassessment Standard              | Post-change monitoring thresholds and reassessment triggers are updated.                                                   |
| AI Control Library                              | Control mappings/evidence are updated where change affects control design or operation.                                    |

## 21. Recommended Implementation Sequence

| **Phase** | **Action**                                                                                                         | **Owner**                                 |
|-----------|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| Phase 1   | Adopt CM-C0–C3 classification; add change fields to AI inventory and change ticket; train system/technical owners. | AI Governance + Technology                |
| Phase 2   | Integrate CM-03 impact screen and CM-04 reassessment checklist into release workflow.                              | AI Governance + Risk                      |
| Phase 3   | Connect security/privacy/legal/vendor/safety review triggers to existing approval routes.                          | CISO / DPO / Legal / Procurement / Safety |
| Phase 4   | Implement evidence register and change metrics; sample-test CM-C2/C3 records.                                      | AI Governance + Internal Controls         |
| Phase 5   | Run tabletop exercise for emergency AI change and vendor-forced model migration.                                   | CISO + Data & AI + Procurement            |
| Phase 6   | Internal Audit considers AI change management in its risk-based assurance plan without assuming control ownership. | Internal Audit                            |

## 22. Portfolio Disclaimer

Duckworks, Project W.I.N.G., all named people, AI systems, change requests, incidents, evidence, approvals and data in this pack are fictional and created solely for educational and professional portfolio purposes.

This document demonstrates an internal AI change-management design. It is not legal advice, certification evidence, a conformity assessment, or a statement that any particular EU or national legal requirement applies. Any legal conclusion must be based on verified system facts, jurisdiction, intended purpose, organizational role and current law.

References to NIST, ISO/IEC or other governance sources within the wider Duckworks portfolio represent standards/framework guidance unless separately identified as binding law. Internal Duckworks requirements in this pack are organizational practices chosen for control, auditability and proportional governance.
