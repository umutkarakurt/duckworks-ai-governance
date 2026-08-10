# Duckworks AI Data Processing Agreement Template

**DUCKWORKS**

AI Data Processing Agreement Template

Controller-processor data protection terms tailored for AI systems, models, APIs, hosted services and AI-enabled SaaS

| **Document control**    | **Value**                                                                                |
|-------------------------|------------------------------------------------------------------------------------------|
| Document ID             | DW-WING-TPRM-03                                                                          |
| Version                 | 1.0                                                                                      |
| Status                  | Portfolio Template - Legal Review Required                                               |
| Organization            | Duckworks (fictional)                                                                    |
| Document owner          | General Counsel / Data Protection Officer / Director of Procurement & Vendor Assurance   |
| Governance contributors | AI Governance, Information Security, Data & AI, Risk & Compliance, Business/System Owner |
| Prepared date           | 9 August 2026                                                                            |
| Classification          | Portfolio / Synthetic / Non-production                                                   |

| **LEGAL STATUS.** This is a fictional portfolio template, not legal advice and not an executed agreement. It is designed to demonstrate how Duckworks would implement GDPR controller-processor requirements and AI-specific privacy safeguards in a supplier relationship. Qualified legal counsel must validate the parties’ actual roles, national law, international transfers, liability terms, sector-specific requirements and the underlying processing facts before real use. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Duckworks principle:** No AI supplier may process personal data for Duckworks unless roles, instructions, permitted data uses, security, subprocessors, transfers, incident duties, deletion and audit evidence are documented and enforceable.

## 1. Purpose, Scope and Use of this Template

**Applicability:** *CORE WHEN VENDOR IS A PROCESSOR*

This Data Processing Agreement (DPA) governs processing of Personal Data by the Supplier on behalf of Duckworks in connection with the AI Service described in Schedule 1. It is intended to form part of the underlying Master Services Agreement, Order Form, AI Vendor Contract or other agreement identified in the cover sheet.

The DPA is drafted primarily for the GDPR controller-to-processor relationship. It does not determine legal roles merely by label. The Parties must assess the actual facts, including who determines the purposes and essential means of processing.

- Use this template only after the Vendor/AI intake record identifies personal-data processing and a controller-processor relationship.

- If the Supplier independently determines purposes or essential means, the relevant processing may require controller-to-controller or joint-controller terms instead of, or in addition to, this DPA.

- If the processing is entirely outside GDPR scope, legal counsel should decide whether to retain this DPA contractually or use another privacy addendum.

- AI-specific clauses in this template are Duckworks organizational safeguards unless expressly identified as mandatory legal requirements.

GDPR Article 28 requires a binding written contract or other legal act when a processor processes personal data on behalf of a controller. EDPB Guidelines 07/2020 emphasize that role allocation follows factual functions, not contractual labels alone.

### 1.1 Relationship to the AI Vendor Contract

Where the Parties have executed the Duckworks AI Vendor Contract Template or equivalent supplier agreement, this DPA supplements that agreement for Personal Data processing. The AI Vendor Contract governs broader AI risk, security, performance, change, IP and resilience matters; this DPA governs data-protection obligations for processing on Duckworks’ behalf.

### 1.2 Order of precedence

For Personal Data processing, this DPA controls over conflicting general privacy terms in the Main Agreement. An applicable EU Standard Contractual Clause (SCC) mechanism controls to the extent a supplemental term in this DPA conflicts with the mandatory wording of the SCCs. Commercial terms, liability and governing law remain subject to the Main Agreement unless this DPA expressly states otherwise and counsel approves the change.

## 2. Legal / Guidance / Internal-Control Classification

**Applicability:** *CORE*

The template deliberately distinguishes legal requirements from guidance and internal safeguards so that portfolio evidence does not overstate compliance.

| **Classification**  | **Meaning in this template**                                                                   | **Examples**                                                                                                                          |
|---------------------|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| MANDATORY LEGAL     | A GDPR obligation that applies when the stated applicability conditions are met.               | Article 28 processor contract; Article 32 security; Article 33(2) processor breach notification; Chapter V transfer rules.            |
| REGULATORY GUIDANCE | Authoritative regulator interpretation or guidance; not legislation itself.                    | EDPB Guidelines 07/2020 on controller/processor concepts; EDPB Opinion 28/2024 on AI-model data protection questions.                 |
| DUCKWORKS CONTROL   | A contractual requirement selected by Duckworks to reduce AI/privacy risk or improve evidence. | Default prohibition on training shared models with Duckworks data; 24-hour contractual incident target; model-data-use change notice. |
| PROJECT ASSUMPTION  | A fictional scenario fact used for the portfolio and requiring verification in real use.       | Duckworks acts as controller; supplier acts as processor; EU/EEA processing; identified AI service and data categories.               |

## 3. Parties, Privacy Roles and Main Agreement

**Applicability:** *MANDATORY ROLE VALIDATION + CORE*

The Parties shall complete the following role and agreement record before execution. A processor that determines purposes and means for a processing activity may be treated as a controller for that activity under GDPR Article 28(10).

| **Field**               | **Duckworks / Customer**                       | **Supplier**              |
|-------------------------|------------------------------------------------|---------------------------|
| Legal entity            | \[Duckworks legal entity\]                     | \[Supplier legal entity\] |
| Registered address      | \[address\]                                    | \[address\]               |
| Primary privacy contact | \[name/email\]                                 | \[name/email\]            |
| DPO (if applicable)     | \[details\]                                    | \[details\]               |
| GDPR role               | Controller / Processor for upstream controller | Processor / Subprocessor  |
| Main Agreement          | \[title/date/order\]                           | \[reference\]             |
| Effective date          | \[date\]                                       | \[date\]                  |

### 3.1 Role-screening questions

- Who determines why the personal data are processed?

- Who determines essential means such as data categories, retention, recipients and affected persons?

- Does the Supplier reuse prompts, files, outputs, embeddings or interaction data for its own product/model development?

- Does the Supplier combine Duckworks data with third-party data for a purpose not instructed by Duckworks?

- Does any subprocessor independently determine purposes for part of the processing?

- Is Duckworks itself processing on behalf of another controller, making the Supplier a subprocessor?

## 4. Definitions

**Applicability:** *CORE*

Capitalized terms have the meanings below. GDPR-defined terms retain their GDPR meaning where the Regulation applies.

