# Duckworks GDPR Data Protection Impact Assessment (DPIA) — DuckTalent AI (AI-005)

*Recruitment screening, candidate ranking, and human decision support*

| **Document field**    | **Value**                                         |
|-----------------------|---------------------------------------------------|
| Document ID           | DW-WING-PRIV-01                                   |
| Version               | 1.0                                               |
| Status                | Draft for Governance / Privacy Review             |
| Assessment date       | 9 August 2026                                     |
| Organization          | Duckworks (fictional)                             |
| System                | DuckTalent AI (AI-005)                            |
| Controller assumption | Duckworks - subject to final Legal/DPO validation |
| DPO                   | Delia Duckham                                     |
| Business owner        | Beatrice Van Duck - Chief People Officer          |
| Technical owner       | Dr. Ada Duckfield - Head of Data & AI             |
| Classification        | Portfolio / Synthetic / Non-production            |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Executive DPIA decision</strong></p>
<p>Treat a GDPR DPIA as required before DuckTalent is deployed on the current project assumptions. The proposed processing uses AI to evaluate, compare and rank job applicants and may materially influence access to employment. Production remains blocked until the processing design, lawful basis, data flows, transparency, human oversight, vendor arrangements, data-subject rights, security safeguards, and evidence are validated. If high residual risk remains despite mitigation, prior consultation under GDPR Article 36 must be assessed before processing begins.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Portfolio disclaimer. Duckworks, Project W.I.N.G., all personnel, applicants, systems, datasets, decisions, incidents, risks, controls and evidence in this document are fictional and created solely for educational and professional portfolio purposes. This is not legal advice, a supervisory-authority filing, or evidence of regulatory compliance.

## 1. Executive Summary

DuckTalent AI is a proposed recruitment decision-support capability intended to parse CVs, extract qualifications and experience, compare applicants against pre-approved job criteria, summarize applications, rank candidates and recommend candidates for further human review. It is not intended to make final hiring or rejection decisions autonomously.

The Duckworks readiness assessment already treats DuckTalent as the most consequential governed AI use case because it can influence employment opportunities and creates material fairness, discrimination, transparency, privacy, explainability, automation-bias and contestability concerns. The current governance gate is “Do not deploy in current state”.

| **DPIA question**                                        | **Current conclusion**                                                                                                                                                   |
|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Is personal data processed?                              | Yes - applicant and recruitment data, including derived rankings/summaries.                                                                                              |
| Is high-risk processing likely?                          | Yes on current assumptions; AI-supported systematic evaluation of applicants can materially affect employment opportunity.                                               |
| Is a DPIA required?                                      | Treat as required before deployment; final confirmation must consider the actual deployment and competent supervisory-authority list.                                    |
| Is Article 22 solely automated decision-making intended? | No. Duckworks requires meaningful human review and prohibits autonomous hiring/rejection. De facto automation remains a risk to control.                                 |
| Is a lawful basis confirmed?                             | No. Legal/DPO validation is a blocking action; national employment law and Article 88 context must be reviewed.                                                          |
| Are special-category data intended?                      | No. Such data may appear incidentally in CVs or be inferred; collection/use should be minimized and prohibited unless a lawful exception and safeguards are established. |
| Can processing proceed now?                              | No. Production remains blocked pending closure of the DPIA action plan and the wider DuckTalent governance gates.                                                        |
| When is supervisory prior consultation relevant?         | Where the DPIA shows high risk remaining in the absence of sufficient mitigating measures, Article 36 prior consultation must be assessed before processing.             |

## 2. DPIA Requirement and Legal Basis

This section distinguishes binding GDPR obligations from Duckworks internal governance practice and project assumptions.

