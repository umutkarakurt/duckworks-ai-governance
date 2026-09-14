# AI-004 WingInspect Vision — Technical Evidence Reconciliation Record

**Project:** Project W.I.N.G. — Phase II Technical AI Security Engineering & Adversarial Validation  
**Document ID:** DW-AI004-REC-SEC-01  
**Version:** 1.0  
**Effective date:** 14 September 2026  
**System:** AI-004 — WingInspect Vision  
**Owner:** Eleanor Duckford — AI Governance Lead  
**Technical-security evidence owner:** Cassandra Duckley — Chief Information Security Officer  
**Business/process owner:** Henrietta Duckwell — Director Manufacturing  
**Product-safety / quality challenger:** Quentin Duckwell — Director Product Safety & Quality  
**AI/ML owner:** Dr. Ada Duckfield — Head of Data & AI  
**Current lifecycle gate:** **Restricted pilot only**  
**Evidence classification:** Fictional / synthetic / non-production  
**Reconciliation status:** Completed for the first WingInspect Phase II validation increment

> **Decision boundary:** This record reconciles synthetic technical evidence into the Duckworks governance evidence architecture. It does not establish production model robustness, manufacturing safety, legal compliance, ISO conformity, product conformity, production control effectiveness, or residual-risk reduction.

---

## 1. Reconciliation trigger

This reconciliation was opened after a clean commit-bound replay of the WingInspect adversarial-ML technical-security validation package.

GitHub Actions **Evidence reproducibility run #124** (`34836419132`) completed successfully against commit `8e8bb9e43aca3d4a9d2f5cfb6e401b8469c4ac0b`.

The run:

- executed under Python `3.12.14`;
- regenerated the WingInspect evidence from source;
- reproduced **8/8 deliberately vulnerable failures**;
- returned **8/8 hardened PASS**;
- ran **6/6 unit tests successfully**;
- passed the WingInspect CI verifier;
- verified `source_commit == GITHUB_SHA`;
- passed the repository-wide semantic-evidence verification step; and
- uploaded the retained WingInspect evidence artifact.

Artifact:

| Field | Value |
|---|---|
| Artifact name | `winginspect-security-evidence-8e8bb9e43aca3d4a9d2f5cfb6e401b8469c4ac0b` |
| Artifact ID | `10344067483` |
| SHA-256 digest | `sha256:d9f524770e3e3c406328245f46c7e610c7682cdd6d0072cb51a7fc01f2074f70` |
| Retention expiry | `14 October 2026` |
| Workflow job | `103951162863` |

---

## 2. Source classification

### 2.1 Mandatory legal requirements

This reconciliation makes **no new legal-classification determination**.

In particular, it does not classify WingInspect as an EU AI Act high-risk AI system and does not claim that the synthetic validation satisfies any legal requirement.

Any future legal applicability assessment must use the actual intended purpose, product/safety role, integration context, jurisdiction and Duckworks legal role.

### 2.2 Standards and framework guidance

The underlying architecture, threat model and validation plan are informed by the existing Duckworks technical-security baseline, including NIST adversarial-ML terminology, NIST AI RMF, MITRE ATLAS, ENISA AI-security guidance and NCSC / partner secure-AI-development guidance.

These inputs support structure and test design. They do not independently establish compliance, conformity or effectiveness.

### 2.3 Recommended organizational practices

The following are Duckworks evidence-governance practices:

- stable evidence IDs;
- vulnerable-versus-hardened replay;
- source-commit binding;
- semantic CI assertions;
- retained evidence artifacts;
- explicit control/evidence maturity separation;
- no automatic residual-risk reduction from synthetic PASS results; and
- human lifecycle decisions remaining independent of technical test automation.

### 2.4 Project assumptions

This reconciliation depends on the existing synthetic assumptions and limitations, including:

- deterministic surrogate computer-vision behavior rather than a real production model;
- synthetic image/challenge fixtures;
- synthetic human authorization;
- no real manufacturing camera or production line;
- no real VisiCore implementation;
- no production defect-rate or product-safety evidence; and
- no production operating period.

`ASM-008` and `ASM-028` remain open; this reconciliation does not close either assumption.

---

## 3. New stable evidence IDs

The following IDs are reserved and authoritative for the AI-004 Phase II technical-validation increment until incorporated into the next consolidated master evidence-index release.

| Evidence ID | Artifact | Evidence state | Primary control linkage | Primary risk linkage |
|---|---|---|---|---|
| `EV-AI004-006` | WingInspect Technical Security Validation Plan v1.0 | Designed | WI-02; WI-04; WI-06; WI-01 supporting boundary | AI-004-R01; AI-004-R03 |
| `EV-AI004-007` | Executable WingInspect Lab v0.1.0 | Synthetic technical implementation demonstrated | WI-02; WI-04; WI-06; WI-01 supporting boundary | AI-004-R01; AI-004-R03 |
| `EV-AI004-008` | Baseline Findings and Remediation Record v1.0 | Synthetic failure detection / remediation demonstrated | WI-02; WI-04; WI-06 | AI-004-R01; AI-004-R03 |
| `EV-AI004-009` | Hardened Campaign + Technical Security Test Report v1.2 | Synthetic operation tested | WI-02; WI-04; WI-06; WI-01 supporting boundary | AI-004-R01; AI-004-R03 |
| `EV-AI004-010` | Detection and Control-Signal Validation v1.0 | Synthetic detection / control-signal validation demonstrated | WI-02; WI-04; WI-06 | AI-004-R01; AI-004-R03 |
| `EV-AI004-011` | Commit-Bound GitHub Actions Replay + Evidence Artifact | Synthetic commit-bound reproducibility demonstrated | WI-02; WI-04; WI-06; WI-01 supporting boundary | AI-004-R01; AI-004-R03 |

