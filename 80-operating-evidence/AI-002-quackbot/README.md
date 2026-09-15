# AI-002 — QuackBot Operating Evidence Package

This package reconciles the first QuackBot Phase II technical-security increment into the Duckworks evidence architecture.

## Evidence chain

**AI-002-R01 / R02 / R03**  
↓  
**Architecture + threat model**  
↓  
**QB-01–QB-06 requirements**  
↓  
**QBSEC-T001–T012 vulnerable baseline**  
↓  
**Findings / remediation**  
↓  
**Same-test hardened campaign**  
↓  
**Detection / control-signal validation**  
↓  
**Commit-bound GitHub Actions replay**  
↓  
**Evidence reconciliation**  
↓  
**Production gate remains blocked**

## Stable evidence IDs

- `EV-AI002-001` — Technical Security Validation Plan
- `EV-AI002-002` — Executable QuackBot Lab
- `EV-AI002-003` — Baseline Findings and Remediation
- `EV-AI002-004` — Hardened Campaign + Technical Security Test Report v1.1
- `EV-AI002-005` — Detection and Control-Signal Validation
- `EV-AI002-006` — Commit-Bound GitHub Actions Replay + Retained Evidence Artifact
- `EV-AI002-007` — AI Interaction Disclosure Design Assertion

## Canonical replay

- commit: `25525cc2c09c6b6557ddb9e7706fdaf81ce1796f`
- run: #147 / `34946047428`
- Python: `3.12.14`
- vulnerable: 0 PASS / 12 FAIL
- hardened: 12 PASS / 0 FAIL
- unit tests: 8/8 PASS
- artifact ID: `10387591380`
- artifact digest: `sha256:a4f50c18553c5996e118b26fedbb4a7e976db703443f7516ec146d673e974391`

## Governance result

No AI-002 risk score changes.

No production-effectiveness conclusion.

`ASM-010` and `ASM-026` remain open.

`QB-COMP-001` is a separate legal-design assertion and does not establish full Article 50 compliance.

The lifecycle gate remains **Pre-Production / Production Blocked**.
