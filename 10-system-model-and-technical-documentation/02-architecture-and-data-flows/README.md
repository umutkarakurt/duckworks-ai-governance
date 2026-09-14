# Architecture and Data Flows

**Repository path:** `10-system-model-and-technical-documentation/02-architecture-and-data-flows/`  
**Status:** Portfolio diagrams / architecture design / illustrative technical evidence

[← Back to main portfolio](../../README.md) · [↑ Parent folder](../README.md)

This folder contains architecture and data-flow material used to make AI processing boundaries, trust relationships, data movement, integration points, authorization enforcement, model/provider boundaries, public/internet boundaries, physical acquisition boundaries, human decision points and security telemetry easier to review.

## Current artifacts

- `Duckworks_AI_Data_Flow_Diagrams_v1.0.pdf`
- `Duckworks DFD.png`
- [`AI-006-pondgpt/Duckworks_PondGPT_Technical_Security_Architecture_v1.0.md`](AI-006-pondgpt/Duckworks_PondGPT_Technical_Security_Architecture_v1.0.md) — Phase II synthetic PondGPT architecture.
- [`AI-004-winginspect/Duckworks_WingInspect_Technical_Security_Architecture_v1.0.md`](AI-004-winginspect/Duckworks_WingInspect_Technical_Security_Architecture_v1.0.md) — Phase II synthetic WingInspect computer-vision architecture.
- [`AI-002-quackbot/Duckworks_QuackBot_Technical_Security_Architecture_v1.0.md`](AI-002-quackbot/Duckworks_QuackBot_Technical_Security_Architecture_v1.0.md) — Phase II synthetic public-facing QuackBot RAG/API architecture.

## AI-006 PondGPT

PondGPT identifies identity, authorization, RAG, provider, tool, egress, secrets, telemetry, build/release and evidence boundaries.

Core invariant:

> Authorization is enforced before retrieved content enters LLM context.

## AI-004 WingInspect Vision

WingInspect identifies image acquisition/provenance, image-quality fail-safe routing, preprocessing/model/configuration integrity, human inspection and Mandatory Human Release Gate boundaries.

Core invariant:

> The model may flag/classify defects but cannot independently authorize product release.

WingInspect has progressed through commit-bound synthetic validation and evidence reconciliation.

## AI-002 QuackBot

QuackBot adds an internet-facing customer-service threat surface.

The architecture identifies:

- public edge/API;
- session isolation;
- anonymous versus authenticated-customer mode;
- object-level customer authorization;
- public versus customer-specific RAG;
- source allowlisting/provenance;
- context minimization;
- hosted provider boundary;
- grounding/citation/abstention;
- human escalation;
- safe output rendering;
- tool/action denial by default;
- rate/resource controls;
- security telemetry; and
- change-triggered regression.

Two critical invariants are:

> **The model is not an access-control mechanism.**

> **Retrieved content and model output are untrusted data and do not acquire application authority through the LLM.**

The architecture is the dependency for the **[QuackBot Technical Threat Model](../03-threat-models/AI-002-quackbot/Duckworks_QuackBot_Threat_Model_v1.0.md)**.

## Governance use

Architecture/data-flow artifacts support:

- privacy and DPIA analysis;
- data classification and provenance;
- security threat modelling;
- third-party boundary identification;
- authorization and session review;
- application/API security;
- model/data supply-chain analysis;
- human escalation/oversight;
- logging/monitoring;
- incident/change analysis.

## Evidence caution

A diagram or target architecture is an explanatory/design artifact, not proof that the depicted production architecture exists or that the controls are operating.

For QuackBot, production claims would require real API/session/auth configuration, customer-object authorization, corpus provenance, provider configuration/contract evidence, escalation records, rate-limit operation, output-handling evidence, security telemetry and defined-period outcomes.

---

> **Portfolio boundary:** Duckworks, Project W.I.N.G., its personnel, systems, datasets, decisions, controls and evidence are fictional or synthetic unless explicitly identified otherwise.
