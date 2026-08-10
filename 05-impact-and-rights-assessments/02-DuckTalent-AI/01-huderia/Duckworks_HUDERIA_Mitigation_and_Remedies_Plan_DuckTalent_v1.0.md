# Duckworks HUDERIA Mitigation & Remedies Plan — DuckTalent AI (AI-005)

**Avoid - mitigate - restore - compensate \| DuckTalent AI (AI-005)**

| **Document ID**    | DW-WING-HUD-05                         |
|--------------------|----------------------------------------|
| **Version / date** | 1.0 / 9 August 2026                    |
| **Status**         | Portfolio Draft                        |
| **Classification** | Portfolio / Synthetic / Non-production |

**Portfolio disclaimer.** Duckworks, Project W.I.N.G., all personnel, AI systems, datasets, decisions, stakeholder inputs and evidence are fictional or synthetic. This document is an internal portfolio artifact, not legal advice, certification evidence, or a statement of regulatory conformity.

## 1. Purpose and Hierarchy

This plan translates the HUDERIA RIA findings into prevention, mitigation, restoration and remedy actions. Duckworks gives priority to avoiding adverse impact, then mitigating remaining risk. Restoration and compensation become relevant where adverse impacts have occurred. Compensation is not automatically available or appropriate; legal remedies depend on applicable law and case facts.

| **Hierarchy**  | **Duckworks use**                                                                                                                   |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------|
| 1 - Avoid      | Change or stop the design/use before harm occurs; remove unacceptable features, purposes or decision pathways.                      |
| 2 - Mitigate   | Reduce probability, scale, scope or persistence through technical, organizational, human and contractual controls.                  |
| 3 - Restore    | Correct the affected person’s situation where possible, e.g., correct data, reopen review, conduct human-only reassessment.         |
| 4 - Compensate | Consider only where legally and factually appropriate after other measures are insufficient; Legal determines the applicable route. |

## 2. Mitigation Action Register

| **ID** | **Impact**     | **Hierarchy**              | **Measure**                                                                                                                                            | **Owner**                                      | **Evidence**                                       | **Timing**             | **Status**      |
|--------|----------------|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------------------|------------------------|-----------------|
| MP-01  | H-01/H-10      | Avoid + Mitigate           | Pre-approve job-related criteria; prohibit protected/sensitive traits and unjustified proxies; validate feature effects; version-control criteria.     | HR + Data & AI                                 | Criteria register; feature list; validation report | Before pilot           | Blocking        |
| MP-02  | H-01/H-03/H-04 | Mitigate                   | Define lawful fairness and differential-error testing across relevant groups; establish thresholds and escalation before real use.                     | Data & AI + HR + Risk                          | Methodology; test report; issue log                | Before pilot           | Blocking        |
| MP-03  | H-02/H-03      | Mitigate + Restore         | Validate CV parsing/ranking accuracy; give recruiters source-document access; allow applicant correction; re-review materially affected applications.  | Data & AI + HR                                 | Validation; correction log; re-review record       | Before pilot / ongoing | Blocking        |
| MP-04  | H-04           | Avoid + Mitigate + Restore | Accessible application and challenge routes; test assistive technologies/formats; provide alternative human route and accommodation.                   | HR + Legal/Accessibility                       | Accessibility review; remediation evidence         | Before pilot           | Blocking        |
| MP-05  | H-05           | Avoid + Mitigate           | Complete/refresh DPIA; minimize data; prohibit unrelated sensitive inference; define retention/deletion; control vendor reuse/training.                | DPO + HR + Procurement                         | DPIA; data map; contract; retention schedule       | Before real data       | Blocking        |
| MP-06  | H-06           | Mitigate                   | Meaningful human oversight: no auto rejection/hiring; source review; explanation; override authority; reason recording; anti-automation-bias training. | HR / Business Owner                            | SOP; training; decision/override logs              | Before pilot           | Blocking        |
| MP-07  | H-07           | Mitigate + Restore         | Provide understandable notice; correction/challenge channel; competent human reconsideration; track outcomes and root causes.                          | HR + Legal + DPO                               | Notice; procedure; case log                        | Before pilot           | Blocking        |
| MP-08  | H-08           | Mitigate                   | Security threat model, least privilege, logging, secure integrations, vendor due diligence, incident notification and model/change controls.           | CISO + IT + Procurement                        | Security assessment; access review; vendor file    | Before pilot           | Blocking        |
| MP-09  | H-09           | Avoid                      | Prohibit emotion/personality inference and opaque/unvalidated behavioral scoring for recruitment suitability.                                          | HR + Legal + Data & AI                         | Requirements; configuration; test evidence         | Design gate            | Blocking        |
| MP-10  | All            | Mitigate                   | Phased/synthetic pilot first; cap scope; define stop-use authority; monitor errors, overrides, complaints, accessibility and fairness indicators.      | AI Governance + HR + Data & AI                 | Pilot plan; dashboard; stop criteria               | Pilot / ongoing        | Blocking        |
| MP-11  | All            | Mitigate                   | Complete stakeholder engagement and document how input changed design, controls or deployment decision.                                                | AI Governance Lead + HR                        | SEP evidence; action closure                       | Before real pilot      | Blocking        |
| MP-12  | All            | Avoid / Stop               | If residual rights impacts remain incompatible or cannot be reduced to an acceptable governance position, do not deploy or retire the use case.        | AI Governance Committee + Executive escalation | Decision record                                    | Release gate           | Governance gate |

