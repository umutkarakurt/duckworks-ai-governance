# Duckworks Skeptical Multi-Perspective AI Governance Project Review

**DUCKWORKS**

Skeptical Multi-Perspective  
AI Governance Project Review

Critical review from five professional perspectives

| **Organization**       | Duckworks (fictional)                                                                       |
|------------------------|---------------------------------------------------------------------------------------------|
| **Project**            | Project W.I.N.G.                                                                            |
| **Review version**     | 1.0                                                                                         |
| **Review posture**     | Skeptical / interview-focused / evidence-focused                                            |
| **Evidence boundary**  | Fictional organization, synthetic data, public-source references and project artifacts only |
| **Change restriction** | No project content has been rewritten in this review                                        |

| **Overall skeptical verdict:** The portfolio demonstrates strong governance architecture and unusually good discipline around legal/framework boundaries, but it is not yet defensible as evidence of an operated AI governance program. The most serious weaknesses are source-of-truth inconsistency, conflicting risk-scoring status, control credit based on unvalidated assumptions, stale document control, and a shortage of worked operating evidence. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## 1. Executive skeptical assessment

**Review conclusion.** I would treat this portfolio as a strong governance-design case study, not yet as proof that Duckworks has a functioning, independently evidenced AI management system. The project is strongest when it describes how governance should work and weakest when it implies that controls, approvals, risk scores, monitoring or assurance are already operating.

| **Area**                            | **Assessment**    | **Skeptical interpretation**                                                                                              |
|-------------------------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------|
| Governance architecture             | Strong            | Clear lifecycle, ownership, risk, impact, change, third-party and evidence concepts.                                      |
| Legal/framework boundary discipline | Strong            | The project repeatedly separates binding law, voluntary frameworks and internal practice.                                 |
| Risk-method consistency             | Material weakness | Active artifacts conflict over whether scoring is authorized and what numeric scores mean.                                |
| Operating control evidence          | Weak              | Most controls are requirements, templates, assumptions or baseline-credited states rather than execution evidence.        |
| Technical AI/security evidence      | Weak              | Threat categories are good, but exact configurations, attack tests and versioned evidence are largely absent.             |
| Data-protection execution           | Moderate-to-weak  | DuckTalent analysis is strong, but it is draft and other personal-data AI systems lack visible formal screening evidence. |
| Product/value evidence              | Weak              | Benefits are intentionally not invented, but baselines, targets, cost and value-realization evidence remain thin.         |
| Interview defensibility today       | Moderate          | Defensible if presented as design/simulation; vulnerable if presented as implemented, approved, tested or compliant.      |

## 2. What survives skeptical scrutiny

- The project consistently distinguishes Duckworks internal risk ratings from legal classifications and avoids claiming that framework mapping equals legal compliance or certification.

- The assumptions register is a strong governance device: material unknowns are explicitly recorded, assigned materiality and given validation evidence expectations.

- The use of cause -\> event -\> impact risk scenarios is materially better than a generic list of AI risks.

- AI-007 is correctly recognized as a shadow-AI governance condition rather than one homogeneous AI system, and the need to decompose material uses is well articulated.

- DuckTalent is appropriately blocked rather than forced through a favorable risk score. The privacy, fairness, human-oversight and evidence limitations are clearly acknowledged.

- Internal Audit independence is consciously preserved in the RACI and policy architecture.

- The control library is unusually audit-oriented in structure: objective, description, classification, owner, frequency, evidence, testing procedure, automation opportunity, risk mapping and status are all captured.

- The portfolio often labels benefits as hypotheses rather than realized ROI, which is more defensible than inventing financial gains.

## 3. Highest-priority weaknesses

