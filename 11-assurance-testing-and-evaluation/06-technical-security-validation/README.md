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
- commit-bound replay completed;
- canonical evidence reconciled as `EV-AI006-017–022`; and
- production effectiveness remains unverified.

See [`AI-006-pondgpt/`](AI-006-pondgpt/).

## AI-004 WingInspect Vision

WingInspect is the second completed Phase II technical-validation increment.

- vulnerable: **0 PASS / 8 FAIL**
- hardened: **8 PASS / 0 FAIL**
- commit-bound replay completed;
- AI-004 evidence reconciled as `EV-AI004-006–011`; and
- production effectiveness remains unverified.

See [`AI-004-winginspect/`](AI-004-winginspect/).

## AI-002 QuackBot

QuackBot is the third Phase II technical-security target and the first explicitly **internet-facing customer-service RAG/API** case.

Current local validation:

- `QBSEC-T001`–`QBSEC-T012`;
- vulnerable: **0 PASS / 12 FAIL**;
- hardened: **12 PASS / 0 FAIL**;
- unit tests: **8/8 PASS**;
- local verifier: PASS;
- `QB-COMP-001` AI-interaction-disclosure design assertion: PASS;
- source binding: `LOCAL_UNBOUND`; and
- repository replay: **pending**.

Primary target controls:

- `QB-01 — Curated RAG Source Allowlist`;
- `QB-02 — Grounding, Citation & Abstention Rules`;
- `QB-03 — Human Escalation SLA`;
- `QB-04 — Prompt Injection & RAG Adversarial Testing`;
- `QB-05 — Least-Privilege Retrieval & Tool Boundaries`; and
- `QB-06 — GenAI Security & Harm Monitoring`.

No `EV-AI002-*` evidence IDs are allocated yet.

See [`AI-002-quackbot/`](AI-002-quackbot/).

## Evidence chain

**Risk → Threat → Security requirement → Deliberately weak baseline → Test → Raw evidence → Finding → Remediation → Same-test retest → Detection/control-signal validation → Commit-bound replay → Control conclusion → Risk/gate reconciliation**

## Evidence boundary

A successful synthetic technical-validation chain does not establish production operation, legal compliance, customer-data protection in production, ISO conformity/certification, independent assurance or residual-risk reduction.

No lifecycle gate changes automatically from local/CI test success.
