# AI-003 FeatherForecast — Technical Security Reference & Applicability Addendum

**Project:** Project W.I.N.G. — Phase II Technical AI Security Engineering & Adversarial Validation  
**Document ID:** DW-AI003-SEC-REF-01  
**Version:** 1.0  
**Date:** 15 September 2026  
**System:** AI-003 — FeatherForecast  
**Status:** System-specific applicability baseline — not legal advice  
**Owner:** Eleanor Duckford — AI Governance Lead  
**Security reviewer:** Cassandra Duckley — Chief Information Security Officer  
**Business owner:** Tobias Duckman — Director Supply Chain  
**Current governance gate:** **Continue with monitoring**

> This addendum supplements the Duckworks Phase II technical-security baseline. It separates mandatory legal requirements, standards/framework guidance, recognized technical-security references, recommended organizational practices and project assumptions. It does not establish legal compliance, certification, production effectiveness or supplier assurance.

## 1. Current portfolio facts

FeatherForecast:

- is `AI-003`;
- supports Supply Chain & Manufacturing Planning;
- forecasts product demand, inventory requirements, manufacturing volumes, component shortages and supplier demand;
- is a predictive ML / time-series forecasting system;
- uses a Duckworks-configured forecasting workflow on the fictional `Northstar Planning Analytics GmbH` platform;
- is **Production / Operational** in the synthetic scenario;
- supports supply-chain planners, procurement personnel and manufacturing planners;
- uses demand history, inventory levels, purchase orders, production schedules, supplier lead times, component availability and aggregated order information;
- remains decision support: authorized managers approve purchasing and production commitments;
- has internal impact indicator **Moderate**; and
- is approved to continue with monitoring in the current governance baseline.

Existing risks:

- `AI-003-R01 — Operational / financial`;
- `AI-003-R02 — Reliability & robustness`;
- `AI-003-R03 — Privacy & data governance`.

Existing controls:

- `FF-01 — Human Planning Approval & Override`;
- `FF-02 — Back-Testing, Stress Testing & Challenger Review`;
- `FF-03 — Automated Drift Alerts & Retraining Trigger`;
- `FF-04 — Supplier/Planning Data Access & Logging`.

Relevant assumptions:

- `ASM-005 — Human accountability`;
- `ASM-011 — FeatherForecast decisions`;
- `ASM-012 — Third-party mix`;
- `ASM-013 — Data`;
- `ASM-027 — FeatherForecast platform`.

## 2. Mandatory legal requirements — applicability-dependent

### 2.1 EU Artificial Intelligence Act — Regulation (EU) 2024/1689

**Official consolidated source:** https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng

The current portfolio does **not** classify FeatherForecast as an EU AI Act high-risk AI system.

On the documented facts, FeatherForecast is internal supply-chain forecasting and decision support. It is not described as a safety component of a regulated product, and the current use does not fall within the portfolio's documented Annex III high-risk categories.

**Reassessment trigger:** legal classification must be revisited if intended purpose, affected persons, decision authority, product integration or safety role materially changes.

### 2.2 NIS2 — Directive (EU) 2022/2555

**Official source:** https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng

NIS2 applicability is an organization- and national-law scope question; Duckworks does not assume mandatory applicability without entity/sector classification.

If Duckworks is in scope, Article 21 cybersecurity risk-management measures include areas directly relevant to FeatherForecast such as:

- risk analysis and information-system security;
- incident handling;
- business continuity and disaster recovery;
- supply-chain security;
- secure acquisition, development and maintenance;
- effectiveness assessment;
- access control; and
- cryptography/encryption where appropriate.

These obligations would attach through the in-scope entity and national implementation, not because a forecasting model is inherently regulated by NIS2.

### 2.3 Trade Secrets Directive — Directive (EU) 2016/943

**Official source:** https://eur-lex.europa.eu/eli/dir/2016/943/oj/eng

Supplier demand, commercial planning, inventory, lead-time and production information may qualify for trade-secret protection where the legal criteria are met, including that reasonable steps have been taken to keep the information secret.

FeatherForecast access control, logging, provider restrictions and data-minimization measures can support that protection, but the Directive is not a prescriptive cybersecurity-control standard and the portfolio does not determine legal trade-secret status for any specific dataset.

### 2.4 GDPR — Regulation (EU) 2016/679

GDPR is not treated as a primary FeatherForecast driver because the documented data categories are operational and aggregated.

It becomes applicable where supplier contacts, employee identifiers, order records or logs contain personal data. Where applicable, controller/processor, minimization, security, retention and breach obligations require separate assessment.

### 2.5 Cyber Resilience Act — Regulation (EU) 2024/2847

CRA applicability is **not established for FeatherForecast**.

The current system is an internal planning/analytics service. A separate assessment would be required if software generated or configured through FeatherForecast were itself placed on the market as a covered product with digital elements.

