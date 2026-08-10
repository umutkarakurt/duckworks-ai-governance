# Duckworks AI Data Management Plan

**DUCKWORKS**

AI Data Management Plan

Data governance, provenance, quality, access, lifecycle, retention and evidence requirements for Project W.I.N.G.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Plan objective</strong></p>
<p>Define how Duckworks identifies, sources, classifies, documents, prepares, accesses, shares, validates, monitors, retains and disposes of data used by or generated through AI systems. The plan covers personal and non-personal data, confidential intellectual property, model-development datasets, retrieval/knowledge sources, prompts, outputs, logs, labels, embeddings and third-party data dependencies.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| **Field**               | **Value**                                              |
|-------------------------|--------------------------------------------------------|
| Document ID             | DW-WING-DATA-01                                        |
| Version                 | 1.0                                                    |
| Status                  | Portfolio Baseline                                     |
| Organization            | Duckworks (fictional)                                  |
| Plan owner              | Dr. Ada Duckfield — Head of Data & AI                  |
| Governance coordination | Eleanor Duckford — AI Governance Lead                  |
| Privacy adviser         | Delia Duckham — Data Protection Officer                |
| Security challenger     | Cassandra Duckley — Chief Information Security Officer |
| Scope                   | AI-001 through AI-007 and future material AI use cases |
| Classification          | Portfolio / Synthetic / Non-production                 |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Data principle</strong></p>
<p>No material AI dataset without a purpose, owner and provenance record; no sensitive data without an approved handling basis; no model or retrieval source without quality criteria; and no material data change without traceable reassessment.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 1. Executive Summary

Duckworks' AI portfolio uses different forms of data: engineering and design information, customer support content, operational supply-chain data, manufacturing images, applicant information, employee knowledge sources and user-generated prompts. The portfolio also includes an uncontrolled condition - AI-007 Unregistered GenAI Usage - where the organization may not know which data was submitted, where it was processed, whether it was retained, or whether a supplier reused it.

This plan establishes a common data-management lifecycle while remaining proportionate to use-case impact. It does not assume that every AI system trains a model, processes personal data, or is legally classified as high-risk. Each system must document its actual data flows and apply only the controls triggered by verified facts.

| **System**                | **Data scope**                                                                                                 | **Primary concern**                                  | **Current gate**                 |
|---------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------|----------------------------------|
| AI-001 DuckDesign         | Engineering requirements, CAD/design artifacts, material/simulation information, prompts and technical outputs | High confidentiality / safety relevance              | Restricted pilot                 |
| AI-002 QuackBot           | Approved product/support knowledge, user/customer prompts, interaction content and logs                        | Personal-data possible; customer/safety relevance    | Production blocked pending gates |
| AI-003 FeatherForecast    | Operational forecasting inputs and resulting demand/inventory/manufacturing forecasts; exact source schema TBD | Operational integrity / quality                      | Continue with monitoring         |
| AI-004 WingInspect        | Production-line images, defect/inspection labels and results; personal data presence TBD                       | Safety/quality relevance                             | Restricted pilot                 |
| AI-005 DuckTalent         | CV/application information, qualifications, experience, job criteria, rankings and summaries                   | Applicant personal data / fairness                   | Do not deploy                    |
| AI-006 PondGPT            | Employee prompts, internal documents/knowledge, code, meeting/process content, retrieval data and logs         | Confidential/personal data likely                    | Restricted pilot                 |
| AI-007 Unregistered GenAI | Unknown prompts/files/data submitted to unapproved services                                                    | Uncontrolled confidentiality/privacy/vendor exposure | Immediate containment            |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Current evidence limitation</strong></p>
<p>The business scenario defines purposes and broad data categories, but it does not provide verified production schemas, actual training datasets, vendor architecture, processing locations, retention configurations or complete data-flow evidence. Those items are therefore treated as validation requirements, not invented facts.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 2. Purpose and Scope

### 2.1 In scope

- Data used to train, fine-tune, validate, test or evaluate AI/ML models where Duckworks controls or materially influences those datasets.

- Input data used by acquired or hosted AI systems where Duckworks controls the input.

- Retrieval-augmented generation (RAG), vector-store, search-index, knowledge-base and reference data.

- User prompts, uploaded files, images, messages, API payloads and contextual data.

- AI outputs including text, code, summaries, recommendations, rankings, classifications, embeddings, forecasts and defect flags.

- Labels, annotations, derived features, metadata, dataset statistics and data-quality records.

- System, security, human-oversight, audit and model-performance logs.

- Third-party datasets, model-provider data dependencies and supplier processing of Duckworks data.

- Synthetic, anonymized, pseudonymized and test data used for portfolio or operational validation.

- Retention, deletion, archival, legal hold, exit, portability and destruction evidence.

### 2.2 Out of scope / separate processes

- This plan is not a substitute for a GDPR Data Protection Impact Assessment where one is legally required.

- It does not provide a formal EU AI Act legal classification or conformity assessment.

- It does not replace Duckworks' enterprise information-classification, records-management, cybersecurity, software-development or business-continuity processes; it adds AI-specific requirements.

- It does not authorize use of real portfolio data. Portfolio artifacts remain fictional, synthetic, anonymized or public.

- Detailed production data engineering, model training and technical penetration testing remain outside the initial portfolio implementation boundary.

## 3. Legal, Standards and Internal-Control Classification

| **Classification**            | **Source**                            | **Data-management use**                                                                                                                                                          | **Applicability caution**                                                   |
|-------------------------------|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| MANDATORY LEGAL - conditional | GDPR Article 5                        | Lawfulness/fairness/transparency, purpose limitation, minimisation, accuracy, storage limitation, integrity/confidentiality and accountability for personal data.                | Applies only to processing of personal data within GDPR scope.              |
| MANDATORY LEGAL - conditional | GDPR Articles 25, 28, 30, 32, 35      | Data protection by design/default; processor arrangements; records; security; DPIA where likely high risk.                                                                       | Role, processing and risk facts must be verified.                           |
| MANDATORY LEGAL - conditional | EU AI Act Article 10                  | Data-governance and quality practices for training/validation/testing data for high-risk AI providers; testing data for certain high-risk systems not using training techniques. | Only where the high-risk/provider conditions and applicable timing are met. |
| MANDATORY LEGAL - conditional | EU AI Act Article 26(4)               | Where a high-risk deployer controls input data, it must ensure input data is relevant and sufficiently representative for the intended purpose.                                  | Conditional on legal high-risk/deployer status and control over input data. |
| MANDATORY LEGAL - conditional | EU AI Act Articles 12 / 26            | Logging/traceability requirements for high-risk AI and deployer log retention where applicable.                                                                                  | Do not apply as a universal Duckworks log rule.                             |
| VOLUNTARY FRAMEWORK           | NIST AI RMF 1.0 / Playbook            | Document data collection/selection, representativeness, suitability, lineage, metadata, third-party data and TEVV considerations.                                                | Guidance, not law.                                                          |
| VOLUNTARY STANDARD            | ISO/IEC 42001:2023 public description | Management-system approach to responsible AI with traceability, transparency and continual improvement.                                                                          | This plan does not reproduce ISO clauses or claim conformity.               |
| DUCKWORKS CONTROL             | Project W.I.N.G.                      | Dataset records, no-training default for vendor use, quality gates, lineage, change control, evidence and system-specific handling rules.                                        | Internal governance requirements.                                           |
| PROJECT ASSUMPTION            | Duckworks fictional scenario          | Mixed internal/third-party AI and possible processing of IP, customer, employee and applicant data.                                                                              | Validate in real deployment.                                                |

