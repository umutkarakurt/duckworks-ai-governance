# Duckworks AI Risk Scenario Register

**Project:** W.I.N.G. — Workflows, Intelligence, Next-Generation Governance  
**Document ID:** DW-AIRR-001  
**Version:** 1.1  
**Effective date:** 7 September 2026  
**Owner:** AI Governance Lead  
**Approval status:** Portfolio draft — fictional approval not recorded  
**Evidence reconciliation snapshot:** `e734ea64d6a9e5db35b59c4855e832aa433b43ad`  
**Supersedes:** Duckworks_AI_Risk_Scenarios_v1.0.md

> Duckworks and all operating records are fictional or synthetic. Scores are retained for traceability and do not demonstrate legal compliance, ISO/IEC 42001 conformity, production effectiveness or independently validated risk reduction.

## 1. Purpose and controlling interpretation

This register preserves the original 21 scenario scores while adding the evidence maturity required to interpret each current-residual reduction. A lower recorded current score cannot relax a lifecycle gate unless the credited control evidence is appropriate to the operating context and accepted by the authorized risk owner.

### Decision rules

1. Synthetic evidence demonstrates only the bounded portfolio exercise described by the artifact.
2. A reduction without linked operating evidence is unsupported pending reassessment.
3. A reduction supported only by synthetic evidence is provisional and receives no production risk-reduction credit.
4. If current residual equals inherent risk, no reduction is claimed even when synthetic evidence exists.
5. Target residual is a treatment objective, not evidence of achieved performance.
6. Existing restrictive gates remain in force. For production authorization, use inherent risk conservatively until sufficient evidence is accepted.
7. AI-007 is an organizational discovery and containment condition, not one homogeneous AI system.

## 2. Portfolio decision summary

| AI ID | System or condition | Risk owner | Original effectiveness / confidence | Reconciled evidence maturity | Reconciled confidence | Current gate | Required next action |
|---|---|---|---|---|---|---|---|
| AI-001 | DuckDesign AI | Felix Duckson - VP Product & Engineering | Partially Effective / Medium | Design/status assertions only; operating effectiveness not evidenced | Low | Restricted pilot only | Produce approval, validation, version and exception records. |
| AI-002 | QuackBot | Clara Duckley - Director Customer Operations | Partially Effective / Low-Medium | Design/status assertions only; operating effectiveness not evidenced | Low | Production blocked pending gates | Produce adversarial/RAG, grounding, escalation and impact evidence. |
| AI-003 | FeatherForecast | Tobias Duckman - Director Supply Chain | Effective / High | Unverified — production-effectiveness evidence not inspected | Low pending retrieval | Continue with monitoring | Retrieve defined-period monitoring, back-test, approval/override, data-quality and change records; reassess if unavailable. |
| AI-004 | WingInspect Vision | Henrietta Duckwell - Director Manufacturing | Partially Effective / Medium | WI-01 synthetic operation tested; production effectiveness unverified | Medium for synthetic workflow / Low for production | Restricted pilot only | Add production inspection authorizations and defect-escape/false-negative outcomes. |
| AI-005 | DuckTalent AI | Beatrice Van Duck - Chief People Officer | Not Implemented / Low | DT-02 synthetic operation tested; critical blockers remain | Medium for synthetic testing / Low for production readiness | Do not deploy in current state | Close privacy, rights, oversight, accessibility, security, vendor and production-validation blockers. |
| AI-006 | PondGPT | Oliver Duckett - Head of IT & Cloud | Partially Effective / Medium | PG-02 synthetic operation tested; production effectiveness unverified | Medium for synthetic workflow / Low for production | Restricted pilot only | Add production permission, connector, DLP/SIEM and regression evidence. |
| AI-007 | Unregistered GenAI Usage | Reginald Duckman - CRCO / business owners by discovered use | Weak / Low | Organizational discovery and containment condition; homogeneous effectiveness rating is invalid | Low | Immediate containment and decomposition | Discover, contain and decompose identified uses into separately owned inventory and risk records. |

## 3. Scenario register

### AI-001-R01 — Safety & physical harm