| **Source / provision**                   | **Status**                          | **Application to this DPIA**                                                                                                                                                             |
|------------------------------------------|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GDPR Article 35(1)                       | Binding where applicable            | Requires a DPIA before processing where a type of processing, including use of new technologies, is likely to result in high risk to rights and freedoms.                                |
| GDPR Article 35(2)                       | Binding where applicable            | The controller must seek the advice of the DPO, where designated, when carrying out the DPIA.                                                                                            |
| GDPR Article 35(3)(a)                    | Binding example                     | Identifies systematic and extensive evaluation based on automated processing, including profiling, on which legally or similarly significant decisions are based as a DPIA case.         |
| GDPR Article 35(7)                       | Binding content minimum             | Requires description/purposes, necessity/proportionality, risk assessment, and measures/safeguards.                                                                                      |
| GDPR Article 35(9)                       | Binding where appropriate           | Controller should seek the views of data subjects or representatives where appropriate, subject to legitimate protection of business/security interests.                                 |
| GDPR Article 35(11)                      | Binding where necessary             | Requires review when the risk represented by processing changes.                                                                                                                         |
| GDPR Article 36                          | Binding where threshold met         | Prior supervisory-authority consultation is required where high risk would remain absent measures sufficient to mitigate it.                                                             |
| GDPR Article 22                          | Binding where conditions met        | Applies to solely automated decisions with legal or similarly significant effects. DuckTalent is designed to avoid solely automated final decisions, but the boundary must be evidenced. |
| GDPR Article 88 / national law           | Binding / jurisdiction-specific     | Member States may provide specific employment-data rules, including recruitment. Final processing basis and safeguards therefore require jurisdiction-specific review.                   |
| EDPB / WP29 DPIA Guidelines WP248 rev.01 | Regulatory guidance                 | Used to support high-risk screening and DPIA methodology; not a substitute for the GDPR or national supervisory-authority lists.                                                         |
| Duckworks AI Governance Framework        | Internal organizational requirement | Requires proportionate assessment, human oversight, evidence, approval and reassessment for material AI systems.                                                                         |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Applicability conclusion</strong></p>
<p>On the current fictional facts, Duckworks should not rely on a narrow argument that a human signs the final hiring decision to avoid a DPIA. DuckTalent still performs systematic evaluation, ranking and recommendation in a consequential recruitment process. The defensible governance position is to complete the DPIA before deployment and treat any uncertainty as a Legal/DPO action, not as permission to proceed.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 3. Processing Description and Scope

| **Element**      | **DPIA record**                                                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Purpose          | Support recruitment triage and structured comparison by parsing applications, extracting job-relevant information, summarizing applications, ranking candidates and recommending candidates for human review. |
| Data subjects    | External job applicants. Internal mobility, employee performance, promotion, termination, workforce monitoring and task allocation are outside this DPIA unless separately added and reassessed.              |
| Business users   | Recruiters, hiring managers and authorized HR personnel.                                                                                                                                                      |
| Decision role    | Decision support only. Qualified humans retain authority for progression, rejection, interview, offer and hiring decisions.                                                                                   |
| Scale            | Expected enterprise recruitment use is not yet quantified. Applicant volumes, business units, countries and user counts must be confirmed before approval.                                                    |
| Geography        | Duckworks is assumed to operate primarily in the EU/EEA; actual applicant jurisdictions and processing/storage locations remain to be validated.                                                              |
| Technology       | AI/ML components and potentially third-party model/service components. Exact provider/model, hosting architecture and subprocessors are not yet fixed in the portfolio baseline.                              |
| Data sources     | Applicant-submitted CV/application information and approved recruitment records. Public-web scraping, social-media enrichment and unrelated third-party enrichment are not approved within this DPIA.         |
| Downstream use   | Recruitment review and workflow. Use for model training, talent analytics, employee monitoring, performance evaluation or unrelated profiling requires separate approval and reassessment.                    |
| Lifecycle status | Concept / governance assessment. Do not deploy in current state.                                                                                                                                              |

### 3.1 Data-flow narrative

1.  Applicant submits a CV and application information through the approved recruitment channel / ATS.

2.  Authorized recruitment data is made available to the DuckTalent processing layer under defined access controls.

3.  DuckTalent parses the application and derives structured fields, summaries, matching indicators and/or candidate ranking against approved criteria.

4.  An authorized recruiter reviews the source application together with DuckTalent outputs; the AI output is not a final decision.

5.  Recruitment decisions, overrides, material corrections and escalations are recorded in the approved recruitment workflow.

6.  Governance, security and performance logs are retained only to the extent necessary for approved purposes and under a defined retention schedule.

7.  Data is deleted, anonymized or moved to an approved talent-pool process when the recruitment purpose and applicable retention requirements end.

## 4. Personal Data Inventory

| **Data category**                        | **Examples**                                                           | **Purpose**                                      | **Treatment / restriction**                                                                     |
|------------------------------------------|------------------------------------------------------------------------|--------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Identity & contact                       | Name, contact details, location where relevant                         | Application administration and identity matching | Collect only required fields; restrict access.                                                  |
| Employment history                       | Employers, roles, dates, responsibilities                              | Assess job-relevant experience                   | No unrelated background inference.                                                              |
| Education & qualifications               | Degrees, certifications, skills, licences                              | Assess role requirements                         | Verify only where necessary and proportionate.                                                  |
| Application responses                    | Role questions, availability, work authorization where lawful          | Recruitment administration / eligibility         | Question design subject to Legal/HR review.                                                     |
| CV free text                             | Narrative descriptions and attachments                                 | Parsing and summarization                        | May contain unexpected sensitive data; minimize exposure and use.                               |
| Derived data                             | Extracted skills, match indicators, summaries, rank/order              | Recruitment decision support                     | Must be explainable, reviewable and correctable; not treated as objective fact.                 |
| Recruitment decisions                    | Progression, rejection, interview/offer status, reviewer rationale     | Workflow and accountability                      | Human decision rationale should be separable from AI recommendation.                            |
| System/audit data                        | User access, model/version, decision-support output, overrides, errors | Security, assurance, reconstruction              | Minimize content; restrict and retain under defined schedule.                                   |
| Special-category / highly sensitive data | May appear incidentally in CVs or be inferred                          | Not an intended input or ranking factor          | Exclude from scoring/use unless Legal/DPO establish a specific lawful condition and safeguards. |
| Criminal-conviction data                 | Potentially relevant only for certain regulated roles                  | Not part of baseline use case                    | Do not process in DuckTalent unless separately justified under applicable law and reassessed.   |

