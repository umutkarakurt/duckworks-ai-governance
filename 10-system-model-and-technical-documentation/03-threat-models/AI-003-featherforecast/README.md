# AI-003 FeatherForecast — Phase II Threat Model

**System:** AI-003 — FeatherForecast  
**Current governance gate:** **Continue with monitoring**  
**Architecture dependency:** `DW-AI003-ARCH-SEC-01 v1.0`  
**Status:** Threat-model baseline complete; validation plan/execution pending

## Current artifact

- [`Duckworks_FeatherForecast_Threat_Model_v1.0.md`](Duckworks_FeatherForecast_Threat_Model_v1.0.md)

The threat model covers:

- source-data poisoning and anomalous input manipulation;
- historical backfill/revision tampering;
- feature-pipeline manipulation;
- training-serving skew;
- model/configuration/threshold integrity;
- data/performance drift and data-quality discrimination;
- forecast-result integrity and staleness;
- manager-approval bypass;
- override/decision-record tampering;
- supplier/planning-data confidentiality and access;
- third-party platform availability; and
- known-good rollback/evidence reconstruction.

## Candidate validation set

`FFSEC-T001`–`FFSEC-T012` are **design-only** test IDs until a separate validation plan defines fixtures, vulnerable/hardened profiles, assertions and evidence schema.

No `EV-AI003-*` evidence IDs are allocated at this stage.

`IAF-2026-003` remains open.

The current governance position remains **Continue with monitoring**.
