# Duckworks AI Governance Project — Assumptions Register

Controlled assumptions that define the portfolio scenario, scope, scoring context, and evidence boundaries.

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
</strong>DW-WING-CHTR-04</th>
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

This register records the assumptions used to design the initial Duckworks AI governance program. Assumptions are not treated as facts: each material assumption should either be validated, converted into a confirmed project fact, or retained as an explicit limitation in the final assessment record.

Duckworks rule: an assumption that changes intended purpose, affected persons, legal role, safety impact, data category, or degree of automation can change the entire assessment and must trigger review.

## 2. Assumption Status

- **Open —** used for planning but not yet validated.

- **Validated —** supported by project evidence or an approved scenario decision.

- **Superseded —** replaced by a newer fact or assumption.

- **Critical —** if incorrect, could materially change risk, impact, or governance conclusions.

## 3. Assumptions Register

| **ID**  | **Category**                  | **Assumption**                                                                                                                                                      | **Status** | **Materiality** | **Why It Matters**                                                                       | **Validation / Evidence**          |
|---------|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|-----------------|------------------------------------------------------------------------------------------|------------------------------------|
| ASM-001 | Organization                  | Duckworks is a fictional European company employing approximately 1,200 people.                                                                                     | Validated  | Medium          | Defines organizational scale and scenario complexity.                                    | Project charter                    |
| ASM-002 | Geography                     | Duckworks operates primarily in the EU/EEA and sells products into European markets.                                                                                | Open       | High            | Drives EU regulatory screening and data/privacy considerations.                          | Validate jurisdiction per use case |
| ASM-003 | Governance maturity           | Duckworks has mature general security/risk processes but no established enterprise AI governance framework at project start.                                        | Validated  | High            | Justifies a readiness and operating-model project rather than a greenfield ERM redesign. | Business scenario                  |
| ASM-004 | AI portfolio                  | The seven inventory entries represent the initial material AI portfolio, not every future AI capability.                                                            | Validated  | Medium          | Defines baseline scope and allows later onboarding.                                      | AI inventory                       |
| ASM-005 | Human accountability          | Humans retain formal accountability for employment, product release, quality, procurement, and material customer decisions.                                         | Open       | Critical        | Human oversight affects impact, regulatory, and residual-risk conclusions.               | Validate per system                |
| ASM-006 | DuckTalent purpose            | DuckTalent parses, compares, ranks, and recommends job applicants but does not autonomously issue final rejection or hiring decisions.                              | Validated  | Critical        | Materially affects employment impact and legal classification analysis.                  | DuckTalent AIA                     |
| ASM-007 | DuckDesign use                | DuckDesign outputs are advisory and require competent engineer review before prototyping or production.                                                             | Open       | Critical        | Safety and product risk depend on meaningful engineering validation.                     | Pilot operating procedure          |
| ASM-008 | WingInspect use               | WingInspect flags defects but qualified human inspectors retain final acceptance/rejection authority.                                                               | Open       | Critical        | Quality/safety exposure changes if the model becomes autonomous.                         | Manufacturing procedure            |
| ASM-009 | PondGPT access                | PondGPT uses enterprise access controls and should not grant users access to documents they could not otherwise access.                                             | Open       | Critical        | Controls cross-user leakage and privilege amplification.                                 | Architecture evidence              |
| ASM-010 | QuackBot escalation           | QuackBot can escalate uncertain, sensitive, or safety-relevant interactions to human support staff.                                                                 | Open       | High            | Reduces customer harm and supports oversight.                                            | Release design                     |
| ASM-011 | FeatherForecast decisions     | FeatherForecast is decision support; purchasing and production commitments require authorized manager approval.                                                     | Open       | Medium          | Limits direct automation risk.                                                           | Supply chain SOP                   |
| ASM-012 | Third-party mix               | Duckworks uses a combination of internally developed AI components and third-party models/services.                                                                 | Validated  | High            | Requires both development governance and supplier risk controls.                         | Architecture scenario              |
| ASM-013 | Data                          | AI systems may process confidential IP and, for selected systems, customer, employee, or applicant personal data.                                                   | Validated  | High            | Drives privacy, security, and data governance controls.                                  | Inventory                          |
| ASM-014 | No real data                  | Portfolio artifacts use only fictional, synthetic, anonymized, or public data.                                                                                      | Validated  | Low             | Protects confidentiality and establishes portfolio evidence boundary.                    | Project rule                       |
| ASM-015 | Legal review                  | Regulatory mappings are governance screening outputs, not formal legal opinions.                                                                                    | Validated  | High            | Prevents overstating compliance conclusions.                                             | Project scope                      |
| ASM-016 | Standards                     | NIST/ISO/OWASP/ENISA mappings are guidance/control references and do not independently prove legal compliance or certification.                                     | Validated  | High            | Keeps framework claims defensible.                                                       | Reference file                     |
| ASM-017 | Risk method                   | Internal Duckworks risk levels are separate from statutory concepts such as an EU AI Act “high-risk AI system.”                                                     | Validated  | Critical        | Avoids conflating enterprise scoring with legal classification.                          | Risk methodology                   |
| ASM-018 | Control credit                | Residual risk may only be reduced where implemented controls and evidence justify revised severity/likelihood.                                                      | Validated  | Critical        | Prevents unsupported mathematical risk discounting.                                      | Risk methodology                   |
| ASM-019 | Shadow AI                     | Unregistered GenAI Usage is an organizational condition containing multiple use cases, not one homogeneous AI system.                                               | Validated  | High            | Requires discovery and decomposition into individual inventory records.                  | AI-007 AIA                         |
| ASM-020 | Product scope                 | Some Duckworks products may include digital or connected functionality; exact machinery/product/cybersecurity regulatory applicability remains product-specific.    | Open       | High            | Requires legal/product assessment before real conformity claims.                         | Product architecture               |
| ASM-021 | Evidence maturity             | Some current-state controls exist but evidence quality is inconsistent; target state requires traceable control evidence.                                           | Validated  | High            | Supports assurance-readiness objective.                                                  | Executive case study               |
| ASM-022 | Internal Audit independence   | Internal Audit observes and assures but does not design, own, or operate first/second-line AI controls.                                                             | Validated  | High            | Preserves three-lines independence.                                                      | Stakeholder model                  |
| ASM-023 | Risk appetite                 | Critical residual AI risk is not acceptable for production without exceptional executive/board-level escalation; specific appetite thresholds may be refined later. | Open       | Critical        | Drives deployment decisions.                                                             | Risk methodology                   |
| ASM-024 | Project technology neutrality | The governance design is model-, vendor-, cloud-, and GRC-platform-neutral unless a system-specific decision requires otherwise.                                    | Validated  | Low             | Keeps portfolio reusable.                                                                | Scope document                     |

## 4. Critical Assumptions Requiring Early Validation

1.  Confirm actual human decision authority for DuckTalent, DuckDesign, WingInspect, QuackBot, and FeatherForecast.

2.  Confirm PondGPT data-access architecture and retrieval authorization boundaries.

3.  Confirm whether any product-integrated AI can perform a safety function or directly control mechanical movement.

4.  Confirm vendor/model data-use, retention, training, and subprocessor arrangements.

5.  Confirm geographic deployment and affected-person jurisdictions before final legal classification.

## 5. Assumption Change Control

Any critical assumption that becomes false, materially changes, or cannot be validated should trigger an update to the relevant inventory record and, where appropriate, a new impact assessment, risk assessment, legal triage, or governance approval. The AI Governance Lead records the change; the system owner supplies evidence; the relevant second-line specialist determines whether reassessment is required.

## Portfolio Disclaimer

Duckworks, Project W.I.N.G., all personnel, committees, systems, datasets, decisions, and evidence referenced in this document are fictional and were created solely for educational and professional portfolio purposes.
