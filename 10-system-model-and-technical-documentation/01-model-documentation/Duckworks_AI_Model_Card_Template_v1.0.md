# Duckworks AI Model Card Template

**DUCKWORKS**

**AI MODEL CARD TEMPLATE**

Concise, auditable model-level documentation for governed AI systems

| **Document control** | **Value**                              |
|----------------------|----------------------------------------|
| **Document ID**      | DW-WING-TPL-MC-01                      |
| **Version**          | 1.0                                    |
| **Status**           | Controlled Template                    |
| **Organization**     | Duckworks (fictional)                  |
| **Owner**            | Head of Data & AI / AI Governance Lead |
| **Classification**   | Portfolio / Synthetic / Non-production |

**Purpose.** Use this template to create a concise model card for each material model or model-based component used within a governed Duckworks AI system. It is designed for portfolio transparency, model limitations, evaluation evidence, human oversight, monitoring, and governance traceability.

This template is not a substitute for the AI System Inventory, Business Use Case, AI/Algorithmic Impact Assessment, DPIA, FRIA/HUDERIA where applicable, AI Risk Assessment, full Model Documentation Record, or regulatory technical documentation.

## 1. Completion and Governance Instructions

The model card should be completed by the Technical / Model Owner and reviewed by the AI Governance Lead. Specialist review is required where the model affects privacy, security, employment, product safety, fundamental rights, or another regulated domain.

| **Rule**                                  | **Duckworks expectation**                                                                                                                                                                                    |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **One card per material model/component** | Create or update a card for each material model, embedding/ranking component, vendor model service, or materially distinct configuration used in a governed AI system.                                       |
| **No invented evidence**                  | Unknown architecture, datasets, performance, fairness, thresholds, provider details, or test results must be recorded as TBD / Not Evidenced.                                                                |
| **Version specificity**                   | Evaluation, approval, and risk conclusions must identify the exact model/version/configuration to which they apply.                                                                                          |
| **System context**                        | A model card describes the model in context but does not replace system-level governance records.                                                                                                            |
| **Material change**                       | Update the card and trigger reassessment when model/provider/version, data, features, thresholds, intended purpose, affected population, integration, autonomy, or operating environment materially changes. |
| **Evidence traceability**                 | Material statements should link to evidence IDs, test reports, architecture records, approvals, or controlled companion documents.                                                                           |

## 2. Model Card Summary

| **Field**                         | **Entry**                                                                           | **Evidence / reference**          |
|-----------------------------------|-------------------------------------------------------------------------------------|-----------------------------------|
| **AI system ID**                  | \[Complete: e.g., AI-005\]                                                          | \[Document / link / evidence ID\] |
| **AI system name**                | \[Complete: governed AI system name\]                                               | \[Document / link / evidence ID\] |
| **Model/component ID**            | \[Complete: unique immutable internal ID\]                                          | \[Document / link / evidence ID\] |
| **Model name**                    | \[Complete: official internal/vendor model name\]                                   | \[Document / link / evidence ID\] |
| **Model family / algorithm type** | \[Complete: e.g., rules, classical ML, vision model, LLM, ranker, hybrid\]          | \[Document / link / evidence ID\] |
| **Model version / release**       | \[Complete: exact version or release identifier\]                                   | \[Document / link / evidence ID\] |
| **Provider / developer**          | \[Complete: internal team or third party\]                                          | \[Document / link / evidence ID\] |
| **Business owner**                | \[Complete: accountable first-line owner\]                                          | \[Document / link / evidence ID\] |
| **Technical / model owner**       | \[Complete: technical accountable owner\]                                           | \[Document / link / evidence ID\] |
| **Lifecycle status**              | \[Complete: concept / pilot / restricted pilot / production / suspended / retired\] | \[Document / link / evidence ID\] |
| **Environment**                   | \[Complete: development / test / production\]                                       | \[Document / link / evidence ID\] |
| **Last validated**                | \[Complete: date and validation report\]                                            | \[Document / link / evidence ID\] |
| **Next review**                   | \[Complete: date or trigger-based review\]                                          | \[Document / link / evidence ID\] |
| **Card status**                   | \[Complete: draft / validated / approved / superseded\]                             | \[Document / link / evidence ID\] |