## 4. Duckworks AI Data Management Principles

| **Principle**                           | **Duckworks rule**                                                                                                                                          |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Purpose before collection               | Every material data asset is linked to an approved AI purpose and documented use. Secondary use requires compatibility/authority review and change control. |
| Provenance before trust                 | Source, collection origin, rights, transformation history and known limitations are recorded before the data can support a material AI decision.            |
| Minimum necessary data                  | Sensitive or personal data is not collected merely because it may improve a model. Necessity and proportionality must be justified.                         |
| Quality is context-specific             | Data is evaluated against the intended AI task and population/context; 'clean' data is not automatically suitable data.                                     |
| Train / validate / test integrity       | Where Duckworks trains models, dataset roles and leakage controls must preserve meaningful evaluation.                                                      |
| Human review does not cure bad data     | Human oversight is a separate control and cannot justify knowingly unsuitable, biased or corrupted data.                                                    |
| Third-party data remains Duckworks risk | Licensing, privacy, bias, provenance and security of external data/model dependencies must be assessed.                                                     |
| Outputs are governed data               | Prompts, outputs, embeddings and logs can contain confidential or personal data and inherit appropriate controls.                                           |
| Change is a reassessment trigger        | Material changes to data source, feature, label, RAG corpus, retention, vendor data use or permissions reopen affected assessments.                         |
| Evidence over assertion                 | Claims of data quality, deletion, no-training, access control or representativeness require supporting evidence.                                            |

## 5. Data Governance Roles and Accountability

| **Role**                                            | **Data-management responsibility**                                                                                                         |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Business / AI System Owner                          | Defines intended purpose, business need, affected people and acceptable use; accountable for system-level data decisions and remediation.  |
| Head of Data & AI - Dr. Ada Duckfield               | Plan owner; defines AI/ML data standards, dataset documentation, quality/lineage requirements, technical validation and monitoring design. |
| AI Governance Lead - Eleanor Duckford               | Ensures DMP evidence links to inventory, risk/impact assessments, approvals, change control and committee reporting.                       |
| DPO - Delia Duckham                                 | Advises independently on personal data, DPIA need, minimisation, retention, rights, transfers and privacy controls.                        |
| CISO - Cassandra Duckley                            | Challenges access, encryption, data leakage, prompt/RAG security, model supply chain, logs, secrets and incident controls.                 |
| General Counsel - Amelia Duckett                    | Reviews legal basis, data rights/licensing, contracts, AI Act role/classification and material legal questions.                            |
| Procurement & Vendor Assurance - Percival Duckworth | Obtains vendor data-use, retention, training, subprocessors, locations, deletion and assurance evidence.                                   |
| HR / CPO - Beatrice Van Duck                        | Owns job-relevance, applicant process/data decisions and enhanced review for DuckTalent.                                                   |
| Product Safety & Quality - Quentin Duckwell         | Challenges data/label quality where design or defect-detection data may affect product safety.                                             |
| Data Steward / Dataset Owner                        | Named owner for each material dataset or corpus; maintains quality, lineage, access, retention and issue records.                          |
| Internal Audit - Penelope Duckins                   | Provides independent assurance over design/operation; does not own dataset controls or approve operational data use.                       |

### 5.1 Minimum ownership rule

- Every material dataset/corpus must have one accountable Dataset Owner or Data Steward.

- A dataset cannot be 'owned by the model' or 'owned by the vendor'; Duckworks must identify an accountable internal owner for its use.

- The DPO, CISO, Legal and Internal Audit are challengers/advisers/assurers, not substitutes for first-line data ownership.

- For AI-007, ownership is assigned only after individual use cases are discovered and decomposed.

## 6. AI Data Lifecycle

| **Stage**              | **Required activity**                                                                                               | **Primary evidence**           |
|------------------------|---------------------------------------------------------------------------------------------------------------------|--------------------------------|
| 1\. Identify           | Register data asset/corpus, owner, system, purpose, sensitivity and legal/privacy flags.                            | AI Data Asset Register         |
| 2\. Source & authorize | Confirm origin, rights, collection purpose, supplier terms and allowed use.                                         | Provenance / rights record     |
| 3\. Profile            | Assess volume, schema, missingness, duplication, distribution, sensitive attributes, quality and known limitations. | Data profile                   |
| 4\. Prepare            | Clean, normalize, label, annotate, enrich or aggregate under version control; preserve transformations.             | Transformation log             |
| 5\. Validate           | Test suitability, representativeness, error, leakage, bias, contextual fit and task-specific acceptance criteria.   | Quality/validation report      |
| 6\. Approve            | Obtain system/data owner and triggered specialist approvals before material use.                                    | Data readiness gate            |
| 7\. Use                | Restrict access and use to approved purpose; log material changes and exceptions.                                   | Access / processing evidence   |
| 8\. Monitor            | Track drift, staleness, quality incidents, rights/privacy/security events and performance impact.                   | Data monitoring record         |
| 9\. Change             | Reassess source, schema, corpus, label, feature, vendor, retention or purpose changes.                              | AI Change Management record    |
| 10\. Retire / delete   | Archive only where justified; delete/return/disable data and derived copies according to retention and contracts.   | Deletion / retirement evidence |

## 7. Duckworks AI Data Categories

