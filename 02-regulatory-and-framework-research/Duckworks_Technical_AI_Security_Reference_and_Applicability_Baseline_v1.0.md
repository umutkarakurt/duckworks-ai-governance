# Duckworks Technical AI Security Reference & Applicability Baseline

**Project:** Project W.I.N.G. — Phase II Technical AI Security Engineering & Adversarial Validation  
**Document ID:** DW-WING-SEC-REF-01  
**Version:** 1.0  
**Research date:** 10 September 2026  
**Status:** Portfolio research baseline — not legal advice  
**Initial system:** AI-006 — PondGPT  
**Owner:** Eleanor Duckford — AI Governance Lead  
**Security reviewer:** Cassandra Duckley — Chief Information Security Officer

> This document separates binding legal requirements, standards/framework guidance, recognized technical-security references, and Duckworks project practices. A reference is not a compliance conclusion. Applicability depends on the actual facts, organizational role, jurisdiction, intended purpose, data, deployment and current law.

---

## 1. Evidence hierarchy used in Phase II

Duckworks uses the following order when making a technical-security or applicability claim:

1. **Binding legal text** — EUR-Lex / Official Journal and applicable national implementing law.
2. **Official regulator or government cybersecurity guidance** — e.g., ENISA, NCSC, CISA, NIST.
3. **International standards and formal frameworks** — e.g., ISO/IEC, NIST.
4. **Recognized technical threat and security references** — e.g., MITRE ATLAS, OWASP.
5. **Internal Duckworks requirements and engineering decisions**.
6. Secondary commentary only when needed for interpretation, and not as the primary authority for a legal conclusion.

---

# 2. Mandatory legal requirements — applicability-dependent

## 2.1 GDPR — Regulation (EU) 2016/679

**Type:** Binding EU regulation.  
**Primary technical-security relevance:** Personal-data security.  
**Official text:** https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng

### Relevant provisions

**Article 5(1)(f) — integrity and confidentiality principle.** Personal data must be processed with appropriate security, including protection against unauthorized or unlawful processing and accidental loss, destruction or damage, using appropriate technical or organizational measures.

**Article 25 — data protection by design and by default.** Where Duckworks acts as controller, the technical design must take data-protection principles and safeguards into account according to the provision's conditions.

**Article 32 — security of processing.** Controllers and processors must implement technical and organizational measures appropriate to risk. Article 32 expressly addresses confidentiality, integrity, availability, resilience and a process for regularly testing, assessing and evaluating the effectiveness of security measures.

**Articles 33–34 — personal-data breach response.** Notification obligations may arise when the conditions in those provisions are met.

### PondGPT applicability

**Potentially mandatory.** The Duckworks scenario allows PondGPT to process employee or other personal data. If PondGPT processes personal data within GDPR scope, the relevant GDPR security requirements apply to that processing.

### Phase II technical use

- permission-aware retrieval;
- least-privilege access;
- secure logging;
- encryption and secret handling;
- isolation of personal-data repositories;
- DLP testing;
- security-effectiveness testing;
- incident evidence; and
- secure supplier processing arrangements.

### Uncertainty / legal boundary

This portfolio does not determine Duckworks' exact controller/processor roles for every PondGPT data flow, lawful bases, international-transfer conditions or breach-notification conclusions.

---

## 2.2 NIS2 — Directive (EU) 2022/2555

**Type:** EU directive requiring national implementation.  
**Primary technical-security relevance:** Organization-level cybersecurity risk management.  
**Official text:** https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng

### Relevant provision

**Article 21 — cybersecurity risk-management measures.** For entities within scope, national law implementing NIS2 must require appropriate and proportionate technical, operational and organizational measures. Article 21 addresses, among other areas:

- risk analysis and information-system security;
- incident handling;
- business continuity;
- supply-chain security;
- secure acquisition, development and maintenance;
- vulnerability handling;
- effectiveness assessment;
- cyber hygiene and training;
- cryptography/encryption;
- access control and asset management; and
- multi-factor or continuous-authentication solutions where appropriate.

