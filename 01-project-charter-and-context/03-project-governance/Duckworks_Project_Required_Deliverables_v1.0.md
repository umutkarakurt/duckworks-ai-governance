# Duckworks AI Governance Project — Required Deliverables

The minimum artifact set required to move Duckworks from scattered AI adoption to an auditable governance baseline.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Document ID<br />
</strong>DW-WING-CHTR-05</th>
<th><strong>Version<br />
</strong>1.0</th>
<th><strong>Status<br />
</strong>Portfolio Baseline</th>
<th><strong>Organization<br />
</strong>Duckworks</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 1. Purpose

This document defines the required outputs of the initial Duckworks AI Governance Project. Deliverables are organized as a dependency chain: foundational governance artifacts must exist before system decisions, control testing, reporting, and assurance can be considered complete.

Duckworks delivery principle: “A pretty policy without an owner, workflow, evidence trail, and operating decision is decoration—not governance.”

## 2. Deliverable Families

- **Charter & context —** why the project exists, what it covers, assumptions, stakeholders, and success criteria.

- **Inventory & intake —** what AI exists and how new use cases enter governance.

- **Assessment —** how risk and impact are evaluated and documented.

- **Controls & policy —** what must be done, by whom, and with what evidence.

- **Monitoring & assurance —** how Duckworks knows controls continue to work and can prove it.

- **Executive reporting —** how leadership receives a prioritized portfolio view rather than raw technical data.

## 3. Required Deliverables Register