| **Data category**      | **Definition**                                                                                                        | **Duckworks treatment**                                                                  |
|------------------------|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Training data          | Data used to fit/model parameters.                                                                                    | Only where Duckworks or a supplier trains/fine-tunes; exact presence must be documented. |
| Validation data        | Data used to tune/select models or configurations without training on the test set.                                   | Separate where needed to preserve evaluation integrity.                                  |
| Test / evaluation data | Held-out or controlled data used to assess model/system performance.                                                  | Must reflect intended use/context and be versioned.                                      |
| Input / inference data | Data supplied at run time: prompts, files, images, records, feature values, API payloads.                             | Can include personal/confidential data; system-specific rules apply.                     |
| RAG / reference data   | Knowledge bases, vector stores, search indexes, manuals and internal repositories retrieved at inference.             | Source authorization, staleness, permissions and injection risk are critical.            |
| Labels / annotations   | Human- or machine-created targets, defect labels, categories, evaluation judgments.                                   | Annotator competence, instructions, disagreement and provenance required.                |
| Derived features       | Engineered variables, normalized values, scores, embeddings and intermediate representations.                         | May preserve or reveal sensitive information; lineage required.                          |
| Outputs                | Forecasts, rankings, recommendations, summaries, generated text/code, defect flags and other results.                 | Governed by downstream use, retention and affected-person impact.                        |
| Logs / telemetry       | Prompts/outputs, user/session identifiers, model version, access, errors, overrides, security and performance events. | Retention/minimisation/privacy balanced against auditability.                            |
| Synthetic data         | Artificially generated data used for testing, simulation or model development.                                        | Must be labeled synthetic; privacy and validity claims require evidence.                 |

## 8. Information Classification and Handling

The four levels below are an AI-specific Duckworks working classification for this portfolio. In a real organization they must map to the existing corporate information-classification standard rather than create a competing taxonomy.

| **Class**    | **Examples**                                                                                                                                                | **AI handling baseline**                                                                                                           |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Public       | Approved public product information, public standards/guidance, approved public datasets.                                                                   | May be used only where license/provenance is acceptable; public does not mean unrestricted intellectual-property use.              |
| Internal     | Routine internal operating information with limited sensitivity.                                                                                            | Approved enterprise AI only; no uncontrolled external sharing.                                                                     |
| Confidential | Engineering IP, source code, internal procedures, supplier/customer commercial data, non-public product information.                                        | Approved systems/providers; least privilege; encryption; vendor no-training default; controlled logs.                              |
| Restricted   | Applicant/employee/customer personal data, special-category data, credentials/secrets, privileged legal material, highly sensitive safety/security records. | Default prohibit from GenAI unless specifically approved; enhanced privacy/security review; strict access/retention; no public AI. |

### 8.1 Absolute data exclusions unless expressly authorized

- Passwords, API keys, access tokens, private keys or authentication secrets.

- Unnecessary special-category or criminal-conviction personal data.

- Legally privileged material in tools not expressly approved for that purpose.

- Production safety/security data in public or unassessed AI services.

- Applicant/customer/employee records in unregistered public GenAI services.

- Data whose license, provenance or right to use for the AI purpose cannot be established.

## 9. AI Data Asset Register, Lineage and Provenance

| **Register field**              | **Minimum record**                                                                                         |
|---------------------------------|------------------------------------------------------------------------------------------------------------|
| Data Asset ID                   | DW-DATA-\[AI ID\]-\[NN\]                                                                                   |
| Name / description              | Human-readable dataset, corpus, source table, image set, knowledge base or log stream.                     |
| AI system(s)                    | AI IDs consuming or generating the asset.                                                                  |
| Dataset owner / steward         | Named first-line accountable person/function.                                                              |
| Approved purpose                | Specific use; training / validation / test / RAG / inference / monitoring / other.                         |
| Source / origin                 | Internal system, user, supplier, public source, synthetic generation, vendor/service.                      |
| Collection context              | Why and how the source data was originally collected; required for personal-data and suitability analysis. |
| Rights / license                | Ownership, contract/license, permitted AI/ML use, restrictions, attribution.                               |
| Data subjects / affected groups | Where relevant.                                                                                            |
| Classification                  | Public / Internal / Confidential / Restricted.                                                             |
| Personal data?                  | No / Possible / Yes; categories if yes.                                                                    |
| Geography / processing location | Known locations and transfer route.                                                                        |
| Transformations                 | Cleaning, filtering, labeling, feature engineering, embeddings, augmentation, deduplication.               |
| Version                         | Immutable version/hash/release identifier.                                                                 |
| Quality status                  | Draft / Conditional / Approved / Suspended / Retired.                                                      |
| Retention / deletion            | Approved schedule and deletion trigger.                                                                    |
| Downstream dependencies         | Models, reports, vector indexes, exports, decisions or systems depending on this data.                     |

### 9.1 Lineage requirements

- For material AI decisions, Duckworks must be able to trace source data -\> transformations -\> dataset/corpus version -\> model/service version -\> output/decision evidence.

- Data copied into vector stores, feature stores, training snapshots, caches, exports or vendor support environments must not disappear from the lineage record.

- Where exact upstream provenance is unavailable, the asset is flagged 'Unknown/Partial Provenance' and cannot receive full data-quality approval for a high-impact use.

- Third-party datasets require provenance and license evidence sufficient to determine permitted AI use; 'publicly accessible' is not treated as proof of unrestricted reuse rights.

## 10. Data Quality Management

| **Dimension**            | **Question**                                                                                        | **Evidence examples**                                  |
|--------------------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| Relevance                | Does the data represent information needed for the intended task rather than merely available data? | Domain review / feature-source rationale               |
| Representativeness       | Does it reasonably reflect intended populations, products, environments or contexts?                | Distribution comparison / coverage analysis            |
| Accuracy / correctness   | Are values, labels and records factually/operationally correct for their purpose?                   | Sampling / source reconciliation / label QA            |
| Completeness             | Are required fields/cases present; are missing data patterns understood?                            | Completeness thresholds / missingness analysis         |
| Consistency              | Do values, units, definitions and labels follow stable rules across sources/time?                   | Schema/constraint tests                                |
| Timeliness / freshness   | Is the data current enough for the intended use?                                                    | Freshness SLA / source timestamps                      |
| Uniqueness / duplication | Are duplicates or repeated entities controlled where they distort model behavior?                   | Deduplication tests                                    |
| Validity                 | Do values conform to defined types, ranges, formats and domain rules?                               | Automated validation rules                             |
| Label quality            | Are labels/annotations defined, competent, reproducible and reviewed?                               | Inter-annotator / adjudication evidence where material |
| Integrity                | Has the data been protected against unauthorized or accidental alteration?                          | Hash/version/access/change evidence                    |

### 10.1 Data quality gate

☐ Acceptance criteria are defined before production use or training.

☐ Known missingness, errors, outliers and exclusions are documented with rationale.

☐ Material quality defects are linked to downstream system risk and not hidden by aggregate accuracy metrics.

☐ High-impact systems receive disaggregated/segment testing where context and lawful data permit.

☐ Data quality approval expires or is reassessed after material source/schema/context change or observed drift.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>DuckTalent caution</strong></p>
<p>For DuckTalent, 'historical recruitment data' is not assumed to be suitable merely because it exists. Any future training, ranking-feature or evaluation dataset would require job-relevance, proxy-bias, representation, privacy and fairness analysis before use. The current portfolio does not claim that such a dataset has been approved.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 11. Bias, Representativeness and Data Gaps