| Field | Record |
|---|---|
| AI entry | AI-001 — DuckDesign AI |
| Risk owner | Felix Duckson - VP Product & Engineering |
| Cause | AI generates an incorrect or hallucinated engineering recommendation. |
| Event | The recommendation is accepted and incorporated into a design. |
| Impact | An unsafe design progresses toward prototyping or production, creating product-safety harm or costly rework. |
| Inherent risk | Severity 5 x Likelihood 3 = 15 High |
| Existing controls recorded in v1.0 | Mandatory engineer approval; pilot restrictions; output validation. |
| Mapped control IDs | AI-GOV-01; AI-GOV-02; AI-INC-01; DD-01; DD-02; DD-03; DD-05 |
| Recorded current residual | Severity 5 x Likelihood 2 = 10 High |
| Target treatment | Independent validation criteria; safety test gates; version/change control; documented design traceability. |
| Target residual | Severity 4 x Likelihood 2 = 8 Moderate |
| Available evidence IDs | None linked |
| Evidence maturity | No linked evidence |
| Score-support status | Unsupported reduction — evidence ID absent |
| Evidence conclusion | The recorded current residual is lower than inherent risk without retrievable operating evidence linked to the scenario. |
| Production decision basis | Do not use the lower score to relax the lifecycle gate; use inherent risk until reassessment. |
| Lifecycle gate | Restricted pilot only |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

### AI-001-R02 — Privacy & data governance

| Field | Record |
|---|---|
| AI entry | AI-001 — DuckDesign AI |
| Risk owner | Felix Duckson - VP Product & Engineering |
| Cause | Proprietary CAD files or specifications are provided to an external model or service. |
| Event | The information is exposed, retained, reused, or accessed outside the approved Duckworks boundary. |
| Impact | Duckworks intellectual property or confidential engineering information is disclosed or reused. |
| Inherent risk | Severity 4 x Likelihood 3 = 12 High |
| Existing controls recorded in v1.0 | Tenant isolation; restricted access; approved data scope. |
| Mapped control IDs | AI-GOV-02; AI-TPR-01; AI-INC-01; DD-04 |
| Recorded current residual | Severity 4 x Likelihood 2 = 8 Moderate |
| Target treatment | Contractual no-training terms; DLP; confidential-data controls; vendor evidence review. |
| Target residual | Severity 4 x Likelihood 1 = 4 Low |
| Available evidence IDs | None linked |
| Evidence maturity | No linked evidence |
| Score-support status | Unsupported reduction — evidence ID absent |
| Evidence conclusion | The recorded current residual is lower than inherent risk without retrievable operating evidence linked to the scenario. |
| Production decision basis | Do not use the lower score to relax the lifecycle gate; use inherent risk until reassessment. |
| Lifecycle gate | Restricted pilot only |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

### AI-001-R03 — Reliability & robustness

| Field | Record |
|---|---|
| AI entry | AI-001 — DuckDesign AI |
| Risk owner | Felix Duckson - VP Product & Engineering |
| Cause | AI generates technically plausible but incorrect material or specification values. |
| Event | Engineers rely on the incorrect values as design assumptions. |
| Impact | Design defects, failed validation, rework, or downstream quality issues occur. |
| Inherent risk | Severity 4 x Likelihood 4 = 16 High |
| Existing controls recorded in v1.0 | Human review; simulation checks. |
| Mapped control IDs | AI-GOV-02; DD-01; DD-03; DD-05 |
| Recorded current residual | Severity 4 x Likelihood 2 = 8 Moderate |
| Target treatment | Versioned benchmark suite; grounded engineering sources; fail-safe validation; monitoring of override and validation failures. |
| Target residual | Severity 4 x Likelihood 2 = 8 Moderate |
| Available evidence IDs | None linked |
| Evidence maturity | No linked evidence |
| Score-support status | Unsupported reduction — evidence ID absent |
| Evidence conclusion | The recorded current residual is lower than inherent risk without retrievable operating evidence linked to the scenario. |
| Production decision basis | Do not use the lower score to relax the lifecycle gate; use inherent risk until reassessment. |
| Lifecycle gate | Restricted pilot only |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

### AI-002-R01 — Reliability & robustness

