# Architecture and Data Flows

**Repository path:** `10-system-model-and-technical-documentation/02-architecture-and-data-flows/`  
**Status:** Portfolio diagrams / architecture design / illustrative technical evidence

[← Back to main portfolio](../../README.md) · [↑ Parent folder](../README.md)

This folder contains architecture and data-flow material used to make AI processing boundaries, trust relationships, data movement, integration points, authorization enforcement, model/provider boundaries, physical acquisition boundaries, human decision points, and security telemetry easier to review.

## Current artifacts

- `Duckworks_AI_Data_Flow_Diagrams_v1.0.pdf`
- `Duckworks DFD.png`
- [`AI-006-pondgpt/Duckworks_PondGPT_Technical_Security_Architecture_v1.0.md`](AI-006-pondgpt/Duckworks_PondGPT_Technical_Security_Architecture_v1.0.md) — Phase II synthetic PondGPT security architecture and engineering baseline.
- [`AI-004-winginspect/Duckworks_WingInspect_Technical_Security_Architecture_v1.0.md`](AI-004-winginspect/Duckworks_WingInspect_Technical_Security_Architecture_v1.0.md) — Phase II synthetic WingInspect computer-vision security architecture.

## AI-006 PondGPT Phase II architecture

The PondGPT architecture identifies identity, authorization, RAG, provider, tool, egress, secrets, telemetry, build/release, and evidence boundaries. It is the dependency for the PondGPT threat model and executable PG-03 security lab.

Two core invariants remain:

> Authorization must be enforced before retrieved content enters the LLM context.

> Retrieved content and model output are untrusted data and do not acquire security authority through the model.

## AI-004 WingInspect Phase II architecture

The WingInspect architecture adds a different class of security problem: a predictive computer-vision system whose outputs can influence manufacturing quality decisions.

It identifies:

- product / fixture and camera acquisition boundaries;
- image-to-item provenance;
- image-quality fail-safe routing;
- versioned preprocessing;
- model, class-map, and threshold integrity;
- dataset / label provenance;
- vendor/component staging;
- human inspection;
- the Mandatory Human Release Gate;
- QMS/security telemetry; and
- change-triggered revalidation.

Its critical invariant is:

> **The model may flag or classify defects, but it cannot independently authorize product release.**

The architecture is the dependency for the **[WingInspect Technical Threat Model](../03-threat-models/AI-004-winginspect/Duckworks_WingInspect_Threat_Model_v1.0.md)**.

## Governance use

Architecture and data-flow artifacts support:

- privacy and DPIA analysis;
- data classification and provenance;
- security threat modelling;
- third-party boundary identification;
- access and integrity review;
- model/data supply-chain analysis;
- human-oversight design;
- logging and monitoring;
- incident and change analysis.

## Evidence caution

A diagram or target architecture is an explanatory/design artifact, not proof that the depicted production architecture exists or that the controls shown are operating.

Material production claims require separate supporting evidence. For WingInspect this includes real camera configuration, actual model/runtime, inspection procedures, human authority, model-performance outcomes, defect-escape evidence, product-safety role, and adversarial robustness.

---

> **Portfolio boundary:** Duckworks, Project W.I.N.G., its personnel, systems, datasets, decisions, controls, and evidence are fictional or synthetic unless a file explicitly identifies a public source.
