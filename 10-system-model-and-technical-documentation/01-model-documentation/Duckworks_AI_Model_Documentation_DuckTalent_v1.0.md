# Duckworks AI Model Documentation Record — DuckTalent AI (AI-005)

**DUCKWORKS**

**AI Model Documentation Record**

**DuckTalent AI (AI-005)**

Model identity, design assumptions, data, evaluation, limitations, oversight, monitoring, change control, and evidence requirements

| **Document control**    | **Value**                                  |
|-------------------------|--------------------------------------------|
| Document ID             | DW-WING-MDL-01                             |
| Version                 | 1.0                                        |
| Assessment date         | 9 August 2026                              |
| Organization            | Duckworks (fictional)                      |
| AI system               | AI-005 - DuckTalent AI                     |
| Business owner          | Beatrice Van Duck - Chief People Officer   |
| Technical / model owner | Dr. Ada Duckfield - Head of Data & AI      |
| Governance owner        | Eleanor Duckford - AI Governance Lead      |
| Status                  | Draft - Pre-deployment model documentation |
| Lifecycle               | Concept / pre-deployment                   |
| Current governance gate | DO NOT DEPLOY with real applicants         |
| Internal risk position  | Critical                                   |
| Classification          | Portfolio / Synthetic / Non-production     |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Critical documentation status</strong></p>
<p>The Duckworks source set defines DuckTalent at AI-system and business-use-case level but does not identify a specific underlying model, model family, provider, version, training corpus, architecture, hyperparameters, validation results, or production hosting design. Those facts are deliberately recorded as TBD / not evidenced. This document must not be represented as a completed model card or regulatory technical file until the missing technical evidence is supplied.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Portfolio disclaimer. Duckworks, Project W.I.N.G., all personnel, applicants, systems, models, datasets, decisions, risks, controls, metrics and evidence referenced here are fictional or synthetic and created solely for educational and professional portfolio purposes. This document is not legal advice, certification evidence, a conformity assessment, or proof of regulatory compliance.

## 1. Executive Documentation Determination

DuckTalent AI is a proposed recruitment decision-support system intended to parse CVs, extract job-relevant information, compare applicants against pre-approved job criteria, summarize applications, rank candidates, and recommend candidates for further human review. The current design prohibits autonomous hiring or rejection; recruiters and hiring managers retain formal accountability for consequential employment decisions.

| **Area**                        | **Current position**     | **Rationale**                                                                                                                                                                      |
|---------------------------------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System documentation maturity   | Moderate                 | Purpose, ownership, affected parties, decision boundary, risk/impact position and governance controls are documented.                                                              |
| Model documentation maturity    | Low                      | Underlying model/provider/version, architecture, training/validation data, performance, fairness, explainability and security evidence are not yet validated.                      |
| Current model identifier        | TBD                      | A unique model/component ID must be assigned once the technical design or vendor/model is selected.                                                                                |
| Validated performance           | None evidenced           | No real applicant validation, accuracy, fairness, robustness or human-factors results are present in the portfolio.                                                                |
| Production status               | Blocked                  | DuckTalent remains Do Not Deploy with real applicants until the blocking technical and governance evidence is complete.                                                            |
| Primary documentation objective | Traceable model evidence | Establish a single controlled record linking model identity and technical evidence to the business use case, risk/impact assessments, approvals, monitoring and lifecycle changes. |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>No false completeness</strong></p>
<p>A strong model document records unknowns explicitly. For DuckTalent, filling the gaps with invented architecture, accuracy, fairness thresholds, training data, or vendor details would undermine auditability. “TBD - evidence required before deployment” is the correct governance state.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 2. Purpose, Scope, and Documentation Boundary

This record documents the AI model or model-based component used within DuckTalent once that component is selected or built. It also records system-level facts needed to understand the model in context. It is designed to be maintained throughout the lifecycle rather than completed once and archived.

### 2.1 Model versus AI system

DuckTalent AI is the governed AI system. An underlying model is only one component of that system. The same model can behave differently depending on prompts, feature engineering, job criteria, ranking logic, thresholds, retrieval sources, user interface, integrations, human review, and operating context. Model documentation therefore does not replace AI-system inventory, risk, impact, privacy, legal, or human-oversight records.

### 2.2 Source classification used in this document

| **Category**                          | **Status**                                    | **How this document uses it**                                                                                                                                                                    |
|---------------------------------------|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mandatory legal requirements          | Conditional / applicability-dependent         | Where Duckworks is legally a provider of an applicable high-risk AI system, EU AI Act technical-documentation obligations may apply. Legal role and classification must be confirmed separately. |
| Standards and framework guidance      | Voluntary unless adopted contractually/policy | NIST AI RMF and ISO public descriptions inform documentation, lifecycle, risk, and evidence practices; they do not by themselves prove compliance.                                               |
| Duckworks organizational requirements | Internal governance requirements              | Model identity, evidence, validation, monitoring, change control, human oversight, and release gates are required by the Duckworks governance design.                                            |
| Project assumptions                   | Scenario inputs, not verified facts           | EU/EEA focus, human accountability, fictional/synthetic data, and mixed internal/third-party technology are maintained as controlled assumptions.                                                |