## 5. Controller, Processor, and Governance Roles

| **Role**                 | **Duckworks assignment / status**                          | **DPIA responsibility**                                                                                                                       |
|--------------------------|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Controller               | Duckworks - assumed for recruitment purpose/means; confirm | Accountable for GDPR compliance, DPIA, lawful basis, rights, vendor arrangements and final processing decision.                               |
| Business owner           | Beatrice Van Duck - Chief People Officer                   | Owns recruitment purpose, business process, human review, operational controls and treatment actions.                                         |
| DPO                      | Delia Duckham                                              | Provides independent advice on DPIA, privacy risk, rights and regulatory requirements; monitors performance of DPIA.                          |
| General Counsel          | Amelia Duckett                                             | Confirms legal basis, employment-law context, contracts, jurisdiction and legal interpretation.                                               |
| Technical owner          | Dr. Ada Duckfield - Head of Data & AI                      | Provides architecture, data/model lifecycle, testing, monitoring and change evidence.                                                         |
| Security challenger      | Cassandra Duckley - CISO                                   | Reviews access, confidentiality, threat model, logging, integrations, vendor/model supply-chain and security testing.                         |
| AI Governance Lead       | Eleanor Duckford                                           | Coordinates inventory, companion AIA/risk records, evidence, approvals, action tracking and reassessment.                                     |
| Processor / subprocessor | TBD - depends on selected provider/architecture            | Article 28 role, instructions, confidentiality, security, subprocessors, deletion/return and assistance duties to be contractually validated. |
| Internal Audit           | Penelope Duckins                                           | Independent assurance only; does not own or approve first-/second-line privacy controls.                                                      |

## 6. Lawfulness, Fairness, and Transparency

The project source set does not provide enough verified jurisdictional facts to select a definitive Article 6 lawful basis. The DPIA therefore records lawful basis as an open blocking decision rather than inventing one.

| **Issue**                       | **Current position**                                            | **Required evidence / decision**                                                                                                                                                                        |
|---------------------------------|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Article 6 lawful basis          | Not yet confirmed                                               | Legal/DPO assessment considering recruitment purpose, jurisdiction, national employment law and actual processing. Do not default to applicant consent without assessing voluntariness and suitability. |
| Article 9 special categories    | Not intended for ranking/use                                    | Design filtering/minimization; establish process for incidental data; any deliberate processing requires a valid Article 9 condition plus applicable national safeguards.                               |
| Article 10 criminal data        | Not part of baseline                                            | Any future processing requires separate lawful authority and safeguards.                                                                                                                                |
| Transparency Articles 13/14     | Required where applicable                                       | Applicant notice describing controller, purposes, legal basis, data categories/sources, recipients, transfers, retention, rights, AI-assisted evaluation and contact/escalation route.                  |
| Article 22 boundary             | Solely automated final decisions prohibited by Duckworks design | Evidence that humans can review source data, understand limitations, override output, record rationale and are not compelled to follow ranking.                                                         |
| Data accuracy / Article 5(1)(d) | Material because parsing/ranking may be wrong                   | Applicant correction route; recruiter ability to correct extracted data; performance testing across relevant document formats/languages.                                                                |
| Purpose limitation              | Recruitment only                                                | No secondary training, talent analytics or other use without compatibility/legal assessment and governance approval.                                                                                    |
| Storage limitation              | Period not yet defined                                          | Records/legal/HR/DPO must define schedule by purpose and jurisdiction; model/provider copies and backups must follow it.                                                                                |
| International transfers         | Unknown                                                         | Map hosting, support, subprocessors and data locations; apply Chapter V transfer mechanism where required.                                                                                              |

## 7. Necessity and Proportionality Assessment