| **ID** | **Severity** | **Issue**                                         | **Why it matters**                                                                                                                                                                           | **Interview challenge**                                                                                                                                      |
|--------|--------------|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| F-001  | Critical     | Risk methodology governance / chronology          | A reviewer cannot determine which methodology is authoritative, whether approval occurred, or whether existing residual-risk decisions are valid under the current method.                   | Which risk methodology is authoritative today, who approved it, when did approval occur, and why does a later workbook say zero systems are formally scored? |
| F-002  | High         | Risk scoring semantics                            | This is more than presentation drift: it changes what the numeric value means and how risk conclusions should be defended.                                                                   | Why should I trust a score of 16 rather than the High band, and what changed between the two scoring designs?                                                |
| F-003  | Critical     | Control credit without validated evidence         | The project's own rule says planned or unvalidated controls must not reduce current residual risk. This finding directly challenges the integrity of the AI-001 residual score.              | Show me the design-review records that justified reducing AI-001 likelihood from 3 to 2. If you cannot, why is DD-01 implemented?                            |
| F-004  | High         | Human-oversight assumption used as risk treatment | A control that determines whether a safety-related system is advisory or autonomous is too material to leave as an unvalidated assumption while taking residual-risk credit.                 | What workflow evidence proves inspectors can and do override the model, and what happens under throughput pressure?                                          |
| F-005  | High         | Access-control assumption used as control         | Cross-user leakage is a primary GenAI threat. Crediting an untested authorization boundary weakens the credibility of the residual-risk conclusion.                                          | Show the negative authorization tests for two users with different repository rights and the exact connector configuration tested.                           |
| F-006  | High         | Evidence-confidence overstatement                 | Within the portfolio's own evidence boundary, 'High' confidence is not demonstrably supported by direct, independently challengeable operating evidence.                                     | What evidence makes the confidence High rather than Medium if no production model, dataset, contract, or test evidence was reviewed?                         |
| F-007  | High         | Inventory source-of-truth                         | The distinction is conceptually defensible, but without an explicit portfolio vs registered-system taxonomy it looks like a count inconsistency and can break dashboard/acceptance criteria. | Does Duckworks have six AI systems or seven inventory entries, and which number should the board see?                                                        |
| F-008  | High         | Ownership inconsistency                           | Ownership is a foundational control. A reviewer will treat conflicting accountable/technical ownership as evidence that the inventory is not under effective configuration control.          | Who is actually accountable for PondGPT's technical implementation and security configuration?                                                               |
| F-009  | High         | Technology/vendor drift across inventories        | Provider role, data flows, security responsibility, IP terms and legal obligations can change materially with these architecture changes.                                                    | Were the risk, privacy, security and legal assessments reopened when the implementation model changed from internal/unknown to named third-party services?   |
| F-011  | High         | Document-control staleness                        | A portfolio that emphasizes evidence and lifecycle control should keep its own master deliverables register current.                                                                         | Which artifact register is authoritative, and why does it say planned for documents you are showing me as complete?                                          |
| F-013  | High         | Evidence repository placeholder                   | A folder label is not evidence traceability. It does not identify the execution record, date, version, owner or result.                                                                      | Give me the exact evidence object for DD-01 for design version Pilot-0.8 and show how it traces back to the risk scenario.                                   |
| F-014  | High         | Approval claims without approval artifacts        | An auditor will distinguish a governance status field from evidence that the designated authority actually made the decision.                                                                | Who approved FeatherForecast for production and WingInspect/PondGPT for restricted pilot, on what date, against which evidence pack?                         |
| F-031  | High         | Document sprawl / authoritative record            | Parallel sources of truth create exactly the inconsistency already visible in owners, vendors, lifecycle labels and scores.                                                                  | Which artifact is the system of record for ownership, vendor, lifecycle, risk and evidence, and how are downstream documents synchronized?                   |
| F-033  | Moderate     | Design-heavy / operation-light portfolio          | A hiring manager may infer document generation skill rather than operating governance experience.                                                                                            | Show me one governance decision from intake through evidence, testing, approval, monitoring and reassessment—not another template.                           |

## 4. Cross-artifact inconsistencies that would be challenged

