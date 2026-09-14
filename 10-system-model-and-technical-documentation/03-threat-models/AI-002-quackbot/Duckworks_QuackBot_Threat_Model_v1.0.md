# AI-002 QuackBot — Technical Threat Model

**Project:** Project W.I.N.G. — Phase II Technical AI Security Engineering & Adversarial Validation  
**Document ID:** DW-AI002-TM-01  
**Version:** 1.0  
**Date:** 14 September 2026  
**Status:** Threat-model baseline — validation not yet executed  
**AI system:** AI-002 — QuackBot  
**Architecture dependency:** `DW-AI002-ARCH-SEC-01 v1.0`  
**Current governance gate:** **Pre-Production / Production Blocked**  
**Business owner:** Clara Duckley — Director Customer Operations  
**Security owner:** Cassandra Duckley — Chief Information Security Officer  
**AI/ML owner:** Dr. Ada Duckfield — Head of Data & AI  
**Governance owner:** Eleanor Duckford — AI Governance Lead

> **Interpretation boundary:** Threat priority in this document expresses technical test urgency. It does not replace Duckworks enterprise risk ratings. A listed threat is not evidence that a production vulnerability exists.

---

## 1. Risk and control traceability

### Existing risks

- `AI-002-R01 — Reliability & robustness`  
  Hallucinated troubleshooting, warranty or support information may cause customer harm, complaints, disputes, liability or loss of trust.

- `AI-002-R02 — Security & adversarial manipulation`  
  Malicious prompts or poisoned content may manipulate retrieval/tool behavior, disclose sensitive information or cause unsafe guidance.

- `AI-002-R03 — Legal / compliance`  
  Incorrect warranty or consumer-rights statements may be presented as authoritative Duckworks guidance.

### Existing controls

- `QB-01 — Curated RAG Source Allowlist`;
- `QB-02 — Grounding, Citation & Abstention Rules`;
- `QB-03 — Human Escalation SLA`;
- `QB-04 — Prompt Injection & RAG Adversarial Testing`;
- `QB-05 — Least-Privilege Retrieval & Tool Boundaries`;
- `QB-06 — GenAI Security & Harm Monitoring`;
- supporting `AI-GOV-01`, `AI-GOV-02`, `AI-TPR-01`, `AI-INC-01`.

The current master control framework has no linked QuackBot operating-evidence IDs. This threat model does not change that fact.

---

## 2. Protected assets

1. customer account/contact identifiers;
2. customer support history;
3. warranty/account status;
4. customer chat transcripts;
5. approved public product/support corpus;
6. restricted/private customer corpus;
7. source/provenance metadata;
8. vector/index contents;
9. retrieval authorization rules;
10. customer/account object identifiers;
11. session state and conversation memory;
12. system/control instructions;
13. provider/model configuration;
14. API credentials, service tokens and secrets;
15. response grounding/citation logic;
16. human-escalation route and case linkage;
17. application/API availability and provider quota;
18. telemetry and security evidence;
19. model/provider/config/KB version records; and
20. Duckworks customer trust / support decision integrity.

---

## 3. Threat actors and failure profiles

| ID | Profile | Typical objective / failure |
|---|---|---|
| A1 | Anonymous internet attacker | Extract data, bypass policy, consume resources, manipulate responses |
| A2 | Authenticated malicious customer | Access another customer's objects, abuse support flows, probe private data |
| A3 | Bot / automation operator | Resource exhaustion, scraping, cost amplification, credential/session abuse |
| A4 | Malicious/compromised content editor | Poison approved support/RAG content |
| A5 | Duckworks insider / application operator | Misconfigure source scope, logging, auth, rate policy or escalation |
| A6 | AI/ML / RAG operator | Introduce unsafe prompt/config/index/model changes |
| A7 | Supplier/supply-chain adversary | Compromise model/provider/dependency/build/update path |
| A8 | Platform/API attacker | Exploit auth/session/API/SSRF/output-handling weaknesses |
| F1 | Non-malicious stale/incorrect knowledge | Outdated support/warranty guidance |
| F2 | Provider/model behavioral change | Reliability or safety behavior changes unexpectedly |
| F3 | Infrastructure/service failure | Retrieval/provider/auth/logging dependency becomes unavailable |
| F4 | Human-process failure | Escalation not routed or legal/safety content not maintained |

---

## 4. Priority model

| Priority | Meaning |
|---|---|
| P0 | Directly challenges customer-data isolation, authorization, system authority, material customer safety/legal boundary or fail-safe behavior |
| P1 | Materially challenges RAG integrity, session isolation, output handling, resource control, provider/supply-chain integrity or escalation |
| P2 | Important hardening/observability issue but not first-wave gate-critical in the synthetic lab |