| **ID** | **Deliverable**                                 | **Purpose**                                                                                                          | **Owner**                              | **Format**        | **Status**   | **Completion Evidence**                           |
|--------|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------|-------------------|--------------|---------------------------------------------------|
| DEL-01 | Executive Case Study                            | Concise organization, objectives, scope, assumptions, and key findings.                                              | Project Sponsor / AI Governance Lead   | DOCX / PDF        | Complete     | Executive baseline approved                       |
| DEL-02 | Business Scenario                               | Narrative describing Project W.I.N.G., business drivers, seven systems, and governance problem.                      | AI Governance Lead                     | DOCX              | Complete     | Scenario consistent with inventory                |
| DEL-03 | Project Objectives                              | Defined primary and specific objectives with target outcome.                                                         | AI Governance Lead                     | DOCX              | Complete     | Objectives trace to deliverables                  |
| DEL-04 | In-Scope / Out-of-Scope                         | Formal project boundaries and future-scope items.                                                                    | AI Governance Lead                     | DOCX              | Complete     | No material scope ambiguity                       |
| DEL-05 | Stakeholder Register                            | Named executive, first/second/third-line, affected, and representative stakeholders.                                 | AI Governance Lead                     | DOCX              | Required     | Roles and engagement model approved               |
| DEL-06 | Assumptions Register                            | Controlled assumptions with materiality and validation requirements.                                                 | AI Governance Lead + System Owners     | DOCX / XLSX       | Required     | Critical assumptions identifiable                 |
| DEL-07 | Acceptance Criteria                             | Measurable conditions for project and artifact acceptance.                                                           | Project Sponsor                        | DOCX              | Required     | Evidence and approvers defined                    |
| DEL-08 | QuackTrack AI System Inventory                  | Central register of approved, pilot, planned, and discovered AI use cases.                                           | AI Governance Lead                     | XLSX              | Complete     | All seven baseline entries populated              |
| DEL-09 | Pond-to-Production AI Intake Form & Workflow    | Standard intake and lifecycle gate workflow for new or materially changed AI.                                        | AI Governance + Technology             | DOCX / form       | Planned      | New material AI cannot bypass registration        |
| DEL-10 | AI Risk Classification & Assessment Methodology | Risk domains, 5x5 criteria, inherent/current/target residual method, treatment and escalation.                       | Risk & Compliance                      | DOCX              | Complete     | Repeatable, auditable methodology                 |
| DEL-11 | System Risk Assessment Pack                     | Risk assessments applied to all seven baseline entries.                                                              | System Owners + Risk                   | DOCX / XLSX       | Complete     | Scores trace to scenarios/controls                |
| DEL-12 | AI Impact Assessment Pack                       | Impact assessments for all seven entries, including affected persons and safeguards.                                 | System Owners + AI Governance          | DOCX              | Complete     | Decision and monitoring conditions documented     |
| DEL-13 | AI Governance Operating Model                   | Committee charter, decision rights, escalation, three-lines model, and governance lifecycle.                         | CRCO / AI Governance Lead              | DOCX              | Planned      | Decision authority is unambiguous                 |
| DEL-14 | Duckworks AI RACI                               | Responsibility matrix across lifecycle and specialist review activities.                                             | AI Governance Lead                     | XLSX / DOCX       | Planned      | Every key activity has one accountable owner      |
| DEL-15 | AI Control Library                              | Control objectives, owners, frequency, evidence, testing, risks, mappings, and implementation status.                | Risk / Security / Privacy / Technology | XLSX              | Planned      | Controls trace to material risks                  |
| DEL-16 | FeatherSafe AI Acceptable Use Standard          | Rules for public GenAI, sensitive data, approved tools, prohibited practices, reporting, and exceptions.             | CISO + CRCO                            | DOCX              | Planned      | Shadow AI containment requirements clear          |
| DEL-17 | Third-Party AI Due Diligence Questionnaire      | AI-specific supplier security, privacy, training data, change, incident, IP, resilience, and exit review.            | Procurement + Security + Privacy       | DOCX / XLSX       | Planned      | No material AI vendor bypasses due diligence      |
| DEL-18 | AI Incident & Escalation Playbook               | AI-specific incident taxonomy, triage, escalation, containment, evidence, regulatory/legal handoff, lessons learned. | CISO + AI Governance                   | DOCX              | Planned      | Material AI incidents have defined route          |
| DEL-19 | Human Oversight Standard                        | Competence, override authority, escalation, logging, contestability, and automation-bias safeguards.                 | AI Governance + Business Owners        | DOCX              | Planned      | High-impact decisions retain meaningful oversight |
| DEL-20 | AI Monitoring & Reassessment Standard           | KPIs/KRIs, drift, complaints, override, incident, vendor/model change, and reassessment triggers.                    | Data & AI + Risk                       | DOCX              | Planned      | Post-deployment monitoring is explicit            |
| DEL-21 | DuckPond Governance Dashboard                   | Portfolio metrics: inventory, lifecycle, risk, approvals, overdue actions, vendors, incidents, reassessments.        | AI Governance Lead                     | XLSX / BI mock-up | Planned      | Management can prioritize from one view           |
| DEL-22 | Framework / Legislation Reference File          | Public authoritative source catalogue and system applicability map.                                                  | AI Governance Lead                     | MD                | Complete     | Official-source references maintained             |
| DEL-23 | AI Assurance & Internal Audit Program           | Risk-based audit universe, control tests, evidence expectations, and sample workpapers.                              | Internal Audit                         | DOCX / XLSX       | Future phase | Independent assurance can be executed             |
| DEL-24 | Implementation Roadmap                          | 90-day / six-month sequence, owners, dependencies, quick wins, and key decision gates.                               | AI Governance Lead                     | DOCX / XLSX       | Planned      | Prioritized implementation path approved          |

## 4. Minimum Repository Structure

duckworks-ai-governance/
├── 00-executive-case-study/
├── 01-project-charter/
├── 02-ai-inventory-and-intake/
├── 03-risk-assessment/
├── 04-impact-assessments/
├── 05-governance-operating-model/
├── 06-control-framework/
├── 07-policies-and-standards/
├── 08-third-party-governance/
├── 09-monitoring-and-dashboard/
├── 10-assurance/
├── 11-roadmap/
└── REFERENCES.md

## 5. Deliverable Dependency Sequence

1.  Approve context: scenario, objectives, scope, stakeholders, assumptions, acceptance criteria.

2.  Establish visibility: inventory and intake workflow.

3.  Assess: risk methodology, risk assessments, and impact assessments.

4.  Govern: operating model, RACI, policy/standards, control library, supplier requirements.

5.  Operate: monitoring, incident management, reassessment, evidence collection.

6.  Assure and report: management dashboard, roadmap, and independent assurance plan.

## Portfolio Disclaimer

Duckworks, Project W.I.N.G., all personnel, committees, systems, datasets, decisions, and evidence referenced in this document are fictional and were created solely for educational and professional portfolio purposes.
