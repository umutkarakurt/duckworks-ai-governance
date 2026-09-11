# Phase II Technical Security Validation

**Repository path:** `11-assurance-testing-and-evaluation/06-technical-security-validation/`  
**Status:** Phase II controlled technical-validation workstream — synthetic / non-production  

[← Back to assurance, testing and evaluation](../README.md) · [← Main portfolio](../../README.md)

This folder contains reproducible security-validation plans, test implementations, execution records, findings, remediation/retest evidence, and detection-validation artifacts for selected Duckworks AI systems.

## Current target — AI-006 PondGPT

The first Phase II implementation targets `PG-03 — Prompt Injection & RAG Poisoning Test Suite`, while exercising supporting authorization, tool, logging, output, provider and change-control boundaries.

Existing `PG-01` / `PG-02` evidence remains a separate bounded synthetic authorization-regression demonstration and does not prove production authorization inheritance, production DLP/SIEM operation, or sustained effectiveness.

## Current artifacts

- [`AI-006-pondgpt/Duckworks_PondGPT_PG03_Technical_Security_Validation_Plan_v1.0.md`](AI-006-pondgpt/Duckworks_PondGPT_PG03_Technical_Security_Validation_Plan_v1.0.md) — validation design.
- [`AI-006-pondgpt/lab/`](AI-006-pondgpt/lab/) — executable `pondgpt-lab-0.1.0` synthetic security lab.
- [`AI-006-pondgpt/lab/reports/Duckworks_PondGPT_PG03_Technical_Security_Test_Report_v1.0.md`](AI-006-pondgpt/lab/reports/Duckworks_PondGPT_PG03_Technical_Security_Test_Report_v1.0.md) — local baseline/remediation/retest result.

## Current local result

- Vulnerable profile: **0 PASS / 8 FAIL** — intentionally seeded security failures reproduced.
- Hardened profile: **8 PASS / 0 FAIL** — same eight case functions pass after hardening.
- Prompt-injection detector coverage in `PG03-T005`: **4/5** with zero restricted context/provider chunks in the hardened profile.
- Local verifier: PASS; pytest: **6 passed**.

## Evidence chain

**Risk → Threat → Security requirement → Deliberately weak baseline → Test → Raw evidence → Finding → Remediation → Same-test retest → Detection validation → Control conclusion → Governance/risk review**

Baseline failure evidence and hardened retest evidence are retained separately and integrity-hashed.

## Repository-replay requirement

The local package is not yet bound to a GitHub commit. The accompanying workflow update adds a `Run PondGPT PG-03 technical security lab` step so `main` can replay the verifier/campaign under Python 3.12 after upload. The workflow also asserts that the generated `source_commit` equals `GITHUB_SHA` and uploads the generated PG-03 evidence as a 30-day GitHub Actions artifact.

Canonical evidence IDs should be allocated only after that repository replay succeeds and the actual artifacts are reconciled into the current evidence index.

## Safety and authorization boundary

Testing must not target real third-party services, real credentials, real personal data, or systems outside the explicitly controlled Duckworks lab boundary. External provider behavior is simulated with the fictional/local LanternMind adapter.

---

> **Evidence boundary:** Technical validation in this folder is synthetic portfolio evidence. It can demonstrate reproducible engineering behavior in the defined lab; it cannot establish production operating effectiveness, validated risk reduction, legal compliance, certification, or independent assurance.
