# Duckworks EU Fundamental Rights Impact Assessment (FRIA) — DuckTalent AI (AI-005)

Article 27-aligned deployer assessment for recruitment screening and candidate ranking

| **Control**      | **Value**                                       |
|------------------|-------------------------------------------------|
| Document ID      | DW-WING-FRIA-01                                 |
| Version          | 1.0                                             |
| Assessment date  | 9 August 2026                                   |
| Organization     | Duckworks (fictional)                           |
| AI system        | AI-005 - DuckTalent AI                          |
| Business owner   | Beatrice Van Duck - Chief People Officer        |
| Technical owner  | Dr. Ada Duckfield - Head of Data & AI           |
| Assessment owner | Eleanor Duckford - AI Governance Lead           |
| Status           | Draft - Voluntary Article 27-aligned assessment |
| Lifecycle gate   | Do not deploy in current state                  |
| Classification   | Portfolio / Synthetic / Non-production          |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Legal posture - important</strong></p>
<p>Based on the current Duckworks assumptions, this document is NOT a mandatory Article 27 FRIA. Duckworks is modelled as a private advanced-manufacturing company, not a body governed by public law or a private entity providing a public service, and DuckTalent is a recruitment use case under Annex III point 4(a), not a creditworthiness or life/health-insurance use case under points 5(b) or 5(c). Duckworks nevertheless performs this assessment voluntarily as a governance and design-readiness control. Legal must reassess if those facts change.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Portfolio disclaimer. Duckworks, Project W.I.N.G., all personnel, AI systems, applicants, data, decisions, risks, controls and evidence referenced in this assessment are fictional and created solely for educational and professional portfolio purposes. This document is not legal advice, a notification to a market surveillance authority, or evidence of regulatory conformity.

## 1. Executive Determination

DuckTalent AI is intended to parse CVs, extract qualifications and experience, compare applicants against pre-approved role criteria, summarize applications, rank candidates, and recommend candidates for further human review. The current Duckworks business-use-case record classifies it as decision support for consequential employment decisions and prohibits autonomous rejection or hiring. The system is currently at concept stage and is not approved for deployment.

The EU AI Act expressly lists AI systems intended to analyse and filter job applications or evaluate candidates in Annex III point 4(a). DuckTalent therefore has a strong preliminary route to classification as a high-risk AI system under Article 6(2), subject to provider-side confirmation of Article 6(3) and the final implementation facts. This portfolio does not treat Duckworks' internal Critical risk rating as the same concept as EU AI Act “high-risk”.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Current decision</strong></p>
<p>Maintain “Do not deploy”. Before any pilot involving real applicants or any production use, Duckworks should complete the blocking legal, privacy, fairness, accessibility, human-oversight, vendor and validation work identified in this assessment. The voluntary FRIA does not itself clear the system for use.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 1.1 Assessment conclusion

| **Question**                  | **Determination**                    | **Basis / limitation**                                                                                                                                       |
|-------------------------------|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Article 27 applicability      | Not mandatory on current assumptions | Duckworks is a private manufacturer; no evidence it is a public-law body or private provider of public services. DuckTalent is Annex III 4(a), not 5(b)/(c). |
| Annex III high-risk route     | Likely / legal confirmation required | Recruitment filtering and candidate evaluation are expressly listed in Annex III 4(a).                                                                       |
| Current legal timing          | Future high-risk regime              | For Annex III systems, Chapter III Sections 1-3 apply from 2 December 2027 under the consolidated Act as amended in July 2026.                               |
| Voluntary governance position | Perform now                          | Duckworks uses Article 27 elements as an enhanced rights-impact control and design-readiness artifact.                                                       |
| Production decision           | Blocked                              | Existing project gate remains “Do not deploy in current state”.                                                                                              |

## 2. Legal Applicability Assessment

This section separates binding legal requirements from internal Duckworks practice and project assumptions. It is a governance screening conclusion, not a formal legal opinion.

