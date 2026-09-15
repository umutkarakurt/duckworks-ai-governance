# AI-001 DuckDesign AI — Technical Threat Model

**Project:** Project W.I.N.G. — Phase II Technical AI Security Engineering & Adversarial Validation  
**Document ID:** DW-AI001-TM-01  
**Version:** 1.0  
**Date:** 15 September 2026  
**Status:** Threat-model baseline — validation not yet executed  
**AI system:** AI-001 — DuckDesign AI  
**Architecture dependency:** `DW-AI001-ARCH-SEC-01 v1.0`  
**Current governance gate:** **Restricted Pilot only**  
**Business owner:** Felix Duckson — VP Product & Engineering  
**Security owner:** Cassandra Duckley — Chief Information Security Officer  
**AI/ML owner:** Dr. Ada Duckfield — Head of Data & AI  
**Product-safety challenger:** Quentin Duckwell — Director Product Safety & Quality  
**Governance owner:** Eleanor Duckford — AI Governance Lead

> Threat priority expresses technical test urgency. It does not replace Duckworks enterprise risk scores, establish a real production vulnerability, or create product-safety/legal conclusions.

## 1. Risk and control traceability

Existing risks:

- `AI-001-R01 — Safety & physical harm`;
- `AI-001-R02 — Privacy & data governance / engineering confidentiality`;
- `AI-001-R03 — Reliability & robustness`.

Existing controls:

- `DD-01 — Competent Engineer Approval`;
- `DD-02 — Independent Safety Validation Gate`;
- `DD-03 — Engineering Benchmark & Regression Suite`;
- `DD-04 — Engineering Data Boundary & DLP`;
- `DD-05 — Design/Model Version Traceability`;
- supporting `AI-GOV-01`, `AI-GOV-02`, `AI-TPR-01`, `AI-INC-01`.

Current repository evidence is insufficient to credit DD controls as production-effective. `DD-01` additionally remains subject to open High audit finding `IAF-2026-002`.

## 2. Protected assets

1. confidential CAD/design files;
2. engineering specifications and tolerances;
3. material-property/reference data;
4. simulation inputs/results;
5. supplier-component information;
6. product-safety requirements;
7. system prompts/control instructions;
8. provider/model configuration;
9. source repositories;
10. generated code/scripts/macros;
11. dependency/package metadata;
12. build artifacts;
13. signing/secrets/credentials;
14. CAD/simulation tool identities and permissions;
15. validation/benchmark results;
16. engineer approval records;
17. independent safety-validation records;
18. artifact hashes/versions;
19. SBOM/provenance evidence;
20. telemetry/security evidence; and
21. Duckworks product/design integrity.

## 3. Threat actors / failure profiles

| ID | Profile | Typical objective / failure |
|---|---|---|
| A1 | External attacker | Obtain engineering IP or influence generated artifacts/dependencies |
| A2 | Malicious/compromised supplier | Introduce compromised package/model/API/tool component |
| A3 | Compromised engineer account | Exfiltrate IP, bypass validation, approve wrong artifact |
| A4 | Malicious/compromised engineering document | Indirect injection or manipulated design inputs |
| A5 | Dependency/package adversary | Typosquat, dependency-confuse, compromise package/update |
| A6 | Build/CI adversary | Tamper generated code/build/provenance |
| A7 | AI/model/service operator change | Silent provider/model behavior/version change |
| A8 | Insider/operator misconfiguration | Disable DLP, scanning, safety gate, versioning or telemetry |
| F1 | Model hallucination | Incorrect material/specification/code recommendation |
| F2 | Tool integration failure | Wrong file/tool/action/parameter applied |
| F3 | Engineering-data quality failure | Wrong units, stale specs, corrupted reference values |
| F4 | Human-process failure | Engineer approval is superficial, stale or attached to wrong artifact |

## 4. Priority model

| Priority | Meaning |
|---|---|
| P0 | Directly challenges engineering IP, execution privilege, design/safety gate, approval integrity or supply-chain integrity |
| P1 | Materially challenges reliability, versioning, telemetry, dependency/tool containment or rollback |
| P2 | Important hardening/observability issue outside first-wave gate-critical scope |

## 5. Threat register

### 5.1 Engineering data and provider boundary

