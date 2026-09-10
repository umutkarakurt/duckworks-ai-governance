# Duckworks Technical AI & Cybersecurity Engineering Scope Addendum

**Project:** Project W.I.N.G. — Workflows, Intelligence, Next-Generation Governance  
**Document ID:** DW-WING-SCOPE-SEC-01  
**Version:** 1.0  
**Effective date:** 10 September 2026  
**Status:** Portfolio design baseline — fictional / synthetic / non-production  
**Owner:** Eleanor Duckford — AI Governance Lead  
**Security owner:** Cassandra Duckley — Chief Information Security Officer  
**Technical owner:** Dr. Ada Duckfield — Head of Data & AI  
**Applies to:** Phase II — Technical AI Security Engineering & Adversarial Validation

> **Scope relationship.** This addendum does not rewrite or invalidate the original Duckworks AI Governance Project scope. The original scope correctly excluded comprehensive penetration testing, AI red teaming, adversarial model testing, vulnerability scanning, source-code review, API security testing and infrastructure penetration testing from the initial governance-readiness phase. This addendum authorizes a bounded **Phase II portfolio workstream** in which selected technical security activities are performed only against fictional Duckworks systems, synthetic data, locally controlled test components, or explicitly authorized test environments.

---

## 1. Purpose

Phase II moves selected Project W.I.N.G. security requirements from governance design toward technically demonstrable engineering evidence.

The objective is not to claim that a production Duckworks environment has been secured. The objective is to demonstrate a defensible security-engineering chain:

**architecture → threat model → security requirement → implementation → adversarial test → telemetry → evidence → remediation → retest → governance conclusion**

The workstream combines conventional cybersecurity with AI-specific security. AI components are treated as part of an end-to-end information system rather than as isolated models.

---

## 2. Phase II objectives

Phase II shall demonstrate that Duckworks can:

1. define security-relevant system architecture, assets, identities, data flows, trust boundaries and external dependencies for selected AI systems;
2. distinguish conventional application, API, identity, cloud, software-supply-chain and infrastructure threats from AI-specific attack mechanisms;
3. perform structured threat modelling using system data flows and realistic attacker objectives;
4. convert identified threats into explicit, testable security requirements;
5. implement selected controls in a synthetic or locally controlled lab;
6. execute controlled adversarial tests against an intentionally weak baseline and against the remediated state;
7. retain reproducible technical evidence including configuration, test inputs, execution logs, results, hashes, exceptions and reviewer conclusions;
8. design detections and incident-response signals for AI-specific and conventional attack paths;
9. connect technical findings to the existing Duckworks risk and control architecture without creating an untraceable parallel risk universe; and
10. preserve a clear boundary between **synthetic technical demonstration** and **production operating effectiveness**.

---

## 3. Initial technical-security target

The first Phase II target is:

**AI-006 — PondGPT**

PondGPT is selected because the current Duckworks portfolio already identifies:

- `AI-006-R01 — Privacy & data governance`;
- `AI-006-R02 — Security & adversarial manipulation`;
- `AI-006-R03 — Reliability & robustness`;
- `PG-01 — Permission-Aware Retrieval`;
- `PG-02 — Automated Permission Regression & DLP Tests`;
- `PG-03 — Prompt Injection & RAG Poisoning Test Suite`;
- `PG-04 — Tool Sandboxing & Allowlisted Actions`;
- `PG-05 — GenAI Security Logging & Alerting`; and
- `PG-06 — Secure Output Verification & Code Scanning`.

Existing PondGPT operating-evidence artifacts demonstrate a bounded synthetic permission-regression and DLP test mechanism for `PG-01` and `PG-02`. They do **not** establish the existence or effectiveness of a real production architecture. Phase II builds from that boundary rather than treating the synthetic evidence as production proof.

---

## 4. In-scope technical activities

### 4.1 Security architecture engineering

In scope:

- logical and deployment architecture;
- component inventory;
- data-flow diagrams;
- network and service boundaries;
- identity flows;
- authorization enforcement points;
- service identities;
- secrets handling;
- model/API gateway architecture;
- RAG ingestion and retrieval paths;
- vector-store security;
- tool and connector boundaries;
- outbound network/egress controls;
- audit logging and telemetry;
- evidence storage;
- failure-mode and fail-safe design; and
- documented security invariants.