| **Category**                  | **Source**               | **Requirement / practice**                                                                                                                                                                                            | **Duckworks position**                                           |
|-------------------------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| Mandatory legal requirement   | AI Act Art. 27(1)        | A FRIA is required before deployment for certain deployers of Article 6(2) high-risk systems: bodies governed by public law, private entities providing public services, and deployers of Annex III 5(b)/(c) systems. | Not triggered on current Duckworks facts.                        |
| Mandatory legal requirement   | AI Act Art. 27(1)(a)-(f) | Where Article 27 applies, the FRIA must cover process, time/frequency, affected categories, specific harms, human oversight, and measures/complaint mechanisms.                                                       | Used voluntarily as the structure of this document.              |
| Mandatory legal requirement   | AI Act Art. 27(2)        | Where Article 27 applies, assessment is for first use and must be updated when listed elements change or become outdated.                                                                                             | Adopted as an internal reassessment rule.                        |
| Mandatory legal requirement   | AI Act Art. 27(3)        | Where Article 27 applies, results are notified to the market surveillance authority using the Article 27(5) template, subject to the Article 46(1) exception.                                                         | Not applicable to this voluntary FRIA on current facts.          |
| Mandatory legal requirement   | AI Act Art. 27(4)        | FRIA may cross-reference or incorporate relevant DPIA content where obligations overlap.                                                                                                                              | DuckTalent DPIA determination remains a separate privacy action. |
| Mandatory legal requirement   | AI Act Art. 113(c)(i)    | Chapter III Sections 1-3 for Annex III high-risk systems apply from 2 Dec 2027.                                                                                                                                       | Timing is relevant to future deployment planning.                |
| Internal recommended practice | Duckworks governance     | Apply Article 27-style FRIA to human-impacting AI even when the statutory deployer trigger is not met.                                                                                                                | Voluntary control; not presented as EU law.                      |
| Project assumption            | Duckworks role           | Duckworks is a private European manufacturer and does not provide a public service for purposes of Article 27.                                                                                                        | Must be validated if organizational activities change.           |

### 2.1 Why DuckTalent is the selected FRIA use case

DuckTalent is the strongest rights-impact candidate in the initial Duckworks portfolio because its ranking and recommendations can materially influence access to employment. The existing readiness assessment identifies fairness, discrimination, transparency, privacy, explainability, automation bias and contestability as material concerns and assigns the current residual enterprise risk as Critical. The current governance gate is “Do not deploy”.

## 3. Assessment Scope and Method

The assessment maps the DuckTalent deployment context to the six mandatory content elements in Article 27(1), then expands those elements into a rights-risk register, human-oversight design, treatment plan, complaint mechanism, evidence-gap register and reassessment triggers. The impact assessment is context-specific: it assesses how Duckworks intends to use the system, not the AI model in the abstract.

The rights screening uses the EU Charter as a reference for rights potentially affected by this recruitment use. Identification of a Charter right in this document does not mean Duckworks has violated that right, nor does it determine the direct horizontal legal effect of the Charter against a private employer. It is a risk-identification lens for the Article 27-style assessment.

### 3.1 Evidence rules

- Existing Duckworks facts are stated as such only where supported by the portfolio baseline.

- Open assumptions are labelled and may not be used to reduce risk without validation.

- Planned controls receive no credit as implemented controls.

- Provider information required for a deployment-level FRIA (including Article 13 instructions for use and group-specific performance information) is currently unavailable and is treated as a blocking evidence gap.

- No real applicant data, demographic data, protected-class data, CVs, employment decisions or vendor evidence are used in this portfolio assessment.

## 4. Article 27(1) Assessment - DuckTalent Deployment Context

### 4.1 Deployer process and intended purpose - Article 27(1)(a)

| **Process step**          | **Intended use**                                                                                                        | **Rights-relevant point**                                                     |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Recruitment intake        | Applicants submit CVs/application data for a specific vacancy.                                                          | Applicant data enter an AI-supported workflow.                                |
| Parsing and extraction    | DuckTalent extracts job-relevant qualifications, skills, employment history and other approved fields.                  | Extraction errors or unsupported inferences may distort the applicant record. |
| Criteria comparison       | System compares applicants against role criteria approved in advance by Duckworks.                                      | Criteria or proxies may create unequal treatment.                             |
| Summarization and ranking | System produces summaries, indicators and a ranked recommendation for review.                                           | Ranking can influence which applicants receive recruiter attention.           |
| Human review              | Recruiter/hiring manager reviews source application and AI output, may override, and records consequential decision.    | Human review must be meaningful rather than a rubber stamp.                   |
| Challenge / correction    | Applicant can use an accessible channel to challenge or correct material information and request human reconsideration. | Process is planned and not yet evidenced.                                     |

### 4.2 Duration and frequency - Article 27(1)(b)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Open deployment assumption</strong></p>
<p>DuckTalent is currently a concept and no verified deployment schedule, applicant volume, operating period, recruitment cadence or geographic rollout is available. The expected pattern is recurring use when Duckworks recruitment campaigns are active. Exact duration, frequency, countries and volume must be recorded before any real deployment.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 4.3 Categories of persons and groups likely to be affected - Article 27(1)(c)