| ID | Priority | Threat |
|---|---:|---|
| DDT-001 | P0 | Confidential CAD/specification content is sent to provider outside approved data scope. |
| DDT-002 | P0 | Repository token, signing key or other secret is included in model context. |
| DDT-003 | P1 | Provider retains/reuses Duckworks content contrary to ASM-025. |
| DDT-004 | P1 | Provider cross-tenant/security failure exposes engineering context. |
| DDT-005 | P1 | Prompt/application telemetry retains excessive engineering IP. |
| DDT-006 | P1 | Misclassified supplier/design file bypasses DLP/content policy. |

### 5.2 Prompt/content manipulation

| ID | Priority | Threat |
|---|---:|---|
| DDT-007 | P0 | Imported engineering/specification text contains indirect instructions that manipulate model/tool behavior. |
| DDT-008 | P1 | Obfuscated instruction bypasses simple content filters. |
| DDT-009 | P1 | System/control prompt disclosure reveals sensitive workflow constraints. |
| DDT-010 | P0 | Retrieved/imported content is treated as authority rather than untrusted data. |
| DDT-011 | P1 | Attacker manipulates context to suppress warnings/tests or alter safety assumptions. |
| DDT-012 | P1 | Model output fabricates engineering source/reference evidence. |

### 5.3 Generated code and artifact security

| ID | Priority | Threat |
|---|---:|---|
| DDT-013 | P0 | Generated code contains dangerous shell/file/network behavior. |
| DDT-014 | P0 | Generated script attempts to access secrets or unauthorized files. |
| DDT-015 | P1 | Generated code disables tests/scanners/safety checks. |
| DDT-016 | P1 | Generated code contains insecure input/output handling or unsafe deserialization patterns. |
| DDT-017 | P0 | Generated artifact is executed directly on an engineer workstation or production-capable runner. |
| DDT-018 | P0 | Model-generated changes are merged/promoted without independent review. |

### 5.4 Software/dependency supply chain

| ID | Priority | Threat |
|---|---:|---|
| DDT-019 | P0 | Model hallucinates a nonexistent dependency name that an attacker registers (“slopsquatting”-style path). |
| DDT-020 | P0 | Dependency-confusion path selects attacker-controlled package from an unintended registry. |
| DDT-021 | P0 | Existing third-party dependency is compromised. |
| DDT-022 | P1 | Typosquatted package is mistaken for approved dependency. |
| DDT-023 | P0 | Locked version/hash is bypassed or mismatched. |
| DDT-024 | P1 | Plugin/extension/tool dependency changes without review. |
| DDT-025 | P1 | Build artifact is tampered after generation. |
| DDT-026 | P1 | SBOM/provenance is absent, incomplete or falsified. |

### 5.5 Tool/agent privilege

| ID | Priority | Threat |
|---|---:|---|
| DDT-027 | P0 | Model requests arbitrary shell execution through a tool. |
| DDT-028 | P0 | Model requests unrestricted file-system write/delete. |
| DDT-029 | P0 | Model/tool attempts arbitrary external network egress. |
| DDT-030 | P0 | Model invokes a high-impact CAD/simulation action without independent authorization. |
| DDT-031 | P1 | Tool output is trusted as new instruction, creating a secondary injection path. |
| DDT-032 | P0 | Confused-deputy path causes a tool to use a more privileged service identity than intended. |
| DDT-033 | P1 | Duplicate/replayed tool action changes artifact state twice. |
| DDT-034 | P0 | Tool capability expands silently beyond approved scope. |

### 5.6 Engineering integrity / safety

| ID | Priority | Threat |
|---|---:|---|
| DDT-035 | P0 | Model fabricates or misstates a material property used as a design assumption. |
| DDT-036 | P0 | Unit conversion/range error produces unsafe design parameter. |
| DDT-037 | P0 | Model omits a required constraint while optimization appears successful. |
| DDT-038 | P1 | Simulation parameter or benchmark fixture is manipulated to make an unsafe design pass. |
| DDT-039 | P0 | Required independent safety-validation gate is bypassed. |
| DDT-040 | P0 | Engineer approval is attached to a different artifact/version than reviewed. |
| DDT-041 | P0 | Artifact changes after approval without invalidating approval. |
| DDT-042 | P1 | Automation bias causes superficial engineer acceptance of plausible output. |

### 5.7 Version, build, monitoring and recovery