## 3. Remedy and Procedural Safeguards

| **Mechanism**         | **Required design**                                                                                 | **Restorative outcome**                                                 | **Evidence**                           |
|-----------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|----------------------------------------|
| Notice                | Explain material AI assistance and provide contact route in accessible language.                    | Enables informed participation and challenge.                           | Approved notice; delivery evidence.    |
| Correction            | Allow correction of materially inaccurate applicant data or parsing.                                | Correct data and re-run/review assessment where appropriate.            | Correction request and closure record. |
| Challenge             | Accessible channel to contest material AI-supported outcome or suspected unfair treatment.          | Independent/competent human reconsideration.                            | Challenge log; decision rationale.     |
| Reconsideration       | Reviewer with authority examines source application without being bound by AI rank.                 | Restore fair consideration where a decision path was affected.          | Human review record.                   |
| Escalation / incident | Rights, discrimination, privacy or security concerns routed to specialists and AI Governance.       | Contain further harm; trigger reassessment and affected-person support. | Incident and escalation records.       |
| External remedies     | Internal mechanisms must not imply waiver or replacement of statutory/regulatory/judicial remedies. | Preserves access to legally available routes.                           | Legal-approved wording.                |

## 4. Legal Obligations Boundary

Applicable legal obligations must be identified by Legal/DPO based on actual jurisdiction, role, data, provider and deployment facts. HUDERIA itself does not create legal obligations. The mitigation plan should cross-reference, rather than merge, obligations arising under GDPR, employment/equality law, the EU AI Act, contractual duties and any domestic implementation of the Council of Europe Framework Convention.

## 5. Approval Gate

| **Release decision.** No blocking mitigation may be treated as implemented without evidence. DuckTalent remains DO NOT DEPLOY until the AI Governance Committee receives Legal, Privacy, HR, Security, Risk and technical evidence demonstrating that blocking actions are closed or explicitly escalated under the Duckworks risk-acceptance model. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Source Basis

- Council of Europe, HUDERIA - Methodology and Model (2026), approved Methodology 26 February 2025 and Model: COBRA 25 February 2026; official consolidated publication dated April 2026.

- Council of Europe official HUDERIA webpage and Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law webpage.

- Duckworks controlled project artifacts: Business Scenario; Business Use Case Portfolio; Stakeholder Register; Assumptions Register; AI Risk Classification & Assessment Methodology; AI RACI; AI Governance Lifecycle SOP; Algorithmic Impact Assessment; EU FRIA; GDPR DPIA; Acceptance Criteria.

**Official HUDERIA publication:** https://rm.coe.int/prems-002726-gbr-2006-huderia-texte-web-a4/48802ba7b1

**Official HUDERIA page:** https://www.coe.int/en/web/artificial-intelligence/huderia-risk-and-impact-assessment-of-ai-systems
