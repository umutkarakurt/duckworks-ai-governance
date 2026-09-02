# Duckworks Algorithmic Impact Assessment (AIA) — DuckTalent AI (AI-005)

Business, people, rights, privacy, security, reliability, and governance impact assessment

| **Control**                    | **Value**                                             |
|--------------------------------|-------------------------------------------------------|
| Document ID                    | DW-WING-AIA-01                                        |
| Version                        | 1.0                                                   |
| Assessment date                | 9 August 2026                                         |
| Organization                   | Duckworks (fictional)                                 |
| AI system                      | AI-005 - DuckTalent AI                                |
| Business owner                 | Beatrice Van Duck - Chief People Officer              |
| Technical owner                | Dr. Ada Duckfield - Head of Data & AI                 |
| Assessment owner               | Eleanor Duckford - AI Governance Lead                 |
| Specialist reviewers           | General Counsel / DPO / CISO / HR / Risk & Compliance |
| Status                         | Draft - Pre-deployment impact assessment              |
| Current lifecycle gate         | Do not deploy in current state                        |
| Internal impact classification | Critical                                              |
| Classification                 | Portfolio / Synthetic / Non-production                |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Assessment decision</strong></p>
<p>DuckTalent may offer business value by reducing recruiter triage effort and structuring application review, but the current evidence is insufficient to justify use with real applicants. The system can materially influence access to employment and creates significant fairness, privacy, transparency, accessibility, reliability, human-oversight, and security impacts. Duckworks therefore retains the existing DO NOT DEPLOY gate until the blocking controls and evidence in this AIA are completed.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Portfolio disclaimer. Duckworks, Project W.I.N.G., all personnel, applicants, systems, datasets, decisions, risks, controls, metrics, and evidence referenced in this assessment are fictional and created solely for educational and professional portfolio purposes. This document is not legal advice, certification evidence, or a statement of regulatory conformity.

## 1. Executive Determination

DuckTalent AI is a proposed recruitment decision-support system intended to parse CVs, extract job-relevant information, compare applicants against pre-approved criteria, summarize applications, rank candidates, and recommend candidates for further human review. It is not intended to make final hiring or rejection decisions autonomously.

| **Assessment area**            | **Determination**                                                                                                                                                                                                                                      |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Business objective             | Reduce recruiter triage workload and improve the structure and consistency of application review.                                                                                                                                                      |
| Primary affected parties       | External applicants; internal candidates if the system is later used for internal mobility; recruiters and hiring managers.                                                                                                                            |
| Positive-impact potential      | Faster initial review; more structured comparison against role criteria; improved recruiter capacity for substantive review.                                                                                                                           |
| Material adverse-impact themes | Discrimination/proxy bias; inaccurate ranking; privacy/data misuse; opacity; automation bias; inaccessible or non-inclusive processing; weak contestability; security/vendor dependency; scale amplification of errors.                                |
| Evidence maturity              | Low to Moderate. Intended purpose and governance boundaries are documented, but production design, fairness validation, accessibility evidence, vendor/model evidence, human-oversight operating evidence, and monitoring baselines remain incomplete. |
| Internal impact classification | Critical - Duckworks internal governance classification, not an EU AI Act legal classification.                                                                                                                                                        |
| Current decision               | DO NOT DEPLOY with real applicants until blocking actions are closed and formally approved.                                                                                                                                                            |
| Required approval              | AI Governance Committee after Legal, Privacy, HR, Security, Risk & Compliance and relevant technical evidence are complete.                                                                                                                            |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Why an AIA is necessary</strong></p>
<p>The AIA is the Duckworks system-level record for evaluating both beneficial and adverse impacts before deployment and throughout the lifecycle. It complements, but does not replace, the system risk assessment, GDPR DPIA where required, legal classification analysis, security assessment, statistical fairness validation, or the separate EU Fundamental Rights Impact Assessment (FRIA).</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 1.1 AIA status and terminology

“Algorithmic Impact Assessment (AIA)” is Duckworks’ internal portfolio term for a structured AI-system impact assessment. This artifact is a recommended organizational governance practice. It is not presented as a universally mandated legal form and it must not be used to imply certification or statutory conformity.

## 2. Assessment Basis and Source Hierarchy

