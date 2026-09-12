# Technical Threat Models

**Repository path:** `10-system-model-and-technical-documentation/03-threat-models/`  
**Status:** Active Phase II system-specific threat-model set

[← Back to main portfolio](../../README.md) · [↑ Parent folder](../README.md)

This folder contains system-specific technical threat models that convert architecture and trust boundaries into attack/failure hypotheses, security requirements, testing priorities, and evidence expectations.

## Current threat models

- [`AI-006-pondgpt/Duckworks_PondGPT_Threat_Model_v1.0.md`](AI-006-pondgpt/Duckworks_PondGPT_Threat_Model_v1.0.md) — RAG / GenAI application threat model and PG-03 test baseline.
- [`AI-004-winginspect/Duckworks_WingInspect_Threat_Model_v1.0.md`](AI-004-winginspect/Duckworks_WingInspect_Threat_Model_v1.0.md) — computer-vision / adversarial-ML threat model covering physical/digital evasion, image-quality degradation, model/configuration integrity, poisoning, supply chain, fail-safe behavior, and release-gate bypass.

## Method

Threat models may use:

- STRIDE-style conventional cybersecurity analysis;
- NIST adversarial-ML terminology;
- MITRE ATLAS attack themes;
- system-specific abuse/failure cases;
- asset and trust-boundary analysis; and
- risk/control traceability.

Threat-model priorities indicate **technical testing urgency**, not Duckworks enterprise risk scores.

## Evidence boundary

A threat model describes plausible attack/failure paths and planned validation. It is not evidence that a threat occurred, a vulnerability exists in production, or a control is effective.