Existing IDs `EV-AI004-001`–`005` remain unchanged.

---

## 4. Control reconciliation decision

### WI-01 — Qualified Human Final Inspection

Existing synthetic operating evidence remains valid. The Phase II lab adds supporting regression evidence that model output cannot independently authorize release in the hardened profile.

**Decision:** no production-effectiveness upgrade and no risk-reduction credit.

### WI-02 — Minimum Sensitivity & Safety Validation

The new evidence demonstrates:

- a defined technical-validation plan;
- deterministic challenge-set execution;
- reproduction of model/input weaknesses;
- same-test hardened retesting;
- validation blocking when expected-label behavior is violated; and
- commit-bound replay.

It does **not** demonstrate a real minimum sensitivity threshold, production false-negative performance, product-safety validation or physical-world adversarial robustness.

**Decision:** evidence maturity increases from design/status assertion to **bounded synthetic technical implementation, operation testing and commit-bound reproducibility demonstrated**. Production effectiveness remains unverified.

### WI-04 — Fail-Safe Manual Fallback & Stop Rule

The hardened lab demonstrates defined image-quality and runtime/dependency failures routing to manual hold rather than fail-open release.

**Decision:** bounded synthetic fail-safe operation is demonstrated. The historical source label remains `Planned` until the authoritative control-library source is separately revised. No production effectiveness is claimed.

### WI-06 — Change-Triggered Revalidation & Locked Baseline

The hardened lab demonstrates synthetic enforcement of:

- model digest integrity;
- configuration / threshold / preprocessing integrity;
- dataset/provenance checks; and
- revalidation requirements on defined baseline changes.

**Decision:** evidence maturity increases to bounded synthetic implementation/operation and commit-bound replay. Production change-control effectiveness remains unverified.

### Controls not upgraded

`WI-03`, `WI-05`, `AI-GOV-02` and `AI-INC-01` do not receive an evidence-maturity upgrade solely from this campaign.

---

## 5. Risk reconciliation decision

### AI-004-R01 — Safety & physical harm

The new technical evidence strengthens the synthetic evidence chain for WI-02/WI-04 and the WI-01 release boundary, but it does not provide production defect-escape, false-negative or product-safety outcomes.

**Recorded score:** unchanged at Severity 5 × Likelihood 2 = **10 High**.  
**Production authorization basis:** continue to use inherent risk conservatively until sufficient production evidence is accepted.  
**Gate:** **Restricted pilot only**.

### AI-004-R02 — Operational / financial

The first-wave technical campaign does not materially validate false-positive tuning, QA feedback or production waste/workload outcomes.

**Decision:** no evidence-maturity change. Existing unsupported reduction remains unresolved.

### AI-004-R03 — Reliability & robustness

The new technical evidence demonstrates synthetic treatment mechanisms for quality degradation, configuration integrity, baseline locking, failure handling and revalidation triggers.

**Recorded score:** unchanged at Severity 4 × Likelihood 2 = **8 Moderate**.  
**Score-support interpretation:** changes from evidence-absent to **provisional synthetic support only**; no production risk-reduction credit.  
**Production authorization basis:** use inherent risk conservatively until defined-period real evidence exists.  
**Gate:** **Restricted pilot only**.

---

## 6. Management conclusion

The evidence supports this narrow conclusion:

> Duckworks can demonstrate, within a deterministic synthetic lab, that defined WingInspect security/robustness weaknesses can be reproduced, detected or contained by specified controls, rerun after hardening, and reproduced from a committed repository state.

The evidence does **not** support:

- broader WingInspect deployment;
- a claim that the surrogate or a real model is adversarially robust;
- production safety or quality effectiveness;
- closure of `ASM-008` or `ASM-028`;
- lower AI-004 residual-risk scores;
- an EU AI Act classification conclusion;
- legal compliance;
- certification; or
- independent assurance.

The lifecycle decision therefore remains:

> **RETAIN RESTRICTED PILOT ONLY.**

---

## 7. Production evidence still required

Before a production-risk or broader-deployment recommendation can rely on WI-02/WI-04/WI-06, the portfolio would require, at minimum:

1. version-bound production or production-equivalent model/camera/configuration identification;
2. defined-period false-negative, defect-recall, defect-escape and image-quality evidence;
3. independent QA sampling and escaped-defect review;
4. real change/revalidation records showing baseline changes are blocked or reassessed before promotion;
5. actual fail-safe/manual fallback execution and exception evidence;
6. authorized human-release records over a defined population and period;
7. owner review, exceptions and incident handling; and
8. competent independent challenge before any effectiveness or risk-reduction credit.

---

## 8. Controlled-document precedence

This record is the authoritative **AI-004 technical-evidence reconciliation overlay** for the first WingInspect Phase II validation increment.

Until the next consolidated portfolio baseline:

- `Duckworks_AI_Control_Evidence_Index_v1.8.md` remains the master base index for all existing records;
- this record and `Duckworks_AI_Control_Evidence_Index_AI004_Reconciliation_v1.0.md` govern the new `EV-AI004-006`–`011` records;
- `Duckworks_AI_Control_Framework_Report_v1.6.md` remains the master base control report, supplemented by the AI-004 control reconciliation addendum;
- `Duckworks_AI_Risk_Scenarios_v1.4.md` remains the master base risk register, supplemented by the AI-004 risk reconciliation addendum; and
- no score or lifecycle-gate field is changed by implication.

This overlay approach preserves the v1.8 governance baseline while allowing Phase II evidence to be reconciled without rewriting unrelated portfolio records.