| Field | Record |
|---|---|
| AI entry | AI-002 — QuackBot |
| Risk owner | Clara Duckley - Director Customer Operations |
| Cause | QuackBot hallucinates troubleshooting, warranty, or product-support information. |
| Event | A customer receives and acts on the incorrect guidance. |
| Impact | Customer harm, complaints, warranty disputes, liability, or loss of trust may result. |
| Inherent risk | Severity 4 x Likelihood 4 = 16 High |
| Existing controls recorded in v1.0 | Escalation rules; source allowlist; draft safety filters. |
| Mapped control IDs | AI-GOV-01; QB-01; QB-02; QB-03; QB-06 |
| Recorded current residual | Severity 4 x Likelihood 3 = 12 High |
| Target treatment | Pre-release evaluations; grounding/citation checks; constrained answers for high-impact topics; human escalation SLA. |
| Target residual | Severity 4 x Likelihood 2 = 8 Moderate |
| Available evidence IDs | None linked |
| Evidence maturity | No linked evidence |
| Score-support status | Unsupported reduction — evidence ID absent |
| Evidence conclusion | The recorded current residual is lower than inherent risk without retrievable operating evidence linked to the scenario. |
| Production decision basis | Do not use the lower score to relax the lifecycle gate; use inherent risk until reassessment. |
| Lifecycle gate | Production blocked pending gates |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

### AI-002-R02 — Security & adversarial manipulation

| Field | Record |
|---|---|
| AI entry | AI-002 — QuackBot |
| Risk owner | Clara Duckley - Director Customer Operations |
| Cause | A malicious prompt or poisoned source content manipulates retrieval or tool behavior. |
| Event | QuackBot retrieves restricted information, follows malicious instructions, or produces unsafe guidance. |
| Impact | Sensitive data may be exposed and customers or systems may be adversely affected. |
| Inherent risk | Severity 4 x Likelihood 4 = 16 High |
| Existing controls recorded in v1.0 | Least-privilege retrieval design; authentication; draft filters. |
| Mapped control IDs | AI-TPR-01; AI-INC-01; QB-04; QB-05; QB-06 |
| Recorded current residual | Severity 4 x Likelihood 3 = 12 High |
| Target treatment | Adversarial testing; content isolation; tool-permission boundaries; injection monitoring; red-team regression suite. |
| Target residual | Severity 4 x Likelihood 2 = 8 Moderate |
| Available evidence IDs | None linked |
| Evidence maturity | No linked evidence |
| Score-support status | Unsupported reduction — evidence ID absent |
| Evidence conclusion | The recorded current residual is lower than inherent risk without retrievable operating evidence linked to the scenario. |
| Production decision basis | Do not use the lower score to relax the lifecycle gate; use inherent risk until reassessment. |
| Lifecycle gate | Production blocked pending gates |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

### AI-002-R03 — Legal / compliance

| Field | Record |
|---|---|
| AI entry | AI-002 — QuackBot |
| Risk owner | Clara Duckley - Director Customer Operations |
| Cause | The chatbot generates incorrect warranty or consumer-rights statements. |
| Event | The incorrect statement is presented to a customer as authoritative Duckworks guidance. |
| Impact | Customers receive misleading information, creating legal, contractual, complaint, or reputational consequences. |
| Inherent risk | Severity 3 x Likelihood 4 = 12 High |
| Existing controls recorded in v1.0 | Knowledge-base allowlist; escalation. |
| Mapped control IDs | AI-GOV-01; QB-01; QB-02; QB-03 |
| Recorded current residual | Severity 3 x Likelihood 3 = 9 Moderate |
| Target treatment | Approved legal content; response templates for regulated topics; confidence/abstention rules. |
| Target residual | Severity 3 x Likelihood 2 = 6 Moderate |
| Available evidence IDs | None linked |
| Evidence maturity | No linked evidence |
| Score-support status | Unsupported reduction — evidence ID absent |
| Evidence conclusion | The recorded current residual is lower than inherent risk without retrievable operating evidence linked to the scenario. |
| Production decision basis | Do not use the lower score to relax the lifecycle gate; use inherent risk until reassessment. |
| Lifecycle gate | Production blocked pending gates |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

### AI-003-R01 — Operational / financial

| Field | Record |
|---|---|
| AI entry | AI-003 — FeatherForecast |
| Risk owner | Tobias Duckman - Director Supply Chain |
| Cause | The forecasting model materially underestimates or overestimates demand. |
| Event | Procurement, inventory, or production planning decisions are made using the inaccurate forecast. |
| Impact | Duckworks experiences stockouts, excess inventory, production inefficiency, service impact, or avoidable cost. |
| Inherent risk | Severity 3 x Likelihood 3 = 9 Moderate |
| Existing controls recorded in v1.0 | Human planning approval; back-testing; overrides. |
| Mapped control IDs | FF-01; FF-02 |
| Recorded current residual | Severity 3 x Likelihood 2 = 6 Moderate |
| Target treatment | Stress testing; scenario ranges; exception thresholds; periodic recalibration. |
| Target residual | Severity 3 x Likelihood 1 = 3 Low |
| Available evidence IDs | None linked |
| Evidence maturity | No linked evidence |
| Score-support status | Unsupported reduction — evidence ID absent |
| Evidence conclusion | The recorded current residual is lower than inherent risk without retrievable operating evidence linked to the scenario. |
| Production decision basis | Do not use the lower score to relax the lifecycle gate; use inherent risk until reassessment. |
| Lifecycle gate | Continue with monitoring |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