| **Term**                | **Definition**                                                                                                                                                                                                          |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AI Service              | The AI system, AI-enabled SaaS, model endpoint, agent, API, application or related service identified in Schedule 1.                                                                                                    |
| Customer Data           | Data, content, prompts, files, records, instructions and materials submitted to or made accessible to the AI Service by or for Duckworks.                                                                               |
| Personal Data           | Personal data within GDPR Article 4(1), where applicable.                                                                                                                                                               |
| Processing              | Processing within GDPR Article 4(2), where applicable.                                                                                                                                                                  |
| Duckworks Personal Data | Personal Data processed by the Supplier on behalf of Duckworks under this DPA.                                                                                                                                          |
| Input Data              | Prompts, documents, images, messages, records or other information provided to or retrieved by the AI Service.                                                                                                          |
| Output Data             | Generated text, code, summary, prediction, recommendation, ranking, classification, embedding or other output associated with Duckworks use.                                                                            |
| Model Improvement       | Training, pre-training, fine-tuning, reinforcement learning, evaluation, benchmarking, tuning, distillation or other use to improve or develop a model or service beyond providing the contracted service to Duckworks. |
| Subprocessor            | A third party engaged by the Supplier to process Duckworks Personal Data on Duckworks’ behalf.                                                                                                                          |
| Personal Data Breach    | A personal data breach as defined by GDPR Article 4(12), where applicable.                                                                                                                                              |
| International Transfer  | A transfer subject to GDPR Chapter V, as determined under applicable law and regulatory guidance.                                                                                                                       |
| Material Privacy Change | A change reasonably capable of altering the purposes, data categories, retention, recipients, subprocessors, transfer locations, model-data use, security or data-subject impact of the processing.                     |

## 5. Processing Details and Controller Rights

**Applicability:** *MANDATORY LEGAL - GDPR ARTICLE 28(3)*

The subject matter, duration, nature and purpose of processing, types of personal data, categories of data subjects, and Duckworks’ obligations and rights shall be documented in Schedule 1. Processing outside that documented scope requires a new or amended instruction and any required privacy or AI-governance reassessment.

- Duckworks retains the right to determine documented processing instructions and to require the Supplier to stop processing that exceeds them.

- The Supplier shall identify any information it requires from Duckworks to perform the instructed processing lawfully and securely.

- A change in intended purpose or data use is not deemed approved merely because it appears in a Supplier product update, online policy or general terms.

## 6. Documented Instructions and Purpose Limitation

**Applicability:** *MANDATORY LEGAL - GDPR ARTICLE 28(3)(a) + DUCKWORKS AI CONTROLS*

The Supplier shall process Duckworks Personal Data only on documented instructions from Duckworks, including instructions concerning transfers to a third country or international organization, unless Union or Member State law requires otherwise. Where legally permitted, the Supplier shall inform Duckworks of that legal requirement before processing.

- The Main Agreement, this DPA, completed schedules, approved support requests and other authorized written instructions constitute documented instructions.

- The Supplier shall not use Duckworks Personal Data for advertising, data brokerage, unrelated analytics, profiling for unrelated purposes, or development of products/services for other customers unless Duckworks expressly approves that separate purpose and the Parties document the appropriate legal role and terms.

- The Supplier shall immediately inform Duckworks if, in its opinion, an instruction infringes GDPR or other applicable Union or Member State data-protection law.

- Where the Supplier receives conflicting or unclear instructions, it shall seek clarification before materially expanding processing.

## 7. AI-Specific Data Use, Training and Model Improvement

**Applicability:** *DUCKWORKS CONTROL; LEGAL DUTIES MAY ALSO APPLY*

Unless expressly authorized in Schedule 3, the Supplier shall not use Duckworks Personal Data, Customer Data, prompts, retrieved documents, embeddings, interaction histories or Output Data for Model Improvement of a model or service made available to other customers, affiliates or the public.

- No default opt-in or changed website policy may override this restriction.

- If Duckworks approves Model Improvement, Schedule 3 must identify the exact data, purpose, model scope, legal role, retention, access, de-identification measures, deletion/unlearning limitations and downstream recipients.

- The Supplier shall disclose whether human reviewers may access prompts, files or outputs and shall restrict such access to authorized personnel under confidentiality obligations.

- The Supplier shall not create persistent cross-customer profiles or memory from Duckworks Personal Data unless specifically instructed.

- The Supplier shall not intentionally include Duckworks Personal Data in training corpora, evaluation sets, benchmark sets or shared prompt libraries except as expressly authorized.

- Where model behavior can reproduce memorized Personal Data, the Supplier shall provide relevant mitigation, investigation and response support.

The default no-training rule is an internal Duckworks contractual control. GDPR requires lawful, fair and purpose-limited processing; whether a separate training or model-development activity makes the Supplier an independent controller depends on the facts.

## 8. Authorized Personnel and Confidentiality

**Applicability:** *MANDATORY LEGAL - GDPR ARTICLE 28(3)(b) / ARTICLE 29*

The Supplier shall ensure that persons authorized to process Duckworks Personal Data are subject to confidentiality obligations and process the data only on instructions, unless required by applicable Union or Member State law.

- Access shall be limited by role and least privilege.

- Privileged administrator, support, safety-review and model-operations access shall be logged where proportionate to risk.

- Human review of AI conversations or outputs shall be limited to approved operational purposes and subject to access and confidentiality controls.

- The Supplier shall provide relevant privacy/security training to personnel with access to Duckworks Personal Data.

## 9. Security of Processing

**Applicability:** *MANDATORY LEGAL - GDPR ARTICLE 28(3)(c) AND ARTICLE 32*

The Supplier shall implement and maintain technical and organizational measures appropriate to the risk, taking into account the state of the art, costs of implementation, and the nature, scope, context and purposes of processing. Schedule 2 records the agreed measures.

- Measures shall address confidentiality, integrity, availability and resilience of systems and services.

- Where appropriate, measures shall include pseudonymization and encryption, timely restoration, and regular testing/assessment of security effectiveness.

- The Supplier shall consider risks from accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to Personal Data.

- Security shall cover AI-specific attack paths where relevant, including prompt injection, indirect prompt injection, retrieval poisoning, excessive permissions, insecure plugins/tools, cross-tenant leakage, model/service supply-chain compromise and unsafe logging.