## 3. Model and System Identity

| **Field**                     | **Current record**                       | **Evidence / action**                                                                                          |
|-------------------------------|------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| AI system ID                  | AI-005                                   | Confirmed in Duckworks portfolio                                                                               |
| AI system name                | DuckTalent AI                            | Confirmed                                                                                                      |
| Model/component ID            | TBD                                      | Assign unique immutable identifier before technical validation                                                 |
| Model name                    | TBD                                      | Not specified in project evidence                                                                              |
| Model family / algorithm type | TBD                                      | Could be rules, classical ML, NLP/LLM, hybrid, or vendor service; do not assume                                |
| Provider / developer          | TBD                                      | Project assumes a mix of internal and third-party AI but DuckTalent source is not validated                    |
| Provider legal role           | TBD                                      | Legal must determine whether Duckworks is provider, deployer, or another operator for the final implementation |
| Model version                 | TBD                                      | Version must be captured for every validation and deployment decision                                          |
| System version / release      | TBD                                      | Production release not authorized                                                                              |
| Lifecycle stage               | Concept / pre-deployment                 | Current portfolio position                                                                                     |
| Deployment form               | TBD                                      | API / SaaS / hosted / internally deployed not validated                                                        |
| Hosting / processing location | TBD                                      | Must be validated for security, privacy, data transfer and resilience analysis                                 |
| Primary business process      | Recruitment and talent acquisition       | Confirmed                                                                                                      |
| Business owner                | Beatrice Van Duck - Chief People Officer | Confirmed                                                                                                      |
| Technical owner               | Dr. Ada Duckfield - Head of Data & AI    | Confirmed                                                                                                      |
| Governance owner              | Eleanor Duckford - AI Governance Lead    | Confirmed                                                                                                      |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Release identification rule</strong></p>
<p>No evaluation result, risk acceptance, fairness test, security test or approval is valid unless it can be tied to the exact model/system version and configuration that is proposed for use.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 4. Intended Purpose, Users, and Decision Boundary

| **Element**                 | **DuckTalent model-context record**                                                                                                                                                                 |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Business need               | Reduce repetitive recruiter triage workload, improve structure/consistency of application review, and focus recruiter attention on job-relevant qualifications and experience.                      |
| Intended AI-enabled use     | Parse CVs; extract job-relevant information; compare applicants against pre-approved criteria; summarize applications; rank candidates; recommend candidates for further human review or interview. |
| Intended users              | Authorized recruiters and hiring managers.                                                                                                                                                          |
| Primary affected persons    | External job applicants; internal candidates if the use later expands to internal mobility.                                                                                                         |
| Decision role               | Decision support for consequential employment decisions.                                                                                                                                            |
| Human accountability        | Recruiters and hiring managers make and document consequential decisions; the AI is not the final decision-maker.                                                                                   |
| Current production boundary | No use with real applicants for consequential decisions until the approved governance gate changes.                                                                                                 |
| Geographic context          | EU/EEA-focused project assumption; actual countries and affected-person jurisdictions must be validated.                                                                                            |

### 4.1 Permitted, unsupported, and prohibited use

| **Permitted / intended in design**                                 | **Unsupported / prohibited in current design**                                                                      |
|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Parse CVs and extract job-relevant qualifications.                 | Automatic rejection or hiring without meaningful human decision.                                                    |
| Summarize application information for authorized reviewers.        | Facial, emotion, personality or unrelated inference for suitability.                                                |
| Compare candidates against pre-approved, job-relevant criteria.    | Use of protected/sensitive traits or unjustified proxies without a specific lawful and governance basis.            |
| Recommend candidates for further human review or interview.        | Opaque vendor ranking criteria Duckworks cannot validate or challenge.                                              |
| Support structured review while source material remains available. | Unrelated applicant-data reuse for model training, model improvement or other purposes without approved governance. |

## 5. Functional Description and Architecture

The following workflow is supported by the business-use-case and DPIA records. It is a functional narrative, not a verified technical architecture.

1.  Applicant submits a CV and approved application information through the recruitment channel / applicant tracking environment.

2.  Authorized recruitment information is made available to the DuckTalent processing layer under defined access controls.

3.  DuckTalent parses/extracts information and generates summaries, comparison indicators and/or ranking against approved role criteria.

4.  An authorized recruiter reviews source application information together with the AI output.

5.  The recruiter or hiring manager makes the consequential decision, may disregard/override the AI output, and records the decision as required.

6.  Logging, monitoring, challenge/correction, incident, and change-management processes create evidence for ongoing governance.

### 5.1 Architecture component register