### AI-003-R02 — Reliability & robustness

| Field | Record |
|---|---|
| AI entry | AI-003 — FeatherForecast |
| Risk owner | Tobias Duckman - Director Supply Chain |
| Cause | Market or supplier conditions change materially from the model's historical operating context. |
| Event | Model drift is not detected or addressed promptly. |
| Impact | Degraded forecasts persist and repeatedly influence planning decisions. |
| Inherent risk | Severity 3 x Likelihood 3 = 9 Moderate |
| Existing controls recorded in v1.0 | Monthly drift review; performance monitoring. |
| Mapped control IDs | AI-GOV-02; FF-02; FF-03 |
| Recorded current residual | Severity 3 x Likelihood 2 = 6 Moderate |
| Target treatment | Automated drift alerts; challenger model; defined retraining trigger. |
| Target residual | Severity 3 x Likelihood 1 = 3 Low |
| Available evidence IDs | None linked |
| Evidence maturity | No linked evidence |
| Score-support status | Unsupported reduction — evidence ID absent |
| Evidence conclusion | The recorded current residual is lower than inherent risk without retrievable operating evidence linked to the scenario. |
| Production decision basis | Do not use the lower score to relax the lifecycle gate; use inherent risk until reassessment. |
| Lifecycle gate | Continue with monitoring |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

### AI-003-R03 — Privacy & data governance

| Field | Record |
|---|---|
| AI entry | AI-003 — FeatherForecast |
| Risk owner | Tobias Duckman - Director Supply Chain |
| Cause | Supplier or confidential planning data is made accessible through analytics integrations or overly broad access. |
| Event | An unauthorized person or system obtains commercially sensitive information. |
| Impact | Supplier confidentiality, commercial position, or Duckworks internal planning information is compromised. |
| Inherent risk | Severity 3 x Likelihood 2 = 6 Moderate |
| Existing controls recorded in v1.0 | Private cloud; role-based access. |
| Mapped control IDs | FF-04; AI-INC-01 |
| Recorded current residual | Severity 3 x Likelihood 1 = 3 Low |
| Target treatment | Periodic access review; encryption; logging; supplier-data minimization. |
| Target residual | Severity 3 x Likelihood 1 = 3 Low |
| Available evidence IDs | None linked |
| Evidence maturity | No linked evidence |
| Score-support status | Unsupported reduction — evidence ID absent |
| Evidence conclusion | The recorded current residual is lower than inherent risk without retrievable operating evidence linked to the scenario. |
| Production decision basis | Do not use the lower score to relax the lifecycle gate; use inherent risk until reassessment. |
| Lifecycle gate | Continue with monitoring |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

### AI-004-R01 — Safety & physical harm

| Field | Record |
|---|---|
| AI entry | AI-004 — WingInspect Vision |
| Risk owner | Henrietta Duckwell - Director Manufacturing |
| Cause | The vision model fails to detect a true product defect. |
| Event | A defective component is not flagged and progresses through the quality process. |
| Impact | An unsafe or defective product could progress toward release, creating physical or product-safety harm. |
| Inherent risk | Severity 5 x Likelihood 3 = 15 High |
| Existing controls recorded in v1.0 | Mandatory human final inspection; pilot limited to non-safety-critical line. |
| Mapped control IDs | AI-GOV-01; AI-INC-01; WI-01; WI-02; WI-03; WI-04 |
| Recorded current residual | Severity 5 x Likelihood 2 = 10 High |
| Target treatment | Validated minimum sensitivity; safety case; independent QA sampling; fail-safe/manual fallback. |
| Target residual | Severity 5 x Likelihood 1 = 5 Moderate |
| Available evidence IDs | EV-AI004-001; EV-AI004-002; EV-AI004-003 |
| Evidence maturity | Designed; Synthetic execution demonstrated; Synthetic operation tested |
| Score-support status | Provisional reduction — synthetic evidence only |
| Evidence conclusion | A bounded synthetic demonstration is linked, but sustained production operation and outcomes are not evidenced. |
| Production decision basis | Use inherent risk for production authorization until evidence is accepted by the authorized risk owner. |
| Lifecycle gate | Restricted pilot only |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

