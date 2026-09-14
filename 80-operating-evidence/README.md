# Operating Evidence

Project W.I.N.G. distinguishes governance documentation from evidence that a governance control is capable of operating.

This folder contains worked examples showing how identified AI risks are translated into:

**Risk → Control → Owner → Execution → Evidence → Testing → Governance Decision → Monitoring / Reassessment**

Phase II technical-security examples extend the chain through:

**Risk → Threat → Security Requirement → Vulnerable Baseline → Technical Test → Raw Evidence → Remediation → Same-Test Retest → Commit-Bound Replay → Reconciliation**

## Authoritative evidence view

[`Duckworks_AI_Control_Evidence_Index_v1.8.md`](Duckworks_AI_Control_Evidence_Index_v1.8.md) remains the master base evidence register for the v1.8 governance baseline.

The first WingInspect technical-security reconciliation is controlled through:

[`Duckworks_AI_Control_Evidence_Index_AI004_Reconciliation_v1.0.md`](Duckworks_AI_Control_Evidence_Index_AI004_Reconciliation_v1.0.md)

The base and AI-004 addendum together represent the current evidence view until the next consolidated master-index release.

Current combined population:

- v1.8 base evidence records: **76**
- new AI-004 technical records: **6**
- combined current records: **82**
- available synthetic records: **76**
- not-available evidence records: **6**
- production-effectiveness conclusions supported: **0**

`EV-AI004-006–011` cover the WingInspect validation plan, executable lab, baseline/remediation, hardened test report, detection/control-signal validation and commit-bound replay.

## Evidence-state discipline

Project W.I.N.G. separates:

1. **Designed**
2. **Implemented / synthetic technical implementation demonstrated**
3. **Operating / synthetic operation tested**
4. **Effective**
5. **Validated**

Synthetic commit-bound reproducibility is an additional evidence attribute; it does not convert synthetic evidence into production evidence.

## Current worked examples

### AI-004 — WingInspect Vision

The AI-004 package now contains:

- `WI-01` Mandatory Human Release Gate design/execution/control-test evidence;
- Phase II architecture and threat model;
- `WISEC-T001`–`T008` adversarial/robustness validation;
- vulnerable/hardened profiles;
- findings/remediation;
- hardened retest;
- detection/control-signal validation;
- successful GitHub Actions replay against `8e8bb9e43aca3d4a9d2f5cfb6e401b8469c4ac0b`;
- retained artifact `winginspect-security-evidence-8e8bb9e43aca3d4a9d2f5cfb6e401b8469c4ac0b`; and
- formal AI-004 evidence reconciliation.

Stable IDs: `EV-AI004-001–011`.

See [`AI-004-winginspect/`](AI-004-winginspect/).

### AI-006 — PondGPT

PondGPT demonstrates permission-aware retrieval / permission regression, supplier-governance lifecycle evidence and the PG-03 adversarial-security extension.

The PG-03 chain is reconciled as `EV-AI006-017–022` and remains synthetic / commit-bound rather than production-effective.

See [`AI-006-pondgpt/`](AI-006-pondgpt/) and [`../11-assurance-testing-and-evaluation/06-technical-security-validation/AI-006-pondgpt/`](../11-assurance-testing-and-evaluation/06-technical-security-validation/AI-006-pondgpt/).

### AI-005 — DuckTalent AI

DuckTalent demonstrates fairness/proxy-feature control testing, lifecycle blocking, material-change monitoring/reassessment and a bounded internal-audit/corrective-action cycle.

Its evidence remains synthetic and does not establish production fairness, legal compliance or deployment readiness.

See [`AI-005-ducktalent/`](AI-005-ducktalent/).

### AIMS evidence

The operating-evidence architecture also links AIMS objective/support, management-review, control-applicability and internal-audit evidence.

These records demonstrate bounded management-system mechanics only; they do not establish an operating enterprise AIMS, ISO/IEC 42001 conformity or certification.

## Important limitation

All execution records, test identities, model behavior, source permissions, alerts, exceptions, code execution and control results are synthetic unless explicitly identified otherwise.

They do not constitute:

- real production records;
- measured WingInspect production model performance;
- verified manufacturing outcomes;
- actual PondGPT identity/RAG/DLP/SIEM activity;
- real DuckTalent applicants or fairness conclusions;
- longitudinal control effectiveness;
- validated reduction of current residual risk; or
- independent assurance over a live environment.

Synthetic evidence may demonstrate control design, workflow logic, technical testability and reproducible evidence generation. It does not by itself justify production residual-risk reduction.
