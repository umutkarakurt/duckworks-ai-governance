# AI-004 WingInspect Vision — Technical Threat Model

**Project:** Project W.I.N.G. — Phase II Technical AI Security Engineering & Adversarial Validation  
**Document ID:** DW-AI004-TM-01  
**Version:** 1.0  
**Date:** 12 September 2026  
**Status:** Threat-model baseline — validation not yet executed  
**AI system:** AI-004 — WingInspect Vision  
**Architecture dependency:** `DW-AI004-ARCH-SEC-01 v1.0`  
**Business / risk owner:** Henrietta Duckwell — Director Manufacturing  
**AI / ML technical owner:** Dr. Ada Duckfield — Head of Data & AI  
**Product safety / quality challenger:** Quentin Duckwell — Director Product Safety & Quality  
**Security owner / challenger:** Cassandra Duckley — Chief Information Security Officer  
**Governance traceability:** Eleanor Duckford — AI Governance Lead  
**Current governance gate:** Restricted pilot only

> **Interpretation rule:** Threat priority in this document is a **technical testing priority**, not a replacement for Duckworks enterprise risk scoring. No threat-model entry changes AI-004's residual risk or lifecycle gate.

---

## 1. Purpose

This threat model converts the WingInspect Vision architecture into explicit attack and failure hypotheses that can later be tested in a synthetic adversarial-ML lab.

It covers:

1. conventional cyber threats affecting the computer-vision system;
2. adversarial-ML attacks affecting inputs, data, model, or inference behavior;
3. physical-environment manipulation relevant to visual inspection;
4. supply-chain and model/configuration integrity;
5. human-control and release-gate bypass; and
6. non-malicious robustness failures that can have security/safety-equivalent consequences.

The model deliberately separates **malicious adversarial activity** from **ordinary degradation / distribution shift**. Both matter, but they should not be reported as the same phenomenon.

---

## 2. Source and claim classification

### Mandatory legal requirements

No legal high-risk classification is assumed for WingInspect.

If WingInspect is later established to be a high-risk AI system under Regulation (EU) 2024/1689, Article 15 would make appropriate accuracy, robustness, and cybersecurity mandatory and explicitly addresses, where appropriate, data/model poisoning and adversarial examples/model evasion. The current portfolio has not established that classification.

### Standards and framework guidance

- **NIST AI 100-2 E2025** supplies common adversarial-ML terminology. For predictive AI, NIST identifies attack families including evasion, poisoning, and privacy attacks.
- **MITRE ATLAS** is used as a living threat-knowledge source. Relevant themes include physical environment access, craft adversarial data, manipulate/corrupt AI models, training-data poisoning, evade AI model, supply-chain compromise, and erode model/dataset integrity.
- **NCSC secure AI development guidance** supports threat modelling, secure development/supply chain, protected deployment, monitoring, and secure update management.
- **ENISA's multilayer framework** reinforces the need to combine normal cybersecurity foundations, AI-specific security, and sector-specific controls.

These sources inform coverage and terminology. They do not prove legal compliance, security, or control effectiveness.

### Duckworks recommended practices

The specific test priorities, security requirements, evidence schema, and candidate test cases below are Project W.I.N.G. practices designed for the fictional portfolio.

---

## 3. Protected assets and security objectives

| Asset | Security / quality objective |
|---|---|
| Product/component inspection image | Authentic, correctly bound to item/batch, suitable for inspection |
| Image metadata | Complete, accurate, non-substituted |
| Camera / fixture configuration | Known, controlled, observable when changed |
| Preprocessing pipeline | Versioned, integrity-protected, consistent with validated baseline |
| Vision model artifact | Approved, hash-identified, not silently replaced |
| Threshold / decision policy | Approved, versioned, protected from unauthorized change |
| Reference / validation datasets | Provenance, label integrity, segregation, reproducibility |
| Model output | Traceable to exact input/model/config; never direct release authority |
| Human inspection decision | Authenticated, complete, reviewable |
| Release-gate record | Mandatory for release; integrity and traceability preserved |
| QMS / evidence records | Complete and retrievable |
| Security / quality telemetry | Correlated, minimally sufficient, tamper-evident within lab scope |
| Vendor/runtime components | Provenance and integrity verified |
| Product-safety / quality decision boundary | Fail safe when AI or evidence is unavailable/untrusted |