### 4.2 Threat modelling

In scope:

- asset identification;
- trust-boundary analysis;
- attacker profiles and preconditions;
- STRIDE-style analysis for conventional system threats;
- AI-specific attack-path analysis informed by NIST adversarial-ML terminology, MITRE ATLAS and OWASP GenAI security guidance;
- abuse cases;
- attack trees where useful;
- threat-to-risk and threat-to-control traceability;
- threat prioritization for technical testing; and
- reassessment after material architectural change.

Threat-model priorities are **not** substitutes for Duckworks' approved enterprise risk ratings.

### 4.3 Identity, authentication and authorization testing

In scope:

- authentication-flow review;
- signed-token validation;
- session and token-lifetime controls;
- role/group claim handling;
- object-level and function-level authorization;
- permission-aware retrieval;
- stale ACL and stale group-membership scenarios;
- cross-user and cross-role isolation;
- service-account privilege;
- fail-open/fail-closed behavior; and
- privilege-boundary regression testing.

### 4.4 Generative-AI and RAG security testing

In scope:

- direct prompt injection;
- indirect prompt injection;
- malicious retrieved instructions;
- RAG corpus poisoning;
- document provenance failures;
- classification/metadata tampering;
- vector/index integrity attacks;
- system-prompt disclosure testing;
- sensitive-information disclosure;
- context-boundary failures;
- unsafe reliance on model refusals as access control;
- encoded/obfuscated adversarial content;
- prompt-to-tool manipulation; and
- output-mediated exfiltration attempts in the synthetic lab.

### 4.5 Application and API security

In scope:

- API authentication and authorization;
- broken object-level authorization;
- broken function-level authorization;
- unsafe API consumption;
- input validation;
- server-side request forgery paths;
- security misconfiguration;
- rate and resource controls;
- injection into downstream components;
- unsafe model-output rendering;
- session isolation;
- transport security;
- dependency exposure; and
- controlled dynamic testing of the synthetic application.

### 4.6 Tool, agent and connector security

Where PondGPT tool use is enabled in the lab, in scope:

- allowlisted tools and actions;
- per-tool service identities;
- argument/schema validation;
- least privilege;
- sandboxing;
- human approval for high-impact actions;
- egress restrictions;
- confused-deputy scenarios;
- tool-output trust boundaries;
- replay and duplicate-action controls; and
- telemetry for tool requests and policy decisions.

Tools remain **disabled by default** unless a test requires them.

### 4.7 Software and AI supply-chain security

In scope:

- software composition analysis;
- dependency pinning;
- lock files;
- container/base-image review;
- SBOM generation;
- AI-BOM extension where useful;
- package integrity and provenance;
- model/provider version tracking;
- embedding-model version tracking;
- image and artifact digest verification;
- secrets scanning;
- source-code scanning;
- CI/CD security gates;
- third-party model/service change handling; and
- rollback to known-good versions.

### 4.8 Security telemetry and detection engineering

In scope:

- authentication events;
- authorization decisions;
- retrieval decisions;
- source-document IDs and provenance metadata;
- prompt-injection detections;
- tool invocation attempts;
- policy denials;
- data-loss prevention signals;
- rate-limit/resource events;
- model/provider version changes;
- integrity failures;
- security exceptions;
- correlation identifiers;
- alert logic; and
- synthetic incident reconstruction.

Logs must be designed so that evidence collection does not itself create uncontrolled sensitive-data exposure.

### 4.9 Controlled red-team and adversarial validation

In scope:

- test plans;
- bounded adversarial campaigns;
- known-safe synthetic payloads;
- baseline exploitation;
- control bypass attempts;
- remediation;
- deterministic or repeatable retesting where feasible;
- evidence capture;
- negative testing;
- detection validation; and
- documented limitations.

The goal is **control validation**, not maximization of exploit impact.

### 4.10 Adversarial ML for later AI systems

After PondGPT, future Phase II targets may include:

- WingInspect Vision — evasion, adversarial examples, image corruption, distribution shift and false-negative resilience;
- DuckDesign AI — generated-code security, engineering-data boundaries, supply-chain compromise and tool-use risk;
- QuackBot — internet-facing RAG, anonymous abuse, session isolation, resource exhaustion and customer-data leakage; and
- FeatherForecast — poisoning, data integrity, model drift and decision-support resilience.

