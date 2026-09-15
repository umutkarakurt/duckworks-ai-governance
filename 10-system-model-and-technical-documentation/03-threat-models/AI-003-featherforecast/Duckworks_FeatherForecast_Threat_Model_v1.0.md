# AI-003 FeatherForecast — Technical Threat Model

**Project:** Project W.I.N.G. — Phase II Technical AI Security Engineering & Adversarial Validation  
**Document ID:** DW-AI003-TM-01  
**Version:** 1.0  
**Date:** 15 September 2026  
**Status:** Threat-model baseline — validation not yet executed  
**AI system:** AI-003 — FeatherForecast  
**Architecture dependency:** `DW-AI003-ARCH-SEC-01 v1.0`  
**Current governance gate:** **Continue with monitoring**  
**Business owner:** Tobias Duckman — Director Supply Chain  
**AI/ML owner:** Dr. Ada Duckfield — Head Data & AI  
**Security owner:** Cassandra Duckley — Chief Information Security Officer  
**Governance owner:** Eleanor Duckford — AI Governance Lead

> Threat priority expresses technical test urgency. It does not replace Duckworks enterprise risk scores, establish a real production vulnerability, prove forecast unreliability or authorize risk reduction.

## 1. Risk and control traceability

Existing risks:

- `AI-003-R01 — Operational / financial`;
- `AI-003-R02 — Reliability & robustness`;
- `AI-003-R03 — Privacy & data governance`.

Existing controls:

- `FF-01 — Human Planning Approval & Override`;
- `FF-02 — Back-Testing, Stress Testing & Challenger Review`;
- `FF-03 — Automated Drift Alerts & Retraining Trigger`;
- `FF-04 — Supplier/Planning Data Access & Logging`;
- supporting `AI-GOV-02` and `AI-INC-01`.

Current repository evidence is insufficient to credit the FF controls as production-effective. `FF-01` additionally remains subject to open High audit finding `IAF-2026-003`.

## 2. Protected assets

1. demand-history datasets;
2. inventory-level data;
3. purchase-order data;
4. production schedules;
5. supplier lead-time data;
6. component-availability data;
7. aggregated order data;
8. feature definitions/transforms;
9. model artifacts;
10. model/configuration/threshold baselines;
11. forecast outputs;
12. back-test/stress-test results;
13. drift/performance metrics;
14. supplier/platform credentials;
15. service identities;
16. approval/override records;
17. procurement/production commitment records;
18. data/model lineage;
19. telemetry/security evidence;
20. known-good rollback state; and
21. Duckworks commercial planning confidentiality.

## 3. Threat actors / failure profiles

| ID | Profile | Typical objective / failure |
|---|---|---|
| A1 | External attacker | Manipulate planning data or gain commercial/supplier intelligence |
| A2 | Compromised supplier/data source | Inject false lead-time, availability or demand signals |
| A3 | Compromised Northstar/platform component | Alter model/configuration/forecast results or expose data |
| A4 | Compromised Duckworks service account | Bypass source/model/configuration/approval boundaries |
| A5 | Malicious or careless insider | Alter thresholds, backfills, forecasts or approval records |
| A6 | Build/configuration operator error | Promote wrong model/config/feature version |
| F1 | Data-quality failure | Missing, duplicate, stale, out-of-range or misaligned inputs |
| F2 | Concept/data drift | Operating conditions diverge from historical context |
| F3 | Model degradation | Forecast accuracy/performance declines without adequate signal |
| F4 | Human-process failure | Manager approval becomes superficial, stale or untraceable |
| F5 | Platform/availability failure | Forecasting service or data feed becomes unavailable/stale |

## 4. Priority model

| Priority | Meaning |
|---|---|
| P0 | Directly challenges data integrity, model/config integrity, material decision authority, confidentiality or continuity |
| P1 | Materially challenges monitoring, drift, lineage, forecast integrity or recovery |
| P2 | Important hardening/observability issue outside first-wave gate-critical scope |

## 5. Threat register

### 5.1 Source data / poisoning / history integrity