### PondGPT applicability

**Scope-dependent; not assumed mandatory.** Duckworks' fictional scale and manufacturing activities justify a NIS2 applicability assessment, but the portfolio does not establish that Duckworks is an essential or important entity under a particular Member State's implementing law.

### Phase II technical use

If Duckworks is in scope, PondGPT security engineering may form part of the entity-level technical and organizational measures used to manage network and information-system risk.

### Uncertainty / legal boundary

A real assessment must use the relevant Member State's current national implementing law and the entity/sector classification.

---

## 2.3 EU Artificial Intelligence Act — Regulation (EU) 2024/1689

**Type:** Binding EU regulation.  
**Working source:** consolidated text as of 27 July 2026.  
**Official consolidated text:** https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng

### Relevant provision

**Article 15 — accuracy, robustness and cybersecurity** applies to **high-risk AI systems** and requires such systems to achieve an appropriate level of accuracy, robustness and cybersecurity and to perform consistently in those respects throughout their lifecycle. The provision also addresses resilience to AI-specific vulnerabilities and attacks.

### PondGPT applicability

**Not currently treated as a mandatory Article 15 case.** PondGPT's current documented intended purpose is an internal employee productivity and knowledge assistant. The current Duckworks materials do not establish a legal classification of PondGPT as a high-risk AI system.

Article 15 is therefore useful as a technical reference, but Phase II must not claim that PondGPT is legally required to comply with Article 15 unless a later legal classification establishes the relevant high-risk route.

### Reassessment triggers

Reassess if PondGPT's intended purpose materially changes, particularly if it begins to perform functions that could fall within a legally high-risk use category or becomes a safety component of a regulated product.

---

## 2.4 Cyber Resilience Act — Regulation (EU) 2024/2847

**Type:** Binding EU regulation with staged application.  
**Official text:** https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng

### PondGPT applicability

**Not presently established.** The CRA applies to products with digital elements under its scope and associated economic-operator roles and conditions. The current PondGPT scenario is an internally operated enterprise AI application supported by a hosted LLM service. That fact pattern does not by itself establish CRA applicability to PondGPT.

### Phase II treatment

CRA concepts can inform secure-product and vulnerability-management thinking, but this portfolio will not describe CRA requirements as mandatory for PondGPT without a product/scope analysis.

---

# 3. International standards and formal frameworks

The sources in this section do not by themselves establish legal compliance.

## 3.1 ISO/IEC 27001:2022 — Information security management systems

**Type:** International requirements standard; certification is voluntary unless made contractual or otherwise required.  
**Official page:** https://www.iso.org/standard/27001

**Duckworks use:** Integrate AI security into the existing information-security management system rather than creating a separate cybersecurity universe.

Phase II uses ISO/IEC 27001 at the **management-system and control-domain level**, including themes such as:

- information-security risk management;
- identity and access;
- supplier security;
- asset management;
- secure development;
- configuration and change management;
- logging and monitoring;
- incident management;
- vulnerability management; and
- protection of information.

**Copyright boundary:** This portfolio does not reproduce the copyrighted standard. Exact clause/control mapping should be performed using an authorized copy and should not be inferred solely from public summaries.

---

## 3.2 ISO/IEC 42001:2023 — Artificial intelligence management system

**Type:** International AIMS requirements standard.  
**Official page:** https://www.iso.org/standard/42001

**Duckworks use:** Management-system integration, lifecycle governance, roles, risk treatment, controlled changes, monitoring, evidence and continual improvement for AI.

**Phase II use:** Demonstrate that technical AI-security testing produces evidence consumable by the broader AIMS rather than existing as an isolated red-team exercise.

**Copyright boundary:** Exact requirement/control text is not reproduced here; mapping should be verified using an authorized copy.

---

## 3.3 NIST Cybersecurity Framework 2.0