| **Category**                             | **How it is used in this AIA**                                                                                                                                                                                                            |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 - Mandatory legal requirements         | Potentially applicable legal duties are screened separately and must be confirmed by Legal/Privacy based on actual deployment facts. The AIA does not convert standards or internal controls into legal obligations.                      |
| 2 - Standards / framework guidance       | ISO/IEC 42005:2025 informs lifecycle impact-assessment thinking; NIST AI RMF informs Govern-Map-Measure-Manage orientation; ISO/IEC 23894 informs AI risk-management integration. These are not treated as proof of legal compliance.     |
| 3 - Recommended organizational practices | Duckworks requires affected-party analysis, positive and adverse impact identification, meaningful human oversight, evidence-based controls, monitoring, reassessment, and lifecycle decisions proportionate to impact.                   |
| 4 - Project assumptions                  | Duckworks is fictional and EU-focused; DuckTalent is decision support only; humans retain formal employment decision authority; the portfolio uses fictional/synthetic/public data; material facts must be revalidated before production. |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Legal screening - separate from AIA classification</strong></p>
<p>The current Duckworks source set flags DuckTalent’s recruitment, application filtering, and candidate evaluation purpose for enhanced EU AI Act legal review. The consolidated EU AI Act lists recruitment/selection systems used to analyse/filter applications or evaluate candidates in Annex III point 4(a). This legal screen is separate from Duckworks’ internal Critical impact/risk labels and requires role- and implementation-specific confirmation.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 2.1 Companion governance records

- AI Business Use Case - business purpose, users, decision boundary, expected value and success measures.

- QuackTrack AI System Inventory - ownership, lifecycle, data, provider/model and governance status.

- AI Risk Assessment - scenario-based inherent/current/target residual risk and treatment.

- EU FRIA - fundamental-rights-focused assessment prepared separately for DuckTalent as a voluntary Article 27-aligned governance artifact under the current Duckworks assumptions.

- GDPR DPIA - separate privacy assessment where required based on verified personal-data processing facts.

- AI RACI and Lifecycle SOP - accountability, specialist review, approval, monitoring, escalation and reassessment workflow.

## 3. System and Business Process Profile

| **Field**                | **Current AIA record**                                                                                                                          |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Business process         | Recruitment and talent acquisition                                                                                                              |
| Lifecycle                | Concept / pre-deployment                                                                                                                        |
| AI role                  | Decision support for consequential employment decisions                                                                                         |
| Intended users           | Recruiters and hiring managers                                                                                                                  |
| Primary affected parties | Applicants; internal candidates if later used internally                                                                                        |
| Inputs                   | CVs, application forms, qualifications, employment history, skills, and other approved recruitment information                                  |
| Outputs                  | Candidate summaries, suitability/comparison indicators, ranked shortlist recommendations                                                        |
| Human decision boundary  | Recruiters/hiring managers remain responsible for consequential decisions; automatic rejection or hiring is not permitted in the current design |
| Third-party dependency   | Combination of internal and third-party AI is a project-wide assumption; exact DuckTalent provider/model architecture remains to be validated   |
| Geography                | EU/EEA-focused project assumption; actual deployment jurisdiction must be validated before approval                                             |

### 3.1 Business need and value hypothesis

Duckworks receives a growing number of applications and expects DuckTalent to reduce manual triage effort, structure comparison against job criteria, and help recruiters focus attention on relevant qualifications and experience. These are benefit hypotheses, not realized benefits. The source set contains no validated ROI, time-saving percentage, productivity target, or financial baseline.

| **Outcome**                           | **Candidate measure**                                                                                        | **Evidence position**                                     |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| Recruitment efficiency                | Recruiter review time per application; time-to-shortlist                                                     | Baseline to be established before pilot                   |
| Review consistency                    | Variation in application treatment against approved criteria; reviewer agreement                             | Measurement design required                               |
| Decision quality                      | Ranking error rate; recruiter correction/override rate                                                       | Pre-deployment validation required                        |
| Fairness                              | Selection-rate differences and error distribution across relevant groups where lawful/appropriate to measure | Testing method, lawful data basis and thresholds required |
| Contestability / applicant experience | Challenge, correction, complaint and reconsideration volumes/outcomes                                        | Process design required                                   |

### 3.2 Intended, unsupported, and prohibited uses

| **Intended / permitted in design**                                                                                                                                          | **Unsupported or prohibited in current design**                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parse CVs and extract job-relevant qualifications; summarize applications; compare applicants against pre-approved criteria; recommend candidates for further human review. | Automatic rejection or hiring; facial/emotion/personality inference for suitability; use of protected or sensitive traits without specific lawful and governance justification; opaque vendor criteria Duckworks cannot validate; unrelated applicant-data reuse for model training. |

## 4. AIA Method and Impact Classification

This AIA evaluates impacts rather than merely listing risks. Each impact scenario considers who may be affected, the consequence if the impact occurs, scale/breadth, reversibility, vulnerability of affected persons, degree of human reliance, and the strength of current evidence. The AIA then identifies controls, evidence, monitoring and a lifecycle decision.