---

## 4. Attacker / failure profiles

| Profile | Capability / access | Objective or failure mode |
|---|---|---|
| A1 — External physical manipulator | Can alter visible product/fixture, marker, lighting, orientation, or occlusion before capture | Cause a defect to be missed or a normal item to be flagged |
| A2 — Malicious insider / operator | Limited access to images, camera settings, inspection workflow, or files | Manipulate inspection evidence or bypass controls |
| A3 — ML / MLOps insider | Access to model/config/dataset pipeline | Change model, labels, thresholds, preprocessing, or approved baseline |
| A4 — Supply-chain adversary | Can influence a dependency, model/component package, or update source | Introduce compromised/backdoored artifact |
| A5 — Platform attacker | Access to host, service account, registry, or evidence pipeline | Replace artifacts, disable logging, disrupt service |
| A6 — Black-box model attacker | Can observe outputs from repeated controlled queries in a test environment | Craft evasion inputs or infer model behavior |
| F1 — Non-malicious environment shift | Lighting, lens, focus, angle, line conditions, product variants change | Reduce model performance without an attacker |
| F2 — Process / human-control failure | Incomplete human review, automation bias, missing authorization | Turn an AI mistake into a release outcome |
| F3 — Data/label quality failure | Incorrect labels, duplicates, contamination, stale reference set | Mislead validation or model tuning |

No profile authorizes testing of real facilities, cameras, suppliers, or production systems.

---

## 5. Technical priority model

| Priority | Meaning |
|---|---|
| **P0** | Test before any broader technical reliance; attack/failure can directly challenge a critical release, integrity, or fail-safe boundary |
| **P1** | High-value Phase II validation after P0; material security/robustness impact or control gap |
| **P2** | Important follow-on coverage; lower immediate test urgency or dependent on a more complete synthetic implementation |

Priority is based on test urgency and evidence value, not enterprise severity × likelihood.

---

## 6. Threat register

### 6.1 Physical / visual input threats

| ID | Threat | Type | Preconditions | Security / quality consequence | Mapped risk | Control focus | Priority |
|---|---|---|---|---|---|---|---|
| WIT-001 | Adversarial patch/marking changes model perception of a defective part | Adversarial evasion | Physical or synthetic image modification | False negative / missed defect | AI-004-R01 | WI-02; WI-03; WI-01 | P0 |
| WIT-002 | Localized occlusion hides the defect region | Evasion / physical manipulation | Access to object/fixture or test image | False negative | AI-004-R01 | WI-02; WI-01 | P0 |
| WIT-003 | Lighting manipulation causes an otherwise detectable defect to disappear | Physical / environmental | Control over illumination or synthetic transform | False negative / instability | AI-004-R01; R03 | WI-02; WI-06 | P0 |
| WIT-004 | Camera angle/pose manipulation moves defect outside expected representation | Physical / environmental | Camera/object position change | False negative / shift | AI-004-R01; R03 | WI-02; WI-06 | P1 |
| WIT-005 | Blur/focus degradation reduces defect visibility | Robustness / environmental | Camera degradation or transform | False negative / uncertain inference | AI-004-R01; R03 | WI-04; WI-02 | P0 |
| WIT-006 | Compression/noise/corruption changes inference materially | Robustness / digital | Image transformation or transport change | False negative/positive | AI-004-R01; R02; R03 | WI-02; WI-04 | P1 |
| WIT-007 | Clean image is replaced with an older/replayed acceptable image | Conventional integrity attack | Access to acquisition path | Defective item may be associated with benign evidence | AI-004-R01 | WI-01; WI-06 | P0 |
| WIT-008 | Image and item/batch metadata are mismatched | Conventional integrity / process | Metadata manipulation or workflow defect | Wrong inspection result applied to item | AI-004-R01; R02 | WI-01; WI-06 | P0 |
| WIT-009 | Malformed/oversized image causes parser/runtime resource failure | Availability | Input path access | Inspection outage or unsafe fallback | AI-004-R01; R02 | WI-04 | P1 |
| WIT-010 | Deliberate chaff stream creates excessive false positives / workload | Abuse / availability | Repeated input control | Inspector overload; degraded workflow | AI-004-R02 | WI-05; WI-04 | P2 |

