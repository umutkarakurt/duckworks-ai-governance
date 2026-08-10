# Duckworks AI Governance Project — Acceptance Criteria

Measurable completion conditions for the project, its core artifacts, and the initial seven-system governance baseline.

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
</strong>DW-WING-CHTR-06</th>
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

Acceptance criteria define the minimum conditions under which the initial Duckworks AI Governance Project can be considered complete and fit for portfolio demonstration. They are written as evidence-based criteria rather than subjective statements such as “looks good” or “appears compliant.”

Duckworks acceptance principle: “If a reviewer cannot point to the evidence, the criterion is not met.”

## 2. Acceptance Status

- **Pass —** criterion is fully met and evidence is available.

- **Pass with Action —** criterion is materially met but a defined non-blocking action remains.

- **Fail —** criterion is not met or evidence is insufficient.

- **Not Applicable —** not relevant to the approved project scope; rationale must be recorded.

## 3. Project-Level Acceptance Criteria

| **ID** | **Area**               | **Acceptance Criterion**                                                                                                                                               | **Required Evidence**                                                                      | **Owner**                    | **Approver**                |
|--------|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|------------------------------|-----------------------------|
| AC-01  | Scope                  | All seven baseline entries are covered by the inventory and assessment pack.                                                                                           | Inventory contains AI-001 through AI-007; no baseline entry omitted.                       | AI Governance Lead           | CRCO                        |
| AC-02  | Ownership              | Every material AI system has a named business owner and technical owner, or an explicit governance exception.                                                          | Inventory ownership fields completed; AI-007 explicitly treated as uncontrolled condition. | AI Governance Lead           | CRCO                        |
| AC-03  | Purpose                | Every governed system has a documented intended purpose and decision/support boundary.                                                                                 | Inventory + system impact assessment.                                                      | System Owner                 | AI Governance Committee     |
| AC-04  | Risk method            | Risk methodology defines severity, likelihood, thresholds, inherent/current/target residual risk, control credit, treatment, and escalation.                           | Approved methodology document.                                                             | Risk & Compliance            | CRCO                        |
| AC-05  | Risk assessment        | All seven entries have documented risk scenarios and current residual risk conclusions.                                                                                | Risk Assessment Report + workbook.                                                         | System Owner + Risk          | AI Governance Committee     |
| AC-06  | Impact assessment      | All seven entries have impact assessments that identify affected parties, benefits, adverse impacts, safeguards, monitoring, and decision.                             | Seven AIA documents + pack index.                                                          | System Owner + AI Governance | AI Governance Committee     |
| AC-07  | Legal separation       | Internal risk classification is clearly separated from legal/regulatory classification.                                                                                | Methodology, assessments, and references use distinct terminology.                         | AI Governance Lead           | General Counsel / CRCO      |
| AC-08  | Critical risk handling | No system with Critical current residual risk is described as cleared for unrestricted production.                                                                     | DuckTalent blocked; shadow AI containment decision recorded.                               | System Owner                 | CRCO / Executive escalation |
| AC-09  | Human oversight        | High-impact systems document who can review, override, escalate, and stop AI-supported decisions.                                                                      | AIA + risk assessment + oversight requirements.                                            | Business Owner               | AI Governance Committee     |
| AC-10  | Shadow AI              | Unregistered GenAI is treated as a discovery/containment problem and requires decomposition into individual use cases.                                                 | AI-007 AIA + governance action.                                                            | CISO / AI Governance         | CRCO                        |
| AC-11  | Sources                | Public legal/framework claims used in the portfolio are traceable to authoritative sources.                                                                            | REFERENCES.md or equivalent source file.                                                   | AI Governance Lead           | General Counsel / Risk      |
| AC-12  | Confidentiality        | No real employer-confidential, customer, employee, applicant, or government data is required to understand the portfolio.                                              | Artifact review confirms fictional/synthetic data and disclaimer.                          | AI Governance Lead           | Project Sponsor             |
| AC-13  | Consistency            | System names, owners, lifecycle states, risk ratings, and decisions are consistent across core documents.                                                              | Cross-artifact QA checklist.                                                               | AI Governance Lead           | Project Sponsor             |
| AC-14  | Auditability           | Material conclusions identify evidence or expected evidence sufficient for later control testing.                                                                      | Control/evidence fields and assessment actions.                                            | Control Owner                | Internal Audit observer     |
| AC-15  | Traceability           | At least each High/Critical system can be traced from inventory -\> impact -\> risk -\> treatment/decision -\> monitoring requirement.                                 | Unique system IDs retained across artifacts.                                               | AI Governance Lead           | CRCO                        |
| AC-16  | Proportionality        | Governance requirements vary according to impact/risk rather than applying the same review intensity to every system.                                                  | FeatherForecast vs DuckTalent/Shadow AI treatment demonstrates tiering.                    | Risk & Compliance            | AI Governance Committee     |
| AC-17  | Independence           | Internal Audit is not assigned operational ownership of controls it may later assure.                                                                                  | Stakeholder/RACI review.                                                                   | Head of Internal Audit       | Audit & Risk Committee      |
| AC-18  | Change triggers        | Material changes in purpose, model, data, vendor, affected population, integration, or legal context trigger reassessment.                                             | Methodology + monitoring/reassessment requirement.                                         | AI Governance Lead           | CRCO                        |
| AC-19  | Management view        | A management-level summary can identify portfolio size, lifecycle, high/critical risk, blocked systems, and priority actions without reading all detailed assessments. | Dashboard / executive summary.                                                             | AI Governance Lead           | CEO / CRCO                  |
| AC-20  | Portfolio usability    | A hiring manager can understand the scenario, methods, decisions, and limitations from the repository without private context.                                         | README / executive case study / structured folders.                                        | Portfolio Owner              | Project Sponsor             |

