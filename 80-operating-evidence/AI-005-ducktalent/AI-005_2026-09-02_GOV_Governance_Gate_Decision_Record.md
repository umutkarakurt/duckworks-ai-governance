# AI-005 DuckTalent — Synthetic Pre-Deployment Governance Gate Decision Record

| **Field** | **Value** |
|---|---|
| **Document ID** | DW-DT-GATE-01 |
| **Version / date** | 1.0 / 2 September 2026 |
| **AI system** | AI-005 — DuckTalent AI |
| **Lifecycle stage reviewed** | Concept / pre-deployment |
| **Decision question** | May DuckTalent advance to a pilot using real applicants? |
| **Current residual risk** | Critical (20) |
| **System control effectiveness** | Not Implemented |
| **Evidence confidence** | Low |
| **Existing governance gate** | Do not deploy in current state |
| **Decision outcome** | **DENIED — maintain DO NOT DEPLOY with real applicants** |
| **Permitted continuation** | Documentation, design, supplier/architecture evaluation, and controlled synthetic testing only |
| **Exceptional risk acceptance** | Not requested / not granted |
| **Evidence snapshot** | GitHub `main` at commit `e2b0a483ea0836bc22f7f9d8471eb50441f3cbcf` |
| **Classification** | Portfolio / Synthetic / Non-production |

> **Synthetic decision-record boundary.** This is a worked portfolio governance record showing how Duckworks would consume assessment and control-test evidence at a lifecycle gate. It is not evidence that a real AI Governance Committee meeting occurred, that real executives approved or rejected a system, or that any real applicant decision was made.

## 1. Decision requested

The governance question is deliberately narrower than “Is DuckTalent fair?” or “Is DuckTalent compliant?”

The decision requested is:

**May AI-005 DuckTalent move from concept / pre-deployment into a pilot that processes or materially influences decisions about real applicants?**

Under the Duckworks lifecycle procedure, a lifecycle stage is a permission boundary. A pilot decision therefore requires evidence appropriate to that stage and does not follow automatically from successful synthetic testing.

## 2. Decision authority and procedural rule

Duckworks assigns consequential AI approval according to current residual risk and system-specific release conditions.

For **Critical** residual risk:

- production or real-world consequential use is normally blocked pending treatment;
- business owners cannot self-approve High or Critical residual risk;
- exceptional acceptance requires executive escalation and does not override applicable law; and
- workforce AI requires fairness, criteria, explainability, meaningful human review, and contestability evidence before any deployment decision.

No exceptional executive acceptance is requested in this worked scenario.

The procedural outcome is therefore to test whether the evidence is sufficient to remove the existing block. It is not sufficient merely to show that one synthetic control test passed.

## 3. Evidence considered

