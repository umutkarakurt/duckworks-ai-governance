# AI Risk Assessment

**Repository path:** `04-risk-assessment/`  
**Status:** Active methodology and evidence-reconciled risk-scenario register  

[← Back to main portfolio](../README.md)

This folder contains the active Duckworks method for identifying, scoring, treating, approving, and monitoring AI risk.

## Current artifacts

- [`Duckworks_AI_Risk_Classification_Assessment_Methodology_v1.0.md`](Duckworks_AI_Risk_Classification_Assessment_Methodology_v1.0.md)
- [`Duckworks_AI_Risk_Scenarios_v1.4.md`](Duckworks_AI_Risk_Scenarios_v1.4.md) — **authoritative current scenario register**
- [`03-risk-evidence-reconciliation/`](03-risk-evidence-reconciliation/) — reconciliation analysis and workbook

Versions 1.0–1.3 are retained for version history and are superseded by v1.4. Superseded v0.9 working material is retained separately under `99-archive/`.

## Method design

The methodology uses concrete **cause → event → impact** scenarios and a 5×5 Severity × Likelihood matrix. It distinguishes:

- inherent risk;
- implemented-control effectiveness and evidence confidence;
- current residual risk;
- target residual risk;
- treatment and approval thresholds.

The system position is driven by the highest material scenario rather than averaging away severe harm.

## Critical control-credit rule

Planned controls receive **no credit** as implemented controls. Residual risk is re-assessed after operating controls; the method does not mechanically divide the inherent score by a control factor.

## Legal separation

Regulatory/legal triage is a separate governance gate. Duckworks Low/Moderate/High/Critical ratings are internal enterprise-risk outcomes and must not be treated as EU AI Act legal classifications.

## PondGPT PG-03 reconciliation

`AI-006-R02 — Security & adversarial manipulation` now links to canonical evidence `EV-AI006-017`–`022`, covering the PG-03 validation plan, executable synthetic lab, baseline failure/remediation, hardened eight-case retest, detection validation and commit-bound GitHub Actions replay.

The evidence changes the **evidence-maturity interpretation**, not the current score or lifecycle gate. The recorded current residual remains **12 High**, PondGPT remains **Restricted pilot only**, and no production risk-reduction credit is granted because production identity/connectors, provider/tool boundaries, SIEM/DLP integration, operating period and outcome effectiveness remain unverified.

## Evidence-chain expectation

A reviewer should be able to trace each material scenario to controls, evidence, treatment, current decision, target state, and monitoring/reassessment requirements. Where target scores depend on future controls, they remain target—not current—risk.

---

> **Portfolio boundary:** Duckworks, Project W.I.N.G., its personnel, systems, datasets, decisions, controls, and evidence are fictional or synthetic unless a file explicitly identifies a public source. Folder descriptions explain the intended governance role of the artifacts; they do not convert draft, planned, or template material into implemented controls, legal compliance, certification, or independent assurance.
