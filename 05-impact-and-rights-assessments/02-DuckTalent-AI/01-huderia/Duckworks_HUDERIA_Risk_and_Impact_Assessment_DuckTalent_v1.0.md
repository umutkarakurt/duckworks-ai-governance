# Duckworks HUDERIA Risk & Impact Assessment — DuckTalent AI (AI-005)

**Human rights, democracy and rule-of-law assessment - DuckTalent AI (AI-005)**

| **Document ID**    | DW-WING-HUD-04                         |
|--------------------|----------------------------------------|
| **Version / date** | 1.0 / 9 August 2026                    |
| **Status**         | Portfolio Draft                        |
| **Classification** | Portfolio / Synthetic / Non-production |

**Portfolio disclaimer.** Duckworks, Project W.I.N.G., all personnel, AI systems, datasets, decisions, stakeholder inputs and evidence are fictional or synthetic. This document is an internal portfolio artifact, not legal advice, certification evidence, or a statement of regulatory conformity.

## 1. Assessment Purpose

This assessment builds on the COBRA triage and the planned SEP. It asks how identified adverse impacts could occur and evaluates each impact using HUDERIA variables: scale, scope, reversibility and probability. It also records potential positive impacts. The assessment does not substitute for the GDPR DPIA, EU AI Act legal classification, statistical fairness validation, security assessment or Duckworks 5x5 enterprise risk assessment.

## 2. Assessment Scale

| **Variable**  | **Qualitative anchors used by Duckworks for this HUDERIA record**                                                                                                                               |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scale         | Limited - modest effect; Major - substantial effect on rights/opportunity; Severe - grave or systemic harm.                                                                                     |
| Scope         | Individual - isolated; Subset - identifiable group; Broad - repeated across many applicants/recruitment rounds; Systemic - organization-wide or wider structural effect.                        |
| Reversibility | Ready - corrected within process; Moderate - meaningful effort/time required; Difficult - opportunity may be lost or effects persist; Irreversible - restoration is not realistically possible. |
| Probability   | Unlikely - credible but uncommon; Possible - foreseeable; Likely - expected without effective controls; Observed - evidenced in operation.                                                      |

These anchors are Duckworks adaptations. HUDERIA permits qualitative, quantitative or mixed calibration and does not mandate these labels.

## 3. Detailed Adverse Impact Assessment

| **ID** | **Concern**                     | **How impact could occur**                                                                                                    | **Affected**                                      | **Scale**       | **Scope**                    | **Reversibility**            | **Probability**         | **Priority** |
|--------|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|-----------------|------------------------------|------------------------------|-------------------------|--------------|
| H-01   | Equality / employment           | Historical or proxy features systematically disadvantage a protected or vulnerable group in ranking.                          | Applicants, especially affected groups            | Severe          | Broad                        | Difficult                    | Possible                | Blocking     |
| H-02   | Employment / dignity            | Parsing or matching errors understate qualifications and deprioritize a suitable applicant.                                   | Applicants                                        | Major           | Broad if systematic          | Difficult after cycle closes | Possible                | High         |
| H-03   | Equality / linguistic diversity | Foreign credentials, non-native language, names or non-standard terminology are interpreted less accurately.                  | International / linguistically diverse applicants | Major           | Subset to broad              | Difficult                    | Possible                | High         |
| H-04   | Accessibility / equality        | Accessible formats, disability-related career patterns or accommodations are mishandled, excluding candidates.                | Applicants with disabilities                      | Severe          | Subset but recurring         | Difficult                    | Possible                | Blocking     |
| H-05   | Privacy / autonomy              | System processes or infers sensitive, private or unrelated characteristics beyond recruitment necessity.                      | Applicants                                        | Severe          | Broad                        | Difficult                    | Possible                | Blocking     |
| H-06   | Human dignity / oversight       | Recruiters mechanically follow rankings; human review becomes nominal and individual circumstances are ignored.               | Applicants; recruiters                            | Severe          | Broad                        | Difficult                    | Likely without controls | Blocking     |
| H-07   | Transparency / remedy           | Applicant cannot understand AI involvement, correct material data, challenge an error or obtain meaningful reconsideration.   | Applicants                                        | Major           | Broad                        | Moderate to difficult        | Likely without process  | High         |
| H-08   | Security / privacy              | Vendor, integration or access-control failure exposes applicant data or corrupts ranking logic.                               | Applicants; Duckworks                             | Severe          | Broad                        | Difficult                    | Possible                | Blocking     |
| H-09   | Dignity / autonomy              | Opaque scoring or inappropriate personality/emotion inference objectifies applicants or bases decisions on irrelevant traits. | Applicants                                        | Major to Severe | Broad                        | Difficult                    | Possible                | Blocking     |
| H-10   | Cumulative / scale effect       | A faulty rule/model version is reused across many vacancies before detection, entrenching unequal outcomes.                   | Current and future applicants                     | Severe          | Broad / potentially systemic | Difficult                    | Possible                | Blocking     |

