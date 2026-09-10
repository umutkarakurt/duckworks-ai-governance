# Operating Evidence

Project W.I.N.G. distinguishes governance documentation from evidence that a governance control is capable of operating.

This folder contains worked examples showing how an identified AI risk is translated into:

**Risk → Control → Owner → Execution → Evidence → Testing → Governance Decision → Monitoring / Reassessment**

## Authoritative evidence index

[`Duckworks_AI_Control_Evidence_Index_v1.7.md`](Duckworks_AI_Control_Evidence_Index_v1.7.md) is the current canonical evidence register. It consolidates 70 stable evidence IDs: 64 available synthetic records and six explicitly unavailable production-evidence records. `EV-AIMS-001`–`008` covers AIMS objectives and support; `EV-AIMS-009`–`016` covers risk, management review and action follow-up; `EV-AIMS-017`–`020` covers control applicability; and `EV-AIMS-021`–`028` covers the internal-audit procedure, universe, programme, first-wave plan, evidence requests, test results, findings, independence limitation and executable gate. Earlier indexes are retained as superseded history.

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

## Current Worked Examples

### AIMS internal audit programme

The [`AIMS internal-audit programme`](../11-assurance-testing-and-evaluation/05-aims-internal-audit-programme/) allocates all 45 controls to a risk-based 2026–2027 schedule and performs a bounded first-wave repository review of `DD-01` and `FF-01`. Two High findings remain open; auditor independence, competence and authorization are not demonstrated; the gate closes zero findings.

### AIMS objectives and support

The [`AIMS objectives-and-support package`](../06-governance-operating-model/01-aims-objectives-and-support/) adds a formula-driven objectives dashboard, competence criteria and records, an executable authorization gate, explicit exceptions, and priority-scope document/evidence control. It demonstrates bounded synthetic management-system support operation and grants no real authorization.

### AIMS risk, opportunity and management review

The [`AIMS management-review cycle`](../12-monitoring-reporting-and-roadmap/01-aims-management-review-cycle/) adds AIMS-level risk/opportunity assessment, a release-triggered objective reconciliation, integrated management-review inputs, a synthetic review record, six assigned actions, deterministic overdue/dependency evaluation and an exception record. It changes no system risk score or lifecycle gate and closes no action automatically.

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

### AI-006 — PondGPT

**Material risk:** Incorrect retrieval permissions or connector authorization may cause PondGPT to return restricted internal information to a user who is not authorized to access the underlying source.

The related [`AI-006 PondGPT supplier-governance package`](../09-third-party-ai-governance/02-worked-supplier-case/AI-006-pondgpt/) extends the evidence chain through `AI-TPR-01`, a conditional supplier decision, material-change response, monitoring and exit design. It does not change the restricted-pilot gate or High-risk position.

**Preventive boundary:** `PG-01 — Permission-Aware Retrieval`

**Detective control demonstrated:** `PG-02 — Automated Permission Regression & DLP Tests`

The worked evidence package demonstrates:

- a synthetic authorization matrix with positive and negative access expectations;
- executable permission-regression logic;
- pilot-source exclusion and synthetic DLP assertions;
- entitlement-change regression;
- one deliberately seeded connector ACL defect;
- automated-style detection of the authorization mismatch;
- exception and alert evidence;
- connector/corpus expansion blocking;
- remediation and successful retesting; and
- a control-test conclusion over the complete synthetic test population.

See: [`AI-006-pondgpt/`](./AI-006-pondgpt/)

### AI-005 — DuckTalent AI

**Material risk:** Training data, ranking criteria, features, or proxies may systematically disadvantage protected or otherwise disadvantaged applicants and restrict fair access to employment.

**Preventive dependency:** `DT-01 — Job-Relevance Criteria & Proxy Feature Governance`

**Detective control demonstrated:** `DT-02 — Pre-Deployment Fairness & Adverse-Impact Testing`

The worked evidence package demonstrates:

- a synthetic approved-feature allow-list;
- 24 synthetic applicants arranged as 12 matched pairs;
- executable fairness/adverse-impact test logic;
- one deliberately seeded unapproved `Career_Gap_Months` scoring penalty;
- matched-pair score and group-level diagnostic metrics;
- detection of the unapproved feature and measurable disparity;
- pre-deployment gate blocking;
- generated exception evidence;
- remediation and full-population retesting;
- a control-test conclusion that successful retest permits only further governance review; and
- a synthetic governance gate decision that reviews the available evidence, denies advancement to a real-applicant pilot, records blocking conditions, and defines a reassessment trigger.

See: [`AI-005-ducktalent/`](./AI-005-ducktalent/)

Governance decision: [`AI-005_2026-09-02_GOV_Governance_Gate_Decision_Record.md`](./AI-005-ducktalent/AI-005_2026-09-02_GOV_Governance_Gate_Decision_Record.md)

Post-decision monitoring / reassessment: [`../12-monitoring-reporting-and-roadmap/AI-005-ducktalent/`](../12-monitoring-reporting-and-roadmap/AI-005-ducktalent/)

Internal audit and corrective action: [`../11-assurance-testing-and-evaluation/04-internal-audit-and-corrective-action/AI-005-ducktalent/`](../11-assurance-testing-and-evaluation/04-internal-audit-and-corrective-action/AI-005-ducktalent/)

## Important Limitation

Duckworks is a fictional portfolio organization.

All execution records, test identities, source permissions, alerts, exceptions, code execution, and control results in this folder are **synthetic portfolio evidence** created solely to demonstrate governance operating-model, technical-control, and assurance design.

They do **not** constitute:

- real production records;
- measured WingInspect model performance;
- verified manufacturing outcomes;
- actual PondGPT identity, connector, RAG, DLP, or SIEM activity;
- validated production authorization inheritance;
- real DuckTalent applicants, protected-characteristic data, production features, model behavior, fairness outcomes, accessibility results, or legal discrimination conclusions;
- a real Duckworks AI Governance Committee meeting, real executive approval/non-approval, or real lifecycle authorization;
- continuous production DuckTalent monitoring, real change telemetry, real reassessment operation, or real production suspension/authorization;
- longitudinal control-effectiveness evidence;
- demonstrated reduction of current residual risk; or
- independent assurance over a live environment.

Synthetic evidence may demonstrate control design, workflow logic, technical testability, and reproducible evidence generation, but it does not justify additional production residual-risk reduction credit.