| ID | Priority | Threat |
|---|---:|---|
| FFT-001 | P0 | A compromised source injects extreme or false demand values. |
| FFT-002 | P0 | Supplier lead-time or availability values are manipulated to influence planning. |
| FFT-003 | P1 | Duplicate/replayed records distort demand or inventory aggregates. |
| FFT-004 | P1 | Stale source data is accepted as current. |
| FFT-005 | P0 | Unauthorized historical backfill rewrites training history. |
| FFT-006 | P0 | Legitimate history revision is accepted without provenance/review, masking manipulation. |
| FFT-007 | P1 | Time-zone/calendar alignment error shifts time-series windows. |
| FFT-008 | P1 | Unit/currency/quantity transformation error produces materially wrong features. |

### 5.2 Feature / training / scoring pipeline

| ID | Priority | Threat |
|---|---:|---|
| FFT-009 | P0 | Feature transformation logic is modified without authorization. |
| FFT-010 | P0 | Training-serving feature/schema skew changes model behavior. |
| FFT-011 | P1 | Missing-value/default handling differs between training and scoring. |
| FFT-012 | P1 | Target leakage creates misleading historical performance. |
| FFT-013 | P1 | Evaluation window is selectively chosen to hide poor periods. |
| FFT-014 | P0 | Training data snapshot is swapped after validation. |
| FFT-015 | P0 | Model artifact is replaced after approval. |
| FFT-016 | P0 | Configuration or forecast threshold is altered without approval. |

### 5.3 Drift / performance / retraining

| ID | Priority | Threat |
|---|---:|---|
| FFT-017 | P0 | Material concept/data drift is not detected. |
| FFT-018 | P1 | Data-quality failure is misclassified as drift, causing inappropriate retraining. |
| FFT-019 | P1 | Drift threshold is weakened to suppress alerts. |
| FFT-020 | P0 | Automated retraining promotes a model without challenger/validation review. |
| FFT-021 | P1 | Challenger model/evaluation baseline is stale or manipulated. |
| FFT-022 | P1 | Forecast error is aggregated so localized product-family degradation is hidden. |
| FFT-023 | P1 | Monitoring window excludes recent adverse performance. |
| FFT-024 | P0 | Retraining uses poisoned or unapproved data. |

### 5.4 Forecast result / decision authority

| ID | Priority | Threat |
|---|---:|---|
| FFT-025 | P0 | Forecast output is modified after model generation. |
| FFT-026 | P1 | Forecast is detached from the model/config/data versions that produced it. |
| FFT-027 | P0 | A stale forecast is presented as current. |
| FFT-028 | P0 | Forecasting service directly triggers a material purchase or production commitment. |
| FFT-029 | P0 | Manager approval is bypassed or forged. |
| FFT-030 | P1 | Manager override/rejection record is deleted or modified. |
| FFT-031 | P1 | Automation bias causes routine rubber-stamping of forecasts. |
| FFT-032 | P1 | A high-confidence or low-error score is misinterpreted as authority to bypass review. |

### 5.5 Confidentiality / access / supplier platform

| ID | Priority | Threat |
|---|---:|---|
| FFT-033 | P0 | Excessive user/service permissions expose supplier or commercial planning data. |
| FFT-034 | P0 | Cross-tenant/platform failure exposes Duckworks data through Northstar. |
| FFT-035 | P1 | Forecast/log exports contain more commercial data than required. |
| FFT-036 | P0 | Credentials or service tokens are exposed in pipeline/log data. |
| FFT-037 | P1 | Unauthorized user can retrieve historical forecasts or supplier data. |
| FFT-038 | P1 | Access logging is disabled or incomplete. |
| FFT-039 | P1 | Platform configuration expands supplier-data retention/use beyond approved purpose. |
| FFT-040 | P1 | Vendor/platform update changes behavior without Duckworks awareness. |

### 5.6 Availability / monitoring / recovery / evidence

| ID | Priority | Threat |
|---|---:|---|
| FFT-041 | P0 | Northstar outage prevents current forecasting during a material planning window. |
| FFT-042 | P0 | Source-feed outage yields incomplete forecast while appearing healthy. |
| FFT-043 | P1 | Monitoring/telemetry fails silently. |
| FFT-044 | P1 | Alert suppression or exception is not recorded. |
| FFT-045 | P1 | Known-good model/config/data state cannot be identified. |
| FFT-046 | P0 | Rollback restores mismatched model/config/data versions. |
| FFT-047 | P1 | Evidence/log records are modified, preventing decision reconstruction. |
| FFT-048 | P1 | Governance review relies on evidence that does not match the active model/config/data state. |

