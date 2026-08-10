# Duckworks AI Risk Classification & Assessment Methodology

A practical governance and risk-assessment method for Duckworks AI systems

| **Organization**    | Duckworks (fictional)                  |
|---------------------|----------------------------------------|
| **Document status** | Version 1.0                            |
| **Assessment date** | 9 August 2026                          |
| **Classification**  | Portfolio / Synthetic / Non-production |

**Purpose.** This document demonstrates a risk-based AI governance approach for a fictional advanced-manufacturing company. It is not legal advice, certification evidence, or a statement of compliance.

## 1. Purpose and scope

This methodology establishes how Duckworks identifies, classifies, assesses, treats, approves and monitors risks arising from AI systems across their lifecycle. It applies to internally developed AI, third-party AI services, AI embedded in products or business processes, pilots, experiments, and discovered “shadow AI” use.

| **Key design choice.** Regulatory classification and Duckworks internal enterprise risk classification are separate. A system can be legally “high-risk” while also receiving a Duckworks High or Critical rating; conversely, a system can be internally High because of safety or confidentiality even when no EU AI Act high-risk category is identified. |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## 2. Methodological basis

The method is informed by the NIST AI Risk Management Framework (AI RMF), ISO/IEC 42001:2023, ISO/IEC 23894:2023, ISO/IEC 42005:2025, and the EU Artificial Intelligence Act as consolidated on 27 July 2026. It is a Duckworks portfolio methodology, not a reproduction of any standard and not a claim of conformity.

- NIST AI RMF provides the overall Govern–Map–Measure–Manage orientation for AI risk management.

- ISO/IEC 42001 informs management-system governance, accountability, lifecycle controls and continual improvement.

- ISO/IEC 23894 informs AI-specific risk-management integration and treatment.

- ISO/IEC 42005 informs impact-assessment thinking for effects on individuals and society.

- The EU AI Act provides legal screening for prohibited practices, high-risk classifications and transparency obligations where applicable.

## 3. Governance principles

| **Principle**                 | **Duckworks rule**                                                                                                                    |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Intended purpose first        | Assess the actual intended use, affected persons and decisions—not merely the model type.                                             |
| Scenario-based risk           | Score concrete cause → event → impact scenarios, not generic labels such as “bias risk.”                                              |
| No averaging away severe harm | The system rating is driven by the highest material scenario rather than an average that could dilute a severe safety or rights risk. |
| Controls require evidence     | Planned controls receive no credit as implemented controls. Evidence confidence is recorded separately.                               |
| Residual risk is re-assessed  | Controls do not mathematically divide the inherent score. Severity and likelihood are reconsidered after operating controls.          |
| Lifecycle governance          | Assessment is repeated after material change, significant incidents, drift, new data sources, new integrations or regulatory changes. |

## 4. Roles and accountability

| **Role**                               | **Primary accountability**                                                                       | **Independence / challenge**                                                |
|----------------------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| Business / AI System Owner             | Owns intended purpose, use case, treatment plan, operating controls and risk acceptance request. | Cannot self-approve High/Critical residual risk.                            |
| Technical Owner / Data & AI            | Architecture, model/service implementation, testing, monitoring and change evidence.             | Provides technical evidence; does not determine legal classification alone. |
| AI Governance Lead / Risk & Compliance | Runs methodology, challenges scoring, maintains inventory and committee reporting.               | Second-line challenge.                                                      |
| CISO / Security                        | AI security, data leakage, integrations, threat modelling and security testing.                  | Independent security challenge.                                             |
| Legal / Privacy / HR SMEs              | Legal classification, privacy, employment, consumer and rights analysis.                         | Required for affected domains.                                              |
| AI Governance Committee                | Approves material High risks, exceptions, risk treatment and production gates.                   | Cross-functional decision body.                                             |
| Internal Audit                         | Independent assurance over design and operation of governance/controls.                          | Does not own or design first/second-line controls.                          |

## 5. Assessment workflow