| **Impact classification** | **Duckworks internal meaning**                                                                                                                                         |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Low                       | Limited, reversible effect with routine safeguards; no material rights, safety, privacy, security or business consequence expected.                                    |
| Moderate                  | Meaningful but generally recoverable effect requiring documented controls, owner review and monitoring.                                                                |
| High                      | Potentially significant effect on individuals, safety, confidentiality, decisions or operations; enhanced assessment, evidence and pre-production governance required. |
| Critical                  | Potential severe or systemic effect, or evidence/control uncertainty is too high for unrestricted deployment; production normally blocked pending treatment.           |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Do not conflate classifications</strong></p>
<p>AIA impact classification, Duckworks residual risk rating, and legal classifications such as an EU AI Act “high-risk AI system” are separate concepts. They may inform one another, but none is a substitute for the others.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 5. Affected Parties and Stakeholder Analysis

| **Stakeholder**                                                           | **Relationship**                                   | **Key interests / possible effects**                                                                                                                         | **Impact** |
|---------------------------------------------------------------------------|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| External applicants                                                       | Directly affected                                  | Fair treatment; accurate representation; privacy; transparency; accessibility; ability to correct/challenge material errors; meaningful human consideration. | High       |
| Internal candidates                                                       | Directly affected if expanded to internal mobility | Equal access to opportunities; workplace transparency; human review; representative consultation as applicable.                                              | High       |
| Applicants with disabilities                                              | Potentially disproportionate effect                | Accessible process; non-standard CV formats; reasonable accommodation; avoidance of proxy disadvantage.                                                      | High       |
| Applicants with foreign qualifications / non-native-language applications | Potentially disproportionate effect                | Equivalent qualification recognition; parsing reliability; language/format bias.                                                                             | High       |
| Applicants with non-linear careers / career gaps                          | Potentially disproportionate effect                | Avoiding unjustified proxy penalties for atypical career patterns.                                                                                           | High       |
| Recruiters / hiring managers                                              | Operational users                                  | Usable explanations; source review; workload; automation-bias safeguards; clear accountability.                                                              | High       |
| HR / People function                                                      | Business owner / control operator                  | Fair process, defensible criteria, complaints, workforce governance, evidence.                                                                               | High       |
| Feathered Workforce Council                                               | Representative stakeholder where applicable        | Transparency, workforce effects and consultation where relevant.                                                                                             | Moderate   |
| Duckworks leadership                                                      | Governance stakeholder                             | Business value, legal/regulatory exposure, reputational risk, operating evidence.                                                                            | Moderate   |

## 6. Positive Impact Assessment

| **ID** | **Positive impact**                  | **Mechanism**                                                                                                         | **Beneficiary**         | **Current status**             | **Evidence needed**                                  |
|--------|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------|------------------------------------------------------|
| P-01   | Recruiter capacity                   | Automation of extraction/summarization may reduce repetitive triage and allow more time for substantive review.       | Recruiters / HR         | Unvalidated benefit hypothesis | Baseline review time; controlled pilot comparison    |
| P-02   | Consistency of initial review        | Use of pre-approved criteria may reduce some reviewer variability if criteria are job-related and properly validated. | Applicants / recruiters | Conditional benefit            | Reviewer agreement; error audit; criteria governance |
| P-03   | Speed of candidate processing        | Faster summarization and comparison may reduce time-to-shortlist.                                                     | Applicants / HR         | Conditional benefit            | Time-to-shortlist baseline and pilot measure         |
| P-04   | Traceability                         | Structured criteria and logged outputs may improve evidence of what information was presented to human reviewers.     | HR / Risk / Audit       | Potential governance benefit   | Logging and decision-record evidence                 |
| P-05   | Accessibility support for recruiters | Structured summaries could make high-volume information easier to navigate for authorized users.                      | Recruiters              | Potential benefit              | User testing; accessibility assessment               |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Benefit discipline</strong></p>
<p>No positive impact receives control credit or business-case value merely because it is plausible. Duckworks must establish a baseline, define a measurement method, and compare pilot results before representing the benefit as realized.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 7. Adverse Impact Assessment