| **Topic**                    | **Artifact position A**                                                                                     | **Artifact position B**                                                                                              | **Risk** |
|------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|----------|
| Risk scoring authorization   | Risk Report v1.0: seven systems assessed and scored.                                                        | Risk Workbook Draft v0.9: do not score until methodology approval; zero systems formally scored.                     | Critical |
| Risk quantity meaning        | v1.0 methodology uses Severity x Likelihood product as the risk score and thresholds.                       | v0.9 says matrix band is authoritative and product is sorting-only.                                                  | High     |
| DuckDesign control status    | DD-01 marked Implemented and credited in residual risk.                                                     | Operating evidence still requires validation; ASM-007 is Open Critical.                                              | Critical |
| WingInspect oversight        | Residual risk credits human final inspection.                                                               | ASM-008 human final authority remains Open Critical.                                                                 | High     |
| PondGPT authorization        | Permission-aware retrieval partially credited.                                                              | ASM-009 and newer ASM-030 authorization boundary remain Open Critical.                                               | High     |
| Portfolio count              | Acceptance baseline and prior inventories use seven entries.                                                | New synthetic inventory uses six registered systems and excludes AI-007.                                             | High     |
| PondGPT technical owner      | AI Asset Inventory: Dr. Ada Duckfield.                                                                      | Synthetic AI System Inventory: Oliver Duckett.                                                                       | High     |
| DuckTalent vendor            | AI Asset Inventory: vendor not selected / model TBD.                                                        | Synthetic inventory: MeritPath HR Technologies S.A., explicitly Open assumption.                                     | High     |
| FeatherForecast architecture | AI Asset Inventory: internal model / no third party.                                                        | Synthetic inventory: Northstar third-party analytics platform, Open assumption.                                      | High     |
| WingInspect architecture     | AI Asset Inventory: internal model.                                                                         | Synthetic inventory: VisiCore third-party components, Open assumption.                                               | High     |
| Master deliverable status    | Required Deliverables still marks RACI/control library/operating model and other items planned or required. | Those artifacts now exist in the project library.                                                                    | High     |
| Evidence confidence          | FeatherForecast: Effective controls / High confidence / approved.                                           | AIA limitation: no production model, source code, vendor contract, real dataset or technical test evidence reviewed. | High     |

## 5. Skeptical AI governance hiring manager review

**Skeptical verdict.** I would see clear conceptual depth and strong portfolio ambition, but I would probe whether the candidate can distinguish designed governance from operated governance. The current document volume is not a substitute for evidence of prioritization, implementation and decision-making.

### What I would challenge

- The portfolio is over-produced relative to its execution evidence. A candidate could look very strong on templates but weak on operating experience.

- The source-of-truth problem is visible: inventory facts, owners, vendors, lifecycle states and scoring status drift across versions.

- The newer risk workbook appears to invalidate the confidence with which older scored reports are presented unless a supersession/approval story is supplied.

- ISO/IEC 42001 and ISO/IEC 27001 mappings are cautious but high-level. They show awareness, not yet detailed management-system/control integration.

- DuckTalent has many assessment artifacts. The candidate must explain the unique decision value of each one, otherwise the portfolio looks document-centric.

- The project would be more convincing with three or four high-quality worked evidence chains than with additional policies or templates.

### Questions I would ask in an interview

1.  Which five artifacts are authoritative, and which are supporting or superseded?

2.  What is the single strongest example of a governance decision that changed because of your assessment?

3.  Where did you deliberately choose not to create a document because an existing enterprise process was sufficient?

4.  How would you explain the project in five minutes to a CISO without listing frameworks?

5.  What part of this portfolio demonstrates implementation rather than documentation?

## 6. Skeptical Internal Auditor review

**Skeptical verdict.** The control design is audit-friendly, but the portfolio is not yet audit-ready. The most material issue is that control credit, evidence confidence and approval statuses sometimes exceed the evidence actually available in the artifact set.

### What I would challenge

- Control design, implementation, operation and effectiveness are not consistently separated. "Implemented" is sometimes used while operating evidence is still unvalidated.

- Residual risk relies on open assumptions for human oversight and access control in several high-impact systems.

- The evidence index is itself only planned, while inventory evidence locations are generic folder references.

- Approval fields do not link to approval records, committee minutes, conditions, exceptions or expiry dates.

