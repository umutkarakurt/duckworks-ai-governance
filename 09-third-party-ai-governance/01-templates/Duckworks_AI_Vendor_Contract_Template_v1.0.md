# Duckworks AI Vendor Contract Template

**DUCKWORKS**

AI Vendor Contract Template

Risk-based contractual clauses for third-party AI systems, models, APIs, hosted services and AI-enabled SaaS

| **Document control**    | **Value**                                                                  |
|-------------------------|----------------------------------------------------------------------------|
| Document ID             | DW-WING-TPRM-02                                                            |
| Version                 | 1.0                                                                        |
| Status                  | Portfolio Template - Legal Review Required                                 |
| Organization            | Duckworks (fictional)                                                      |
| Document owner          | General Counsel / Director of Procurement & Vendor Assurance               |
| Governance contributors | AI Governance, Information Security, Privacy, Data & AI, Risk & Compliance |
| Prepared date           | 9 August 2026                                                              |
| Classification          | Portfolio / Synthetic / Non-production                                     |

| **LEGAL STATUS.** This is a fictional portfolio template, not legal advice and not an executed agreement. It is designed to demonstrate how Duckworks would translate AI governance, privacy, security, auditability and third-party risk requirements into contract terms. Qualified legal counsel must tailor governing law, liability, indemnities, sector requirements, national implementing law and commercial terms before real use. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Duckworks principle:** No material AI vendor relationship should proceed without a documented intended purpose, accountable owner, due diligence, enforceable controls, change notification, incident cooperation, exit rights and evidence sufficient for assurance.

## 1. Purpose and How to Use This Template

This template is intended for contracts in which Duckworks acquires, subscribes to, integrates, embeds, fine-tunes, hosts or otherwise depends on a third-party AI capability. It supplements, rather than replaces, Duckworks procurement, security, privacy, legal and risk processes.

The template is deliberately risk-tiered. Clauses labelled CORE are the Duckworks baseline for material AI suppliers. ENHANCED clauses are expected for High/Critical internal risk, employment-related AI, product/safety-impacting AI, customer-facing generative AI, personal-data processing, or substantial operational dependency. CONDITIONAL LEGAL clauses apply only when the stated legal trigger is met.

| **Tag**           | **Meaning**                                       | **Duckworks use**                                                                                                 |
|-------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| CORE              | Default organizational requirement                | Use for all material external AI systems/services unless an approved exception is documented.                     |
| ENHANCED          | Stronger risk-based requirement                   | Use for High/Critical systems, sensitive data, safety/rights impacts, GenAI, or material dependency.              |
| CONDITIONAL LEGAL | Triggered by a legal role or processing condition | Use only after Legal/Privacy confirms applicability; do not infer legal classification from Duckworks risk score. |
| OPTIONAL          | Commercial or use-case-specific term              | Include where relevant to architecture, service model, jurisdiction or negotiation position.                      |

| **Duckworks use case** | **Recommended template modules**                                                                                                            |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| DuckDesign AI          | CORE + ENHANCED security/IP + safety/engineering validation + change control; High-Risk Addendum only if legal screening later confirms it. |
| QuackBot               | CORE + GenAI controls + customer-impact safeguards + prompt/RAG security + incident/change monitoring.                                      |
| FeatherForecast        | CORE + performance/drift + availability/change controls; lighter evidence cadence may be proportionate.                                     |
| WingInspect Vision     | CORE + ENHANCED performance/safety + false-negative testing + human authority + model-change gate.                                          |
| DuckTalent AI          | CORE + ENHANCED people/fairness/privacy + High-Risk AI Addendum if applicable + strict human oversight and audit evidence.                  |
| PondGPT                | CORE + GenAI + access control + data-use/training restrictions + logging + prompt/RAG security.                                             |
| Unregistered GenAI     | Do not contract through informal click-through terms. Route through intake, due diligence and approved contracting before material use.     |

## 2. Agreement Parties and Commercial Cover Sheet

**Applicability:** *CORE*

This AI Services Agreement (the “Agreement”) is entered into as of \[Effective Date\] between Duckworks \[legal entity and registered address\] (“Duckworks”) and \[Vendor legal name, registration number and address\] (“Vendor”). Duckworks and Vendor are each a “Party” and together the “Parties”.

The Agreement governs the AI Services identified in Schedule 1 and any Order Form or Statement of Work that expressly incorporates this Agreement.

| **Field**                    | **Contract value / instruction**                                                           |
|------------------------------|--------------------------------------------------------------------------------------------|
| Vendor legal entity          | \[Insert\]                                                                                 |
| AI service/system/model      | \[Insert product and version\]                                                             |
| Duckworks AI inventory ID    | \[AI-\_\_\_\]                                                                              |
| Business owner               | \[Insert\]                                                                                 |
| Technical owner              | \[Insert\]                                                                                 |
| Vendor owner                 | \[Insert\]                                                                                 |
| Term                         | \[Initial term / renewal\]                                                                 |
| Fees                         | \[Order Form\]                                                                             |
| Hosting/data regions         | \[Insert\]                                                                                 |
| Internal Duckworks risk tier | \[Low / Moderate / High / Critical - not a legal classification\]                          |
| Preliminary legal role       | \[Vendor provider / processor / subprocessor / model provider / other - Legal to confirm\] |

## 3. Definitions and Interpretation

**Applicability:** *CORE*

The following definitions apply unless an Order Form defines a narrower term. Legal definitions that are incorporated by reference take their meaning from the applicable law, not from Duckworks internal risk terminology.