Each target requires its own architecture and threat-model record before testing.

---

## 5. Out-of-scope and prohibited activities

Phase II does **not** authorize:

- testing any real third-party system without explicit authorization;
- attacking a real LLM provider, SaaS platform, cloud tenant or vendor;
- credential theft from real users;
- use of real employee, customer, applicant, government or employer-confidential information;
- persistence on systems outside the controlled lab;
- malware deployment against third parties;
- destructive payloads;
- denial-of-service against external services;
- uncontrolled internet scanning;
- exploiting unrelated vulnerable systems;
- social engineering of real people;
- bypassing provider terms or technical access restrictions;
- collection of production secrets;
- real-world phishing;
- any claim that lab results prove production security;
- any claim that framework mapping proves legal compliance or certification; or
- independent-assurance claims where Internal Audit or another independent reviewer has not actually performed the work.

---

## 6. Authorization boundary

Every technical test must identify:

| Field | Required record |
|---|---|
| Target | Exact Duckworks synthetic component or controlled test endpoint |
| Environment | Local lab, synthetic CI environment, or other explicitly authorized test environment |
| Data | Synthetic only unless separately approved |
| Test owner | Named technical tester |
| Security owner | CISO or delegated security reviewer |
| Allowed techniques | Defined in test plan |
| Excluded techniques | Explicitly recorded |
| Start/end condition | Defined before execution |
| Evidence location | Repository path / evidence ID |
| Stop condition | Unexpected external impact, uncontrolled data exposure, instability, or scope ambiguity |

If target ownership or authorization is uncertain, testing stops until the boundary is clarified.

---

## 7. Evidence rules

### 7.1 Minimum evidence package

A material technical security test should retain, where applicable:

- test ID and version;
- date/time;
- target component and version/digest;
- environment identifier;
- tester;
- test objective;
- preconditions;
- sanitized test input;
- expected result;
- actual result;
- HTTP/API response metadata where relevant;
- application/retrieval/policy logs;
- security alert or detection record;
- relevant configuration snapshot;
- tool/version information;
- exit code;
- evidence hash;
- result classification;
- remediation reference;
- retest result; and
- reviewer conclusion.

### 7.2 Evidence maturity

Phase II uses the existing Duckworks evidence-aware status principle.

A reproducible synthetic test can demonstrate that a mechanism exists and behaves as recorded within the defined lab. It does **not** provide production risk-reduction credit unless the authorized Duckworks risk methodology has evidence sufficient to justify that conclusion.

### 7.3 Negative evidence

Absence of an alert is not automatically evidence that no attack occurred.

Detection tests must establish:

1. the attack/test was executed;
2. the relevant telemetry source was operating;
3. the event should have matched the detection logic; and
4. whether the detection fired.

---

## 8. Technical security deliverables

The Phase II workstream will produce, at minimum:

| ID | Deliverable | Repository location | Status at addendum |
|---|---|---|---|
| SEC-DEL-01 | Technical AI & Cybersecurity Engineering Scope Addendum | `01-project-charter-and-context/02-objectives-and-scope/` | This document |
| SEC-DEL-02 | Technical AI Security Reference & Applicability Baseline | `02-regulatory-and-framework-research/` | Required |
| SEC-DEL-03 | PondGPT Technical Security Architecture | `10-system-model-and-technical-documentation/02-architecture-and-data-flows/AI-006-pondgpt/` | Required |
| SEC-DEL-04 | PondGPT Threat Model | `10-system-model-and-technical-documentation/03-threat-models/AI-006-pondgpt/` | Required |
| SEC-DEL-05 | PondGPT Technical Security Validation Plan | `11-assurance-testing-and-evaluation/06-technical-security-validation/AI-006-pondgpt/` | Next |
| SEC-DEL-06 | PG-03 Prompt Injection & RAG Poisoning Test Suite | Same technical-validation branch | Next |
| SEC-DEL-07 | Raw/reproducible technical evidence | `80-operating-evidence/AI-006-pondgpt/` | Extend existing |
| SEC-DEL-08 | Remediation & retest record | `80-operating-evidence/AI-006-pondgpt/` | After findings |
| SEC-DEL-09 | Detection-engineering package | technical-validation + operating evidence | Planned |
| SEC-DEL-10 | Security conclusion / residual-risk input | risk/control artifacts by normal change control | After evidence review |