- The Required Deliverables register is stale, which undermines the claim that document control is mature.

- Acceptance criteria exist but there is no reviewed acceptance-results register showing Pass/Fail/Pass with Action and evidence.

- Independent assurance is largely future-state; no complete workpaper demonstrates population, sample, testing, exceptions and conclusion.

### Questions I would ask in an interview

6.  Show the evidence that caused one residual-risk downgrade.

7.  How do you prevent a planned control from being accidentally credited in current risk?

8.  What is your population for testing AI-GOV-01 and how would you sample it?

9.  How would you detect that an approved model version changed without governance review?

10. Which current project acceptance criteria would fail today?

## 7. Skeptical CISO review

**Skeptical verdict.** The threat vocabulary is good and the control library is directionally sound. The weak point is technical proof: exact models, configurations, trust boundaries, attack paths, test results, telemetry and version-bound evidence are mostly missing or marked TBD.

### What I would challenge

- Prompt injection, RAG poisoning, privilege amplification and data leakage are named, but there is no worked threat model/test report demonstrating exploitation and regression testing.

- PondGPT access inheritance is one of the most consequential security boundaries and is still an Open Critical assumption.

- The AIBOM contains many TBD model/version/hash/license/configuration fields, limiting reproducibility and incident response.

- Shadow-AI containment is well designed but lacks a synthetic discovery data set or telemetry case showing how detection actually works.

- Supplier controls are template-heavy; security assurance evidence, change notification and exact model/provider facts are incomplete.

- Safety-related systems need tighter linkage between AI security failure modes and the product/quality safety case.

### Questions I would ask in an interview

11. Draw the PondGPT trust boundaries and show where indirect prompt injection can cross an authorization boundary.

12. What evidence proves the RAG connector cannot return a document the user cannot access directly?

13. Which exact model/configuration was security tested, and how would you detect a silent provider update?

14. What is the kill/fallback mechanism for QuackBot and PondGPT?

15. How would a malicious or malformed image affect WingInspect, and where is that tested?

## 8. Skeptical Data Protection Specialist review

**Skeptical verdict.** The privacy work is careful about legal uncertainty and avoids simplistic AI-Act/GDPR conflation. The remaining weakness is factual completeness: privacy decisions are often well-designed but cannot be finalized without exact processing, role, retention, transfer, vendor and human-decision evidence.

### What I would challenge

- DuckTalent DPIA is a draft and explicitly leaves lawful basis, data flow, scale, location, provider role and employment-law context open.

- Meaningful human involvement is a privacy/legal dependency, but operational evidence of recruiter behavior is absent.

- QuackBot and PondGPT process personal data, but the reviewed set does not show a formal DPIA screening record for each.

- The DPA is a template rather than an executed vendor-specific record; subprocessors, transfers, deletion and training-use settings are not evidenced.

- Data asset records include many TBD retention, provenance, rights/license and quality fields.

- WingInspect camera scope and PondGPT employee/meeting logging require explicit purpose-limitation and workforce privacy controls.

### Questions I would ask in an interview

16. What lawful basis would DuckTalent rely on and what facts are still needed before selecting it?

17. How do you prove recruiter review is meaningful rather than de facto automated decision-making?

18. Where are the DPIA screening decisions for QuackBot and PondGPT?

19. Which processors/subprocessors receive applicant or employee data and where is it stored?

20. What retention period applies to prompts, embeddings, rankings and human-review logs?

## 9. Skeptical AI Product Owner review

**Skeptical verdict.** The project is optimized for governance coverage, not product decision quality. The controls are detailed, but the business problem, user evidence, value baselines, operational thresholds and learning loops are comparatively underdeveloped.

### What I would challenge

- Most value statements remain hypotheses or baseline TBD. This is correct from an evidence perspective, but it means value has not yet been demonstrated.

- There is little evidence of user research, workflow observation, usability testing, adoption behavior or failure-tolerance decisions.

- KPIs/KRIs are frequently listed without thresholds, sample windows or go/no-go criteria.