| **Category / group**                                                       | **Relationship**                                        | **Potential effect**                                                                                                  |
|----------------------------------------------------------------------------|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| External applicants                                                        | Directly affected                                       | May be ranked, shortlisted, deprioritized or recommended for further review.                                          |
| Internal candidates                                                        | Directly affected if tool is used for internal mobility | Employment opportunity and workplace-process effects; worker/representative requirements may also arise.              |
| Applicants with disabilities                                               | Potentially disproportionately affected                 | Accessibility barriers, non-standard CV formats, gaps or atypical career pathways can create disadvantage.            |
| Applicants associated with protected characteristics                       | Potentially disproportionately affected                 | Historical or proxy variables may correlate with protected grounds and produce unequal outcomes.                      |
| Applicants with foreign qualifications or non-native-language applications | Potentially disproportionately affected                 | Parsing and criteria models may under-recognise equivalent experience, credentials or language formats.               |
| Applicants with non-linear careers / caregiving gaps                       | Potentially disproportionately affected                 | Proxy features may penalise career gaps or atypical progression.                                                      |
| Recruiters and hiring managers                                             | Operational users                                       | Automation bias, workload shift, false confidence and unclear accountability can affect decision quality.             |
| Workers’ representatives                                                   | Representative stakeholder where applicable             | Potential information/consultation interest where the system is used at the workplace or affects internal candidates. |

### 4.4 Specific risks of harm - Article 27(1)(d)

The following scenarios are plausible harms to rights in the stated use case. They are not findings that harm has occurred. Severity and evidence confidence are qualitative FRIA judgements; the EU AI Act does not prescribe this scoring scale.

| **ID** | **Rights lens**                            | **Risk**                                 | **Scenario**                                                                                                                                                        | **Potential impact** | **Evidence**                      |
|--------|--------------------------------------------|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|-----------------------------------|
| FR-01  | Arts. 20, 21, 23; Art. 15                  | Discriminatory ranking / proxy bias      | Historical data, role criteria or proxy features systematically disadvantage a protected group, reducing access to employment.                                      | Severe               | Low - no real validation evidence |
| FR-02  | Art. 15; Art. 1                            | Inaccurate exclusion or deprioritisation | Parsing or ranking error misrepresents an applicant and causes them to receive less human attention or lose an employment opportunity.                              | Major                | Low                               |
| FR-03  | Arts. 7 and 8                              | Privacy and data misuse                  | CV/application data are over-collected, retained, reused for unrelated model training, or used to infer sensitive information beyond recruitment necessity.         | Major                | Low                               |
| FR-04  | Arts. 21 and 26                            | Disability / accessibility disadvantage  | Application formats, accessibility needs or career patterns of persons with disabilities are handled less accurately or interfaces prevent effective participation. | Severe               | Low                               |
| FR-05  | Arts. 20, 21, 15; Art. 1                   | Automation bias / ineffective oversight  | Recruiters over-rely on rankings, fail to review source material, or treat AI scores as objective, making human review nominal.                                     | Severe               | Low                               |
| FR-06  | Art. 47 (remedy dimension); Arts. 8 and 15 | Opacity and weak contestability          | Applicant cannot understand that AI materially assisted the process, correct data, challenge a material error or obtain meaningful reconsideration.                 | Major                | Low                               |
| FR-07  | Arts. 20, 21, 23; Art. 15                  | Historical-pattern entrenchment          | Training or benchmark data reproduce historic workforce patterns, making apparently neutral ranking rules systematically unequal.                                   | Severe               | Low                               |
| FR-08  | Arts. 21, 22, 15                           | Language / credential bias               | System under-values foreign qualifications, alternative terminology, linguistic variation or non-standard career histories.                                         | Major                | Low                               |
| FR-09  | Arts. 7, 8, 21                             | Sensitive or unrelated inference         | System infers personality, emotion, health, ethnicity, religion or other non-job-relevant characteristics from application content.                                 | Severe               | Low                               |
| FR-10  | Arts. 15, 20, 21                           | Scale amplification                      | A faulty criterion or model version affects many applicants before detection because automated ranking is repeatedly reused.                                        | Severe               | Low                               |

### 4.5 Human oversight measures - Article 27(1)(e)

| **Oversight element**               | **Required design**                                                                                                                             | **Current evidence position**         |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| Decision authority                  | Recruiter/hiring manager remains accountable for shortlist, rejection, interview and hiring decisions.                                          | Design requirement; not yet operating |
| No automated rejection              | System may recommend or rank but may not autonomously reject or hire applicants.                                                                | Existing Duckworks use-case boundary  |
| Source review                       | Reviewer must be able to inspect the original application and relevant criteria, not only the AI score/rank.                                    | Planned control                       |
| Override                            | Reviewer must have authority and a usable mechanism to disregard or override AI output without penalty.                                         | Planned control                       |
| Reason recording                    | Material decisions influenced by AI should record the human basis and, where appropriate, the reason for overriding/accepting a recommendation. | Planned control                       |
| Competence and AI literacy          | Reviewers must understand known limitations, bias risks, confidence, prohibited uses and escalation paths.                                      | Planned training                      |
| Sampling and second-line monitoring | Periodically sample decisions, overrides and group-level outcomes for error and unequal-impact signals.                                         | Planned monitoring                    |
| Stop-use authority                  | Business owner / AI Governance can suspend ranking or the whole use case when rights, privacy, fairness or control thresholds are breached.     | Governance requirement                |

