# Technical Threat Models

**Repository path:** `10-system-model-and-technical-documentation/03-threat-models/`  
**Status:** Active Phase II system-specific threat-model set

[← Back to main portfolio](../../README.md) · [↑ Parent folder](../README.md)

This folder contains system-specific technical threat models that convert architecture and trust boundaries into attack/failure hypotheses, security requirements, testing priorities and evidence expectations.

## Current threat models

- [`AI-006-pondgpt/Duckworks_PondGPT_Threat_Model_v1.0.md`](AI-006-pondgpt/Duckworks_PondGPT_Threat_Model_v1.0.md) — internal RAG / GenAI.
- [`AI-004-winginspect/Duckworks_WingInspect_Threat_Model_v1.0.md`](AI-004-winginspect/Duckworks_WingInspect_Threat_Model_v1.0.md) — adversarial ML / computer vision.
- [`AI-002-quackbot/Duckworks_QuackBot_Threat_Model_v1.0.md`](AI-002-quackbot/Duckworks_QuackBot_Threat_Model_v1.0.md) — public-facing RAG/API.
- [`AI-001-duckdesign/Duckworks_DuckDesign_Threat_Model_v1.0.md`](AI-001-duckdesign/Duckworks_DuckDesign_Threat_Model_v1.0.md) — generated code, engineering data, software supply chain, build/provenance and tool privilege.

## Current validation state

- PondGPT — commit-bound synthetic validation completed and reconciled.
- WingInspect — commit-bound synthetic validation completed and reconciled.
- QuackBot — commit-bound synthetic validation completed and reconciled.
- DuckDesign — architecture/threat-model foundation complete; `DDSEC-T001`–`DDSEC-T012` are design-only pending validation plan/lab.

## Evidence boundary

Threat models identify plausible attack/failure paths and test priorities.

They are not evidence that an attack occurred, a production vulnerability exists, a product is unsafe or a control is effective.