### AI-004-R02 — Operational / financial

| Field | Record |
|---|---|
| AI entry | AI-004 — WingInspect Vision |
| Risk owner | Henrietta Duckwell - Director Manufacturing |
| Cause | The model produces excessive false-positive defect alerts. |
| Event | Good components are incorrectly flagged and held, scrapped, or reworked. |
| Impact | Manufacturing cost, waste, delay, and inspector workload increase. |
| Inherent risk | Severity 3 x Likelihood 4 = 12 High |
| Existing controls recorded in v1.0 | Human inspector confirmation. |
| Mapped control IDs | WI-01; WI-05 |
| Recorded current residual | Severity 3 x Likelihood 2 = 6 Moderate |
| Target treatment | Threshold tuning; cost-weighted evaluation; feedback loop with QA. |
| Target residual | Severity 3 x Likelihood 1 = 3 Low |
| Available evidence IDs | None linked |
| Evidence maturity | No linked evidence |
| Score-support status | Unsupported reduction — evidence ID absent |
| Evidence conclusion | The recorded current residual is lower than inherent risk without retrievable operating evidence linked to the scenario. |
| Production decision basis | Do not use the lower score to relax the lifecycle gate; use inherent risk until reassessment. |
| Lifecycle gate | Restricted pilot only |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

### AI-004-R03 — Reliability & robustness

| Field | Record |
|---|---|
| AI entry | AI-004 — WingInspect Vision |
| Risk owner | Henrietta Duckwell - Director Manufacturing |
| Cause | Camera, lighting, product-line, or component characteristics change from the validated baseline. |
| Event | Distribution shift degrades model detection performance without timely revalidation. |
| Impact | Defect escape rates increase and confidence in the inspection control becomes unreliable. |
| Inherent risk | Severity 4 x Likelihood 3 = 12 High |
| Existing controls recorded in v1.0 | Performance by product line; camera monitoring. |
| Mapped control IDs | AI-GOV-02; WI-03; WI-06 |
| Recorded current residual | Severity 4 x Likelihood 2 = 8 Moderate |
| Target treatment | Change-triggered revalidation; automated drift detection; locked deployment baselines. |
| Target residual | Severity 4 x Likelihood 1 = 4 Low |
| Available evidence IDs | None linked |
| Evidence maturity | No linked evidence |
| Score-support status | Unsupported reduction — evidence ID absent |
| Evidence conclusion | The recorded current residual is lower than inherent risk without retrievable operating evidence linked to the scenario. |
| Production decision basis | Do not use the lower score to relax the lifecycle gate; use inherent risk until reassessment. |
| Lifecycle gate | Restricted pilot only |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

### AI-005-R01 — Fundamental rights & fairness

| Field | Record |
|---|---|
| AI entry | AI-005 — DuckTalent AI |
| Risk owner | Beatrice Van Duck - Chief People Officer |
| Cause | Training data, features, criteria, or proxy variables encode historical or structural bias. |
| Event | DuckTalent systematically ranks members of a protected or otherwise disadvantaged group lower. |
| Impact | Applicants experience discriminatory or unfair restriction of access to employment, with associated legal and reputational harm. |
| Inherent risk | Severity 5 x Likelihood 4 = 20 Critical |
| Existing controls recorded in v1.0 | No implemented control; concept-stage principles only. |
| Mapped control IDs | AI-GOV-01; AI-TPR-01; DT-01; DT-02; DT-07 |
| Recorded current residual | Severity 5 x Likelihood 4 = 20 Critical |
| Target treatment | Legal review; job-relevance controls; representative testing; fairness metrics; adverse-impact investigation; challenge process. |
| Target residual | Severity 5 x Likelihood 2 = 10 High |
| Available evidence IDs | EV-AI005-001; EV-AI005-002; EV-AI005-003; EV-AI005-004; EV-AI005-005; EV-AI005-006; EV-AI005-009; EV-AI005-010; EV-AI005-011; EV-AI005-012; EV-AI005-013; EV-AI005-014 |
| Evidence maturity | Designed; Designed test input; Synthetic technical implementation demonstrated; Synthetic fairness execution demonstrated; Synthetic failure detection / gate response demonstrated; Synthetic operation tested; Synthetic lifecycle decision demonstrated; Synthetic material-change input; Synthetic monitoring mechanism demonstrated; Synthetic reassessment trigger demonstrated; Synthetic reassessment performed; Synthetic revised lifecycle decision demonstrated |
| Score-support status | No reduction claimed |
| Evidence conclusion | Recorded current residual equals inherent risk. Available synthetic evidence may demonstrate workflow behavior but does not establish validated effectiveness. |
| Production decision basis | Use the recorded current/inherent position and preserve the existing gate. |
| Lifecycle gate | Do not deploy in current state |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