### 6.2 Model, preprocessing, and decision-policy threats

| ID | Threat | Type | Preconditions | Consequence | Mapped risk | Control focus | Priority |
|---|---|---|---|---|---|---|---|
| WIT-011 | Small digital perturbation produces a model-evasion false negative | Adversarial evasion | Ability to modify input pixels in lab | Missed defect | AI-004-R01 | WI-02 | P0 |
| WIT-012 | Preprocessing parameters are changed without revalidation | Configuration integrity | Config write access | Validation/runtime mismatch | AI-004-R01; R03 | WI-06 | P0 |
| WIT-013 | Decision threshold is lowered/raised without approval | Configuration integrity | Policy/config access | False-negative or false-positive rate shifts | AI-004-R01; R02 | WI-06; WI-05 | P0 |
| WIT-014 | Model artifact is replaced with unapproved version | Model integrity | Registry/runtime write access | Unknown behavior or degraded safety | AI-004-R01; R03 | WI-06; WI-02 | P0 |
| WIT-015 | Class map / label mapping is altered | Configuration integrity | Config write access | Defects misinterpreted | AI-004-R01; R03 | WI-06 | P0 |
| WIT-016 | Runtime uses stale model/config after approved change | Change-control failure | Deployment drift | Evidence refers to wrong baseline | AI-004-R01; R03 | WI-06 | P1 |
| WIT-017 | Inference error defaults to "pass" | Fail-open design | Runtime failure | Product can progress without valid inference | AI-004-R01 | WI-04; WI-01 | P0 |
| WIT-018 | Output/result object is modified between model and inspector UI | Conventional integrity | App/service compromise | Human sees falsified AI result | AI-004-R01; R02 | WI-01; WI-06 | P1 |

### 6.3 Dataset and validation threats

| ID | Threat | Type | Preconditions | Consequence | Mapped risk | Control focus | Priority |
|---|---|---|---|---|---|---|---|
| WIT-019 | Training/validation image is poisoned with crafted content | Data poisoning | Dataset contribution/update access | Model or validation integrity degraded | AI-004-R01; R03 | WI-02; WI-06 | P0 |
| WIT-020 | Defect labels are deliberately or accidentally changed | Label poisoning / data quality | Label-edit access | Incorrect validation/performance conclusions | AI-004-R01; R03 | WI-02; WI-06 | P0 |
| WIT-021 | Backdoor trigger is introduced through poisoned training examples | Model/data poisoning | Training/update influence | Triggered false negatives | AI-004-R01 | WI-02; WI-06 | P1 |
| WIT-022 | Test/adversarial samples leak into tuning data | Evaluation contamination | Poor dataset segregation | Inflated robustness claims | AI-004-R01; R03 | WI-02 | P1 |
| WIT-023 | Dataset provenance/hash is missing or invalid but data is accepted | Integrity / governance | Weak ingestion gate | Untraceable or tampered evidence | AI-004-R01; R03 | WI-06 | P0 |
| WIT-024 | Reference set no longer represents current line/product variants | Distribution shift | Product/process evolution | False reassurance from stale testing | AI-004-R01; R03 | WI-03; WI-06 | P1 |

### 6.4 Supply-chain and platform threats

| ID | Threat | Type | Preconditions | Consequence | Mapped risk | Control focus | Priority |
|---|---|---|---|---|---|---|---|
| WIT-025 | VisiCore/model/runtime package is compromised before staging | Supply-chain compromise | Supplier/distribution compromise | Backdoor or malicious runtime/model | AI-004-R01; R03 | WI-06; supplier controls | P1 |
| WIT-026 | Dependency package or base runtime is malicious/vulnerable | Software supply chain | Build dependency compromise | Code execution / integrity loss | AI-004-R01; R03 | WI-06; AI-INC-01 | P1 |
| WIT-027 | Artifact digest/provenance check is bypassed | Integrity control bypass | Registry/build access | Untrusted artifact becomes approved | AI-004-R01; R03 | WI-06 | P0 |
| WIT-028 | Model/config registry credentials are compromised | Credential / privilege attack | Secret or admin access | Model/config replacement | AI-004-R01; R03 | WI-06; AI-INC-01 | P1 |
| WIT-029 | Security/quality telemetry is disabled or selectively deleted | Defense evasion | Platform/admin access | Failures/attacks cannot be reconstructed | AI-004-R01; R03 | WI-03; AI-INC-01 | P1 |
| WIT-030 | QMS/release records are altered after decision | Evidence integrity | QMS/admin access | False release/override evidence | AI-004-R01; R02 | WI-01; AI-INC-01 | P1 |
| WIT-031 | Model service is unavailable and workflow silently continues | Availability / fail-open | Outage | Inspection bypass or unsafe continuation | AI-004-R01; R02 | WI-04 | P0 |