| **Test**                                               | **Assessment**                                                                                                                                                            | **Required control / evidence**                                                                                                                        |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Defined business need                                  | Duckworks expects growing application volumes and wants to reduce repetitive screening while improving structured comparison. Benefit is a hypothesis, not yet evidenced. | Baseline current process, workload, quality and candidate experience before claiming benefit.                                                          |
| Can the purpose be achieved with less intrusive means? | Possibly in part through ATS rules, structured application forms, recruiter process improvements or narrower AI functions.                                                | Compare alternatives and justify which AI functions add necessary value.                                                                               |
| Data minimization                                      | Risk of over-collecting CV/free-text data and extracting irrelevant attributes.                                                                                           | Approved field list; feature allow-list; suppress/exclude sensitive/unnecessary fields from ranking.                                                   |
| Accuracy                                               | Inaccurate parsing or derived scores can distort opportunity.                                                                                                             | Validation by language/document type/job family; correction pathway; confidence/uncertainty handling.                                                  |
| Human oversight                                        | Necessary because output may materially influence employment.                                                                                                             | Competent reviewer, source-data visibility, override ability, time to review, prohibition on auto-rejection and monitored override patterns.           |
| Transparency                                           | Applicants need meaningful information about processing and routes to exercise rights.                                                                                    | Privacy notice and AI-use disclosure appropriate to actual logic and impact; contact/contest channel.                                                  |
| Retention                                              | Long retention increases exposure and may create incompatible future use.                                                                                                 | Purpose-based retention schedule and deletion verification including vendors/backups where feasible.                                                   |
| Access                                                 | Recruitment data is sensitive and should be limited to authorized roles.                                                                                                  | Role-based access, least privilege, MFA/enterprise controls, logging and periodic review.                                                              |
| Vendor dependency                                      | Third-party model/service may create unverified data use or transfer.                                                                                                     | Due diligence, Article 28 terms as applicable, data-use restrictions, subprocessor review, change notice, deletion/exit terms.                         |
| Monitoring                                             | Without monitoring, drift/errors/automation bias may persist.                                                                                                             | Accuracy, correction, override, complaints, fairness signals, incidents and vendor/model change monitoring with thresholds approved before production. |

## 8. Risk Assessment to Rights and Freedoms

This DPIA assesses risk to applicants and other data subjects. The labels below are DPIA privacy/right-impact judgments and must not be confused with the EU AI Act legal concept of a “high-risk AI system”. They also do not replace the separate Duckworks enterprise AI risk assessment.