---

## 9. Repository and branch convention

The existing Duckworks repository structure remains authoritative.

Recommended working branch for the first technical-security increment:

`feature/pondgpt-technical-security-phase2`

No new top-level technical-security folder is required. Technical design, assurance/testing and operating evidence remain separated using the repository's existing control architecture:

- `10-system-model-and-technical-documentation/` — what the system is and how security is designed;
- `11-assurance-testing-and-evaluation/` — how controls are challenged and evaluated;
- `80-operating-evidence/` — what was actually executed and evidenced.

---

## 10. Roles and segregation of duties

| Role | Phase II responsibility |
|---|---|
| Oliver Duckett — Head of IT & Cloud | PondGPT application/platform ownership; technical control implementation |
| Dr. Ada Duckfield — Head of Data & AI | AI/ML implementation, model/RAG technical evidence, secure-output engineering |
| Cassandra Duckley — CISO | Security threat-model challenge, test authorization, PG-03/PG-05 ownership, security acceptance criteria |
| Eleanor Duckford — AI Governance Lead | Traceability to inventory, risk, controls, decisions and evidence |
| Percival Duckworth — Director Procurement & Vendor Assurance | Supplier/model-service security evidence and change governance |
| Delia Duckham — Data Protection Officer | Privacy/security consultation where personal data processing is implicated |
| Amelia Duckett — General Counsel | Legal applicability and contractual interpretation |
| Penelope Duckins — Head of Internal Audit | Independent assurance only; does not design or operate the technical controls |

A person who builds a security control may execute engineering tests, but a claim of **independent validation** requires sufficient reviewer independence.

---

## 11. Acceptance criteria

Phase II's first PondGPT increment is acceptable for portfolio publication when:

1. the architecture distinguishes verified portfolio facts from Phase II design assumptions;
2. all security-relevant data flows and trust boundaries are identified;
3. the threat model includes conventional cyber and AI-specific attack paths;
4. every P0/P1 threat has a testable security requirement or an explicit accepted gap;
5. existing risk IDs and control IDs are reused where applicable;
6. new security requirements are not falsely represented as already implemented controls;
7. PG-03 has a reproducible test suite and result record;
8. at least one intentionally vulnerable condition is demonstrated, remediated and retested;
9. telemetry demonstrates whether relevant test events were detected;
10. raw evidence is traceable to stable evidence identifiers;
11. synthetic evidence is not represented as production effectiveness;
12. external services are not attacked; and
13. limitations and unresolved risks remain visible.

---

## 12. Relationship to laws, standards and guidance

This scope addendum creates **internal Duckworks project authorization and practice** only.

It does not itself create a legal obligation.

Technical work may be informed by binding law, standards, frameworks and recognized technical references. Applicability is maintained in the accompanying **Technical AI Security Reference & Applicability Baseline** and must preserve the following distinctions:

1. **Mandatory legal requirements** — only where the relevant legal scope and conditions are met.
2. **Standards/framework guidance** — requirements or guidance adopted voluntarily or contractually; not automatic legal compliance.
3. **Recommended organizational/technical practices** — defensible engineering choices based on threat and risk.
4. **Project assumptions** — fictional technical decisions used to make the portfolio executable.

---

## 13. Change and reassessment triggers

The PondGPT architecture and threat model must be reassessed when there is a material change to:

- intended purpose;
- user population;
- data classification;
- identity provider;
- authorization model;
- RAG source;
- ingestion method;
- vector store;
- embedding model;
- foundation model/provider;
- model gateway;
- tool/agent capability;
- service account;
- external integration;
- network egress;
- logging/monitoring architecture;
- production/pilot boundary;
- supplier terms;
- known critical vulnerability; or
- relevant legal/security requirement.

---

## 14. Portfolio limitation

Duckworks, Project W.I.N.G., PondGPT, LanternMind Enterprise AI Ltd., all personnel, systems, datasets, incidents, configurations, attack results and evidence created under this addendum are fictional or synthetic unless a source is explicitly identified as public.

This work demonstrates security-engineering methodology and evidence design. It does not represent an assessment of a real employer, vendor or production system.
