# AI-005 DuckTalent — Fairness & Adverse-Impact Operating-Evidence Demonstration

**AI system:** `AI-005 — DuckTalent AI`  
**Primary risk:** `AI-005-R01 — Fundamental rights & fairness`  
**Preventive dependency:** `DT-01 — Job-Relevance Criteria & Proxy Feature Governance`  
**Detective control demonstrated:** `DT-02 — Pre-Deployment Fairness & Adverse-Impact Testing`  
**Current governance gate:** Do not deploy in current state  
**Evidence classification:** Portfolio / Synthetic / Non-production

## Purpose

This package demonstrates a third Project W.I.N.G. control archetype:

**AI-005-R01 → DT-01 job-relevance/proxy boundary → DT-02 fairness testing → matched synthetic applicants → seeded unapproved proxy → measured outcome difference → deployment block → remediation → retest → governance gate review → real-applicant pilot denied**

It is deliberately different from:

- WingInspect, which demonstrates human final authority; and
- PondGPT, which demonstrates executable technical authorization assurance.

This package focuses on **fairness, job relevance, proxy-feature governance, and pre-deployment evidence** for a consequential employment use case.

## Current DuckTalent boundary

DuckTalent remains a pre-deployment concept. The portfolio's current governance decision is **Do not deploy in current state**.

The synthetic DT-02 evidence does not change that decision. The worked governance gate record now demonstrates how the available evidence is consumed at a lifecycle gate and reaches the same result: **DENIED — maintain DO NOT DEPLOY with real applicants**.

## Control relationship

### DT-01 — Job-Relevance Criteria & Proxy Feature Governance

Preventive dependency. Recruitment criteria and features should be justified as job-related, approved, versioned, and challenged for direct, proxy, derived, accessibility, and disproportionate-impact concerns.

This package uses a synthetic approved-feature allow-list as a test input. It does **not** establish that real DuckTalent criteria governance is implemented.

### DT-02 — Pre-Deployment Fairness & Adverse-Impact Testing

Detective control. A pre-deployment test should examine outcome differences, error distribution, proxy effects, relevant subgroup patterns, and the relationship between ranking logic and approved job criteria before any real-applicant use.

The worked demonstration implements this control as a deterministic Python test harness.

## Synthetic test design

The dataset contains **24 synthetic applicants arranged as 12 matched pairs**.

Within each pair:

- approved job-related features are identical;
- the applicants differ only in `Career_Gap_Months`;
- the group labels `Reference` and `Comparison` are synthetic portfolio test labels and are **not real protected characteristics**.

The deliberately defective pre-remediation scoring logic applies a penalty to `Career_Gap_Months`, even though that feature is not on the approved feature allow-list.

This creates a controlled demonstration of how an apparently plausible but unapproved criterion can create unequal screening outcomes.

## Why there is no legal fairness threshold

The DuckTalent source documents explicitly avoid inventing validated fairness thresholds before a controlled pilot or other valid evidence exists.

Accordingly:

- the script calculates selection rates and error metrics;
- it does **not** use a ratio as a legal compliance test;
- it does **not** declare discrimination or fairness from one metric; and
- the synthetic shortlist threshold exists only to make the test deterministic.

The pre-deployment gate is blocked because an **unapproved feature is used and produces a measurable matched-pair effect**, not because a particular legal ratio has been crossed.

## Deliberate seeded issue

**Seeded issue:** `Career_Gap_Months` is used as an unapproved score penalty.

Expected DT-02 response:

1. detect that the feature is outside the approved allow-list;
2. measure the resulting synthetic group and matched-pair outcome differences;
3. block the deployment gate;
4. remove the unapproved feature;
5. rerun the full synthetic population; and
6. record the remediation result without treating the retest as deployment approval.

## Evidence in this package

1. `AI-005_Control_Implementation_Card_Fairness_Testing.md`
2. `AI-005_Synthetic_Applicant_Fairness_Test_Dataset.csv`
3. `dt02_test_config.json`
4. `dt02_fairness_adverse_impact_test.py`
5. `AI-005_2026-09-02_FAIR_Fairness_Test_Results.csv`
6. `AI-005_2026-09-02_FAIR_Fairness_Exception.json`
7. `AI-005_2026-09-02_FAIR_Fairness_Run_Summary.json`
8. `AI-005_2026-09-02_MON_Fairness_Control_Test.md`
9. `AI-005_2026-09-02_GOV_Governance_Gate_Decision_Record.md`

## Governance gate decision

The worked gate decision asks:

**May DuckTalent advance to a pilot using real applicants?**

The record consumes the current risk assessment, acceptance criteria, lifecycle SOP, AIA/FRIA/DPIA, model-documentation gaps, DT-02 implementation evidence, run summary, and control-test result.

The decision is:

**DENIED — maintain DO NOT DEPLOY with real applicants**

The reason is not that the DT-02 test failed. The DT-02 synthetic control test passed.

The denial occurs because the wider evidence pack still shows:

- **Critical (20)** current residual risk;
- system control effectiveness **Not Implemented**;
- `DT-01` **Not Implemented**;
- production model/provider/version and architecture unresolved;
- production-representative validation absent;
- real-applicant fairness and lawful fairness-data methodology unvalidated;
- meaningful human-oversight evidence absent;
- transparency, contestability, remedy, accessibility, privacy, security, third-party, and monitoring conditions incomplete.

The gate record therefore demonstrates a key governance principle:

> **A successful control test does not authorize progression beyond the boundary supported by the total evidence.**

The record is synthetic portfolio evidence. It is **not** evidence that a real Duckworks AI Governance Committee meeting occurred or that real executives approved or rejected a real system.

## Run locally

```bash
python dt02_fairness_adverse_impact_test.py
```

No third-party Python package or network access is required.

## Evidence maturity

### DT-02 control evidence

**Designed → Synthetic technical implementation demonstrated → Synthetic fairness execution demonstrated → Synthetic operation tested**

### Governance-decision evidence

**Synthetic control evidence available → Governance evidence pack reviewed → Synthetic lifecycle decision demonstrated**

Not demonstrated:

**Real committee approval/non-approval → Real pilot authorization → Production fairness validated → Real-applicant operating effectiveness → Legal compliance → Validated rights-risk reduction → Independent assurance**

## Critical limitation

> This package is a synthetic portfolio demonstration. It contains no real applicants, no real protected-characteristic data, no real DuckTalent model, no lawful-basis determination for fairness data, no legal discrimination analysis, and no evidence of a real committee meeting or real executive approval/non-approval.

The package therefore does not justify lowering DuckTalent's current **Critical (20)** residual-risk position or changing the **Do not deploy in current state** gate.
