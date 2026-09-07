# DuckTalent Remediation and Retest Record

**Project:** W.I.N.G. — Workflows, Intelligence, Next-Generation Governance  
**AI system:** AI-005 — DuckTalent AI  
**Primary risk:** AI-005-R01 — Bias and discrimination  
**Finding:** IAF-2026-001  
**Corrective action:** CAPA-2026-001  
**Package version:** 1.0  
**Package date:** 7 September 2026  
**Classification:** Fictional and synthetic portfolio evidence

> **Evidence boundary.** Duckworks, its personnel, decisions, dates and operating records are fictional. This package demonstrates a bounded management-system workflow. It does not demonstrate production operation, legal compliance, ISO/IEC 42001 conformity, certification, independent assurance or validated production risk reduction.

**Document ID:** DW-RTR-001  
**Record ID:** RTR-2026-001  
**Evidence ID:** EV-AI005-018  
**Executed by:** Data & AI control operator (fictional role)  
**Reviewed by:** Beatrice Van Duck — Chief People Officer  
**Execution date:** 25 August 2026 (synthetic exercise timeline)

## 1. Purpose

Record the immediate correction of DT-CHG-001 and verify that the remediated synthetic control configuration operates as designed. This retest confirms remediation; it is not the later effectiveness review.

## 2. Before-and-after configuration

| Attribute | Failed proposal | Remediated baseline |
|---|---|---|
| Configuration ID | DT-CHG-001 / proposed v0.9.2 | DT-CFG-0.9.3-capa |
| Approved-feature allowlist | Documented but not enforced | Versioned as DT-ALW-0.9.3 and enforced as a blocking prerequisite |
| `Career_Gap_Months` | Present and active | Removed; explicit deny test added |
| Version-difference artifact | Not mandatory | Mandatory for features, criteria and weights |
| DT-02 execution | Downstream detection | Mandatory prerequisite before promotion |
| Evidence completeness | Manual reviewer dependency | Incomplete package is automatically ineligible |
| Owner attestation | Not consistently required | Technical and HR attestations required |

## 3. Retest method

The existing executable DT-02 logic and 24-record, 12-matched-pair synthetic dataset were rerun against the remediated configuration. The package also checked the allowlist, version difference, evidence completeness and dual-attestation prerequisites.

The preventive prerequisites are implemented in `evidence/ducktalent_change_gate.py`. The executable reads a versioned baseline and proposed change, computes feature and weight differences, verifies mandatory evidence and attestations, and can return only `blocked` or `eligible_for_governance_review`. It never authorizes deployment.

## 4. Retest results

| Test | Expected result | Observed result | Status |
|---|---|---|---|
| RT-01 Prohibited feature absence | `Career_Gap_Months` absent | Absent | Pass |
| RT-02 Explicit deny rule | Attempted inclusion fails build | Build blocked | Pass |
| RT-03 Allowlist conformance | All active inputs are approved | All active inputs matched DT-ALW-0.9.3 | Pass |
| RT-04 Version-difference generation | Difference record produced | Feature/criteria/weight difference produced | Pass |
| RT-05 DT-02 prerequisite | Promotion blocked without current result | Missing-result case blocked | Pass |
| RT-06 DT-02 assertions | Ten control assertions pass | 10 of 10 passed | Pass |
| RT-07 Matched-pair dataset | All 12 matched pairs evaluated | 12 of 12 evaluated | Pass |
| RT-08 Evidence completeness | Incomplete package rejected | Missing-evidence case rejected | Pass |
| RT-09 Dual attestation | Two attestations required | Technical and HR attestations recorded | Pass |
| RT-10 Gate preservation | No deployment authorization created | DO NOT DEPLOY preserved | Pass |

## 5. Exceptions

No exception occurred within the synthetic retest population. This result does not predict production performance and does not demonstrate behavior with real applicants, production data, vendor services or human reviewers.

## 6. Retest conclusion

The correction and redesigned preventive prerequisites operated as designed in the immediate synthetic retest. CAPA-2026-001 could proceed to a separate effectiveness review. AI-005-R01 remained Critical and the DuckTalent lifecycle decision remained **DO NOT DEPLOY**.