### AI-005-R02 — Human oversight & automation bias

| Field | Record |
|---|---|
| AI entry | AI-005 — DuckTalent AI |
| Risk owner | Beatrice Van Duck - Chief People Officer |
| Cause | Recruiters place excessive trust in AI rankings or summaries. |
| Event | A flawed recommendation becomes the de facto screening or selection decision despite nominal human review. |
| Impact | Qualified candidates are unfairly screened out and human accountability becomes ineffective. |
| Inherent risk | Severity 4 x Likelihood 4 = 16 High |
| Existing controls recorded in v1.0 | Planned human review; no-automated-rejection principle not yet implemented. |
| Mapped control IDs | AI-GOV-01; DT-03; DT-04; DT-07 |
| Recorded current residual | Severity 4 x Likelihood 4 = 16 High |
| Target treatment | Human-oversight procedure; forced rationale; no automated rejection; reviewer training; override and appeal monitoring. |
| Target residual | Severity 4 x Likelihood 2 = 8 Moderate |
| Available evidence IDs | None linked |
| Evidence maturity | No linked evidence |
| Score-support status | No reduction claimed |
| Evidence conclusion | Recorded current residual equals inherent risk. Available synthetic evidence may demonstrate workflow behavior but does not establish validated effectiveness. |
| Production decision basis | Use the recorded current/inherent position and preserve the existing gate. |
| Lifecycle gate | Do not deploy in current state |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

### AI-005-R03 — Privacy & data governance

| Field | Record |
|---|---|
| AI entry | AI-005 — DuckTalent AI |
| Risk owner | Beatrice Van Duck - Chief People Officer |
| Cause | CV or application data contains sensitive attributes or proxy information beyond what is necessary for recruitment. |
| Event | The system infers, processes, or uses those attributes in ranking, summarization, or recommendations. |
| Impact | Applicants face privacy intrusion, inappropriate profiling, discrimination exposure, or inability to understand/correct the use of their data. |
| Inherent risk | Severity 4 x Likelihood 3 = 12 High |
| Existing controls recorded in v1.0 | No production data; vendor not selected. |
| Mapped control IDs | AI-TPR-01; AI-INC-01; DT-05; DT-06 |
| Recorded current residual | Severity 4 x Likelihood 3 = 12 High |
| Target treatment | Data minimization; field exclusion; DPIA/privacy review; vendor restrictions; retention controls. |
| Target residual | Severity 4 x Likelihood 2 = 8 Moderate |
| Available evidence IDs | None linked |
| Evidence maturity | No linked evidence |
| Score-support status | No reduction claimed |
| Evidence conclusion | Recorded current residual equals inherent risk. Available synthetic evidence may demonstrate workflow behavior but does not establish validated effectiveness. |
| Production decision basis | Use the recorded current/inherent position and preserve the existing gate. |
| Lifecycle gate | Do not deploy in current state |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

### AI-006-R01 — Privacy & data governance

| Field | Record |
|---|---|
| AI entry | AI-006 — PondGPT |
| Risk owner | Oliver Duckett - Head of IT & Cloud |
| Cause | Retrieval permissions or connector authorization are configured incorrectly. |
| Event | PondGPT returns restricted internal information to a user who is not authorized to access the underlying source. |
| Impact | Sensitive IP, customer data, employee information, or other confidential content is disclosed across access boundaries. |
| Inherent risk | Severity 4 x Likelihood 4 = 16 High |
| Existing controls recorded in v1.0 | SSO; source authorization inheritance; restricted pilot repositories. |
| Mapped control IDs | AI-TPR-01; AI-INC-01; PG-01; PG-02; PG-05 |
| Recorded current residual | Severity 4 x Likelihood 3 = 12 High |
| Target treatment | Automated permission-regression tests; DLP; sensitive-source denylist; logging and alerting. |
| Target residual | Severity 4 x Likelihood 2 = 8 Moderate |
| Available evidence IDs | EV-AI006-001; EV-AI006-002; EV-AI006-003; EV-AI006-004; EV-AI006-005; EV-AI006-006 |
| Evidence maturity | Designed; Designed test input; Synthetic technical implementation demonstrated; Synthetic technical execution demonstrated; Synthetic failure detection / containment demonstrated; Synthetic operation tested |
| Score-support status | Provisional reduction — synthetic evidence only |
| Evidence conclusion | A bounded synthetic demonstration is linked, but sustained production operation and outcomes are not evidenced. |
| Production decision basis | Use inherent risk for production authorization until evidence is accepted by the authorized risk owner. |
| Lifecycle gate | Restricted pilot only |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

