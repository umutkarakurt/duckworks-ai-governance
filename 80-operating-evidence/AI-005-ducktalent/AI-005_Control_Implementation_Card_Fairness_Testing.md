# AI-005 DuckTalent — DT-02 Control Implementation Card

| **Field** | **Value** |
|---|---|
| **Document ID** | DW-DT-DT02-IMPL-01 |
| **Version / date** | 1.0 / 2 September 2026 |
| **AI system** | AI-005 — DuckTalent AI |
| **Linked risk** | AI-005-R01 — Fundamental rights & fairness |
| **Preventive dependency** | DT-01 — Job-Relevance Criteria & Proxy Feature Governance |
| **Control demonstrated** | DT-02 — Pre-Deployment Fairness & Adverse-Impact Testing |
| **Control type** | Detective |
| **Operating owner** | Beatrice Van Duck — Chief People Officer |
| **Evidence status** | Synthetic technical implementation demonstration |
| **Production evidence** | Not available |
| **Classification** | Portfolio / Synthetic / Non-production |

## 1. Risk

Training data, ranking criteria, features, or proxy variables may create systematic disadvantage for a protected or otherwise disadvantaged group, causing qualified applicants to receive lower rankings or less human consideration and creating fairness, fundamental-rights, legal, and reputational harm.

## 2. Control

`DT-02 — Pre-Deployment Fairness & Adverse-Impact Testing` evaluates DuckTalent outputs before any real-applicant deployment.

The control should test, where lawful and appropriate:

- approved versus actually used criteria/features;
- direct, proxy, and derived feature risks;
- selection-rate differences;
- error-rate differences;
- matched or otherwise comparable applicant patterns;
- accessibility and atypical-profile effects;
- model/version changes;
- material anomalies and exceptions; and
- remediation/retest evidence.

A material feature-governance violation or unexplained adverse pattern must block the relevant deployment or model-change gate pending investigation, remediation, and governance review.

## 3. Operating owner

**Beatrice Van Duck — Chief People Officer**

The CPO owns the recruitment control boundary and is accountable for ensuring that the employment use case is not advanced merely because a technical test runs successfully.

Technical execution may be supported by Data & AI. AI Governance, Legal, Privacy, Risk & Compliance, and other specialists provide challenge. Internal Audit remains independent assurance.

## 4. Trigger / frequency

The control is designed to operate:

- before any use with real applicants;
- on every material ranking/model/version change;
- on approved-feature or criteria changes;
- after material parsing/accuracy/fairness findings;
- after material applicant challenge patterns;
- before expansion to new job families, geographies, languages, or applicant populations; and
- after remediation of a fairness or proxy-feature issue.

## 5. Evidence produced

Expected evidence includes:

- approved job-criteria and feature allow-list;
- proxy/derived-feature review;
- versioned test dataset and population description;
- lawful/appropriate group-data rationale for any real fairness testing;
- model/configuration version;
- selection and error metrics;
- matched/comparable-case analysis where appropriate;
- test code and results;
- exceptions/findings;
- deployment-gate decision;
- remediation evidence;
- retest evidence; and
- specialist/governance review.

## 6. Synthetic worked-example metrics

The worked example reports:

- selection rate by synthetic comparison group;
- true-positive rate relative to the synthetic approved-feature qualification label;
- false-negative rate;
- matched-pair score difference;
- feature allow-list conformance; and
- remediation/retest results.

These metrics are **diagnostic**, not legal thresholds.

The portfolio deliberately does not invent a validated fairness or adverse-impact acceptance threshold.

## 7. Decision rule in the worked example

The synthetic pre-deployment gate is blocked when:

- the scoring logic uses a feature not present on the approved feature allow-list; **and**
- the seeded feature produces a measurable difference between otherwise matched synthetic applicants.

The remediation removes the unapproved feature and reruns the complete synthetic population.

A passing retest results only in:

**Eligible for further governance review**

—not deployment approval.

## 8. Current conclusion

This package demonstrates:

- explicit job-relevance/feature-governance dependency;
- an executable fairness test;
- matched synthetic applicant testing;
- seeded proxy-feature failure;
- group and error metrics;
- deployment blocking;
- remediation; and
- deterministic retesting.

It does **not** demonstrate:

- actual DuckTalent feature governance;
- real applicant fairness;
- lawful collection/use of protected-characteristic data;
- production model behavior;
- legal non-discrimination compliance;
- effective candidate remedy;
- sustained operating effectiveness; or
- validated reduction of current residual risk.

**Evidence state:**  
**Designed → Synthetic technical implementation demonstrated → Synthetic fairness execution demonstrated → Synthetic operation tested**