| **Component**                | **Function**                                                            | **Current evidence**              | **Required artifact**                                      |
|------------------------------|-------------------------------------------------------------------------|-----------------------------------|------------------------------------------------------------|
| Recruitment / ATS interface  | Receives applications and presents authorized workflow                  | Exact product/integration TBD     | Architecture/data-flow diagram                             |
| Document ingestion / parsing | Extracts structured information from CV/application material            | Technology and parser TBD         | Component/version record; parsing validation               |
| Criteria configuration       | Stores or applies approved job criteria                                 | Weighting/logic TBD               | Approved criteria specification and version history        |
| Model / ranking component    | Produces comparison, suitability indicator and/or rank                  | Model family/provider/version TBD | Model card / vendor technical evidence / validation report |
| Human review interface       | Shows source data and model outputs to authorized users                 | UI and explanation design TBD     | User-interface specification; usability/human-factors test |
| Logging / audit trail        | Supports traceability of use, outputs, overrides, decisions and changes | Logging design TBD                | Log schema; retention; test evidence                       |
| Monitoring layer             | Tracks performance, fairness, override, complaints, incidents and drift | Metrics/thresholds TBD            | Monitoring plan and dashboard evidence                     |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Architecture evidence gate</strong></p>
<p>Before pilot or deployment, Duckworks should have a version-controlled architecture/data-flow diagram that identifies the model/service, preprocessing, feature/criteria logic, interfaces, storage, integrations, user roles, external providers, logging and monitoring points.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 6. Data Documentation

DuckTalent is expected to process applicant/recruitment information. The portfolio intentionally uses no real applicant or protected-class data. Production data design, training data, validation data, and lawful use of any sensitive/proxy information remain unresolved.

| **Data area**            | **Known / expected record**                                                                                         | **Current evidence position**                              |
|--------------------------|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| Operational input data   | CVs, application forms, qualifications, employment history, skills, and other approved recruitment information.     | Business use case documented; exact schema TBD.            |
| Derived data             | Candidate summaries, comparison/suitability indicators, rankings and recommendations.                               | Expected output types documented; calculation logic TBD.   |
| Training data            | TBD. No training corpus or fine-tuning data identified.                                                             | Not evidenced.                                             |
| Validation data          | TBD. Controlled synthetic/approved validation data required before real use.                                        | Not evidenced.                                             |
| Test data                | TBD. Must cover representative formats, languages, career patterns and error cases consistent with intended use.    | Not evidenced.                                             |
| Protected/sensitive data | Not intended for ranking unless specifically lawful, necessary and approved; may appear incidentally in CVs.        | Restriction documented; detection/minimization design TBD. |
| Data provenance          | Source, collection, licensing/rights, selection and transformation must be documented.                              | Not evidenced.                                             |
| Labeling / ground truth  | If supervised labels or historical decisions are used, source, quality and bias implications must be documented.    | Not evidenced.                                             |
| Cleaning / preprocessing | Parsing, normalization, missing values, duplicates, credential equivalence and outlier handling must be documented. | Not evidenced.                                             |
| Retention / deletion     | Production retention schedule and vendor deletion behavior must be defined.                                         | Open DPIA/vendor action.                                   |

### 6.1 Minimum training / validation / test dataset record

| **Required field**                                     | **Status for DuckTalent v1.0** |
|--------------------------------------------------------|--------------------------------|
| Dataset identifier and version                         | TBD                            |
| Purpose: training / validation / test / benchmark      | TBD                            |
| Data source and provenance                             | TBD                            |
| Collection period and geographic scope                 | TBD                            |
| Population / sample definition                         | TBD                            |
| Feature schema / modality                              | TBD                            |
| Label definition and labeling process                  | TBD                            |
| Selection / exclusion criteria                         | TBD                            |
| Cleaning / transformation / augmentation               | TBD                            |
| Known missingness / quality issues                     | TBD                            |
| Representativeness analysis                            | TBD                            |
| Sensitive / protected characteristics and proxy review | TBD                            |
| Legal/contractual rights and permitted use             | TBD                            |
| Data split and leakage controls                        | TBD                            |
| Retention / deletion / reproducibility location        | TBD                            |

## 7. Model Design and Development Record

| **Documentation element**       | **Current status** | **Evidence / next action**                                                                                        |
|---------------------------------|--------------------|-------------------------------------------------------------------------------------------------------------------|
| Model/algorithm family          | TBD                | Record whether rules, statistical ML, transformer/LLM, embedding/ranker, hybrid, or vendor service.               |
| Build / buy / adapt decision    | TBD                | Record supplier, pre-trained components, open-source components, internal code and modifications.                 |
| General model logic             | TBD                | Document how inputs become summaries/scores/ranks without exposing irrelevant proprietary detail.                 |
| Optimization objective          | Partly defined     | Business target is job-relevant comparison/reviewer support; technical loss/objective and ranking target are TBD. |
| Feature / criteria logic        | TBD                | Create approved feature/criteria allow-list, weighting/rule specification and proxy-feature challenge.            |
| Pre-trained components          | TBD                | List model names, versions, licences, use restrictions, known limitations and change dependencies.                |
| Hyperparameters / configuration | TBD                | Record material parameters and configuration used for each validation and release.                                |
| Computational resources         | TBD                | Document development/training/validation/production resources where material.                                     |
| Development environment         | TBD                | Record code repository, dependency versions, build artefacts, change approvals and reproducibility process.       |
| Explainability method           | TBD                | Document explanation/interpretation method appropriate to ranking/recommendation and reviewer needs.              |