- The portfolio lacks a clear risk-adjusted value prioritization view: which system should receive investment first and why?

- FeatherForecast should be the mature product example, yet it lacks the strongest end-to-end operating and business evidence.

- For DuckTalent, a large control burden may make the use case uneconomic even if risks become manageable; that trade-off is not evaluated.

### Questions I would ask in an interview

21. What user problem is QuackBot solving and what baseline proves it exists?

22. What is the minimum acceptable performance for WingInspect and why?

23. At what benefit level does the DuckTalent control burden stop being worth the investment?

24. Which metric would cause you to stop PondGPT despite positive adoption?

25. What did users learn during the DuckDesign pilot that changed the product scope?

## 10. Unsupported or weakly supported assumptions

| **ID**             | **Assumption**                                             | **Status**      | **Why skeptical reviewers care**                                                                                |
|--------------------|------------------------------------------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------|
| ASM-005            | Human accountability across consequential decisions        | Open / Critical | This is a cross-portfolio dependency and cannot safely be treated as a blanket fact.                            |
| ASM-007            | DuckDesign competent-engineer review                       | Open / Critical | Used to support safety and residual-risk conclusions.                                                           |
| ASM-008            | WingInspect final human acceptance/rejection authority     | Open / Critical | Defines whether the system is advisory or effectively autonomous.                                               |
| ASM-009            | PondGPT authorization inheritance                          | Open / Critical | Directly affects cross-user leakage and privilege amplification.                                                |
| ASM-010            | QuackBot escalation capability                             | Open / High     | Human escalation is central to customer harm controls.                                                          |
| ASM-011            | FeatherForecast manager approval                           | Open / Medium   | Used to limit automation risk in the production baseline.                                                       |
| ASM-023            | Critical residual risk appetite and exceptional escalation | Open / Critical | Yet used across risk methodology, RACI and approval rules.                                                      |
| ASM-025 to ASM-030 | New vendor/implementation facts                            | Open            | Materially change supplier, security, data-flow and legal assumptions; reassessment execution is not evidenced. |

## 11. Missing evidence that would materially strengthen interview defensibility

| **Evidence area**   | **What is missing**                                                                                               |
|---------------------|-------------------------------------------------------------------------------------------------------------------|
| Risk governance     | Authoritative methodology approval/supersession record and a reconciled scored workbook.                          |
| Approvals           | Synthetic committee/release decision records linked to exact evidence packs and conditions.                       |
| Control evidence    | Evidence index with control ID, AI ID, version, date, owner, result and expiry.                                   |
| DuckDesign          | One completed engineer-review record and safety validation gate execution.                                        |
| WingInspect         | One human-review/override sample plus false-negative validation and independent QA sample.                        |
| FeatherForecast     | Version 2.3.1 back-test, drift report, data-quality result, access review and approval record.                    |
| QuackBot            | Threat model, prompt/RAG attack test results, content-boundary testing and escalation test.                       |
| PondGPT             | Permission regression test, prompt/RAG poisoning test, DLP/logging evidence and exact connector baseline.         |
| DuckTalent          | Vendor/model evidence, fairness evaluation, accessibility test, human-oversight test and completed privacy facts. |
| Third-party         | One completed supplier due-diligence/contract/DPA pack rather than templates only.                                |
| Data governance     | One complete data-lineage example with provenance, purpose, retention, rights/license and quality evidence.       |
| Change management   | One worked CM-C2/C3 change caused by a provider/model/data change.                                                |
| Incident management | One tabletop or synthetic incident with evidence preservation, containment and restart decision.                  |
| Assurance           | One independent control-test workpaper showing population, sample, evidence, exceptions and conclusion.           |
| Board reporting     | One governance committee pack/minutes/action log demonstrating dashboard-driven decisions.                        |

## 12. Content that may be perceived as generic or AI-generated

- Repeated framework phrases ("Govern-Map-Measure-Manage", "lifecycle governance", "meaningful human oversight", "prompt injection/RAG poisoning") are correct but appear across many documents without enough system-specific execution evidence.