### 4.6 Measures if risks materialise - Article 27(1)(f)

- Suspend the affected model function, ranking workflow or full use case where a material rights, fairness, privacy or control issue is identified.

- Preserve relevant logs, model/version identifiers, criteria configuration, decision records and evidence needed for investigation.

- Escalate to the Business Owner, AI Governance Lead, CRCO, General Counsel, DPO and other specialists according to incident type.

- Provide a human-only reassessment route for affected candidates where a material AI error or unfair outcome may have influenced the process.

- Correct inaccurate data or decision records and prevent reuse of the affected output until remediation is validated.

- Assess whether notification to affected persons, a data protection authority, market surveillance authority or another body is required under applicable law; no notification duty is invented by this document.

- Retest the affected model/criteria, reassess the FRIA/risk assessment/DPIA as applicable, and obtain renewed governance approval before resuming use.

- Use complaint trends, appeals, override rates and outcome data as monitoring inputs and reassessment triggers.

## 5. Fundamental Rights Mapping

| **Charter right**                                                        | **Potential relevance to DuckTalent**                                                                                                                                                                 | **Assessment note**                                              |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| Article 1 - Human dignity                                                | Reduction of applicants to opaque scores; demeaning or arbitrary treatment; lack of meaningful consideration of individual circumstances.                                                             | Relevant risk lens; not a finding of violation.                  |
| Article 7 - Respect for private and family life                          | Collection or inference of personal information beyond recruitment necessity; use of private-life details contained in CVs.                                                                           | Relevant where application data reveal private-life information. |
| Article 8 - Protection of personal data                                  | Fair, purpose-limited and secure processing; accuracy and correction of applicant data.                                                                                                               | Core privacy lens; GDPR analysis remains separate.               |
| Article 15 - Freedom to choose an occupation and right to engage in work | Ranking errors or unfair filtering can materially influence access to employment opportunities.                                                                                                       | Core employment-rights lens.                                     |
| Article 20 - Equality before the law                                     | Consistent and non-arbitrary treatment across applicant groups.                                                                                                                                       | Used as equality lens in FRIA.                                   |
| Article 21 - Non-discrimination                                          | Direct or indirect discriminatory ranking or proxy effects across protected grounds.                                                                                                                  | Core fairness lens.                                              |
| Article 22 - Cultural, religious and linguistic diversity                | Model performance may differ across languages, names, cultural/credential conventions or linguistic styles.                                                                                           | Contextual lens; requires testing rather than assumptions.       |
| Article 23 - Equality between women and men                              | Recruitment outcomes may reproduce gender imbalance or discriminatory historical patterns.                                                                                                            | Core employment-equality lens.                                   |
| Article 26 - Integration of persons with disabilities                    | Accessibility, accommodation and atypical employment histories may be mishandled by standardized ranking logic.                                                                                       | Core accessibility lens.                                         |
| Article 47 - Effective remedy and fair trial                             | Where rights under Union law are infringed, access to effective legal remedy must not be undermined; Duckworks internal challenge channel supports correction but does not replace judicial remedies. | Secondary remedy lens.                                           |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Charter field-of-application caution</strong></p>
<p>The Charter is addressed to EU institutions and to Member States when implementing Union law (Article 51). This FRIA uses Charter rights as the rights framework contemplated by the AI Act; it does not assert that every Charter provision independently creates a directly enforceable private-employer obligation in every recruitment scenario.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 6. Rights-Risk Treatment and Control Plan