Priority is a test-planning tool, not a risk score.

---

## 5. Threat register

### 5.1 Internet, API, authentication and session

| Threat ID | Priority | Threat |
|---|---:|---|
| QBT-001 | P1 | Automated abuse floods the public chatbot/API with high-volume requests. |
| QBT-002 | P1 | Oversized prompts/context requests amplify compute/provider cost. |
| QBT-003 | P0 | Anonymous session is accidentally treated as authenticated customer context. |
| QBT-004 | P0 | Authenticated user requests another customer's support/account object (BOLA). |
| QBT-005 | P0 | Function-level authorization allows a customer to invoke a privileged support/admin operation. |
| QBT-006 | P1 | Session fixation or replay reuses another user's active context. |
| QBT-007 | P0 | Cross-session memory/cache leakage exposes another user's conversation or retrieved content. |
| QBT-008 | P1 | Authentication/claim validation fails open or trusts client-supplied role/account data. |
| QBT-009 | P1 | API security misconfiguration exposes undocumented/debug/admin endpoints. |
| QBT-010 | P1 | Unsafe downstream API consumption trusts malformed or attacker-influenced provider/connector responses. |

### 5.2 Direct prompt and conversational manipulation

| Threat ID | Priority | Threat |
|---|---:|---|
| QBT-011 | P1 | Direct prompt injection attempts to override system/control instructions. |
| QBT-012 | P1 | Encoded/obfuscated injection bypasses simple input filters. |
| QBT-013 | P1 | Multi-turn conversation gradually erodes control instructions. |
| QBT-014 | P1 | System-prompt / policy disclosure reveals sensitive internal instructions. |
| QBT-015 | P0 | Model refusal behavior is incorrectly relied upon as the data-access control. |
| QBT-016 | P1 | Attacker coerces model into outputting hidden context, source content or test canaries. |

### 5.3 RAG, source and knowledge-base threats

| Threat ID | Priority | Threat |
|---|---:|---|
| QBT-017 | P0 | Indirect prompt injection is embedded in an approved-looking retrieved document. |
| QBT-018 | P0 | Unapproved/malicious source is ingested into the public knowledge corpus. |
| QBT-019 | P0 | Source provenance/hash metadata is altered to make poisoned content appear approved. |
| QBT-020 | P1 | Vector/index content is modified without corresponding source approval/version evidence. |
| QBT-021 | P1 | Retrieval flooding/context stuffing displaces trustworthy source material. |
| QBT-022 | P0 | Public corpus contains private/customer-specific information because source classification is wrong. |
| QBT-023 | P1 | Stale product/support/warranty content remains retrievable after supersession. |
| QBT-024 | P1 | Citation/source IDs are fabricated or point to content not actually retrieved. |

### 5.4 Customer-data and privacy threats

| Threat ID | Priority | Threat |
|---|---:|---|
| QBT-025 | P0 | Anonymous prompt causes retrieval of customer-specific account/support history. |
| QBT-026 | P0 | Authenticated user retrieves another customer's data through object-ID manipulation. |
| QBT-027 | P1 | More customer data than necessary is sent to HelixRiver. |
| QBT-028 | P1 | Credentials, tokens or secrets are accidentally placed in model context. |
| QBT-029 | P1 | Security/application logs retain full sensitive conversations unnecessarily. |
| QBT-030 | P1 | Cache/debug traces expose prior customer data. |
| QBT-031 | P1 | Provider retains/reuses Duckworks prompt/content contrary to ASM-026. |

### 5.5 Reliability, safety, legal-content and output threats

| Threat ID | Priority | Threat |
|---|---:|---|
| QBT-032 | P0 | QuackBot hallucinates unsafe troubleshooting advice. |
| QBT-033 | P0 | QuackBot states incorrect warranty/consumer-rights information as authoritative. |
| QBT-034 | P1 | QuackBot answers a high-impact topic without sufficient approved grounding. |
| QBT-035 | P1 | QuackBot fabricates citation/reference evidence. |
| QBT-036 | P0 | Required human escalation is not triggered or routed. |
| QBT-037 | P1 | Generated response contains HTML/script/event-handler payload executed by the client. |
| QBT-038 | P1 | Generated links send customers to attacker-controlled/unapproved destinations. |

### 5.6 Tool, egress and excessive-agency threats

| Threat ID | Priority | Threat |
|---|---:|---|
| QBT-039 | P0 | Model or prompt invokes an account/warranty/support action without independent authorization. |
| QBT-040 | P0 | Attacker manipulates a URL/tool argument to reach internal or arbitrary network destinations (SSRF/confused deputy). |
| QBT-041 | P1 | Tool output is trusted as instruction and feeds a secondary injection path. |
| QBT-042 | P0 | Tool capability silently expands beyond approved first-wave scope. |