### 7.1 Criteria and feature governance

- Job criteria must be defined and approved by HR/business owners before model validation; the model must not silently introduce new decision criteria.

- Direct, proxy and derived features should be inventoried and challenged for job relevance, legality, fairness, accessibility and potential disproportionate effects.

- Any weighting, threshold, scoring or ranking configuration must be version-controlled and traceable to an approval decision.

- If a third-party model performs opaque ranking or feature inference that Duckworks cannot validate, that is a deployment blocker rather than a documentation footnote.

## 8. Validation, Testing, and Evaluation Plan

No validated model-performance results are present in the current source set. The table below defines the evidence Duckworks should require. Candidate metrics are not acceptance thresholds; thresholds must be approved after baseline and pilot evidence exists.

| **Evaluation domain**             | **Candidate metrics / tests**                                                                                                                              | **Evidence basis**                                          | **Gate**                                                            |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|---------------------------------------------------------------------|
| Parsing / extraction quality      | Field-level precision/recall or error rate; missing-field rate; credential/language/format error patterns                                                  | Approved test set reflecting intended documents/populations | Threshold TBD before deployment                                     |
| Ranking / recommendation quality  | Ranking error/discordance; reviewer correction; top-k relevance or task-specific measure as appropriate                                                    | Validated benchmark with documented ground truth            | Metric/threshold must match actual design                           |
| Reliability / robustness          | Performance under missing data, unusual formats, adversarial/malformed documents, distribution shift and integration failure                               | Stress/edge-case test set                                   | Blocking if material failure modes lack controls                    |
| Fairness / non-discrimination     | Group-level error and selection/shortlisting indicators where lawful and methodologically appropriate                                                      | Approved fairness method and lawful data basis              | No threshold fabricated; investigation/acceptance criteria required |
| Accessibility / inclusion         | Performance on non-standard formats, disability-related accommodations, foreign qualifications, non-linear careers and language variations                 | Accessibility/user testing                                  | Blocking until material barriers addressed                          |
| Human oversight / automation bias | Source-review completion, reviewer disagreement/override, comprehension and decision-quality testing                                                       | Controlled user test                                        | Human review must be demonstrably meaningful                        |
| Explainability / interpretability | Reviewer ability to understand relevant factors, limitations and confidence/uncertainty where available                                                    | Usability/explanation testing                               | Must support correct interpretation and challenge                   |
| Privacy / data protection         | Data minimization, retention, rights handling, access and leakage tests                                                                                    | DPIA/privacy evidence                                       | Blocking legal/privacy actions must close                           |
| Security                          | Threat model, document/file handling, access, API/integration, supply-chain and adversarial tests; prompt/injection testing if generative components exist | Security test plan/report                                   | High-risk findings require treatment before release                 |
| Operational resilience            | Failure modes, fallback, service unavailability, vendor/model change and recovery                                                                          | Operational test / continuity plan                          | Human/manual fallback must remain usable                            |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Testing discipline</strong></p>
<p>Each test report should identify the exact model/system version, configuration, dataset version, evaluation method, metric definition, threshold/acceptance criterion, tester, date, result, exceptions and approval. A metric without that context is weak evidence.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 9. Performance, Known Limitations, and Failure Modes

Current validated performance: none evidenced. The following are known or reasonably foreseeable failure modes derived from the Duckworks impact/risk work; they are not claims that the system has already failed in these ways.

| **ID** | **Failure mode**                      | **Description**                                                                                                                        | **Impact** |
|--------|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|------------|
| FM-01  | Parsing error                         | CV extraction misstates qualification, employment history, skill or experience and affects comparison/ranking.                         | High       |
| FM-02  | Proxy bias / historical pattern       | Criteria, features, training data or historical labels reproduce unequal treatment.                                                    | Critical   |
| FM-03  | Non-standard applicant representation | Disability-related formats, foreign qualifications, language differences, atypical careers or career gaps are handled less accurately. | Critical   |
| FM-04  | Automation bias                       | Recruiters mechanically follow ranking or treat output as objectively correct.                                                         | Critical   |
| FM-05  | Opaque ranking logic                  | Users cannot understand or challenge material factors behind output.                                                                   | High       |
| FM-06  | Data misuse / leakage                 | Applicant data are retained, reused, exposed or sent to unauthorized parties/services.                                                 | High       |
| FM-07  | Adversarial / malformed input         | Malicious or unusual documents manipulate processing or compromise integrations.                                                       | High       |
| FM-08  | Vendor/model change                   | Provider changes model/behavior/data terms and invalidates prior evidence.                                                             | High       |
| FM-09  | Scale amplification                   | A flawed configuration is applied across many applications before detection.                                                           | Critical   |
| FM-10  | Purpose creep                         | Use expands into automatic rejection, workforce monitoring or unrelated evaluation without reassessment.                               | Critical   |