- Framework mappings are broad and recurring. Without a worked control/evidence crosswalk they can look like name-checking rather than applied integration.

- Multiple DuckTalent assessments repeat the same concerns and decision. The unique purpose of each assessment must be explained succinctly.

- Many documents use polished governance language and disclaimers but few contain messy operational artifacts such as failed tests, exceptions, disputed decisions, overdue actions or imperfect evidence.

- The control library is very complete structurally. That is a strength, but 45 controls across a fictional seven-entry baseline may feel generated unless the candidate can justify materiality and show which controls are actually relied upon.

- The duck-themed naming makes the fictional boundary memorable, but senior interviewers may focus more readily on the substance if the presentation remains visually restrained and the candidate avoids leaning into the jokes.

## 13. Claims that should not be made in an interview yet

| **Risky claim**                                                            | **Why it would be challenged**                                                                                        |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| "All seven systems were formally risk-assessed under the approved method." | Not defensible until the v1.0 report is reconciled with the newer v0.9 scoring gate.                                  |
| "The implemented controls are operating effectively."                      | Several controls are baseline-credited, partially implemented or unvalidated; design and operation must be separated. |
| "FeatherForecast is a fully evidenced mature production system."           | Its AIA explicitly notes the absence of production model/data/technical test evidence in the portfolio.               |
| "PondGPT permissions are proven safe."                                     | Permission inheritance remains an Open Critical assumption.                                                           |
| "Duckworks discovered real employee shadow-AI misuse."                     | The scenario is synthetic unless a synthetic discovery case is shown; do not imply real telemetry.                    |
| "The project is compliant with the EU AI Act/GDPR/ISO 42001/ISO 27001."    | The project itself correctly disclaims legal compliance, conformity and certification.                                |
| "The AI Governance Committee is operating."                                | Design is strong, but recurring decision/minutes evidence was not reviewed.                                           |
| "Vendor due diligence is implemented across the portfolio."                | Templates exist; system-specific operating evidence is incomplete.                                                    |
| "The project has passed all acceptance criteria."                          | Acceptance criteria are defined, but a completed acceptance-results register was not reviewed.                        |

## 14. High-probability interview challenge questions

**1. Which risk methodology is authoritative today, who approved it, when did approval occur, and why does a later workbook say zero systems are formally scored?** *\[F-001\]*

**2. Why should I trust a score of 16 rather than the High band, and what changed between the two scoring designs?** *\[F-002\]*

**3. Show me the design-review records that justified reducing AI-001 likelihood from 3 to 2. If you cannot, why is DD-01 implemented?** *\[F-003\]*

**4. What workflow evidence proves inspectors can and do override the model, and what happens under throughput pressure?** *\[F-004\]*

**5. Show the negative authorization tests for two users with different repository rights and the exact connector configuration tested.** *\[F-005\]*

6\. What evidence makes the confidence High rather than Medium if no production model, dataset, contract, or test evidence was reviewed? *\[F-006\]*

7\. Does Duckworks have six AI systems or seven inventory entries, and which number should the board see? *\[F-007\]*

8\. Who is actually accountable for PondGPT's technical implementation and security configuration? *\[F-008\]*

9\. Were the risk, privacy, security and legal assessments reopened when the implementation model changed from internal/unknown to named third-party services? *\[F-009\]*

10\. Which artifact register is authoritative, and why does it say planned for documents you are showing me as complete? *\[F-011\]*

11\. Give me the exact evidence object for DD-01 for design version Pilot-0.8 and show how it traces back to the risk scenario. *\[F-013\]*

12\. Who approved FeatherForecast for production and WingInspect/PondGPT for restricted pilot, on what date, against which evidence pack? *\[F-014\]*

13\. Which artifact is the system of record for ownership, vendor, lifecycle, risk and evidence, and how are downstream documents synchronized? *\[F-031\]*

14\. Show me one governance decision from intake through evidence, testing, approval, monitoring and reassessment—not another template. *\[F-033\]*

15\. Show the last monthly drift report, last manager override sample, back-test result and approval record for FeatherForecast. *\[F-036\]*