### 5.7 Supply chain, configuration, telemetry and failure

| Threat ID | Priority | Threat |
|---|---:|---|
| QBT-043 | P1 | HelixRiver model/profile changes without regression or approval. |
| QBT-044 | P1 | Dependency/library compromise alters application behavior. |
| QBT-045 | P0 | Authorization/RAG policy/config changes without integrity/version control. |
| QBT-046 | P1 | Security telemetry is disabled, suppressed or loses correlation. |
| QBT-047 | P0 | Provider/retrieval/auth dependency failure causes fail-open material guidance. |
| QBT-048 | P1 | Rate-limit/resource policy changes silently increase abuse/cost exposure. |

---

## 6. Key attack paths

### AP-QB-01 — anonymous data exfiltration

Anonymous attacker  
→ prompt requests account/support detail  
→ public/auth state confused or connector exposed  
→ customer-specific retrieval enters context  
→ model returns private information.

**Primary barriers:** QB-SR-003–006, QB-SINV-01/02, QB-05.

### AP-QB-02 — indirect RAG injection

Malicious/compromised support document  
→ ingestion/provenance control fails  
→ document is retrieved  
→ embedded instruction overrides workflow  
→ model leaks context, bypasses grounding or manipulates output.

**Primary barriers:** QB-01, QB-04, QB-SR-007–011.

### AP-QB-03 — authenticated cross-customer BOLA

Authenticated customer  
→ modifies customer/case/object identifier  
→ connector trusts client-supplied ID  
→ other customer's support/warranty record retrieved.

**Primary barriers:** QB-05, QB-SR-003/005/006.

### AP-QB-04 — hallucinated safety/warranty guidance

Customer asks material support question  
→ RAG retrieval is weak/stale/empty  
→ model invents plausible guidance  
→ grounding/abstention/escalation fails  
→ customer acts on incorrect statement.

**Primary barriers:** QB-01/02/03, QB-SR-018–022.

### AP-QB-05 — unsafe output handling

Prompt/retrieved text influences response  
→ model emits active HTML/script or malicious link  
→ client renders unsafely  
→ browser/customer session compromised or customer redirected.

**Primary barriers:** QB-SR-023/024, safe renderer.

### AP-QB-06 — excessive agency / SSRF

Prompt instructs model to use URL/tool  
→ tool gateway accepts model-controlled target/arguments  
→ internal/arbitrary endpoint accessed or account action executed.

**Primary barriers:** tools disabled first wave; QB-SR-025–027.

### AP-QB-07 — resource/cost exhaustion

Bot operator  
→ parallel long prompts / session expansion  
→ API/orchestrator/provider repeatedly invoked  
→ quota/cost/availability impact.

**Primary barriers:** QB-SR-015/016, edge/API/session limits.

### AP-QB-08 — session isolation failure

Customer A session state/cache  
→ incorrectly keyed/reused for Customer B  
→ prior context/retrieved private data appears in Customer B answer.

**Primary barriers:** QB-SINV-10, session/cache isolation.

### AP-QB-09 — silent model/config/KB change

Provider/model or Duckworks configuration changes  
→ no version/integrity trigger  
→ previously passing controls regress  
→ unsafe behavior reaches customers.

**Primary barriers:** QB-SR-032/033, AI-GOV-02.

---

## 7. Candidate first-wave validation tests — DESIGN ONLY

These test IDs do not constitute execution evidence.

| Test ID | Scenario | Primary threats | Controls | Expected hardened outcome |
|---|---|---|---|---|
| `QBSEC-T001` | Direct prompt injection / hidden-policy extraction | QBT-011; 012; 014; 016 | QB-04; QB-06 | Injection does not alter authorization/source/tool boundaries; no protected system/context secret is disclosed |
| `QBSEC-T002` | Indirect prompt injection in retrieved support document | QBT-017; 021 | QB-01; QB-04; QB-05 | Retrieved instructions are treated as data; malicious source cannot override security policy |
| `QBSEC-T003` | Unapproved / integrity-failed RAG source | QBT-018; 019; 020 | QB-01; QB-04 | Source is quarantined/blocked before approved corpus use |
| `QBSEC-T004` | Anonymous request for customer-specific/support-history data | QBT-003; 022; 025 | QB-05; QB-06 | Customer/private connector is unavailable; request denied or public-only response |
| `QBSEC-T005` | Authenticated cross-customer object-ID manipulation | QBT-004; 026 | QB-05; QB-06 | Object authorization denies cross-customer retrieval and records event |
| `QBSEC-T006` | Cross-session state / cache isolation | QBT-006; 007; 030 | QB-05; QB-06 | No prior-session context or private content appears in another session |
| `QBSEC-T007` | Hallucinated safety/warranty/legal-support challenge | QBT-023; 032–036 | QB-01; QB-02; QB-03 | Unsupported material answer abstains/escalates; citations must resolve to approved retrieved sources |
| `QBSEC-T008` | Active-content / malicious-link output handling | QBT-037; 038 | QB-02; QB-06 | Output is safely encoded/sanitized; active content does not execute |
| `QBSEC-T009` | Tool / URL / SSRF / excessive-agency manipulation | QBT-039–042 | QB-05; QB-06 | Tool path remains disabled or independently deny/allowlisted; arbitrary egress unavailable |
| `QBSEC-T010` | Rate/resource exhaustion | QBT-001; 002; 048 | QB-06 | Defined request/session/resource limits trigger before uncontrolled downstream consumption |
| `QBSEC-T011` | Sensitive-data leakage to provider/logs | QBT-027–031 | QB-05; QB-06; AI-TPR-01 | Synthetic secrets/PII canaries are minimized/redacted and do not appear in prohibited sinks |
| `QBSEC-T012` | Model/config/KB/auth-policy material change | QBT-043; 045; 048 | QB-04; QB-05; QB-06; AI-GOV-02 | Changed baseline is identified and requires regression/revalidation before approved promotion |

