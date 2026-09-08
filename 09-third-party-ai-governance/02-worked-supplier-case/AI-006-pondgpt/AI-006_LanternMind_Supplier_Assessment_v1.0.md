# PondGPT Supplier Intake and Due-Diligence Assessment

| Field | Record |
|---|---|
| Document ID | DW-TPR-AI006-001 |
| Version / date | 1.0 / 8 September 2026 |
| Assessment ID | `TPR-AI006-2026-001` |
| Supplier | LanternMind Enterprise AI Ltd. (fictional) |
| Service | Hosted enterprise LLM service integrated with PondGPT |
| AI system | `AI-006 — PondGPT` |
| Risk | `AI-006-R01 — Privacy & data governance` |
| Control | `AI-TPR-01 — AI Supplier Due Diligence & Contract Controls` |
| Assessment owner | Percival Duckworth — Director Procurement & Vendor Assurance |
| Technical contributor | Oliver Duckett — Head of IT & Cloud |
| Independent challenge | Cassandra Duckley — Chief Information Security Officer; Daria Duckworth — DPO & Head of Privacy |
| Evidence class | Synthetic portfolio evidence |

## 1. Intake record

PondGPT is a Duckworks-controlled enterprise application using a third-party hosted LLM. Duckworks controls identity, retrieval connectors, source authorization and application configuration. The supplier is assumed to provide tenant isolation and to refrain from training on Duckworks content under `ASM-030`; those assumptions are not validated production facts.

### Proposed processing and service boundary

| Dimension | Proposed boundary |
|---|---|
| Users | Approved Duckworks employees in a restricted pilot |
| Inputs | Drafting prompts and content retrieved from specifically approved repositories |
| Excluded data | Privileged legal material, special-category HR data, secrets, credentials, unrestricted source-code repositories and any source not approved for the pilot |
| Supplier role | Hosted model/API service provider; exact legal role requires formal privacy/legal determination |
| Model training | Supplier training or model improvement using Duckworks data prohibited unless separately assessed and approved |
| Retention | Contractual zero/shortest technically necessary retention target; actual configuration and verification pending |
| Hosting | EU/EEA target; actual regions, support access and subprocessors require evidence |
| Integrations | Duckworks identity and approved knowledge connectors only; tool execution disabled in the assessed boundary |

## 2. Due-diligence results

| Domain | Result | Evidence basis | Finding / condition |
|---|---|---|---|
| Corporate identity and ownership | Conditional | Synthetic supplier profile only | Legal entity, ownership and financial viability not verified. |
| Service and model description | Conditional | Proposed service description | Exact model/version, routing and fallback providers not evidenced. |
| Information security governance | Gap | No assurance report supplied | Independent security assurance and current remediation status required. |
| Tenant isolation | Gap | Provider assertion assumed by `ASM-030` | Architecture and test evidence required before broader rollout. |
| Identity and access | Conditional | Duckworks design plus `PG-01/PG-02` synthetic evidence | Real connector, identity synchronization and support-access controls unverified. |
| Encryption and key management | Gap | No supplier evidence supplied | In-transit/at-rest encryption and key ownership evidence required. |
| Data use and model training | Conditional | Proposed contract restriction | Binding executed commitment and technical configuration evidence required. |
| Retention and deletion | Gap | Proposed contractual requirement | Configured retention and deletion/termination attestation unavailable. |
| Hosting and international transfers | Gap | EU/EEA target only | Actual regions, transfer mechanism and remote support locations require review. |
| Subprocessors | Conditional | Partial synthetic register | Complete current list, purpose, location and change-notice mechanism required. |
| Secure development and vulnerability management | Conditional | Questionnaire response only | Current testing summary and critical-vulnerability treatment evidence required. |
| Incident management | Conditional | Proposed 24-hour notification term | Executed obligation, escalation contacts and cooperation procedure required. |
| Model/service change management | Conditional | Proposed 30-day notice term | Emergency-change path and materiality criteria require agreement. |
| Logging and evidence access | Gap | No supplier evidence export demonstrated | Duckworks needs audit logs, investigation support and evidence-retention terms. |
| Availability and continuity | Conditional | Proposed service objective | Tested resilience evidence and recovery dependencies unavailable. |
| Intellectual property | Conditional | Template terms only | Input/output rights, claims support and infringement allocation require execution. |
| Regulatory cooperation | Conditional | Template terms only | Assistance, records and authority-response obligations require execution. |
| Exit and portability | Gap | Exit plan designed by Duckworks | Export test, deletion proof and transition assistance not demonstrated. |

## 3. Assessment conclusion

The evidence is insufficient for an unrestricted procurement or production decision. The service may remain in the existing restricted pilot only if approved repositories, excluded data, user population and disabled tool-execution boundaries remain enforced.

The following are blocking conditions for broader rollout:

1. Executed no-training/data-use, incident-notification, material-change, audit/evidence and deletion terms.
2. Verified tenant-isolation, encryption, hosting/transfer, support-access and subprocessor evidence.
3. Real configuration evidence for retention, connector authorization, identity synchronization, logging and DLP.
4. Tested continuity, export and deletion procedures.
5. Completion of security and privacy challenge with no unresolved critical finding.

## 4. Review triggers

Reassess before renewal or expansion and upon a material model, subprocessor, hosting, data-use, retention, security, incident, ownership, financial-viability, integration or service-scope change.

> This is a synthetic portfolio assessment. Questionnaire answers, findings, decisions and supplier records are fictional and are not legal advice or evidence about any real company.