| **ID**  | **Control**                      | **Owner**                        | **Requirement**                                                                                                                                                       | **Evidence**                                           | **Status**             |
|---------|----------------------------------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|------------------------|
| FRIA-01 | Job-criteria governance          | HR / Business Owner              | Pre-approve job-relevant criteria; document necessity; prohibit unrelated or unvalidated criteria and proxies.                                                        | Approved criteria register; rationale; change history  | Planned - blocking     |
| FRIA-02 | Feature / inference restrictions | HR + Legal + Data & AI           | Prohibit emotion/personality inference and sensitive/unrelated trait inference; restrict derived features.                                                            | Feature list; model configuration; test evidence       | Planned - blocking     |
| FRIA-03 | Fairness validation              | Data & AI + HR + Risk            | Test relevant group performance/outcome disparities using lawful, appropriate methodology and synthetic/test data before production; establish escalation thresholds. | Validation plan/report; methodology; issue log         | Planned - blocking     |
| FRIA-04 | Accuracy / ranking validation    | Data & AI                        | Validate parsing, ranking, false-negative/false-positive behaviour and error distribution against stated purpose.                                                     | Test dataset description; results; limitations         | Planned - blocking     |
| FRIA-05 | Accessibility assessment         | HR + Accessibility/Legal         | Test candidate-facing workflow and alternative application/review route; accommodate accessibility needs.                                                             | Accessibility review; remediation evidence             | Planned - blocking     |
| FRIA-06 | DPIA / privacy controls          | DPO + Privacy                    | Determine GDPR Article 35 DPIA requirement; define lawful basis, minimisation, retention, access, correction and processor terms.                                     | DPIA or documented determination; RoPA; privacy notice | Planned - blocking     |
| FRIA-07 | Meaningful human oversight       | Business Owner + HR              | No automatic rejection/hiring; reviewer access to source data; override authority; anti-automation-bias training.                                                     | SOP; training; decision logs; override evidence        | Planned - blocking     |
| FRIA-08 | Applicant transparency           | HR + Legal + DPO                 | Provide clear notice of AI-supported recruitment and relevant information required by applicable law before use.                                                      | Notice text; publication evidence                      | Planned - blocking     |
| FRIA-09 | Challenge and correction         | HR + Legal                       | Accessible channel for correction, challenge and human reconsideration; preserve external legal remedies.                                                             | Procedure; case log; response evidence                 | Planned - blocking     |
| FRIA-10 | Vendor/provider due diligence    | Procurement + Security + Privacy | Obtain provider Article 13 information, performance by relevant groups where available, training/data terms, change controls and audit evidence.                      | Vendor assessment; contract; instructions for use      | Planned - blocking     |
| FRIA-11 | Security and access controls     | CISO / IT                        | Least privilege, secure data transfer/storage, logging, tenant isolation and incident response.                                                                       | Access review; security assessment; logs               | Planned - blocking     |
| FRIA-12 | Change and version governance    | Data & AI + AI Governance        | Material model, criteria, data, vendor or purpose change triggers reassessment and approval.                                                                          | Change record; version register; reassessment          | Planned                |
| FRIA-13 | Outcome monitoring               | HR + AI Governance               | Monitor errors, overrides, challenges, group-level fairness indicators where lawful, and complaint trends.                                                            | Dashboard; review minutes; action log                  | Planned                |
| FRIA-14 | Stop-use / incident mechanism    | Business Owner + AI Governance   | Suspend use when material rights, fairness, privacy, safety or control failure occurs.                                                                                | Incident ticket; suspension record; approval to resume | Governance requirement |

## 7. Complaint, Contestability and Remedy Design

Duckworks should establish an applicant-facing mechanism that is usable without specialist AI knowledge and does not require the applicant to prove how the model works. The mechanism is an internal governance safeguard; it does not displace rights or remedies available under applicable law.

| **Mechanism**         | **Required design**                                                                                                     | **Evidence / note**                                                           |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Notice                | Explain that AI materially assists application analysis/ranking where applicable and identify a contact route.          | Before or at relevant processing stage; exact legal wording to be approved.   |
| Correction            | Allow applicants to correct materially inaccurate application data or parsing errors.                                   | Human review of correction.                                                   |
| Challenge             | Allow an applicant to challenge a material AI-supported outcome or suspected unfair treatment.                          | No retaliation; accessible submission channel.                                |
| Human reconsideration | Provide review by a competent person who can disregard the AI output.                                                   | Reviewer must examine source evidence rather than simply reconfirm the score. |
| Escalation            | Escalate discrimination, accessibility, privacy, security or systemic issues to specialist functions.                   | Trigger incident/reassessment process where material.                         |
| Recordkeeping         | Log challenge category, outcome, root cause and remediation without unnecessary sensitive data.                         | Supports trend monitoring and audit evidence.                                 |
| External remedies     | Do not imply that the internal process replaces data-protection complaints, employment-law claims or judicial remedies. | Legal notice to be validated per jurisdiction.                                |

## 8. Stakeholder and Specialist Review

