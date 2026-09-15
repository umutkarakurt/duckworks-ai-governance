# Operating Evidence

Project W.I.N.G. distinguishes governance documentation from evidence that a governance control is capable of operating.

Phase II technical-security evidence follows:

**Risk → Threat → Security Requirement → Vulnerable Baseline → Technical Test → Raw Evidence → Remediation → Same-Test Retest → Commit-Bound Replay → Reconciliation**

## Authoritative evidence view

`Duckworks_AI_Control_Evidence_Index_v1.8.md` remains the master base evidence register.

Controlled reconciliation overlays supplement it:

- `Duckworks_AI_Control_Evidence_Index_AI004_Reconciliation_v1.0.md` — WingInspect `EV-AI004-006–011`
- `Duckworks_AI_Control_Evidence_Index_AI002_Reconciliation_v1.0.md` — QuackBot `EV-AI002-001–007`

Current combined population:

- v1.8 base records: **76**
- AI-004 reconciliation records: **6**
- AI-002 reconciliation records: **7**
- combined current records: **89**
- available synthetic records: **83**
- not-available evidence records: **6**
- production-effectiveness conclusions supported: **0**

## Current worked examples

### AI-002 — QuackBot

The QuackBot package demonstrates public-facing RAG/API security boundaries across prompt/RAG injection, source provenance, anonymous/private retrieval, cross-customer BOLA, session isolation, grounding/escalation, output handling, tool/egress, resource controls, provider/log minimization and change-triggered regression.

The campaign is commit-bound to `25525cc2c09c6b6557ddb9e7706fdaf81ce1796f` and reconciled as `EV-AI002-001–007`.

See [`AI-002-quackbot/`](AI-002-quackbot/).

### AI-004 — WingInspect Vision

WingInspect combines `WI-01` human-release evidence with the adversarial-ML Phase II chain and reconciliation `EV-AI004-006–011`.

See [`AI-004-winginspect/`](AI-004-winginspect/).

### AI-006 — PondGPT

PondGPT demonstrates permission-aware retrieval, supplier-governance evidence and PG-03 adversarial-security validation reconciled as `EV-AI006-017–022`.

See [`AI-006-pondgpt/`](AI-006-pondgpt/).

### AI-005 — DuckTalent AI

DuckTalent demonstrates fairness/proxy-feature testing, lifecycle blocking, change/reassessment and a bounded audit/corrective-action cycle.

See [`AI-005-ducktalent/`](AI-005-ducktalent/).

## Important limitation

All execution records, identities, sessions, prompts, corpora, alerts, exceptions, code execution and control results are synthetic unless explicitly identified otherwise.

Synthetic evidence may demonstrate control design, workflow logic, technical testability and reproducible evidence generation. It does not by itself establish legal compliance, production control effectiveness, validated residual-risk reduction or independent assurance.
