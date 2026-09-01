# Project W.I.N.G. — Operating Evidence Index

This register maps material AI risks to controls and the evidence available to demonstrate control design, implementation, operation, and effectiveness.

Synthetic portfolio evidence is explicitly distinguished from production operating evidence.

| Evidence ID | AI System | Risk | Control | Artifact | Evidence State | What It Demonstrates |
|---|---|---|---|---|---|---|
| EV-AI004-001 | AI-004 — WingInspect Vision | AI-004-R01 | CTRL-004-01 | Control Implementation Card | Designed | Control objective, owner, trigger, evidence requirements, and measurement approach |
| EV-AI004-002 | AI-004 — WingInspect Vision | AI-004-R01 | CTRL-004-01 | Synthetic Inspection Log | Synthetic execution demonstrated | Human decision workflow, override authority, timestamps, and final disposition trail |
| EV-AI004-003 | AI-004 — WingInspect Vision | AI-004-R01 | CTRL-004-01 | Human Release Gate Control Test | Synthetic operation tested | Control execution against the complete synthetic population |
| EV-AI004-004 | AI-004 — WingInspect Vision | AI-004-R01 | CTRL-004-01 | Production Inspection Records | Not available | Real-world operating evidence |
| EV-AI004-005 | AI-004 — WingInspect Vision | AI-004-R01 | CTRL-004-01 | Post-release Material Defect Trend | Not available | Outcome effectiveness / risk-reduction evidence |

## Interpretation

A higher evidence state should not be inferred merely because a lower-state artifact exists.

For example:

- a control card demonstrates **design**;
- a synthetic execution log demonstrates **workflow logic**;
- a control test over synthetic data demonstrates **testable operation in a portfolio scenario**;
- only sustained production records could demonstrate **real operating effectiveness**.

## Current Evidence Conclusion

For `CTRL-004-01`, Project W.I.N.G. demonstrates:

**Designed → Synthetic execution demonstrated → Synthetic operation tested**

It does **not** claim:

**Production operating effectiveness → Validated effectiveness**