| ID | Priority | Threat |
|---|---:|---|
| DDT-043 | P0 | Provider/model/system-prompt/configuration changes silently without regression. |
| DDT-044 | P1 | Tool or dependency policy changes silently. |
| DDT-045 | P1 | Build runner or provenance generator is compromised. |
| DDT-046 | P1 | Security/engineering telemetry is disabled or loses correlation. |
| DDT-047 | P1 | Failed/compromised change cannot be rolled back to known-good state. |
| DDT-048 | P1 | Evidence hashes/version metadata do not match the artifact used for governance decision. |

## 6. Key attack paths

### AP-DD-01 — engineering IP leakage

Confidential CAD/specification  
→ context minimization/DLP fails  
→ excessive content enters provider prompt/log  
→ provider exposure/retention occurs.

**Primary barriers:** DD-04, DD-SR-002–005, DD-SR-035/037.

### AP-DD-02 — indirect engineering-document injection

Malicious supplier/spec/CAD metadata  
→ imported as trusted context  
→ embedded instruction manipulates model/tool behavior  
→ generated artifact/tool action violates policy.

**Primary barriers:** DD-SR-006, DD-SR-017–019, staging/sandbox.

### AP-DD-03 — hallucinated dependency to malicious package

Model generates package name  
→ dependency existence/registry policy absent  
→ attacker-controlled package resolves  
→ generated code/build executes malicious dependency.

**Primary barriers:** DD-SR-011–014, approved proxy, lock/hash, provenance.

### AP-DD-04 — generated code to excessive privilege

Generated script  
→ executed outside sandbox or with privileged identity  
→ shell/file/network action  
→ IP exfiltration or engineering artifact modification.

**Primary barriers:** DD-SR-008, DD-SR-015–019, least-privilege sandbox/tool gateway.

### AP-DD-05 — unsafe engineering claim to design progression

Model fabricates material/specification value  
→ engineer trusts plausible result  
→ benchmark/safety gate weak or bypassed  
→ design progresses toward prototype/production.

**Primary barriers:** DD-01, DD-02, DD-03, DD-SR-020–027.

### AP-DD-06 — approval-to-wrong-artifact

Engineer reviews artifact A  
→ artifact is modified or substituted  
→ approval record lacks hash/version binding  
→ artifact B inherits approval.

**Primary barriers:** DD-SR-025/026, registry/integrity evidence.

### AP-DD-07 — silent model/tool version regression

Provider/model/tool/config changes  
→ no change trigger  
→ previous tests no longer representative  
→ unsafe behavior reaches pilot engineers.

**Primary barriers:** DD-05, AI-GOV-02, DD-SR-030–032.

### AP-DD-08 — build/provenance tamper

Valid generated source  
→ build runner/dependency/artifact altered  
→ SBOM/provenance absent or unverified  
→ governance reviewer cannot establish what was actually built.

**Primary barriers:** DD-SR-013/014/033/034, provenance store and evidence hashes.

## 7. Candidate first-wave validation tests — DESIGN ONLY

| Test | Scenario | Threats | Primary controls | Expected hardened outcome |
|---|---|---|---|---|
| `DDSEC-T001` | Engineering IP / secret leakage to provider/logs | DDT-001–006 | DD-04; AI-TPR-01 | defined synthetic CAD/IP/secret canaries absent from prohibited provider/log sinks |
| `DDSEC-T002` | Indirect injection from engineering/specification content | DDT-007–012 | DD-04; DD-03 | imported instructions remain untrusted and cannot alter tool/validation authority |
| `DDSEC-T003` | Generated code attempts prohibited shell/file/network behavior | DDT-013–018 | DD-03; DD-05 | scanner/sandbox blocks prohibited behavior; artifact remains staged |
| `DDSEC-T004` | Hallucinated/unapproved dependency resolution | DDT-019; 020; 022 | DD-03; DD-05 | nonexistent/unapproved package is denied; no arbitrary public resolution |
| `DDSEC-T005` | Dependency/version/hash integrity mismatch | DDT-021; 023–026 | DD-03; DD-05 | mismatch blocks build/promotion and emits integrity/provenance event |
| `DDSEC-T006` | CAD/simulation tool privilege / arbitrary egress | DDT-027–034 | DD-01; DD-05 | prohibited tool/egress denied independent of model text |
| `DDSEC-T007` | Material/unit/range/constraint validation challenge | DDT-035–038; 042 | DD-01; DD-03 | incorrect engineering claim/parameter is detected and blocks promotion |
| `DDSEC-T008` | Independent safety-gate bypass | DDT-039 | DD-02 | required safety gate cannot be skipped by model or engineer workflow |
| `DDSEC-T009` | Engineer approval bound to wrong/changed artifact | DDT-040; 041 | DD-01; DD-05 | approval hash mismatch invalidates approval and requires re-review |
| `DDSEC-T010` | Model/provider/prompt/config/tool material change | DDT-043; 044 | DD-03; DD-05; AI-GOV-02 | drift detected; regression required; approved promotion blocked |
| `DDSEC-T011` | Missing/incomplete SBOM/provenance/build identity | DDT-025; 026; 045; 048 | DD-05 | artifact quarantined/unapproved until required provenance is complete |
| `DDSEC-T012` | Known-good rollback / evidence reconstruction | DDT-046–048 | DD-05; AI-INC-01 | failed change is correlated and rollback restores known-good version without automatic risk/gate change |