- Material reduction of an agreed security control requires prior notice and, where it increases risk, Duckworks approval.

### 9.1 Minimum security evidence

The Supplier shall maintain evidence reasonably sufficient to demonstrate the design and operation of applicable controls. Duckworks may accept current independent assurance reports or certifications as evidence, but certification does not eliminate the Supplier’s contractual obligations or Duckworks’ risk-based review rights.

## 10. Data Minimization, Storage Limitation and Retention

**Applicability:** *MANDATORY GDPR PRINCIPLES FOR CONTROLLER; CONTRACTUAL PROCESSOR IMPLEMENTATION*

The Supplier shall configure and operate the service to support Duckworks instructions concerning data minimization and retention. Retention periods and deletion behavior shall be documented in Schedules 1 and 6.

- Collect or retain only the data needed for the instructed processing.

- Separate service content from diagnostic/security logs where feasible and apply defined retention to each.

- Identify unavoidable backup retention and the period during which deleted data may remain in protected backups.

- Do not retain prompts or outputs indefinitely by default where a shorter period is sufficient.

- Provide configurable history/memory controls where these features materially affect privacy risk.

GDPR Article 5 principles primarily bind the controller; the processor contract and technical design should enable the controller to comply with them.

## 11. Subprocessors and Processing Chain

**Applicability:** *MANDATORY LEGAL - GDPR ARTICLE 28(2) AND 28(4)*

The Supplier shall not engage a Subprocessor without Duckworks’ prior specific or general written authorization. If general authorization is used, the Supplier shall provide advance notice of intended additions or replacements and a genuine opportunity for Duckworks to object.

- Approved Subprocessors, their functions, processing locations and transfer mechanisms shall be listed in Schedule 4.

- The Supplier shall impose on each Subprocessor data-protection obligations equivalent in substance to those required by GDPR Article 28 for the relevant processing.

- The Supplier remains fully liable to Duckworks for performance of the Subprocessor’s data-protection obligations as provided by GDPR Article 28(4).

- A foundation-model provider, moderation provider, vector database, hosting provider, observability service or support provider is a Subprocessor where it processes Duckworks Personal Data on Duckworks’ behalf; role must be assessed rather than assumed.

- Duckworks objection rights and the operational response to an unresolved objection shall be defined in Schedule 4.

## 12. Data Subject Rights Assistance

**Applicability:** *MANDATORY LEGAL - GDPR ARTICLE 28(3)(e)*

Taking into account the nature of processing, the Supplier shall assist Duckworks through appropriate technical and organizational measures, insofar as possible, with requests to exercise data-subject rights under GDPR Chapter III.

- The Supplier shall promptly forward any request received directly from a data subject relating to Duckworks-controlled processing and shall not respond substantively except on Duckworks’ instructions or where legally required.

- Assistance shall include locating, accessing, correcting, exporting, restricting or deleting Personal Data where technically and legally applicable.

- For AI services, assistance may require identifying data within conversation histories, logs, retrieval stores, embeddings, user profiles, feedback records or model-support systems.

- If deletion from an AI model itself is technically infeasible, the Supplier shall explain the architecture, relevant safeguards and available mitigation rather than implying that account-level deletion erases all model effects.

## 13. Assistance with Security, Breach, DPIA and Prior Consultation

**Applicability:** *MANDATORY LEGAL - GDPR ARTICLE 28(3)(f)*

Taking into account the nature of processing and information available to it, the Supplier shall assist Duckworks with compliance obligations under GDPR Articles 32 to 36.

- Provide information reasonably required for risk and security assessment.

- Support Duckworks investigations and documentation of Personal Data Breaches.

- Provide architecture, data-flow, retention, subprocessor, transfer and control information reasonably needed for a DPIA.

- Support prior consultation with a supervisory authority where required, including supplying processing and safeguard information under the Supplier’s control.

- Notify Duckworks when a material change may invalidate a prior DPIA or privacy assessment.

## 14. Personal Data Breach Notification and Cooperation

**Applicability:** *MANDATORY LEGAL - GDPR ARTICLE 33(2) + ENHANCED CONTRACTUAL TIMING*

The Supplier shall notify Duckworks without undue delay after becoming aware of a Personal Data Breach affecting Duckworks Personal Data. As a Duckworks contractual safeguard, the Supplier shall provide an initial notification within 24 hours of awareness unless the Parties specify a shorter period in Schedule 5.

- Initial notification need not contain every fact, but shall state what is known, what remains under investigation and the next update time.

- The Supplier shall provide information needed by Duckworks to assess notification duties, including the nature of the breach, affected data/data subjects where known, likely consequences, containment and remediation measures, and a contact point.

- Information may be provided in phases without undue further delay when not available at once.

- The Supplier shall preserve relevant evidence and cooperate with forensic, legal, privacy, security and regulatory response activities.

- The Supplier shall not notify affected data subjects or supervisory authorities on Duckworks’ behalf without instruction unless legally required to do so; if legally permitted it shall inform Duckworks before such communication.

- AI-specific privacy incidents include cross-user or cross-tenant disclosure, unintended retrieval of restricted records, prompt/output logging exposure, unauthorized model-human-review access, or reproduction of sensitive Personal Data.

The 24-hour target is an internal contractual enhancement. GDPR Article 33(2) requires processor-to-controller notification “without undue delay”; the controller’s separate supervisory-authority deadline is generally 72 hours where Article 33(1) applies.

## 15. Audit, Information and Demonstration of Compliance

**Applicability:** *MANDATORY LEGAL - GDPR ARTICLE 28(3)(h)*

The Supplier shall make available to Duckworks all information necessary to demonstrate compliance with Article 28 obligations and shall allow for and contribute to audits, including inspections, by Duckworks or another auditor mandated by Duckworks.

- Duckworks will ordinarily use a risk-based evidence hierarchy: current independent assurance/certification, targeted evidence requests, remote review, then on-site inspection where justified.

- The Supplier may protect other customers’ confidential information and security-sensitive material using reasonable safeguards, but those safeguards shall not nullify Duckworks’ audit right.

- A material incident, regulator request, evidence gap, critical control failure or material change may justify enhanced audit activity outside routine cadence.

- The Supplier shall retain evidence required by Schedule 8 and identify control/evidence owners.

## 16. Records, Regulator Cooperation and Accountability Evidence

