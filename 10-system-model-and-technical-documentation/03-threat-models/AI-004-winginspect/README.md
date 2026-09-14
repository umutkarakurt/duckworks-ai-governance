# AI-004 WingInspect Vision — Phase II Threat Model

**System:** AI-004 — WingInspect Vision  
**Current governance gate:** Restricted pilot only  
**Architecture dependency:** `DW-AI004-ARCH-SEC-01 v1.0`  
**Status:** Threat-model baseline complete; first validation increment locally and commit-bound replayed

## Current artifact

- [`Duckworks_WingInspect_Threat_Model_v1.0.md`](Duckworks_WingInspect_Threat_Model_v1.0.md)

The first-wave cases `WISEC-T001`–`WISEC-T008` are now implemented in the synthetic validation lab:

[`../../../11-assurance-testing-and-evaluation/06-technical-security-validation/AI-004-winginspect/`](../../../11-assurance-testing-and-evaluation/06-technical-security-validation/AI-004-winginspect/)

Local and commit-bound execution records 8/8 deliberately vulnerable failures and 8/8 hardened control PASS outcomes. The WingInspect replay succeeded against `5f06f4c13fc45ad3cdc15d5192d26e034f004863` and produced retained artifact `winginspect-security-evidence-5f06f4c13fc45ad3cdc15d5192d26e034f004863`. Canonical evidence reconciliation remains pending until the corrected full workflow reruns green because run #115 failed afterward on an unrelated Portfolio Integrity JSON-path assertion.

## Evidence boundary

The threat model remains a planning/design artifact. The local lab does not establish a real production vulnerability, real model robustness, product safety, or production control effectiveness.