| **ID** | **Domain**                          | **Impact scenario**                                                                                                                           | **Affected party**               | **Significance** | **Evidence confidence** |
|--------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|------------------|-------------------------|
| A-01   | Fairness & discrimination           | Historical patterns, proxy variables, criteria design, or data quality cause one group to be ranked lower or receive less human attention.    | Applicants / protected groups    | Critical         | Low                     |
| A-02   | Accuracy & representation           | CV parsing or extraction error misstates qualifications, employment history, skills, or experience and affects ranking.                       | Applicants                       | High             | Low                     |
| A-03   | Automation bias                     | Recruiters over-rely on a score/rank or assume model output is objective, making human review nominal.                                        | Applicants / recruiters          | Critical         | Low                     |
| A-04   | Privacy & data governance           | Applicant data are over-collected, retained, reused, exposed, or used beyond the approved recruitment purpose.                                | Applicants / data subjects       | High             | Low                     |
| A-05   | Transparency & explanation          | Applicants or reviewers cannot understand how material outputs were produced or which factors influenced them.                                | Applicants / recruiters          | High             | Low                     |
| A-06   | Contestability & correction         | Applicants lack an effective route to correct data, challenge a material error, or obtain meaningful human reconsideration.                   | Applicants                       | High             | Low                     |
| A-07   | Accessibility & inclusion           | System or process handles disability-related needs, non-standard formats, foreign qualifications, or atypical careers less accurately.        | Potentially disadvantaged groups | Critical         | Low                     |
| A-08   | Security / adversarial manipulation | Malicious documents, prompt injection, insecure integrations, excessive permissions, or model compromise alter outputs or expose data.        | Applicants / Duckworks           | High             | Low                     |
| A-09   | Vendor / model opacity              | Duckworks cannot validate model changes, ranking logic, data use, training/retention terms, or performance evidence.                          | Applicants / Duckworks           | High             | Low                     |
| A-10   | Scale amplification                 | A flawed rule/model version is reused across many applications before detection, multiplying harm.                                            | Applicant population             | Critical         | Low                     |
| A-11   | Purpose creep                       | System expands from summarization/recommendation into automated rejection, employee monitoring, or unrelated assessment without reassessment. | Applicants / workers             | Critical         | Low                     |
| A-12   | Operational/reputational impact     | Poor outcomes, complaints, discriminatory patterns, or inability to evidence controls damage trust and create remediation burden.             | Duckworks / applicants           | High             | Medium                  |

### 7.1 Overall adverse-impact conclusion

The concentration of Critical/High impact scenarios, together with low evidence confidence at concept stage, supports the existing Do Not Deploy decision. Human involvement alone does not materially reduce the assessment unless the review process is designed, tested, logged, resourced, and demonstrated to operate effectively.

## 8. Data, Fairness, and Inclusion Assessment

The AIA does not assert that DuckTalent is biased; it identifies where unfair outcomes could arise and what evidence would be required to support deployment. Formal statistical bias/fairness validation using real applicant data is outside the initial portfolio scope and has not been performed.

| **Assessment topic**    | **Required Duckworks control / evidence**                                                                                                                     | **Current status**                    |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| Job criteria governance | Document role criteria; demonstrate job relevance; prohibit criteria that cannot be justified; version and approve changes.                                   | Required / not evidenced              |
| Feature review          | Identify direct, proxy and derived features; challenge features that can reproduce protected-characteristic patterns or irrelevant disadvantage.              | Required / not evidenced              |
| Data quality            | Validate parsing accuracy, missingness, duplicate handling, credential equivalence, language/format handling and source provenance.                           | Required / not evidenced              |
| Group performance       | Where lawful and appropriate, evaluate error rates and selection/shortlisting outcomes across relevant groups; define investigation thresholds before launch. | Synthetic DT-02 method demonstrated; production method, lawful data basis and thresholds not approved |
| Accessibility           | Test application ingestion, recruiter interface and candidate-facing notices/challenge route for accessibility barriers.                                      | Required / not evidenced              |
| Human review quality    | Test whether reviewers inspect source applications, understand model limitations, use override authority and do not mechanically follow ranking.              | Required / not evidenced              |
| Feedback-loop risk      | Prevent recruiter/model outputs from becoming unchallenged future training labels that reinforce previous decisions.                                          | Required / architecture not validated |

### 8.1 Related synthetic operating evidence — DT-02

A worked operating-evidence package is available at [`../../80-operating-evidence/AI-005-ducktalent/`](../../80-operating-evidence/AI-005-ducktalent/).

The package demonstrates `DT-02 — Pre-Deployment Fairness & Adverse-Impact Testing` against a synthetic `DT-01` feature-governance boundary using 24 synthetic applicants arranged as 12 matched pairs. It deliberately introduces an unapproved `Career_Gap_Months` score penalty, detects the resulting matched-pair and group-level effect, blocks the pre-deployment gate, records an exception, removes the feature, and successfully retests the complete synthetic population.

The diagnostic pre-remediation results include a Reference selection rate of **58.33%** and Comparison selection rate of **25.00%**, with corresponding true-positive rates of **100%** and **42.86%**. After removal of the seeded feature, both synthetic groups have a **58.33%** selection rate and **100%** true-positive rate in this matched test population.

These values are **not** legal fairness thresholds, adverse-impact safe harbors, or evidence of real-world discrimination. The group labels are synthetic test constructs and no real protected-characteristic data are used.

**Evidence state:** **Designed → Synthetic technical implementation demonstrated → Synthetic fairness execution demonstrated → Synthetic operation tested**

`DT-02` may therefore be treated as **Partially implemented within the synthetic portfolio boundary**. `DT-01` remains **Not implemented**, and the existing **DO NOT DEPLOY** decision remains unchanged.