| **Stage**                  | **Required activity**                                                                                                                   | **Output**                               |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| 1 — Inventory & scope      | Confirm intended purpose, lifecycle, owner, users, affected persons, data, model/provider, integrations, geographies and decision role. | Validated inventory entry                |
| 2 — Regulatory triage      | Screen prohibited practices, EU AI Act high-risk routes, transparency obligations and other applicable law.                             | Legal classification / legal-review flag |
| 3 — Context criticality    | Identify people/rights, safety, privacy, security, reliability, autonomy, scale, reversibility and third-party factors.                 | Assessment context                       |
| 4 — Risk scenarios         | Write material cause → event → impact scenarios across Duckworks risk domains.                                                          | Risk scenario register                   |
| 5 — Inherent scoring       | Score severity and likelihood assuming no specific Duckworks mitigating controls.                                                       | Inherent rating                          |
| 6 — Control assessment     | Credit only implemented controls and assess evidence confidence.                                                                        | Control effectiveness                    |
| 7 — Residual scoring       | Re-score severity and likelihood after implemented controls.                                                                            | Current residual rating                  |
| 8 — Treatment & monitoring | Define treatment, target residual, KPIs/KRIs, review cadence and approval authority.                                                    | Treatment/monitoring plan                |

## 6. Regulatory and legal triage

Regulatory triage is a gate, not a risk multiplier. The assessor records the preliminary classification and obtains Legal/Compliance confirmation when required. A prohibited or otherwise unlawful use cannot be approved simply because its internal numerical risk score is low.

- Prohibited-practice screening: determine whether the intended practice falls within an applicable prohibition.

- High-risk screening: evaluate Article 6 and the relevant Annex I / Annex III route. For Annex III, document any reliance on the Article 6(3) derogation and the basis for it.

- Transparency screening: identify systems that directly interact with natural persons or generate/manipulate content where Article 50 duties may apply.

- Role classification: determine whether Duckworks is acting as provider, deployer, importer/distributor or may become a provider because of rebranding or substantial/intended-purpose modification.

- Other law: privacy/data protection, employment, product safety, consumer protection, cybersecurity, intellectual property and sector-specific requirements remain separate applicability questions.

| **Current legal timing used in this portfolio.** The consolidated EU AI Act applies generally from 2 August 2026. Following Regulation (EU) 2026/1744, Chapter III Sections 1–3 for AI systems classified as high-risk under Article 6(2) and Annex III apply from 2 December 2027. DuckTalent is therefore treated as a high-risk design target now, while the document clearly distinguishes future application dates from current governance good practice. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## 7. Risk domains

| **Risk domain**                               | **Assessment lens**                                                                          |
|-----------------------------------------------|----------------------------------------------------------------------------------------------|
| Fundamental rights, fairness & discrimination | Unequal treatment, accessibility, discrimination, exclusion or other adverse rights impacts. |
| Safety & physical harm                        | Physical injury, unsafe product outcomes, hazardous operating decisions.                     |
| Privacy & data governance                     | Personal data, confidentiality, IP, data minimization, provenance and retention.             |
| Security, abuse & adversarial manipulation    | Prompt injection, data poisoning, model abuse, exfiltration, insecure tools/integrations.    |
| Reliability, robustness & model performance   | Hallucination, accuracy, drift, distribution shift, brittleness, instability.                |
| Transparency & explainability                 | Disclosure, traceability, understandable output/limitations, contestability.                 |
| Human oversight & automation bias             | Over-reliance, ineffective review, inappropriate autonomy, unclear accountability.           |
| Third-party & supply chain                    | Vendor/model dependencies, contractual terms, sub-processors, model/service changes.         |
| Operational, financial & reputational         | Service disruption, poor planning, cost, customer complaints, brand impact.                  |
| Legal, regulatory & compliance                | Applicable legal duties, documentation, approval, recordkeeping and control failure.         |

## 8. Scenario formulation

Each material risk is written as a scenario:

**CAUSE → EVENT → IMPACT**

Example: Because candidate ranking uses historical or proxy features (cause), DuckTalent systematically ranks one group lower (event), resulting in discriminatory access to employment and regulatory/reputational harm (impact).