### 6.5 Human, process, and purpose-boundary threats

| ID | Threat | Type | Preconditions | Consequence | Mapped risk | Control focus | Priority |
|---|---|---|---|---|---|---|---|
| WIT-032 | Inspector over-relies on high-confidence AI "pass" | Automation bias | Weak UI/process/training | Model false negative escapes human challenge | AI-004-R01 | WI-01; WI-03 | P0 |
| WIT-033 | Release is attempted without complete human authorization | Control bypass | Workflow/API access | Autonomous or unauthorised release | AI-004-R01 | WI-01 | P0 |
| WIT-034 | Human override/rejection record lacks rationale/identity/timestamp | Evidence-quality failure | Weak control operation | Auditability and challenge weakened | AI-004-R01; R02 | WI-01 | P1 |
| WIT-035 | Material model/camera/data change is promoted without revalidation | Change-control bypass | Release/config authority | Prior evidence no longer applicable | AI-004-R01; R03 | WI-06; AI-GOV-02 | P0 |
| WIT-036 | Camera purpose expands to worker monitoring/biometrics without reassessment | Purpose creep | Operational scope change | Privacy/workforce/legal impact outside current assessment | governance/privacy | AI-GOV-02; ASM-028 | P1 |

---

## 7. Attack / failure paths

### AP-WI-01 — Physical evasion to missed defect

```text
Access to product / fixture
→ apply adversarial marking or occlusion
→ image remains processable
→ model returns benign / pass-like result
→ inspector is exposed to automation-bias pressure
→ human release gate is the final barrier
→ if human review is ineffective, defective item may progress
```

**Critical point:** a successful model evasion does not automatically mean the release control failed. Model robustness and human release effectiveness must be tested and concluded separately.

### AP-WI-02 — Environment degradation to silent false negative

```text
Lighting / focus / angle changes
→ image quality degrades or distribution shifts
→ quality gate fails to detect unsuitable input
→ model inference proceeds outside validated conditions
→ false-negative risk increases
→ item reaches human review with misleading model result
```

### AP-WI-03 — Model/configuration integrity attack

```text
Registry/config access
→ replace model / preprocessing / class map / threshold
→ integrity/version check absent or bypassed
→ runtime executes unapproved baseline
→ prior validation evidence no longer applies
→ false-negative / false-positive behavior may change
```

### AP-WI-04 — Dataset poisoning / backdoor

```text
Contribute or modify dataset/labels
→ provenance/integrity control fails
→ poisoned samples enter training/validation/tuning
→ model or benchmark becomes biased toward attacker condition
→ trigger/condition produces targeted misclassification
→ validation may provide false reassurance
```

### AP-WI-05 — Supply-chain artifact compromise

```text
Compromised vendor/dependency artifact
→ weak provenance / digest enforcement
→ artifact enters approved registry
→ malicious or degraded runtime/model executes
→ output/evidence integrity affected
```

### AP-WI-06 — Release-gate bypass

```text
AI result exists
→ required human authorization missing or forged
→ workflow incorrectly permits release
→ AI effectively gains de facto release authority
```

This path directly challenges `WI-01` and the critical `ASM-008` boundary.

---

## 8. Security requirements under test

The threat model adopts `WI-SR-001` through `WI-SR-020` from `DW-AI004-ARCH-SEC-01 v1.0`.

Highest-priority requirements for first-wave technical validation:

- `WI-SR-001` / `002` — AI cannot release; human authorization is mandatory.
- `WI-SR-004` — quality failure routes to manual/hold.
- `WI-SR-006` / `007` / `008` — model, preprocessing, class-map, and threshold integrity/versioning.
- `WI-SR-009` / `010` — dataset/label provenance and quarantine.
- `WI-SR-012` — adversarial and corruption challenge coverage.
- `WI-SR-013` — fail-safe fallback.
- `WI-SR-014` — material changes trigger regression.
- `WI-SR-015` / `016` — correlated, reproducible evidence.
- `WI-SR-020` — synthetic PASS does not change production governance automatically.

---

## 9. Initial validation cases — design only

The following cases are proposed for the next validation-plan step. They are **not executed evidence** in this document.

| Test ID | Candidate test | Primary threats | Expected security property |
|---|---|---|---|
| `WISEC-T001` | Synthetic patch / localized occlusion evasion | WIT-001; WIT-002; WIT-011 | Model weakness is measurable; release still requires independent human authorization; result is attributed to exact fixture/model version |
| `WISEC-T002` | Lighting / blur / noise / compression challenge | WIT-003–006 | Unsuitable input is detected/routed or robustness degradation is explicitly surfaced; no silent automatic pass |
| `WISEC-T003` | Model artifact digest mismatch | WIT-014; WIT-027 | Unapproved model cannot become the approved inference baseline |
| `WISEC-T004` | Threshold / preprocessing / class-map tamper | WIT-012; WIT-013; WIT-015 | Configuration mismatch blocks baseline use and creates revalidation evidence |
| `WISEC-T005` | Dataset / label provenance poisoning | WIT-019; WIT-020; WIT-023 | Unapproved or integrity-failed sample/label set is quarantined before approved validation |
| `WISEC-T006` | Synthetic backdoor-trigger fixture | WIT-021; WIT-022 | Triggered misclassification can be detected as a model weakness without contaminating the clean benchmark; evidence remains segregated |
| `WISEC-T007` | Camera/model/quality dependency failure | WIT-005; WIT-017; WIT-031 | Failure routes to manual inspection/hold; never defaults to automatic acceptance |
| `WISEC-T008` | Mandatory Human Release Gate bypass attempt | WIT-032–035 | Release without complete authenticated human authorization is denied and logged |

A later validation plan must define exact fixtures, clean/adversarial pairing, deterministic transformations, expected outputs, evidence schema, and acceptance logic before these IDs are treated as executable tests.

---

## 10. Initial assertions

The validation plan should make at least these assertions machine-checkable where feasible:

1. `release_gate == ALLOW` requires a complete human inspector authorization record.
2. Model output alone can never set `release_gate == ALLOW`.
3. `image_quality != PASS` results in `MANUAL_HOLD` or equivalent safe route.
4. `model_digest != approved_model_digest` prevents approved-baseline inference.
5. Preprocessing / threshold / class-map mismatch prevents approved-baseline inference.
6. Dataset/label provenance or hash failure prevents sample promotion into the approved reference set.
7. Every material test result records image/fixture, model, config, dataset, and test-suite versions.
8. Every material event has a correlation ID joining acquisition, quality, inference, human disposition, and release-gate evidence.
9. A material baseline change requires a recorded regression/revalidation result before promotion.
10. A synthetic attack PASS/FAIL cannot automatically change the AI-004 risk score or gate.

---

## 11. Detection hypotheses

The first validation plan should assess, separately from prevention:

- model/configuration integrity mismatch;
- abnormal image-quality patterns;
- repeated camera/fixture degradation;
- unapproved threshold or preprocessing changes;
- dataset/label integrity failures;
- release attempts without complete human authorization;
- missing expected telemetry;
- repeated AI/human disagreement patterns;
- model/runtime failures invoking manual fallback; and
- material version changes without linked revalidation evidence.

A model-attack detector is not a substitute for model robustness, human inspection, or the release gate.

---

## 12. Control and risk traceability