**Applicability:** *MANDATORY LEGAL WHERE APPLICABLE + CORE*

The Supplier shall maintain records required of processors under applicable data-protection law and cooperate, on request, with competent supervisory authorities as required by GDPR Article 31. On reasonable request, the Supplier shall provide Duckworks with information necessary to maintain its own records of processing and accountability evidence.

- Record categories of processing performed for Duckworks.

- Record relevant third-country transfers and safeguards where applicable.

- Maintain a general description of security measures where required.

- Preserve versions of processing descriptions, Subprocessor lists and material privacy notices relevant to the service during the agreed evidence-retention period.

## 17. International Transfers and Remote Access

**Applicability:** *MANDATORY LEGAL WHEN GDPR CHAPTER V APPLIES*

The Supplier shall not make an International Transfer of Duckworks Personal Data except on documented Duckworks instructions and in compliance with GDPR Chapter V. Schedule 5 identifies transfer destinations, legal mechanisms and required supplementary measures.

- Where a valid adequacy decision covers the transfer, the Supplier shall document the applicable scope.

- Where appropriate safeguards are required, the Parties may use the applicable Commission Standard Contractual Clauses under Implementing Decision (EU) 2021/914, selecting the correct module and completing the annexes without altering the mandatory clauses.

- If the Parties use the Commission controller-processor SCCs under Implementing Decision (EU) 2021/915 for Article 28 requirements, this DPA may supplement them only to the extent permitted and non-conflicting.

- The Supplier shall support transfer-risk assessment and reasonable supplementary measures where required.

- Remote administrative, support or human-review access from a third country shall be assessed as part of the transfer architecture rather than treated as irrelevant solely because the primary hosting region is in the EEA.

- The Supplier shall notify Duckworks of material changes to transfer locations or mechanisms before implementation where reasonably possible.

## 18. Government and Third-Party Disclosure Requests

**Applicability:** *DUCKWORKS CONTROL; SCC/LAW MAY IMPOSE ADDITIONAL DUTIES*

Unless prohibited by law, the Supplier shall promptly notify Duckworks of a legally binding request from a public authority or third party seeking Duckworks Personal Data and shall provide reasonable information and assistance to enable Duckworks to protect data-subject rights and assess the request.

- The Supplier shall disclose no more data than legally required and shall document the legal basis and scope of disclosure where permitted.

- Where applicable SCCs impose specific obligations concerning public-authority access, those SCC obligations control.

- The Supplier shall maintain a process for reviewing authority requests and escalating legally questionable or disproportionate requests where permitted.

## 19. Return, Deletion and Termination Assistance

**Applicability:** *MANDATORY LEGAL - GDPR ARTICLE 28(3)(g) + DUCKWORKS EXIT CONTROL*

At Duckworks’ choice, the Supplier shall delete or return all Duckworks Personal Data after the end of services relating to processing and shall delete existing copies unless Union or Member State law requires storage. Schedule 6 records the selected option and operational deletion process.

- Export shall be provided in a usable, commonly readable format where applicable before deletion.

- Deletion shall cover primary stores, prompt/conversation histories, retrieval stores, embeddings, support artifacts and other service repositories containing Duckworks Personal Data, subject to documented backup handling.

- Where legal retention is required, the Supplier shall identify the data, legal basis, retention period and access restrictions.

- The Supplier shall provide a deletion/return certificate or equivalent evidence on request.

- The Parties shall document any technical limitation preventing deletion from a model or derived artifact and agree risk mitigation rather than describing the data as deleted without qualification.

## 20. Privacy by Design, Configuration and AI Feature Controls

**Applicability:** *DUCKWORKS CONTROL SUPPORTING GDPR ARTICLE 25 OBLIGATIONS*

The Supplier shall provide reasonable product capabilities and information enabling Duckworks to implement privacy by design and by default for the approved processing.

- Controls for retention/history, access, sharing, connectors, retrieval scope, user memory and external tools where supported by the service.

- Administrative ability to disable or restrict optional features that materially increase Personal Data exposure.

- Clear indication when a feature changes data use, retention, recipient categories or cross-border processing.

- Reasonable separation of tenant/customer data and prevention of unauthorized cross-tenant retrieval.

- Configurable logging adequate for investigation while avoiding unnecessary sensitive content capture.

## 21. Profiling, Automated Decisions and High-Impact Use

**Applicability:** *CONDITIONAL LEGAL + ENHANCED DUCKWORKS CONTROL*

The Supplier shall not materially change the AI Service so that it performs profiling or automated decision-making on Duckworks’ behalf beyond the purpose documented in Schedule 1. Where processing may engage GDPR Article 22, a DPIA, employment/privacy rules or other high-impact requirements, the Supplier shall provide the functionality and information reasonably needed for Duckworks review.

- Identify whether outputs are rankings, scores, recommendations, classifications or decisions concerning natural persons.

- Provide information about relevant data inputs, decision logic at an appropriate level, limitations and human-review controls to the extent available and legally required.

- Support correction/challenge workflows for inaccurate Personal Data or materially incorrect AI-supported records where applicable.

- For DuckTalent AI or similar recruitment processing, no production use is authorized merely by executing this DPA; the separate Duckworks AI governance, legal/privacy/fairness and human-oversight gates remain controlling.

## 22. Material Privacy Change Management

**Applicability:** *DUCKWORKS CONTROL; MAY SUPPORT LEGAL REASSESSMENT*

The Supplier shall give Duckworks reasonable advance notice of a Material Privacy Change and shall not implement a change that materially expands processing beyond documented instructions without Duckworks approval.

- New or replaced Subprocessor.

- New processing country or transfer mechanism.

- New Model Improvement use or changed human-review practice.

- Material retention increase or new persistent memory/profile feature.

- New data categories, integrations, connectors or recipients.

- Material change in model/provider architecture that affects Personal Data processing.

- Change in security controls that materially increases risk.

## 23. Suspension, Unlawful Instructions and Remediation

**Applicability:** *CORE + LEGAL SAFEGUARDS*

Duckworks may suspend affected processing where it reasonably determines that continued processing presents an unacceptable privacy/security risk, materially breaches this DPA, or lacks a required transfer mechanism or approval. The Parties shall cooperate in good faith on remediation.

- The Supplier shall immediately inform Duckworks if it believes an instruction violates applicable data-protection law.

