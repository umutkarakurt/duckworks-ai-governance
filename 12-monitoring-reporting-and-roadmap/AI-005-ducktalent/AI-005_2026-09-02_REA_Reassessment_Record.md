# AI-005 DuckTalent — Synthetic Reassessment Record IR-001

| **Field** | **Value** |
|---|---|
| **Document ID** | DW-DT-REA-01 |
| **Review ID** | IR-001 |
| **Version / date** | 1.0 / 2 September 2026 |
| **AI system** | AI-005 — DuckTalent AI |
| **Trigger** | Proposed material ranking / feature-set change |
| **Trigger evidence** | `DT-MON-001` / `DT-TRG-001` |
| **Prior lifecycle decision** | DENIED — maintain DO NOT DEPLOY with real applicants |
| **Current residual risk before reassessment** | Critical (20) |
| **Evidence confidence** | Low |
| **Classification** | Portfolio / Synthetic / Non-production |

> **Boundary.** This is a synthetic targeted reassessment. No real applicant, production model, real complaint, real monitoring telemetry, or real committee event is represented.

## 1. Trigger

`DT-CHG-001` proposes a synthetic ranking-configuration change that reintroduces `Career_Gap_Months` as a scoring penalty.

The executable change-regression monitor detects:

- a material feature/ranking-logic change;
- a feature outside the approved synthetic feature allow-list;
- non-zero matched-pair score differences;
- a group-level selection-rate difference in the synthetic test population; and
- a requirement to reopen lifecycle review.

The change therefore meets the DuckTalent event-driven reassessment rule.

## 2. Why reassessment is required

The DuckTalent iterative-review plan identifies the following as material triggers:

- change in ranking logic or feature set;
- material configuration change;
- fairness signal or unequal effect;
- control failure / ineffective mitigation; and
- any change that may invalidate prior assessment evidence.

This event engages several of those categories simultaneously.

## 3. Records reopened

| **Record / area** | **Reason reopened** | **Reassessment conclusion** |
|---|---|---|
| `AI-005-R01` — Fundamental rights & fairness | Proposed feature can recreate disadvantage among otherwise matched synthetic applicants. | Current Critical system risk remains appropriate; no reduction is justified. |
| `DT-01` — Job-Relevance Criteria & Proxy Feature Governance | Proposed feature is outside the approved synthetic allow-list. | Remains **Not Implemented** for production; change must not proceed without real criteria/feature governance. |
| `DT-02` — Pre-Deployment Fairness & Adverse-Impact Testing | Regression test is required after material feature/ranking change. | Synthetic control remains **Partially Implemented** and successfully detects the proposed regression. |
| DuckTalent AIA | Fairness, affected-person and non-linear-career impacts are implicated. | Existing DO NOT DEPLOY conclusion remains valid. |
| DuckTalent FRIA / HUDERIA | Equality/fairness rights analysis and mitigation effectiveness are implicated. | Blocking rights/fairness evidence remains incomplete; preserve block. |
| DuckTalent DPIA | Profiling/fairness-data implications remain relevant to any production design. | No new lawful-basis or real-data conclusion; existing open actions remain. |
| Model documentation | Feature/criteria logic is a material model/system documentation element. | Proposed synthetic configuration is not an approved production configuration; production model/version remains TBD. |
| Governance gate decision | Material new evidence must be tested against the prior gate. | Prior non-approval remains valid and the proposed change is explicitly rejected. |

## 4. Risk and evidence conclusion

The monitoring event does **not** justify changing the system-level risk score.

DuckTalent remains:

- **Current residual risk:** Critical (20)
- **System control effectiveness:** Not Implemented
- **Evidence confidence:** Low
- **DT-01:** Not Implemented
- **DT-02:** Partially Implemented within the synthetic portfolio boundary
- **Governance gate:** Do not deploy in current state

No production exposure occurred because the change is synthetic and unapproved.

The appropriate treatment is therefore **preventive rejection of the proposed change**, not post-harm remediation.

## 5. Mitigation-effectiveness conclusion

The prior DT-02 remediation removed the unapproved feature in the worked fairness test.

This reassessment shows why remediation must be coupled with change controls:

> A remediation is not durable if a later configuration change can silently reintroduce the same risk condition.

Required next-state governance design:

1. version-control the approved job criteria / feature allow-list;
2. require feature/ranking diffs for material changes;
3. trigger DT-02 regression on every material scoring/feature change;
4. block progression when an unapproved feature appears;
5. retain change-test and approval evidence;
6. reopen risk/impact/privacy/rights records when the change is material.

These are portfolio design conclusions, not claims that production change controls currently operate.

## 6. Reassessment decision

**IR-001 outcome: prior gate preserved; proposed change rejected.**

The new evidence does not support loosening the gate.

Instead, it confirms an additional explicit condition:

**No proposed ranking/feature configuration may progress unless the feature set is traceable to approved job criteria and the required regression evidence passes within the authorized governance boundary.**

## 7. Next review trigger

Reassessment should occur again when either:

- a materially revised evidence pack addresses the existing blocking conditions;
- a new model/provider/version/configuration/data/population/purpose change is proposed;
- a new synthetic or future real fairness/rights/security/oversight signal is detected; or
- evidence expiry/control failure requires renewed review.

**Evidence maturity:**  
**Synthetic trigger detected → Targeted reassessment performed → Prior risk/gate conclusion revalidated**