## 3. Standards and formal frameworks

These are guidance / adopted-management references, not independent legal-compliance conclusions.

### ISO/IEC 27001:2022

Relevant areas include access control, supplier security, secure configuration/change, logging, backup/recovery, information integrity and incident management.

Exact control mappings require an authorized copy.

### ISO/IEC 42001:2023

Relevant for AI lifecycle governance, roles, risk treatment, data governance, monitoring, controlled change, supplier integration, records and continual improvement.

No conformity or certification claim is made.

### NIST CSF 2.0

Relevant outcomes span Govern, Identify, Protect, Detect, Respond and Recover for data pipelines, supplier platforms, identities, model/configuration changes, monitoring and continuity.

### NIST AI RMF 1.0

Relevant to valid/reliable AI, data/model governance, measurement, monitoring, human oversight and risk treatment.

### NIST AI 100-2 E2025 — Adversarial Machine Learning taxonomy

**Official source:** https://csrc.nist.gov/pubs/ai/100/2/e2025/final

Useful for threat terminology around poisoning, evasion, data/model manipulation and lifecycle attack surfaces. It is technical guidance, not mandatory law.

## 4. Technical-security references

### NCSC / partners — Guidelines for Secure AI System Development

**Official source:** https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development

Relevant to secure data/model pipelines, supply-chain dependencies, asset/version management, deployment controls, logging and restoration to known-good state.

### MITRE ATLAS

**Official source:** https://atlas.mitre.org/

Useful for AI attack/failure-path taxonomy and detection hypotheses. ATLAS is a living reference; identifiers should be rechecked before final test mapping.

### OWASP / secure ML engineering practices

OWASP AI/ML and application-security guidance may inform pipeline, API, data validation and dependency-control design. These are technical references, not legal obligations.

## 5. FeatherForecast applicability matrix

| Source | Category | Current treatment | Technical use | Boundary |
|---|---|---|---|---|
| EU AI Act | Binding law | High-risk status not established | Classification/change triggers | Reassess if intended purpose/safety role changes |
| NIS2 | National-law dependent | Scope unresolved | Supplier/platform, resilience, access, effectiveness testing | Requires entity/sector applicability |
| Trade Secrets Directive | EU directive / national implementation | Potentially relevant to commercial planning/supplier information | Reasonable protective measures | Does not prescribe exact controls |
| GDPR | Binding regulation | Conditional | Personal data in supplier/contact/log data where present | Operational data is not automatically personal data |
| CRA | Binding regulation | Not established | Product/software context only | Internal planning service not automatically covered |
| ISO/IEC 27001 | Standard | Applicable reference | ISMS integration | Not certification proof |
| ISO/IEC 42001 | Standard | Applicable reference | AIMS lifecycle / monitoring / change | Not conformity proof |
| NIST AI RMF | Framework | Applicable | Reliability, monitoring, measurement, governance | Not law |
| NIST AI 100-2 | Technical guidance | Applicable | Poisoning/manipulation terminology | Not law |
| NCSC / MITRE ATLAS | Technical guidance | Applicable | Threat/control design | Not law |

## 6. Recommended Duckworks organizational practices

The following are project practices, not externally mandated requirements unless separately identified:

- identify and version every material forecast input dataset;
- validate schema, range, time-window, duplication and freshness before model ingestion;
- quarantine unexpected historical backfills or supplier-data revisions;
- preserve lineage from source record to feature to forecast;
- separate data-quality failure from genuine market drift;
- prevent unapproved retraining or model/configuration promotion;
- bind forecasts to model, configuration, feature and source-data versions;
- detect training-serving skew;
- use independent benchmark/back-test and stress-test cases;
- retain authorized human decision authority for material purchase/production commitments;
- record override/rejection rationale;
- prohibit direct forecast-to-commitment automation without a separate approved control decision;
- enforce least-privilege access to supplier and planning data;
- minimize data sent to the third-party platform;
- monitor vendor/platform availability and stale-forecast age;
- support manual planning fallback and known-good rollback;
- trigger reassessment on material model/data/configuration/vendor/use changes; and
- keep synthetic validation conclusions separate from production effectiveness.

## 7. Governance conclusion

This addendum creates no evidence ID and upgrades no control.

It establishes the reference boundary for FeatherForecast architecture and threat modelling.

The current governance position remains:

> **CONTINUE WITH MONITORING**

The FeatherForecast architecture, threat model, `DW-AI003-VAL-SEC-01` validation plan and deterministic `FFSEC-T001`–`FFSEC-T012` lab have now completed commit-bound replay and canonical evidence reconciliation. The next evidence requirement is production or production-equivalent operating evidence before any production-effectiveness, residual-risk, supplier-assurance or stronger governance conclusion.