16\. Who approved the critical-risk appetite and exceptional acceptance authority? *\[F-038\]*

17\. What is the difference in this portfolio between 'implemented', 'operating', 'effective' and 'validated'? *\[F-047\]*

18\. Which credited controls are genuinely operating versus assumed for the fictional baseline? *\[F-048\]*

19\. Show me one completed CM-C2/C3 change record caused by the new vendor assumptions and the artifacts it reopened. *\[F-010\]*

20\. Which criteria currently fail, who accepted the residual actions, and where is the signed acceptance record? *\[F-012\]*

21\. Show me a successful indirect prompt-injection test, the affected trust boundary, remediation, and regression result. *\[F-015\]*

22\. Which exact model, embedding model, vector-store version and prompt/configuration hash were in the approved PondGPT pilot? *\[F-016\]*

23\. How was shadow AI discovered, how many tools/users were involved, and what evidence confirmed the exposure? *\[F-017\]*

24\. What is the lawful basis, who is controller/processor for each processing step, where is data stored, and what is the retention schedule? *\[F-019\]*

25\. Where is the documented DPIA threshold screening for QuackBot and PondGPT? *\[F-020\]*

## 15. Bottom line

| **Hiring-manager bottom line:** This project can become an excellent AI governance portfolio piece. Today, however, its defensible claim is: "I designed a comprehensive fictional AI governance operating model and applied it to synthetic use cases." Its least defensible claim is: "I demonstrated that the controls are implemented, approved, effective and auditable." The next maturity jump should come from reconciliation and worked evidence, not from creating more policy documents. |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**No project rewrite was performed.** This review intentionally identifies weaknesses, contradictions and evidence gaps only. Remediation should begin after the owner decides which artifacts and versions are authoritative.

## Appendix A. Primary project artifacts used in the review

- Duckworks AI Governance Readiness Assessment.pdf

- Duckworks_Project_Assumptions_Register_v1.0.docx

- Duckworks_Project_Acceptance_Criteria_v1.0.docx

- Duckworks_Project_Required_Deliverables_v1.0.docx

- Duckworks_AI_Risk_Classification_Assessment_Methodology_v1.0.docx

- Duckworks_AI_Risk_Assessment_Report_v1.0.docx

- Duckworks_AI_Risk_Assessment_Workbook_Draft_v0.9.xlsx

- Duckworks_AI_Asset_Inventory_v1.0.xlsx

- Duckworks_Synthetic_AI_System_Inventory_v1.0.xlsx and report

- Duckworks_AI_Control_Library_v1.0.xlsx

- Duckworks_AI_RACI_Chart_v1.0.xlsx

- Duckworks_AI_Impact_Assessment_Pack_Index_v1.0.docx and system AIAs

- Duckworks_AI_Business_Use_Case_Portfolio_v1.0.docx

- Duckworks_GDPR_Data_Protection_Impact_Assessment_DuckTalent_v1.0.docx

- Duckworks_EU_Fundamental_Rights_Impact_Assessment_DuckTalent_v1.0.docx

- Duckworks_HUDERIA_Assessment_Pack_Index_v1.0.docx and related records

- Duckworks_AI_Model_Documentation_DuckTalent_v1.0.docx

- Duckworks_AI_Bill_of_Materials_Register_v1.0.xlsx

- Duckworks_AI_Governance_Lifecycle_SOP_v1.0.docx

- Duckworks_AI_Change_Management_Process_Documentation_Pack_v1.0.docx

- Duckworks_AI_Data_Management_Plan_v1.0.docx

- Duckworks_AI_Data_Processing_Agreement_Template_v1.0.docx

- Duckworks_Public_Frameworks_Legislation_Links.md and regulatory/framework research artifacts

## Appendix B. Complete finding index

