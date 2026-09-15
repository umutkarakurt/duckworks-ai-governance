# AI-001 DuckDesign AI — Phase II Technical Architecture

**System:** AI-001 — DuckDesign AI  
**Business function:** Product & Engineering  
**Current governance gate:** **Restricted Pilot only**  
**Status:** Synthetic security-architecture baseline established; technical validation not yet executed

## Current artifact

- [`Duckworks_DuckDesign_Technical_Security_Architecture_v1.0.md`](Duckworks_DuckDesign_Technical_Security_Architecture_v1.0.md)

The architecture turns DuckDesign's engineering-IP, generated-code, dependency, build, tool-privilege and validation risks into explicit trust boundaries and testable security requirements.

Core invariants include:

> **DuckDesign cannot authorize prototype or production release.**

> **Generated code, dependency names, tool commands and engineering claims are untrusted until independently validated.**

> **Engineer approval is valid only for the exact artifact hash/version that was reviewed.**

Related artifacts:

- [`../../03-threat-models/AI-001-duckdesign/Duckworks_DuckDesign_Threat_Model_v1.0.md`](../../03-threat-models/AI-001-duckdesign/Duckworks_DuckDesign_Threat_Model_v1.0.md)
- [`../../../02-regulatory-and-framework-research/Duckworks_DuckDesign_Technical_Security_Reference_Applicability_Addendum_v1.0.md`](../../../02-regulatory-and-framework-research/Duckworks_DuckDesign_Technical_Security_Reference_Applicability_Addendum_v1.0.md)

## Evidence boundary

This is a target design, not evidence that a production DuckDesign deployment uses this architecture.

It does not establish:

- actual AetherForge data handling;
- production engineering-data DLP;
- production generated-code security;
- production dependency/build integrity;
- production tool privilege;
- real engineer approval operation;
- product safety;
- machinery/product conformity;
- legal compliance; or
- control effectiveness.

`IAF-2026-002` remains open and the Restricted Pilot gate remains unchanged.