| **Term**                     | **Template definition**                                                                                                                                                                                                                                                      |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AI Component                 | Any AI model, algorithm, AI-enabled function, dataset-dependent inference capability, AI agent, model endpoint, AI tool, service, library or material AI-related component supplied or controlled by Vendor.                                                                 |
| AI System                    | A system within the meaning of applicable AI law where that law applies; otherwise the AI-enabled system or service described in Schedule 1.                                                                                                                                 |
| Approved Purpose             | The intended purpose, authorized users, decision boundary and operating context stated in Schedule 1.                                                                                                                                                                        |
| Customer Data                | Data, prompts, files, content, records, telemetry or other information submitted by or for Duckworks, excluding Vendor-owned service metadata expressly identified in Schedule 1.                                                                                            |
| Output                       | Any prediction, recommendation, ranking, generated content, classification, alert, design suggestion or other inference produced by the AI Service for Duckworks.                                                                                                            |
| Material Change              | A change reasonably capable of altering intended purpose, legal classification, risk, performance, security, data use, human oversight, affected population, model behavior, interoperability or Vendor dependency, including a new foundation/model version where material. |
| Security Incident            | An event compromising or reasonably suspected to compromise confidentiality, integrity, availability, authentication, authorization or resilience of the AI Service or Duckworks data.                                                                                       |
| AI Incident                  | A harmful, unsafe, discriminatory, materially inaccurate, uncontrolled, anomalous or otherwise governance-significant AI behavior, including any event that may meet a statutory serious-incident definition.                                                                |
| High-Risk AI System          | Only an AI system legally classified as high-risk under applicable law. Duckworks High/Critical internal risk ratings do not create this status.                                                                                                                             |
| Subprocessor / Subcontractor | A third party engaged by Vendor that processes Duckworks Personal Data or materially contributes to the AI Service, model, hosting, inference, moderation, monitoring or support.                                                                                            |

## 4. Approved Purpose, Use Restrictions and Decision Boundary

**Applicability:** *CORE*

Vendor shall provide the AI Service only for the Approved Purpose in Schedule 1. Vendor shall not materially expand or alter the functional purpose of the AI Service for Duckworks without Duckworks written approval and completion of any required reassessment.

- The authorized users, affected persons, business process and expected outputs shall be documented before production use.

- The Vendor shall identify use cases it prohibits, discourages or considers outside validated operating conditions.

- Duckworks may impose narrower internal restrictions than Vendor acceptable-use terms.

- No autonomous consequential decision authority is created merely because the AI Service technically supports automation.

Duckworks organizational practice. This clause operationalizes intended-purpose governance and supports reassessment when purpose or autonomy changes.

## 5. Regulatory Role Allocation and Compliance Cooperation

**Applicability:** *CONDITIONAL LEGAL + CORE*

Each Party shall comply with laws applicable to its own role. The Parties shall document their preliminary AI regulatory roles in Schedule 1 and shall promptly reassess those roles following a Material Change, rebranding, substantial modification, intended-purpose modification or change in the supply chain.

- Vendor shall provide information reasonably necessary for Duckworks to determine whether it acts as deployer, provider, importer, distributor, product manufacturer, controller, processor or another regulated role.

- Where Vendor is the legal provider of an AI system or model, Vendor remains responsible for obligations that applicable law assigns to that role and shall not contractually mischaracterize Duckworks as the provider solely to avoid those obligations.

- Where Duckworks becomes a provider by operation of law, Vendor shall provide the information, capabilities, technical access and assistance required by Schedule 5.

- A contractual allocation of tasks does not override statutory responsibility.

## 6. Vendor Representations on AI System Status

**Applicability:** *CORE*

Vendor represents, on the Effective Date and at each renewal, that the disclosures in Schedule 1 are complete and not materially misleading to Vendor’s knowledge. Vendor shall identify whether the service includes a general-purpose AI model, open-source model, third-party model, embedded AI function or safety-related component.

- Vendor shall disclose material limitations, known failure modes and reasonably foreseeable misuse relevant to Duckworks use.

- Vendor shall disclose any geographic or sector restrictions material to lawful use.

- Vendor shall disclose any material dependence on a single third-party model, cloud or data service that could affect continuity, security or compliance.

- Any compliance certification or conformity claim must identify its scope, issuer, validity period and exclusions.

## 7. Documentation, Transparency and Instructions for Use

**Applicability:** *CORE; ENHANCED for legally high-risk systems*

Vendor shall provide and maintain documentation sufficient for Duckworks to configure, use, monitor and govern the AI Service appropriately. Documentation shall be updated following Material Changes and shall be made available in a format that Duckworks can retain as contract evidence.

- Intended purpose, capabilities, limitations and unsupported uses.

- Relevant accuracy/performance metrics, evaluation method, validation context and known conditions that degrade performance.

- Human oversight expectations and technical controls available to support interpretation, review, override, escalation and suspension.

- Input specifications, relevant data dependencies, integrations and permissions.

- Logging, monitoring, retention and audit capabilities.

- Maintenance, update, deprecation and support requirements.

- For a general-purpose AI model supplied for integration, information reasonably necessary to understand capabilities/limitations and integrate the model lawfully and safely.

Where the AI Act high-risk requirements apply, Article 13 requires provider instructions for use with specified transparency content. Article 53 also requires certain documentation to downstream AI-system providers integrating GPAI models.

## 8. Customer Data, Training Data and Vendor Data Use

**Applicability:** *CORE*