## 9. Privacy, Security, and Third-Party Impact

| **Domain**                   | **Impact concern**                                                                                                                    | **Minimum evidence before deployment**                                                                                                     |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Privacy / purpose limitation | Applicant information may be reused beyond recruitment purpose or retained longer than necessary.                                     | Verified data flow, purposes, lawful basis analysis, retention rule, processor/controller arrangements, DPIA decision and approved notice. |
| Confidentiality / access     | Applicant or interview information may be exposed to unauthorized users or systems.                                                   | Access model, least privilege, logging, encryption/security design, test evidence.                                                         |
| AI security                  | Malicious CV/document content or integration pathways may influence prompts, retrieval, tools or outputs.                             | Threat model; prompt/injection controls where relevant; file/content handling; secure integration testing; incident route.                 |
| Vendor data use              | Provider may retain prompts/data, use content for model improvement, change subprocessors/model behavior, or restrict audit evidence. | Vendor due diligence; contract/data terms; retention/training/subprocessor evidence; change/incident clauses; exit approach.               |
| Model / service change       | Unannounced model or scoring changes may invalidate prior fairness and accuracy evidence.                                             | Version identification; change notification; approval/revalidation trigger; monitoring.                                                    |
| Evidence availability        | Duckworks may be unable to reconstruct why an output or decision occurred.                                                            | Versioned criteria, model/provider identifier, relevant input/output logs, human decision record, approvals and monitoring evidence.       |

## 10. Human Oversight and Decision Integrity

Meaningful human oversight is a design and operating control, not a label. Duckworks must demonstrate that the human reviewer has competence, time, information, authority, and a usable mechanism to challenge the output.

| **Oversight function**   | **Primary role**                                                 | **Required condition**                                                                                       | **Evidence**                              |
|--------------------------|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| Final decision authority | Recruiter/hiring manager                                         | AI may not automatically reject or hire in the stated design.                                                | Documented process + access control       |
| Source verification      | Recruiter                                                        | Reviewer can inspect the original application and approved criteria, not only the AI summary/rank.           | User-interface evidence + operating test  |
| Override / disregard     | Recruiter/hiring manager                                         | Reviewer may disregard, override or reverse AI output without penalty.                                       | Workflow + override logs                  |
| Escalation               | HR / Business Owner / AI Governance                              | Material anomaly, potential discrimination, privacy issue or control failure triggers specialist escalation. | SOP + incident evidence                   |
| Stop-use authority       | Business Owner / AI Governance / CRCO within delegated authority | Ranking can be disabled or system use suspended when thresholds are breached.                                | Technical/operational stop procedure      |
| Competence               | HR / AI Governance                                               | Reviewers understand limitations, automation bias, prohibited uses and challenge obligations.                | Training completion + competency evidence |
| Decision rationale       | Hiring decision-maker                                            | Material decisions record sufficient human rationale where required by Duckworks process.                    | Decision record sample                    |
| Quality monitoring       | HR + AI Governance                                               | Override, error, complaint and outcome indicators reviewed for patterns.                                     | Dashboard / review minutes                |

## 11. Impact Treatment and Blocking Action Plan

