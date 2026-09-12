# AI-004 WingInspect Vision — Phase II Threat Model

**System:** AI-004 — WingInspect Vision  
**Current governance gate:** Restricted pilot only  
**Architecture dependency:** `DW-AI004-ARCH-SEC-01 v1.0`  
**Status:** Threat-model baseline complete; validation plan / execution pending

## Current artifact

- [`Duckworks_WingInspect_Threat_Model_v1.0.md`](Duckworks_WingInspect_Threat_Model_v1.0.md) — adversarial-ML, physical-input, model/data integrity, supply-chain, fail-safe, and release-gate threat model.

## First-wave validation candidates

The threat model defines eight candidate cases, `WISEC-T001`–`WISEC-T008`, covering:

- adversarial patch / occlusion evasion;
- lighting, blur, noise, and compression robustness;
- model artifact integrity;
- threshold / preprocessing / class-map tamper;
- dataset / label poisoning;
- synthetic backdoor trigger behavior;
- fail-safe handling of camera/model/quality dependency failure; and
- Mandatory Human Release Gate bypass attempts.

These IDs are **test design only** until a separate validation plan defines exact fixtures, assertions, evidence schema, vulnerable/hardened profiles, and acceptance logic.

## Evidence boundary

No threat listed here is claimed to exist in a real Duckworks environment. No technical PASS/FAIL evidence is created by this folder.
