# Operating Evidence

Project W.I.N.G. distinguishes governance documentation from evidence that a governance control is capable of operating.

This folder contains worked examples showing how an identified AI risk is translated into:

**Risk → Control → Owner → Execution → Evidence → Testing → Monitoring**

## Purpose

Policies, standards, methodologies, and control descriptions do not by themselves demonstrate implementation.

The artifacts in this folder demonstrate the evidence architecture that would be required to assess whether AI governance controls are operating as intended.

## Evidence States

Project W.I.N.G. distinguishes between five evidence states:

1. **Designed** — the control has been defined, including its objective, owner, trigger, and required evidence.
2. **Implemented** — the mechanism, workflow, or system capability required to perform the control exists.
3. **Operating** — evidence demonstrates that the control is being executed.
4. **Effective** — evidence indicates that the control materially reduces or manages the underlying risk.
5. **Validated** — independent or sufficiently rigorous assurance supports the effectiveness conclusion.

These states are intentionally separated to avoid granting control-effectiveness credit based only on documentation.

## Current Worked Example

### AI-004 — WingInspect Vision

**Material risk:** A manufacturing defect may be missed by WingInspect Vision, allowing a defective component to progress through quality control and creating downstream product-quality or physical-safety harm.

**Canonical control:** `WI-01 — Qualified Human Final Inspection`

**Operational mechanism demonstrated:** Mandatory Human Release Gate

The worked evidence package demonstrates:

- control design;
- accountable operating ownership;
- execution triggers;
- independent human decision authority;
- meaningful AI override capability;
- auditable decision evidence; and
- control testing against synthetic records.

See: [`AI-004-winginspect/`](./AI-004-winginspect/)

## Important Limitation

Duckworks is a fictional portfolio organization.

All execution records in this folder are **synthetic portfolio evidence** created solely to demonstrate governance operating-model, control, and assurance design.

They do **not** constitute:

- real production records;
- measured WingInspect model performance;
- verified manufacturing outcomes;
- longitudinal control-effectiveness evidence; or
- independent assurance over a live environment.

Synthetic evidence may demonstrate control design and workflow logic, but it does not justify additional production residual-risk reduction credit.