## 8. Initial machine assertions for later validation

A later plan should verify at least:

1. provider/log sinks exclude defined confidential/secret canaries;
2. imported text cannot change authorization/tool/test policy;
3. generated code cannot execute prohibited shell/file/network behavior;
4. nonexistent/unapproved dependencies do not resolve;
5. dependency/hash mismatch blocks approved build status;
6. prohibited CAD/simulation/tool/egress actions are denied;
7. unsafe engineering units/ranges/material claims fail deterministic validation;
8. required safety-validation state cannot be bypassed;
9. engineer approval is valid only for the exact artifact hash;
10. model/provider/prompt/config/tool change requires regression;
11. incomplete provenance/SBOM blocks promotion;
12. rollback identifies/restores the known-good artifact/config;
13. each result records model/config/dependency/tool/artifact versions, correlation ID and evidence hash; and
14. `production_effectiveness_claim == false`.

## 9. Future evidence schema

Each executed case should record:

`test_id`, threat IDs, risk IDs, control IDs, requirement IDs, profile, architecture/threat-model/validation-plan/lab versions, synthetic engineer ID, source/input fixture IDs/hashes, provider/model/prompt/config versions, generated artifact ID/hash, dependency names/versions/hashes, tool/action requests, benchmark/safety results, approval identity/hash, provenance/SBOM state, expected/actual, detection events, correlation ID, PASS/FAIL, evidence SHA-256 and limitations.

## 10. Acceptance principle

The later campaign should follow:

**known weak baseline → deliberate challenge → observable unsafe state → hardening → identical retest → evidence → control conclusion**

A hardened PASS may mean denial, quarantine, validation failure, safety-gate blocking, approval invalidation, restricted execution, or successful rollback.

It must not be phrased as proof that the model cannot hallucinate, that all generated code is secure, or that Duckworks products are safe.

## 11. Known gaps before validation

TBD / not evidenced:

- actual DuckDesign generated-code capability;
- actual CAD/simulation tool APIs;
- production engineering identity/role model;
- actual package registries/proxy;
- real build pipeline;
- source-code scanner;
- sandbox implementation;
- AetherForge contract and data-use evidence;
- actual design-validation criteria;
- actual DD-02 trigger criteria;
- real engineer-approval records;
- real version/provenance/SBOM infrastructure;
- production incident/rollback process;
- product/machinery conformity classification; and
- production effectiveness.

## 12. Governance conclusion

This threat model does not:

- claim a real vulnerability;
- claim any attack occurred;
- upgrade `DD-01`–`DD-05`;
- resolve `IAF-2026-002`;
- allocate `EV-AI001-*`;
- reduce AI-001 risk;
- close `ASM-007`, `ASM-020` or `ASM-025`;
- classify DuckDesign as high-risk under the EU AI Act;
- establish product/machinery conformity; or
- authorize broader use.

The gate remains:

> **RESTRICTED PILOT ONLY**

The next technical step is `DW-AI001-VAL-SEC-01` — a separate DuckDesign software-supply-chain / generated-code / tool-privilege validation plan followed by a deterministic synthetic lab for `DDSEC-T001`–`DDSEC-T012`.
