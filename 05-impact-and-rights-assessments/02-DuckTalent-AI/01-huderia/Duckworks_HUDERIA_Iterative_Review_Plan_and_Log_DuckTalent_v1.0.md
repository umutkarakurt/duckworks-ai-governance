# Duckworks HUDERIA Iterative Review Plan & Log — DuckTalent AI (AI-005)

**Lifecycle monitoring, reassessment and mitigation-effectiveness review - DuckTalent AI (AI-005)**

| **Document ID**    | DW-WING-HUD-06                         |
|--------------------|----------------------------------------|
| **Version / date** | 1.0 / 9 August 2026                    |
| **Status**         | Portfolio Draft                        |
| **Classification** | Portfolio / Synthetic / Non-production |

**Portfolio disclaimer.** Duckworks, Project W.I.N.G., all personnel, AI systems, datasets, decisions, stakeholder inputs and evidence are fictional or synthetic. This document is an internal portfolio artifact, not legal advice, certification evidence, or a statement of regulatory conformity.

## 1. Purpose

HUDERIA treats risk and impact assessment as an iterative lifecycle process. This plan defines how Duckworks will revisit COBRA, stakeholder evidence, the RIA and the Mitigation Plan when the system, its data, its users, or the real-world environment changes.

## 2. Review Cadence

| **Review point**        | **Duckworks proposed cadence**                         | **Minimum scope**                                                                                                               |
|-------------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Pre-pilot gate          | Before any real-applicant pilot                        | Refresh COBRA; complete SEP; RIA; mitigation closure; Legal/Privacy/Security/HR review.                                         |
| Pre-production gate     | Before production authorization                        | Full HUDERIA update using pilot evidence; verify remedies, human oversight, fairness, accessibility and monitoring.             |
| Early production review | Quarterly for the first year if production is approved | Impact trends, complaints/challenges, override behavior, error distribution, security/privacy events, mitigation effectiveness. |
| Steady-state review     | At least annually while material use continues         | Full rights/context review plus change history and stakeholder feedback.                                                        |
| Event-driven review     | Immediately on a material trigger                      | Reopen affected HUDERIA elements; suspend use where needed.                                                                     |

The cadence above is Duckworks recommended practice, not a HUDERIA-prescribed legal interval. Faster review is required where risk or contextual change warrants it.

## 3. Material Reassessment Triggers

- Change in intended purpose, autonomy, decision authority, ranking logic, feature set or use beyond recruitment screening/recommendation.

- New model/provider/version, material configuration change, hosting/subprocessor change or new third-party integration.

- New data categories, training/reference data, sensitive inferences, connectors, permissions or retention practices.

- Expansion to new countries, business units, languages, job families, internal mobility, promotion, performance, termination or workforce monitoring.

- Material change in applicant population, social context, employment practices or data distribution that may create drift or unequal effects.

- Fairness signal, discriminatory outcome, material parsing/ranking error, accessibility failure, complaint pattern or successful challenge.

- Evidence that recruiters are mechanically following rank, cannot override, lack training or do not review source information.

- Privacy or security incident, unauthorized access, data leakage, vendor/model compromise or supply-chain event.

- New misuse or out-of-scope use, including personality/emotion inference or automatic rejection/hiring.

- Change in applicable law, regulatory guidance, policy or legal interpretation.

- Control failure, evidence expiry, ineffective mitigation or inability to reconstruct material AI-supported decisions.

- Decision to retire, replace or substantially redesign the system.

## 4. Monitoring Indicators