Vendor shall process Customer Data solely to provide, secure, support and improve the contracted service in accordance with documented Duckworks instructions and Schedule 4. Unless Duckworks gives prior written approval, Vendor shall not use Customer Data, prompts, outputs or Duckworks Confidential Information to train, fine-tune, evaluate or improve a model made available to other customers or the public.

- Any approved model-improvement use shall state the exact data categories, purpose, retention, access, de-identification controls, model scope and deletion/unlearning limitations.

- Vendor shall not sell Customer Data or disclose it for advertising, profiling or unrelated product development.

- Vendor shall disclose whether prompts, outputs or content are reviewed by humans and under what access controls.

- Data retention shall be limited to the periods in Schedule 4 and operationally necessary backups, with documented deletion controls.

- Vendor shall support export and deletion at termination and provide deletion confirmation on request.

The no-training default is a Duckworks organizational control, not a universal statutory rule. If personal data are processed, GDPR purpose limitation, processor instructions and other applicable requirements remain separate legal duties.

## 9. Data Protection and International Transfers

**Applicability:** *CONDITIONAL LEGAL*

Where Vendor processes Personal Data on behalf of Duckworks, Schedule 4 forms part of this Agreement and the Parties shall enter any additional data-processing or transfer instrument required by applicable data-protection law.

- Vendor shall process Personal Data only on documented instructions, maintain confidentiality, implement appropriate security, control subprocessors, assist with data-subject rights and compliance obligations, and return/delete Personal Data at termination as required by the applicable processor terms.

- Vendor shall notify Duckworks without undue delay of a Personal Data Breach and, contractually, within \[24\] hours of awareness for material incidents unless a shorter period is required in Schedule 7.

- Where Personal Data is transferred outside the EEA without an adequacy basis, the Parties shall implement an appropriate transfer mechanism and necessary supplementary measures.

- Vendor shall provide information reasonably requested for Duckworks DPIA or privacy reassessment.

GDPR Article 28 imposes mandatory processor-contract content when Vendor is a processor. The \[24\]-hour notification target is a Duckworks contractual safeguard; GDPR itself requires a processor to notify the controller without undue delay.

## 10. Information Security Baseline

**Applicability:** *CORE; ENHANCED for sensitive or connected AI*

Vendor shall maintain a documented information-security program appropriate to the risks of the AI Service and Customer Data. Minimum requirements are set out in Schedule 3 and shall be implemented throughout the Term.

- Identity and access management, least privilege, strong authentication and privileged-access controls.

- Encryption in transit and at rest where appropriate to risk.

- Secure configuration, vulnerability management, patching and dependency management.

- Separation of customer tenants and controls against cross-user or cross-tenant data exposure.

- Logging and monitoring sufficient to investigate security and AI incidents.

- Secure development practices and independent security testing proportionate to the service.

- Backup, recovery, resilience and tested business-continuity procedures.

- Controls for secrets, API keys, service accounts, connectors, tools and agent permissions.

## 11. AI-Specific Security and Supply-Chain Controls

**Applicability:** *ENHANCED for GenAI, externally exposed AI, safety-impacting AI or significant integrations*

Vendor shall maintain controls proportionate to AI-specific threats and supply-chain dependencies. Vendor shall disclose material third-party model/service dependencies and shall not introduce a dependency that materially reduces Duckworks security or assurance without prior notice.

- Prompt injection and indirect prompt injection defenses where applicable.

- Retrieval-augmented generation protections against unauthorized retrieval, poisoning and privilege bypass.

- Input/output validation, abuse controls and isolation for tool-using or agentic functions.

- Model, dataset, package and artifact provenance controls appropriate to the architecture.

- Controls for unsafe generated code, executable content or tool invocation.

- Adversarial testing/red-teaming commensurate with exposure and impact.

- Secure update and rollback mechanisms for models and AI components.

These are Duckworks risk-based security requirements informed by recognized AI security guidance; they are not presented as a single statutory checklist.

## 12. Performance, Validation, Robustness and Safety

**Applicability:** *CORE; ENHANCED for employment, safety, product quality and material decisions*

Vendor shall identify the metrics and validation evidence used to support claimed performance. Schedule 2 shall define any minimum acceptance threshold, operating boundary and revalidation trigger material to Duckworks deployment.

- Vendor shall not present a benchmark as representative of Duckworks operating context unless the conditions are reasonably comparable.

- Vendor shall disclose material known error patterns, limitations and distribution-shift sensitivity relevant to Duckworks use.

- Where false negatives or false positives can materially affect safety, rights or quality, Vendor shall support scenario-specific testing and threshold configuration.

- Vendor shall provide reasonable cooperation with Duckworks pilot testing and post-deployment performance review.

- If agreed performance falls below a Critical threshold, Duckworks may suspend affected AI functions pending remediation.

## 13. Human Oversight, Override and Automation Bias Safeguards

**Applicability:** *ENHANCED for consequential decision support*

Vendor shall provide the features and documentation reasonably necessary for Duckworks to implement meaningful human oversight consistent with the Approved Purpose.

- Outputs must be identifiable as AI-generated or AI-assisted where required by the use case.

- Authorized reviewers must be able to inspect relevant context, reject or override outputs, escalate uncertainty and stop use where necessary.

- Vendor shall disclose design choices likely to create misleading confidence, hidden automation, or materially constrained override capability.

- For employment, safety, product release or other consequential use, Vendor shall not disable configured human-review controls without Duckworks approval.

- The Parties shall agree escalation and fallback procedures in Schedule 1.

## 14. Generative AI and Content Controls

