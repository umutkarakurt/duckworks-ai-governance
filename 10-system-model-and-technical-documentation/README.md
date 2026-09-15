# System, Model and Technical Documentation

**Repository path:** `10-system-model-and-technical-documentation/`  
**Status:** Portfolio technical documentation set

[← Back to main portfolio](../README.md)

This folder connects business-level governance decisions to technical evidence about models, system behavior, architecture, data flows, dependencies, security boundaries and technical threat models.

## Subfolders

| Folder | Purpose |
|---|---|
| `01-model-documentation/` | Model/system documentation and reusable model-card structure. |
| `02-architecture-and-data-flows/` | Data-flow and architecture material for Phase II system security analysis. |
| `03-threat-models/` | System-specific threat models linking assets, trust boundaries, attack paths, risks/controls and planned validation. |

## Phase II technical-security systems

### AI-006 PondGPT

Architecture, threat model, executable PG-03 validation, commit-bound replay and evidence reconciliation completed within the synthetic portfolio boundary.

### AI-004 WingInspect Vision

Architecture, threat model, executable adversarial-ML validation, commit-bound replay and AI-004 evidence reconciliation completed within the synthetic portfolio boundary.

### AI-002 QuackBot

Architecture, threat model, executable public-facing RAG/API validation, commit-bound replay and AI-002 evidence reconciliation completed within the synthetic portfolio boundary.

### AI-001 DuckDesign AI

- **[DuckDesign Technical Security Architecture v1.0](02-architecture-and-data-flows/AI-001-duckdesign/Duckworks_DuckDesign_Technical_Security_Architecture_v1.0.md)**
- **[DuckDesign Technical Threat Model v1.0](03-threat-models/AI-001-duckdesign/Duckworks_DuckDesign_Threat_Model_v1.0.md)**

DuckDesign is currently at **architecture + threat-model foundation**.

The new design focuses on:

- confidential engineering IP;
- generated-code staging and sandboxing;
- dependency/package integrity;
- build/provenance/SBOM evidence;
- CAD/simulation tool privilege;
- engineering validation and safety-gate separation;
- engineer-approval-to-artifact binding;
- material-change regression; and
- rollback to known-good state.

`DDSEC-T001`–`DDSEC-T012` are design-only candidate tests. No `EV-AI001-*` IDs have been allocated.

The technical-security workstream remains governed by the **[Phase II Scope Addendum](../01-project-charter-and-context/02-objectives-and-scope/Duckworks_Technical_AI_and_Cybersecurity_Engineering_Scope_Addendum_v1.0.md)**.

## Evidence boundary

Unknown technical facts remain **TBD / not evidenced** rather than being silently replaced with plausible production detail.

Phase II may introduce explicit synthetic design assumptions to make later validation executable; those assumptions remain labelled as assumptions.

An architecture, model card, threat model or test design is not proof of deployed production architecture, legal classification, product conformity or control effectiveness.