## 3. Intended Purpose and Decision Boundary

| **Field**                             | **Entry**                                                                                  | **Evidence / reference**          |
|---------------------------------------|--------------------------------------------------------------------------------------------|-----------------------------------|
| **Business problem / opportunity**    | \[Complete: why the model is used\]                                                        | \[Document / link / evidence ID\] |
| **Intended purpose**                  | \[Complete: specific supported function\]                                                  | \[Document / link / evidence ID\] |
| **Intended users**                    | \[Complete: authorized user groups\]                                                       | \[Document / link / evidence ID\] |
| **Affected persons / groups**         | \[Complete: people or groups potentially affected\]                                        | \[Document / link / evidence ID\] |
| **Decision role**                     | \[Complete: information / recommendation / ranking / detection / generation / automation\] | \[Document / link / evidence ID\] |
| **Human accountability**              | \[Complete: who makes consequential decisions and can override/stop\]                      | \[Document / link / evidence ID\] |
| **Geographic / organizational scope** | \[Complete: countries, functions, business units\]                                         | \[Document / link / evidence ID\] |
| **Out-of-scope use**                  | \[Complete: uses not validated or approved\]                                               | \[Document / link / evidence ID\] |

### 3.1 Permitted, unsupported, and prohibited use

| **Permitted / intended** | **Unsupported / not validated** | **Prohibited by current Duckworks design** |
|--------------------------|---------------------------------|--------------------------------------------|
| **\[Complete\]**         | \[Complete\]                    | \[Complete\]                               |
| **\[Complete\]**         | \[Complete\]                    | \[Complete\]                               |
| **\[Complete\]**         | \[Complete\]                    | \[Complete\]                               |

## 4. Model Context and Architecture

Keep this concise. Link to the full architecture/data-flow record rather than reproducing technical diagrams in the card.

| **Field**                    | **Entry**                                                                           | **Evidence / reference**          |
|------------------------------|-------------------------------------------------------------------------------------|-----------------------------------|
| **Model function in system** | \[Complete: what component does\]                                                   | \[Document / link / evidence ID\] |
| **Inputs**                   | \[Complete: data/features/prompts/images/documents/signals\]                        | \[Document / link / evidence ID\] |
| **Outputs**                  | \[Complete: scores, classes, summaries, recommendations, generated content\]        | \[Document / link / evidence ID\] |
| **Pre-processing**           | \[Complete: material transformations\]                                              | \[Document / link / evidence ID\] |
| **Post-processing**          | \[Complete: thresholds, ranking logic, filters, business rules\]                    | \[Document / link / evidence ID\] |
| **Key integrations**         | \[Complete: APIs, RAG stores, ATS/ERP/CAD/SaaS, downstream systems\]                | \[Document / link / evidence ID\] |
| **Hosting / execution**      | \[Complete: cloud/on-prem/vendor service/device\]                                   | \[Document / link / evidence ID\] |
| **Material dependencies**    | \[Complete: libraries, foundation models, embeddings, datasets, external services\] | \[Document / link / evidence ID\] |
| **Architecture reference**   | \[Complete: controlled architecture/data-flow document ID\]                         | \[Document / link / evidence ID\] |

## 5. Data Documentation Summary

| **Data area**                                | **Model card summary**                 | **Evidence / detailed record**                           |
|----------------------------------------------|----------------------------------------|----------------------------------------------------------|
| **Training data**                            | \[Complete or N/A\]                    | \[Dataset card / vendor evidence / N/A rationale\]       |
| **Validation data**                          | \[Complete or N/A\]                    | \[Dataset / validation report\]                          |
| **Test / benchmark data**                    | \[Complete\]                           | \[Test dataset / benchmark record\]                      |
| **Operational input data**                   | \[Complete\]                           | \[Data dictionary / inventory / DPIA\]                   |
| **Derived / generated data**                 | \[Complete\]                           | \[Output schema / log schema\]                           |
| **Sensitive / personal / confidential data** | \[Complete restrictions and controls\] | \[DPIA / data classification / access-control evidence\] |
| **Data provenance / rights**                 | \[Complete\]                           | \[Licensing / source / contractual evidence\]            |
| **Representativeness / known gaps**          | \[Complete\]                           | \[Data quality / sampling analysis\]                     |
| **Retention / deletion**                     | \[Complete or reference policy\]       | \[Retention schedule / vendor terms\]                    |