| **ID** | **Action**                                                                                                                                          | **Owner**                         | **Timing**                                    | **Required evidence**                                 | **Gate** |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|-----------------------------------------------|-------------------------------------------------------|----------|
| AIA-01 | Validate intended purpose, role criteria and unsupported uses; prohibit autonomous rejection/hiring.                                                | Beatrice Van Duck / HR            | Before pilot with any applicant-like data     | Approved use-case specification and criteria register | Blocking |
| AIA-02 | Complete Legal classification and applicability review using verified provider/deployer role, geography and intended purpose.                       | Amelia Duckett / General Counsel  | Before procurement/deployment decision        | Legal triage record                                   | Blocking |
| AIA-03 | Complete privacy assessment and determine whether a formal GDPR DPIA is required; approve data flow, notices, retention and vendor roles.           | Delia Duckham / DPO               | Before personal-data processing               | Privacy review / DPIA decision                        | Blocking |
| AIA-04 | Approve fairness-validation methodology, test design, protected/proxy feature review and acceptance/escalation thresholds.                          | HR + AI Governance + Data & AI    | Before deployment                             | Approved production fairness method/results; synthetic DT-02 package demonstrates test logic only | Blocking |
| AIA-05 | Validate parsing/ranking accuracy, error distribution, credential/language handling and failure modes.                                              | Dr. Ada Duckfield / Data & AI     | Before deployment                             | Validation report                                     | Blocking |
| AIA-06 | Perform accessibility and inclusive-design assessment for candidate and recruiter interaction points.                                               | HR / Product or Accessibility SME | Before deployment                             | Accessibility assessment                              | Blocking |
| AIA-07 | Implement meaningful human oversight, source review, override, reason recording, escalation and stop-use capabilities.                              | Beatrice Van Duck + HR Ops        | Before deployment                             | Procedure + workflow evidence + user testing          | Blocking |
| AIA-08 | Design candidate transparency, correction, challenge and human reconsideration process.                                                             | HR + Legal + Privacy              | Before deployment                             | Notice + challenge workflow                           | Blocking |
| AIA-09 | Complete AI security threat model and testing for file/document handling, prompt/injection exposure, integrations, access and logging.              | Cassandra Duckley / CISO          | Before deployment                             | Threat model + security test evidence                 | Blocking |
| AIA-10 | Complete third-party AI due diligence and contractual review, including data use, retention, model change, subprocessors, incident notice and exit. | Percival Duckworth / Procurement  | Before supplier approval                      | Vendor assessment + contract evidence                 | Blocking |
| AIA-11 | Define monitoring metrics, owners, thresholds, review cadence and incident/reassessment triggers.                                                   | Eleanor Duckford + HR + Data & AI | Before release approval                       | Monitoring plan                                       | Blocking |
| AIA-12 | Train recruiters/hiring managers on system limits, automation bias, review obligations, prohibited uses and escalation.                             | HR + AI Governance                | Before pilot/deployment                       | Training records                                      | Blocking |
| AIA-13 | Run controlled pilot using synthetic or otherwise approved data and produce evidence pack against acceptance criteria.                              | Data & AI + HR                    | After design controls; before real deployment | Pilot report + evidence pack                          | Blocking |
| AIA-14 | Obtain AI Governance Committee approval based on closed actions and updated residual risk/impact assessment.                                        | Reginald Duckman / CRCO           | Final pre-production gate                     | Committee decision record                             | Blocking |

## 12. Monitoring, Metrics, and Impact Verification

| **Monitoring area**  | **Candidate indicators**                                                                                    | **Owner**                          | **Decision rule**                                                                                  |
|----------------------|-------------------------------------------------------------------------------------------------------------|------------------------------------|----------------------------------------------------------------------------------------------------|
| Model / data quality | Parsing error rate; missing-field rate; ranking error/discordance; credential/language error patterns       | HR + Data & AI                     | Threshold TBD from validated pilot; breach triggers investigation/reassessment                     |
| Human oversight      | Override rate; source-review completion; decision-rationale completion; reviewer disagreement               | HR                                 | Unexpectedly low overrides or mechanical agreement may indicate automation bias and require review |
| Fairness / inclusion | Group-level error/selection indicators where lawful and methodologically appropriate; accessibility defects | HR + AI Governance + Privacy/Legal | Thresholds must be set in approved fairness/accessibility method before launch                     |
| Applicant impact     | Complaints; correction requests; challenges; reconsiderations; substantiated errors                         | HR + Legal/Privacy                 | Material or repeated complaints trigger investigation                                              |
| Security / privacy   | Access violations; data leakage; malicious-document/prompt events; vendor incidents                         | CISO + DPO                         | Significant event triggers containment and incident process                                        |
| Vendor / change      | Model/version change; terms/data-use change; subprocessor change; material feature change                   | Procurement + Technical Owner      | Material change triggers reassessment before continued reliance                                    |
| Business value       | Review time; time-to-shortlist; recruiter workload distribution                                             | Business Owner                     | Benefit must be demonstrated without degrading impact safeguards                                   |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>No fabricated thresholds</strong></p>
<p>The project source set does not contain validated fairness, accuracy, override, complaint, productivity, or financial thresholds. This AIA therefore records them as “TBD after baseline/pilot” rather than inventing values.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 13. Reassessment, Suspension, and Retirement Triggers

- Change in intended purpose, autonomy, ranking logic, decision authority, or use of DuckTalent beyond recruitment screening/recommendation.

- New model/provider/version or a substantial configuration, prompt, feature, weighting, or criteria change.

- New data categories, data sources, training/reference data, connectors, permissions, or applicant populations.

- Expansion to internal mobility, performance management, promotion, termination, task allocation, or monitoring.

- Expansion to new countries, business units, languages, occupational groups, or materially different applicant populations.

- Material fairness signal, discriminatory outcome, significant ranking/parsing error, accessibility failure, complaint pattern, or challenge outcome.

- Privacy, security, data leakage, vendor, model supply-chain, or access-control incident.

- Loss of meaningful human oversight, inability to override, or evidence that reviewers are mechanically following rankings.

- Control failure, evidence expiry, monitoring threshold breach, or inability to reconstruct material decisions.

- New or amended legal/regulatory requirement or change in Duckworks’ role that affects the assessment.