### 9.1 Model limitation statement for reviewers

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Required reviewer warning</strong></p>
<p>DuckTalent output is a decision-support signal, not an objective fact or final employment decision. Reviewers must inspect relevant source information, understand documented limitations, consider missing context and accessibility, and have authority to disregard or override the model output.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 10. Fairness, Explainability, and Human Oversight

| **Control area**         | **Minimum model-documentation requirement**                                                                                                   | **Current status**                                     |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| Fairness design          | Define fairness objectives, relevant groups, metrics, lawful data basis, limitations, investigation thresholds and remediation process.       | Not evidenced                                          |
| Feature/proxy analysis   | Document direct/proxy/derived features and reasons for inclusion/exclusion.                                                                   | Not evidenced                                          |
| Explainability           | Describe what explanations are available to recruiters, what they mean, and what they do not prove.                                           | Not evidenced                                          |
| Confidence / uncertainty | Where the model provides confidence, score or rank, document meaning, calibration/limitations and acceptable interpretation.                  | TBD - model design unknown                             |
| Source traceability      | Reviewer should be able to inspect the applicant source information underlying a material summary or recommendation.                          | Required                                               |
| Override / disregard     | Reviewer must be able to disregard/override the model output without artificial friction and record rationale where required.                 | Required; operating evidence absent                    |
| Stop / escalation        | Users and owners must know when to suspend use or escalate anomalies, discriminatory patterns, security/privacy incidents or control failure. | Defined in governance SOP; model-specific triggers TBD |
| Training                 | Recruiters/hiring managers require training on limitations, automation bias, prohibited uses and escalation.                                  | Required; delivery evidence absent                     |

## 11. Privacy, Security, and Third-Party Model Controls

The separate DuckTalent DPIA and security review remain companion records. Model documentation should contain or link the technical evidence that makes those assessments testable.

| **Domain**              | **Model documentation evidence**                                                                                                                                 | **Status**                                     |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| Identity & access       | Service identities, roles, privileges, administrative access, API credentials, separation of duties.                                                             | TBD                                            |
| Data protection         | Data flows, minimization, encryption, retention/deletion, caches/logs, processor locations, rights handling.                                                     | TBD / DPIA actions open                        |
| Model/provider data use | Whether prompts/applicant content are retained, used for provider training/improvement, or accessible to subprocessors.                                          | TBD / blocking vendor review                   |
| Supply chain            | Model provenance, dependencies, licences, open-source/vendor components, integrity verification, update sources.                                                 | TBD                                            |
| Adversarial security    | Threat model for malicious documents, prompt/instruction injection if applicable, data exfiltration, insecure tools/APIs, model abuse and excessive permissions. | TBD                                            |
| Secrets / credentials   | No credentials, secrets or unrelated restricted data in prompts/training/evaluation artefacts; secure secret management.                                         | Required                                       |
| Logging                 | Security and governance logging sufficient to reconstruct material events without indiscriminate sensitive-content retention.                                    | Design TBD                                     |
| Incident response       | Model/security/privacy incident triggers, containment, evidence preservation, vendor notification and reassessment route.                                        | Governance route exists; technical runbook TBD |
| Supplier change control | Model/version, terms, subprocessor, hosting, data-use or feature change notification and approval.                                                               | TBD / blocking contract evidence               |
| Exit / continuity       | Fallback/manual process, data/model portability where applicable, deletion, transition and service discontinuation plan.                                         | TBD                                            |

## 12. Monitoring, Drift, and Operational Control

| **Monitoring area**   | **Candidate indicators**                                                                         | **Owner**                          | **Decision rule**                                                                        |
|-----------------------|--------------------------------------------------------------------------------------------------|------------------------------------|------------------------------------------------------------------------------------------|
| Model/data quality    | Parsing errors; missing-field rates; ranking discordance/correction; distribution/format changes | HR + Data & AI                     | Thresholds TBD from validated pilot; material breach triggers investigation/reassessment |
| Human oversight       | Override/disagreement; source-review completion; decision rationale; reviewer comprehension      | HR                                 | Unexpected mechanical agreement or inability to override triggers automation-bias review |
| Fairness / inclusion  | Group-level error/selection indicators where lawful/appropriate; accessibility defects           | HR + AI Governance + Privacy/Legal | Approved fairness/accessibility method required before launch                            |
| Applicant impact      | Complaints, corrections, challenges, reconsiderations, substantiated errors                      | HR + Legal/Privacy                 | Material/repeated issues trigger investigation and potentially suspension                |
| Security / privacy    | Access violations, leakage, malicious document events, model/service compromise, vendor incident | CISO + DPO                         | Significant event triggers containment and incident process                              |
| Vendor / model change | Model/version, data-use terms, subprocessor, hosting, feature or ranking logic change            | Procurement + Technical Owner      | Material change triggers reassessment before continued reliance                          |
| Business value        | Review time, time-to-shortlist, workload distribution                                            | Business Owner                     | Benefit must be demonstrated without degrading safeguards                                |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>No fabricated thresholds</strong></p>
<p>The project evidence does not contain validated accuracy, fairness, override, complaint, drift, latency, productivity, or ROI thresholds. They remain TBD until a controlled pilot or other valid evidence supports them.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 13. Versioning, Change Control, and Reassessment