## 6. Key attack / failure paths

### AP-FF-01 — supplier-data poisoning to procurement distortion

Compromised supplier/source feed  
→ false lead time/availability enters ingestion  
→ validation/provenance fails to detect it  
→ forecast changes materially  
→ planner relies on forecast  
→ unnecessary/insufficient procurement commitment.

**Primary barriers:** FF-SR-002–007, FF-02, FF-01.

### AP-FF-02 — historical backfill poisoning

Attacker/operator modifies historical demand data  
→ training history silently changes  
→ model retrained/recalibrated  
→ backtest appears valid against manipulated history  
→ degraded baseline promoted.

**Primary barriers:** FF-SR-006–014, FF-02, AI-GOV-02.

### AP-FF-03 — training-serving skew

Feature/schema changes in scoring  
→ training pipeline remains unchanged  
→ forecasts degrade despite stable model artifact  
→ monitoring fails to distinguish skew from normal variation.

**Primary barriers:** FF-SR-008–010, FF-02, FF-03.

### AP-FF-04 — silent model/config change

Platform/operator changes model/config/threshold  
→ change trigger absent  
→ prior validation no longer representative  
→ forecast decisions use unvalidated baseline.

**Primary barriers:** FF-SR-011–015, FF-SR-034, AI-GOV-02.

### AP-FF-05 — drift missed or misdiagnosed

Market/supplier regime changes  
→ performance/data distribution shifts  
→ drift signal missing or confused with data-quality issue  
→ degraded forecasts persist.

**Primary barriers:** FF-SR-010, FF-SR-018–019, FF-03.

### AP-FF-06 — forecast output to unauthorized commitment

Forecast produced  
→ output tampered/stale or treated as authoritative  
→ human approval bypassed  
→ purchase/production commitment issued.

**Primary barriers:** FF-SR-015–023, FF-01.

### AP-FF-07 — commercial planning data exposure

Overbroad service/user access  
→ supplier/planning dataset or logs accessible  
→ unauthorized retrieval/export  
→ confidentiality/commercial harm.

**Primary barriers:** FF-SR-024–027, FF-04.

### AP-FF-08 — outage to stale forecast reliance

Northstar/source feed unavailable  
→ last forecast remains visible without staleness marker  
→ planner assumes it is current  
→ material decision based on stale state.

**Primary barriers:** FF-SR-017, FF-SR-028–031, FF-01.

## 7. Candidate first-wave validation tests — DESIGN ONLY

| Test | Scenario | Threats | Primary controls | Expected hardened outcome |
|---|---|---|---|---|
| `FFSEC-T001` | Source-data poisoning / extreme-value manipulation | FFT-001–004 | FF-02; FF-04 | invalid/unapproved batch quarantined; forecast not produced from poisoned batch |
| `FFSEC-T002` | Historical backfill / revision tampering | FFT-005–008 | FF-02; FF-04 | unapproved backfill blocked/review-required with lineage preserved |
| `FFSEC-T003` | Training-serving schema / feature skew | FFT-010–012 | FF-02; FF-03 | skew detected and affected scoring/promotion blocked |
| `FFSEC-T004` | Unauthorized feature-pipeline manipulation | FFT-009; 014 | FF-02; AI-GOV-02 | unauthorized feature/snapshot change detected; revalidation required |
| `FFSEC-T005` | Model / configuration / threshold integrity change | FFT-015; 016; 040 | FF-02; FF-03; AI-GOV-02 | change detected; prior validation invalidated; promotion blocked |
| `FFSEC-T006` | Data/performance drift detection and quality discrimination | FFT-017–024 | FF-02; FF-03 | drift/data-quality condition correctly separated; no silent auto-promotion |
| `FFSEC-T007` | Forecast-output mutation / version-integrity failure | FFT-025–027 | FF-01; FF-02 | altered/stale/unbound forecast invalidated |
| `FFSEC-T008` | Manager-approval bypass / direct commitment attempt | FFT-028; 029; 031; 032 | FF-01 | material commitment blocked without valid manager approval |
| `FFSEC-T009` | Override / decision-record tampering | FFT-030; 047; 048 | FF-01; FF-04 | tamper detected; decision evidence treated as invalid/incomplete |
| `FFSEC-T010` | Supplier/planning-data access-control challenge | FFT-033–039 | FF-04 | unauthorized access denied and logged; prohibited data absent from response/export |
| `FFSEC-T011` | Northstar/source outage / stale-forecast resilience | FFT-041–043 | FF-01; FF-03; AI-INC-01 | stale/unavailable forecast clearly marked; manual/degraded mode used |
| `FFSEC-T012` | Unvalidated retraining/change promotion and rollback | FFT-020; 024; 045; 046 | FF-02; FF-03; AI-GOV-02; AI-INC-01 | unvalidated promotion blocked; known-good model/config/data restored and verified |

