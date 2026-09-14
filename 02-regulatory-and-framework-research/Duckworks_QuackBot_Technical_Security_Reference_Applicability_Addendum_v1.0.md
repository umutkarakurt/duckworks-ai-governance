# AI-002 QuackBot — Technical Security Reference & Applicability Addendum

**Project:** Project W.I.N.G. — Phase II Technical AI Security Engineering & Adversarial Validation  
**Document ID:** DW-AI002-SEC-REF-01  
**Version:** 1.0  
**Research / review date:** 14 September 2026  
**System:** AI-002 — QuackBot  
**Status:** System-specific applicability baseline — not legal advice  
**Owner:** Eleanor Duckford — AI Governance Lead  
**Security reviewer:** Cassandra Duckley — Chief Information Security Officer  
**Legal reviewer:** Amelia Duckett — General Counsel  
**Privacy reviewer:** Delia Duckham — Data Protection Officer  
**Current governance gate:** **Pre-Production / Production Blocked**

> This addendum supplements `Duckworks_Technical_AI_Security_Reference_and_Applicability_Baseline_v1.0.md`. It separates mandatory legal requirements from standards/framework guidance, recognized technical references, recommended organizational practices, and project assumptions. It does not establish legal compliance, certification, conformity, or production security.

---

## 1. QuackBot portfolio facts used by this addendum

Current Duckworks records establish that QuackBot:

- is `AI-002`;
- supports Customer Operations;
- is a generative-AI / conversational-AI / RAG system;
- is intended to answer common customer questions, retrieve technical product information, provide troubleshooting and warranty guidance, and escalate complex or sensitive cases;
- uses the fictional HelixRiver AI Services S.A. hosted LLM while Duckworks controls the RAG knowledge base, customer-support workflow and escalation logic;
- may process customer contact/account data, support history, warranty information, chat transcripts, product documentation and troubleshooting knowledge;
- is **Pre-Production / Production Blocked**;
- has internal impact indicator **High**;
- remains blocked pending prompt/RAG security testing, escalation controls, content boundaries and monitoring; and
- is linked to `AI-002-R01`, `AI-002-R02` and `AI-002-R03`.

The primary existing control IDs are:

- `QB-01 — Curated RAG Source Allowlist`;
- `QB-02 — Grounding, Citation & Abstention Rules`;
- `QB-03 — Human Escalation SLA`;
- `QB-04 — Prompt Injection & RAG Adversarial Testing`;
- `QB-05 — Least-Privilege Retrieval & Tool Boundaries`; and
- `QB-06 — GenAI Security & Harm Monitoring`.

Existing Duckworks assumptions relevant to this phase include `ASM-005`, `ASM-010`, `ASM-012`, `ASM-013`, `ASM-014`, `ASM-016`, `ASM-018` and `ASM-026`.

---

# 2. Mandatory legal requirements — applicability-dependent

## 2.1 GDPR — Regulation (EU) 2016/679

**Type:** Binding EU regulation.  
**Official text:** https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng

### QuackBot relevance

The current QuackBot inventory allows processing of customer account/contact data, support history, warranty information and chat transcripts. Where those data constitute personal data and the GDPR applies, relevant data-protection obligations are mandatory.

Technical-security relevance includes, depending on the actual processing role and facts:

- data minimization and purpose limitation;
- integrity/confidentiality;
- data protection by design/default;
- risk-appropriate security;
- access control;
- logging and breach evidence;
- processor/supplier controls; and
- regular testing/assessment/evaluation of security measures.

### Boundary

This portfolio does not determine Duckworks' controller/processor role for each flow, lawful basis, retention period, transfer mechanism or breach-notification outcome.

## 2.2 EU Artificial Intelligence Act — Regulation (EU) 2024/1689

**Type:** Binding EU regulation.  
**Current consolidated working source:** https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng

### Article 50 — direct interaction transparency

Article 50(1) addresses AI systems intended to interact directly with natural persons and requires the relevant provider-side design/development transparency unless the interaction is obvious or an exception applies. Article 50(5) addresses how and when the information must be provided.

