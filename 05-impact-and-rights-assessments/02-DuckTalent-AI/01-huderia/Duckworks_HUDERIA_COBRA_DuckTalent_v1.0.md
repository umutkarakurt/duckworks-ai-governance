# Duckworks HUDERIA COBRA Assessment — DuckTalent AI (AI-005)

**Context-Based Risk Analysis - DuckTalent AI (AI-005)**

| **Document ID**    | DW-WING-HUD-02                         |
|--------------------|----------------------------------------|
| **Version / date** | 1.0 / 9 August 2026                    |
| **Status**         | Portfolio Draft                        |
| **Classification** | Portfolio / Synthetic / Non-production |

**Portfolio disclaimer.** Duckworks, Project W.I.N.G., all personnel, AI systems, datasets, decisions, stakeholder inputs and evidence are fictional or synthetic. This document is an internal portfolio artifact, not legal advice, certification evidence, or a statement of regulatory conformity.

## 1. Assessment Scope

| **Field**                | **Current record**                                                                                                                                                                   |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System                   | AI-005 - DuckTalent AI                                                                                                                                                               |
| Business owner           | Beatrice Van Duck - Chief People Officer                                                                                                                                             |
| Technical owner          | Dr. Ada Duckfield - Head of Data & AI                                                                                                                                                |
| Assessment owner         | Eleanor Duckford - AI Governance Lead                                                                                                                                                |
| Lifecycle                | Concept / pre-deployment                                                                                                                                                             |
| Intended purpose         | Parse CVs, extract job-relevant qualifications/experience, compare against pre-approved criteria, summarize applications, rank candidates and recommend candidates for human review. |
| Decision boundary        | No autonomous hiring or rejection. Recruiters/hiring managers retain formal decision authority.                                                                                      |
| Primary affected persons | External applicants; internal candidates if scope later expands.                                                                                                                     |
| Current governance gate  | DO NOT DEPLOY with real applicants.                                                                                                                                                  |
| Key open assumptions     | Exact provider/model, geography, data flow, lawful basis, fairness method, accessibility evidence, human-oversight operating design.                                                 |

## 2. Preliminary Scoping

DuckTalent addresses a real business need: growing recruitment volume and repetitive application triage. The expected value is reduced manual review effort and more structured comparison against job criteria. These are benefit hypotheses; no validated productivity or ROI baseline exists in the current project evidence.

## 3. Application Context - COBRA Resource A

| **Resource area**                  | **Relevance** | **DuckTalent analysis**                                                                                                                                                                                                             |
|------------------------------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A.1 Sector / high-impact function  | High          | Recruitment is not a safety-critical sector, but the function materially influences access to employment. The Model itself uses recruitment as an example of a high-impact function outside a traditionally safety-critical sector. |
| A.2 Legal / regulatory environment | High          | Employment, equality, data protection and AI-specific requirements may apply. Existing DPIA/FRIA/legal triage are supporting records but do not replace HUDERIA.                                                                    |
| A.3 Deployment scope               | High          | A single ranking or parsing defect can affect repeated recruitment rounds. Actual annual applicant volume and jurisdictions are not validated.                                                                                      |
| A.4 Legacy bias / vulnerability    | High          | Historical recruitment patterns, proxy variables, non-standard career histories, disability, language and credential differences may create unequal effects. No finding of actual bias is asserted.                                 |
| A.5 Environmental context          | Low / open    | No material environmental impact has been evidenced for the current use case. Provider/model compute footprint is not known and should be considered if material.                                                                   |

## 4. Design and Development Context - COBRA Resource B

| **Resource area**                 | **Relevance** | **DuckTalent analysis**                                                                                                                                                                                             |
|-----------------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| B.1 Need and alternatives         | High          | Human-only review, rules-based ATS screening and process redesign are feasible alternatives. Duckworks has not yet demonstrated that AI delivers enough incremental benefit to justify the added rights risk.       |
| B.2 Technological maturity        | Open / High   | Exact model architecture and validation precedent are not confirmed. Deployment should not rely on maturity assumptions without evidence.                                                                           |
| B.3 Existing process              | High          | Current recruitment practices may already contain inconsistency or bias. DuckTalent must not encode or amplify these weaknesses.                                                                                    |
| B.4 Cybersecurity                 | High          | Applicant data and model/integration surfaces create confidentiality, manipulation, supply-chain and data-exfiltration risks.                                                                                       |
| B.5 Data quality / personal data  | High          | Representativeness, completeness, proxy effects, provenance, lawful processing and retention require validation. Sensitive or unrelated inference is prohibited by design unless specifically justified and lawful. |
| B.6 Model design / implementation | High          | Explainability, validation, error distribution, drift monitoring, feature governance, meaningful human oversight, performance communication and scope-creep controls are all material.                              |

## 5. Deployment Context - COBRA Resource C

