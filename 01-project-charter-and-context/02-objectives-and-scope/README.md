# Objectives and Scope

**Repository path:** `01-project-charter-and-context/02-objectives-and-scope/`  
**Status:** Portfolio baseline + Phase II technical-security scope extension  

[← Back to main portfolio](../../README.md) · [↑ Parent folder](../README.md)

This folder defines **what Project W.I.N.G. is intended to achieve and where the project deliberately stops**.

## Current artifacts

- `Duckworks AI Governance Project — Project Objectives.md` — primary objective, fifteen specific objectives, target outcomes, and the overall success principle.
- `Duckworks AI Governance Project — In-Scope and Out-of-Scope Items.md` — organizational, geographic, data, technology, implementation, legal, certification, and assurance boundaries.
- [`Duckworks_Technical_AI_and_Cybersecurity_Engineering_Scope_Addendum_v1.0.md`](Duckworks_Technical_AI_and_Cybersecurity_Engineering_Scope_Addendum_v1.0.md) — Phase II authorization and scope extension for bounded synthetic AI-security engineering, adversarial validation, application/API testing, RAG testing, supply-chain analysis, detection engineering, remediation, and retesting.
- A DOCX objectives version may be retained as a formatted source/export.


## Phase II scope extension

The original Project W.I.N.G. governance-readiness scope remains authoritative for the initial portfolio phase. It deliberately excluded comprehensive penetration testing, AI red-team execution, adversarial model testing, vulnerability scanning, source-code review, API security testing, and infrastructure penetration testing as initial deliverables.

Phase II does **not** rewrite that historical boundary. The **[Technical AI & Cybersecurity Engineering Scope Addendum](Duckworks_Technical_AI_and_Cybersecurity_Engineering_Scope_Addendum_v1.0.md)** creates a separate, bounded workstream for selected technical security activities against fictional Duckworks systems, synthetic data, locally controlled test components, or explicitly authorized test environments.

The first Phase II target is **AI-006 PondGPT**.

In-scope Phase II activities include:

- technical security architecture and trust-boundary analysis;
- threat modelling;
- identity, authentication, and authorization testing;
- application and API security testing;
- direct and indirect prompt-injection testing;
- RAG poisoning and retrieval-integrity testing;
- controlled tool/agent security testing where tools are explicitly enabled;
- software and AI supply-chain analysis;
- secrets, egress, logging, and telemetry validation;
- controlled adversarial testing;
- remediation and retesting; and
- reproducible technical evidence generation.

The Phase II scope remains explicitly non-production and does not authorize testing of real third-party systems, real credentials, real personal data, destructive techniques, uncontrolled scanning, external denial-of-service, or any activity outside the defined synthetic/authorized boundary.

## Core objective

The project is designed to establish a practical, risk-based, auditable governance capability in which material AI use is **known, owned, assessed, controlled, monitored, and evidenced in proportion to impact**.

## Important boundaries

This project does not claim to perform real production deployment, penetration testing of real production or third-party systems, uncontrolled AI red-team activity, real fairness validation, legal advice, certification, formal conformity assessment, live monitoring operations, or real board/regulator approval.

**Phase II exception:** bounded penetration-style, API, RAG, adversarial, supply-chain, and detection testing is now in scope only for fictional Duckworks systems, synthetic data, locally controlled components, or explicitly authorized test environments under the Phase II scope addendum.

That distinction matters when reviewing later folders: an artifact may define or execute a synthetic control/test workflow without proving that the same architecture, control, or operating effectiveness exists in production.

## Reviewer use

Use this folder to distinguish:

- initial governance-phase deliverables from Phase II technical-security work;
- design-readiness and synthetic technical validation from production operating effectiveness;
- framework mapping from legal compliance;
- internal governance decisions from statutory classifications.

---

> **Portfolio boundary:** Duckworks, Project W.I.N.G., its personnel, systems, datasets, decisions, controls, and evidence are fictional or synthetic unless a file explicitly identifies a public source. Folder descriptions explain the intended governance role of the artifacts; they do not convert draft, planned, or template material into implemented controls, legal compliance, certification, or independent assurance.