| **ID** | **Severity** | **Theme**                                                | **Claim status**                |
|--------|--------------|----------------------------------------------------------|---------------------------------|
| F-001  | Critical     | Risk methodology governance / chronology                 | Inconsistent                    |
| F-002  | High         | Risk scoring semantics                                   | Inconsistent                    |
| F-003  | Critical     | Control credit without validated evidence                | Inconsistent                    |
| F-004  | High         | Human-oversight assumption used as risk treatment        | Partially supported             |
| F-005  | High         | Access-control assumption used as control                | Inconsistent                    |
| F-006  | High         | Evidence-confidence overstatement                        | Unsupported                     |
| F-007  | High         | Inventory source-of-truth                                | Inconsistent                    |
| F-008  | High         | Ownership inconsistency                                  | Inconsistent                    |
| F-009  | High         | Technology/vendor drift across inventories               | Inconsistent                    |
| F-010  | High         | Change-control execution                                 | Missing evidence                |
| F-011  | High         | Document-control staleness                               | Inconsistent                    |
| F-012  | High         | Acceptance not actually demonstrated                     | Missing evidence                |
| F-013  | High         | Evidence repository placeholder                          | Unverifiable                    |
| F-014  | High         | Approval claims without approval artifacts               | Unverifiable                    |
| F-015  | High         | GenAI technical security evidence                        | Missing evidence                |
| F-016  | High         | AIBOM technical incompleteness                           | Missing evidence                |
| F-017  | High         | Shadow-AI discovery claim                                | Partially supported             |
| F-018  | Moderate     | Incident-history wording                                 | Unverifiable                    |
| F-019  | High         | DuckTalent DPIA is structurally strong but not completed | Missing evidence                |
| F-020  | High         | Portfolio-wide DPIA screening evidence                   | Missing evidence                |
| F-021  | High         | Third-party privacy evidence                             | Missing evidence                |
| F-022  | High         | Data governance completeness                             | Missing evidence                |
| F-023  | Moderate     | Worker-privacy boundary                                  | Unsupported assumption          |
| F-024  | High         | Human oversight is mostly design intent                  | Missing evidence                |
| F-025  | Moderate     | Target residual-risk precision                           | Unverifiable                    |
| F-026  | Moderate     | Severity reduction rationale                             | Partially supported             |
| F-027  | Moderate     | Risk/impact terminology collision                        | Generic / potentially confusing |
| F-028  | Moderate     | Framework mapping depth                                  | Generic                         |
| F-029  | Moderate     | ISO/IEC 27001 integration                                | Generic                         |
| F-030  | Moderate     | ISO/IEC 42001 demonstrability                            | Partially supported             |
| F-031  | High         | Document sprawl / authoritative record                   | Inconsistent                    |
| F-032  | Moderate     | Assessment duplication                                   | Generic / over-engineered       |
| F-033  | Moderate     | Design-heavy / operation-light portfolio                 | Missing evidence                |
| F-034  | High         | Business value evidence                                  | Missing evidence                |
| F-035  | Moderate     | Monitoring metrics without thresholds                    | Generic                         |
| F-036  | High         | FeatherForecast production decision                      | Partially supported             |
| F-037  | Moderate     | Operating-model adoption                                 | Unverifiable                    |
| F-038  | High         | Risk appetite authority                                  | Unsupported assumption          |
| F-039  | High         | Circular validation                                      | Weak support                    |
| F-040  | Moderate     | Legal-source verification audit trail                    | Unverifiable                    |
| F-041  | Moderate     | Current-sensitive legal claims                           | Requires external verification  |
| F-042  | Moderate     | Professional presentation risk                           | Presentation concern            |
| F-043  | Moderate     | Independent assurance not demonstrated                   | Missing evidence                |
| F-044  | High         | Executive reporting operating evidence                   | Missing evidence                |
| F-045  | Moderate     | Incident response operation                              | Missing evidence                |
| F-046  | Moderate     | Third-party control maturity                             | Overstated status               |
| F-047  | High         | Control-status taxonomy                                  | Inconsistent                    |
| F-048  | High         | Risk-report wording overstates operation                 | Overstated claim                |
| F-049  | Moderate     | Likelihood assessment horizon                            | Missing rationale               |
| F-050  | Moderate     | KPI/KRI measurability                                    | Generic                         |