| **ID**  | **Risk scenario / potential harm**                                                                                                                                    | **Inherent** | **Key measures**                                                                                                                    | **Target residual**  | **Evidence required**                                   |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------|----------------------|---------------------------------------------------------|
| DPIA-01 | Excessive or irrelevant data extraction - Applicant data beyond job relevance is processed, increasing intrusion and unfair inference.                                | High         | Feature/data allow-list; minimization; exclude irrelevant fields; testing and periodic review.                                      | Medium               | Approved data dictionary; extraction test results.      |
| DPIA-02 | Special-category data captured or inferred - Sensitive information present in CVs or inferred from names, photos, memberships or text is used directly/indirectly.    | High         | Do not intentionally use sensitive attributes; strip/suppress where feasible; proxy analysis; Legal/DPO exception process.          | Medium               | Feature review; model prompts/config; proxy testing.    |
| DPIA-03 | Incorrect parsing / derived data - CV content is misread or qualifications/experience are incorrectly extracted.                                                      | High         | Accuracy validation, source visibility, correction route, uncertainty flags, human review.                                          | Medium               | Validation report; correction logs.                     |
| DPIA-04 | Opaque or inappropriate ranking - Criteria/weights do not reflect approved job requirements or cannot be explained.                                                   | High         | Pre-approved criteria; job analysis; version control; documented rationale; recruiter-facing explanation.                           | Medium               | Criteria approval record; model/version record.         |
| DPIA-05 | Discriminatory / proxy effects - Ranking systematically disadvantages protected or otherwise vulnerable groups through data patterns or proxies.                      | High         | Fairness methodology; bias testing using lawful/synthetic/approved data; proxy review; human challenge; complaint monitoring.       | High until validated | Fairness report; HR/Legal/DPO approval.                 |
| DPIA-06 | Automation bias / de facto automated rejection - Recruiters mechanically follow ranking, making human review ineffective.                                             | High         | No auto-reject; reviewer training; source application visible; override authority; rationale logging; override/reliance monitoring. | Medium-High          | User testing; training; decision logs.                  |
| DPIA-07 | Insufficient applicant transparency - Applicant cannot understand AI involvement, purpose, data use or consequences.                                                  | High         | Clear privacy/AI notice; meaningful description; rights/contact route; change-controlled notices.                                   | Medium               | Approved notice; candidate testing.                     |
| DPIA-08 | Rights cannot be exercised effectively - Access, rectification, restriction, objection or contest requests cannot be fulfilled across AI-derived data/vendor systems. | High         | DSAR mapping; derived-data retrieval/correction; vendor assistance; escalation and SLA under existing privacy process.              | Medium               | Rights procedure test; processor commitments.           |
| DPIA-09 | Unauthorized access / data breach - Applicant CVs, rankings or decisions are exposed to unauthorized users or attackers.                                              | High         | RBAC, least privilege, encryption, logging, secure integration, vulnerability/security testing, incident response.                  | Medium               | Security assessment; access review; logs.               |
| DPIA-10 | Vendor/model data reuse - Provider retains prompts/CVs, trains models, or uses data beyond Duckworks instructions.                                                    | High         | Contractual prohibition/limits; data-use review; enterprise settings; retention/deletion terms; provider evidence.                  | Medium               | DPA/contract; vendor due diligence.                     |
| DPIA-11 | Unmapped international transfers - Applicant data is transferred to third countries without valid safeguards.                                                         | High         | Data-flow/subprocessor map; transfer assessment; lawful Chapter V mechanism; regional hosting where justified.                      | Medium               | Transfer register; SCC/adequacy evidence if applicable. |
| DPIA-12 | Excessive retention / secondary use - Rejected candidate data, rankings or logs persist or are reused for unrelated talent analytics/model training.                  | High         | Retention schedule; deletion; separate consent/legal analysis where new purpose proposed; purpose limitation controls.              | Low-Medium           | Retention policy; deletion evidence.                    |
| DPIA-13 | Uncontrolled model/vendor change - Provider/model update changes scoring behavior, data use or subprocessor chain without reassessment.                               | High         | Change notice; version pinning where possible; regression testing; material-change trigger; approval before rollout.                | Medium               | Change log; reassessment records.                       |
| DPIA-14 | Inability to reconstruct a decision - Duckworks cannot show which version, criteria, input or human action influenced candidate progression/rejection.                | High         | Audit trail proportionate to decision; version/criteria/output/override record; access controls; retention schedule.                | Medium               | Decision/evidence sample; audit-log test.               |
| DPIA-15 | Candidate challenge causes retaliation or hidden disadvantage - Applicant who exercises privacy/contest rights is treated adversely or flagged.                       | Medium-High  | Separate rights-handling from selection criteria; prohibition on adverse use; access separation and monitoring.                     | Low-Medium           | Procedure; access design; complaint review.             |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Current residual-risk conclusion</strong></p>
<p>The current concept-stage evidence is insufficient to demonstrate that the high-risk applicant impacts above are adequately mitigated. Duckworks must therefore maintain the existing “Do Not Deploy” decision. Target residual ratings describe the intended state after controls and evidence; they are not current control effectiveness claims.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 8.1 Related synthetic operating evidence — DT-02

A synthetic `DT-02 — Pre-Deployment Fairness & Adverse-Impact Testing` evidence package is available at [`../../80-operating-evidence/AI-005-ducktalent/`](../../80-operating-evidence/AI-005-ducktalent/).

The package uses no real applicant or protected-characteristic data. It demonstrates how Duckworks could test an approved-feature boundary, identify a deliberately unapproved `Career_Gap_Months` scoring penalty, quantify the resulting matched-pair/group effect, block progression, remediate the feature configuration, and retest the full synthetic population.

**Evidence state:** **Designed → Synthetic technical implementation demonstrated → Synthetic fairness execution demonstrated → Synthetic operation tested**

The package is relevant to `DPIA-05` and action `DP-07` as **design and synthetic test evidence only**. It does not establish a lawful basis for fairness data, actual job relevance, real subgroup performance, legal non-discrimination compliance, or evidence sufficient for the intended real applicant population.

`DP-07` therefore remains open and the DPIA's **DO NOT DEPLOY** decision is unchanged.

## 9. Data-Subject Rights and Human Oversight