For a public-facing customer chatbot such as QuackBot, **Article 50 transparency is a direct applicability question and should be treated as a mandatory-law review item**, not merely a voluntary framework mapping.

The Phase II target architecture therefore includes a testable requirement that users are clearly informed that they are interacting with an AI system at or before the first interaction, subject to confirmation of Duckworks' exact legal role and any applicable exception.

### High-risk / Article 15 boundary

This technical-security phase does **not** classify QuackBot as a high-risk AI system.

The documented customer-service purpose does not, by itself, establish an Article 6 / Annex I or Annex III high-risk route. Article 15 must therefore not be represented as a mandatory QuackBot requirement unless a later legal classification establishes that status.

## 2.3 NIS2 — Directive (EU) 2022/2555

**Type:** EU directive implemented through national law.  
**Official text:** https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng

QuackBot is internet-facing and therefore relevant to entity-level cybersecurity risk management if Duckworks falls within applicable national NIS2 scope. Duckworks' fictional manufacturing profile justifies a scope assessment but does not establish mandatory applicability.

**Status:** scope-dependent; not assumed mandatory.

## 2.4 Cyber Resilience Act — Regulation (EU) 2024/2847

The current QuackBot scenario is a customer-facing AI service using a hosted model. That fact alone does not establish that QuackBot is a product with digital elements within CRA scope or that Duckworks holds a covered economic-operator role for this system.

**Status:** not established; product/scope analysis required.

## 2.5 Consumer, warranty and product-support law

QuackBot's ability to provide warranty and product-support information creates a legal-content risk already recorded as `AI-002-R03`.

This addendum does **not** invent a single EU-wide warranty/consumer-law rule for all QuackBot deployments. Applicable consumer, sales, warranty, product-safety and national rules must be reviewed for the actual markets, products and statements involved.

Duckworks therefore treats legal/warranty response boundaries, approved content and human escalation as **organizational controls pending system-specific legal confirmation**.

---

# 3. Standards and formal frameworks

These sources are guidance or voluntary standards unless another mechanism makes them binding.

## 3.1 ISO/IEC 27001:2022

Use at the management-system/control-domain level for:

- internet-facing application security;
- identity/access;
- supplier security;
- secure development;
- configuration/change control;
- logging/monitoring;
- incident response;
- vulnerability management; and
- information protection.

No clause/control text is reproduced here; exact mapping requires an authorized copy.

## 3.2 ISO/IEC 42001:2023

Use for:

- lifecycle governance;
- role/accountability;
- AI risk treatment;
- controlled change;
- monitoring;
- evidence;
- supplier integration; and
- continual improvement.

This does not establish AIMS conformity or certification.

## 3.3 NIST CSF 2.0

QuackBot use:

- **Govern:** ownership, risk/gate decisions, supplier boundaries;
- **Identify:** internet/API assets, data, dependencies and attack surface;
- **Protect:** session/authentication, retrieval authorization, secure development, rate controls, data minimization;
- **Detect:** injection, retrieval anomaly, leakage, resource-abuse and integrity signals;
- **Respond:** containment, escalation, account/session blocking, corpus quarantine;
- **Recover:** known-good KB/model/config restoration and lessons learned.

## 3.4 NIST AI RMF 1.0 and NIST AI 600-1

Use for GenAI risk framing, measurement, human interaction, content reliability, monitoring and risk-management decisions.

## 3.5 NIST SP 800-218 / 800-218A

Use for secure development, dependency/version management, build/release integrity, artifact provenance and vulnerability handling.

---

# 4. Official and recognized technical-security guidance

## 4.1 ENISA Multilayer Framework

QuackBot follows the principle:

**cybersecurity foundations → AI-specific cybersecurity → customer-service / internet-facing system context**

## 4.2 NCSC / partner Guidelines for Secure AI System Development

Use across secure design, development, deployment, operation and maintenance.

## 4.3 OWASP GenAI Security Project

Relevant QuackBot themes include:

- prompt injection;
- sensitive-information disclosure;
- supply-chain vulnerabilities;
- data/model poisoning;
- improper output handling;
- excessive agency;
- system-prompt leakage;
- vector/embedding weaknesses;
- misinformation; and
- unbounded resource consumption.