**Type:** Voluntary cybersecurity risk-management framework.  
**Official publication:** https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20  
**CSF resource center:** https://www.nist.gov/cyberframework

**Core functions:** Govern, Identify, Protect, Detect, Respond, Recover.

**PondGPT use:**

- **Govern:** technical-security ownership, risk decisions and supplier governance;
- **Identify:** assets, architecture, dependencies, data and vulnerabilities;
- **Protect:** IAM, authorization, secure development, egress and data protection;
- **Detect:** AI/application telemetry and alerting;
- **Respond:** AI incident triage, containment and evidence;
- **Recover:** rollback, re-indexing, key rotation, known-good restoration and lessons learned.

The CSF is outcome-oriented and does not prescribe a single implementation.

---

## 3.4 NIST AI Risk Management Framework 1.0

**Type:** Voluntary AI risk-management framework.  
**Official publication:** https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf  
**Resource center:** https://airc.nist.gov/

**Functions:** Govern, Map, Measure, Manage.

**PondGPT use:** Connect threat modelling, adversarial measurement, control implementation and residual-risk decisions to the existing Duckworks AI risk method.

---

## 3.5 NIST AI 600-1 — Generative AI Profile

**Type:** NIST AI RMF profile for generative AI.  
**Official PDF:** https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf

**PondGPT use:** Generative-AI risk analysis, evaluation design, content/data risks, human-AI interaction and GenAI-specific risk-management practices.

---

## 3.6 NIST AI 100-2 E2025 — Adversarial Machine Learning

**Full title:** *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations*  
**Type:** NIST technical taxonomy and terminology.  
**Official page:** https://csrc.nist.gov/pubs/ai/100/2/e2025/final  
**DOI:** https://doi.org/10.6028/NIST.AI.100-2e2025

**PondGPT use:**

- common adversarial-ML terminology;
- attacker goals, capabilities and knowledge;
- lifecycle stage of attack;
- poisoning and evasion concepts;
- privacy attacks;
- abuse/misuse analysis; and
- mitigation terminology.

**Important:** This is not a legal requirement and not a control checklist. It is used to improve technical precision in threat statements and test design.

---

## 3.7 NIST SP 800-218 and SP 800-218A

**SP 800-218:** Secure Software Development Framework (SSDF).  
**SP 800-218A:** *Secure Software Development Practices for Generative AI and Dual-Use Foundation Models: An SSDF Community Profile*.  
**Official SP 800-218A page:** https://csrc.nist.gov/pubs/sp/800/218/a/final

**PondGPT use:**

- secure development requirements;
- dependency and artifact integrity;
- build/release controls;
- AI-specific software/model lifecycle considerations;
- versioning;
- provenance;
- vulnerability handling; and
- security testing integrated into development.

---

# 4. Official cybersecurity guidance

## 4.1 ENISA — Multilayer Framework for Good Cybersecurity Practices for AI

**Type:** Official EU cybersecurity good-practice guidance.  
**Official page:** https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai

ENISA structures AI cybersecurity across three layers:

1. cybersecurity foundations;
2. AI-specific cybersecurity; and
3. sector-specific cybersecurity for AI.

**PondGPT use:** This is a strong architectural principle for Phase II: conventional cybersecurity controls remain the foundation, with AI-specific controls added where the AI attack surface requires them.

---

## 4.2 NCSC / international partners — Guidelines for Secure AI System Development

**Type:** Government cybersecurity guidance, originally published by the UK NCSC with international partners.  
**Official collection:** https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development

The guidance is structured around:

- secure design;
- secure development;
- secure deployment; and
- secure operation and maintenance.

**PondGPT use:**

- threat modelling during design;
- supply-chain protection;
- documentation of AI assets;
- secure infrastructure;
- model/data protection;
- incident procedures;
- logging and monitoring;
- secure updates; and
- lifecycle security.

---

# 5. Recognized technical threat and security references

## 5.1 MITRE ATLAS

**Type:** Living knowledge base of adversary tactics and techniques involving AI.  
**Official site:** https://atlas.mitre.org/