**Applicability:** *ENHANCED for QuackBot, PondGPT, DuckDesign AI or other GenAI*

Where the AI Service generates text, code, images, designs or other content, Vendor shall support configurable safeguards appropriate to the use case.

- Content boundaries, system instructions and moderation controls relevant to the Approved Purpose.

- Controls and documentation addressing hallucination, unsupported claims and unsafe instructions.

- Grounding/retrieval controls where the system uses Duckworks knowledge repositories.

- Citation/provenance or source-attribution functionality where contractually specified and technically available.

- Restrictions on autonomous execution of generated code or actions unless separately approved.

- Mechanisms for reporting harmful or materially incorrect outputs and preserving investigation evidence.

## 15. Logging, Monitoring, Audit Trail and Governance Evidence

**Applicability:** *CORE; ENHANCED for High/Critical systems*

Vendor shall provide Duckworks with sufficient logging, telemetry and evidence to monitor use, investigate incidents, test agreed controls and support regulatory or internal-assurance obligations.

- At minimum: service/model version, material configuration changes, administrative actions, relevant authentication events, incidents, agreed performance metrics and material availability events.

- For high-risk AI where applicable, the service shall support the automatic logging and deployer retention requirements relevant to Duckworks role, including access/export needed for Duckworks to retain logs under its control.

- Vendor shall preserve incident-relevant evidence following a Duckworks legal hold or investigation request, subject to applicable law.

- Evidence provided for audits shall be current, scoped and attributable to the contracted service rather than generic marketing material.

## 16. Model, Service and Material Change Management

**Applicability:** *CORE*

Vendor shall operate documented change management and shall notify Duckworks in advance of Material Changes. The notice shall contain sufficient information for Duckworks to determine whether risk, privacy, security, legal or business reassessment is required.

- Model/provider replacement, major model-version changes or material fine-tuning.

- Changes to training/data-use practices, retention, subprocessors or hosting region.

- Changes to safety, moderation, logging, access-control or human-oversight features.

- Material changes to accuracy, known limitations, performance thresholds, API behavior or output modality.

- Deprecation of a model or feature relied upon by Duckworks.

- Changes that could cause Duckworks to become a regulated provider or materially alter an existing legal classification.

Schedule 6 contains a default notification matrix. Duckworks may require approval rather than notice for Critical dependencies.

## 17. AI Incidents, Security Incidents and Vulnerability Cooperation

**Applicability:** *CORE*

Vendor shall maintain incident-response processes and promptly notify Duckworks of incidents that materially affect the AI Service, Customer Data, safety, rights, regulatory compliance or Duckworks ability to operate the service as approved.

- Initial notice shall contain known scope, affected systems/data, timing, impact, containment status and a contact point.

- Vendor shall provide phased updates as facts become available and a root-cause/corrective-action report for material incidents.

- Vendor shall preserve relevant logs and cooperate with Duckworks Security, Privacy, Legal, Risk and product/safety teams as applicable.

- Where Vendor has statutory serious-incident or cybersecurity reporting duties, Vendor shall perform them and provide Duckworks information necessary for Duckworks own duties, without delaying urgent containment.

- Vendor shall coordinate vulnerability disclosure and remediation for vulnerabilities affecting the AI Service and its material dependencies.

Contract notification windows in Schedule 7 are negotiated safeguards. Statutory reporting deadlines depend on the specific law, role and incident and must be handled separately.

## 18. Subprocessors, Subcontractors and Model Dependencies

**Applicability:** *CORE*

Vendor remains responsible for its subcontracted performance and shall maintain an up-to-date list of material subprocessors and AI/model dependencies used to deliver the service.

- For Personal Data, subprocessor authorization and flow-down obligations shall comply with Schedule 4.

- Vendor shall provide \[30\] days prior notice of a material new subprocessor/model dependency unless urgent security circumstances require faster change.

- Duckworks may object on reasonable security, privacy, legal, resilience or conflict grounds and the Parties shall seek a commercially reasonable alternative.

- Vendor shall flow down confidentiality, security, data-use, incident and cooperation obligations appropriate to the subcontracted role.

## 19. Audit, Assurance and Evidence Rights

**Applicability:** *CORE; ENHANCED for material/high-risk services*

Vendor shall provide reasonable evidence that the contracted controls are designed and operating. Duckworks shall use a proportionate assurance model and avoid unnecessary duplication where current independent evidence is sufficient.

- Annual or event-driven security/AI assurance package as specified in Schedule 2.

- Access to relevant independent audit reports, certifications, penetration-test summaries and remediation status, subject to appropriate confidentiality controls.

- Questionnaire or evidence refresh on renewal and following a Material Change or significant incident.

- Targeted remote or onsite audit rights where evidence is insufficient, a material incident occurs, a regulator requires access, or High/Critical risk cannot otherwise be validated.

- No certification shall be treated as automatic proof of legal compliance or complete control effectiveness.

## 20. Intellectual Property, Licensing and Output Rights

**Applicability:** *CORE; legal tailoring required*

The Parties shall specify ownership and license rights for Customer Data, Vendor materials, model weights/configuration, fine-tuning artifacts and Outputs. Nothing in this clause authorizes Vendor to use Duckworks Confidential Information for unrelated model training.

- Vendor shall identify material third-party/open-source license conditions that restrict Duckworks intended use, modification, redistribution or product integration.

- Vendor shall disclose if output-use rights differ by model, modality, geography or customer tier.

- For Duckworks-provided training/fine-tuning data, ownership and permitted derivative use shall be expressly stated.