## 6. Development and Configuration

| **Field**                         | **Entry**                                                                 | **Evidence / reference**          |
|-----------------------------------|---------------------------------------------------------------------------|-----------------------------------|
| **Build / buy / adapt**           | \[Complete: internal build, vendor service, adapted/open-source, hybrid\] | \[Document / link / evidence ID\] |
| **General model logic**           | \[Complete: high-level explanation of how inputs become outputs\]         | \[Document / link / evidence ID\] |
| **Optimization objective**        | \[Complete: technical/business objective\]                                | \[Document / link / evidence ID\] |
| **Features / criteria**           | \[Complete: material features, prompts, criteria, embeddings, signals\]   | \[Document / link / evidence ID\] |
| **Thresholds / weights**          | \[Complete: material decision thresholds or ranking weights\]             | \[Document / link / evidence ID\] |
| **Fine-tuning / adaptation**      | \[Complete: methods and datasets, if applicable\]                         | \[Document / link / evidence ID\] |
| **Safety / policy configuration** | \[Complete: filters, system prompts, content constraints, guardrails\]    | \[Document / link / evidence ID\] |
| **Material parameters**           | \[Complete: parameters/configuration affecting behavior\]                 | \[Document / link / evidence ID\] |
| **Development assumptions**       | \[Complete: assumptions that affect validity\]                            | \[Document / link / evidence ID\] |
| **Known design trade-offs**       | \[Complete: accuracy/latency/explainability/cost/recall/precision etc.\]  | \[Document / link / evidence ID\] |

## 7. Evaluation and Validation Results

Do not enter target values as if they were achieved results. Distinguish baseline, acceptance threshold, observed result, and evidence status.

| **Evaluation area**                                  | **Metric / method**          | **Acceptance criterion** | **Observed result** | **Evidence / status** |
|------------------------------------------------------|------------------------------|--------------------------|---------------------|-----------------------|
| **Task performance**                                 | \[Complete\]                 | \[Approved threshold\]   | \[Result / TBD\]    | \[Report ID\]         |
| **Reliability / robustness**                         | \[Complete\]                 | \[Approved threshold\]   | \[Result / TBD\]    | \[Report ID\]         |
| **Fairness / differential performance**              | \[Complete / N/A rationale\] | \[Approved threshold\]   | \[Result / TBD\]    | \[Report ID\]         |
| **Accessibility / inclusion**                        | \[Complete / N/A rationale\] | \[Approved criterion\]   | \[Result / TBD\]    | \[Report ID\]         |
| **Explainability / interpretability**                | \[Complete\]                 | \[Approved criterion\]   | \[Result / TBD\]    | \[Report ID\]         |
| **Human factors / oversight effectiveness**          | \[Complete\]                 | \[Approved criterion\]   | \[Result / TBD\]    | \[Report ID\]         |
| **Privacy**                                          | \[Complete\]                 | \[Approved criterion\]   | \[Result / TBD\]    | \[DPIA / test\]       |
| **Security / adversarial testing**                   | \[Complete\]                 | \[Approved criterion\]   | \[Result / TBD\]    | \[Security report\]   |
| **Latency / availability / operational performance** | \[Complete if material\]     | \[Approved threshold\]   | \[Result / TBD\]    | \[Test evidence\]     |

## 8. Capabilities, Limitations, and Failure Modes