A material trigger requires the AI Governance Lead to update the inventory record and coordinate the appropriate AIA, risk assessment, legal/privacy/security review, FRIA/DPIA, control testing, approval, suspension or retirement action in accordance with the Lifecycle SOP.

## 14. Lifecycle Decision and Approval Record

| **Decision element**             | **Current AIA position**                                                                                                                                                                    |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Overall impact classification    | Critical - Duckworks internal governance label                                                                                                                                              |
| Current residual risk            | Critical - per existing Duckworks readiness/risk conclusions                                                                                                                                |
| Evidence confidence              | Low to Moderate - concept-stage design; several blocking controls are not yet evidenced                                                                                                     |
| Lifecycle decision               | DO NOT DEPLOY in current state                                                                                                                                                              |
| Permitted activity               | Documentation, design, assessment, controlled technical work and synthetic/approved testing consistent with existing project scope; no use with real applicants for consequential decisions |
| Approval required to change gate | AI Governance Committee following Legal, Privacy, HR, Security, Risk & Compliance and technical review                                                                                      |
| Independent assurance            | Internal Audit may later assess design/operation but must not own first- or second-line controls                                                                                            |

### 14.1 Draft sign-off

| **Role**                            | **Named stakeholder**                    | **AIA action**                                                                         |
|-------------------------------------|------------------------------------------|----------------------------------------------------------------------------------------|
| Business Owner                      | Beatrice Van Duck - Chief People Officer | Own intended purpose, business value, treatment and operating controls                 |
| AI Governance Lead                  | Eleanor Duckford                         | Maintain AIA, evidence pack, inventory traceability and governance coordination        |
| Risk & Compliance / Committee Chair | Reginald Duckman - CRCO                  | Challenge risk/impact conclusions and chair material approval decision                 |
| General Counsel                     | Amelia Duckett                           | Confirm legal classification/applicability and employment/legal issues                 |
| DPO                                 | Delia Duckham                            | Privacy advice, DPIA decision/guidance and personal-data challenge                     |
| CISO                                | Cassandra Duckley                        | Security challenge, threat-model/testing expectations and security acceptance criteria |
| Technical Owner                     | Dr. Ada Duckfield                        | Architecture, model/service, validation, monitoring and technical evidence             |
| Internal Audit                      | Penelope Duckins                         | Independent assurance observer; no operational ownership                               |

## 15. Duckworks Portfolio AIA Screening

DuckTalent is the detailed worked example because it has the strongest direct impact on individuals and the current Critical governance position. The same AIA process applies proportionately to the rest of the Duckworks portfolio.

| **ID** | **System**               | **Purpose**                    | **Impact** | **Primary AIA focus**                                                                               | **Current gate**                  |
|--------|--------------------------|--------------------------------|------------|-----------------------------------------------------------------------------------------------------|-----------------------------------|
| AI-001 | DuckDesign AI            | Engineering design assistance  | High       | Engineering decision quality; IP/confidentiality; product quality/safety; human validation          | Restricted pilot only             |
| AI-002 | QuackBot                 | Customer support               | High       | Hallucination; customer harm; transparency; privacy; prompt/RAG security; escalation                | Production blocked pending gates  |
| AI-003 | FeatherForecast          | Supply-chain forecasting       | Moderate   | Forecast accuracy/drift; operational/financial reliance; supplier impacts; human approval           | Continue with monitoring          |
| AI-004 | WingInspect Vision       | Manufacturing defect detection | High       | False negatives; product quality/safety; inspector reliance; performance drift                      | Restricted pilot only             |
| AI-005 | DuckTalent AI            | Recruitment screening/ranking  | Critical   | Fairness; employment opportunity; privacy; transparency; accessibility; human oversight             | Do not deploy                     |
| AI-006 | PondGPT                  | Internal employee assistant    | High       | Sensitive-data leakage; access amplification; hallucination; prompt/RAG security; employee reliance | Restricted pilot only             |
| AI-007 | Unregistered GenAI Usage | Shadow/uncontrolled use        | Critical   | Unknown purposes/owners/data/vendors; confidentiality/privacy; uncontrolled third-party exposure    | Immediate containment / decompose |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>AI-007 treatment</strong></p>
<p>Unregistered GenAI Usage is an organizational condition containing multiple use cases, not one homogeneous AI system. Each material discovered use must be decomposed into its own inventory record and, where warranted, its own AIA.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 16. Reusable Duckworks AIA Checklist