- Vendor shall maintain a process to receive and address credible IP infringement claims relating to the contracted AI Service.

- \[Choose negotiated position\] Vendor warrants/indemnifies for specified IP claims, subject to agreed exclusions and liability terms.

IP ownership, warranties and indemnities are jurisdiction- and service-specific. Qualified counsel should tailor them rather than treating this bracketed language as a default legal position.

## 21. Business Continuity, Resilience, Portability and Exit

**Applicability:** *CORE*

Vendor shall maintain continuity and recovery capabilities proportionate to Duckworks dependency. Schedule 8 shall document exit and transition requirements before production deployment for High/Critical or operationally critical AI services.

- Service recovery objectives and backup/restore arrangements where relevant.

- Advance notice of end-of-life, model retirement or material service discontinuation.

- Export of Customer Data, relevant configurations, prompts/templates, agreed logs and other Duckworks-owned artifacts in a usable format.

- Transition assistance for \[X\] days where agreed and priced in the Order Form.

- Secure deletion and revocation of Duckworks credentials, connectors and access after exit.

- Fallback or degraded-mode procedures for business processes that materially depend on AI.

## 22. Service Levels, Support and Performance Remedies

**Applicability:** *OPTIONAL / COMMERCIAL*

The Order Form shall define availability, support response, capacity, rate limits, maintenance windows and any performance commitments material to Duckworks. Service credits do not limit Duckworks rights to suspend unsafe or non-compliant AI functionality where the Agreement permits suspension.

## 23. Insurance, Liability and Indemnities

**Applicability:** *OPTIONAL / LEGAL REVIEW REQUIRED*

The Parties shall agree liability caps, exclusions, insurance and indemnities appropriate to the risk profile. Duckworks Legal shall separately consider higher or uncapped exposure for categories such as confidentiality breach, data-protection breach, IP infringement, willful misconduct, fraud, regulatory non-cooperation, or bodily injury where legally and commercially appropriate.

This template intentionally does not prescribe monetary caps. Those terms depend on contract value, risk, governing law, market position and insurance.

## 24. Confidentiality and Restricted Information

**Applicability:** *CORE*

Each Party shall protect the other Party’s Confidential Information using at least reasonable care and shall use it only for the Agreement. Vendor shall apply the same restrictions to prompts, uploaded files, embeddings, retrieval content, fine-tuning data, logs and incident evidence containing Duckworks Confidential Information.

- Vendor personnel access shall be limited to authorized need-to-know roles.

- Confidentiality obligations survive termination for the period specified in the master agreement, with trade-secret protection continuing as required by applicable law.

- Disclosure to regulators or authorities shall be handled consistently with applicable law and, where permitted, with prompt notice to Duckworks.

## 25. Suspension, Remediation and Termination Rights

**Applicability:** *CORE*

Duckworks may suspend an affected AI function or data flow where reasonably necessary to contain a material security, privacy, safety, rights, regulatory or operational risk. The Parties shall cooperate on remediation and safe restoration.

- Duckworks may require suspension after a Critical control failure, unauthorized data use, material unnotified change, loss of required human oversight, material performance failure, significant incident or credible unlawful-use concern.

- Vendor shall not retaliate through unrelated service degradation solely because Duckworks exercises a good-faith governance suspension right.

- Termination rights shall include material breach, repeated control failure, inability to remediate unacceptable risk, prohibited or unlawful use, and material non-cooperation with required assurance.

## 26. Records, Regulatory Requests and Cooperation

**Applicability:** *CONDITIONAL LEGAL + CORE*

Each Party shall maintain records required for its role and shall cooperate in good faith with lawful regulatory, supervisory or market-surveillance requests relevant to the AI Service.

- Vendor shall promptly route regulatory inquiries affecting Duckworks to the agreed legal contact, where legally permitted.

- Vendor shall provide documentation within timeframes reasonably necessary for Duckworks to respond to competent authorities.

- Vendor shall not knowingly destroy relevant evidence after notice of an investigation, legal hold or statutory retention requirement.

- Trade secrets and confidential business information shall be protected to the extent permitted by law.

## 27. Order of Precedence, Changes and General Terms

**Applicability:** *CORE*

The master commercial agreement, this AI addendum, Order Form, Schedule 4 Data Protection Addendum and any applicable High-Risk AI Addendum shall be read together. In the event of conflict, the following order applies unless the Parties state otherwise: (1) mandatory law; (2) signed DPA/transfer terms for Personal Data matters; (3) signed High-Risk AI Addendum for AI compliance cooperation; (4) this AI Vendor Contract Template as executed; (5) Order Form/SOW; (6) other incorporated policies. Standard terms, governing law, notices, assignment, force majeure, waiver, severability and dispute resolution shall be stated in the master agreement or Order Form.

## 28. Signature Block

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>For Duckworks</strong></th>
<th><strong>For Vendor</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Name: [ ]<br />
Title: [ ]<br />
Signature: [ ]<br />
Date: [ ]</td>
<td>Name: [ ]<br />
Title: [ ]<br />
Signature: [ ]<br />
Date: [ ]</td>
</tr>
</tbody>
</table>

## Schedule 1 - AI System Description, Intended Purpose and Role Record

