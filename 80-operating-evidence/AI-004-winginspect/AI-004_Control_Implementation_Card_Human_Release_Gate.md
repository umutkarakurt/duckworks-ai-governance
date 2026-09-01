# Control Implementation Card
## AI-004 — WingInspect Vision

| Field | Value |
|---|---|
| Document ID | DW-WING-CTRL-01 |
| Version | 1.0 |
| Date | 2026-09-01 |
| AI System | AI-004 — WingInspect Vision |
| Risk ID | AI-004-R01 |
| Control ID | CTRL-004-01 |
| Control Name | Mandatory Human Release Gate |
| Control Type | Preventive |
| Evidence Status | Synthetic implementation demonstration |
| Production Evidence | Not available |
| Portfolio Status | Worked example |

> **Portfolio disclaimer:** This artifact demonstrates the intended control design and evidence architecture for the fictional Duckworks environment. It does not represent actual production operation or measured model performance.

## 1. Risk

WingInspect Vision may fail to identify a material manufacturing defect, resulting in erroneous acceptance of a defective component and downstream product-quality or safety harm.

## 2. Control

**Preventive — Mandatory Human Release Gate:** WingInspect Vision output must not independently authorize product acceptance.

Before any AI-inspected item is released from quality control, a qualified manufacturing inspector must:

1. review the inspected item;
2. consider the WingInspect result;
3. make and record an independent accept/reject decision;
4. document any disagreement with the AI output and the reason for the override; and
5. authorize or block final release.

No item may proceed to release without completed qualified-inspector authorization.

## 3. Operating Owner

**Control performer:** Qualified Manufacturing Inspector

**Process owner:** Director of Manufacturing

The qualified manufacturing inspector performs and records the final acceptance/rejection decision. The Director of Manufacturing owns the operating process and is accountable for ensuring that the control is applied consistently.

Internal Audit remains independent from control operation and may assess the control as an assurance function.

## 4. Trigger / Frequency

The control operates for **every AI-assisted quality inspection before final product acceptance or release**.

The control must also be revalidated following any material change to:

- model version;
- training or operational data;
- inspection thresholds;
- system integration;
- decision authority;
- quality-control procedure; or
- manufacturing inspection workflow.

## 5. Evidence Produced

The electronic inspection record must contain:

- inspection identifier;
- item and batch identifier;
- WingInspect result;
- AI confidence or flag status;
- named qualified inspector;
- inspector qualification status;
- independent human accept/reject decision;
- AI override status;
- override rationale, where applicable;
- AI-result timestamp;
- human-decision timestamp;
- final release/block authorization; and
- final-disposition timestamp.

The record must support traceability through:

**AI output → human review → human decision → final disposition**

## 6. Effectiveness Metric

### Primary Operating Metric — Human-Gate Compliance Rate

**Human-gate compliance rate**

=  
(AI-assisted product releases with complete, timestamped qualified-inspector approval recorded before release ÷ total AI-assisted product releases) × 100

**Target: 100%.**

Any release without valid prior qualified-human authorization constitutes a control failure and requires escalation and investigation.

### Outcome Effectiveness Indicator

Where production evidence becomes available, management should also monitor:

**Post-release material defect escape rate for AI-assisted inspections**

This distinguishes **control execution** from **actual risk-reduction effectiveness**.

A 100% human-gate compliance rate demonstrates that the release gate operated. It does not, by itself, prove that the combined AI-plus-human inspection process prevented defective products from escaping.

## Evidence Maturity Conclusion

This portfolio package demonstrates:

- control design;
- operating ownership;
- execution logic;
- meaningful human override authority;
- audit-trace design; and
- synthetic control testing.

It does not establish real-world production operating effectiveness.