| **Stakeholder**                              | **Role**                                | **FRIA contribution**                                                                                                             | **Status**                                      |
|----------------------------------------------|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| Beatrice Van Duck - Chief People Officer     | Business owner / workforce-domain owner | Own intended purpose, job criteria, human decision process, accessibility and recruitment controls.                               | Required                                        |
| Dr. Ada Duckfield - Head of Data & AI        | Technical owner                         | Provide architecture, model, validation, performance, version and monitoring evidence.                                            | Required                                        |
| Amelia Duckett - General Counsel             | Legal adviser                           | Confirm AI Act classification, Article 27 applicability, employment/equality-law issues, transparency and challenge requirements. | Required                                        |
| Delia Duckham - DPO                          | Privacy adviser                         | Determine and oversee DPIA; review lawful basis, minimisation, transparency, retention and rights.                                | Required                                        |
| Reginald Duckman / Eleanor Duckford          | Governance sponsor / AI Governance Lead | Challenge assessment, coordinate evidence, maintain decision trail and committee gate.                                            | Required                                        |
| Cassandra Duckley - CISO                     | Security challenger                     | Review access, leakage, vendor, integration and incident controls.                                                                | Required                                        |
| Recruiters / hiring managers                 | Operational users                       | User testing, oversight usability, automation-bias controls and feedback.                                                         | Required before pilot                           |
| Future Ducklings - applicant representatives | Affected-party perspective              | Fair treatment, accessibility, clarity, contestability and human review.                                                          | Planned representation; no real applicants used |
| Feathered Workforce Council                  | Employee representative body            | Relevant if system is used for internal mobility or in workplace context.                                                         | Consult as applicable                           |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Consultation evidence gap</strong></p>
<p>This portfolio assessment does not claim that real applicants, employee representatives or affected communities were consulted. A real deployment should document an appropriate consultation strategy, particularly where internal candidates, accessibility needs or materially affected groups are involved.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 9. Relationship with the GDPR DPIA

Article 27(4) permits FRIA content to cross-reference or incorporate relevant parts of a GDPR Article 35 DPIA where obligations overlap. DuckTalent will process applicant personal data and perform automated analysis that may materially influence recruitment decisions. GDPR Article 35 therefore requires a specific DPIA determination and may require a DPIA depending on the verified processing design, scale, degree of automation and national supervisory-authority lists. This FRIA does not substitute for that determination.

| **Overlap area**          | **FRIA source**               | **DPIA action**                                                                           |
|---------------------------|-------------------------------|-------------------------------------------------------------------------------------------|
| Purpose and process       | FRIA section 4.1              | DPIA should describe processing operations, purposes and lawful basis.                    |
| Data categories / sources | Business use case + inventory | DPIA should define exact personal data, special-category handling, source and recipients. |
| Affected persons          | FRIA 4.3                      | DPIA should identify data subjects and privacy-specific vulnerabilities.                  |
| Privacy harms             | FRIA FR-03 / FR-09            | DPIA should assess data-protection risks, necessity and proportionality.                  |
| Safeguards                | FRIA section 6                | DPIA should cross-reference technical/organizational privacy controls.                    |
| Review triggers           | FRIA section 12               | DPIA must be reviewed when processing risk changes; align change control.                 |

## 10. Blocking Evidence and Assumptions Register

| **ID** | **Gap**                                                | **Current position**                                                         | **Owner**                        | **Required evidence/action**                                                              | **Status**      |
|--------|--------------------------------------------------------|------------------------------------------------------------------------------|----------------------------------|-------------------------------------------------------------------------------------------|-----------------|
| EG-01  | Duckworks Article 27 deployer status                   | Current assumption: private manufacturer, not public-service provider.       | Legal                            | Confirm before any mandatory-FRIA conclusion; reassess if services/business model change. | Open - High     |
| EG-02  | Final EU AI Act classification                         | Likely Annex III 4(a); provider-side Article 6(3) assessment not available.  | Legal / Provider                 | Obtain provider classification and Legal confirmation.                                    | Open - Critical |
| EG-03  | Provider instructions for use / Article 13 information | No real provider or technical documentation in portfolio.                    | Technical / Procurement          | Obtain before deployment; use in rights-risk analysis.                                    | Open - Critical |
| EG-04  | Model and data provenance                              | Training/validation data, feature logic and known limitations unknown.       | Data & AI                        | Document provenance, data governance, performance and limitations.                        | Open - Critical |
| EG-05  | Deployment scale / countries / cadence                 | No verified applicant volume, frequency or jurisdictions.                    | Business Owner                   | Confirm before final assessment and legal analysis.                                       | Open - High     |
| EG-06  | Fairness / subgroup performance                        | No real or synthetic statistical validation has been completed in this FRIA. | Data & AI / HR                   | Complete lawful, methodologically justified fairness testing.                             | Open - Critical |
| EG-07  | Human oversight operation                              | No evidence that proposed reviewer controls operate effectively.             | HR / Business Owner              | Pilot only after oversight procedure, training and testing are evidenced.                 | Open - Critical |
| EG-08  | DPIA determination                                     | No formal GDPR DPIA in portfolio.                                            | DPO                              | Complete documented DPIA decision and DPIA if required.                                   | Open - Critical |
| EG-09  | Applicant challenge mechanism                          | Not yet implemented.                                                         | HR / Legal                       | Design, test and evidence accessible human reconsideration route.                         | Open - High     |
| EG-10  | Vendor contract / data reuse / subprocessors           | No real vendor due diligence.                                                | Procurement / Privacy / Security | Complete AI-specific supplier assessment and contract review.                             | Open - Critical |

