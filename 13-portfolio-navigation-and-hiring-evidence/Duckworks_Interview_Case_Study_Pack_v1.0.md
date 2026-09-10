# Duckworks Interview Case Study Pack v1.0

## How to use this pack

Each case is anchored to repository evidence. Use the short answer first, then expand only when asked. State the evidence limitation without prompting.

## Case 1 — Converting governance design into an operating control

**Question:** Give an example of moving from policy language to an auditable control.

**Answer:** For WingInspect Vision, I translated the risk of a missed manufacturing defect into `WI-01`, a mandatory human release gate. A qualified inspector must record accept or reject, the item and inspector identifiers, the timestamp and any override rationale before release. I created synthetic execution records and a control-test workpaper to demonstrate the audit trail. The evidence supports the control design and test method, but it does not prove production operation or defect-risk reduction.

**Evidence:** [`80-operating-evidence/AI-004-winginspect/`](../80-operating-evidence/AI-004-winginspect/)

## Case 2 — Using executable tests to enforce an AI-security boundary

**Question:** How have you connected GRC requirements to technical validation?

**Answer:** For PondGPT, I linked the permission-aware retrieval control to an executable authorization-regression test. The synthetic matrix includes permitted, denied, excluded and DLP-blocked sources. A seeded Finance connector ACL defect produces an exception and blocks expansion. After remediation, the full population is retested. Passing the test satisfies one technical prerequisite; it does not establish live production authorization inheritance or approval to deploy.

**Evidence:** [`80-operating-evidence/AI-006-pondgpt/`](../80-operating-evidence/AI-006-pondgpt/)

## Case 3 — Responding to evidence that contradicts an earlier decision

**Question:** Describe a situation where governance had to survive change.

**Answer:** DuckTalent initially failed because an unapproved career-gap feature influenced ranking. The feature was removed and the fairness control passed on retest, but the system remained blocked because other prerequisites were unresolved. I then modelled a later material-change event that reintroduced the prohibited feature. The regression monitor detected it, opened an incident, triggered reassessment and produced a revised decision that rejected the change and preserved the deployment block.

**Evidence:** [`12-monitoring-reporting-and-roadmap/AI-005-ducktalent/`](../12-monitoring-reporting-and-roadmap/AI-005-ducktalent/)

## Case 4 — Governing third-party AI risk

**Question:** How would you make an AI supplier decision with incomplete evidence?

**Answer:** In the PondGPT supplier case, I structured intake, an 18-item due-diligence evidence register, supplier-risk scenarios and proposed contract controls. The gate is conditional because critical evidence is incomplete. The package includes monitoring, exit design and a material-change event that blocks progression. This demonstrates disciplined decision conditions without pretending that a template or vendor statement proves control effectiveness.

**Evidence:** [`09-third-party-ai-governance/02-worked-supplier-case/AI-006-pondgpt/`](../09-third-party-ai-governance/02-worked-supplier-case/AI-006-pondgpt/)

## Case 5 — Preserving assurance independence and narrow closure

**Question:** How do you prevent an audit finding from being closed too broadly?

**Answer:** The DuckTalent corrective-action chain separates the finding, root cause, action owner, remediation evidence, effectiveness test, management review and closure decision. The finding closes only after the defined recurrence-prevention test passes. Closure does not reduce the system risk rating, remove the deployment block or assert production effectiveness. Internal Audit evaluates the evidence but does not own the underlying control.

**Evidence:** [`11-assurance-testing-and-evaluation/04-internal-audit-and-corrective-action/AI-005-ducktalent/`](../11-assurance-testing-and-evaluation/04-internal-audit-and-corrective-action/AI-005-ducktalent/)

## Case 6 — Building an ISO/IEC 42001 readiness view without claiming conformity

**Question:** How would you organize an ISO/IEC 42001 readiness programme?

**Answer:** I built a thematic evidence baseline and master crosswalk linking systems, risks, controls, evidence, decisions, triggers, findings and AIMS themes. Later releases added objectives, competence and document control, management review, control applicability and a risk-based internal-audit programme. The crosswalk supports readiness planning and traceability. It is not a clause-by-clause conformity determination, certification audit or legal opinion.

**Evidence:** [`11-assurance-testing-and-evaluation/03-iso42001/`](../11-assurance-testing-and-evaluation/03-iso42001/)

## Ninety-second walkthrough

> Duckworks is a fictional European technology and advanced-manufacturing organization with seven AI portfolio entries. I began with inventory, risk classification, impact assessment, ownership and lifecycle gates. I then built three different operating-evidence archetypes: a human-authority control for WingInspect, executable authorization testing for PondGPT and fairness testing with change-triggered reassessment for DuckTalent. The evidence feeds governance decisions rather than automatically approving deployment. I extended the portfolio into supplier governance, corrective action, management review, control applicability and internal-audit planning. The master crosswalk connects 45 controls and 70 evidence records. Every synthetic or unavailable production record is marked so the portfolio demonstrates assurance reasoning without claiming real deployment, certification or legal compliance.

## Evidence-bound closing statement

> The portfolio shows how I design and challenge an AI governance system. Its strongest proof is reproducible control logic and traceable decision-making. Its main limitation is that Duckworks is synthetic, so real-world authority, sustained operation and production effectiveness still require external validation.