- Where only one function or data flow is affected, the Parties should consider proportionate feature or processing suspension before full service termination where this adequately controls risk.

- Suspension does not waive deletion, evidence preservation, incident, regulatory cooperation or confidentiality duties.

## 24. Liability, Indemnities and Commercial Terms

**Applicability:** *LEGAL COUNSEL REVIEW REQUIRED*

Liability allocation, indemnities, insurance, damages exclusions and financial caps shall be governed by the Main Agreement or a counsel-approved amendment. This portfolio template does not invent monetary caps or indemnity positions.

GDPR statutory responsibility, regulatory powers and data-subject rights cannot necessarily be reallocated by contract. Commercial risk allocation must be tailored to the parties, jurisdiction and service.

## 25. Term, Survival and Amendments

**Applicability:** *CORE*

This DPA takes effect on the later of its execution date and the date the Supplier begins processing Duckworks Personal Data. It remains effective for as long as the Supplier processes Duckworks Personal Data. Confidentiality, audit/evidence, incident cooperation, return/deletion and any obligations that by nature must survive shall continue as necessary after termination.

## 26. Execution

**Applicability:** *CORE*

Authorized representatives should execute this DPA or incorporate it into a binding electronic contract or other legal act in writing, including electronic form.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>For Duckworks</strong></th>
<th><strong>For Supplier</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Name: [____________________]<br />
Title: [____________________]<br />
Signature: [________________]<br />
Date: [____________________]</td>
<td>Name: [____________________]<br />
Title: [____________________]<br />
Signature: [________________]<br />
Date: [____________________]</td>
</tr>
</tbody>
</table>

## Schedule 1 - Processing Description and AI Data Map

**Legal basis for schedule:** *GDPR Article 28(3) requires the processor contract to state the subject matter and duration, nature and purpose, data types, data-subject categories, and controller obligations/rights.*

| **Field**                              | **Required entry**                                                                                        |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------|
| AI system / AI ID                      | \[e.g., AI-006 PondGPT\]                                                                                  |
| Service / product / module             | \[supplier service and relevant AI features\]                                                             |
| Subject matter                         | \[what processing service is provided\]                                                                   |
| Duration                               | \[term + post-termination handling\]                                                                      |
| Nature of processing                   | \[collection, access, storage, retrieval, generation, classification, transmission, deletion, etc.\]      |
| Purpose(s)                             | \[specific instructed purposes only\]                                                                     |
| Duckworks role                         | Controller / Processor for upstream controller                                                            |
| Supplier role                          | Processor / Subprocessor                                                                                  |
| Data subjects                          | Employees / applicants / customers / users / contacts / other                                             |
| Personal Data categories               | Identity/contact; account; support content; documents; usage; device/logs; CV/application; other          |
| Special-category data                  | Prohibited unless expressly approved / \[approved category + condition\]                                  |
| Criminal-conviction data               | Prohibited unless expressly approved and lawful / \[details\]                                             |
| Input sources                          | Direct user input / Duckworks systems / approved retrieval repositories / API integrations                |
| Outputs containing Personal Data       | \[possible/expected categories\]                                                                          |
| Processing locations                   | \[EEA countries / third countries\]                                                                       |
| Retention                              | \[content / logs / backups / support tickets\]                                                            |
| Authorized users                       | \[roles/groups\]                                                                                          |
| Human review by Supplier               | None / limited / \[purpose + access controls\]                                                            |
| Automated decision/profiling relevance | No / possible / yes - describe                                                                            |
| Duckworks rights/instructions          | Configuration, access, export, restriction, deletion, audit, suspension, change approval as stated in DPA |

### S1.1 Data flow summary

| **Step** | **Source**  | **Processing / AI operation** | **Destination / recipient** | **Personal Data?** | **Evidence**      |
|----------|-------------|-------------------------------|-----------------------------|--------------------|-------------------|
| 1        | \[source\]  | \[ingest/retrieve\]           | \[service\]                 | Y/N                | \[diagram/log\]   |
| 2        | \[service\] | \[inference/RAG/tool call\]   | \[model/subprocessor\]      | Y/N                | \[architecture\]  |
| 3        | \[service\] | \[output/logging\]            | \[user/log store\]          | Y/N                | \[config\]        |
| 4        | \[support\] | \[support/diagnostics\]       | \[authorized staff\]        | Y/N                | \[access record\] |

## Schedule 2 - Technical and Organizational Measures (TOMs)

**Legal basis:** *GDPR Articles 28(3)(c) and 32. Measures must be appropriate to the risk; the examples below are a Duckworks baseline to tailor to the service.*

| **Control area**     | **Minimum expectation**                                                                                                                    | **Evidence** | **Status**     |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|--------------|----------------|
| Governance           | Documented security/privacy program; named owners; risk assessment; policies; control review.                                              | \[evidence\] | Required / N/A |
| Identity & access    | SSO/MFA where appropriate; RBAC; least privilege; joiner/mover/leaver; privileged access review.                                           | \[evidence\] | Required / N/A |
| Encryption           | Encryption in transit and at rest where appropriate; key management; secrets protection.                                                   | \[evidence\] | Required / N/A |
| Tenant isolation     | Logical separation; access-scoping; controls preventing cross-customer retrieval or memory leakage.                                        | \[evidence\] | Required / N/A |
| Logging & monitoring | Security/admin/access logs; protected log integrity; retention; anomaly detection; investigation access.                                   | \[evidence\] | Required / N/A |
| Secure SDLC/change   | Code/config review; vulnerability management; release controls; dependency/model change assessment.                                        | \[evidence\] | Required / N/A |
| AI-specific security | Prompt-injection defenses; untrusted-content controls; tool permission boundaries; RAG authorization; model/service supply-chain controls. | \[evidence\] | Risk-based     |
| Data handling        | Data classification; minimization; retention configuration; secure deletion; backup management.                                            | \[evidence\] | Required       |
| Personnel            | Confidentiality; screening where lawful/appropriate; security/privacy training; human-review restrictions.                                 | \[evidence\] | Required       |
| Resilience           | Backups; restoration testing; availability/resilience; incident response; BCP/DR as appropriate.                                           | \[evidence\] | Risk-based     |
| Testing              | Regular testing/assessment of TOM effectiveness; independent assurance where appropriate.                                                  | \[evidence\] | Risk-based     |
| Incident response    | Documented detection, escalation, evidence preservation, notification and remediation.                                                     | \[evidence\] | Required       |

