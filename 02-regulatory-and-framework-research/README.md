# Regulatory and Framework Research

**Repository path:** `02-regulatory-and-framework-research/`  
**Status:** Research baseline — verify currency before reuse

[← Back to main portfolio](../README.md)

This folder contains the legal, regulatory, standards, framework and technical-security research used to inform Project W.I.N.G. governance and Phase II engineering decisions.

## Core research artifacts

- [`Duckworks_AI_Governance_Regulatory_and_Framework_Research_Report_v1.0.md`](Duckworks_AI_Governance_Regulatory_and_Framework_Research_Report_v1.0.md)
- [`Duckworks_AI_Governance_Regulatory_and_Framework_Research_Report_v1.0.docx`](Duckworks_AI_Governance_Regulatory_and_Framework_Research_Report_v1.0.docx)
- [`Duckworks_AI_Governance_Obligations_and_Guidance_Register_v1.0.xlsx`](Duckworks_AI_Governance_Obligations_and_Guidance_Register_v1.0.xlsx)

## Current Phase II applicability artifacts

- [`Duckworks_Technical_AI_Security_Reference_and_Applicability_Baseline_v1.0.md`](Duckworks_Technical_AI_Security_Reference_and_Applicability_Baseline_v1.0.md)
- [`Duckworks_QuackBot_Technical_Security_Reference_Applicability_Addendum_v1.0.md`](Duckworks_QuackBot_Technical_Security_Reference_Applicability_Addendum_v1.0.md)
- [`Duckworks_DuckDesign_Technical_Security_Reference_Applicability_Addendum_v1.0.md`](Duckworks_DuckDesign_Technical_Security_Reference_Applicability_Addendum_v1.0.md)
- [`Duckworks_FeatherForecast_Technical_Security_Reference_Applicability_Addendum_v1.0.md`](Duckworks_FeatherForecast_Technical_Security_Reference_Applicability_Addendum_v1.0.md)
- The root [`REFERENCES.md`](../REFERENCES.md) remains the controlled public-source catalogue.

## Research hierarchy

1. **Mandatory legal requirements** — only where scope/trigger conditions are met.
2. **Standards/formal frameworks** — voluntary/adopted requirements that do not independently establish legal compliance.
3. **Official cybersecurity guidance**.
4. **Recognized technical threat/security references**.
5. **Duckworks engineering requirements and assumptions**.

## DuckDesign applicability highlights

The DuckDesign addendum records:

- no current basis to classify the internal advisory design assistant as a high-risk AI system;
- mandatory reassessment if its intended role changes into a product/safety-component function;
- Machinery Regulation relevance as a product-context question rather than automatic DuckDesign applicability;
- CRA relevance where generated software enters covered products with digital elements;
- Trade Secrets Directive relevance where engineering information meets the trade-secret definition and Duckworks must demonstrate reasonable protective steps;
- GDPR only where personal data enters the engineering workflow;
- NIS2 as organization/national-law dependent;
- NIST SSDF / 800-218A, NCSC, SLSA, OpenSSF, OWASP and MITRE as guidance/reference rather than law.


## FeatherForecast applicability highlights

The FeatherForecast addendum records:

- no current basis to classify the internal supply-chain forecasting/decision-support system as an EU AI Act high-risk AI system;
- reassessment if intended purpose, affected persons, product integration, decision authority or safety role changes;
- NIS2 as an organization/national-law scope question, with supply-chain security, resilience, access and effectiveness testing relevant if Duckworks is in scope;
- Trade Secrets Directive relevance where supplier/commercial planning information meets the legal definition;
- GDPR only where personal data enter supplier/contact/log data;
- CRA applicability as unestablished for the internal planning service; and
- NIST AI RMF, NIST AI 100-2, NCSC, MITRE ATLAS and secure-ML references as guidance rather than mandatory law.

## Important interpretation rule

Do not treat ISO, NIST, ENISA, NCSC, MITRE, OWASP, SLSA or OpenSSF mappings as proof of legal compliance, certification, product conformity or control effectiveness.

A Duckworks internal High/Critical score is not an EU AI Act legal classification.

Living technical sources should be rechecked when executable test identifiers/mappings are finalized.