**PondGPT use:**

- attacker-behavior analysis;
- AI threat scenarios;
- red-team planning;
- attack-path decomposition;
- technique-to-mitigation traceability; and
- detection hypotheses.

**Versioning rule:** ATLAS is a living knowledge base. Technique names/IDs used in future test cases must be checked against the live catalogue at the date of the test. This baseline does not freeze technique identifiers.

---

## 5.2 OWASP GenAI Security Project — LLM/GenAI Top 10

**Type:** Community technical-security guidance.  
**Current 2026 resource:** https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/  
**Project:** https://genai.owasp.org/

Security themes particularly relevant to PondGPT include:

- prompt injection;
- sensitive-information disclosure;
- supply-chain vulnerabilities;
- data/model poisoning;
- improper output handling;
- excessive agency;
- system-prompt leakage;
- vector and embedding weaknesses;
- misinformation/reliability risk; and
- unbounded resource consumption.

**PondGPT use:** Threat coverage and adversarial-test completeness.

**Important:** OWASP categories are not legal requirements and are not themselves proof that a control is effective.

---

## 5.3 OWASP API Security Top 10 — 2023

**Type:** Community API-security guidance.  
**Official project:** https://owasp.org/API-Security/  
**2023 edition:** https://owasp.org/API-Security/editions/2023/en/0x11-t10/

Relevant API risk areas include:

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

**PondGPT use:** Prevent the technical-security phase from reducing application security to prompt injection alone.

---

# 6. PondGPT applicability matrix

| Source | Category | Current PondGPT status | Technical use | Legal/compliance caution |
|---|---|---|---|---|
| GDPR | Binding law | Potentially applicable where personal data are processed | CIA, access control, DLP, security testing, incidents | Confirm actual processing roles/data flows |
| NIS2 | Binding through national implementation | Organization-level applicability unresolved | Secure development, supply chain, incidents, access, effectiveness testing | Must assess national implementing law |
| EU AI Act Art. 15 | Binding for covered high-risk AI | Not currently established as mandatory for PondGPT | Useful high-risk cybersecurity reference | Do not call PondGPT high-risk without legal basis |
| CRA | Binding EU regulation | Not established for internal PondGPT service | Product-security reference only | Requires product/scope analysis |
| ISO/IEC 27001 | Standard | Applicable as Duckworks ISMS reference | Conventional cyber controls and management system | Does not prove compliance/certification |
| ISO/IEC 42001 | Standard | Applicable as AIMS reference | AI lifecycle, evidence, monitoring, change | Does not prove certification |
| NIST CSF 2.0 | Voluntary framework | Applicable as cyber-risk structure | Govern/Identify/Protect/Detect/Respond/Recover | Not law |
| NIST AI RMF | Voluntary framework | Applicable | AI risk structure and measurement | Not law |
| NIST AI 600-1 | Voluntary profile | Strong relevance | GenAI risk/evaluation | Not law |
| NIST AI 100-2 E2025 | Technical taxonomy | Strong relevance | Adversarial-ML terminology/test design | Not a control checklist |
| NIST SP 800-218A | Secure-development guidance/profile | Strong relevance | GenAI SDLC / supply chain / testing | Not law |
| ENISA AI cybersecurity framework | Official good-practice guidance | Strong relevance | Foundational + AI-specific layers | Guidance |
| NCSC secure AI development | Government guidance | Strong relevance | Secure design/develop/deploy/operate | Guidance |
| MITRE ATLAS | Threat knowledge base | Strong relevance | Adversary behavior, red team, detection | Living taxonomy |
| OWASP GenAI | Community security guidance | Core technical reference | LLM/RAG attack coverage | Not compliance |
| OWASP API Security | Community security guidance | Core application reference | API/auth/resource/SSRF risks | Not compliance |

---

# 7. Duckworks Phase II engineering requirements derived from the reference set

The following are **Duckworks recommended organizational/technical practices**. They are not presented as verbatim requirements of any external source.

