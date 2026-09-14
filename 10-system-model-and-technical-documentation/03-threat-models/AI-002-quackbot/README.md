# AI-002 QuackBot — Phase II Threat Model

**System:** AI-002 — QuackBot  
**Current governance gate:** **Pre-Production / Production Blocked**  
**Architecture dependency:** `DW-AI002-ARCH-SEC-01 v1.0`  
**Status:** Threat-model baseline complete; validation plan / execution pending

## Current artifact

- [`Duckworks_QuackBot_Threat_Model_v1.0.md`](Duckworks_QuackBot_Threat_Model_v1.0.md)

The threat model covers:

- internet/API abuse;
- authentication and session isolation;
- anonymous versus customer-specific data boundaries;
- direct prompt injection;
- indirect RAG injection;
- corpus poisoning/provenance failure;
- object-level authorization;
- customer-data leakage;
- unsafe/high-impact support guidance;
- warranty/legal-content misinformation;
- output handling;
- tool/SSRF/excessive-agency paths;
- rate/resource exhaustion;
- provider/model/configuration change;
- telemetry failure; and
- fail-open dependency behavior.

## Candidate validation set

`QBSEC-T001`–`QBSEC-T012` are **design-only** test IDs until a separate validation plan specifies:

- synthetic fixtures;
- deliberately vulnerable and hardened profiles;
- exact assertions;
- resource/rate conditions;
- session/customer identities;
- RAG corpus fixtures;
- provider/log canaries;
- telemetry schema;
- evidence hashing;
- remediation/retest; and
- local/CI replay.

No `EV-AI002-*` evidence IDs are allocated at this stage.

## Evidence boundary

The threat model identifies plausible attack/failure paths. It does not establish that a production QuackBot vulnerability exists, that an attack occurred, or that `QB-01`–`QB-06` are effective.

The production gate remains **blocked**.
