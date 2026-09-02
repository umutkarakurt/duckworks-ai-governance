# AI-005 DuckTalent — Synthetic Monitoring, Reassessment & Revised Decision

**Lifecycle chain:**  
**Prior governance decision → Proposed material change → Monitoring / regression check → Reassessment trigger → Targeted reassessment → Revised governance decision**

**AI system:** `AI-005 — DuckTalent AI`  
**Current residual risk:** Critical (20)  
**Current system control effectiveness:** Not Implemented  
**Current evidence confidence:** Low  
**Real-applicant gate:** DO NOT DEPLOY  
**Classification:** Portfolio / Synthetic / Non-production

## Purpose

This package demonstrates the next Project W.I.N.G. maturity layer after the DuckTalent control-test and governance-gate evidence.

The existing DuckTalent gate decision denied progression to a real-applicant pilot and defined an event-driven reconsideration trigger.

The HUDERIA iterative-review plan separately requires event-driven review for material changes in ranking logic, feature set, model/provider/version, data, applicant population, fairness signals, human oversight, incidents, legal context, control failure, or evidence expiry.

This worked example demonstrates one of those triggers without pretending that DuckTalent is operating in production.

## Synthetic change scenario

A deliberately constructed change request, `DT-CHG-001`, proposes a new synthetic scoring configuration after the earlier DT-02 remediation.

The proposed configuration reintroduces:

`Career_Gap_Months`

as a score penalty.

This is intentionally the same feature previously removed by the synthetic DT-02 remediation. The scenario therefore tests whether governance detects **regression after remediation**, rather than merely detecting a defect once.

The change is:

**PROPOSED / NOT APPROVED**

No production model, real applicant, real protected-characteristic data, or real deployment change is represented.

## Monitoring logic

The executable change-regression check:

1. reads the existing DT-02 approved synthetic feature allow-list;
2. reads the existing 24-applicant / 12-pair synthetic fairness dataset;
3. compares the proposed feature set to the approved synthetic feature boundary;
4. re-runs the synthetic scoring effect;
5. checks matched-pair and group outcome differences;
6. opens a material reassessment trigger when the unapproved feature is detected and produces a measurable effect; and
7. preserves the existing real-applicant deployment block.

## Trigger result

Expected result:

**MATERIAL REASSESSMENT TRIGGER — OPEN**

Immediate action:

**REJECT the proposed configuration; do not approve or merge it; preserve DO NOT DEPLOY with real applicants; open `IR-001` reassessment.**

## Evidence in this package

1. `AI-005_2026-09-02_MON_Proposed_Change_Event.json`
2. `AI-005_2026-09-02_MON_Change_Regression_Check.py`
3. `AI-005_2026-09-02_MON_Change_Regression_Result.json`
4. `AI-005_2026-09-02_REA_Reassessment_Record.md`
5. `AI-005_2026-09-02_GOV_Revised_Gate_Decision_Record.md`

## Run locally

From the repository:

```bash
python 12-monitoring-reporting-and-roadmap/AI-005-ducktalent/AI-005_2026-09-02_MON_Change_Regression_Check.py
```

The script uses the canonical synthetic DT-02 configuration and dataset already stored under:

`80-operating-evidence/AI-005-ducktalent/`

No third-party Python package or network access is required.

## Evidence maturity

**Synthetic material-change event → Synthetic change-monitor execution → Synthetic reassessment trigger demonstrated → Synthetic reassessment performed → Synthetic revised lifecycle decision demonstrated**

Not demonstrated:

**Production monitoring → Real drift/complaint/incident signal → Real committee reassessment → Real lifecycle authorization/suspension → Validated operating effectiveness**

## Critical boundary

This package does not represent continuous production monitoring.

DuckTalent is still not authorized to process or rank real applicants.

The worked event is a **pre-deployment synthetic configuration-change regression**. Its value is to demonstrate that prior remediation and governance decisions remain subject to change detection, regression testing, reassessment, and renewed lifecycle control.