| **Check** | **Area**            | **Minimum AIA record**                                                                                                                        |
|-----------|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| AIA-CK-01 | Identity & purpose  | Unique AI ID; intended purpose; business owner; technical owner; lifecycle; provider/model; integrations; geography.                          |
| AIA-CK-02 | Business value      | Problem/opportunity; value hypothesis; beneficiaries; measurable baseline; evidence position.                                                 |
| AIA-CK-03 | Affected parties    | Direct, indirect and potentially disproportionate groups; representative stakeholders; vulnerable populations where relevant.                 |
| AIA-CK-04 | Data & inputs       | Data categories; provenance; quality; personal/confidential data; sensitive/proxy features; retention; access.                                |
| AIA-CK-05 | Decision role       | What AI generates/predicts/ranks; what humans decide; override/stop authority; prohibited/unsupported uses.                                   |
| AIA-CK-06 | Positive impacts    | Expected beneficial impacts, conditions needed for benefit, and measurable evidence.                                                          |
| AIA-CK-07 | Adverse impacts     | Fairness, safety, privacy, security, reliability, transparency, autonomy, accessibility, third-party, operational and reputational scenarios. |
| AIA-CK-08 | Controls & evidence | Existing controls; control effectiveness; evidence confidence; treatment owner; due point; acceptance evidence.                               |
| AIA-CK-09 | Specialist review   | Legal/regulatory triage; Privacy/DPIA; Security; HR; Product Safety; Procurement/vendor review as applicable.                                 |
| AIA-CK-10 | Monitoring          | KPIs/KRIs; complaints; overrides; drift; fairness; incidents; vendor changes; cadence; thresholds.                                            |
| AIA-CK-11 | Decision            | Approve / conditionally approve / restrict / reject / suspend / retire; approver; rationale; conditions.                                      |
| AIA-CK-12 | Reassessment        | Material-change, incident, drift, control failure, data/vendor/model, population, geography and legal-change triggers.                        |

## 17. Evidence and Source Index

The AIA is defensible only to the extent that its conclusions trace to source documents or evidence. Planned controls are not treated as implemented controls.

| **Source / evidence**                           | **AIA use**                                                                                                                                             |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| DuckTalent DT-02 Operating Evidence Package     | Synthetic executable fairness/proxy-feature worked example supporting Section 8.1; not production fairness, legal discrimination analysis, or deployment approval. |
| Duckworks Business Scenario                     | Business drivers, intended DuckTalent capabilities, affected applicant concerns, governance mandate and seven-system portfolio.                         |
| Duckworks Readiness Assessment                  | Critical DuckTalent residual-risk conclusion; priority governance issues; evidence maturity and portfolio findings.                                     |
| Project Objectives / Scope                      | AIA objectives, affected-party domains, proportionality, evidence/auditability and explicit out-of-scope limitations.                                   |
| Assumptions Register                            | Human accountability; DuckTalent advisory purpose; data assumptions; legal-screening limitations; separation of internal risk and legal classification. |
| Stakeholder Register                            | Business owner, technical owner, Legal, DPO, CISO, AI Governance Lead, Internal Audit and affected/representative stakeholders.                         |
| Acceptance Criteria                             | Current DuckTalent gate, minimum release conditions, Critical impact and evidence expectations.                                                         |
| AI Risk Classification & Assessment Methodology | Scenario-based assessment, severity/likelihood, evidence confidence, risk appetite, approval rules and reassessment triggers.                           |
| AI Business Use Case Portfolio                  | DuckTalent business need, intended use, input/output/human boundary, metrics and current gate.                                                          |
| AI Responsible Use Policy                       | People-related AI, data, human oversight, security, third-party and prohibited-use requirements.                                                        |
| AI Governance Lifecycle SOP                     | Intake, legal triage, assessment, specialist review, approval, monitoring, reassessment, suspension and shadow-AI process.                              |
| Duckworks EU FRIA - DuckTalent                  | Companion fundamental-rights-focused analysis and rights-specific treatment considerations.                                                             |
| Official public sources                         | EU AI Act (EUR-Lex); ISO/IEC 42005 public description; NIST AI RMF and AI RMF Playbook; other Duckworks reference-file sources as applicable.           |

### 17.1 Public-source interpretation

- EU AI Act: binding law where applicable. Legal applicability, organizational role and implementation facts must be confirmed separately; this AIA is not itself a conformity assessment.

- ISO/IEC 42005:2025: voluntary standard guidance for AI system impact assessment; public ISO descriptions are used without reproducing copyrighted standard text.

- NIST AI RMF 1.0 and Playbook: voluntary risk-management guidance; used to support structured governance, mapping, measurement and management of impacts/risks.

- Duckworks internal policy/methodology: organizational requirements for this fictional portfolio and not external legal requirements.

### Portfolio disclaimer

Duckworks, Project W.I.N.G., all named personnel, applicants, systems, datasets, decisions, measures, incidents, risks, controls, and evidence are fictional. This assessment demonstrates professional AI governance practice using synthetic/project data and public sources. It does not constitute legal advice, certification, independent assurance, a production approval, or a statement that Duckworks complies with any law or standard.