| **Field**                                 | **Required entry / guidance**                                                   |
|-------------------------------------------|---------------------------------------------------------------------------------|
| Duckworks AI inventory ID                 | \[AI-\_\_\_\]                                                                   |
| Vendor / product / version                | \[Insert\]                                                                      |
| AI type                                   | \[GenAI / predictive ML / computer vision / other\]                             |
| Approved Purpose                          | \[Precise intended purpose, business process and expected outcome\]             |
| Prohibited / unsupported uses             | \[Insert Vendor and Duckworks restrictions\]                                    |
| Authorized users                          | \[Roles / business units\]                                                      |
| Affected persons / groups                 | \[Applicants / employees / customers / product users / other\]                  |
| Decision boundary                         | \[Advisory / recommendation / human approval required / automated action\]      |
| Human oversight                           | \[Role, competence, override, escalation, stop authority\]                      |
| Data categories                           | \[Public / internal / confidential / personal / special category / IP / other\] |
| Models / material AI dependencies         | \[Provider, model name/version, hosting, third-party services\]                 |
| Integrations / connectors / tools         | \[Insert\]                                                                      |
| Hosting and processing regions            | \[Insert\]                                                                      |
| Internal risk rating                      | \[Low / Moderate / High / Critical\]                                            |
| Preliminary EU AI Act role/classification | \[Legal triage only - provider/deployer/etc.; high-risk status if confirmed\]   |
| GDPR relationship                         | \[Controller-processor / independent controllers / no personal data / other\]   |
| Go-live gate                              | \[Approved / conditional / pilot / blocked\]                                    |
| Review cadence                            | \[Annual / quarterly / event-driven\]                                           |
| Named contacts                            | Duckworks owner: \[ \] \| Vendor product/security/legal: \[ \]                  |

## Schedule 2 - Minimum AI Control and Evidence Requirements

| **Control area**    | **Contract requirement**                                                            | **Minimum evidence**                                            | **Tier**      |
|---------------------|-------------------------------------------------------------------------------------|-----------------------------------------------------------------|---------------|
| Inventory & purpose | System/version/purpose/owner documented and kept current.                           | Schedule 1; release notes; architecture summary.                | CORE          |
| Risk & limitations  | Material limitations, failure modes and operating boundaries disclosed.             | Model/system card, limitations statement, test summary.         | CORE          |
| Data use            | No Duckworks data training beyond approved terms; retention/deletion defined.       | Data-use statement; DPA; deletion evidence.                     | CORE          |
| Human oversight     | Review/override/escalation features and instructions available where consequential. | User guide; workflow evidence; screenshots/config.              | ENHANCED      |
| Performance         | Metrics and validation context defined; revalidation after material changes.        | Evaluation report; versioned benchmark; drift report.           | CORE/ENHANCED |
| AI security         | AI-specific attack paths addressed and tested proportionately.                      | Threat model; test/red-team summary; remediation log.           | ENHANCED      |
| Logging             | Logs sufficient for incident investigation and agreed governance monitoring.        | Logging schema; sample export; retention setting.               | CORE          |
| Change control      | Material changes notified and reassessment supported.                               | Release/change notices; version history.                        | CORE          |
| Incident response   | Security/AI incidents reported, investigated and corrected.                         | IR procedure; incident record; RCA/CAPA.                        | CORE          |
| Supply chain        | Material models/subprocessors/dependencies disclosed.                               | Subprocessor/model list; assurance evidence.                    | CORE          |
| Assurance           | Evidence current and scoped to the service.                                         | Independent report/certification + bridge letter or equivalent. | CORE          |
| Exit                | Data/config/log export and deletion path tested or documented.                      | Exit plan; export format; deletion attestation.                 | High/Critical |

## Schedule 3 - Information Security Requirements

| **Area**                 | **Default Duckworks requirement**                                                                                          |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Identity & access        | SSO/federation where feasible; MFA for privileged access; role-based access; least privilege; periodic access review.      |
| Tenant isolation         | Logical segregation appropriate to service architecture; controls against cross-tenant leakage.                            |
| Encryption               | Encrypted network transport using current protocols; encryption at rest where appropriate to data classification and risk. |
| Secrets & keys           | Secure storage/rotation of credentials, API keys, service accounts and integration secrets.                                |
| Vulnerability management | Risk-based remediation targets; disclosure of material unremediated vulnerabilities affecting Duckworks.                   |
| Secure development       | Change review, dependency management, security testing and protected build/deployment pipeline appropriate to service.     |
| AI-specific security     | Prompt/RAG/tool-invocation protections, adversarial testing and model/artifact provenance controls where applicable.       |
| Logging & monitoring     | Security-relevant logging, detection, incident investigation support and time synchronization.                             |
| Resilience               | Backups/recovery, capacity management, business continuity and tested incident response.                                   |
| Personnel                | Confidentiality, access authorization, security awareness and role-appropriate training.                                   |
| Evidence                 | Current independent assurance report/certification or equivalent evidence; material remediation tracked.                   |

## Schedule 4 - Data Protection Addendum: Minimum Required Terms

Use this schedule only when Vendor processes Personal Data for Duckworks. It is a portfolio summary of minimum contract content and must be replaced or reviewed by qualified privacy counsel for an executed agreement.

