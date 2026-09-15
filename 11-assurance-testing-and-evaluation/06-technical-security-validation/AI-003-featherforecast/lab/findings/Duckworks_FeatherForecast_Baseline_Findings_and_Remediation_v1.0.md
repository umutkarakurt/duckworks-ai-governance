# AI-003 FeatherForecast — Baseline Findings and Remediation

**Document ID:** DW-AI003-FIND-SEC-01  
**Version:** 1.0  
**Date:** 15 September 2026  
**Status:** Synthetic seeded findings / local remediation and retest completed  
**System:** AI-003 — FeatherForecast  
**Lab:** `featherforecast-lab-0.1.0`  
**Current governance position:** **Continue with monitoring**

> These are deliberately seeded portfolio findings. They are not claims that a production FeatherForecast deployment has these vulnerabilities or that its forecasts are inaccurate.

## 1. Baseline result

The vulnerable profile reproduced **12/12 deliberately seeded unsafe outcomes**.

The hardened profile reran the same twelve cases and returned **12/12 PASS** locally.

The local campaign remains `LOCAL_UNBOUND`; commit-bound repository replay is pending.

## 2. Findings

| Finding | Tests | Seeded baseline condition | Synthetic remediation demonstrated | Retest |
|---|---|---|---|---|
| FF-F01 — Poisoned/extreme input enters forecasting path | T001 | Unapproved extreme demand batch accepted and used | Approved-source/data validation and quarantine | PASS |
| FF-F02 — Historical backfill silently rewrites approved history | T002 | Unapproved revision applied without review/lineage preservation | Backfill review, blocking and approved-history hash preservation | PASS |
| FF-F03 — Training-serving skew is not detected | T003 | Scoring proceeds with mismatched feature/schema state | Schema/feature skew detection and scoring/promotion blocking | PASS |
| FF-F04 — Unauthorized feature/snapshot change is used | T004 | Changed feature/data baseline proceeds without revalidation | Change detection, revalidation requirement and promotion blocking | PASS |
| FF-F05 — Model/config/threshold drift silently promotes | T005 | Changed baseline retains prior validation and promotes | Version/change detection, prior-validation invalidation and promotion blocking | PASS |
| FF-F06 — Data-quality failure and drift are confused | T006 | Quality failure is treated as drift and real drift as healthy; auto-promotion proceeds | Distinct quality/drift classification with review before promotion | PASS |
| FF-F07 — Altered/stale forecast remains decision-eligible | T007 | Mutated stale forecast is presented as current and usable | Hash/staleness validation and forecast invalidation | PASS |
| FF-F08 — Material commitment bypasses manager approval | T008 | Direct commitment proceeds without valid approval | Approval gate and direct-commitment blocking | PASS |
| FF-F09 — Decision/override record tampering is accepted | T009 | Modified decision record remains treated as valid | Record-integrity detection and investigation requirement | PASS |
| FF-F10 — Unauthorized planning-data access exposes commercial data | T010 | Unauthorized requester receives commercial planning canary | Least-privilege denial, access logging and response minimization | PASS |
| FF-F11 — Platform/source outage leaves stale forecast looking current | T011 | Stale last-known forecast remains active | Staleness marking and manual/degraded planning mode | PASS |
| FF-F12 — Unvalidated retraining promotes and rollback is unreliable | T012 | Unapproved retraining promotes; rollback state is mismatched/unverified | Promotion blocking and matched model/config/data known-good rollback | PASS |

## 3. Interpretation

The hardened profile demonstrates intended **synthetic forecasting-pipeline and decision-control behavior**.

It does not prove:

- FeatherForecast is accurate in production;
- production source data cannot be poisoned;
- every form of drift will be detected;
- actual Northstar changes are observable;
- real planning-data access controls are effective;
- managers meaningfully challenge forecasts;
- production rollback will succeed;
- actual purchasing/production commitments are protected; or
- AI-003 residual risk has decreased.

## 4. Audit-finding boundary

`IAF-2026-003` remains open.

The lab demonstrates a manager-approval gate and decision-record integrity in a synthetic environment. It does not demonstrate production or production-equivalent `FF-01` operation and therefore does not satisfy the finding's closure criteria.

## 5. Governance consequence

No AI-003 risk-score changes.

No production-effectiveness credit for `FF-01`–`FF-04`.

No assumption closure.

No `EV-AI003-*` IDs yet.

The governance position remains **Continue with monitoring**.