These are technical references, not legal obligations.

## 4.4 OWASP API Security Top 10 — 2023

Particularly relevant:

- broken object-level authorization;
- broken authentication;
- broken object-property authorization;
- unrestricted resource consumption;
- broken function-level authorization;
- unrestricted access to sensitive business flows;
- server-side request forgery;
- security misconfiguration;
- improper inventory management; and
- unsafe consumption of APIs.

## 4.5 MITRE ATLAS

Use for attacker behavior, GenAI/RAG attack-path design, poisoning/injection analysis, red-team planning and detection hypotheses.

ATLAS is a living resource. Technique names/IDs should be checked at test-execution time rather than frozen prematurely in this design record.

---

# 5. QuackBot applicability matrix

| Source | Category | Current QuackBot treatment | Phase II technical use | Caution |
|---|---|---|---|---|
| GDPR | Binding law | Potentially mandatory where personal data are processed | Minimize context, authorization, logging/redaction, supplier processing, security testing | Confirm roles, data flows and jurisdiction |
| EU AI Act Article 50 | Binding law | Direct applicability review required for customer-facing AI interaction | AI-interaction disclosure and accessible first-interaction notice | Confirm Duckworks legal role and exception analysis |
| EU AI Act Article 15 | Binding only for covered high-risk AI | High-risk status not established | Robustness/cybersecurity reference only | Do not imply high-risk classification |
| NIS2 | Binding via national law if in scope | Organization-level applicability unresolved | Internet-facing security, incidents, supply chain, effectiveness testing | Assess national implementation/entity scope |
| CRA | Binding EU regulation where scope met | Not established | Product-security reference only | Requires product/economic-operator analysis |
| ISO/IEC 27001 | Standard | Management-system/control reference | App/API security, supplier, logging, incidents, secure development | Not proof of certification |
| ISO/IEC 42001 | Standard | AIMS reference | AI lifecycle, roles, monitoring, change/evidence | Not proof of conformity |
| NIST AI RMF / 600-1 | Voluntary framework/profile | Applicable as risk structure | Map/Measure/Manage GenAI risk | Not law |
| OWASP GenAI | Technical guidance | Applicable | GenAI threat/test coverage | Not law |
| OWASP API Top 10 | Technical guidance | Applicable | API/session/resource/SSRF coverage | Not law |
| MITRE ATLAS | Threat knowledge base | Applicable | Attack-path and test planning | Living source; re-check at execution |

---

# 6. Duckworks recommended organizational practices for QuackBot

The following are **recommended project practices**, not statements of external legal requirement unless separately identified:

- separate anonymous/public interaction from authenticated customer-account access;
- enforce customer/account authorization outside the model;
- treat retrieved text and model output as untrusted;
- permit retrieval only from approved/provenanced corpora;
- disable tools/actions by default for the first Phase II increment;
- keep account/warranty state-changing actions outside the model path;
- rate-limit and resource-limit public/API traffic;
- constrain safety, warranty and legal-topic answers to approved sources or human escalation;
- redact/minimize customer data sent to the model provider and telemetry;
- enforce session isolation and cache partitioning;
- record model/config/KB/provider versions;
- require regression testing after material change; and
- retain evidence that distinguishes synthetic security behavior from production effectiveness.

---

# 7. Project assumptions used by the technical foundation

The authoritative assumptions register remains controlling.

Phase II additionally uses explicit synthetic design assumptions `QBA-001` onward in the QuackBot architecture. These assumptions make the lab/test design executable but are **not production facts**.

`ASM-010 — QuackBot escalation` remains Open / High.

`ASM-026 — QuackBot vendor architecture` remains Open / High.

No architecture or threat-model document closes either assumption.

---

# 8. Governance conclusion

This addendum authorizes no deployment.

It establishes the legal/framework/technical reference boundary for the **design** of QuackBot's Phase II architecture and threat model.

The current lifecycle decision remains:

> **PRODUCTION BLOCKED PENDING GATES**

The next evidence step is a separate QuackBot technical-security validation plan and controlled synthetic test lab.