### AI-006-R02 — Security & adversarial manipulation

| Field | Record |
|---|---|
| AI entry | AI-006 — PondGPT |
| Risk owner | Oliver Duckett - Head of IT & Cloud |
| Cause | A malicious prompt or poisoned retrieved document contains instructions intended to manipulate the assistant. |
| Event | The assistant follows the malicious instruction, exposes data, produces unsafe output, or misuses an integrated tool. |
| Impact | Confidentiality, integrity, code security, or business operations are compromised. |
| Inherent risk | Severity 4 x Likelihood 4 = 16 High |
| Existing controls recorded in v1.0 | Restricted connectors; logging; pilot controls. |
| Mapped control IDs | AI-INC-01; PG-03; PG-04; PG-05 |
| Recorded current residual | Severity 4 x Likelihood 3 = 12 High |
| Target treatment | Injection testing; content provenance; tool sandboxing; allowlisted actions; response monitoring. |
| Target residual | Severity 4 x Likelihood 2 = 8 Moderate |
| Available evidence IDs | None linked |
| Evidence maturity | No linked evidence |
| Score-support status | Unsupported reduction — evidence ID absent |
| Evidence conclusion | The recorded current residual is lower than inherent risk without retrievable operating evidence linked to the scenario. |
| Production decision basis | Do not use the lower score to relax the lifecycle gate; use inherent risk until reassessment. |
| Lifecycle gate | Restricted pilot only |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

### AI-006-R03 — Reliability & robustness

| Field | Record |
|---|---|
| AI entry | AI-006 — PondGPT |
| Risk owner | Oliver Duckett - Head of IT & Cloud |
| Cause | PondGPT generates hallucinated code or incorrect operational guidance. |
| Event | An employee uses the output without adequate verification. |
| Impact | Vulnerable code, erroneous configuration, incorrect business action, or operational disruption is introduced. |
| Inherent risk | Severity 4 x Likelihood 3 = 12 High |
| Existing controls recorded in v1.0 | Mandatory user responsibility; pilot guidance. |
| Mapped control IDs | PG-05; PG-06 |
| Recorded current residual | Severity 4 x Likelihood 3 = 12 High |
| Target treatment | Secure-code scanning; human review for consequential outputs; source grounding; user training. |
| Target residual | Severity 4 x Likelihood 2 = 8 Moderate |
| Available evidence IDs | None linked |
| Evidence maturity | No linked evidence |
| Score-support status | No reduction claimed |
| Evidence conclusion | Recorded current residual equals inherent risk. Available synthetic evidence may demonstrate workflow behavior but does not establish validated effectiveness. |
| Production decision basis | Use the recorded current/inherent position and preserve the existing gate. |
| Lifecycle gate | Restricted pilot only |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

### AI-007-R01 — Privacy & data governance

| Field | Record |
|---|---|
| AI entry | AI-007 — Unregistered GenAI Usage |
| Risk owner | Reginald Duckman - CRCO / business owners by discovered use |
| Cause | An employee uploads confidential, IP, customer, HR, source-code, or personal data to an unapproved public AI service. |
| Event | The provider retains, trains on, transfers, or otherwise exposes the information outside Duckworks' approved control boundary. |
| Impact | Confidentiality, privacy, intellectual-property, contractual, or incident-response consequences arise. |
| Inherent risk | Severity 5 x Likelihood 4 = 20 Critical |
| Existing controls recorded in v1.0 | Limited awareness; no consistent technical enforcement. |
| Mapped control IDs | AI-INC-01; SH-01; SH-02; SH-03; SH-04; SH-06 |
| Recorded current residual | Severity 5 x Likelihood 4 = 20 Critical |
| Target treatment | Approved-tool catalogue; DLP/CASB/SSE discovery; blocking; awareness; exception workflow. |
| Target residual | Severity 5 x Likelihood 2 = 10 High |
| Available evidence IDs | None linked |
| Evidence maturity | No linked evidence |
| Score-support status | No reduction claimed |
| Evidence conclusion | Recorded current residual equals inherent risk. Available synthetic evidence may demonstrate workflow behavior but does not establish validated effectiveness. |
| Production decision basis | Use the recorded current/inherent position and preserve the existing gate. |
| Lifecycle gate | Immediate containment and decomposition |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