## 9. Inherent risk scoring

For each material scenario, inherent risk is assessed before crediting specific Duckworks mitigating controls:

**Inherent Risk Score = Severity × Likelihood**

### 9.1 Severity scale

| **Score**      | **Anchor**                                                                                                                        |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| 1 — Negligible | Minimal reversible effect; no material rights, safety, privacy, security or business impact.                                      |
| 2 — Minor      | Limited/localized effect; straightforward remediation; low sensitivity.                                                           |
| 3 — Moderate   | Meaningful impact on individuals or operations; recoverable with management action.                                               |
| 4 — Major      | Significant rights, privacy, security, financial, operational or reputational impact; substantial remediation.                    |
| 5 — Severe     | Potential serious physical harm, systemic fundamental-rights harm, major IP/confidentiality breach, or broad/irreversible impact. |

### 9.2 Likelihood scale

| **Score**          | **Anchor**                                                                                            |
|--------------------|-------------------------------------------------------------------------------------------------------|
| 1 — Rare           | Requires an exceptional combination of conditions; no meaningful evidence of recurrence.              |
| 2 — Unlikely       | Credible but uncommon in normal use; limited exposure or difficult-to-trigger failure mechanism.      |
| 3 — Possible       | Foreseeable in ordinary or reasonably foreseeable use.                                                |
| 4 — Likely         | Expected to occur repeatedly without effective controls; frequent exposure or attractive attack path. |
| 5 — Almost Certain | Persistent, observed or structurally expected condition absent redesign.                              |

### 9.3 Risk matrix and governance thresholds

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Likelihood ↓ / Severity →</strong></th>
<th><strong>1</strong></th>
<th><strong>2</strong></th>
<th><strong>3</strong></th>
<th><strong>4</strong></th>
<th><strong>5</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>1<br />
Low</td>
<td>2<br />
Low</td>
<td>3<br />
Low</td>
<td>4<br />
Low</td>
<td>5<br />
Moderate</td>
</tr>
<tr class="even">
<td>2</td>
<td>2<br />
Low</td>
<td>4<br />
Low</td>
<td>6<br />
Moderate</td>
<td>8<br />
Moderate</td>
<td>10<br />
High</td>
</tr>
<tr class="odd">
<td>3</td>
<td>3<br />
Low</td>
<td>6<br />
Moderate</td>
<td>9<br />
Moderate</td>
<td>12<br />
High</td>
<td>15<br />
High</td>
</tr>
<tr class="even">
<td>4</td>
<td>4<br />
Low</td>
<td>8<br />
Moderate</td>
<td>12<br />
High</td>
<td>16<br />
High</td>
<td>20<br />
Critical</td>
</tr>
<tr class="odd">
<td>5</td>
<td>5<br />
Moderate</td>
<td>10<br />
High</td>
<td>15<br />
High</td>
<td>20<br />
Critical</td>
<td>25<br />
Critical</td>
</tr>
</tbody>
</table>

| **Rating** | **Score** | **Governance response**                                                                                                     |
|------------|-----------|-----------------------------------------------------------------------------------------------------------------------------|
| Low        | 1–4       | Owner acceptance; routine controls; at least annual review.                                                                 |
| Moderate   | 5–9       | Owner + AI Governance review; documented controls and monitoring.                                                           |
| High       | 10–16     | AI Governance Committee approval/treatment; enhanced evidence; pre-production gate.                                         |
| Critical   | 17–25     | Deployment/continued use normally blocked pending treatment or exceptional executive risk acceptance; immediate escalation. |

## 10. Control effectiveness and evidence confidence

| **Control effectiveness**     | **Meaning**                                                                        | **Evidence expectation**      |
|-------------------------------|------------------------------------------------------------------------------------|-------------------------------|
| Not Implemented / Ineffective | No meaningful operating control or control fails its objective.                    | No reliable evidence          |
| Weak                          | Ad hoc or incomplete control; material gaps remain.                                | Limited evidence              |
| Partially Effective           | Control operates but coverage, consistency or testing is incomplete.               | Some evidence; gaps tracked   |
| Effective                     | Implemented, appropriately designed and operating with supporting evidence.        | Repeatable evidence           |
| Strong / Verified             | Effective control plus mature monitoring and independent/second-line verification. | High-quality current evidence |