## 4. Artifact Quality Criteria

| **ID** | **Quality Area**          | **Criterion**                                                                                           |
|--------|---------------------------|---------------------------------------------------------------------------------------------------------|
| Q-01   | Versioning                | Core artifacts carry a title, version, and document identifier.                                         |
| Q-02   | Terminology               | Use “AI system,” “risk rating,” “legal classification,” “control,” and “impact” consistently.           |
| Q-03   | Assumptions               | Material unknowns are labeled as assumptions rather than presented as verified facts.                   |
| Q-04   | Evidence                  | Claims of control implementation are supported by evidence or explicitly marked planned/not validated.  |
| Q-05   | Decision clarity          | Each impact assessment states a current lifecycle decision or restriction.                              |
| Q-06   | No false compliance claim | Artifacts do not state that framework alignment equals certification or legal compliance.               |
| Q-07   | Readability               | Tables are legible, headings are structured, and executive sections avoid unnecessary technical detail. |
| Q-08   | Portfolio disclaimer      | Each externally shareable artifact makes clear that Duckworks and its data are fictional.               |

## 5. System-Specific Release / Governance Gates

| **System**               | **Current Gate**                 | **Minimum Acceptance Conditions**                                                                                                    | **Current Impact** |
|--------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| DuckDesign AI            | Restricted pilot only            | Competent engineer review; design validation; IP/data controls; no autonomous release to production design.                          | High               |
| QuackBot                 | Production blocked pending gates | Prompt/RAG security testing; safe escalation; content boundaries; monitoring; customer-impact safeguards.                            | High               |
| FeatherForecast          | Continue with monitoring         | Manager approval for material commitments; drift/performance monitoring; data-quality controls.                                      | Moderate           |
| WingInspect Vision       | Restricted pilot only            | Human inspector remains final authority; false-negative testing; no unvalidated safety-critical reliance.                            | High               |
| DuckTalent AI            | Do not deploy in current state   | Enhanced legal/privacy/fairness analysis; meaningful human review; bias testing; transparency/contestability; critical risk reduced. | Critical           |
| PondGPT                  | Restricted pilot only            | Enterprise access enforcement; sensitive repository exclusions; prompt/RAG security; logging; acceptable-use controls.               | High               |
| Unregistered GenAI Usage | Immediate containment            | Discover use cases; prevent sensitive uploads; approve tools; register material uses; investigate exposure.                          | Critical           |

## 6. Formal Project Acceptance

The project may be accepted when all blocking project-level criteria are marked Pass, any Pass-with-Action items have named owners and due dates, and no unresolved inconsistency undermines a Critical/High system decision. Acceptance of the governance project does not constitute approval of every AI system for production.

| **Acceptance Role**                           | **Acceptance Focus**                                                  |
|-----------------------------------------------|-----------------------------------------------------------------------|
| Project Sponsor — Dr. Mallory Duckworth       | Confirms business objectives and portfolio usability.                 |
| Governance Sponsor — Reginald Duckman         | Confirms governance model, risk method, and acceptance status.        |
| Technology Executive — Prof. Archibald McDuck | Confirms technical feasibility and ownership model.                   |
| CISO — Cassandra Duckley                      | Confirms security governance requirements are represented.            |
| Head of Internal Audit — Penelope Duckins     | Acknowledges assurance-readiness design while retaining independence. |

## Portfolio Disclaimer

Duckworks, Project W.I.N.G., all personnel, committees, systems, datasets, decisions, and evidence referenced in this document are fictional and were created solely for educational and professional portfolio purposes.