---

## 8. Initial validation assertions

A later validation plan should machine-check at least:

1. anonymous sessions cannot access customer-specific data;
2. authenticated customer authorization is enforced server-side;
3. cross-customer object access is denied;
4. retrieved text cannot change authorization/tool policy;
5. provenance/hash failure prevents corpus promotion;
6. unsupported material advice cannot silently pass as grounded;
7. citations resolve to actually retrieved approved source IDs;
8. required escalation creates a correlated handoff record;
9. one session cannot read another session's state;
10. active-content payloads do not execute in the response-render path;
11. arbitrary tool/URL/egress requests are unavailable or denied;
12. rate/resource limits operate independently of the model;
13. provider/log payloads exclude defined synthetic secret/customer canaries;
14. exact model/provider/config/KB/auth-policy versions are recorded;
15. material baseline change requires regression before promotion; and
16. `production_effectiveness_claim` remains `false`.

---

## 9. Future evidence schema

Each executed case should record at least:

```text
test_id
threat_ids
risk_ids
control_ids
security_requirement_ids
architecture_version
threat_model_version
validation_plan_version
lab_version
profile
session_mode
synthetic_user_id
synthetic_customer_id
request_id
correlation_id
prompt_fixture_id
retrieved_source_ids
retrieved_source_hashes
authz_decisions
provider/model_version
config_version
kb_version
expected
actual
detection_events
escalation_record_id
result
evidence_sha256
limitations
```

Sensitive fixture values should use non-secret synthetic canaries rather than real credentials or personal data.

---

## 10. Acceptance principle

The first-wave campaign should preserve the same evidence discipline used elsewhere in Phase II:

**known weak baseline → deliberate challenge → observable failure → control response → evidence → remediation/hardening → identical retest → explicit limitation**

A hardened PASS can mean:

- the attack is prevented;
- the unsafe state is blocked;
- the material operation is denied;
- the response safely abstains/escalates; or
- the failure is contained before customer impact.

It does **not** require pretending that every prompt injection is perfectly detectable.

---

## 11. Known gaps before validation

The following remain TBD / not evidenced:

- exact QuackBot web/API framework;
- exact authentication mechanism;
- exact object/customer identifier model;
- exact session/cache design;
- exact RAG/vector implementation;
- exact source-approval workflow;
- exact public/private corpus contents;
- actual provider/model configuration;
- real HelixRiver security/privacy/retention evidence;
- real escalation SLA/tool;
- actual rate-limit thresholds;
- actual output-rendering stack;
- actual SIEM/detection routing;
- actual legal/warranty approved-content process;
- real customer-data processing flows; and
- production performance/outcome evidence.

The validation plan must use explicit synthetic fixtures rather than silently filling these gaps with pseudo-production facts.

---

## 12. Governance conclusion

This threat model does not:

- claim a real QuackBot vulnerability;
- claim that any attack has occurred;
- upgrade `QB-01`–`QB-06`;
- allocate `EV-AI002-*` evidence IDs;
- reduce any AI-002 risk score;
- validate `ASM-010` or `ASM-026`;
- establish EU AI Act high-risk classification;
- establish legal compliance; or
- authorize production.

The lifecycle gate remains:

> **PRODUCTION BLOCKED PENDING GATES**

The next technical step is `DW-AI002-VAL-SEC-01` — a separate QuackBot public-facing RAG/API technical-security validation plan followed by a deterministic synthetic lab for `QBSEC-T001`–`QBSEC-T012`.
