# AI-001 DuckDesign AI — Technical Security Reference & Applicability Addendum

**Project:** Project W.I.N.G. — Phase II Technical AI Security Engineering & Adversarial Validation  
**Document ID:** DW-AI001-SEC-REF-01  
**Version:** 1.0  
**Research / review date:** 15 September 2026  
**System:** AI-001 — DuckDesign AI  
**Status:** System-specific applicability baseline — not legal advice  
**Owner:** Eleanor Duckford — AI Governance Lead  
**Security reviewer:** Cassandra Duckley — Chief Information Security Officer  
**Product-safety reviewer:** Quentin Duckwell — Director Product Safety & Quality  
**Legal reviewer:** Amelia Duckett — General Counsel  
**Current governance gate:** **Restricted Pilot only**

> This addendum supplements `Duckworks_Technical_AI_Security_Reference_and_Applicability_Baseline_v1.0.md`. It separates mandatory legal requirements, standards/framework guidance, recognized technical-security references, recommended organizational practices, and project assumptions. It does not establish legal compliance, product conformity, certification, or production security.

## 1. DuckDesign facts used by this addendum

Current Duckworks records establish that DuckDesign:

- is `AI-001`;
- supports Product & Engineering;
- assists with design generation, component optimization, material selection, CAD workflows, simulation support and comparison of alternative mechanical-arm designs;
- uses a Duckworks-developed engineering workflow integrated with the fictional AetherForge AI GmbH hosted foundation-model service;
- may process confidential engineering IP, CAD files, specifications, material/simulation data and supplier-component information;
- requires competent engineer review before prototyping or production;
- cannot authorize a production design;
- is a **Restricted Pilot** with internal impact indicator **High**; and
- remains subject to unresolved control-validation actions.

Existing risks:

- `AI-001-R01 — Safety & physical harm`;
- `AI-001-R02 — Privacy & data governance / engineering confidentiality`; and
- `AI-001-R03 — Reliability & robustness`.

Existing controls:

- `DD-01 — Competent Engineer Approval`;
- `DD-02 — Independent Safety Validation Gate`;
- `DD-03 — Engineering Benchmark & Regression Suite`;
- `DD-04 — Engineering Data Boundary & DLP`; and
- `DD-05 — Design/Model Version Traceability`.

Relevant assumptions include `ASM-005`, `ASM-007`, `ASM-012`, `ASM-013`, `ASM-020` and `ASM-025`.

## 2. Mandatory legal requirements — applicability-dependent

### 2.1 EU Artificial Intelligence Act — Regulation (EU) 2024/1689, current consolidated text

**Official consolidated source:** https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng

DuckDesign is **not classified as a high-risk AI system by this portfolio**.

Under the current Article 6 framework, a product/safety-component route to high-risk status depends on the intended safety role and the associated Union harmonisation legislation/conformity-assessment conditions. DuckDesign's current documented purpose is internal engineering decision support with mandatory engineer review; it is not established as a product safety component or as an AI system controlling machinery.

**Reassessment trigger:** if DuckDesign becomes embedded in a Duckworks product, performs a safety function, directly controls mechanical movement, or otherwise moves from advisory design support to a product/safety-component role, legal classification must be reassessed before relying on this baseline.

### 2.2 Machinery Regulation — Regulation (EU) 2023/1230

**Official consolidated source:** https://eur-lex.europa.eu/eli/reg/2023/1230/en

The Regulation generally applies from **20 January 2027**, with specified provisions applying earlier.

Duckworks' fictional mechanical/robotic arms may fall within machinery legislation depending on actual product facts. DuckDesign is not automatically regulated as machinery merely because it assists engineers. However, AI-generated designs, software, parameters or safety-related functions incorporated into a covered product can affect the manufacturer's technical documentation, risk assessment, validation and conformity obligations.

The current 2026 legal framework also contains a sectoral interaction for AI systems that are high-risk because they are safety components in machinery. This does not make DuckDesign high-risk by default.

### 2.3 Cyber Resilience Act — Regulation (EU) 2024/2847

**Official source:** https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng

CRA applicability is **not established for DuckDesign itself**.

If AI-generated software or software components are incorporated into a Duckworks product with digital elements, and Duckworks holds a covered economic-operator role, the product-specific CRA assessment may become relevant. An internal design assistant is not automatically a product with digital elements.

### 2.4 Trade Secrets Directive — Directive (EU) 2016/943

**Official source:** https://eur-lex.europa.eu/eli/dir/2016/943/oj/eng

DuckDesign processes information that Duckworks intends to treat as confidential engineering IP.

The Directive defines a trade secret using conditions that include secrecy, commercial value because it is secret, and **reasonable steps under the circumstances to keep it secret**. Actual protection operates through Member State law implementing the Directive.

DuckDesign data-boundary, DLP, access, provider-contract and logging controls may help demonstrate reasonable protective measures where the information meets the legal definition. This Directive is not a prescriptive cybersecurity-control standard and the portfolio does not determine trade-secret status for any particular artifact.

### 2.5 GDPR — Regulation (EU) 2016/679

GDPR is not assumed to be a primary DuckDesign legal driver because the documented data set is engineering-focused.

It becomes relevant where prompts, logs, supplier records or engineering workflows contain personal data. In those cases, applicable controller/processor, minimization, security, retention and breach requirements must be assessed.

### 2.6 NIS2 — Directive (EU) 2022/2555

NIS2 remains an organization-level, national-implementation scope question.

