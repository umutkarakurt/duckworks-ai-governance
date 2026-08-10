# Duckworks HUDERIA Applicability & Portfolio Triage

**Initial proportionality decision across the seven Duckworks AI entries**

| **Document ID**    | DW-WING-HUD-01                         |
|--------------------|----------------------------------------|
| **Version / date** | 1.0 / 9 August 2026                    |
| **Status**         | Portfolio Draft                        |
| **Classification** | Portfolio / Synthetic / Non-production |

**Portfolio disclaimer.** Duckworks, Project W.I.N.G., all personnel, AI systems, datasets, decisions, stakeholder inputs and evidence are fictional or synthetic. This document is an internal portfolio artifact, not legal advice, certification evidence, or a statement of regulatory conformity.

## 1. Purpose and Method

This is a Duckworks internal triage record informed by the HUDERIA COBRA approach. HUDERIA does not prescribe a mandatory scoring formula or fixed risk tiers; the descriptors below are Duckworks governance labels used only to decide the depth of subsequent HUDERIA activity.

| **Triage principle.** A system with limited or unlikely human-rights impact may stop after COBRA, while a system with significant potential impacts should proceed to stakeholder engagement, detailed risk and impact assessment, mitigation planning, and iterative review. A system judged incompatible with respect for human rights, democracy or the rule of law should not proceed merely because its business value is high. |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## 2. Triage Descriptors

| **Descriptor** | **Duckworks interpretation**                                                                                                                                                                           |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Limited        | No material direct impact identified under the current intended purpose; monitor for material change.                                                                                                  |
| Material       | Plausible rights impact requiring targeted controls and potentially a focused RIA.                                                                                                                     |
| Significant    | High-impact function, safety/rights implications, broad scope, or consequential decision proximity; detailed HUDERIA activities expected.                                                              |
| Severe         | Potentially grave or systemic impact, difficult reversibility, vulnerable groups, high decision proximity, or evidence gaps incompatible with deployment; full HUDERIA and blocking governance action. |

## 3. Portfolio Triage

| **ID** | **System**               | **HUDERIA triage**                      | **Affected parties**                                   | **Primary HR/DR/Rule-of-law concern**                                                                                                | **Required next step**                                                                                         |
|--------|--------------------------|-----------------------------------------|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| AI-001 | DuckDesign AI            | Significant                             | Product users; engineers                               | Physical integrity/dignity if unsafe design recommendations influence product outcomes; IP/privacy secondary.                        | Focused full HUDERIA before production design reliance; retain competent engineer validation.                  |
| AI-002 | QuackBot                 | Material / Significant                  | Customers; product users                               | Privacy, access to accurate information, dignity/autonomy, accessibility; safety relevance where troubleshooting is relied upon.     | COBRA + targeted SEP/RIA before external production; escalate to full assessment for safety-relevant guidance. |
| AI-003 | FeatherForecast          | Limited / Material                      | Supply-chain staff; suppliers                          | Primarily operational/financial; indirect labour and supplier impacts possible if decision automation or workforce effects increase. | COBRA sufficient at current boundary; full RIA only on material change.                                        |
| AI-004 | WingInspect Vision       | Significant                             | Product users; inspectors                              | Physical integrity and safety if false negatives permit defective products; operator autonomy and accountability.                    | Focused full HUDERIA before safety-critical reliance; human inspector remains final authority.                 |
| AI-005 | DuckTalent AI            | Severe                                  | Applicants; internal candidates; recruiters            | Labour/employment, equality/non-discrimination, privacy/data protection, dignity, accessibility, effective challenge/remedy.         | Full HUDERIA now. Current gate remains DO NOT DEPLOY.                                                          |
| AI-006 | PondGPT                  | Material                                | Employees; internal stakeholders                       | Employee privacy, confidentiality, autonomy, accessibility, information quality; higher impact if used in HR/performance decisions.  | COBRA + targeted RIA before broad production; re-triage if used for consequential people decisions.            |
| AI-007 | Unregistered GenAI Usage | Cannot be validly triaged as one system | Employees; customers; applicants; other unknown groups | Unknown purposes, providers, data, decision roles and affected persons prevent a defensible HUDERIA analysis.                        | Discover, contain and decompose into individual use cases; perform COBRA on each material use.                 |

## 4. Triage Rationale for DuckTalent

- The system substantially informs access to employment and therefore sits close to a consequential decision pathway.

- Applicants may include groups exposed to historical or structural disadvantage, creating material equality and non-discrimination concerns.

- The system processes personal information and may infer or use proxies that affect privacy, dignity, and fairness.

- Errors can be repeated at scale across multiple recruitment rounds, making scope and cumulative effects important.

- A rejected or deprioritized opportunity may be difficult to fully restore after recruitment has closed, increasing reversibility concerns.

- Existing fairness, accessibility, vendor/model, and human-oversight operating evidence remains incomplete.

## 5. Triage Decision

| **Decision.** AI-005 DuckTalent proceeds to the complete Duckworks HUDERIA sequence. AI-001 and AI-004 require focused full assessments before production/safety-critical reliance. AI-002 and AI-006 require targeted assessments at their release gates. AI-003 remains on COBRA-level monitoring. AI-007 must first be decomposed. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Source Basis

- Council of Europe, HUDERIA - Methodology and Model (2026), approved Methodology 26 February 2025 and Model: COBRA 25 February 2026; official consolidated publication dated April 2026.

- Council of Europe official HUDERIA webpage and Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law webpage.

- Duckworks controlled project artifacts: Business Scenario; Business Use Case Portfolio; Stakeholder Register; Assumptions Register; AI Risk Classification & Assessment Methodology; AI RACI; AI Governance Lifecycle SOP; Algorithmic Impact Assessment; EU FRIA; GDPR DPIA; Acceptance Criteria.

**Official HUDERIA publication:** https://rm.coe.int/prems-002726-gbr-2006-huderia-texte-web-a4/48802ba7b1

**Official HUDERIA page:** https://www.coe.int/en/web/artificial-intelligence/huderia-risk-and-impact-assessment-of-ai-systems