Evidence confidence is recorded as Low, Medium or High. A High/Critical inherent-risk system should not be represented as Low residual risk when the evidence supporting its controls is weak or unverified. This is a governance override rather than a mathematical adjustment.

## 11. Residual risk, target risk and risk treatment

Current residual risk reflects the risk remaining after controls that are actually implemented and operating. Target residual risk is the planned rating after additional treatment and must not be reported as the current state.

- Avoid / stop the use case when risk is outside tolerance or the practice is unlawful.

- Reduce through technical, organizational, human-oversight, data, security and process controls.

- Transfer/share selected financial or contractual exposures where appropriate; accountability is not transferred by contract alone.

- Accept within delegated authority when residual risk is within appetite and documented.

- Retire/decommission when risk cannot be managed or business value no longer justifies exposure.

## 12. Risk appetite and approval rules

- No appetite for prohibited/unlawful AI practices, intentional discrimination, or knowingly bypassing required human authority.

- Very low tolerance for unmanaged safety risk, systemic fundamental-rights impact and uncontrolled restricted-data exposure.

- High residual risk requires AI Governance Committee approval plus a dated treatment plan and monitoring.

- Critical residual risk normally blocks production deployment or requires explicit exceptional executive acceptance with Legal, Risk and Security challenge.

- Risk acceptance expires when material assumptions, intended purpose, provider/model, data scope or controls change.

## 13. Review and reassessment triggers

- Change in intended purpose, autonomy or decision authority.

- New model/provider/version or substantial configuration change.

- New data categories, sensitive sources, connectors, APIs or permissions.

- Expansion to new users, affected groups, countries or product lines.

- Material incident, near miss, complaint, security event or rights challenge.

- Drift, performance threshold breach or change in error distribution.

- Control failure or evidence expiry.

- New or amended legal/regulatory requirement.

- Transition between lifecycle gates, especially pilot → production.

## 14. Minimum assessment record

- AI ID and intended purpose

- Business/technical/data owners

- Lifecycle and deployment context

- Users and affected persons

- Data and integrations

- Preliminary legal/regulatory classification

- Material risk scenarios by domain

- Inherent severity/likelihood/score

- Implemented controls and evidence

- Control effectiveness and evidence confidence

- Residual severity/likelihood/score

- Target controls and target residual risk

- Risk owner and approval authority

- KPIs/KRIs and monitoring cadence

- Review triggers and next assessment date

## 15. References

1\. NIST, Artificial Intelligence Risk Management Framework (AI RMF 1.0): [<u>https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf</u>](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)

2\. NIST AI Resource Center, AI RMF Playbook: [<u>https://airc.nist.gov/airmf-resources/playbook/</u>](https://airc.nist.gov/airmf-resources/playbook/)

3\. ISO/IEC 42001:2023 — Artificial intelligence — Management system: [<u>https://www.iso.org/standard/42001</u>](https://www.iso.org/standard/42001)

4\. ISO/IEC 23894:2023 — Artificial intelligence — Guidance on risk management: [<u>https://www.iso.org/standard/77304.html</u>](https://www.iso.org/standard/77304.html)

5\. ISO/IEC 42005:2025 — Artificial intelligence — AI system impact assessment: [<u>https://www.iso.org/standard/42005</u>](https://www.iso.org/standard/42005)

6\. EU Artificial Intelligence Act — consolidated text as of 27 July 2026: [<u>https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R1689-20260727</u>](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R1689-20260727)

7\. Regulation (EU) 2026/1744 — Digital Omnibus on AI: [<u>https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng</u>](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng)

Note: ISO standards are copyrighted publications. This portfolio document references their public descriptions and does not reproduce the standards.