## 8. Initial machine assertions for later validation

A later validation plan should verify at least:

1. poisoned/out-of-range source batches cannot enter the approved forecast path;
2. unapproved historical backfills are quarantined and cannot rewrite the approved history silently;
3. training-serving schema/feature skew is detected;
4. unauthorized feature/snapshot changes require revalidation;
5. model/config/threshold changes are version-detected and cannot silently promote;
6. drift is separated from data-quality failure in defined synthetic cases;
7. altered or stale forecast outputs are invalidated;
8. material purchase/production commitment is blocked without valid manager approval;
9. override/decision-record tampering is detected;
10. unauthorized supplier/planning-data access is denied and logged;
11. outage/staleness enters a controlled manual/degraded planning state;
12. failed/unvalidated change can be rolled back to a hash/version-verified known-good baseline;
13. every result records data/model/config/forecast/approval versions, correlation ID and evidence hash; and
14. `production_effectiveness_claim == false` and `iaf_2026_003_closure_authorized == false`.

## 9. Future evidence schema

Each executed case should record:

`test_id`, threat IDs, risk IDs, control IDs, requirement IDs, profile, architecture/threat-model/validation-plan/lab versions, source fixture IDs/hashes, data snapshot/version, feature schema/version, model/config/threshold version, forecast ID/hash/staleness, drift/data-quality state, manager approval/override state, access decision, detection events, rollback state, correlation ID, PASS/FAIL, evidence SHA-256 and limitations.

## 10. Acceptance principle

The later campaign should follow:

**known weak baseline → deliberate challenge → observable unsafe state → hardening → identical retest → evidence → control conclusion**

A hardened PASS may mean quarantine, validation failure, change blocking, access denial, approval blocking, stale-state rejection, manual fallback or successful rollback.

It must not be phrased as proof that FeatherForecast is accurate in production, immune to poisoning, always detects drift or produces optimal supply-chain decisions.

## 11. Known gaps before validation

TBD / not evidenced:

- actual data connectors and integrity controls;
- production dataset versions / lineage;
- real feature pipeline;
- actual Northstar architecture and contract;
- real model/configuration registry;
- actual forecast-accuracy/drift thresholds;
- real back-testing/challenger evidence;
- actual manager approval/override records;
- real access/logging configuration;
- actual fallback/manual planning SOP;
- production rollback exercises;
- sustained monitoring outcomes; and
- production incident/effectiveness evidence.

## 12. Governance conclusion

This threat model does not:

- claim a real attack or vulnerability;
- upgrade `FF-01`–`FF-04`;
- resolve `IAF-2026-003`;
- allocate `EV-AI003-*`;
- reduce AI-003 risk;
- close `ASM-011` or `ASM-027`; or
- change the current production/monitoring decision.

The governance position remains:

> **CONTINUE WITH MONITORING**

The validation plan and deterministic `FFSEC-T001`–`FFSEC-T012` lab have now completed commit-bound replay and canonical evidence reconciliation. Further testing should be triggered by production or production-equivalent evidence, material model/data/configuration/vendor/use change, control failure, adverse planning outcome or a deliberate next-phase assurance objective.
