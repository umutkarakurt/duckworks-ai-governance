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
| ASM-008 | WingInspect use               | WingInspect flags defects but qualified human inspectors retain final acceptance/rejection authority.                                                               | Open       | Critical        | Quality/safety exposure changes if the model becomes autonomous.                         | WI-01 synthetic operating-evidence package demonstrates workflow/override logic; manufacturing procedure and production authority remain to be validated |
| ASM-009 | PondGPT access                | PondGPT uses enterprise access controls and should not grant users access to documents they could not otherwise access.                                             | Open       | Critical        | Controls cross-user leakage and privilege amplification.                                 | PG-02 synthetic executable evidence demonstrates test logic/detection/gating; production architecture and authorization inheritance remain to be validated |
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
| ASM-025 | DuckDesign vendor architecture | DuckDesign AI uses a Duckworks-developed engineering workflow integrated with the fictional AetherForge AI GmbH hosted model service; Duckworks engineering data is contractually excluded from provider model training. | Open | High | Determines third-party, IP, confidentiality, training-data-use, and supplier-control requirements. | Vendor contract; architecture diagram; data-use terms |
| ASM-026 | QuackBot vendor architecture | QuackBot uses the fictional HelixRiver AI Services S.A. hosted LLM, while Duckworks controls the RAG knowledge base, customer-support workflow, and escalation logic; provider reuse of Duckworks prompts/content for training is prohibited. | Open | High | Determines customer-data exposure, supplier controls, RAG accountability, and data-use restrictions. | Vendor contract; solution architecture; retention/training terms |
| ASM-027 | FeatherForecast platform | FeatherForecast uses the fictional Northstar Planning Analytics GmbH ML platform, with Duckworks controlling datasets, forecasting configuration, thresholds, and operational decisions. | Open | Medium | Clarifies provider dependency while retaining Duckworks accountability for data and operational decisions. | Platform architecture; configuration record; supplier agreement |
| ASM-028 | WingInspect imaging scope | WingInspect Vision uses fictional VisiCore Industrial AI components; production cameras are intended to capture products/components rather than perform employee surveillance or biometric identification. | Open | High | Materially affects privacy, workforce-impact, security, and regulatory screening. | Camera field-of-view review; system design; privacy assessment |
| ASM-029 | DuckTalent vendor and decision boundary | DuckTalent AI is provided by fictional MeritPath HR Technologies S.A.; special-category attributes are not intended ranking features, and the system cannot autonomously reject or hire an applicant. | Open | Critical | Affects fairness testing, privacy, legal classification, human oversight, and deployment decision. | Vendor documentation; feature inventory; workflow configuration; HR procedure |
| ASM-030 | PondGPT enterprise controls | PondGPT uses fictional LanternMind Enterprise AI Ltd. under an enterprise arrangement providing tenant isolation and no provider training on Duckworks content; retrieval permissions inherit authorization from source systems. | Open | Critical | Controls cross-user leakage, privilege amplification, third-party data use, and deployment scope. | PG-02 synthetic executable evidence demonstrates permission-regression logic; contract, production architecture, source authorization, DLP and retrieval-security evidence remain required |

### 3.1 WingInspect evidence boundary for ASM-008

The Project W.I.N.G. operating-evidence package for `WI-01 — Qualified Human Final Inspection` provides a worked synthetic demonstration of the intended final-inspection workflow, including qualified-human decision sequencing, documented disagreement with AI output, override rationale, release authorization, and a synthetic control test.

This evidence improves the **design and workflow evidence** for ASM-008 but does not validate the assumption as a production fact. The portfolio does not contain real manufacturing procedure evidence, sustained inspector-behavior evidence, or independently verified production authority records.

Accordingly:

- `ASM-008` remains **Open / Critical**;
- `WI-01` should not be described as production-validated or operating effectively;
- the synthetic evidence does not justify additional residual-risk reduction credit; and
- closure requires evidence that qualified inspectors actually retain and exercise final acceptance/rejection authority in the operating environment.

Related evidence: [`../../../80-operating-evidence/AI-004-winginspect/`](../../../80-operating-evidence/AI-004-winginspect/)

### 3.2 PondGPT evidence boundary for ASM-009 / ASM-030

The Project W.I.N.G. operating-evidence package for `PG-02 — Automated Permission Regression & DLP Tests` provides a worked executable synthetic demonstration of the intended PondGPT authorization-assurance process.

The package exercises the `PG-01 — Permission-Aware Retrieval` boundary through positive/negative personas, source entitlements, pilot exclusions, DLP assertions, permission changes, a deliberately seeded connector ACL defect, alert/exception generation, expansion blocking, remediation, and successful retesting.

This evidence improves the **design, technical implementation, and synthetic test evidence** for PondGPT authorization controls but does not validate either assumption as a production fact. The portfolio does not contain real PondGPT connector configuration, identity-provider synchronization, production ACL mappings, actual DLP/SSE/CASB enforcement, real SIEM evidence, actual provider contract evidence, or sustained scheduled PG-02 execution.

Accordingly:

- `ASM-009` remains **Open / Critical**;
- `ASM-030` remains **Open / Critical**;
- `PG-02` may be described as **Partially implemented in the synthetic portfolio demonstration**, not production-validated;
- the synthetic evidence does not justify additional residual-risk reduction credit; and
- closure requires real architecture, contractual, authorization, DLP, connector, logging, and operating evidence.

Related evidence: [`../../../80-operating-evidence/AI-006-pondgpt/`](../../../80-operating-evidence/AI-006-pondgpt/)

## 4. Critical Assumptions Requiring Early Validation

1.  Confirm actual human decision authority for DuckTalent, DuckDesign, WingInspect, QuackBot, and FeatherForecast. For WingInspect, the synthetic `WI-01` package demonstrates the intended workflow, but production authority remains unvalidated.

2.  Confirm PondGPT data-access architecture, source-system authorization inheritance, connector ACLs, DLP enforcement, and enterprise-provider controls. The synthetic `PG-02` package demonstrates the intended test/control logic, but `ASM-009` and `ASM-030` remain unvalidated production assumptions.

3.  Confirm whether any product-integrated AI can perform a safety function or directly control mechanical movement.

4.  Confirm vendor/model data-use, retention, training, and subprocessor arrangements.

5.  Confirm geographic deployment and affected-person jurisdictions before final legal classification.

## 5. Assumption Change Control

Any critical assumption that becomes false, materially changes, or cannot be validated should trigger an update to the relevant inventory record and, where appropriate, a new impact assessment, risk assessment, legal triage, or governance approval. The AI Governance Lead records the change; the system owner supplies evidence; the relevant second-line specialist determines whether reassessment is required.

## Portfolio Disclaimer

Duckworks, Project W.I.N.G., all personnel, committees, systems, datasets, decisions, and evidence referenced in this document are fictional and were created solely for educational and professional portfolio purposes.