## Schedule 3 - Approved AI Data Use and Model-Improvement Matrix

| **Default rule.** Any row not explicitly approved is prohibited for Duckworks data. “Service operation” does not automatically include model training, fine-tuning or cross-customer evaluation. |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Processing use**                   | **Approved?**      | **Scope/purpose** | **Retention** | **Conditions**                             |
|--------------------------------------|--------------------|-------------------|---------------|--------------------------------------------|
| Provide contracted inference/service | Yes                | \[purpose\]       | \[retention\] | Core service                               |
| Security/fraud/abuse detection       | \[Y/N\]            | \[scope\]         | \[retention\] | Necessary support use only                 |
| Troubleshooting/support              | \[Y/N\]            | \[scope\]         | \[retention\] | Human access restrictions apply            |
| Customer-specific fine-tuning        | No unless approved | \[model\]         | \[retention\] | Define ownership/deletion                  |
| Shared/general model training        | No unless approved | \[exact purpose\] | \[retention\] | Requires separate review                   |
| Model evaluation/benchmarking        | No unless approved | \[scope\]         | \[retention\] | No shared prompt library by default        |
| Human quality review                 | No unless approved | \[purpose/roles\] | \[retention\] | Authorized reviewers only                  |
| Advertising/marketing                | No                 | N/A               | N/A           | Prohibited                                 |
| Sale/data brokerage                  | No                 | N/A               | N/A           | Prohibited                                 |
| Persistent user memory/profile       | No unless approved | \[scope\]         | \[retention\] | Configurable/off by default where feasible |

### S3.1 Approved Model Improvement - additional record

Complete only when Duckworks expressly authorizes a model-improvement purpose.

| **Field**                        | **Required detail**                                                |
|----------------------------------|--------------------------------------------------------------------|
| Model / version                  | \[exact model\]                                                    |
| Data categories                  | \[specific categories\]                                            |
| Training purpose                 | \[purpose\]                                                        |
| Legal role for this activity     | Processor / Controller / Joint controller - validated by Legal/DPO |
| Legal basis / instruction        | \[controller assessment / documented instruction\]                 |
| De-identification/anonymization  | \[method + limitations\]                                           |
| Access                           | \[teams/roles\]                                                    |
| Retention                        | \[period\]                                                         |
| Downstream reuse                 | \[prohibited/limited\]                                             |
| Deletion / unlearning capability | \[what is technically possible; limitations\]                      |
| Impact on outputs                | \[memorization/reproduction controls\]                             |
| Approval                         | \[DPO/Legal/AI Governance/Business Owner\]                         |

## Schedule 4 - Approved Subprocessors

| **Subprocessor** | **Function**                      | **Personal Data** | **Location(s)** | **Transfer basis**   | **Notice date** | **Status** |
|------------------|-----------------------------------|-------------------|-----------------|----------------------|-----------------|------------|
| \[name\]         | \[hosting/model/moderation/etc.\] | \[categories\]    | \[country\]     | Adequacy / SCC / N/A | \[date\]        | Approved   |
| \[name\]         | \[function\]                      | \[categories\]    | \[country\]     | \[basis\]            | \[date\]        | Approved   |

### S4.1 General authorization process

- Supplier notice period before a new/replacement Subprocessor: \[30\] days unless urgent security/continuity circumstances justify shorter notice and Supplier explains the reason.

- Notice must identify identity, function, locations, data categories and applicable transfer mechanism.

- Duckworks may object on reasonable data-protection grounds within \[15\] days of notice.

- If the Parties cannot resolve a substantiated objection, available options are: do not use the Subprocessor for Duckworks; provide an alternative configuration; suspend affected processing; or terminate the affected service without penalty, subject to the Main Agreement and counsel-approved terms.

## Schedule 5 - International Transfer and Breach Addendum

### S5.1 Transfer register

| **Exporter role** | **Importer role** | **Country** | **Data / processing** | **Mechanism**          | **SCC module / adequacy scope** | **Supplementary measures** |
|-------------------|-------------------|-------------|-----------------------|------------------------|---------------------------------|----------------------------|
| \[Controller\]    | \[Processor\]     | \[country\] | \[scope\]             | Adequacy / SCC / other | \[module/details\]              | \[measures\]               |
| \[Processor\]     | \[Subprocessor\]  | \[country\] | \[scope\]             | Adequacy / SCC / other | \[module/details\]              | \[measures\]               |

### S5.2 Breach notification record

| **Information item**                 | **Supplier initial notice**   | **Follow-up requirement**      |
|--------------------------------------|-------------------------------|--------------------------------|
| Date/time Supplier became aware      | \[timestamp\]                 | Confirm/update if changed      |
| Nature of breach                     | \[known facts\]               | Root cause when known          |
| Affected systems/services            | \[scope\]                     | Version/tenant/components      |
| Data subjects / records              | \[categories/count if known\] | Refine estimates               |
| Data categories                      | \[categories\]                | Sensitivity/special categories |
| Likely consequences                  | \[initial assessment\]        | Update risk analysis           |
| Containment/remediation              | \[actions\]                   | Completion/effectiveness       |
| Contact point                        | \[name/contact\]              | 24/7 escalation if material    |
| Regulator/data-subject communication | \[none/planned/required\]     | Coordinate unless law prevents |
| Evidence preserved                   | \[logs/snapshots/etc.\]       | Evidence index                 |

## Schedule 6 - Retention, Return and Deletion Plan

| **Data store / artifact**         | **Retention during service** | **Termination action** | **Backup tail** | **Deletion evidence** | **Exception**            |
|-----------------------------------|------------------------------|------------------------|-----------------|-----------------------|--------------------------|
| Prompts/conversations             | \[period\]                   | Return/Delete          | \[days\]        | \[certificate/log\]   | \[legal hold\]           |
| Uploaded files                    | \[period\]                   | Return/Delete          | \[days\]        | \[evidence\]          | \[exception\]            |
| Retrieval index / embeddings      | \[period\]                   | Delete                 | \[days\]        | \[evidence\]          | \[exception\]            |
| Outputs                           | \[period\]                   | Return/Delete          | \[days\]        | \[evidence\]          | \[exception\]            |
| Security/audit logs               | \[period\]                   | Delete per retention   | \[days\]        | \[evidence\]          | \[security/legal\]       |
| Support tickets                   | \[period\]                   | Delete/redact          | \[days\]        | \[evidence\]          | \[legal\]                |
| Fine-tuning artifacts if approved | \[period\]                   | \[delete/retain\]      | \[days\]        | \[evidence\]          | \[technical limitation\] |