| **Area**                         | **Documented statement**                                                                  | **User / operator implication**    |
|----------------------------------|-------------------------------------------------------------------------------------------|------------------------------------|
| **Validated capabilities**       | \[What the model is demonstrated to do under tested conditions\]                          | \[How users may rely on it\]       |
| **Known limitations**            | \[Accuracy, context, population, language, environment, data, or reasoning limits\]       | \[Restrictions / review required\] |
| **Out-of-distribution behavior** | \[Known or unknown behavior outside validated conditions\]                                | \[Fallback / stop-use rule\]       |
| **Uncertainty**                  | \[How confidence/uncertainty is represented, if at all\]                                  | \[How users should interpret it\]  |
| **Known failure modes**          | \[False positives/negatives, hallucination, extraction error, ranking instability, etc.\] | \[Detection / escalation\]         |
| **Foreseeable misuse**           | \[Misuse scenarios\]                                                                      | \[Prevention / monitoring\]        |

## 9. Fairness, Explainability, and Human Oversight

| **Field**                                     | **Entry**                                                                         | **Evidence / reference**          |
|-----------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------|
| **Fairness relevance**                        | \[Complete: affected groups, fairness risks, or N/A rationale\]                   | \[Document / link / evidence ID\] |
| **Fairness evaluation**                       | \[Complete: methods, metrics, populations, limitations\]                          | \[Document / link / evidence ID\] |
| **Proxy / sensitive feature controls**        | \[Complete: how direct and indirect sensitive signals are governed\]              | \[Document / link / evidence ID\] |
| **Explanation available to users**            | \[Complete: what explanation accompanies outputs\]                                | \[Document / link / evidence ID\] |
| **Explanation available to affected persons** | \[Complete: where applicable\]                                                    | \[Document / link / evidence ID\] |
| **Human review point**                        | \[Complete: where a person reviews before consequential action\]                  | \[Document / link / evidence ID\] |
| **Override authority**                        | \[Complete: who may disregard or reverse output\]                                 | \[Document / link / evidence ID\] |
| **Stop / suspend authority**                  | \[Complete: who can stop use\]                                                    | \[Document / link / evidence ID\] |
| **Automation-bias safeguards**                | \[Complete: training, interface design, review requirements, independent checks\] | \[Document / link / evidence ID\] |
| **Contestability / correction**               | \[Complete: mechanism to challenge or correct outcome where applicable\]          | \[Document / link / evidence ID\] |

## 10. Privacy, Security, Safety, and Third-Party Controls

| **Control domain**            | **Model-specific summary**                                                        | **Evidence / companion record**           |
|-------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------|
| **Privacy & personal data**   | \[Complete / N/A\]                                                                | \[DPIA / privacy review\]                 |
| **Confidentiality / IP**      | \[Complete\]                                                                      | \[Data handling / DLP / access evidence\] |
| **Access control**            | \[Complete\]                                                                      | \[IAM / authorization test\]              |
| **AI-specific security**      | \[Prompt injection, poisoning, adversarial input, model abuse, extraction, etc.\] | \[Threat model / security test\]          |
| **Secure integration**        | \[API, connector, tool/agent permissions\]                                        | \[Architecture / security review\]        |
| **Product / physical safety** | \[Complete / N/A rationale\]                                                      | \[Safety / quality evidence\]             |
| **Third-party provider**      | \[Provider dependency and contractual controls\]                                  | \[Due diligence / contract / SLA\]        |
| **Supply-chain provenance**   | \[Model/library/dataset provenance\]                                              | \[SBOM/ML-BOM/vendor evidence if used\]   |

## 11. Deployment and Operational Requirements

| **Field**                    | **Entry**                                                              | **Evidence / reference**          |
|------------------------------|------------------------------------------------------------------------|-----------------------------------|
| **Approved environment**     | \[Complete: where this version may operate\]                           | \[Document / link / evidence ID\] |
| **User access restrictions** | \[Complete: roles and permissions\]                                    | \[Document / link / evidence ID\] |
| **Required human review**    | \[Complete: mandatory review steps\]                                   | \[Document / link / evidence ID\] |
| **Fallback / safe state**    | \[Complete: what happens if model unavailable or unreliable\]          | \[Document / link / evidence ID\] |
| **Logging requirements**     | \[Complete: inputs/outputs/overrides/decisions/errors as appropriate\] | \[Document / link / evidence ID\] |
| **User instructions**        | \[Complete: training and usage guidance\]                              | \[Document / link / evidence ID\] |
| **Known dependencies**       | \[Complete: services/infrastructure/data required\]                    | \[Document / link / evidence ID\] |
| **Release gate**             | \[Complete: approval authority and current decision\]                  | \[Document / link / evidence ID\] |