| **Requirement**       | **DuckTalent design expectation**                                                                                                                                                      |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Notice                | Applicants receive clear information about Duckworks, recruitment purposes, AI-assisted analysis/ranking, categories/sources of data, recipients, retention, rights and contact route. |
| Access                | Duckworks can identify and provide relevant applicant personal data, including material derived data, subject to applicable limitations and rights of others.                          |
| Rectification         | Applicants can correct inaccurate source data and material derived information; recruitment teams can re-run/review where correction could affect outcome.                             |
| Erasure / restriction | Requests are handled under applicable GDPR conditions, with propagation to relevant processors and systems where required.                                                             |
| Objection             | Where Article 21 applies based on lawful basis, Duckworks can identify, assess and action objections.                                                                                  |
| Article 22 safeguard  | System design prohibits solely automated final hiring/rejection. Human intervention must be real, not ceremonial.                                                                      |
| Contestability        | Applicants have a route to query or contest material AI-supported outcomes and obtain human reconsideration where appropriate.                                                         |
| Human competence      | Reviewers understand system purpose, known limitations, error patterns, fairness/automation-bias risk, and when to disregard/escalate output.                                          |
| Override              | Reviewer can change or ignore ranking without technical or managerial obstruction and can document rationale.                                                                          |
| Stop authority        | Business owner / governance functions can suspend DuckTalent when data protection, fairness, security, performance or oversight controls fail.                                         |

## 10. Security and Privacy-by-Design Measures

- Enterprise identity, role-based access control, least privilege and periodic access recertification for applicant data and AI administration.

- Encryption in transit and at rest where appropriate; secrets and credentials segregated from prompts/application data.

- Approved integrations only; no uncontrolled browser extensions or public GenAI services in the recruitment workflow.

- Input and output controls to reduce prompt injection, malicious attachments, data exfiltration and unauthorized tool execution if generative components are used.

- Segregation between applicant records, model/service configuration, logs, and administrative functions.

- Logging sufficient to reconstruct material actions without indiscriminately retaining full prompt/content histories.

- Secure development/change control, model/version management, vulnerability management and dependency/supply-chain review.

- Data-loss prevention and contractual restrictions against provider model training or unrelated reuse where applicable.

- Retention/deletion controls covering primary storage, caches, exports, test environments and processor copies as far as contractually/technically possible.

- Incident escalation integrated with Duckworks security/privacy processes, including assessment of GDPR breach notification obligations where relevant.

## 11. Consultation, DPO Advice, and Stakeholder Input

| **Consultation**                        | **Status**                                        | **Required output**                                                                                                                        |
|-----------------------------------------|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| DPO advice - Delia Duckham              | Required before approval                          | Written advice on DPIA completeness, lawful basis, rights, minimization, Article 22 boundary, processor/transfer issues and residual risk. |
| General Counsel                         | Required                                          | Employment-law / Article 88 / jurisdiction-specific assessment; legal basis and contractual position.                                      |
| HR / business owner                     | Required                                          | Approved job criteria, decision process, oversight procedure and candidate remedy route.                                                   |
| CISO / Security                         | Required                                          | Threat model, architecture/security review, access/logging and vendor/model supply-chain controls.                                         |
| Procurement / Vendor Assurance          | Required if third party                           | Processor terms, subprocessors, data use, retention, incident notice, audit/evidence and exit arrangements.                                |
| Applicant / representative views        | Recommended where appropriate under Article 35(9) | Structured feedback on notice, usability, accessibility, contestability and perceived impact; document rationale if not sought.            |
| Recruiter / hiring-manager user testing | Required organizational practice                  | Demonstrate comprehension, meaningful review, correction/override capability and acceptable reliance patterns.                             |
| Internal Audit                          | Observer / future assurance                       | May later test design and operating effectiveness; does not approve the DPIA or own controls.                                              |

## 12. Blocking Action and Treatment Plan

| **ID** | **Action**                                                                                                                           | **Owner**                          | **Gate**                         | **Status**  |
|--------|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|----------------------------------|-------------|
| DP-01  | Confirm controller/processor roles, provider/model, hosting, support locations and subprocessors.                                    | Technical Owner + Procurement      | Before design approval           | Open        |
| DP-02  | Confirm Article 6 lawful basis and national employment-law / Article 88 requirements for each deployment jurisdiction.               | General Counsel + DPO              | Before pilot with applicant data | Open        |
| DP-03  | Approve data inventory, feature allow-list, prohibited data/proxy attributes and incidental sensitive-data handling.                 | DPO + HR + Data & AI               | Before validation                | Open        |
| DP-04  | Define and approve applicant privacy / AI transparency notice and contestability route.                                              | DPO + Legal + HR                   | Before applicant processing      | Open        |
| DP-05  | Demonstrate no autonomous rejection/hiring and validate meaningful human review, override and decision logging.                      | HR + AI Governance                 | Before controlled pilot          | Open        |
| DP-06  | Complete parsing/ranking accuracy validation across relevant roles, formats, languages and edge cases.                               | Data & AI + HR                     | Before pilot approval            | Open        |
| DP-07  | Complete fairness/proxy testing methodology and evidence sufficient for the intended applicant population.                           | HR + Data & AI + Legal/DPO         | Before production                | Open — synthetic DT-02 demonstration only |
| DP-08  | Complete security architecture/threat assessment and remediate material findings.                                                    | CISO + Technical Owner             | Before pilot                     | Open        |
| DP-09  | Complete processor/vendor due diligence, Article 28 terms as applicable, data-use/retention/subprocessor/incident/exit controls.     | Procurement + Legal + DPO + CISO   | Before contract/use              | Open        |
| DP-10  | Map international transfers and establish valid safeguards where required.                                                           | DPO + Legal + Procurement          | Before data transfer             | Open        |
| DP-11  | Define purpose-based retention and deletion schedule for applications, derived scores, audit logs and vendor copies.                 | HR + DPO + Records/Legal           | Before production                | Open        |
| DP-12  | Test access, rectification, restriction/erasure and contest workflows across source and derived data.                                | DPO + HR + Technical Owner         | Before production                | Open        |
| DP-13  | Define monitoring thresholds for accuracy, corrections, overrides, complaints, fairness signals, incidents and model/vendor changes. | AI Governance + Data & AI + HR     | Before production                | Open        |
| DP-14  | Obtain written DPO advice and close/accept all DPIA findings within delegated authority.                                             | AI Governance Lead                 | Before approval                  | Open        |
| DP-15  | If high residual risk remains after measures, assess and complete Article 36 prior consultation before processing.                   | DPO + General Counsel + Controller | Before production                | Conditional |