## 11. FRIA Decision and Governance Conditions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>FRIA decision: DO NOT DEPLOY</strong></p>
<p>The voluntary Article 27-aligned assessment identifies potentially severe impacts on access to employment, equality/non-discrimination, privacy/data protection, disability inclusion, dignity and contestability. Existing evidence is insufficient to demonstrate that those risks are adequately controlled. DuckTalent therefore remains blocked from real-applicant pilot or production deployment.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 11.1 Minimum conditions before reconsideration

- Legal confirms AI Act role/classification and Article 27 applicability using verified deployment facts.

- DPO completes a documented GDPR DPIA determination and any required DPIA.

- Job criteria and features are validated as job-relevant, necessary, explainable and free from prohibited/unapproved inferences.

- Pre-deployment accuracy, robustness, fairness and accessibility testing is completed with documented methodology, limitations and remediation.

- Meaningful human oversight is implemented and tested, including source review, override authority and anti-automation-bias training.

- Applicant transparency, correction, challenge and human-reconsideration mechanisms are implemented.

- Provider/vendor due diligence supplies required instructions, performance, data-use, change, security and contractual evidence.

- Monitoring metrics and escalation thresholds are approved; stop-use and incident procedures are operational.

- AI Governance Committee formally reviews evidence and approves any change to the current “Do not deploy” gate.

### 11.2 Residual rights-risk statement

This FRIA does not create a separate statutory “FRIA score”. For portfolio consistency, the system retains the existing Duckworks current residual enterprise risk of Critical (20) until the related risk assessment is formally updated with evidence of implemented controls. Target-state controls and planned mitigations must not be represented as current control effectiveness.

## 12. Reassessment Triggers

- Change in intended purpose, including use for promotion, termination, task allocation, performance monitoring or other workforce management.

- Increase in autonomy, including automatic rejection, automatic shortlist cut-offs, or restrictions on human override.

- New model, vendor, algorithm, ranking method, scoring threshold, feature set or material configuration change.

- New training, validation, reference or applicant data sources, including inferred or special-category data.

- Expansion to new countries, applicant populations, internal candidates, apprentices/minors or vulnerable groups.

- Material change in Duckworks’ legal role, including becoming a public-law body or private provider of a public service relevant to Article 27.

- Material disparity, complaint, accessibility failure, security/privacy incident, or evidence of systematic ranking error.

- Change to provider instructions, known limitations, group-specific performance or EU AI Act classification.

- New or amended EU/national law, regulatory guidance, official Article 27 template, or supervisory-authority instruction.

- Any decision to move from concept to real-world pilot or production.

## 13. Article 27 Traceability Checklist

| **Provision** | **Element**                                              | **Document location**          | **Status**                                                                    |
|---------------|----------------------------------------------------------|--------------------------------|-------------------------------------------------------------------------------|
| Art. 27(1)(a) | Deployer process / intended purpose                      | Section 4.1                    | Covered                                                                       |
| Art. 27(1)(b) | Period and frequency                                     | Section 4.2                    | Partially covered - deployment facts TBD                                      |
| Art. 27(1)(c) | Affected categories/groups                               | Section 4.3                    | Covered at design level                                                       |
| Art. 27(1)(d) | Specific risks of harm, using provider information       | Sections 4.4-5                 | Risks covered; provider information missing                                   |
| Art. 27(1)(e) | Human oversight                                          | Section 4.5                    | Design covered; operation not evidenced                                       |
| Art. 27(1)(f) | Measures if risks materialise, governance and complaints | Sections 4.6-7                 | Design covered; implementation not evidenced                                  |
| Art. 27(2)    | First use / update when changed                          | Section 12                     | Adopted as internal lifecycle rule                                            |
| Art. 27(3)    | Notify market surveillance authority                     | Section 2                      | Not applicable to voluntary FRIA on current assumptions                       |
| Art. 27(4)    | DPIA cross-reference                                     | Section 9                      | Planned; DPIA decision outstanding                                            |
| Art. 27(5)    | AI Office questionnaire/template                         | Appendix B / governance action | Use official template if applicable/available at time of mandatory assessment |

## 14. Review and Sign-Off Record

The signatures below are intentionally shown as draft portfolio governance roles. No real executive, legal, regulatory or assurance approval is claimed.