### AI-007-R02 — Legal / compliance

| Field | Record |
|---|---|
| AI entry | AI-007 — Unregistered GenAI Usage |
| Risk owner | Reginald Duckman - CRCO / business owners by discovered use |
| Cause | Unregistered AI is introduced into HR, customer, engineering, or another consequential process without governance intake. |
| Event | Applicable legal, regulatory, contractual, policy, or human-oversight requirements are not identified before outputs are relied upon. |
| Impact | Duckworks operates unlawful or uncontrolled decision support and cannot demonstrate appropriate accountability or evidence. |
| Inherent risk | Severity 5 x Likelihood 3 = 15 High |
| Existing controls recorded in v1.0 | No centralized inventory or control over the individual use cases. |
| Mapped control IDs | AI-GOV-01; SH-01; SH-05; SH-06 |
| Recorded current residual | Severity 5 x Likelihood 3 = 15 High |
| Target treatment | Mandatory registration; periodic attestations; manager accountability; risk-based approval before consequential use. |
| Target residual | Severity 5 x Likelihood 2 = 10 High |
| Available evidence IDs | None linked |
| Evidence maturity | No linked evidence |
| Score-support status | No reduction claimed |
| Evidence conclusion | Recorded current residual equals inherent risk. Available synthetic evidence may demonstrate workflow behavior but does not establish validated effectiveness. |
| Production decision basis | Use the recorded current/inherent position and preserve the existing gate. |
| Lifecycle gate | Immediate containment and decomposition |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

### AI-007-R03 — Third-party & supply chain

| Field | Record |
|---|---|
| AI entry | AI-007 — Unregistered GenAI Usage |
| Risk owner | Reginald Duckman - CRCO / business owners by discovered use |
| Cause | Employees use unknown public AI vendors, browser extensions, plugins, or embedded AI features with unreviewed terms. |
| Event | Company data is processed under unknown retention, training, security, subprocessor, or service-change conditions. |
| Impact | Unmanaged third-party exposure persists and Duckworks lacks contractual leverage, assurance evidence, incident visibility, or exit controls. |
| Inherent risk | Severity 4 x Likelihood 4 = 16 High |
| Existing controls recorded in v1.0 | Ad hoc browser/security controls. |
| Mapped control IDs | AI-TPR-01; SH-02; SH-04; SH-06 |
| Recorded current residual | Severity 4 x Likelihood 4 = 16 High |
| Target treatment | Vendor allowlist; extension controls; procurement gate; contractual, privacy, and security review. |
| Target residual | Severity 4 x Likelihood 2 = 8 Moderate |
| Available evidence IDs | None linked |
| Evidence maturity | No linked evidence |
| Score-support status | No reduction claimed |
| Evidence conclusion | Recorded current residual equals inherent risk. Available synthetic evidence may demonstrate workflow behavior but does not establish validated effectiveness. |
| Production decision basis | Use the recorded current/inherent position and preserve the existing gate. |
| Lifecycle gate | Immediate containment and decomposition |
| Evidence period | Not established in the repository evidence set |
| Reviewer status | Open — authorized risk-owner acceptance not recorded |
| Reassessment trigger | Material model/data/configuration/vendor/use change; control failure; adverse outcome; evidence expiry; or inability to retrieve evidence supporting a current-residual reduction |

## 4. AI-007 organizational-risk treatment

AI-007 represents unregistered generative-AI usage across the organization. Its aggregate score is retained only as a historical prioritization signal. It must not be interpreted as a system-level assessment or authorization.

Required workflow: discover use → contain prohibited activity → identify owner and purpose → assign a new AI inventory ID → conduct intake and classification → assess system-specific risks → approve, restrict or prohibit the use → monitor closure.

## 5. Review and maintenance

The AI Governance Lead coordinates updates. Each risk owner remains accountable for accepting, treating, avoiding or escalating risk. Updates to a score must identify the evidence IDs, operating population and period, exceptions, reviewer and approval decision. The risk register, control framework, evidence index, AIMS crosswalk and management report must be updated together after a material decision.

**Next scheduled review:** After completion of P1 evidence actions or a material repository change, whichever occurs first.