| Threat area | Primary Duckworks risk | Main controls |
|---|---|---|
| Adversarial evasion / false negatives | `AI-004-R01` | WI-02; WI-03; WI-01 |
| Image/environment degradation | `AI-004-R01`; `AI-004-R03` | WI-02; WI-04; WI-06 |
| Model/config tamper | `AI-004-R01`; `AI-004-R03` | WI-06; WI-02 |
| Dataset/label poisoning | `AI-004-R01`; `AI-004-R03` | WI-02; WI-06 |
| False-positive manipulation / chaff | `AI-004-R02` | WI-05; WI-04 |
| Release-gate bypass / automation bias | `AI-004-R01` | WI-01; WI-03 |
| Supply-chain compromise | `AI-004-R01`; `AI-004-R03` | WI-06; AI-INC-01; third-party controls as applicable |
| Availability / fail-open | `AI-004-R01`; `AI-004-R02` | WI-04; WI-01 |
| Purpose creep / workforce camera use | governance/privacy reassessment | AI-GOV-02; ASM-028 |

No new parallel enterprise risk IDs are created by the threat model.

---

## 13. Evidence schema for future test execution

Each future machine-readable test result should include at least:

```text
test_id
threat_ids
risk_ids
control_ids
security_requirement_ids
architecture_version
threat_model_version
test_suite_version
fixture_or_image_ids
fixture_type: clean | corrupted | adversarial | poisoned
expected_label_or_condition
camera_profile_version
preprocessing_version
model_version
model_sha256
threshold_policy_version
dataset_or_fixture_registry_version
human_release_gate_tested: true/false
expected_result
actual_result
detection_events
correlation_id
result: PASS | FAIL | ERROR | BLOCKED | NOT_RUN
evidence_sha256
limitations
```

Raw execution evidence should be preserved separately from management conclusions.

---

## 14. First-wave acceptance boundary

A later WingInspect Phase II validation increment should not be considered complete merely because the model classifies all challenge samples correctly.

The meaningful acceptance chain is:

**known baseline → deliberate weakness/challenge → observable result → control response → evidence → remediation where needed → identical retest → explicit limitation**

A strong technical result may show that:

- the model is vulnerable to a defined adversarial condition **but the release/fail-safe controls contain the system-level consequence**; or
- a model/config/data integrity control blocks the unsafe baseline before inference; or
- a challenge exposes a real gap that remains open.

The objective is evidence quality, not manufacturing a perfect PASS rate.

---

## 15. Known gaps before validation

Before any test execution is treated as canonical evidence, the lab design still needs to define:

1. deterministic synthetic clean/defect image fixtures;
2. how adversarial patches/perturbations are generated without implying physical-world effectiveness beyond the lab;
3. a simple reproducible vision-model or deterministic surrogate suitable for testing;
4. image-quality checks and failure routing;
5. approved model/config/dataset manifests and hashing;
6. a simulated human-release-gate interface reusing the existing `WI-01` evidence logic where appropriate;
7. telemetry/correlation event schema;
8. exact criteria for vulnerable vs hardened profiles;
9. CI replay and evidence-retention design; and
10. explicit divergence from any real production camera/model architecture.

The lab should not claim to validate employee behavior, real product safety, a real VisiCore model, or real factory conditions.

---

## 16. Governance conclusion

This threat model **does not**:

- establish a production vulnerability;
- establish that an attacker can manipulate a real manufacturing line;
- demonstrate adversarial robustness;
- validate `WI-02`–`WI-06`;
- close `ASM-008` or `ASM-028`;
- lower `AI-004-R01/R02/R03`;
- alter the Restricted Pilot gate; or
- establish legal compliance / EU AI Act classification.

It establishes the security questions and testable boundaries required for the next Phase II step.

**Next technical step:** create `DW-AI004-VAL-SEC-01` — the WingInspect adversarial-ML technical-security validation plan — and then build a deterministic synthetic lab implementing `WISEC-T001`–`WISEC-T008`.

---

## 17. External public references

- NIST AI 100-2 E2025 — https://csrc.nist.gov/pubs/ai/100/2/e2025/final
- MITRE ATLAS — https://atlas.mitre.org/
- NCSC Guidelines for Secure AI System Development — https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development
- ENISA Multilayer Framework for Good Cybersecurity Practices for AI — https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai
- EU AI Act consolidated text — https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng

---

> **Portfolio boundary:** This threat model is a fictional/synthetic portfolio artifact. It authorizes no testing of real Duckworks, manufacturing facilities, employees, products, cameras, networks, suppliers, or third parties.