Every model release must be traceable to the evidence used to approve it. A new version is not presumed equivalent to the version previously tested.

| **Change trigger**                                                       | **Required action**                                                                                         |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| New model/provider/version or substantial configuration                  | Create/update model record; determine whether validation must be repeated; update inventory and change log. |
| Change in intended purpose, autonomy or decision authority               | Full governance reassessment; legal/privacy/impact/risk review before use.                                  |
| New data source, feature, criterion or ranking logic                     | Data/feature review; fairness/quality validation; privacy/legal triage; updated test evidence.              |
| New country, language, job family or applicant population                | Assess representativeness, performance, accessibility and legal context before expansion.                   |
| Material incident, complaint, discriminatory outcome or rights challenge | Contain as appropriate; investigate; preserve evidence; reassess model/system before resuming use.          |
| Drift or performance threshold breach                                    | Investigate root cause; restrict/suspend if safeguards are no longer effective; revalidate after treatment. |
| Vendor terms, subprocessor, hosting or data-use change                   | Re-run supplier/privacy/security review and determine whether prior approval remains valid.                 |
| Control failure or evidence expiry                                       | No continued risk credit for failed/unverified control; update residual risk and approval status.           |

### 13.1 Model change log

| **Version** | **Date** | **Change summary**                | **Reason**               | **Validation impact**             | **Approver / status** |
|-------------|----------|-----------------------------------|--------------------------|-----------------------------------|-----------------------|
| TBD         | TBD      | Initial model/component selection | Initial technical design | Full baseline validation required | Not approved          |

## 14. Evidence and Traceability Pack

| **ID** | **Evidence item**                                                    | **Gate**                  | **Current status**                                             |
|--------|----------------------------------------------------------------------|---------------------------|----------------------------------------------------------------|
| MD-01  | Unique system/model/version identifiers                              | Blocking                  | Not evidenced                                                  |
| MD-02  | Approved business use case and intended-purpose statement            | Blocking                  | Available at system level                                      |
| MD-03  | Architecture and data-flow diagram                                   | Blocking                  | Not evidenced                                                  |
| MD-04  | Model/provider technical specification and provenance                | Blocking                  | Not evidenced                                                  |
| MD-05  | Training/validation/test dataset documentation                       | Blocking where applicable | Not evidenced                                                  |
| MD-06  | Approved job-criteria / feature specification and version history    | Blocking                  | Not evidenced                                                  |
| MD-07  | Validation plan, metric definitions and acceptance thresholds        | Blocking                  | Not evidenced                                                  |
| MD-08  | Signed validation/test reports tied to exact version                 | Blocking                  | Not evidenced                                                  |
| MD-09  | Fairness and accessibility method/results                            | Blocking                  | Not evidenced                                                  |
| MD-10  | Explainability / reviewer interpretation evidence                    | Blocking                  | Not evidenced                                                  |
| MD-11  | Human-oversight design and user testing                              | Blocking                  | Not evidenced                                                  |
| MD-12  | Security threat model and test evidence                              | Blocking                  | Not evidenced                                                  |
| MD-13  | Privacy/DPIA and data-governance evidence                            | Blocking                  | DPIA draft exists; actions open                                |
| MD-14  | Third-party due diligence, contract and change-notification evidence | Blocking if third party   | Not evidenced                                                  |
| MD-15  | Monitoring plan, thresholds, owners and dashboard/log specification  | Blocking                  | Plan partially defined; model thresholds TBD                   |
| MD-16  | Incident/fallback/stop-use procedure                                 | Blocking                  | Governance route exists; model-specific technical evidence TBD |
| MD-17  | AIA / FRIA / HUDERIA / risk assessment traceability                  | Blocking                  | Companion governance artifacts exist                           |
| MD-18  | AI Governance Committee release decision                             | Final gate                | Not approved                                                   |

### 14.1 Companion records

- AI Business Use Case - business objective, intended use, users, inputs/outputs, decision boundary and value hypotheses.

- QuackTrack AI System Inventory - system ownership, lifecycle, data, provider/model and governance status.

- Algorithmic Impact Assessment - affected parties, positive/adverse impacts, fairness, security, reliability, human oversight and monitoring.