| **Role**                | **Named stakeholder**                    | **Review focus**                                   | **Status** |
|-------------------------|------------------------------------------|----------------------------------------------------|------------|
| Business Owner          | Beatrice Van Duck - Chief People Officer | Purpose, recruitment process, human accountability | Pending    |
| AI Governance Lead      | Eleanor Duckford                         | FRIA completeness, evidence and traceability       | Pending    |
| General Counsel         | Amelia Duckett                           | Legal applicability/classification review          | Pending    |
| DPO                     | Delia Duckham                            | Privacy/DPIA review                                | Pending    |
| CISO                    | Cassandra Duckley                        | Security and third-party controls                  | Pending    |
| AI Governance Committee | Cross-functional committee               | Lifecycle gate / treatment decision                | Pending    |

## Appendix A - Key Source Basis

| **Type**                     | **Source**                                                          | **Relevant provisions/section**                                | **Use in this FRIA**                                                                                                           |
|------------------------------|---------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Binding EU law               | Regulation (EU) 2024/1689 (AI Act), consolidated 27 Jul 2026        | Article 6; Article 27; Article 113; Annex III 4(a), 5(b), 5(c) | Legal classification, FRIA trigger/content, application timing.                                                                |
| Binding EU law               | Charter of Fundamental Rights of the European Union (2012/C 326/02) | Arts. 1, 7, 8, 15, 20, 21, 22, 23, 26, 47, 51                  | Rights-screening reference and field-of-application caution.                                                                   |
| Binding EU law               | Regulation (EU) 2016/679 (GDPR)                                     | Article 35                                                     | Separate DPIA requirement/determination and relationship to FRIA.                                                              |
| Official Commission guidance | Navigating the AI Act - European Commission FAQ                     | High-risk examples; deployer obligations; FRIA scope           | Supports interpretation that FRIA applies to public/public-service deployers and specified financial/insurance use cases.      |
| Internal Duckworks artifact  | AI Business Use Case Portfolio v1.0                                 | AI-005 DuckTalent                                              | Intended purpose, business/technical owners, inputs/outputs, human decision boundary, do-not-deploy gate.                      |
| Internal Duckworks artifact  | AI Risk Classification & Assessment Methodology v1.0                | Legal triage; risk domains; control evidence; residual risk    | Keeps internal risk separate from legal classification and prevents credit for planned controls.                               |
| Internal Duckworks artifact  | Project Stakeholder Register v1.0                                   | HR, Legal, DPO, CISO, AI Governance, affected applicants       | Defines review and affected-stakeholder roles.                                                                                 |
| Internal Duckworks artifact  | Project Acceptance Criteria v1.0                                    | DuckTalent release gate                                        | Requires enhanced legal/privacy/fairness analysis, meaningful human review, bias testing and contestability before deployment. |

## Appendix B - Official Public Links

| **Source**                                   | **Official link**                                                                  |
|----------------------------------------------|------------------------------------------------------------------------------------|
| EU AI Act - consolidated text (27 July 2026) | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R1689-20260727 |
| European Commission - Navigating the AI Act  | https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act                    |
| EU Charter of Fundamental Rights             | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:12012P/TXT          |
| GDPR - consolidated text                     | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02016R0679-20160504 |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Template note</strong></p>
<p>Article 27(5) requires the AI Office to develop a questionnaire template. This portfolio artifact is an internal Article 27-aligned assessment, not a substitute for any official template that is applicable and available when a legally mandatory FRIA is performed.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Appendix C - Reusable Duckworks FRIA Intake Checklist

| **\#** | **Checklist item**                                                                                            |
|--------|---------------------------------------------------------------------------------------------------------------|
| 1      | Confirm system ID, intended purpose, provider/deployer role and high-risk route.                              |
| 2      | Determine whether the Article 27 deployer trigger applies; document legal basis and assumptions.              |
| 3      | Describe the business process, duration and frequency of use.                                                 |
| 4      | Identify affected natural persons, groups and vulnerability factors.                                          |
| 5      | Map plausible harms to relevant fundamental rights; use provider Article 13 information.                      |
| 6      | Describe human oversight in operational terms: competence, source review, override, escalation and stop-use.  |
| 7      | Define mitigation, internal governance, complaint/challenge and incident measures.                            |
| 8      | Cross-reference the DPIA where applicable; do not duplicate privacy analysis unnecessarily.                   |
| 9      | Record evidence gaps, control status and residual uncertainty; planned controls are not implemented controls. |
| 10     | Set lifecycle decision, approval authority, monitoring metrics and reassessment triggers.                     |
| 11     | If Article 27 is mandatory, complete the official Article 27(5) template and required notification.           |
| 12     | Update the assessment when material elements change or before a new use context.                              |
