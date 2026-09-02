# AI Control Framework

**Repository path:** `07-control-framework/`  
**Status:** Portfolio baseline / control design  

[← Back to main portfolio](../README.md)

This folder translates material AI risks and governance requirements into **testable controls with defined ownership and evidence expectations**.

## Current artifacts

- `Duckworks_AI_Control_Library_v1.0.xlsx`
- `Duckworks_AI_Control_Framework_Report_v1.0.md`

## Control design fields

The control library is intended to capture, where relevant:

- control objective;
- control description;
- preventive, detective, or corrective classification;
- owner;
- frequency;
- evidence;
- testing procedure;
- automation opportunity;
- related risks;
- framework mapping;
- implementation status.

## Evidence rule

A control description is not evidence of implementation. Planned or unvalidated controls should remain clearly distinguished from controls that are implemented, operating, and supported by current evidence.

Synthetic portfolio evidence may demonstrate control design, workflow logic, or testability, but it does not by itself establish production operating effectiveness.

### Status interpretation

- **Not implemented** — the control mechanism is not in place.
- **Planned** — the control requirement and intended design are defined, but implementation has not been demonstrated.
- **Weak / ad hoc** — some control activity exists, but it is informal, inconsistent, or materially incomplete.
- **Partially implemented** — a control mechanism or material part of it exists, but coverage, evidence, consistency, or operating validation remains incomplete.
- **Implemented** — the control mechanism is in place and supported by evidence appropriate to the claimed implementation boundary.

An **Implemented** label does not automatically mean the control is operating effectively, effective at reducing the underlying risk, or independently validated. Those are separate assurance conclusions.

For the current WingInspect worked example, `WI-01 — Qualified Human Final Inspection` is treated as **Partially implemented** because the portfolio demonstrates the intended workflow and synthetic control testing while real production authority and operating effectiveness remain unvalidated.

For the current PondGPT worked example, `PG-02 — Automated Permission Regression & DLP Tests` is treated as **Partially implemented** because the portfolio contains a reproducible executable synthetic test mechanism, generated evidence, seeded-defect detection, gate enforcement, and remediation/retest logic while production identity/connector/DLP/SIEM integration, sustained operating history, and production operating effectiveness remain unvalidated.

For the current DuckTalent worked example, `DT-02 — Pre-Deployment Fairness & Adverse-Impact Testing` is treated as **Partially implemented** because the portfolio contains a reproducible executable synthetic fairness-test mechanism, matched-pair test data, seeded unapproved-feature detection, deployment blocking, remediation and retest evidence. Real-applicant fairness, production feature governance, lawful fairness-data processing, legal compliance, and sustained operating effectiveness remain unvalidated. `DT-01` remains **Not implemented**.

## Framework mapping

Mappings to NIST, ISO/IEC, ENISA, OWASP, MITRE, or legal sources are used for traceability and design context. A mapping does not itself demonstrate:

- legal compliance;
- certification;
- conformity;
- operating effectiveness.

## Reviewer approach

Choose a material risk scenario and follow it into the control library. The strongest portfolio demonstration is not the number of mapped frameworks; it is whether the control has a clear objective, owner, evidence source, test method, and a defensible causal relationship to the risk being treated.

Three worked examples demonstrate different control archetypes:

- [`AI-004 WingInspect operating-evidence package`](../80-operating-evidence/AI-004-winginspect/) — links `AI-004-R01` to `WI-01`, synthetic inspection execution, meaningful human overrides, and a control-test workpaper.
- [`AI-005 DuckTalent operating-evidence package`](../80-operating-evidence/AI-005-ducktalent/) — links `AI-005-R01` to the `DT-01` job-relevance/proxy boundary and `DT-02` detective control, matched synthetic applicants, seeded proxy-feature failure, diagnostic disparity metrics, deployment blocking, remediation, and retesting.
- [`AI-006 PondGPT operating-evidence package`](../80-operating-evidence/AI-006-pondgpt/) — links `AI-006-R01` to the `PG-01` authorization boundary and `PG-02` detective control, executable permission-regression logic, negative authorization testing, seeded-defect detection, exception/gate evidence, remediation, and retesting.

All three preserve the distinction between synthetic portfolio implementation/testing evidence and production operating effectiveness. The DuckTalent example additionally preserves the boundary between diagnostic fairness testing and any legal discrimination or compliance conclusion.

---

> **Portfolio boundary:** Duckworks, Project W.I.N.G., its personnel, systems, datasets, decisions, controls, and evidence are fictional or synthetic unless a file explicitly identifies a public source. Folder descriptions explain the intended governance role of the artifacts; they do not convert draft, planned, or template material into implemented controls, legal compliance, certification, or independent assurance.