## 12. Monitoring and Reassessment

| **Monitoring area**                       | **Indicator / metric**      | **Threshold / trigger** | **Owner** | **Evidence location**    |
|-------------------------------------------|-----------------------------|-------------------------|-----------|--------------------------|
| **Performance / drift**                   | \[Complete\]                | \[Approved trigger\]    | \[Role\]  | \[Dashboard/log\]        |
| **Fairness / impact**                     | \[Complete where relevant\] | \[Approved trigger\]    | \[Role\]  | \[Report\]               |
| **Human override / reliance**             | \[Complete where relevant\] | \[Approved trigger\]    | \[Role\]  | \[Logs\]                 |
| **Complaints / challenges / corrections** | \[Complete\]                | \[Approved trigger\]    | \[Role\]  | \[Case log\]             |
| **Security / privacy events**             | \[Complete\]                | \[Incident trigger\]    | \[Role\]  | \[SIEM/incident log\]    |
| **Vendor / model change**                 | \[Complete\]                | \[Material change\]     | \[Role\]  | \[Vendor/change record\] |
| **Business value**                        | \[Complete\]                | \[Review trigger\]      | \[Role\]  | \[Business KPI\]         |

### 12.1 Mandatory reassessment triggers

- Change in intended purpose, autonomy, or decision authority.

- New model/provider/version or substantial configuration change.

- New data source, feature, prompt logic, criterion, connector, permission, or retrieval source.

- Expansion to new users, affected groups, countries, languages, product lines, or operating conditions.

- Material incident, near miss, complaint, security event, discriminatory outcome, or rights challenge.

- Drift, performance threshold breach, change in error distribution, or material control failure.

- Vendor terms, data-use, training, hosting, subprocessor, or service change that invalidates prior evidence.

- New or amended legal/regulatory requirement or internal policy requirement.

## 13. Model Version and Change History

| **Version**     | **Date** | **Change summary** | **Reason**   | **Validation impact**                 | **Approval / status** |
|-----------------|----------|--------------------|--------------|---------------------------------------|-----------------------|
| **\[Version\]** | \[Date\] | \[Complete\]       | \[Complete\] | \[Full / partial / none + rationale\] | \[Approver / status\] |
|                 |          |                    |              |                                       |                       |
|                 |          |                    |              |                                       |                       |

## 14. Governance, Legal, and Framework Classification

Keep legal classification separate from Duckworks internal risk rating. Model-card completion does not establish legal compliance or certification.

| **Classification area**                  | **Current conclusion**                                  | **Basis / owner**                      |
|------------------------------------------|---------------------------------------------------------|----------------------------------------|
| **Duckworks internal risk rating**       | \[Low / Moderate / High / Critical / Not yet assessed\] | \[AI Risk Assessment ID\]              |
| **EU AI Act screening**                  | \[Classification / applicability status / TBD\]         | \[Legal review / inventory\]           |
| **GDPR / DPIA relevance**                | \[Required / completed / N/A / TBD\]                    | \[DPO / DPIA ID\]                      |
| **Fundamental-rights assessment**        | \[FRIA / HUDERIA / AIA status where relevant\]          | \[Assessment ID\]                      |
| **Product / safety / sector regulation** | \[Applicable / possible / N/A / TBD\]                   | \[Legal / product safety review\]      |
| **ISO / NIST mapping**                   | \[Voluntary guidance / internal adoption status\]       | \[Control framework / reference file\] |

## 15. Evidence and Companion Records

