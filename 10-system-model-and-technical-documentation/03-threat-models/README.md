# Technical Threat Models

**Repository path:** `10-system-model-and-technical-documentation/03-threat-models/`  
**Status:** Active Phase II system-specific threat-model set

[← Back to main portfolio](../../README.md) · [↑ Parent folder](../README.md)

This folder contains system-specific technical threat models that convert architecture and trust boundaries into attack/failure hypotheses, security requirements, testing priorities and evidence expectations.

## Current threat models

- [`AI-006-pondgpt/Duckworks_PondGPT_Threat_Model_v1.0.md`](AI-006-pondgpt/Duckworks_PondGPT_Threat_Model_v1.0.md) — internal RAG / GenAI application threat model and PG-03 baseline.
- [`AI-004-winginspect/Duckworks_WingInspect_Threat_Model_v1.0.md`](AI-004-winginspect/Duckworks_WingInspect_Threat_Model_v1.0.md) — adversarial-ML / computer-vision threat model.
- [`AI-002-quackbot/Duckworks_QuackBot_Threat_Model_v1.0.md`](AI-002-quackbot/Duckworks_QuackBot_Threat_Model_v1.0.md) — public-facing customer chatbot/RAG/API threat model covering internet abuse, session/auth, BOLA, prompt/RAG injection, customer-data leakage, misinformation, output handling, excessive agency/SSRF, resource exhaustion and change integrity.

## Method

Threat models may use:

- STRIDE-style conventional cybersecurity analysis;
- NIST adversarial-ML / GenAI risk terminology;
- MITRE ATLAS attack themes;
- OWASP GenAI Security;
- OWASP API Security;
- system-specific abuse/failure cases;
- asset/trust-boundary analysis; and
- risk/control traceability.

Threat-model priorities indicate **technical testing urgency**, not Duckworks enterprise risk scores.

## Current validation state

- PondGPT — commit-bound synthetic technical validation completed and reconciled.
- WingInspect — commit-bound synthetic technical validation completed and reconciled.
- QuackBot — architecture/threat-model baseline complete; `QBSEC-T001`–`QBSEC-T012` are design-only pending validation plan/lab.

## Evidence boundary

A threat model describes plausible attack/failure paths and planned validation.

It is not evidence that a threat occurred, a production vulnerability exists or a control is effective.