### S6.1 Deletion / return certificate

**Service / tenant:** \[Complete before execution\]

**Termination / deletion instruction date:** \[Complete before execution\]

**Return completed:** \[Complete before execution\]

**Primary deletion completed:** \[Complete before execution\]

**Backups scheduled for expiry by:** \[Complete before execution\]

**Residual legal retention and basis:** \[Complete before execution\]

**Known model/unlearning limitation:** \[Complete before execution\]

**Authorized certifier:** \[Complete before execution\]

**Certificate date:** \[Complete before execution\]

## Schedule 7 - Data Subject Request Assistance Workflow

| **Step** | **Supplier action**                                                                                         | **Target**                 | **Evidence**        |
|----------|-------------------------------------------------------------------------------------------------------------|----------------------------|---------------------|
| 1        | Forward request received directly to Duckworks privacy contact; preserve original request.                  | Within \[1\] business day  | Ticket/email        |
| 2        | Confirm systems and likely data locations.                                                                  | Within \[2\] business days | Search plan         |
| 3        | Execute Duckworks instruction for access/correction/export/restriction/deletion where technically possible. | Per Duckworks due date     | Action log/export   |
| 4        | Identify data that cannot be acted on and explain technical/legal reason.                                   | With response              | Exception rationale |
| 5        | Confirm completion and residual backup/model limitations.                                                   | With response              | Completion record   |

## Schedule 8 - Audit and Privacy Evidence Register

| **ID** | **Evidence**                         | **Owner**                    | **Cadence**                   | **Minimum record**                       |
|--------|--------------------------------------|------------------------------|-------------------------------|------------------------------------------|
| E-01   | Executed DPA + schedules             | Legal / Procurement          | At execution/change           | Current signed version                   |
| E-02   | Processing/data-flow diagram         | Supplier technical owner     | At onboarding/material change | Versioned architecture                   |
| E-03   | TOM evidence / assurance report      | Supplier Security            | Annual / renewal              | Current report/certification + scope     |
| E-04   | Subprocessor register                | Supplier Privacy             | Continuous                    | Current list + notices                   |
| E-05   | Transfer register / SCC annexes      | Supplier Privacy / Legal     | On change                     | Executed mechanism + assessment evidence |
| E-06   | Retention/deletion configuration     | Supplier Technical           | Onboarding/change             | Config evidence                          |
| E-07   | AI data-use / training configuration | Supplier AI/Privacy          | Onboarding/change             | Contract + product setting evidence      |
| E-08   | Access and human-review controls     | Supplier Security/Operations | Annual/change                 | Policy/config/access review              |
| E-09   | Incident records                     | Supplier Security/Privacy    | Event-driven                  | Notifications + RCA + remediation        |
| E-10   | Data-subject request support records | Supplier Privacy             | Event-driven                  | Tickets/exports/completion               |
| E-11   | Deletion certificate                 | Supplier Privacy/Operations  | Termination                   | Signed/electronic evidence               |
| E-12   | Material privacy change notices      | Supplier Product/Privacy     | Event-driven                  | Notice + Duckworks decision              |

## Schedule 9 - Duckworks DPA Review Checklist

☐ Role assessment completed and factual controller/processor relationship supported.

☐ Schedule 1 fully describes subject matter, duration, nature, purpose, Personal Data and data subjects.

☐ Documented-instruction clause includes third-country transfers and unlawful-instruction notification.

☐ Confidentiality and Article 32 security obligations are included.

☐ Subprocessor authorization, notice, equivalent obligations and liability are included.

☐ Data-subject rights assistance is included.

☐ Articles 32-36 assistance is included.

☐ Return/delete choice and legal-retention exception are included.

☐ Audit/information rights are included.

☐ AI data-use / Model Improvement settings are explicitly documented.

☐ Processing locations and Chapter V transfer mechanisms are verified.

☐ Incident process can support Duckworks’ regulatory timelines.

☐ Retention, backups, retrieval stores, embeddings and logs are addressed.

☐ Material privacy changes trigger notice and reassessment.

☐ DPA aligns with AI Vendor Contract, vendor due diligence and Duckworks AI inventory record.

☐ No clause falsely claims ISO/NIST/AI Act alignment equals GDPR compliance.

## Appendix A - GDPR Article 28 Contract Mapping

| **Provision**               | **Requirement summary**                                                                                      | **Template location**        | **Classification**                         |
|-----------------------------|--------------------------------------------------------------------------------------------------------------|------------------------------|--------------------------------------------|
| Art. 28(3) opening text     | Binding written contract; subject matter/duration/nature/purpose/data types/data subjects/controller rights. | Sections 1, 3, 5; Schedule 1 | Mandatory legal when Supplier is processor |
| Art. 28(3)(a)               | Documented instructions incl. transfers; legal requirement notice; unlawful-instruction warning.             | Section 6                    | Mandatory legal                            |
| Art. 28(3)(b)               | Authorized persons confidentiality.                                                                          | Section 8                    | Mandatory legal                            |
| Art. 28(3)(c)               | Article 32 security measures.                                                                                | Section 9; Schedule 2        | Mandatory legal                            |
| Art. 28(3)(d), 28(2), 28(4) | Subprocessor authorization, equivalent obligations, initial processor liability.                             | Section 11; Schedule 4       | Mandatory legal                            |
| Art. 28(3)(e)               | Assistance with Chapter III data-subject rights.                                                             | Section 12; Schedule 7       | Mandatory legal                            |
| Art. 28(3)(f)               | Assistance with Articles 32-36.                                                                              | Sections 13-14               | Mandatory legal                            |
| Art. 28(3)(g)               | Return/delete at controller choice; legal-retention exception.                                               | Section 19; Schedule 6       | Mandatory legal                            |
| Art. 28(3)(h)               | Information to demonstrate compliance; audits/inspections.                                                   | Section 15; Schedule 8       | Mandatory legal                            |
| Art. 28(9)                  | Contract/legal act in writing incl. electronic form.                                                         | Section 26                   | Mandatory legal                            |
| Art. 28(10)                 | Processor determining purposes/means becomes controller for that processing.                                 | Sections 1 and 3             | Mandatory legal rule                       |