| **Indicator**                                   | **Purpose**                                                       | **Source**                     | **Trigger approach**                                                                  |
|-------------------------------------------------|-------------------------------------------------------------------|--------------------------------|---------------------------------------------------------------------------------------|
| Parsing/ranking error distribution              | Detect reliability problems and uneven error patterns.            | Validation / QA samples        | Thresholds must be defined before production; material deviation triggers review.     |
| Human override / correction rate                | Detect over-reliance, model weakness or workflow problems.        | Recruitment decision logs      | Unexpected collapse or spike requires investigation; no invented target in portfolio. |
| Applicant challenges / corrections / complaints | Detect transparency, accuracy, fairness and remedy issues.        | Case-management log            | Pattern, severity or systemic issue triggers RIA/MP review.                           |
| Accessibility defects                           | Detect barriers for disabled or differently situated applicants.  | Accessibility tests / feedback | Material barrier triggers stop/rework for affected workflow.                          |
| Fairness / group-level outcome indicators       | Detect disparate effects where lawful and appropriate to measure. | Approved fairness monitoring   | Material unexplained disparity triggers specialist review.                            |
| Security/privacy incidents                      | Detect confidentiality, integrity, vendor or access failures.     | SOC/privacy incident process   | Material event triggers immediate containment and reassessment.                       |
| Model/vendor changes                            | Detect evidence invalidation.                                     | Change/vendor management       | Material change requires revalidation before use.                                     |
| Operator training / oversight failures          | Detect illusory human oversight.                                  | Training, QA, decision review  | Material failure may suspend ranking until remediated.                                |

## 5. Iterative Review Workflow

1.  Detect trigger or scheduled review point and open a HUDERIA review record.

2.  Determine which assumptions, risk factors, affected groups, rights areas or mitigations may have changed.

3.  Refresh COBRA and re-triage the system; determine whether stakeholder re-engagement is needed.

4.  Update the RIA variables using current evidence, including actual impacts where available.

5.  Review mitigation effectiveness and apply avoid/mitigate/restore/compensate as appropriate.

6.  Determine whether the current lifecycle approval remains valid, requires conditions, suspension, or retirement.

7.  Record decision, owners, evidence, affected-person remedy actions and next review point.

## 6. Review Log

| **Review ID** | **Date**   | **Trigger**                     | **HUDERIA elements reopened** | **Key changes / impacts**                                                                    | **Decision**  | **Owner**                           | **Next review**                                           |
|---------------|------------|---------------------------------|-------------------------------|----------------------------------------------------------------------------------------------|---------------|-------------------------------------|-----------------------------------------------------------|
| IR-000        | 9 Aug 2026 | Initial pre-deployment baseline | COBRA / SEP / RIA / MP        | Full HUDERIA baseline created; stakeholder evidence and blocking controls remain incomplete. | DO NOT DEPLOY | AI Governance Lead / Business Owner | At completion of blocking actions / before any real pilot |
| IR-001        | TBD        | Future                          | TBD                           | TBD                                                                                          | TBD           | TBD                                 | TBD                                                       |
| IR-002        | TBD        | Future                          | TBD                           | TBD                                                                                          | TBD           | TBD                                 | TBD                                                       |

## 7. Stop-Use Criteria

- Evidence of systemic discriminatory ranking or serious rights impact.

- Loss of meaningful human oversight or unauthorized automatic rejection/hiring.

- Material data leakage, model compromise or corrupted ranking logic.

- Inability to provide correction, challenge or human reconsideration for materially affected applicants.

- Material accessibility failure without an effective alternative route.

- Unvalidated model/provider/data change that invalidates prior assessment evidence.

- Any use found incompatible with applicable law or Duckworks risk appetite.

## 8. Governance Decision

| **Current state.** Iterative review controls are designed but cannot be considered operational until DuckTalent reaches an approved pilot or production state. The current baseline review preserves the DO NOT DEPLOY decision. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Source Basis

- Council of Europe, HUDERIA - Methodology and Model (2026), approved Methodology 26 February 2025 and Model: COBRA 25 February 2026; official consolidated publication dated April 2026.

- Council of Europe official HUDERIA webpage and Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law webpage.

- Duckworks controlled project artifacts: Business Scenario; Business Use Case Portfolio; Stakeholder Register; Assumptions Register; AI Risk Classification & Assessment Methodology; AI RACI; AI Governance Lifecycle SOP; Algorithmic Impact Assessment; EU FRIA; GDPR DPIA; Acceptance Criteria.

**Official HUDERIA publication:** https://rm.coe.int/prems-002726-gbr-2006-huderia-texte-web-a4/48802ba7b1

**Official HUDERIA page:** https://www.coe.int/en/web/artificial-intelligence/huderia-risk-and-impact-assessment-of-ai-systems
