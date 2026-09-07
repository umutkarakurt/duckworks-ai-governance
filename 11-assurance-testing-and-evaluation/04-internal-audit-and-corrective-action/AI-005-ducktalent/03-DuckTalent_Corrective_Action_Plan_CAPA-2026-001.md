# DuckTalent Corrective Action Plan

**Project:** W.I.N.G. — Workflows, Intelligence, Next-Generation Governance  
**AI system:** AI-005 — DuckTalent AI  
**Primary risk:** AI-005-R01 — Bias and discrimination  
**Finding:** IAF-2026-001  
**Corrective action:** CAPA-2026-001  
**Package version:** 1.0  
**Package date:** 7 September 2026  
**Classification:** Fictional and synthetic portfolio evidence

> **Evidence boundary.** Duckworks, its personnel, decisions, dates and operating records are fictional. This package demonstrates a bounded management-system workflow. It does not demonstrate production operation, legal compliance, ISO/IEC 42001 conformity, certification, independent assurance or validated production risk reduction.

**Document ID:** DW-CAPA-001  
**CAPA ID:** CAPA-2026-001  
**Evidence ID:** EV-AI005-017  
**CAPA owner:** Beatrice Van Duck — Chief People Officer  
**Technical action owner:** Dr. Ada Duckfield — Head of Data & AI  
**Governance oversight:** Eleanor Duckford — AI Governance Lead  
**Status:** Complete within the synthetic exercise boundary

## 1. Objective

Prevent a DuckTalent ranking configuration containing an unapproved feature, undocumented feature/weight change or missing DT-02 result from becoming eligible for governance-gate review.

## 2. Corrective-action register

| Action | Type | Required action | Owner | Target date | Completion evidence | Status |
|---|---|---|---|---|---|---|
| CA-01 | Correction | Remove `Career_Gap_Months` from DT-CHG-001 and reject the affected configuration. | Head of Data & AI | 22 Aug 2026 | EV-AI005-018 | Complete |
| CA-02 | Corrective | Convert the approved feature set into versioned allowlist `DT-ALW-0.9.3`; fail the build on any unapproved feature. | Head of Data & AI | 24 Aug 2026 | EV-AI005-018 | Complete |
| CA-03 | Corrective | Generate a machine-readable feature, criteria and weight difference against the last approved baseline for every change. | Head of Data & AI | 24 Aug 2026 | EV-AI005-018 | Complete |
| CA-04 | Corrective | Make the DT-02 ten-assertion regression suite a mandatory prerequisite; a failure or missing result blocks promotion. | Head of Data & AI | 25 Aug 2026 | EV-AI005-018 | Complete |
| CA-05 | Corrective | Make the governance package ineligible unless current risk, impact/rights/privacy, model/change and test evidence IDs are present. | AI Governance Lead | 25 Aug 2026 | EV-AI005-018 | Complete |
| CA-06 | Preventive | Require dual attestation by the technical change owner and HR process owner before gate submission. | Chief People Officer | 25 Aug 2026 | EV-AI005-018 | Complete |
| CA-07 | Effectiveness | Run three independent synthetic change cases after remediation, including attempted recurrence and incomplete-evidence cases. | Internal Audit Manager | 4 Sep 2026 | EV-AI005-019 | Complete |
| CA-08 | Governance | Submit finding, RCA, CAPA, retest and effectiveness evidence to management review; record deployment and risk decisions separately from finding closure. | AI Governance Lead | 5 Sep 2026 | EV-AI005-020 | Complete |

## 3. Closure criteria

CAPA-2026-001 is eligible for closure only when:

- the prohibited feature is absent from the remediated baseline;
- the allowlist rejects an unapproved feature automatically;
- a version-difference record is generated for every synthetic test change;
- a missing or failing DT-02 result prevents promotion;
- the governance package rejects missing mandatory evidence;
- both required attestations are present;
- all immediate retest assertions pass;
- a separate effectiveness review demonstrates recurrence prevention;
- management records that finding closure does not authorize deployment.

## 4. Measures

| Measure | Acceptance threshold |
|---|---:|
| Proposed changes screened against allowlist | 100% |
| Proposed changes with version-difference record | 100% |
| Proposed changes with current DT-02 result | 100% |
| Prohibited-feature promotion attempts blocked | 100% |
| Gate packages containing all mandatory evidence IDs | 100% |
| Required owner attestations completed | 100% |
| Production-effectiveness claim | 0; outside this package |

## 5. Risk and deployment constraint

Completion of this CAPA supports closure of IAF-2026-001 only. It does not reduce AI-005-R01, establish DT-01/DT-02 production effectiveness or satisfy DuckTalent's remaining blockers. **DO NOT DEPLOY** remains mandatory.
