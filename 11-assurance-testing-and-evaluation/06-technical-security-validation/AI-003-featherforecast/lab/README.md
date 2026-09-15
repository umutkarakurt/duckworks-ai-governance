# FeatherForecast Data-Integrity / Poisoning / Drift / Decision-Resilience Security Lab

**Lab version:** `featherforecast-lab-0.1.0`  
**System:** AI-003 — FeatherForecast  
**Status:** deterministic synthetic / non-production

This lab implements `FFSEC-T001`–`FFSEC-T012` from `DW-AI003-TM-01 v1.0` using only the Python standard library.

The objective is **forecasting-pipeline and decision-boundary validation**, not proof of production forecasting accuracy.

## Profiles

**Vulnerable:** deliberately reproduces twelve unsafe outcomes across source poisoning, historical backfills, training-serving skew, feature/model/configuration change, drift misclassification, forecast mutation/staleness, approval bypass, decision-record tampering, unauthorized planning-data access, outage handling and rollback.

**Hardened:** reruns identical cases with quarantine, backfill review/lineage preservation, skew detection, revalidation, change/promotion blocking, drift-quality separation, forecast invalidation, manager-approval enforcement, record-integrity checks, least-privilege access, manual/degraded planning and known-good rollback.

## Commands

```bash
python scripts/run_campaign.py
python -m unittest discover -s tests -p "test_*.py"
python scripts/ci_verify.py
python scripts/build_hash_manifest.py
```

## Expected local result

- vulnerable: **0 PASS / 12 FAIL**
- hardened: **12 PASS / 0 FAIL**
- unit tests: **10/10 PASS**
- semantic verifier: **PASS**
- `source_commit`: `LOCAL_UNBOUND`
- `production_effectiveness_claim`: `false`
- `forecast_accuracy_claim`: `false`
- `legal_compliance_claim`: `false`
- `risk_score_change_authorized`: `false`
- `governance_gate_change_authorized`: `false`
- `evidence_id_allocation_authorized`: `false`
- `iaf_2026_003_closure_authorized`: `false`

## Important interpretation boundary

A hardened PASS means the **defined synthetic control outcome** was achieved.

For example, `FFSEC-T006` proves only that the synthetic lab distinguishes one defined data-quality case from one defined drift case. It does not validate a universal drift detector or production threshold.

## Evidence boundary

The lab does not demonstrate:

- production forecast accuracy;
- real source-data integrity;
- real poisoning resistance;
- real Northstar security;
- real drift-detection performance;
- real manager-approval operation;
- production supplier/planning-data access control;
- legal compliance; or
- residual-risk reduction.

No `EV-AI003-*` IDs should be allocated until a clean commit-bound repository replay succeeds.

`IAF-2026-003` remains open.

Governance remains **Continue with monitoring**.
