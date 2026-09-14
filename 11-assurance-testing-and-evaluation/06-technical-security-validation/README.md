# Phase II Technical Security Validation

**Repository path:** `11-assurance-testing-and-evaluation/06-technical-security-validation/`  
**Status:** Phase II controlled technical-validation workstream — synthetic / non-production

[← Back to assurance, testing and evaluation](../README.md) · [← Main portfolio](../../README.md)

This folder contains reproducible security-validation plans, test implementations, execution records, findings, remediation/retest evidence, and detection-validation artifacts for selected Duckworks AI systems.

## AI-006 PondGPT

PondGPT is the first completed Phase II technical-validation chain.

- `PG-03 — Prompt Injection & RAG Poisoning Test Suite`
- 8/8 vulnerable seeded failures reproduced;
- 8/8 hardened PASS;
- commit-bound GitHub Actions replay completed;
- canonical evidence reconciled as `EV-AI006-017–022`; and
- production effectiveness remains unverified.

See [`AI-006-pondgpt/`](AI-006-pondgpt/).

## AI-004 WingInspect Vision

WingInspect is the second Phase II target.

The first validation increment targets:

- `WI-02 — Minimum Sensitivity & Safety Validation`;
- `WI-04 — Fail-Safe Manual Fallback & Stop Rule`;
- `WI-06 — Change-Triggered Revalidation & Locked Baseline`; and
- supporting boundary `WI-01 — Qualified Human Final Inspection`.

Current result:

- vulnerable profile: **0 PASS / 8 FAIL**;
- hardened profile: **8 PASS / 0 FAIL**;
- six standard-library unit tests passed;
- WingInspect verifier PASS;
- commit-bound WingInspect replay succeeded against `5f06f4c13fc45ad3cdc15d5192d26e034f004863`;
- retained artifact `winginspect-security-evidence-5f06f4c13fc45ad3cdc15d5192d26e034f004863` (`10338040691`; `sha256:d35cd1e5233f34fa0bcf7d04130f92ae6c0bc35640cba81dc148355b2f49285b`); and
- full workflow run #115 failed only afterward because the final Portfolio Integrity assertion used the wrong JSON path. A corrected clean rerun is pending before canonical evidence reconciliation.

See [`AI-004-winginspect/`](AI-004-winginspect/).

## Evidence chain

**Risk → Threat → Security requirement → Deliberately weak baseline → Test → Raw evidence → Finding → Remediation → Same-test retest → Detection/control-signal validation → Control conclusion → Governance/risk review**

Canonical WingInspect evidence IDs and control/risk reconciliation remain deferred until the corrected full workflow completes green. The WingInspect lab itself has already demonstrated commit-bound reproducibility.

## Safety boundary

Testing must not target real third parties, real manufacturing systems, real credentials, real people, real products/facilities, or systems outside the controlled synthetic lab.

> **Evidence boundary:** Technical validation here is synthetic portfolio evidence. It cannot establish production effectiveness, validated risk reduction, legal compliance, certification, or independent assurance.
