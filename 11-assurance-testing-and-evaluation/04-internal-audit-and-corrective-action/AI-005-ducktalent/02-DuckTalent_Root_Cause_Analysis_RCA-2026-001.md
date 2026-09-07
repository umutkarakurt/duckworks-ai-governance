# DuckTalent Root-Cause Analysis

**Project:** W.I.N.G. — Workflows, Intelligence, Next-Generation Governance  
**AI system:** AI-005 — DuckTalent AI  
**Primary risk:** AI-005-R01 — Bias and discrimination  
**Finding:** IAF-2026-001  
**Corrective action:** CAPA-2026-001  
**Package version:** 1.0  
**Package date:** 7 September 2026  
**Classification:** Fictional and synthetic portfolio evidence

> **Evidence boundary.** Duckworks, its personnel, decisions, dates and operating records are fictional. This package demonstrates a bounded management-system workflow. It does not demonstrate production operation, legal compliance, ISO/IEC 42001 conformity, certification, independent assurance or validated production risk reduction.

**Document ID:** DW-RCA-001  
**RCA ID:** RCA-2026-001  
**Evidence ID:** EV-AI005-016  
**RCA owner:** Dr. Ada Duckfield — Head of Data & AI  
**Governance challenger:** Eleanor Duckford — AI Governance Lead  
**Completed:** 21 August 2026 (synthetic exercise timeline)

## 1. Problem statement

An unapproved proxy-risk feature, `Career_Gap_Months`, was reintroduced in proposed DuckTalent change `DT-CHG-001` after earlier removal. The downstream DT-02 regression control detected and blocked the change, but preventive change governance did not stop the feature from entering the proposed release candidate.

## 2. Causal analysis

| Causal layer | Determination | Evidence or rationale |
|---|---|---|
| Direct cause | The proposed configuration referenced a feature outside the approved job-relevance set. | DT-CHG-001 and EV-AI005-012 |
| Preventive-control weakness | The approved-feature allowlist was guidance, not a technically enforced promotion condition. | The prohibited feature could be packaged before DT-02 execution. |
| Process weakness | The change template did not require a machine-readable comparison against the last approved configuration. | Reviewers lacked a mandatory version-difference artifact. |
| Workflow weakness | DT-02 was a downstream detector rather than a required build/release dependency. | Detection occurred after the release candidate was assembled. |
| Governance weakness | The release package could be considered incomplete without automatically becoming ineligible for gate review. | Evidence completeness was reviewer-dependent rather than enforced. |
| Human factor | The proposer relied on prior configuration logic without explicit feature-by-feature attestation. | No deliberate misconduct is assumed or evidenced. |

## 3. Five-whys analysis

1. **Why was the prohibited feature present?** It was included in the proposed ranking configuration.
2. **Why could it be included?** The approved-feature allowlist was not enforced by the configuration pipeline.
3. **Why was the violation not prevented during change preparation?** A machine-readable version difference and feature attestation were not mandatory package components.
4. **Why could the package progress without those components?** DT-02 and evidence-completeness checks were not configured as release prerequisites.
5. **Why was this dependency absent?** Control design treated policy, change review, testing and governance-gate review as separate activities rather than one evidence-enforced workflow.

## 4. Root-cause statement

The root cause was incomplete integration of DuckTalent feature governance with the technical change and release workflow: the approved-feature boundary, version-difference review, DT-02 regression result and evidence-completeness check were not enforced as inseparable prerequisites for release-candidate eligibility.

## 5. Contributing factors

- Preventive DT-01 implementation remained incomplete.
- Control ownership was split across HR, Data & AI and AI Governance without one release-accountability checkpoint.
- The source-status label “Partially implemented” did not identify which enforcement steps were absent.
- The repository demonstrated detection and gating but did not yet demonstrate a preventive pipeline control.

## 6. Extent-of-condition review

| Question | Result |
|---|---|
| Other DuckTalent synthetic changes reviewed | Existing synthetic package only; no additional prohibited-feature event identified |
| Production configurations reviewed | None available |
| Real applicant records reviewed | None; out of scope and not present |
| Other AI systems tested for the same weakness | Not tested by this RCA |
| Systemic implication | The evidence-completeness and change-gate design should be considered for other material AI systems, but no cross-system effectiveness claim is made. |

## 7. Cause-to-action linkage

| Cause | Corrective action |
|---|---|
| Allowlist not enforced | CA-01 and CA-02 |
| Version difference not mandatory | CA-03 |
| DT-02 not a release prerequisite | CA-04 |
| Gate eligibility not evidence-enforced | CA-05 |
| Split accountability and reviewer reliance | CA-06 |

The proposed actions correct both the specific configuration and the management-system weakness that permitted it.