## 13. DPIA Decision and Approval Record

| **Decision field**     | **Current record**                                                                                                                                                                                                                                          |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DPIA outcome           | High-risk processing concerns identified; controls and evidence incomplete.                                                                                                                                                                                 |
| Lifecycle decision     | DO NOT DEPLOY in current state.                                                                                                                                                                                                                             |
| Controlled testing     | Only synthetic or otherwise lawfully approved test data under a documented test plan; real applicant processing requires completion of applicable privacy/legal gates.                                                                                      |
| Condition for approval | Blocking actions closed or formally dispositioned; DPO advice received; lawful basis and data flows verified; privacy/security/fairness/human-oversight evidence supports acceptable residual risk; wider Duckworks AI Governance approval gates satisfied. |
| Article 36             | If high residual risk remains after mitigation, prior consultation must be assessed/completed before processing as required.                                                                                                                                |
| Risk acceptance        | Business owner cannot self-approve unresolved High/Critical enterprise risk. Privacy legal obligations cannot be waived through internal risk acceptance.                                                                                                   |
| Approval validity      | Expires / requires reassessment upon material changes listed in Section 14.                                                                                                                                                                                 |

### 13.1 Draft sign-off

| **Role**                | **Name**          | **DPIA position**                                    | **Status / date** |
|-------------------------|-------------------|------------------------------------------------------|-------------------|
| Business Owner          | Beatrice Van Duck | Confirms purpose, process and controls               | Draft - pending   |
| DPO                     | Delia Duckham     | Provides Article 35 advice / privacy challenge       | Draft - pending   |
| General Counsel         | Amelia Duckett    | Confirms legal basis / employment-law context        | Draft - pending   |
| CISO                    | Cassandra Duckley | Confirms security/privacy control position           | Draft - pending   |
| AI Governance Lead      | Eleanor Duckford  | Confirms evidence, actions and governance gate       | Draft - pending   |
| AI Governance Committee | Cross-functional  | Approves governance treatment when prerequisites met | Not submitted     |

## 14. Review and Reassessment Triggers

- Change in intended purpose, autonomy, decision authority, job family, ranking logic, feature set or criteria weighting.

- New model/provider/version, prompt/configuration, hosting region, subprocessor, integration or data source.

- Use of special-category, criminal-conviction, biometric, inferred-sensitive or other materially different data.

- Expansion to new countries, languages, applicant populations, internal mobility, promotion, performance, termination or workforce monitoring.

- Material accuracy failure, unexpected error distribution, fairness concern, discriminatory outcome, accessibility issue, complaint or successful challenge.

- Evidence that recruiters are mechanically following the rank or cannot meaningfully override the output.

- Privacy/security incident, data leakage, unauthorized access, model/service compromise or vendor incident.

- Change to lawful basis, employment law, supervisory-authority DPIA list, regulatory interpretation or other legal requirement.

- Control failure, evidence expiry, retention breach, rights-handling failure or inability to reconstruct material processing/decision support.

- Any transition from concept/pilot to production or material scale increase.

Under GDPR Article 35(11), the controller must review the DPIA where necessary, at least when there is a change in the risk represented by the processing operations. Duckworks applies this through its broader AI Lifecycle SOP and material-change process.

## 15. Article 35 Minimum-Content Traceability