| **Evidence object** | **What the evidence establishes** | **What remains unresolved** | **Decision effect** |
|---|---|---|---|
| `04-risk-assessment/Duckworks_AI_Risk_Scenarios_v1.0.md` | DuckTalent current residual risk is **Critical (20)**; system control effectiveness is **Not Implemented**; evidence confidence is **Low**; current gate is **Do not deploy in current state**. `DT-02` synthetic evidence receives no residual-risk reduction credit. | Current Critical risk has not been reduced. | **Blocking** |
| `01-project-charter-and-context/03-project-governance/Duckworks_Project_Acceptance_Criteria_v1.0.md` | Critical-risk systems must not be described as cleared for unrestricted production. DuckTalent requires enhanced legal/privacy/fairness analysis, meaningful human review, bias testing, transparency/contestability, and reduction of Critical risk. | DuckTalent-specific acceptance conditions are not all satisfied. | **Blocking** |
| `06-governance-operating-model/Duckworks_AI_Governance_Lifecycle_SOP_v1.0.md` | Critical risk is normally blocked; workforce AI requires fairness, criteria, explainability, human-review and contestability evidence; all blocking release conditions must be satisfied before lifecycle authorization. | Required release evidence remains incomplete. | **Blocking** |
| `05-impact-and-rights-assessments/02-DuckTalent-AI/Duckworks_Algorithmic_Impact_Assessment_DuckTalent_v1.0.md` | Intended purpose and decision boundary are documented. The AIA retains **DO NOT DEPLOY** because real-applicant evidence is insufficient and material fairness, privacy, transparency, accessibility, human-oversight and security impacts remain. | Production design, fairness validation, accessibility, human-oversight operation, monitoring baseline and other blocking evidence remain incomplete. | **Blocking** |
| `05-impact-and-rights-assessments/02-DuckTalent-AI/Duckworks_EU_Fundamental_Rights_Impact_Assessment_DuckTalent_v1.0.md` | Fundamental-rights risks and blocking fairness/remedy requirements are documented; the synthetic DT-02 package improves testability only. | Real-applicant rights/fairness evidence, lawful methodology, meaningful human oversight and remedy remain incomplete. | **Blocking** |
| `05-impact-and-rights-assessments/02-DuckTalent-AI/Duckworks_GDPR_Data_Protection_Impact_Assessment_DuckTalent_v1.0.md` | Privacy/data-protection risks and required safeguards are documented; synthetic DT-02 evidence is not sufficient production fairness evidence. | Production processing facts, lawful basis, data design, retention/vendor facts, real fairness-data method and other DPIA actions remain open. | **Blocking** |
| `10-system-model-and-technical-documentation/01-model-documentation/Duckworks_AI_Model_Documentation_DuckTalent_v1.0.md` | The synthetic DT-02 dataset/test is now traceably documented. | Production model/component ID, provider/version, architecture, production data, production validation, explainability, accessibility, human-factors, security and monitoring evidence remain unresolved. | **Blocking** |
| `80-operating-evidence/AI-005-ducktalent/AI-005_Control_Implementation_Card_Fairness_Testing.md` | `DT-02` has a defined owner, trigger, evidence model, decision rule, and synthetic executable implementation. | `DT-01` real feature/job-relevance governance and production operation are not established. | **Supports design/test maturity; insufficient for release** |
| `80-operating-evidence/AI-005-ducktalent/AI-005_2026-09-02_FAIR_Fairness_Run_Summary.json` | 24 synthetic applicants / 12 matched pairs; 10/10 control assertions passed; seeded unapproved feature detected; pre-remediation gate `BLOCK`; remediation retest passed. | Production operating effectiveness and legal compliance/discrimination conclusions are explicitly **Not established**. | **Supports further governance review only** |
| `80-operating-evidence/AI-005-ducktalent/AI-005_2026-09-02_MON_Fairness_Control_Test.md` | `DT-02` operated as designed within the synthetic test population. | Real applicant fairness, production feature governance, lawful fairness-data processing, legal compliance and sustained operation remain unvalidated. | **Supports further governance review only** |

## 4. Evidence synthesis

The evidence demonstrates a meaningful improvement in governance maturity:

**AI-005-R01 → DT-01 boundary → DT-02 executable synthetic testing → seeded issue detected → deployment block → remediation → full-population retest**

The strongest new evidence is that `DT-02` is no longer merely a planned control description. The portfolio demonstrates a reproducible synthetic testing mechanism that identifies an unapproved feature, quantifies the matched-pair/group effect, blocks progression, records an exception, removes the feature, and retests the population.

However, the gate decision must consume **all material evidence**, not only the successful control test.

The successful synthetic retest explicitly ends at:

**ELIGIBLE FOR FURTHER GOVERNANCE REVIEW**

It does not end at:

**APPROVED FOR REAL-APPLICANT PILOT**

## 5. Blocking conditions

The following conditions prevent advancement to a real-applicant pilot:

| **Blocking condition** | **Current position** | **Required before reconsideration** |
|---|---|---|
| Current residual risk | **Critical (20)** | Reassess after evidence-backed treatment; any reduction must be supported by implemented controls and evidence. |
| DT-01 job-relevance / proxy-feature governance | **Not Implemented** | Approved, version-controlled production job criteria and feature specification; direct/proxy/derived feature challenge; approval traceability. |
| Model / system identity | Production model/provider/version **TBD** | Exact model/component/system version and material configuration fixed and traceable to the evidence pack. |
| Production architecture / data | Incomplete | Version-controlled architecture/data-flow and verified production processing design. |
| Production validation | Not established | Representative validation tied to the exact proposed model/system version and intended applicant population. |
| Fairness methodology | Synthetic demonstration only | Lawful, governance-approved production fairness method, relevant population design, metric definitions, investigation/escalation rules and specialist review. |
| Meaningful human oversight | Design requirement only | Demonstrated source review, ability to disregard/override, no automated rejection, reviewer competence/training, rationale and escalation evidence. |
| Transparency / contestability / remedy | Incomplete | Applicant notice, correction/challenge, human reconsideration and case-handling evidence. |
| Accessibility / inclusion | Not validated | Accessibility and non-standard applicant-format testing appropriate to intended use. |
| Privacy / legal | Open | Production processing facts, lawful basis/role analysis, DPIA actions and applicable employment/regulatory review completed. |
| Security / third party | Incomplete | Threat model, security testing, vendor due diligence, contractual/data-use evidence and change-notification controls. |
| Monitoring / reassessment | Not operational | Defined production indicators, owners, triggers and evidence-generation process tied to the approved version. |