| **Area**                        | **Duckworks requirement**                                                                                                                             |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Population / context definition | Define who/what the system is intended to operate on before assessing representativeness.                                                             |
| Proxy review                    | Identify variables/labels that may proxy protected, sensitive or irrelevant characteristics.                                                          |
| Historical bias                 | Document whether source data reflects past policies/processes that could embed undesirable patterns.                                                  |
| Sampling / coverage             | Identify underrepresented products, environments, languages, user types, defect classes or applicant profiles.                                        |
| Feedback loops                  | Identify when AI outputs become future input data, potentially reinforcing earlier errors or decisions.                                               |
| Data gaps                       | Record missing contexts that cannot be adequately represented and convert them into use restrictions or targeted data collection.                     |
| Mitigation                      | Use redesign, additional data, reweighting, targeted evaluation, changed criteria or use restrictions only where technically and legally appropriate. |

## 12. Annotation and Label Management

- Annotation instructions must define the construct/label, inclusion/exclusion rules, uncertainty handling and examples.

- Annotators must have appropriate domain competence for safety, engineering, recruitment or quality labels.

- The source of labels - human, machine, weak supervision, legacy business rule or vendor - must be recorded.

- Material disagreements are measured and adjudicated; forced certainty should not replace an 'uncertain/not assessable' label where appropriate.

- Changes to label taxonomy are versioned and treated as material data changes when they can alter model behavior or evaluation conclusions.

- Personal data in annotation environments follows the same privacy and access rules as the source dataset.

## 13. Training, Validation and Test Dataset Controls

These controls apply only where Duckworks trains, fine-tunes or directly manages model-development datasets. Acquired AI may instead require supplier evidence demonstrating equivalent data-governance practices where contractually and legally relevant.

| **Dataset role**                  | **Purpose**                      | **Control**                                                                                 |
|-----------------------------------|----------------------------------|---------------------------------------------------------------------------------------------|
| Training                          | Fit parameters / learn patterns  | Document source, version, preprocessing, rights, sampling and approved purpose.             |
| Validation                        | Tune/select model/configuration  | Prevent inappropriate reuse that makes reported results optimistic.                         |
| Test / holdout                    | Independent performance estimate | Restrict access/reuse where leakage would undermine evaluation.                             |
| Challenge / edge-case             | Stress rare/high-impact cases    | Maintain separately where needed; do not report as representative prevalence.               |
| Post-deployment monitoring sample | Assess live/context drift        | Sampling and privacy must be defined; do not silently feed production data into retraining. |

☐ Dataset splits and snapshot versions are reproducible.

☐ Leakage checks consider duplicates, near-duplicates, temporal leakage and target-derived features.

☐ Retraining with production data requires an approved change and new provenance/rights/privacy review.

☐ Performance results identify which dataset/version produced the metric.

## 14. RAG, Knowledge Base and Retrieval Data Management

| **Control**                  | **Requirement**                                                                                                                 |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Source approval              | Only approved repositories/content classes may be indexed or retrieved.                                                         |
| Permission inheritance       | Retrieval must not grant a user access to content they could not access in the source system.                                   |
| Freshness                    | Owner and update cadence are recorded; stale/obsolete documents are removed or clearly marked.                                  |
| Authoritativeness            | Critical policies, engineering instructions, warranty or safety content identify authoritative versions.                        |
| Content provenance           | Responses should retain sufficient source reference/provenance for material use where technically feasible.                     |
| Poisoning / prompt injection | Untrusted content is treated as data, not instructions; security tests cover indirect prompt injection and malicious documents. |
| Deletion propagation         | Deleted/expired source content is removed from index/vector store/caches within the defined process.                            |
| Embeddings                   | Embeddings/vector records inherit source classification, retention and access restrictions.                                     |
| Corpus change                | Material additions/removals/re-indexing trigger change screening and targeted regression tests.                                 |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>PondGPT architecture gap</strong></p>
<p>PondGPT's permission-aware retrieval boundary is a Critical open assumption in the project. The plan therefore requires architecture and access evidence before sensitive repositories can be approved; it does not assume that cross-user leakage is already prevented.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 15. Personal Data and Privacy Management

Where an AI data asset contains personal data, Duckworks applies GDPR requirements based on the actual controller/processor roles and processing facts. Confidential business data that is not personal data remains governed by security, IP and contractual controls even when GDPR does not apply.

| **Privacy area**          | **Duckworks requirement**                                                                                                                             |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lawfulness / transparency | Record the lawful basis and relevant notice/transparency route; do not infer legal basis from the AI use case name.                                   |
| Purpose limitation        | Document original collection purpose and assess reuse for AI; incompatible reuse requires a different lawful basis/authority or must not proceed.     |
| Minimisation              | Use only necessary categories/fields and reduce prompt/retrieval exposure where possible.                                                             |
| Accuracy                  | Provide correction mechanisms where inaccurate personal data can materially influence outputs/decisions.                                              |
| Storage limitation        | Define retention by purpose; GDPR does not create one universal AI retention period.                                                                  |
| Privacy by design/default | Restrict default access, amount, duration and exposure of personal data.                                                                              |
| Processor controls        | Use approved DPA/processor terms and document subprocessors, transfers, deletion and audit evidence.                                                  |
| Records                   | Maintain GDPR processing records where Article 30 applies and link them to the AI system/data record.                                                 |
| Security                  | Apply technical/organizational measures appropriate to risk, including access, encryption/pseudonymisation where appropriate, resilience and testing. |
| DPIA                      | Perform a separate DPIA before processing where Article 35's high-risk trigger is met; review if the processing risk changes.                         |

### 15.1 High-sensitivity data rule

- Special-category and criminal-conviction data are prohibited from AI processing unless a specific lawful, necessary and approved use is documented.

- DuckTalent must not infer or introduce sensitive/protected characteristics for unrelated ranking purposes.

- PondGPT/QuackBot must not use personal interaction data for supplier model improvement by default unless separately approved and documented.

- Unregistered public AI use with applicant, employee or customer personal data is not permitted.

## 16. Security, Access and Environment Separation