| **Required element**    | **Template requirement**                                                                                                                                   |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Processing details      | Subject matter, duration, nature, purpose, types of Personal Data, categories of data subjects, and Duckworks rights/obligations are recorded in an annex. |
| Instructions            | Vendor processes Personal Data only on documented Duckworks instructions, including international transfers unless law requires otherwise.                 |
| Confidentiality         | Authorized personnel are bound by confidentiality.                                                                                                         |
| Security                | Vendor implements appropriate technical and organizational measures and provides sufficient guarantees.                                                    |
| Subprocessors           | Prior specific/general written authorization; advance notice of changes; equivalent data-protection obligations flowed down.                               |
| Data-subject rights     | Vendor assists Duckworks through appropriate technical/organizational measures.                                                                            |
| Articles 32-36 support  | Vendor assists with security, breach response, DPIAs and prior consultation as applicable.                                                                 |
| End of service          | At Duckworks choice, return/delete Personal Data and delete copies unless law requires storage.                                                            |
| Audit/evidence          | Vendor makes information available to demonstrate compliance and permits/contributes to audits.                                                            |
| Unlawful instruction    | Vendor informs Duckworks if it believes an instruction infringes applicable data-protection law.                                                           |
| Breach notice           | Without undue delay; contractual target \[24\] hours for material breach awareness.                                                                        |
| International transfers | Identify transfer locations and implement adequacy/SCC/BCR or other valid mechanism as applicable.                                                         |

## Schedule 5 - High-Risk AI / GPAI Integration Addendum

Conditional legal module. Activate only after Legal confirms the relevant AI Act role and applicability. This schedule is designed to obtain the information and cooperation Duckworks may need where it is a deployer of a high-risk AI system, or where Duckworks becomes a provider integrating a third-party AI model/component into a high-risk AI system.

| **Requirement**                       | **Vendor obligation / evidence**                                                                                                                                                                                         |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Written value-chain cooperation       | Where Article 25(4) applies, Parties specify in writing the necessary information, capabilities, technical access and assistance enabling the high-risk AI provider to comply with applicable obligations.               |
| Technical documentation               | Provide sufficient current documentation regarding system/model architecture, intended purpose, capabilities, limitations, relevant data, testing, integrations and changes, subject to lawful trade-secret protections. |
| Known limitations/failure modes       | Notify Duckworks of known limitations and failure modes material to high-risk integration or use.                                                                                                                        |
| Technical access                      | Provide targeted access reasonably necessary for testing, validation and compliance where legally required and contractually scoped.                                                                                     |
| Instructions for use                  | For provider-supplied high-risk AI, provide the instructions and transparency information required by applicable law.                                                                                                    |
| Logging                               | Support automatic logging, export and retention arrangements necessary for Duckworks obligations where applicable.                                                                                                       |
| Human oversight                       | Provide technical and instructional measures enabling competent human oversight.                                                                                                                                         |
| Post-market monitoring                | Share performance/incident information reasonably necessary for monitoring and corrective action.                                                                                                                        |
| Serious incidents                     | Promptly notify and cooperate on events that may trigger statutory serious-incident duties.                                                                                                                              |
| GPAI downstream information           | Where Vendor supplies a GPAI model for integration, provide and update downstream documentation required by applicable law, including capabilities/limitations and integration information.                              |
| Substantial modification / role shift | Notify Duckworks before changes that could cause a change in legal provider/deployer role or high-risk classification.                                                                                                   |

## Schedule 6 - Material Change Notification Matrix

| **Change type**                                | **Default notice**                                                        | **Duckworks action**                                              |
|------------------------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------|
| Model/provider replacement                     | 60 days before, where practicable; immediate if emergency security change | Reassess performance, legal role, security and approvals.         |
| Major model version / behavior change          | 30 days before production rollout                                         | Impact/risk reassessment; regression test.                        |
| New training/data-use practice                 | 60 days before                                                            | Privacy/legal/data-governance approval required before effect.    |
| New material subprocessor / hosting region     | 30 days before                                                            | Privacy/security/vendor review; objection right where applicable. |
| Change to logging/retention/oversight controls | 30 days before                                                            | Control/evidence reassessment.                                    |
| Critical security patch                        | As soon as practicable                                                    | Security review; expedited approval allowed.                      |
| Service/model deprecation                      | At least 90 days before where commercially feasible                       | Exit/transition plan.                                             |
| Known material performance degradation         | Without undue delay                                                       | Suspend/restrict/revalidate depending on impact.                  |

## Schedule 7 - Incident Notification Matrix

| **Event**                                          | **Contract notification target**                     | **Minimum first notice**                                                              |
|----------------------------------------------------|------------------------------------------------------|---------------------------------------------------------------------------------------|
| Confirmed Personal Data Breach affecting Duckworks | Without undue delay; target \<=24 hours              | Time discovered; data/systems affected; current scope; containment; contact.          |
| Material Security Incident                         | Target \<=24 hours; Critical incident immediately    | Affected service, IOCs/known attack path, containment, data impact, continuity.       |
| Material AI Incident / harmful output pattern      | Target \<=24 hours after confirmation                | Model/version, use context, affected decisions/persons, severity, temporary controls. |
| Potential statutory serious incident               | Immediate escalation to named legal contacts         | Known facts, suspected statutory trigger, reporting deadlines/authorities if known.   |
| Material vulnerability with active exploitation    | Immediate / \<=24 hours                              | Affected versions, exploit status, mitigations, patch plan.                           |
| Critical service outage                            | Per SLA; immediate if safety/rights process affected | Scope, start time, workaround, expected restoration.                                  |

These are Duckworks contractual targets. They do not replace statutory notification/reporting deadlines, which depend on the applicable law and each Party’s role.

## Schedule 8 - Exit, Portability and Decommissioning Checklist