| **GDPR requirement**                                             | **Where addressed**                                                                                               |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| 35(7)(a) - systematic description and purposes                   | Sections 3-6; processing scope, data flows, roles, purpose, lawful-basis decision.                                |
| 35(7)(b) - necessity and proportionality                         | Section 7; alternatives, minimization, accuracy, oversight, transparency, retention, access and vendor necessity. |
| 35(7)(c) - risks to rights and freedoms                          | Sections 8-10; applicant risk register, rights, human oversight, privacy/security measures.                       |
| 35(7)(d) - measures/safeguards and mechanisms                    | Sections 8-12; technical, organizational, contractual, human and monitoring controls plus evidence plan.          |
| 35(2) - DPO advice                                               | Section 11 and sign-off record.                                                                                   |
| 35(9) - views of data subjects/representatives where appropriate | Section 11; candidate/representative feedback approach or documented rationale.                                   |
| 35(11) - review on change of risk                                | Section 14 reassessment triggers.                                                                                 |
| 36 - prior consultation where high risk remains                  | Sections 12-13; conditional prior-consultation gate.                                                              |

## 16. Minimum DPIA Evidence Pack

- Approved AI Business Use Case and QuackTrack inventory record for AI-005.

- Data-flow / architecture diagram showing systems, interfaces, storage locations, users, processors and subprocessors.

- Record of processing activity (ROPA) link / entry and approved Article 6/Article 9 legal-basis analysis.

- Applicant privacy notice and AI-use transparency text.

- Data dictionary, feature/criteria allow-list, exclusion list and data-minimization rationale.

- Processor / vendor due diligence, contract/DPA, subprocessor list, data-use/retention terms and transfer evidence.

- Security threat model, access-control design, security test results and remediation evidence.

- Parsing/ranking validation, accuracy/error analysis and documented limitations.

- Fairness/proxy testing methodology and results appropriate to the lawful data available and intended population; the synthetic DT-02 package is supporting design/test evidence and is not sufficient production evidence.

- Human-oversight SOP, recruiter training, override mechanism and user-acceptance evidence.

- Data-subject rights test results, including access/rectification and candidate challenge/reconsideration workflow.

- Retention/deletion schedule and evidence that vendor copies/logs follow approved rules.

- Monitoring specification, thresholds, complaint/incident triggers and model/vendor change process.

- DPO advice, Legal review, governance approvals, exceptions/risk decisions and action-closure evidence.

## 17. Source Basis and Limitations

Duckworks project sources used: Business Scenario; Project Objectives; In-Scope / Out-of-Scope; Stakeholder Register; Assumptions Register; Acceptance Criteria; AI Risk Classification & Assessment Methodology; AI Responsible Use Policy; AI Governance Lifecycle SOP; DuckTalent Algorithmic Impact Assessment; DuckTalent EU Fundamental Rights Impact Assessment; and the public frameworks/legislation reference file.

| **Source**                                                                     | **Use in this DPIA**                                                                                                              |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Regulation (EU) 2016/679 (GDPR) - EUR-Lex                                      | Binding legal basis for DPIA content, DPO advice, rights, privacy by design, prior consultation and employment-context screening. |
| EDPB-endorsed WP29 Guidelines on DPIA / high-risk processing (WP248 rev.01)    | Regulatory guidance supporting high-risk screening and DPIA methodology.                                                          |
| EDPB-endorsed Guidelines on automated individual decision-making and profiling | Regulatory guidance supporting interpretation of automated decision-making/profiling risks and safeguards.                        |
| Duckworks source set                                                           | Fictional processing purpose, roles, lifecycle position, risk assumptions, governance gates and evidence requirements.            |

Official public references: GDPR: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng \| EDPB DPIA guidance: https://www.edpb.europa.eu/documents/guideline/data-protection-impact-assessments-high-risk-processing_en \| EDPB automated decision-making/profiling guidance: https://www.edpb.europa.eu/documents/guideline/automated-decision-making-and-profiling_en

### Limitations

- The exact AI vendor/model, hosting, subprocessors, applicant volume, processing geography, data-flow architecture, retention schedule and lawful basis are not verified in the current project evidence.

- The DPIA does not substitute for jurisdiction-specific legal advice, national supervisory-authority DPIA lists, employment-law analysis, a processor contract review, or a real production privacy assessment.

- No real applicant or protected-class data is used in this portfolio. Fairness and privacy validation results must not be fabricated; production evidence would need to be generated lawfully.

- Target controls and target residual risks are planned states and do not represent implemented or effective controls until supported by evidence.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Final portfolio position</strong></p>
<p>DuckTalent AI remains blocked from production. The DPIA should be re-issued as a validated production record only after the open facts are confirmed and the blocking actions have evidence. The document is designed to show the complete privacy-governance reasoning chain without overstating legal certainty or control effectiveness.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
