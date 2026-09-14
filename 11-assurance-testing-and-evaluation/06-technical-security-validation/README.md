# Phase II Technical Security Validation

**Repository path:** `11-assurance-testing-and-evaluation/06-technical-security-validation/`  
**Status:** Phase II controlled technical-validation workstream — synthetic / non-production

[← Back to assurance, testing and evaluation](../README.md) · [← Main portfolio](../../README.md)

This folder contains reproducible security-validation plans, executable test implementations, failure/remediation evidence, same-test retesting, detection/control-signal validation and commit-bound replay evidence for selected Duckworks AI systems.

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

WingInspect is the second completed Phase II technical-validation increment.

Primary validation targets:

- `WI-02 — Minimum Sensitivity & Safety Validation`;
- `WI-04 — Fail-Safe Manual Fallback & Stop Rule`;
- `WI-06 — Change-Triggered Revalidation & Locked Baseline`; and
- supporting boundary `WI-01 — Qualified Human Final Inspection`.

Canonical replay:

- vulnerable profile: **0 PASS / 8 FAIL**;
- hardened profile: **8 PASS / 0 FAIL**;
- six unit tests passed;
- verifier PASS;
- full repository semantic verification PASS;
- commit `8e8bb9e43aca3d4a9d2f5cfb6e401b8469c4ac0b`;
- run #124 (`34836419132`); and
- retained artifact `winginspect-security-evidence-8e8bb9e43aca3d4a9d2f5cfb6e401b8469c4ac0b` / `sha256:d9f524770e3e3c406328245f46c7e610c7682cdd6d0072cb51a7fc01f2074f70`.

AI-004 technical evidence is reconciled as `EV-AI004-006–011` through the controlled AI-004 evidence-reconciliation overlay.

See [`AI-004-winginspect/`](AI-004-winginspect/).

## Evidence chain

**Risk → Threat → Security requirement → Deliberately weak baseline → Test → Raw evidence → Finding → Remediation → Same-test retest → Detection/control-signal validation → Commit-bound replay → Control conclusion → Risk/gate reconciliation**

## Evidence boundary

A successful synthetic technical-validation chain does not establish:

- production operation;
- product safety;
- legal compliance;
- ISO conformity/certification;
- independent assurance; or
- residual-risk reduction.

No lifecycle gate changes automatically from CI or test success.

## Next technical target

The next planned Phase II system is **AI-002 QuackBot**, focusing on public-facing RAG/API security.