If Duckworks is in scope, secure development, supply-chain security, vulnerability handling, access control and effectiveness testing around DuckDesign may contribute to the entity's cybersecurity risk-management measures.

## 3. Standards and formal frameworks

These are not legal-compliance conclusions.

### ISO/IEC 27001:2022

Use for information-security risk, supplier security, access control, secure development, configuration/change control, logging, incident management, vulnerability handling and protection of engineering information.

Exact mappings require an authorized copy.

### ISO/IEC 42001:2023

Use for AI lifecycle governance, roles, risk treatment, controlled change, monitoring, supplier integration, records and continual improvement.

No conformity or certification claim is made.

### NIST CSF 2.0

Relevant outcomes span Govern, Identify, Protect, Detect, Respond and Recover, particularly for source repositories, build systems, dependencies, model/provider changes, engineering data and incident rollback.

### NIST AI RMF 1.0 / NIST AI 600-1

Use for generative-AI risk framing, measurement, content reliability, human-AI interaction, monitoring and governance decisions.

### NIST SP 800-218 / SP 800-218A

**Official SP 800-218A source:** https://csrc.nist.gov/pubs/sp/800/218/a/final

Use for secure software development, dependency/artifact integrity, model/application lifecycle security, provenance, vulnerability handling, testing and release controls.

## 4. Official / recognized technical-security guidance

### NCSC / international partners — Guidelines for Secure AI System Development

**Official source:** https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development

Especially relevant to DuckDesign because the guidance explicitly addresses AI supply chains, third-party models/APIs, software components, asset tracking, version control and restoration to known-good state.

### SLSA 1.2

**Official specification:** https://slsa.dev/spec/v1.2/

SLSA is an industry supply-chain security specification, not law. DuckDesign uses its provenance/build-integrity concepts to make generated-code and build-artifact claims traceable and testable.

### OpenSSF secure software development guidance

**Official resources:** https://openssf.org/resources/guides/

Relevant to source-code management, dependency evaluation, secure development, build protection and software-supply-chain transparency.

### OWASP GenAI Security

Relevant DuckDesign themes include:

- supply-chain vulnerabilities;
- improper output handling;
- excessive agency;
- sensitive-information disclosure;
- data/model poisoning;
- system-prompt leakage; and
- insecure downstream handling of generated artifacts.

These are technical references, not mandatory legal requirements.

### MITRE ATLAS

Use for AI-enabled attack paths, prompt/data manipulation, supply-chain compromise, model/service abuse and detection hypotheses.

ATLAS is a living resource; technique identifiers should be rechecked when the executable validation plan is finalized.

## 5. DuckDesign applicability matrix

| Source | Category | Current treatment | Technical use | Boundary |
|---|---|---|---|---|
| EU AI Act | Binding law | High-risk status not established | Classification triggers, lifecycle/security reference | Reassess if safety-component/product role changes |
| Machinery Regulation | Binding regulation | Product applicability depends on actual Duckworks products; general application from 20 Jan 2027 | Design/safety validation and product-conformity context | DuckDesign is not automatically machinery |
| CRA | Binding regulation | Not established for internal assistant | Generated-software/product supply-chain context | Assess covered product/economic-operator facts |
| Trade Secrets Directive | EU directive / national implementation | Relevant where engineering IP meets trade-secret definition | Reasonable protective measures around CAD/specs/IP | Does not prescribe exact cybersecurity controls |
| GDPR | Binding regulation | Conditional | Personal-data minimization/security where present | Engineering IP is not automatically personal data |
| NIS2 | National-law dependent | Unresolved | Secure development/supply chain/effectiveness testing | Entity/sector scope required |
| ISO/IEC 27001 | Standard | Applicable as management/control reference | ISMS integration | Not certification proof |
| ISO/IEC 42001 | Standard | Applicable as AIMS reference | AI lifecycle/evidence/change | Not conformity proof |
| NIST SSDF / 218A | Guidance | Applicable | Generated-code/build/dependency security | Not law |
| NCSC secure-AI guidance | Government guidance | Applicable | Supply chain, asset/version security, known-good restoration | Not law |
| SLSA / OpenSSF | Industry guidance | Applicable | Provenance, builds, dependencies, SCM | Not law |
| OWASP / MITRE ATLAS | Technical references | Applicable | Threat/test coverage | Not law |

## 6. Recommended Duckworks organizational practices

The following are project design choices, not external requirements unless separately identified:

- treat generated code, dependency names and tool commands as untrusted until validated;
- prohibit direct AI-to-production-design or AI-to-product-release authority;
- require exact artifact/version/hash binding for engineer approval;
- execute generated scripts/macros only in an isolated sandbox before approval;
- deny arbitrary shell/network/file-system privilege to the model;
- use approved dependency registries/proxies with lock/hash verification;
- generate and retain software-component provenance/SBOM where generated code enters a build;
- keep confidential CAD/specification content behind explicit data-boundary policy;
- minimize provider prompts/context and prohibit secrets/credentials;
- pin provider/model/system-prompt/configuration versions;
- require safety/engineering validation independently of model confidence;
- record engineer rejection/override and validation failures;
- require regression after material model/provider/tool/dependency/prompt/data changes; and
- support rollback to a known-good design/build state.

## 7. Governance conclusion

This addendum authorizes no production use and upgrades no control.

It establishes the legal/framework/technical reference boundary for DuckDesign's Phase II architecture and threat model.

The lifecycle decision remains:

> **RESTRICTED PILOT ONLY**

The next evidence step is a separate DuckDesign technical-security validation plan after architecture and threat-model approval.
