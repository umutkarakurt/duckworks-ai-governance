# Project W.I.N.G. — Operating Evidence Index

This register maps material AI risks to controls and the evidence available to demonstrate control design, implementation, operation, and effectiveness.

Synthetic portfolio evidence is explicitly distinguished from production operating evidence.

| Evidence ID | AI System | Risk | Control | Artifact | Evidence State | What It Demonstrates |
|---|---|---|---|---|---|---|
| EV-AI004-001 | AI-004 — WingInspect Vision | AI-004-R01 | WI-01 | Control Implementation Card | Designed | Control objective, owner, trigger, evidence requirements, and measurement approach |
| EV-AI004-002 | AI-004 — WingInspect Vision | AI-004-R01 | WI-01 | Synthetic Inspection Log | Synthetic execution demonstrated | Human decision workflow, override authority, timestamps, and final disposition trail |
| EV-AI004-003 | AI-004 — WingInspect Vision | AI-004-R01 | WI-01 | Human Release Gate Control Test | Synthetic operation tested | Control execution against the complete synthetic population |
| EV-AI004-004 | AI-004 — WingInspect Vision | AI-004-R01 | WI-01 | Production Inspection Records | Not available | Real-world operating evidence |
| EV-AI004-005 | AI-004 — WingInspect Vision | AI-004-R01 | WI-01 | Post-release Material Defect Trend | Not available | Outcome effectiveness / risk-reduction evidence |
| EV-AI006-001 | AI-006 — PondGPT | AI-006-R01 | PG-01 / PG-02 | Control Implementation Card | Designed | Authorization-risk objective, owner, triggers, evidence, gate rule, and measurement approach |
| EV-AI006-002 | AI-006 — PondGPT | AI-006-R01 | PG-01 / PG-02 | Synthetic Authorization Matrix | Designed test input | Personas, source entitlements, repository exclusions, and DLP expectations |
| EV-AI006-003 | AI-006 — PondGPT | AI-006-R01 | PG-02 | Executable Permission Regression Control | Synthetic technical implementation demonstrated | Reproducible control logic that executes authorization, DLP, change, exception, gate, and retest assertions |
| EV-AI006-004 | AI-006 — PondGPT | AI-006-R01 | PG-02 | Permission Regression Test Log | Synthetic technical execution demonstrated | Twenty executed assertions across normal access, denials, exclusions, DLP, permission changes, seeded defect, remediation, and retest |
| EV-AI006-005 | AI-006 — PondGPT | AI-006-R01 | PG-02 | Seeded Authorization Exception | Synthetic failure detection / containment demonstrated | Detection of an intentionally misconfigured Finance connector ACL, alert generation, expansion blocking, and remediation tracking |
| EV-AI006-006 | AI-006 — PondGPT | AI-006-R01 | PG-02 | Permission Regression Control Test | Synthetic operation tested | Full-population control test and conclusion that PG-02 operated as designed within the synthetic population |
| EV-AI006-007 | AI-006 — PondGPT | AI-006-R01 | PG-01 / PG-02 | Production Permission / DLP / SIEM Records | Not available | Real operating evidence for authorization inheritance, DLP, alerting, and change-triggered regression |
| EV-AI006-008 | AI-006 — PondGPT | AI-006-R01 | PG-01 / PG-02 | Unauthorized Retrieval Escape Trend | Not available | Outcome effectiveness / actual cross-boundary data-exposure rate |

## Interpretation

A higher evidence state should not be inferred merely because a lower-state artifact exists.

For example:

- a control card demonstrates **design**;
- a synthetic execution log demonstrates **workflow or technical execution logic**;
- executable synthetic code can demonstrate **reproducible control implementation in the portfolio scenario**;
- a control test over synthetic data demonstrates **testable operation in a portfolio scenario**;
- only sustained production records could demonstrate **real operating effectiveness**; and
- validated effectiveness requires sufficiently rigorous or independent assurance over actual operation and outcomes.

## Current Evidence Conclusions

### WI-01 — Qualified Human Final Inspection

Project W.I.N.G. demonstrates:

**Designed → Synthetic execution demonstrated → Synthetic operation tested**

It does **not** claim:

**Production operating effectiveness → Validated effectiveness**

### PG-02 — Automated Permission Regression & DLP Tests

Project W.I.N.G. demonstrates:

**Designed → Synthetic technical implementation demonstrated → Synthetic technical execution demonstrated → Synthetic operation tested**

The executable demonstration includes one seeded authorization defect that is detected, alerted, gated, remediated, and successfully retested. The control therefore does not pass because the synthetic environment contains no defects; it passes because the detective process identifies and contains the seeded defect as designed.

It does **not** claim:

**Production authorization validated → Sustained operating effectiveness → Validated risk reduction → Independent assurance**