- GDPR DPIA - processing design, lawfulness, necessity/proportionality, rights risks, security/privacy controls and DPO advice.

- EU FRIA - fundamental-rights-focused analysis prepared separately for DuckTalent under the portfolio assumptions.

- HUDERIA pack - COBRA, stakeholder engagement design, risk/impact assessment, mitigation/remedies and iterative review.

- AI Risk Assessment - scenario-based inherent/current/target risk, control effectiveness and treatment.

- AI RACI and Lifecycle SOP - accountability, review, approval, release, monitoring, change and escalation procedures.

## 15. Legal and Framework Mapping

This section is a governance mapping, not a legal conclusion. Duckworks must confirm the final system classification, legal role, deployment facts and application dates before treating any conditional EU AI Act requirement as applicable to DuckTalent.

| **Source**                        | **Type**                                                 | **Potential relevance to model documentation**                                                                                                                                                                                                           | **Duckworks position**                                                                                                                                          |
|-----------------------------------|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EU AI Act - Annex III 4(a)        | Binding legal classification route where applicable      | Recruitment/selection systems that analyse/filter applications or evaluate candidates are listed in Annex III.                                                                                                                                           | DuckTalent has a strong preliminary route based on intended purpose; Legal must confirm final classification.                                                   |
| EU AI Act - Article 11 + Annex IV | Binding for providers of applicable high-risk AI systems | Technical documentation must be prepared/kept current and, at minimum, cover system description, development/design, architecture/data, validation/testing, cybersecurity, performance/limitations, risk management, changes and post-market monitoring. | This document is designed to support those evidence categories but is not represented as a complete Annex IV file. Provider role and applicability remain open. |
| GDPR / DPIA                       | Binding where applicable                                 | Applicant personal-data processing, privacy-by-design, security, rights, automated evaluation and DPIA obligations may require technical evidence about model/data behavior.                                                                             | Separate DuckTalent DPIA treats production as blocked pending validated processing design and safeguards.                                                       |
| NIST AI RMF 1.0                   | Voluntary framework                                      | Supports Govern-Map-Measure-Manage risk management, documentation, transparency, evaluation and monitoring.                                                                                                                                              | Used as guidance; not proof of compliance.                                                                                                                      |
| ISO/IEC 42001:2023                | Management-system requirements standard                  | Supports documented AI governance, roles, lifecycle controls, objectives, risk treatment and continual improvement.                                                                                                                                      | Voluntary unless adopted/contractually required; no certification claim.                                                                                        |
| ISO/IEC 5338:2023                 | AI lifecycle-process standard                            | Provides processes supporting definition, control, management, execution and improvement of AI systems through lifecycle stages.                                                                                                                         | Useful lifecycle reference; no conformity claim.                                                                                                                |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Regulatory technical-documentation boundary</strong></p>
<p>If Duckworks becomes the provider of an applicable high-risk DuckTalent system, this internal record should be expanded into a controlled technical-documentation dossier rather than merely relabelled as “Annex IV compliant.” Missing provider/model, architecture, data, testing, cybersecurity, performance and post-market evidence must be generated and validated.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 16. Approval, Lifecycle Decision, and Model Record Acceptance

| **Decision element**          | **Current record**                                                                                                                                                                                        |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lifecycle decision            | DO NOT DEPLOY with real applicants in current state.                                                                                                                                                      |
| Permitted activity            | Documentation, design, governance assessment, supplier/architecture evaluation, and controlled synthetic/approved testing consistent with project scope.                                                  |
| Production approval authority | AI Governance Committee after required Legal, Privacy, HR, Security, Risk & Compliance and technical evidence is complete.                                                                                |
| Model documentation owner     | Dr. Ada Duckfield - Head of Data & AI; coordinated with Eleanor Duckford - AI Governance Lead.                                                                                                            |
| Business accountability       | Beatrice Van Duck - Chief People Officer owns the intended purpose and business use.                                                                                                                      |
| Independent assurance         | Penelope Duckins / Internal Audit may later assess design and operating effectiveness but does not own model documentation controls.                                                                      |
| Condition to change gate      | Blocking evidence closed; model/system version fixed; validation demonstrates approved performance and safeguards; companion assessments updated; residual risk/impact accepted at the correct authority. |

### 16.1 Draft sign-off

| **Role**                | **Named stakeholder** | **Status** | **Required confirmation**                                                       |
|-------------------------|-----------------------|------------|---------------------------------------------------------------------------------|
| Business Owner          | Beatrice Van Duck     | Open       | Purpose, intended use, decision boundary, business acceptance criteria.         |
| Technical / Model Owner | Dr. Ada Duckfield     | Open       | Model identity, architecture, data, validation, monitoring and change evidence. |
| AI Governance Lead      | Eleanor Duckford      | Open       | Traceability, evidence completeness, governance gate and reassessment triggers. |
| CISO                    | Cassandra Duckley     | Open       | Security design, threat model, testing and incident readiness.                  |
| DPO                     | Delia Duckham         | Open       | Personal-data design, DPIA closure and privacy evidence.                        |
| General Counsel         | Amelia Duckett        | Open       | Legal role/classification and employment/regulatory applicability.              |
| CRCO / Committee Chair  | Reginald Duckman      | Open       | Risk treatment, exception/escalation and approval decision.                     |
| Internal Audit          | Penelope Duckins      | Observer   | Independent assurance readiness only; no operational approval ownership.        |