| **Resource area**             | **Relevance** | **DuckTalent analysis**                                                                                                                                                |
|-------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C.1 Privacy / personal data   | High          | Real applicant data would require validated data-protection controls, transparency, minimisation, rights handling, retention and processor governance.                 |
| C.2 Non-discrimination / bias | High          | Deployment choices, job criteria, recruiter behavior and local population differences could amplify model or data bias.                                                |
| C.3 System operators          | Material      | Recruiters may experience workflow pressure or reduced professional autonomy if rankings become de facto directives.                                                   |
| C.4 Training                  | High          | Operators need training on limitations, uncertainty, prohibited uses, override, escalation and automation bias.                                                        |
| C.5 Human in the loop         | High          | Nominal human review is insufficient. Reviewers must have time, source evidence, competence and authority to disagree with the system.                                 |
| C.6 Out-of-scope use          | High          | Use for promotion, performance, termination, personality/emotion inference or autonomous rejection would materially change the risk profile and requires reassessment. |
| C.7 Decision proximity        | High          | DuckTalent substantially informs shortlist and candidate-priority decisions, creating high proximity to employment outcomes.                                           |

## 6. Potential Impact Mapping - COBRA Resources E and F

| **Area of concern**                      | **Relevance**                        | **Potential impact**                                                                                                                                                    |
|------------------------------------------|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Human dignity / autonomy                 | Relevant                             | Reduction of applicants to opaque rankings; dehumanized treatment; hidden inferences; inability to meaningfully participate.                                            |
| Privacy and data protection              | Core                                 | Processing, inference, retention, access, vendor reuse, confidentiality and correction of applicant data.                                                               |
| Equality and non-discrimination          | Core                                 | Direct/indirect discrimination, proxy bias, unequal error rates, language/credential effects, disability/accessibility.                                                 |
| Labour and employment                    | Core                                 | Access to work, fair treatment in recruitment, discrimination, human decision integrity.                                                                                |
| Opinions / expression / information      | Contextual                           | Application wording or inferred traits should not be used to penalize lawful expression or irrelevant personal characteristics.                                         |
| Effective challenge / rule-of-law values | Relevant                             | Transparency, accountability, ability to correct data, challenge material errors and obtain competent human reconsideration.                                            |
| Democracy                                | No direct material impact identified | Current private recruitment use does not directly influence democratic processes. Reassess if used for public office/civil-service or political participation contexts. |
| Children                                 | Open / low at present                | No child applicant population is assumed. Reassess if roles are opened to minors or young workers.                                                                      |

## 7. Initial Risk Variables

HUDERIA uses scale, scope, reversibility and probability. The following qualitative judgments are preliminary and must be revalidated with technical evidence and stakeholder input; they are not Duckworks 5x5 enterprise risk scores.

| **Potential impact**                   | **Scale** | **Scope**                        | **Reversibility**                   | **Probability**               | **COBRA outcome**                  |
|----------------------------------------|-----------|----------------------------------|-------------------------------------|-------------------------------|------------------------------------|
| Discriminatory ranking / proxy effects | Severe    | Broad                            | Difficult                           | Possible                      | Proceed to full RIA - blocking     |
| Inaccurate parsing or ranking          | Major     | Broad                            | Difficult after hiring cycle closes | Possible                      | Proceed to full RIA                |
| Privacy / sensitive inference          | Severe    | Broad                            | Difficult                           | Possible                      | Proceed to full RIA / DPIA linkage |
| Automation bias / illusory oversight   | Severe    | Broad                            | Difficult                           | Likely absent strong controls | Proceed to full RIA - blocking     |
| Opacity / weak contestability          | Major     | Broad                            | Moderate to difficult               | Likely absent process design  | Proceed to full RIA                |
| Accessibility / language disadvantage  | Major     | Subset but potentially recurring | Moderate to difficult               | Possible                      | Proceed to full RIA                |

## 8. Zero Questions

| **Zero-question theme**                                           | **Current answer**                                                                                            |
|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Is AI appropriate to the problem?                                 | Not yet demonstrated. A non-AI or rules-based process could address some triage needs with lower rights risk. |
| Will the system meet Duckworks needs?                             | Plausible but unvalidated. Business benefits require controlled pilot evidence.                               |
| Will impacts be equitable?                                        | Not established. Fairness, accessibility and error-distribution evidence is missing.                          |
| Are data quality and representativeness sufficient?               | Not established. Production data design and lawful testing approach are unresolved.                           |
| Are sufficient human/material resources available for governance? | Partially. Roles exist, but operating evidence, training and technical validation remain incomplete.          |
| Are misuse and scope-creep risks controlled?                      | Not yet. Restrictions are defined in policy, but implementation evidence is incomplete.                       |

## 9. COBRA Triage Decision

| **Decision.** Potential impacts are significant and potentially severe. Benefits are not yet evidenced to outweigh rights risks. DuckTalent must proceed to SEP, detailed RIA and Mitigation Plan, and the existing DO NOT DEPLOY gate remains in force. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Source Basis

- Council of Europe, HUDERIA - Methodology and Model (2026), approved Methodology 26 February 2025 and Model: COBRA 25 February 2026; official consolidated publication dated April 2026.

- Council of Europe official HUDERIA webpage and Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law webpage.

- Duckworks controlled project artifacts: Business Scenario; Business Use Case Portfolio; Stakeholder Register; Assumptions Register; AI Risk Classification & Assessment Methodology; AI RACI; AI Governance Lifecycle SOP; Algorithmic Impact Assessment; EU FRIA; GDPR DPIA; Acceptance Criteria.

**Official HUDERIA publication:** https://rm.coe.int/prems-002726-gbr-2006-huderia-texte-web-a4/48802ba7b1

**Official HUDERIA page:** https://www.coe.int/en/web/artificial-intelligence/huderia-risk-and-impact-assessment-of-ai-systems
