# AI-003 FeatherForecast — Detection and Control-Signal Validation

**Document ID:** DW-AI003-DET-SEC-01  
**Version:** 1.0  
**Date:** 15 September 2026  
**Status:** Local synthetic validation complete; repository replay pending  
**System:** AI-003 — FeatherForecast

## 1. Purpose

This record separates **pipeline/decision outcome** from **detection signal**.

FeatherForecast must not depend on an alert firing before untrusted data, changed model/configuration, stale forecasts, unauthorized access or approval bypass are contained.

## 2. Signal coverage

| Test | Primary control signal | Hardened outcome |
|---|---|---|
| T001 | source-integrity/range event | poisoned/extreme batch quarantined; no forecast from affected batch |
| T002 | historical-revision review event | unapproved backfill blocked; approved history preserved |
| T003 | training-serving skew event | skew detected; scoring/promotion blocked |
| T004 | feature/snapshot change event | unauthorized change detected; revalidation required |
| T005 | model/config/threshold change event | prior validation invalidated; promotion blocked |
| T006 | data-quality + distribution-drift events | quality failure and drift correctly separated; no automatic promotion |
| T007 | forecast-integrity/staleness event | altered/stale forecast invalidated |
| T008 | manager-approval gate denial | material commitment blocked without approval |
| T009 | decision-record integrity event | tampered record invalid; investigation required |
| T010 | unauthorized-access denial event | access denied/logged; commercial canary absent |
| T011 | platform/source outage event | stale state rejected; manual/degraded planning mode active |
| T012 | promotion/rollback event | unvalidated promotion blocked; known-good state restored |

## 3. Control hierarchy

The intended hierarchy is:

> **preventive/containment boundary → validation/detection signal → correlated evidence → governance conclusion**

Examples:

- poisoning detection does not replace source validation/quarantine;
- drift alerting does not replace back-testing/challenger review;
- model-change alerting does not replace promotion blocking;
- forecast-integrity logging does not replace forecast invalidation;
- approval logging does not replace the commitment gate;
- access monitoring does not replace authorization denial; and
- outage telemetry does not replace manual/degraded planning.

## 4. Drift interpretation limit

`FFSEC-T006` demonstrates only that **two defined synthetic cases** can be distinguished:

- duplicate/missing input records → `DATA_QUALITY`;
- sustained demand-distribution shift → `DRIFT`.

It does not establish that production FeatherForecast can distinguish every operational data-quality issue from concept/data/performance drift, nor does it validate production drift thresholds.

## 5. Evidence limitations

The portfolio does not contain real:

- demand/inventory/supplier data-lineage records;
- Northstar platform telemetry;
- production feature/schema versions;
- model/configuration promotion records;
- accuracy/drift thresholds;
- planning-manager approval populations;
- decision/override records;
- supplier/planning-data access logs;
- outage/manual-fallback evidence; or
- production rollback outcomes.

## 6. Governance consequence

The local result supports only a bounded synthetic conclusion.

It does not change risk scores, close assumptions, close `IAF-2026-003`, establish production forecast accuracy or alter the **Continue with monitoring** governance position.