| **Exit requirement**                                                            | **Owner**                 | **Evidence / completion**          |
|---------------------------------------------------------------------------------|---------------------------|------------------------------------|
| Export Customer Data and agreed AI artifacts in documented format               | Vendor                    | Export package + checksum/manifest |
| Export relevant logs/configurations/prompts/templates where contractually owned | Vendor                    | Archive / handover record          |
| Revoke Vendor access, API keys, service accounts and connectors                 | Duckworks + Vendor        | Access revocation record           |
| Disable integrations and automation safely                                      | Duckworks technical owner | Change ticket / rollback evidence  |
| Confirm deletion/return of Customer Data                                        | Vendor                    | Deletion attestation               |
| Identify residual legal/backup retention                                        | Vendor + Privacy          | Retention exception record         |
| Transition to replacement / manual fallback                                     | Business owner            | Continuity sign-off                |
| Update AI inventory and risk record to Retired/Terminated                       | AI Governance Lead        | QuackTrack record                  |
| Close open incidents and preserve required evidence                             | Security/Risk/Legal       | Case closure / legal hold record   |

## Appendix A - Legal, Framework and Duckworks Practice Classification

This appendix prevents the template from presenting every clause as a legal obligation. Applicability must be validated per system, role, jurisdiction and contract architecture.

| **Category**                              | **Source / trigger**                                                                                                    | **What it supports in this template**                                                                                                                                                     | **Caution**                                                                                                                                               |
|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mandatory legal requirement - conditional | EU AI Act, consolidated 27 Jul 2026, Article 25(4)                                                                      | Written agreement specifying information, capabilities, technical access and assistance when a high-risk AI provider depends on third-party AI/model/tools/services/components/processes. | Applies only when Article 25(4) trigger and legal roles are met.                                                                                          |
| Mandatory legal requirement - conditional | EU AI Act Articles 13, 26, 53, 72-73                                                                                    | Instructions/transparency, deployer monitoring/logging, GPAI downstream documentation, post-market monitoring and incident cooperation clauses.                                           | Many obligations attach directly to providers/deployers rather than universally requiring contract clauses; contract terms are used to enable compliance. |
| Mandatory legal requirement - conditional | GDPR Article 28                                                                                                         | Processor contract terms, subprocessors, security assistance, audit, deletion/return, documented instructions.                                                                            | Only when Vendor is a processor for Duckworks.                                                                                                            |
| Mandatory legal requirement - conditional | GDPR Articles 32, 33, 35, 46                                                                                            | Security, breach cooperation, DPIA support, international-transfer safeguards.                                                                                                            | Applicability depends on processing and transfer facts; 24-hour vendor notice is Duckworks contract policy, not the GDPR statutory wording.               |
| Voluntary framework guidance              | NIST AI RMF 1.0, Govern 6 and Manage 3                                                                                  | Third-party AI/supply-chain risk governance, monitoring and documented controls.                                                                                                          | Voluntary framework, not law.                                                                                                                             |
| Voluntary standard                        | ISO/IEC 42001:2023 public description                                                                                   | Management-system approach to responsible development/provision/use of AI, governance and continual improvement.                                                                          | This template does not reproduce ISO clauses or claim conformity/certification.                                                                           |
| Recognized cybersecurity guidance         | ENISA Multilayer Framework for Good Cybersecurity Practices for AI                                                      | Lifecycle and supply-chain security expectations for AI components and actors.                                                                                                            | Good-practice guidance, not a universal legal contract checklist.                                                                                         |
| Duckworks organizational practice         | Project W.I.N.G. governance baseline                                                                                    | No-training default, material-change notice, evidence pack, enhanced audit, human oversight, exit plan, proportionality.                                                                  | Internal control choices intended to manage Duckworks risk; subject to commercial negotiation and approved exceptions.                                    |
| Project assumption                        | Duckworks fictional EU-focused organization; mixed internal/third-party AI; personal/confidential data may be processed | Template prioritizes EU AI Act/GDPR and European security context.                                                                                                                        | Real jurisdiction, sector, product and role must be confirmed before use.                                                                                 |

## Appendix B - Source Register

1.  Duckworks AI Governance Project - Business Scenario (Project W.I.N.G., seven-system portfolio and third-party/shadow AI problem).

2.  Duckworks AI Governance Project - In-Scope and Out-of-Scope Items (third-party AI assessment areas, contractual obligations, incident notification, service continuity, model/service change and exit).

3.  Duckworks AI Governance Project - Project Objectives (strengthen third-party AI governance; establish evidence and auditability).

4.  Duckworks AI Governance Project - Assumptions Register v1.0 (mixed internal/third-party AI; confidential/personal data; legal mappings are screening outputs; evidence maturity).

5.  Duckworks AI Governance Project - Stakeholder Register v1.0 (General Counsel, DPO, CISO, Procurement & Vendor Assurance, AI Governance Lead roles).

6.  Regulation (EU) 2024/1689 (Artificial Intelligence Act), consolidated text 27 July 2026: https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng

7.  Regulation (EU) 2016/679 (GDPR): https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng

8.  NIST Artificial Intelligence Risk Management Framework (AI RMF 1.0): https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf

9.  NIST AI RMF Core / Playbook: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ and https://airc.nist.gov/airmf-resources/playbook/

10. ISO/IEC 42001:2023 public standard description: https://www.iso.org/standard/42001

11. ENISA, Multilayer Framework for Good Cybersecurity Practices for AI: https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai

## Portfolio Disclaimer

Duckworks, Project W.I.N.G., all named personnel, AI systems, suppliers, data, contractual decisions and evidence referenced in this template are fictional and were created solely for educational and professional portfolio purposes. The template demonstrates governance design and contracting controls; it is not legal advice, an executed contract, regulatory approval, certification evidence or a determination of legal compliance.