| **Control area**       | **Requirement**                                                                                                                               |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Identity and access    | Role-based/least privilege; strong authentication; separate privileged administration; periodic access review.                                |
| Secrets                | Never place credentials/tokens/keys in training data, prompts, knowledge corpora or code-generation context.                                  |
| Encryption             | Protect sensitive data in transit and at rest using approved enterprise controls.                                                             |
| Environment separation | Separate development/test/production data access; production personal data is not copied into lower environments without approved protection. |
| DLP / egress           | Monitor/prevent sensitive uploads to unapproved AI services; define exceptions and investigation route.                                       |
| Logging                | Record material data access, model/corpus version, security events and high-impact decisions while minimising unnecessary personal data.      |
| Integrity              | Version/hashes/change records protect datasets, labels and critical knowledge sources from unauthorized modification.                         |
| Backup / recovery      | Backups follow the same classification and deletion/retention requirements; recovery is tested where operationally material.                  |
| Prompt/RAG security    | Test indirect prompt injection, data exfiltration and privilege amplification for GenAI applications.                                         |

## 17. Third-Party Data and Model Provider Management

| **Vendor data issue**            | **Duckworks requirement**                                                                                                                |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Data-use purpose                 | Document whether vendor uses Duckworks inputs/outputs/logs solely to provide the service or for its own purposes.                        |
| Model improvement                | Duckworks default: no shared-model training, fine-tuning or service improvement using Duckworks Customer Data unless expressly approved. |
| Retention                        | Document content/log/support/backups/embeddings retention and configuration; verify deletion capability.                                 |
| Subprocessors / model providers  | Maintain current list, functions, locations and material-change notices.                                                                 |
| Processing locations / transfers | Verify locations and applicable transfer mechanism for personal data.                                                                    |
| Data rights / licensing          | Vendor must have rights to necessary components; Duckworks must understand restrictions on supplied datasets/models.                     |
| Security / assurance             | Obtain current scoped evidence appropriate to risk; certification alone is not proof of AI data quality.                                 |
| Change notices                   | Model/service/data-use/retention/subprocessor changes enter AI Change Management.                                                        |
| Exit / deletion                  | Export required data/evidence; remove vendor access; obtain deletion evidence where contractually required.                              |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Contract alignment</strong></p>
<p>The Data Management Plan must remain consistent with the Duckworks AI Vendor Contract and AI Data Processing Agreement. The DPA already requires explicit documentation of AI data use/model improvement settings, retention, backups, retrieval stores, embeddings, logs, subprocessors and deletion evidence where applicable.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 18. Prompts, Outputs, Embeddings and Logs

| **Data artifact**            | **Management rule**                                                                                                                                    |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Prompts / uploaded content   | Classify according to underlying data; minimize logging content where metadata is sufficient; prohibit secrets/restricted data in unapproved services. |
| Outputs                      | Retain only where business, audit, safety, legal or quality purpose justifies; downstream records may become official business records.                |
| Rankings / recommendations   | Link to system/data/model version and human decision record where consequential.                                                                       |
| Embeddings / vector records  | Treat as derived data that can preserve sensitive information; inherit source access and retention.                                                    |
| Model telemetry              | Use for drift/performance/security with defined fields, access and retention.                                                                          |
| Human override / review logs | Capture enough evidence to demonstrate meaningful oversight without excessive employee surveillance.                                                   |
| Incident evidence            | Preserve under incident/legal hold when needed even if ordinary retention would otherwise expire.                                                      |

## 19. Retention, Archival and Deletion

Duckworks does not adopt one universal retention period for AI data. Every material asset must have a purpose-based retention rule consistent with legal, contractual, operational, safety, audit and privacy requirements. Where personal data is involved, GDPR storage limitation applies; where a legally high-risk AI logging rule applies, that requirement is assessed separately.

| **Data category**            | **Retention rule**                         | **Owner**              | **End-of-life action**                      | **Evidence**                  |
|------------------------------|--------------------------------------------|------------------------|---------------------------------------------|-------------------------------|
| Source / training data       | \[purpose + approved duration\]            | Dataset Owner          | Delete / archive justified snapshot         | Deletion job / archive record |
| Validation / test data       | \[duration supporting model evidence\]     | Technical Owner        | Delete / controlled archive                 | Evidence index                |
| RAG / knowledge content      | \[source system rule + index refresh\]     | Repository Owner       | Remove from index/vector store/caches       | Index/deletion evidence       |
| Prompts / outputs            | \[purpose-specific; minimize\]             | System Owner           | Delete / redact / retain as business record | Config + sample test          |
| Logs / telemetry             | \[security/audit/performance/legal basis\] | Technical Owner / CISO | Delete/aggregate/archive                    | Log-retention config          |
| Vendor copies / support data | \[contract/DPA\]                           | Procurement / DPO      | Return/delete                               | Vendor certificate/evidence   |
| Backups                      | \[enterprise backup schedule\]             | IT                     | Expiry/secure destruction                   | Backup policy/config          |

- Deletion must propagate to derived copies that are within Duckworks' control where the purpose requires deletion.

- If data cannot be deleted from a model or immutable backup in the ordinary way, Legal/Privacy/Security/Technical owners must document the limitation, residual exposure and compensating controls rather than claiming deletion.

- Legal hold, incident preservation and product-safety evidence can override ordinary deletion only under an approved basis and scope.

## 20. Synthetic, Anonymized and Pseudonymized Data

| **Type**           | **Duckworks rule**                                                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Synthetic data     | Label clearly; record generator/source and intended validity; test whether synthetic patterns realistically cover the target condition.   |
| Pseudonymized data | Still personal data under GDPR where re-identification remains possible; protect linkage keys separately.                                 |
| Anonymized data    | Do not label as anonymous solely because names were removed; the anonymization conclusion requires defensible re-identification analysis. |
| Portfolio data     | Only fictional, synthetic, anonymized or public data may be used in portfolio artifacts.                                                  |

## 21. Data Change Management

| **Data change**                               | **Required response**                                                              |
|-----------------------------------------------|------------------------------------------------------------------------------------|
| New data source / repository                  | Run CM-03 change screen; provenance, rights, privacy, security and quality review. |
| New feature / label / ranking criterion       | Reassess validity, bias/fairness, explainability and downstream impact.            |
| RAG corpus material addition/removal          | Security/injection, permission, content-quality and regression testing.            |
| Retraining / fine-tuning                      | New dataset snapshot, lineage, privacy/rights, performance and risk reassessment.  |
| Schema / unit / sensor / camera change        | Revalidate data contracts and performance assumptions.                             |
| New population / geography / language         | Representativeness/context/legal review.                                           |
| Vendor retention/training/subprocessor change | Procurement/Legal/DPO/CISO review and contract/DPA impact.                         |
| Retention or logging change                   | Privacy/security/auditability review.                                              |
| Data incident / poisoning / corruption        | Incident containment, evidence preservation and reassessment.                      |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Change-control link</strong></p>
<p>Duckworks' AI Change Management Process already treats new training/reference data, RAG sources, features, data categories, vendor data-use terms, retention, connectors and permissions as CM-C2/CM-C3 triggers where material. This plan supplies the data-specific evidence required by that process.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 22. AI Data Incident and Quality Event Management