## Appendix B - AI-Specific Privacy Control Mapping

| **ID**   | **Control**                             | **Objective**                                                                        | **Location**                | **Classification**                               |
|----------|-----------------------------------------|--------------------------------------------------------------------------------------|-----------------------------|--------------------------------------------------|
| AI-DP-01 | No shared-model training by default     | Prevent unapproved secondary use of Duckworks data.                                  | Section 7 / Schedule 3      | Duckworks control                                |
| AI-DP-02 | Prompt/output/human-review transparency | Identify where Personal Data may be persistently stored or accessed.                 | Sections 7, 10 / Schedule 1 | Duckworks control supporting accountability      |
| AI-DP-03 | RAG / embedding deletion                | Avoid leaving personal data in derivative retrieval artifacts after source deletion. | Section 19 / Schedule 6     | Duckworks control                                |
| AI-DP-04 | Cross-tenant / memory isolation         | Reduce unauthorized disclosure across users/customers.                               | Sections 9, 20              | Duckworks security/privacy control               |
| AI-DP-05 | Model-data-use change notification      | Reassess new training, retention or human review before use.                         | Section 22                  | Duckworks control                                |
| AI-DP-06 | Model memorization/reproduction support | Investigate and mitigate unexpected disclosure of Personal Data from model behavior. | Sections 7, 14              | Duckworks control / legal analysis case-specific |
| AI-DP-07 | High-impact human-decision boundary     | Do not treat DPA signature as approval for employment/rights-impacting AI.           | Section 21                  | Duckworks governance control                     |

## Appendix C - Duckworks AI Portfolio DPA Applicability Screening

| **System**                | **DPA relevance**       | **Reason / qualification**                                                                                                                                                          |
|---------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AI-001 DuckDesign AI      | Possible                | If supplier processes identifiable engineer/user data, support logs or uploaded content on Duckworks’ behalf. Engineering IP may be confidential but not necessarily Personal Data. |
| AI-002 QuackBot           | Likely                  | Customer/user data, support content and interaction logs may contain Personal Data; vendor role and locations must be verified.                                                     |
| AI-003 FeatherForecast    | Possible / lower        | Depends on whether supplier processing includes identifiable supplier contacts, users or operational logs.                                                                          |
| AI-004 WingInspect Vision | Possible                | Images may contain individuals or identifiers depending on camera placement and dataset; validate facts.                                                                            |
| AI-005 DuckTalent AI      | Core / enhanced         | Applicant and recruitment data are Personal Data. DPA is necessary if vendor is processor, but does not replace DPIA, legal/fairness review or employment safeguards.               |
| AI-006 PondGPT            | Core / enhanced         | Employee content, documents, identities, logs and retrieval data are likely to include Personal Data. Strong no-training, access, retention and subprocessor controls required.     |
| AI-007 Unregistered GenAI | Not a single DPA object | Decompose into individual tools/use cases. Public AI tools processing Duckworks Personal Data should not be used without approved vendor/privacy terms and governance review.       |

## Appendix D - Authoritative Source Register

| **Source**                                     | **Type**                                     | **Use in template**                                                                                                                   | **Official reference**            |
|------------------------------------------------|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| GDPR - Regulation (EU) 2016/679                | Binding EU regulation                        | Articles 5, 25, 28-36, 44-49 used for controller/processor, security, assistance and transfer provisions.                             | EUR-Lex ELI: reg/2016/679/oj      |
| Commission Implementing Decision (EU) 2021/915 | EU standard clauses under GDPR Article 28(7) | Standard contractual clauses between controllers and processors; may be used instead of bespoke Article 28 text.                      | EUR-Lex ELI: dec_impl/2021/915/oj |
| Commission Implementing Decision (EU) 2021/914 | EU international-transfer SCCs               | Standard contractual clauses for transfers to third countries under GDPR Article 46; includes modular controller/processor scenarios. | EUR-Lex ELI: dec_impl/2021/914/oj |
| EDPB Guidelines 07/2020                        | Regulatory guidance                          | Final guidance on controller/processor concepts and Article 28 arrangements.                                                          | EDPB, final version 7 July 2021   |
| EDPB Opinion 28/2024                           | Regulatory opinion                           | AI-model data-protection considerations including personal data, lawfulness and accountability.                                       | EDPB, adopted 17 December 2024    |

| **Source-use rule.** Check legal conclusions against current official text and actual processing facts before execution. |
|--------------------------------------------------------------------------------------------------------------------------|

## Appendix E - Negotiation Priority Matrix

| **Priority**                 | **Topics**                                                                                                                  | **Duckworks action**                                                                  |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Non-negotiable legal minimum | Article 28 mandatory processor terms; valid Chapter V transfer mechanism when required; security appropriate to risk.       | Escalate to General Counsel/DPO; do not execute if legally required terms are absent. |
| High-priority AI privacy     | No shared-model training by default; prompt/output retention; human review; cross-tenant isolation; model-data-use changes. | Require exception approval if vendor cannot meet baseline.                            |
| High-priority operational    | Breach timing; DSR support; deletion evidence; subprocessor transparency; audit evidence.                                   | Negotiate measurable workflow and evidence.                                           |
| Context-dependent            | Exact audit frequency, notice periods, backup tails, data export formats, support SLAs.                                     | Tailor to risk and vendor service model.                                              |
| Commercial/legal counsel     | Liability caps, indemnities, governing law, insurance, termination fees.                                                    | Do not invent portfolio values; counsel/commercial negotiation required.              |

## Portfolio Disclaimer

Duckworks, Project W.I.N.G., all personnel, systems, datasets, suppliers, contracts, incidents, data flows and processing activities referenced in this document are fictional and were created solely for educational and professional portfolio purposes. This template does not constitute legal advice, an executed data processing agreement, certification evidence, or a determination that GDPR or another law applies to any real organization or service.

Before real use, qualified counsel and the relevant privacy, security, procurement and AI-governance stakeholders must validate the parties’ factual roles, processing description, lawful basis, DPIA obligations, international-transfer mechanism, national requirements, security measures, commercial terms and the current version of the authoritative legal sources.