## 17. Reusable Duckworks Model Documentation Template

The following minimum record should be created for each material model or model-based component used in a governed AI system. It should be proportionate: a simple deterministic component may require less detail than a complex learned model, but material unknowns must still be visible.

| **Model documentation area** | **Minimum record**                                                                                                                                 |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Identity                     | System ID; model/component ID; model name/family; provider/developer; version; release; environment; owner.                                        |
| Purpose & scope              | Intended purpose; users; affected persons; decisions supported; permitted/prohibited uses; geography.                                              |
| Architecture                 | Component diagram; interfaces; preprocessing/postprocessing; integrations; hardware/hosting; dependencies.                                         |
| Data                         | Training/validation/test/operational datasets; provenance; labels; transformations; representativeness; sensitive/proxy data; retention.           |
| Design                       | Algorithm/general logic; objectives; features/criteria; parameters/configuration; pre-trained components; assumptions; trade-offs.                 |
| Evaluation                   | Metric definitions; test datasets; thresholds; accuracy/reliability; robustness; fairness; accessibility; explainability; human-factors; security. |
| Capabilities & limitations   | Supported conditions; known limitations; failure modes; uncertainty; out-of-distribution behavior; foreseeable misuse.                             |
| Human oversight              | Interpretation guidance; reviewer competence; source access; override/disregard/stop authority; automation-bias safeguards.                        |
| Security & privacy           | Threat model; access; data leakage; supply chain; vendor data use; privacy controls; logging; incident response.                                   |
| Monitoring                   | Performance/drift; fairness; overrides; complaints; incidents; vendor/model change; thresholds; owners; cadence.                                   |
| Change control               | Version history; material changes; validation impact; approvals; rollback/fallback; retirement.                                                    |
| Evidence & approval          | Linked risk/AIA/DPIA/FRIA/HUDERIA; validation reports; supplier evidence; committee decision; assurance evidence.                                  |

## 18. Source Basis and Limitations

| **Source / evidence**                                        | **Use in this model document**                                                                                        |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Duckworks Business Scenario                                  | DuckTalent purpose, recruitment problem, human-review intent, governance context.                                     |
| Duckworks Readiness Assessment                               | Critical DuckTalent risk position, evidence maturity and cross-functional governance need.                            |
| Duckworks Assumptions Register                               | Human accountability; DuckTalent advisory purpose; data/provider assumptions; legal-classification boundary.          |
| Duckworks Scope / Acceptance Criteria                        | Synthetic-data boundary, technical testing limits, current Do Not Deploy gate and evidence expectations.              |
| Duckworks Business Use Case Portfolio                        | Business owner, technical owner, inputs/outputs, permitted/prohibited uses, value measures and current gate.          |
| DuckTalent AIA / DPIA / FRIA / HUDERIA records               | Impact, privacy, rights, stakeholder, mitigation and evidence requirements.                                           |
| Duckworks AI Risk Methodology / RACI / Lifecycle SOP         | Risk, accountability, approval, monitoring, change and escalation expectations.                                       |
| EU AI Act consolidated text, 27 July 2026 - EUR-Lex          | Conditional legal mapping for Annex III recruitment classification and Article 11 / Annex IV technical documentation. |
| NIST AI RMF 1.0 / NIST AI RMF Playbook                       | Voluntary risk-management and documentation guidance.                                                                 |
| ISO/IEC 42001:2023 and ISO/IEC 5338:2023 public descriptions | AI management-system and lifecycle-process reference points; full standards not reproduced.                           |

### Official public references:

- EU AI Act consolidated text (27 July 2026): https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R1689-20260727

- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework

- NIST AI RMF Playbook: https://airc.nist.gov/airmf-resources/playbook/

- ISO/IEC 42001:2023 public page: https://www.iso.org/standard/42001

- ISO/IEC 5338:2023 public page: https://www.iso.org/standard/81118.html

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Final portfolio position</strong></p>
<p>This document demonstrates how Duckworks would maintain an audit-ready model record without fabricating unavailable technical facts. DuckTalent remains blocked from production. The next legitimate step is to select or design the actual model/service, assign a versioned model ID, produce the missing architecture/data/provider evidence, execute approved validation and security/fairness testing, and then re-issue this record as a validated model documentation baseline.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Portfolio disclaimer: Duckworks, Project W.I.N.G., all personnel, systems, models, datasets, decisions and evidence are fictional or synthetic. No real applicant records, employer-confidential information, certification claims or legal opinions are represented.