| **Record / evidence**                     | **Reference / ID** | **Status**                    |
|-------------------------------------------|--------------------|-------------------------------|
| **AI Business Use Case**                  | \[ID\]             | \[Available / Missing / N/A\] |
| **AI System Inventory record**            | \[ID\]             | \[Available / Missing\]       |
| **Full Model Documentation Record**       | \[ID\]             | \[Available / Missing / N/A\] |
| **Architecture / data-flow diagram**      | \[ID\]             | \[Available / Missing\]       |
| **Dataset documentation / dataset cards** | \[ID\]             | \[Available / Missing / N/A\] |
| **Validation / evaluation report**        | \[ID\]             | \[Available / Missing\]       |
| **AI / Algorithmic Impact Assessment**    | \[ID\]             | \[Available / Missing / N/A\] |
| **DPIA**                                  | \[ID\]             | \[Available / Missing / N/A\] |
| **FRIA / HUDERIA**                        | \[ID\]             | \[Available / Missing / N/A\] |
| **AI Risk Assessment**                    | \[ID\]             | \[Available / Missing\]       |
| **Security threat model / testing**       | \[ID\]             | \[Available / Missing / N/A\] |
| **Third-party due diligence**             | \[ID\]             | \[Available / Missing / N/A\] |
| **Human oversight procedure**             | \[ID\]             | \[Available / Missing / N/A\] |
| **Monitoring plan / dashboard**           | \[ID\]             | \[Available / Missing\]       |
| **Approval / exception record**           | \[ID\]             | \[Available / Missing\]       |

## 16. Approval and Publication Record

| **Role**                                                   | **Name / function** | **Decision / status**                        | **Date** | **Comments / conditions** |
|------------------------------------------------------------|---------------------|----------------------------------------------|----------|---------------------------|
| **Business Owner**                                         | \[Complete\]        | \[Approve / Reject / Conditional\]           | \[Date\] | \[Complete\]              |
| **Technical / Model Owner**                                | \[Complete\]        | \[Validated / Not validated\]                | \[Date\] | \[Complete\]              |
| **AI Governance Lead**                                     | \[Complete\]        | \[Governance complete / incomplete\]         | \[Date\] | \[Complete\]              |
| **Security / Privacy / Legal / HR / Safety specialist(s)** | \[As applicable\]   | \[Reviewed / conditions\]                    | \[Date\] | \[Complete\]              |
| **AI Governance Committee / delegated approver**           | \[Complete\]        | \[Approve / Reject / Conditional / Suspend\] | \[Date\] | \[Complete\]              |

**Publication rule.** A model card may be shared internally or externally only at the level approved by the information owner. Confidential architecture, personal data, security-sensitive details, proprietary vendor material, or legally privileged analysis should not be exposed merely to make the card appear complete.

## 17. Source Basis and Template Boundary

This template is derived from the existing Duckworks governance architecture and model documentation record. It is a Duckworks organizational practice designed to support concise, repeatable, audit-ready model transparency.

| **Source category**                                                      | **How the template uses it**                                                                                                                       |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Duckworks Business Scenario / Objectives**                             | Purpose, ownership, proportionality, evidence, monitoring and lifecycle governance.                                                                |
| **Duckworks AI Risk Methodology**                                        | Internal risk separation, evidence discipline, approval, monitoring and reassessment.                                                              |
| **Duckworks Model Documentation Record**                                 | Model identity, architecture, data, evaluation, limitations, oversight, monitoring, change control and evidence fields.                            |
| **Duckworks AIA / DPIA / FRIA / HUDERIA**                                | Companion impact, privacy and rights analysis rather than duplication inside the model card.                                                       |
| **NIST AI RMF / ISO public references already maintained by Duckworks**  | Voluntary governance and lifecycle guidance; not proof of legal compliance or certification.                                                       |
| **EU AI Act / GDPR screening maintained by Duckworks Legal and Privacy** | Conditional legal applicability is documented separately; the model card records references and status but does not substitute for legal analysis. |

Portfolio disclaimer: Duckworks, Project W.I.N.G., all personnel, systems, models, datasets, decisions, metrics, controls, and evidence in this template are fictional or placeholders. The template is for educational and professional portfolio purposes and does not constitute legal advice, certification evidence, a conformity assessment, or a regulatory filing.