| Requirement ID | Duckworks requirement | Primary rationale |
|---|---|---|
| TSR-001 | Enforce authorization before any retrieved chunk enters the LLM context. | Prevent confidentiality failure regardless of model behavior |
| TSR-002 | Treat retrieved content as untrusted data, never as authoritative instructions. | Reduce indirect prompt-injection risk |
| TSR-003 | Treat model output as untrusted input to downstream systems. | Prevent output-mediated injection/execution |
| TSR-004 | Enforce tool authorization outside the model and per action. | Prevent excessive agency/confused deputy |
| TSR-005 | Fail closed when identity/authorization state cannot be verified. | Prevent authorization bypass during dependency failure |
| TSR-006 | Use deny-by-default outbound network policy for model/tool workloads. | Restrict exfiltration and SSRF paths |
| TSR-007 | Keep secrets out of prompts, retrieved documents and model-readable configuration. | Reduce secret disclosure |
| TSR-008 | Validate document provenance, classification and integrity before indexing. | Reduce poisoning/tampering |
| TSR-009 | Separate document ingestion privilege from retrieval/user privilege. | Reduce insider/poisoning blast radius |
| TSR-010 | Version and identify model, embedding model, index, system prompt and security policy for each test. | Reproducibility and change control |
| TSR-011 | Pin and scan application dependencies and container artifacts. | Conventional software-supply-chain security |
| TSR-012 | Redact/minimize sensitive prompt and response content in security logs. | Avoid turning telemetry into a data-leak repository |
| TSR-013 | Correlate user, retrieval, policy, model and tool events with a common request ID. | Incident reconstruction and detection |
| TSR-014 | Apply request/token/tool budgets and rate limits. | Resource-consumption control |
| TSR-015 | Disable active external content in rendered model output unless explicitly allowed and sanitized. | Prevent output-based exfiltration/XSS |
| TSR-016 | Maintain a reproducible adversarial regression suite for security-critical AI behavior. | Detect control regression after change |
| TSR-017 | Preserve raw test evidence and hashes separately from the analyst conclusion. | Auditability |
| TSR-018 | Do not grant residual-risk reduction solely because a security control is documented. | Existing Duckworks evidence principle |

---

# 8. PondGPT legal-security conclusion

For the current fictional PondGPT design:

- **GDPR security requirements are potentially mandatory** when PondGPT processes personal data within GDPR scope.
- **NIS2 remains scope-dependent** and cannot be treated as mandatory for Duckworks without a national/entity applicability analysis.
- **EU AI Act Article 15 is not currently asserted as a mandatory PondGPT requirement** because the current internal-assistant intended purpose does not establish high-risk classification.
- **CRA applicability is not currently established** for the internal PondGPT service.
- ISO, NIST, ENISA, NCSC, MITRE and OWASP sources are used as standards, frameworks, guidance or technical references according to their actual status.
- Duckworks Phase II security requirements are internal engineering choices informed by those sources and by the documented threat model.

---

# 9. Maintenance and verification rules

1. Re-check legal consolidated texts before publishing a material legal conclusion.
2. Re-check MITRE ATLAS and OWASP living resources when assigning technique/category identifiers to test cases.
3. Do not reproduce copyrighted ISO standard text beyond public descriptions; verify exact mappings against an authorized copy.
4. Record the source version/date used in each technical test plan.
5. Reassess applicability when PondGPT's intended purpose, user population, data, deployment model, supplier or integration pattern changes.
6. Update the root `REFERENCES.md` when this Phase II baseline is merged, but keep this focused security baseline as the detailed working source for technical artifacts.

---

# 10. Portfolio disclaimer

Duckworks, PondGPT, LanternMind Enterprise AI Ltd., personnel, systems, data, attacks and evidence are fictional or synthetic. Public laws, standards, frameworks and technical-security sources are identified above.

This document is a portfolio research and engineering artifact, not legal advice, certification evidence, a penetration-test authorization for real systems, or a statement of production security.