| **Event**                                    | **Minimum response**                                                                                                                                   |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Privacy/confidentiality disclosure           | Contain access/egress; preserve evidence; invoke Security/Privacy incident routes; assess vendor notification and data-subject/regulatory obligations. |
| Data poisoning / malicious retrieval content | Isolate source/corpus; disable retrieval/retrain path; security investigation; validate clean baseline.                                                |
| Corrupted or wrong-version dataset           | Stop training/deployment affected by the data; identify downstream models/outputs; rollback/revalidate.                                                |
| Bias / representation defect                 | Assess affected decisions/populations; suspend use if material; correct data/process and retest.                                                       |
| Stale authoritative content                  | Remove/replace source; identify outputs/decisions that may require correction; update freshness control.                                               |
| Labeling defect                              | Quarantine affected labels/data; estimate impact on model/evaluation; relabel/adjudicate.                                                              |
| Vendor data-use violation                    | Suspend data flows if needed; Legal/Privacy/Procurement investigation; enforce contract/DPA; reassess provider.                                        |
| Deletion failure                             | Document residual copies/location; remediate; notify Privacy/Legal where personal data is involved.                                                    |

## 23. Data Management Metrics and KRIs

| **Metric / KRI**                               | **Measure**                  | **Expectation**                                               | **Owner**            |
|------------------------------------------------|------------------------------|---------------------------------------------------------------|----------------------|
| Material data assets with named owner          | %                            | Target 100%                                                   | Head of Data & AI    |
| Material data assets with complete provenance  | %                            | Risk-based threshold; High/Critical systems expected complete | Data Stewards        |
| Datasets/corpora with current quality approval | %                            | Before release                                                | Technical Owner      |
| Unknown/partial provenance assets              | Count                        | Escalate for high-impact systems                              | AI Governance        |
| Data quality exceptions past due               | Count / age                  | Trend down                                                    | Dataset Owners       |
| RAG sources past freshness SLA                 | % / count                    | Threshold by corpus                                           | Repository Owners    |
| Sensitive-data DLP events                      | Count / severity             | Immediate review for material events                          | CISO                 |
| Vendor data-use / training changes             | Count assessed before effect | 100% material notices                                         | Procurement          |
| Deletion / exit actions overdue                | Count                        | Zero critical overdue                                         | Data Owner / DPO     |
| Data-driven model drift / segment degradation  | Threshold breaches           | Per system monitoring plan                                    | Data & AI            |
| Human override linked to data issue            | Count / trend                | Investigate clusters                                          | Business Owner       |
| Unregistered AI data exposures                 | Count / severity             | Immediate containment                                         | CISO + AI Governance |

## 24. System-Specific Data Management Baseline

The profiles below intentionally distinguish known scenario facts from required validation. They do not invent production schemas, vendors or retention settings.

| **System**                | **Current data picture**                                                                                                                                     | **Sensitivity**                                                                                 | **Minimum controls**                                                                                                                                                              | **Validation gaps**                                                                                                                                         |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AI-001 DuckDesign         | Known: design generation, component/material/CAD/simulation support. Likely data objects: design requirements/artifacts and user prompts; exact sources TBD. | Confidential engineering IP; user identity/logs may be personal.                                | Data provenance for engineering references; IP/licensing; validation data; source traceability; vendor no-training; engineer-review evidence.                                     | Confirm vendor/model, repositories, upload paths, retention, training use, exact data classification.                                                       |
| AI-002 QuackBot           | Known: customer questions, technical product information, troubleshooting and warranty support. Customer interactions/logs may contain personal data.        | Customer personal data possible; product/support content.                                       | Approved knowledge sources; freshness/authority; prompt/RAG security; minimisation; escalation logging; DPA/vendor data-use evidence.                                             | Confirm supplier role/locations, log/content retention, model-improvement settings, support-ticket integration.                                             |
| AI-003 FeatherForecast    | Known outputs: demand, inventory, manufacturing volume, shortages and supplier demand forecasts. Exact input tables are not defined in scenario.             | Operational/commercial data; personal data possible only if identifiable contacts/users appear. | Source lineage; time-series quality; missingness/outliers; drift; historical/context fit; manager decision boundary.                                                              | Document actual source systems, features, retraining process, vendor/model, retention and supplier-personal-data presence.                                  |
| AI-004 WingInspect        | Known: manufacturing-line images used to detect missing components, assembly problems, cracks and surface defects.                                           | Production images/metadata; personal data depends on camera placement.                          | Image provenance; defect labels; class balance; false-negative coverage; camera/environment changes; retention; prohibit workforce-monitoring repurposing without new assessment. | Confirm cameras, fields of view, label process, worker visibility, model training ownership, storage/retention.                                             |
| AI-005 DuckTalent         | Known: CVs, qualifications/experience, job criteria, summaries, rankings and recommendations. Applicant data is personal data.                               | Restricted applicant/HR data; sensitive/proxy attributes require strict control.                | Data minimisation; job relevance; parsing accuracy; fairness/representation; proxy review; source correction; retention; DPIA/legal/vendor evidence; no autonomous rejection.     | No real deployment dataset approved. Confirm vendor/model, training source, feature set, special-category handling, fairness data, retention and locations. |
| AI-006 PondGPT            | Known: drafting, summarization, research, knowledge retrieval, coding, meeting summaries and internal-process questions.                                     | Confidential/personal employee/internal data likely; repository sensitivity varies.             | Permission-aware retrieval; corpus register; restricted-source exclusions; DLP; prompt injection; embeddings access; no vendor training; usage-log purpose limitation.            | Critical: validate architecture/access boundaries, repositories, connectors, model/provider, logging/retention and support access.                          |
| AI-007 Unregistered GenAI | Known condition: public AI used for correspondence, code, translation, technical material, customer communications, HR documents and browser extensions.     | Unknown; may include confidential IP and personal data.                                         | Contain uploads; discover tools/use cases; preserve exposure evidence; no sensitive public-AI use; register each material use; obtain vendor/privacy terms.                       | Cannot create a single stable data plan until individual uses are decomposed.                                                                               |

## 25. Enhanced Data Governance for High-Impact Systems

