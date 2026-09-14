# Regulatory and Framework Research

**Repository path:** `02-regulatory-and-framework-research/`  
**Status:** Research baseline — verify currency before reuse

[← Back to main portfolio](../README.md)

This folder contains the legal, regulatory, standards, framework and technical-security reference research used to inform Project W.I.N.G. governance and Phase II security-engineering decisions.

## Current artifacts

- `Duckworks_AI_Governance_Regulatory_and_Framework_Research_Report_v1.0.md`
- `Duckworks_AI_Governance_Regulatory_and_Framework_Research_Report_v1.0.pdf`
- `Duckworks_AI_Governance_Obligations_and_Guidance_Register_v1.0.xlsx`
- [`Duckworks_Technical_AI_Security_Reference_and_Applicability_Baseline_v1.0.md`](Duckworks_Technical_AI_Security_Reference_and_Applicability_Baseline_v1.0.md) — Phase II technical-security baseline initially worked through PondGPT.
- [`Duckworks_QuackBot_Technical_Security_Reference_Applicability_Addendum_v1.0.md`](Duckworks_QuackBot_Technical_Security_Reference_Applicability_Addendum_v1.0.md) — system-specific QuackBot applicability addendum for public-facing RAG/API security, GDPR, AI Act Article 50 transparency, and technical guidance.
- The repository root [`REFERENCES.md`](../REFERENCES.md) is the controlled public-source catalogue.

## Phase II technical-security research

Phase II separates:

1. **Mandatory legal requirements** — only where scope/trigger conditions are met.
2. **Standards/formal frameworks** — voluntary or adopted requirements that do not independently prove legal compliance.
3. **Official cybersecurity guidance** — government/agency security guidance.
4. **Recognized technical threat/security references** — e.g. MITRE ATLAS and OWASP.
5. **Duckworks engineering requirements and assumptions** — internal design/test choices.

### PondGPT

The original technical-security baseline covers internal enterprise RAG, authorization, provider/tool and telemetry boundaries.

### QuackBot

The **QuackBot addendum** applies the hierarchy to an internet-facing customer chatbot.

It identifies:

- GDPR as potentially mandatory where customer personal data are processed;
- EU AI Act Article 50 direct-interaction transparency as a specific mandatory-law applicability review item;
- no current basis to classify QuackBot as a high-risk AI system;
- NIS2 applicability as organization/national-law dependent;
- CRA applicability as not established; and
- OWASP GenAI/API, NIST, ENISA, NCSC and MITRE sources as guidance/reference rather than law.

The addendum deliberately does not invent a universal customer-warranty legal rule; actual consumer/warranty/product-support obligations require market/product-specific legal review.

## Evidence hierarchy

1. Binding legal text.
2. Official regulator/government guidance.
3. Standards/formal frameworks.
4. Recognized technical threat/control guidance.
5. Duckworks organizational practices and assumptions.

## Important interpretation rule

Do not treat ISO, NIST, ENISA, MITRE, OWASP or similar mappings as proof of legal compliance, certification, conformity, control effectiveness or production security.

Likewise, a Duckworks High/Critical internal rating does not establish an EU AI Act legal classification.

Living sources should be re-checked when assigning current technique/category identifiers to executable tests.

---

> **Portfolio boundary:** Duckworks, Project W.I.N.G., its personnel, systems, datasets, decisions, controls and evidence are fictional or synthetic unless explicitly identified otherwise.
