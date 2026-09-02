# AI-005 DuckTalent — DT-02 Fairness Control Test

| **Field** | **Value** |
|---|---|
| **Document ID** | DW-DT-DT02-TEST-01 |
| **Version / test date** | 1.0 / 2 September 2026 |
| **AI system** | AI-005 — DuckTalent AI |
| **Risk** | AI-005-R01 — Fundamental rights & fairness |
| **Preventive dependency** | DT-01 — Job-Relevance Criteria & Proxy Feature Governance |
| **Control tested** | DT-02 — Pre-Deployment Fairness & Adverse-Impact Testing |
| **Control owner** | Beatrice Van Duck — Chief People Officer |
| **Test population** | 24 synthetic applicants / 12 matched pairs |
| **Evidence classification** | Portfolio / Synthetic / Non-production |

## 1. Objective

Determine whether the worked `DT-02` process can detect an unapproved proxy-like scoring feature, show its measurable effect on otherwise matched synthetic applicants, block the pre-deployment gate, and verify remediation through a full-population retest.

## 2. Synthetic setup

Each matched pair has identical values for the approved job-related test features:

- relevant experience;
- skill match;
- qualification match; and
- required certification.

The deliberately defective pre-remediation configuration additionally penalizes `Career_Gap_Months`.

`Career_Gap_Months` is not on the synthetic approved-feature allow-list.

The `Reference` and `Comparison` labels are synthetic test labels only. They are not real protected characteristics and are not intended to represent a legal discrimination analysis.

## 3. Control assertions

The executable test evaluates ten control assertions:

1. the unapproved feature is detected;
2. the pre-remediation deployment gate is blocked;
3. group metrics are generated;
4. matched-pair score effects are detected;
5. remediation removes the unapproved feature;
6. post-remediation matched-pair scores are equal where approved job features are identical;
7. post-remediation selection rates are equal in the matched synthetic population;
8. post-remediation true-positive rates are equal in the matched synthetic population;
9. the remediation retest passes; and
10. a successful retest does **not** automatically approve deployment.

## 4. Results

The executable run produced:

- **24** synthetic applicants;
- **12** matched pairs;
- **10 / 10** expected control assertions passed;
- seeded unapproved feature detected: **Yes**;
- pre-remediation gate: **BLOCK**;
- post-remediation gate: **ELIGIBLE_FOR_FURTHER_GOVERNANCE_REVIEW**.

The generated run summary contains the exact group-level selection-rate and error metrics.

## 5. Why the pre-remediation test is a control success

The synthetic scoring configuration is intentionally defective.

The control is successful because it:

- identifies the use of an unapproved feature;
- quantifies its effect;
- prevents the configuration from progressing;
- creates an exception record;
- requires remediation; and
- retests the complete population.

The defective configuration itself is **not** treated as acceptable merely because the detective control found it.

## 6. Threshold and legal boundary

The script uses a synthetic shortlist threshold only to create deterministic screening outcomes for the portfolio demonstration.

It is not:

- a validated hiring threshold;
- a fairness threshold;
- an adverse-impact legal threshold;
- an EU AI Act requirement;
- an employment-law safe harbor; or
- evidence that a real system is fair.

No single ratio or metric is used to declare legal compliance or discrimination.

## 7. Control-test conclusion

**Assessment:** `DT-02 — Pre-Deployment Fairness & Adverse-Impact Testing` operated as designed **within the synthetic test population**.

The defensible evidence state is:

**Designed → Synthetic technical implementation demonstrated → Synthetic fairness execution demonstrated → Synthetic operation tested**

## 8. Assurance limitations

This result does **not** establish:

- real-applicant fairness;
- real protected-group outcomes;
- actual DuckTalent model behavior;
- actual job-relatedness of production features;
- lawful processing basis for fairness data;
- accessibility performance;
- actual candidate challenge/remedy effectiveness;
- sustained control operation;
- legal compliance;
- reduction of DuckTalent's current Critical residual risk; or
- independent assurance.

## 9. Production evidence required for stronger assurance

A real pre-deployment or operating-effectiveness conclusion would require evidence such as:

- approved job-analysis and job-relevance criteria;
- actual model/feature inventory and weighting/rule logic;
- lawful and governance-approved fairness-data method;
- representative test design;
- parsing/ranking accuracy evidence;
- subgroup and intersectional analysis where appropriate;
- accessibility testing;
- real version/configuration traceability;
- exception investigation;
- candidate notice/challenge/remedy workflow evidence;
- reviewer training and override logs;
- change-triggered retesting; and
- specialist/legal/privacy review appropriate to the actual deployment facts.

The current **Do not deploy in current state** gate therefore remains unchanged.