| **System / trigger**                                          | **Enhanced data requirement**                                                                                                                                                                                                                                                                  |
|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DuckTalent                                                    | Pre-use data approval; job-relevance and proxy review; applicant-data minimisation; accuracy/correction; fairness and accessibility testing; documented representativeness limits; strict vendor training/retention controls; separate DPIA/legal review; versioned feature/criteria register. |
| DuckDesign / WingInspect safety-relevant expansion            | Domain-specific validation data; edge/failure-case coverage; provenance and label quality; environment/context validation; human authority; safety-quality review; strict change control.                                                                                                      |
| QuackBot / PondGPT GenAI                                      | Knowledge-source register; permission-aware retrieval; prompt/RAG poisoning controls; sensitive-data filters; vendor no-training evidence; output/log retention rules; source freshness and incident traceability.                                                                             |
| Any legally high-risk AI where Duckworks is provider/deployer | Legal confirms applicable AI Act role/timing and identifies Article 10/12/26 data/log obligations; DMP evidence is then updated to demonstrate the specific mandatory requirements.                                                                                                            |

## 26. Minimum AI Data Evidence Pack

| **Evidence ID** | **Minimum record**                                                          |
|-----------------|-----------------------------------------------------------------------------|
| DATA-EV-01      | AI Data Asset Register entries                                              |
| DATA-EV-02      | Dataset / corpus provenance and rights record                               |
| DATA-EV-03      | Data-flow diagram and processing locations                                  |
| DATA-EV-04      | Data profile and quality/representativeness assessment                      |
| DATA-EV-05      | Transformation / annotation / preprocessing record                          |
| DATA-EV-06      | Dataset/corpus version manifest and hashes/IDs                              |
| DATA-EV-07      | Train/validation/test split evidence where applicable                       |
| DATA-EV-08      | Access-control / permission review evidence                                 |
| DATA-EV-09      | Privacy/DPIA/ROPA linkage where applicable                                  |
| DATA-EV-10      | Vendor data-use, no-training, retention, subprocessor and deletion evidence |
| DATA-EV-11      | RAG / knowledge-source register and freshness evidence                      |
| DATA-EV-12      | Data quality exceptions and remediation                                     |
| DATA-EV-13      | Monitoring / drift / data-incident records                                  |
| DATA-EV-14      | Change-management records for material data changes                         |
| DATA-EV-15      | Retention / deletion / exit evidence                                        |
| DATA-EV-16      | Governance approval / exception / risk acceptance records                   |

## 27. Data Readiness Gate Checklist

☐ AI ID, intended purpose and dataset/corpus use are documented.

☐ Dataset Owner / Data Steward is named.

☐ Source, collection context, rights/license and provenance are recorded.

☐ Personal data and information-classification status are determined.

☐ Required Privacy/Legal/Security/Vendor/Safety/HR reviews are complete.

☐ Quality acceptance criteria and results are documented.

☐ Known errors, gaps, exclusions, bias/representation limitations and affected contexts are documented.

☐ Training/validation/test roles are controlled where applicable.

☐ RAG permissions, freshness and source authority are validated where applicable.

☐ Vendor data-use/model-improvement and retention settings are evidenced.

☐ Access, environment separation, secrets and encryption requirements are met.

☐ Retention/deletion schedule is approved.

☐ Lineage links the data version to model/service version and material outputs/decisions.

☐ Monitoring and reassessment triggers are defined.

☐ No material unresolved data issue is being hidden by a generic 'human review' statement.

## 28. Appendix A - AI Dataset / Corpus Card Template

