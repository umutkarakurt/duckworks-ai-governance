# DuckTalent Internal Audit Finding

**Project:** W.I.N.G. — Workflows, Intelligence, Next-Generation Governance  
**AI system:** AI-005 — DuckTalent AI  
**Primary risk:** AI-005-R01 — Bias and discrimination  
**Finding:** IAF-2026-001  
**Corrective action:** CAPA-2026-001  
**Package version:** 1.0  
**Package date:** 7 September 2026  
**Classification:** Fictional and synthetic portfolio evidence

> **Evidence boundary.** Duckworks, its personnel, decisions, dates and operating records are fictional. This package demonstrates a bounded management-system workflow. It does not demonstrate production operation, legal compliance, ISO/IEC 42001 conformity, certification, independent assurance or validated production risk reduction.

**Document ID:** DW-IAF-001  
**Engagement ID:** AUD-AIMS-2026-001  
**Evidence ID:** EV-AI005-015  
**Finding classification:** Significant nonconformity — internal portfolio classification  
**Finding status:** Closed on 7 September 2026; see FCR-2026-001  
**Auditor:** Internal Audit Manager (fictional role)  
**Finding owner:** Beatrice Van Duck — Chief People Officer

## 1. Audit objective and scope

The review assessed whether DuckTalent material changes are prevented from bypassing approved feature governance, fairness regression testing, reassessment and the lifecycle gate. The scope was limited to the synthetic `DT-CHG-001` change chain and its linked records. No production system or real applicant data was inspected.

## 2. Criteria

| Criterion | Expected condition |
|---|---|
| DT-01 | Only approved, job-relevant features may enter a candidate ranking configuration; proxy-risk changes require documented approval. |
| DT-02 | A version-bound fairness and adverse-impact regression result must be completed before lifecycle consideration. |
| AI-GOV-01 | The lifecycle gate must consume current risk, impact, rights/privacy, model and control evidence. |
| AI-GOV-02 | A material feature, criteria, weight or ranking change must trigger reassessment before approval. |
| Internal evidence rule | The release candidate must include retrievable feature-difference, test, exception and approval records. |

These are internal portfolio criteria. No exact ISO/IEC 42001 clause-level conformity conclusion is made.

## 3. Condition observed

Proposed configuration `DT-CHG-001` reintroduced `Career_Gap_Months`, a feature previously removed after a synthetic fairness failure. The feature reached the proposed release candidate because the approved-feature allowlist was documented but not enforced as a mandatory build/release condition, and the change package did not initially require a machine-readable version difference or linked DT-02 result.

DT-02 subsequently detected the prohibited feature and recreated synthetic disparity. `DT-MON-001 / DT-TRG-001` rejected the configuration, opened `IR-001` and preserved the deployment block.

## 4. Finding statement

Duckworks had not implemented an enforced preventive control ensuring that every DuckTalent ranking change was restricted to approved features and accompanied by version-difference and DT-02 regression evidence before it became eligible for lifecycle-gate review. As a result, a prohibited proxy-risk feature could enter a proposed release candidate, although the downstream detective control identified and blocked it before deployment.

## 5. Evidence inspected

| Evidence | Relevance |
|---|---|
| EV-AI005-003 | Executable DT-02 fairness and adverse-impact test |
| EV-AI005-004 | Pre/post-remediation synthetic results |
| EV-AI005-005 | Seeded prohibited-feature exception |
| EV-AI005-006 | Ten-assertion synthetic control test |
| EV-AI005-009 | Initial governance-gate decision maintaining the real-applicant block |
| EV-AI005-010 | Proposed change DT-CHG-001 |
| EV-AI005-011 | Executable change-regression check |
| EV-AI005-012 | Detection and trigger DT-MON-001 / DT-TRG-001 |
| EV-AI005-013 | Reassessment IR-001 |
| EV-AI005-014 | Revised governance-gate decision rejecting the change |

## 6. Risk and significance

| Factor | Assessment |
|---|---|
| Affected risk | AI-005-R01 — bias and discrimination |
| Potential consequence | Discriminatory ranking, rights impact, employment-law exposure, complaints and loss of trust if a prohibited feature reached real use |
| Actual portfolio outcome | The synthetic change was detected and blocked; no real applicant processing or production harm occurred |
| Severity | Significant because the preventive control was not enforced for a high-impact employment context |
| Residual-risk impact | No reduction; recorded current risk remains Critical |
| Lifecycle impact | No change; **DO NOT DEPLOY** remains |

## 7. Immediate correction and containment

1. Reject `DT-CHG-001` and prevent promotion of its configuration.
2. Preserve the prior deployment block.
3. Remove `Career_Gap_Months` from the proposed configuration.
4. Freeze further feature, weight, criteria and ranking changes pending CAPA approval.
5. Open RCA-2026-001 and CAPA-2026-001.

## 8. Required response

The finding owner must establish the direct and systemic causes, implement an enforced approved-feature allowlist, require machine-readable version-difference evidence, make DT-02 regression a release prerequisite, establish dual review and demonstrate recurrence prevention. Closure requires a separate effectiveness review and management decision.