## 6. Governance decision

### Decision

**DENIED — DuckTalent may not advance to a pilot using real applicants.**

The existing governance gate remains:

**DO NOT DEPLOY WITH REAL APPLICANTS / DO NOT DEPLOY IN CURRENT STATE**

### Rationale

1. Current residual risk remains **Critical (20)**.
2. The system-level control-effectiveness position remains **Not Implemented**.
3. `DT-02` is only **Partially Implemented within the synthetic portfolio boundary**.
4. `DT-01` remains **Not Implemented**.
5. Production model, version, architecture, data, validation, fairness, oversight, privacy, security, accessibility, transparency/contestability, vendor and monitoring evidence remain incomplete.
6. The successful DT-02 retest is evidence for **further governance review**, not production or pilot authorization.
7. No exceptional executive risk acceptance has been requested or granted.

## 7. Permitted activity while the gate remains closed

The following work may continue because it does not involve real-applicant consequential use:

- documentation and assessment refinement;
- model/vendor/architecture evaluation;
- approved synthetic-data testing;
- criteria and feature-governance design;
- fairness-test methodology design;
- accessibility and human-factors test design;
- privacy/legal/security/vendor review;
- monitoring and evidence-design work; and
- remediation of blocking actions.

The following remain outside the authorized boundary:

- processing real applicant data through DuckTalent for consequential evaluation;
- AI-ranked real-applicant shortlisting;
- AI-supported rejection or hiring;
- any automatic rejection/hiring;
- a real-applicant pilot represented as approved; or
- reliance on the synthetic DT-02 result as proof of legal fairness or compliance.

## 8. Required action ownership

| **Action area** | **Primary accountable / responsible role** | **Status** |
|---|---|---|
| Intended purpose and production recruitment criteria | Beatrice Van Duck — Chief People Officer | Blocking / Open |
| Model identity, architecture, data and technical validation | Dr. Ada Duckfield — Head of Data & AI | Blocking / Open |
| Governance traceability and gate coordination | Eleanor Duckford — AI Governance Lead | Open |
| Employment/fairness and legal applicability review | General Counsel + HR | Blocking / Open |
| Privacy / DPIA closure and fairness-data method | DPO + HR + Data & AI | Blocking / Open |
| Security architecture and testing | CISO + Technical Owner | Blocking / Open |
| Supplier due diligence / contractual evidence | Procurement & Vendor Assurance + Legal | Blocking / Open |
| Final lifecycle reconsideration | Appropriate Duckworks governance authority under the residual-risk rule | Not yet eligible |

No artificial due dates are assigned in this synthetic record. The next review is **event-driven** when the blocking evidence is materially complete or when a material system/provider/data/purpose change requires reassessment.

## 9. Reconsideration trigger

The gate may be reconsidered only when a new evidence pack demonstrates that the relevant blocking conditions have been materially addressed.

At minimum, the reconsideration record should:

1. identify the exact model/system version and configuration;
2. refresh the AIA, risk assessment, FRIA/DPIA and specialist reviews as required;
3. show the status and evidence for each blocking control;
4. include production-relevant validation rather than only synthetic demonstration;
5. record current residual risk and evidence confidence;
6. state unresolved exceptions and conditions;
7. identify the correct approval authority based on the then-current residual risk; and
8. retain the resulting lifecycle decision as a traceable evidence object.

## 10. Decision-record conclusion

This worked record demonstrates the governance transition:

**Assessment → Control evidence → Specialist evidence → Gate review → Decision → Conditions → Reassessment trigger**

The key governance outcome is not that a test passed.

The key governance outcome is that Duckworks **uses the evidence to refuse progression beyond the evidence-supported boundary**.

### Evidence maturity created by this record

**Synthetic control evidence available → Governance evidence pack reviewed → Synthetic lifecycle decision demonstrated**

Not established:

**Real committee approval → Real pilot authorization → Production operation → Validated risk reduction → Independent assurance**

> **Portfolio conclusion:** A governance program demonstrates maturity not only by approving systems, but by making a traceable, evidence-based decision **not to approve** a system when the evidence is insufficient.
