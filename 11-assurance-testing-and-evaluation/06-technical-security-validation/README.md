# Phase II Technical Security Validation

**Repository path:** `11-assurance-testing-and-evaluation/06-technical-security-validation/`  
**Status:** Phase II controlled technical-validation workstream — synthetic / non-production

[← Back to assurance, testing and evaluation](../README.md) · [← Main portfolio](../../README.md)

This folder contains reproducible security-validation plans, executable test implementations, failure/remediation evidence, same-test retesting, detection/control-signal validation and commit-bound replay evidence for selected Duckworks AI systems.

## AI-006 PondGPT

PondGPT is the first completed Phase II technical-validation chain.

- 8/8 vulnerable seeded failures reproduced;
- 8/8 hardened PASS;
- commit-bound replay completed;
- canonical evidence reconciled as `EV-AI006-017–022`; and
- production effectiveness remains unverified.

See [`AI-006-pondgpt/`](AI-006-pondgpt/).

## AI-004 WingInspect Vision

WingInspect is the second completed Phase II technical-validation increment.

- vulnerable: 0 PASS / 8 FAIL;
- hardened: 8 PASS / 0 FAIL;
- commit-bound replay completed;
- AI-004 evidence reconciled as `EV-AI004-006–011`; and
- production effectiveness remains unverified.

See [`AI-004-winginspect/`](AI-004-winginspect/).

## AI-002 QuackBot

QuackBot is the third completed Phase II technical-validation increment and the first explicitly internet-facing customer-service RAG/API case.

Canonical result:

- vulnerable: **0 PASS / 12 FAIL**;
- hardened: **12 PASS / 0 FAIL**;
- unit tests: **8/8 PASS**;
- QuackBot semantic verifier: PASS;
- `QB-COMP-001`: PASS;
- commit `25525cc2c09c6b6557ddb9e7706fdaf81ce1796f`;
- run #147 / `34946047428`;
- retained artifact `quackbot-security-evidence-25525cc2c09c6b6557ddb9e7706fdaf81ce1796f`; and
- evidence reconciled as `EV-AI002-001–007`.

The interaction-disclosure assertion is kept separate from the twelve adversarial-security tests and does not establish full legal compliance.

See [`AI-002-quackbot/`](AI-002-quackbot/).

## AI-001 DuckDesign AI

DuckDesign is the fourth Phase II technical-security target and the first dedicated **engineering / generated-code / software-supply-chain / build-provenance / tool-privilege** case.

Current local validation:

- `DDSEC-T001`–`DDSEC-T012`;
- vulnerable: **0 PASS / 12 FAIL**;
- hardened: **12 PASS / 0 FAIL**;
- unit tests: **10/10 PASS**;
- semantic verifier: **PASS**;
- source binding: `LOCAL_UNBOUND`;
- repository replay: **pending**;
- canonical `EV-AI001-*` allocation: **none**; and
- `IAF-2026-002`: **remains open**.

Primary target controls:

- `DD-01 — Competent Engineer Approval`;
- `DD-02 — Independent Safety Validation Gate`;
- `DD-03 — Engineering Benchmark & Regression Suite`;
- `DD-04 — Engineering Data Boundary & DLP`; and
- `DD-05 — Design/Model Version Traceability`.

The local lab demonstrates synthetic technical behavior only. It does not prove that `DD-01` operates in a production or production-equivalent process and therefore does not close the open High audit finding.

See [`AI-001-duckdesign/`](AI-001-duckdesign/).

## Evidence chain

**Risk → Threat → Security requirement → Deliberately weak baseline → Test → Raw evidence → Finding → Remediation → Same-test retest → Detection/control-signal validation → Commit-bound replay → Control conclusion → Risk/gate reconciliation**

## Evidence boundary

A successful synthetic validation chain does not establish production operation, product safety, product/machinery conformity, legal compliance, ISO conformity/certification, independent assurance or residual-risk reduction.

No lifecycle gate changes automatically from local/CI test success.

## Next Phase II milestone

Upload the DuckDesign validation increment and obtain a clean commit-bound replay plus retained evidence artifact. Only after that should AI-001 canonical evidence reconciliation be performed.