## 4. Positive Impact Assessment

| **Potential positive impact** | **Mechanism**                                                                      | **Beneficiary**         | **Evidence status**    | **Rights caveat**                                                                          |
|-------------------------------|------------------------------------------------------------------------------------|-------------------------|------------------------|--------------------------------------------------------------------------------------------|
| Greater recruiter capacity    | Automated extraction/summarization may reduce repetitive triage.                   | Recruiters / applicants | Unvalidated hypothesis | Time savings are not beneficial if faster processing scales unfair or inaccurate outcomes. |
| More structured review        | Pre-approved criteria may reduce some reviewer inconsistency.                      | Applicants / HR         | Conditional            | Only if criteria are job-related, fair, explainable and validated.                         |
| Better audit trail            | Structured outputs and decision logging can support review.                        | Applicants / governance | Potential              | Logging must not become excessive surveillance or unnecessary personal-data retention.     |
| Accessible alternatives       | If deliberately designed, AI-enabled tools may support multiple formats/languages. | Some applicants         | Unvalidated            | Must be tested; AI can also create new accessibility and language disparities.             |

## 5. Democracy and Rule-of-Law Analysis

| **Dimension**      | **Current conclusion**                                                                                                                                                                                       | **Reassessment trigger**                                                                                                           |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Democracy          | No material direct effect identified under the current private recruitment purpose.                                                                                                                          | Use in public-office/civil-service selection, political participation, large-scale public employment, or other democratic process. |
| Rule-of-law values | Relevant through transparency, accountability, procedural fairness and effective challenge/remedy. This is a governance lens, not a claim that every cited human-rights instrument directly binds Duckworks. | Inability to explain, correct, challenge or review material AI-supported outcomes; legal/regulatory changes.                       |

## 6. Evidence Confidence

| **Evidence area**                    | **Confidence**  | **Reason**                                                                                          |
|--------------------------------------|-----------------|-----------------------------------------------------------------------------------------------------|
| Intended purpose / decision boundary | High            | Documented consistently across Duckworks use case, AIA, DPIA and governance records.                |
| Actual model performance             | Low             | Provider/model and production validation are not confirmed.                                         |
| Fairness / differential error        | Low             | No real fairness validation or lawful protected-group evidence exists.                              |
| Accessibility                        | Low             | No completed accessibility/user evidence.                                                           |
| Human oversight operation            | Low             | Design requirement exists, but no real recruiter operating evidence.                                |
| Privacy/legal analysis               | Moderate        | DPIA/FRIA identify issues, but exact lawful basis, jurisdiction and provider facts remain open.     |
| Security/vendor                      | Low to Moderate | Governance requirements exist; DuckTalent-specific architecture and vendor evidence are incomplete. |
| Affected-person perspectives         | Low             | SEP has not been conducted with real stakeholders.                                                  |

## 7. Overall Assessment Outcome

| **Outcome.** The combination of severe potential scale, broad scope, difficult reversibility, consequential decision proximity, and low evidence confidence makes unrestricted deployment indefensible at present. The RIA supports the existing DO NOT DEPLOY gate and requires a mitigation plan with blocking controls and remedy mechanisms. |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Source Basis

- Council of Europe, HUDERIA - Methodology and Model (2026), approved Methodology 26 February 2025 and Model: COBRA 25 February 2026; official consolidated publication dated April 2026.

- Council of Europe official HUDERIA webpage and Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law webpage.

- Duckworks controlled project artifacts: Business Scenario; Business Use Case Portfolio; Stakeholder Register; Assumptions Register; AI Risk Classification & Assessment Methodology; AI RACI; AI Governance Lifecycle SOP; Algorithmic Impact Assessment; EU FRIA; GDPR DPIA; Acceptance Criteria.

**Official HUDERIA publication:** https://rm.coe.int/prems-002726-gbr-2006-huderia-texte-web-a4/48802ba7b1

**Official HUDERIA page:** https://www.coe.int/en/web/artificial-intelligence/huderia-risk-and-impact-assessment-of-ai-systems
