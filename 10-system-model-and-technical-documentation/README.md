# System, Model and Technical Documentation

**Repository path:** `10-system-model-and-technical-documentation/`  
**Status:** Portfolio technical documentation set

[← Back to main portfolio](../README.md)

This folder connects business-level governance decisions to technical evidence about models, system behavior, architecture, data flows, dependencies, security boundaries, and technical threat models.

## Subfolders

| Folder | Purpose |
|---|---|
| `01-model-documentation/` | Model/system documentation and reusable model-card structure. |
| `02-architecture-and-data-flows/` | Data-flow and architecture material supporting threat, privacy, data and control analysis, including Phase II PondGPT, WingInspect and QuackBot security architectures. |
| `03-threat-models/` | System-specific threat models linking assets, trust boundaries, attackers, attack paths, existing risks/controls, security requirements and planned validation. |

## Phase II technical-security baseline

Phase II now has three system-specific architecture/threat-model foundation sets.

### AI-006 PondGPT

- **[PondGPT Technical Security Architecture v1.0](02-architecture-and-data-flows/AI-006-pondgpt/Duckworks_PondGPT_Technical_Security_Architecture_v1.0.md)**
- **[PondGPT Technical Threat Model v1.0](03-threat-models/AI-006-pondgpt/Duckworks_PondGPT_Threat_Model_v1.0.md)**

PondGPT has progressed into executable PG-03 validation, commit-bound synthetic evidence and evidence reconciliation.

### AI-004 WingInspect Vision

- **[WingInspect Technical Security Architecture v1.0](02-architecture-and-data-flows/AI-004-winginspect/Duckworks_WingInspect_Technical_Security_Architecture_v1.0.md)**
- **[WingInspect Technical Threat Model v1.0](03-threat-models/AI-004-winginspect/Duckworks_WingInspect_Threat_Model_v1.0.md)**

WingInspect has progressed through executable adversarial-ML validation, commit-bound replay and the AI-004 evidence-reconciliation overlay.

### AI-002 QuackBot

- **[QuackBot Technical Security Architecture v1.0](02-architecture-and-data-flows/AI-002-quackbot/Duckworks_QuackBot_Technical_Security_Architecture_v1.0.md)** — internet-facing RAG/API architecture covering public/authenticated session separation, customer-data authorization, RAG provenance, provider boundary, grounding/escalation, output handling, rate/resource controls and telemetry.
- **[QuackBot Technical Threat Model v1.0](03-threat-models/AI-002-quackbot/Duckworks_QuackBot_Threat_Model_v1.0.md)** — public/API abuse, prompt/RAG injection, BOLA/session isolation, customer-data leakage, misinformation, output injection, excessive agency/SSRF, resource exhaustion and change-integrity threats.

QuackBot is currently at **architecture + threat-model foundation**. `QBSEC-T001`–`QBSEC-T012` are design-only candidate tests. The next step is a separate validation plan and deterministic synthetic lab.

The technical-security workstream is governed by the **[Phase II Scope Addendum](../01-project-charter-and-context/02-objectives-and-scope/Duckworks_Technical_AI_and_Cybersecurity_Engineering_Scope_Addendum_v1.0.md)**.

## Why this matters

AI governance is not defensible if the organization cannot identify the actual model/service, version, data flows, permissions, integrations, session boundaries, public/private data boundaries, environmental assumptions and technical limitations supporting a material use case.

Technical documentation should feed:

- risk scenarios;
- privacy and rights assessments;
- security review;
- human-oversight design;
- change management;
- vendor governance;
- monitoring;
- evidence and assurance.

## Evidence boundary

Unknown technical facts remain **TBD / not evidenced** rather than being filled with plausible but unsupported details.

Phase II may introduce explicit **synthetic design assumptions** to make a controlled test lab executable; those assumptions remain labelled as assumptions.

An architecture, model card, threat model or test design is not proof of deployed production architecture, actual model configuration, production security, legal classification or control effectiveness.

---

> **Portfolio boundary:** Duckworks, Project W.I.N.G., its personnel, systems, datasets, decisions, controls and evidence are fictional or synthetic unless a file explicitly identifies a public source.