| **Field**                                    | **Entry**                                                              |
|----------------------------------------------|------------------------------------------------------------------------|
| Data Asset ID                                | \[DW-DATA-AI###-NN\]                                                   |
| Dataset / corpus name                        | \[name\]                                                               |
| AI system / AI ID                            | \[AI-###\]                                                             |
| Owner / steward                              | \[name / function\]                                                    |
| Purpose / dataset role                       | Training / validation / testing / RAG / inference / monitoring / other |
| Source / origin                              | \[system / user / vendor / public / synthetic\]                        |
| Original collection context                  | \[why/how data was created or collected\]                              |
| Rights / license / contract                  | \[evidence\]                                                           |
| Data subjects / population / product context | \[details\]                                                            |
| Data categories / schema                     | \[summary\]                                                            |
| Personal / sensitive data                    | \[No / Possible / Yes + categories\]                                   |
| Information classification                   | \[Public / Internal / Confidential / Restricted\]                      |
| Geography / locations                        | \[source and processing locations\]                                    |
| Time period represented                      | \[range\]                                                              |
| Volume / scale                               | \[records/images/tokens/etc.\]                                         |
| Transformations / annotation                 | \[steps + versions\]                                                   |
| Quality criteria/results                     | \[metrics / thresholds / exceptions\]                                  |
| Representativeness / data gaps               | \[assessment\]                                                         |
| Known limitations                            | \[limitations\]                                                        |
| Version / hash / snapshot                    | \[identifier\]                                                         |
| Access roles                                 | \[authorized roles\]                                                   |
| Retention / deletion                         | \[rule\]                                                               |
| Downstream dependencies                      | \[models/indexes/reports/decisions\]                                   |
| Approval status                              | Draft / Conditional / Approved / Suspended / Retired                   |
| Next review / trigger                        | \[trigger\]                                                            |

## 29. Appendix B - Data Quality Assessment Template

| **Assessment area**             | **Record**                                                 |
|---------------------------------|------------------------------------------------------------|
| Relevance                       | \[criterion / result / evidence / exception\]              |
| Representativeness              | \[criterion / result / evidence / unrepresented contexts\] |
| Accuracy / label correctness    | \[criterion / sampling method / result\]                   |
| Completeness / missingness      | \[threshold / result / handling\]                          |
| Consistency / schema            | \[tests / result\]                                         |
| Timeliness / freshness          | \[SLA / latest source date / result\]                      |
| Duplicates / leakage            | \[test / result\]                                          |
| Bias / proxy / segment analysis | \[method / lawful data / result / limitations\]            |
| Integrity / version             | \[hash / source / change control\]                         |
| Decision                        | Approve / Approve with conditions / Hold / Reject          |
| Approver(s)                     | \[Dataset Owner / Technical Owner / required specialists\] |

## 30. Appendix C - RAG / Knowledge Source Register Template

| **Field**                        | **Entry**                                                     |
|----------------------------------|---------------------------------------------------------------|
| Source ID                        | \[KB-###\]                                                    |
| Repository / document class      | \[name/type\]                                                 |
| Owner                            | \[repository owner\]                                          |
| Authority level                  | Authoritative / Reference / Draft / User-generated / External |
| Classification                   | \[Public/Internal/Confidential/Restricted\]                   |
| Permitted users                  | \[roles/groups\]                                              |
| Index / vector store             | \[location / collection\]                                     |
| Refresh rule                     | \[cadence/event\]                                             |
| Staleness threshold              | \[rule\]                                                      |
| Prompt-injection trust level     | \[trusted / semi-trusted / untrusted\]                        |
| Personal data                    | \[No/Possible/Yes\]                                           |
| Retention / deletion propagation | \[rule\]                                                      |
| Last validation                  | \[evidence / reviewer\]                                       |
| Status                           | Approved / Conditional / Suspended / Retired                  |

## 31. Appendix D - AI Data Retention Schedule Template

| **Asset / category** | **Purpose** | **Legal / contractual basis** | **Retention**     | **Trigger** | **Deletion method** | **Owner** | **Evidence** |
|----------------------|-------------|-------------------------------|-------------------|-------------|---------------------|-----------|--------------|
| \[asset\]            | \[purpose\] | \[basis\]                     | \[duration/rule\] | \[event\]   | \[method\]          | \[owner\] | \[evidence\] |
| \[asset\]            | \[purpose\] | \[basis\]                     | \[duration/rule\] | \[event\]   | \[method\]          | \[owner\] | \[evidence\] |
| \[asset\]            | \[purpose\] | \[basis\]                     | \[duration/rule\] | \[event\]   | \[method\]          | \[owner\] | \[evidence\] |

## 32. Plan Acceptance Criteria

| **ID**    | **Acceptance criterion**                                                                                                          |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------|
| DMP-AC-01 | All seven baseline entries have a documented system-specific data baseline and validation gaps.                                   |
| DMP-AC-02 | Every material approved dataset/corpus has an internal owner and unique Data Asset ID.                                            |
| DMP-AC-03 | Material data can be traced from source/provenance through transformations to the relevant AI system/version.                     |
| DMP-AC-04 | Personal-data handling is linked to Privacy/DPIA/ROPA and DPA evidence where applicable.                                          |
| DMP-AC-05 | Third-party AI data-use/model-improvement, retention and subprocessor facts are verified before material use.                     |
| DMP-AC-06 | High-impact datasets/corpora have documented quality, representativeness and limitation evidence.                                 |
| DMP-AC-07 | RAG corpora have permission, freshness, provenance and injection/security controls.                                               |
| DMP-AC-08 | Material data changes trigger the existing AI Change Management process.                                                          |
| DMP-AC-09 | Retention/deletion rules exist for source data, derived data, outputs, logs, embeddings, vendor copies and backups as applicable. |
| DMP-AC-10 | No portfolio artifact claims legal compliance or ISO/NIST conformity solely because the DMP exists.                               |
| DMP-AC-11 | Internal Audit is not assigned operational ownership of dataset controls.                                                         |
| DMP-AC-12 | Open architecture/data assumptions remain visible and are not represented as implemented controls.                                |

## 33. Source and Framework Register

| **Source**                                       | **Classification**                   | **Use in DMP**                                                                                                                            | **Reference**                                              |
|--------------------------------------------------|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| Regulation (EU) 2016/679 (GDPR)                  | Binding EU regulation                | Articles 5, 25, 28, 30, 32, 35 for personal-data principles, design/default, processor terms, records, security and DPIA.                 | https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng          |
| Regulation (EU) 2024/1689 (AI Act), consolidated | Binding EU regulation                | Article 10 data/data governance; Article 26(4) deployer input-data relevance/representativeness; Articles 12/26 logging where applicable. | https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng |
| NIST AI RMF 1.0                                  | Voluntary framework                  | MAP 2.3 data collection/selection suitability/representativeness; MAP 4 third-party data; lifecycle documentation/TEVV.                   | https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf     |
| NIST AI RMF Playbook                             | Voluntary implementation guidance    | Suggested lineage, metadata, data-selection, curation, preparation, bias/privacy/security and third-party data practices.                 | https://airc.nist.gov/airmf-resources/playbook/            |
| ISO/IEC 42001:2023                               | Voluntary management-system standard | Public description supports management-system governance, traceability, transparency, risk and continual improvement.                     | https://www.iso.org/standard/42001                         |
| ISO/IEC 23894:2023                               | Voluntary AI risk guidance           | Supports integration of AI-specific risk management across lifecycle.                                                                     | https://www.iso.org/standard/77304.html                    |
| Duckworks Project W.I.N.G. artifacts             | Internal project basis               | Business scenario, objectives, assumptions, stakeholders, risk methodology, DPA/vendor contract and change-management process.            | Portfolio repository                                       |

## 34. Material Assumptions and Implementation Gaps

| **Gap**     | **Limitation**                                                                                                                                   | **Materiality**    | **Owner**                        |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|----------------------------------|
| GAP-DATA-01 | Actual production data inventories, schemas, volumes and source systems for most use cases are not yet verified.                                 | High               | System / Dataset Owners          |
| GAP-DATA-02 | Third-party model/service providers, processing locations, retention and data-use settings require verification.                                 | Critical for GenAI | Procurement / Legal / DPO / CISO |
| GAP-DATA-03 | PondGPT permission-aware retrieval architecture is an open Critical assumption.                                                                  | Critical           | Head of IT & Cloud / Data & AI   |
| GAP-DATA-04 | DuckTalent has no approved real applicant training/fairness dataset in this portfolio.                                                           | Critical           | CPO / Data & AI / Legal / DPO    |
| GAP-DATA-05 | WingInspect camera content and whether individuals are captured are not verified.                                                                | High               | Manufacturing / DPO / CISO       |
| GAP-DATA-06 | FeatherForecast exact source features and retraining/version process are not specified in the business scenario.                                 | Medium-High        | Supply Chain / Data & AI         |
| GAP-DATA-07 | AI-007 is not a single dataset/system and must be decomposed into individual uses before stable lineage/retention can be established.            | Critical           | CISO / AI Governance             |
| GAP-DATA-08 | A real organization would need to map this AI-specific handling model to its existing records-retention and information-classification policies. | High               | CRCO / DPO / CISO                |

## 35. Final Governance Position

Duckworks should treat data management as a lifecycle control rather than a one-time data-cleaning task. A model or AI service can remain technically unchanged while its risk materially changes because the data source, knowledge corpus, label definition, population, retention practice or vendor data-use terms changed.

Accordingly, this Data Management Plan is designed to operate with QuackTrack, the AI Risk Classification & Assessment Methodology, AI Impact Assessments, the AI Vendor Contract, AI DPA, AI Change Management Process, incident/runbook processes and future control library. It provides the data evidence layer needed to support the project's wider auditability principle: material data claims should be traceable to owners, sources, quality evidence, controls and decisions.

## Portfolio Disclaimer

Duckworks, Project W.I.N.G., all named personnel, AI systems, datasets, data flows, vendors, processing activities, controls and evidence in this document are fictional and created solely for educational and professional portfolio purposes. Portfolio artifacts use only fictional, synthetic, anonymized or public data.

This plan is not legal advice, a GDPR DPIA, an EU AI Act conformity assessment, ISO certification evidence or a statement of regulatory compliance. Legal applicability must be validated against actual jurisdiction, organizational role, intended purpose, system classification and processing facts.
