# AI-002 QuackBot — Phase II Threat Model

**System:** AI-002 — QuackBot  
**Current governance gate:** **Pre-Production / Production Blocked**  
**Architecture dependency:** `DW-AI002-ARCH-SEC-01 v1.0`  
**Status:** Threat-model baseline complete; first local validation increment executed

## Current artifact

- [`Duckworks_QuackBot_Threat_Model_v1.0.md`](Duckworks_QuackBot_Threat_Model_v1.0.md)

The threat model defines `QBT-001`–`QBT-048` and first-wave cases `QBSEC-T001`–`QBSEC-T012`.

Those twelve cases are now implemented in:

[`../../../11-assurance-testing-and-evaluation/06-technical-security-validation/AI-002-quackbot/`](../../../11-assurance-testing-and-evaluation/06-technical-security-validation/AI-002-quackbot/)

Current local execution:

- vulnerable: **0 PASS / 12 FAIL**;
- hardened: **12 PASS / 0 FAIL**;
- unit tests: **8/8 PASS**;
- local verifier: PASS;
- source binding: `LOCAL_UNBOUND`; and
- commit-bound replay: pending.

No `EV-AI002-*` IDs are allocated yet.

## Evidence boundary

The threat model and local lab do not establish a production vulnerability, production prompt-injection resistance, customer-data protection, legal compliance or control effectiveness.

The production gate remains **blocked**.
