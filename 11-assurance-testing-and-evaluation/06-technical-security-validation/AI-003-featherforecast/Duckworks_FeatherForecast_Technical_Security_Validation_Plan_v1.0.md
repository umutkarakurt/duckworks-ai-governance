# AI-003 FeatherForecast — Data Integrity / Poisoning / Drift / Decision-Support Resilience Technical Security Validation Plan

**Project:** Project W.I.N.G. — Phase II Technical AI Security Engineering & Adversarial Validation  
**Document ID:** DW-AI003-VAL-SEC-01  
**Version:** 1.0  
**Date:** 15 September 2026  
**Status:** Approved-for-build portfolio validation design — fictional / synthetic / non-production  
**AI system:** AI-003 — FeatherForecast  
**Architecture dependency:** `DW-AI003-ARCH-SEC-01 v1.0`  
**Threat-model dependency:** `DW-AI003-TM-01 v1.0`  
**Current governance position:** **Continue with monitoring**  
**Primary control targets:** `FF-01`, `FF-02`, `FF-03`, `FF-04`

> **Conclusion boundary:** This plan validates a deterministic synthetic forecasting-pipeline and decision-control chain. It does not establish production forecast accuracy, poisoning resistance, drift-detection effectiveness, Northstar security, supplier assurance, human-approval operating effectiveness, residual-risk reduction or legal compliance.

## 1. Objective

Convert the FeatherForecast architecture and threat model into a reproducible first-wave campaign that:

- reproduces deliberately seeded source-data, history, feature, model/configuration, drift, forecast-integrity, approval, access, availability and rollback weaknesses;
- demonstrates that pipeline and decision controls—not forecast confidence or model error metrics alone—enforce governance boundaries;
- distinguishes data-quality failure from statistical/performance drift;
- records raw machine-readable evidence;
- applies deterministic hardening;
- reruns identical cases after hardening;
- validates defined security/control signals;
- keeps human planning authority independent of forecast output; and
- supports later evidence reconciliation without changing current risk scores, assumptions, audit findings or the Continue-with-monitoring position automatically.

## 2. Authorization and scope

Testing is limited to:

- synthetic demand, inventory, purchase-order, production, supplier and order data;
- synthetic feature transformations;
- synthetic model/configuration/threshold versions;
- synthetic forecasts and forecast hashes;
- synthetic Northstar platform behavior;
- synthetic planner identities and approvals;
- synthetic supplier/planning access decisions;
- synthetic drift/data-quality states;
- local deterministic control logic;
- repository-local evidence; and
- later GitHub Actions replay.

Out of scope:

- real Duckworks planning or procurement systems;
- real Northstar systems;
- real supplier/customer data;
- real credentials or service tokens;
- real production retraining;
- live purchasing/production commitments;
- destructive or unauthorized testing;
- real commercial confidentiality assessment;
- production forecast accuracy validation; and
- legal or contractual assurance.

## 3. Source classification

### 3.1 Mandatory legal requirements

The validation preserves the FeatherForecast applicability addendum:

- FeatherForecast is **not classified as a high-risk AI system** by this portfolio on the current internal supply-chain forecasting/decision-support facts;
- EU AI Act classification must be reassessed if intended purpose, affected persons, decision authority, product integration or safety role changes;
- NIS2 remains an organization/national-law scope question;
- Trade Secrets Directive relevance depends on the legal status of supplier/commercial information and national implementation;
- GDPR applies where personal data enter the workflow; and
- CRA applicability is not established for the internal planning service.

No executable test below is itself a legal-compliance, conformity or supplier-assurance test.

### 3.2 Standards / framework guidance

The plan is informed by the existing Duckworks baseline and FeatherForecast addendum, including ISO/IEC 27001, ISO/IEC 42001, NIST CSF 2.0, NIST AI RMF, NIST AI 100-2 E2025, NCSC secure-AI-development guidance and MITRE ATLAS.

These references do not independently establish compliance, certification or effectiveness.

### 3.3 Recommended organizational practice

The two-profile campaign, deterministic fixtures, version binding, quarantine, backfill review, training-serving skew checks, controlled retraining, manager-approval separation, staleness handling, rollback and evidence-retention rules are Duckworks portfolio practices.

## 4. Control targets

| Control | Validation role | Synthetic conclusion available |
|---|---|---|
| `FF-01 — Human Planning Approval & Override` | Primary | Manager-approval and decision-record control mechanics can be exercised; **does not prove production operation or close IAF-2026-003** |
| `FF-02 — Back-Testing, Stress Testing & Challenger Review` | Primary | Defined data/model/configuration challenges can require review or block promotion |
| `FF-03 — Automated Drift Alerts & Retraining Trigger` | Primary | Defined drift/data-quality, retraining, staleness and change signals can be exercised |
| `FF-04 — Supplier/Planning Data Access & Logging` | Primary | Defined access, minimization and logging boundaries can be exercised |
| `AI-GOV-02` | Supporting | Material data/model/configuration changes can require revalidation |
| `AI-INC-01` | Supporting | Defined outage/rollback behavior can be exercised; enterprise incident capability is not established |

## 5. Test profiles

### Vulnerable profile

The deliberately weak profile:

- accepts poisoned/extreme source data;
- applies historical backfills without review;
- scores with training-serving schema/feature skew;
- accepts unauthorized feature-pipeline changes;
- uses changed model/configuration/thresholds without revalidation;
- misclassifies data-quality failure and drift and allows silent automated promotion;
- accepts altered/stale/unbound forecast output;
- permits a material commitment without valid manager approval;
- accepts tampered decision/override records;
- exposes supplier/planning data to an unauthorized user;
- presents stale forecasts as current during platform outage; and
- promotes unvalidated retraining and cannot reliably restore a matched known-good state.

### Hardened profile

The hardened profile:

- quarantines invalid/unapproved source batches;
- requires review for historical backfills and preserves lineage;
- detects training-serving skew and blocks affected scoring/promotion;
- detects unauthorized feature/snapshot change and requires revalidation;
- detects model/configuration/threshold drift and blocks promotion;
- separates defined data-quality failures from defined drift cases;
- invalidates altered, stale or version-unbound forecasts;
- requires authorized manager approval before material commitment;
- detects decision-record tampering;
- denies and logs unauthorized supplier/planning-data access;
- enters controlled manual/degraded mode during outage/staleness; and
- blocks unvalidated retraining/promotion and restores a version/hash-matched known-good baseline.

## 6. First-wave cases

| Test | Scenario | Threats | Primary controls | Hardened acceptance condition |
|---|---|---|---|---|
| `FFSEC-T001` | Source-data poisoning / extreme-value manipulation | FFT-001–004 | FF-02; FF-04 | invalid/unapproved batch quarantined; no forecast from poisoned batch |
| `FFSEC-T002` | Historical backfill / revision tampering | FFT-005–008 | FF-02; FF-04 | unapproved backfill blocked/review-required; approved-history hash preserved |
| `FFSEC-T003` | Training-serving schema / feature skew | FFT-010–012 | FF-02; FF-03 | skew detected; affected scoring/promotion blocked |
| `FFSEC-T004` | Unauthorized feature-pipeline manipulation | FFT-009; FFT-014 | FF-02; AI-GOV-02 | unauthorized feature/snapshot change detected; revalidation required |
| `FFSEC-T005` | Model / configuration / threshold integrity change | FFT-015; FFT-016; FFT-040 | FF-02; FF-03; AI-GOV-02 | change detected; prior validation invalidated; promotion blocked |
| `FFSEC-T006` | Drift detection and data-quality discrimination | FFT-017–024 | FF-02; FF-03 | defined quality case classified as data quality and defined distribution case as drift; no silent auto-promotion |
| `FFSEC-T007` | Forecast-output mutation / version-integrity / staleness failure | FFT-025–027 | FF-01; FF-02 | altered/stale/unbound forecast invalidated and cannot support commitment |
| `FFSEC-T008` | Manager-approval bypass / direct commitment attempt | FFT-028; FFT-029; FFT-031; FFT-032 | FF-01 | material commitment blocked without valid authorized approval |
| `FFSEC-T009` | Override / decision-record tampering | FFT-030; FFT-047; FFT-048 | FF-01; FF-04 | tamper detected; decision evidence invalid/incomplete; investigation required |
| `FFSEC-T010` | Supplier/planning-data access-control challenge | FFT-033–039 | FF-04 | unauthorized access denied and logged; prohibited commercial canary absent from response/export |
| `FFSEC-T011` | Northstar/source outage / stale-forecast resilience | FFT-041–043 | FF-01; FF-03; AI-INC-01 | stale/unavailable forecast visibly rejected; manual/degraded planning mode used |
| `FFSEC-T012` | Unvalidated retraining/change promotion and rollback | FFT-020; FFT-024; FFT-045; FFT-046 | FF-02; FF-03; AI-GOV-02; AI-INC-01 | unvalidated promotion blocked; matched known-good model/config/data state restored and verified |

## 7. Machine-checkable acceptance assertions

The campaign must demonstrate:

1. twelve vulnerable cases and twelve hardened cases;
2. vulnerable profile reproduces all twelve deliberately seeded unsafe states;
3. hardened profile returns **12 PASS / 0 FAIL**;
4. T001 prevents a poisoned/unapproved batch from entering the approved forecast path;
5. T002 blocks an unapproved historical backfill and preserves the approved-history identity;
6. T003 detects training-serving schema/feature skew;
7. T004 detects unauthorized feature/snapshot change and requires revalidation;
8. T005 detects model/configuration/threshold change, invalidates prior validation and blocks promotion;
9. T006 correctly separates the defined data-quality condition from the defined distribution-drift condition and performs no automatic promotion;
10. T007 invalidates altered, stale or version-unbound forecast output;
11. T008 prevents a material commitment without valid manager approval;
12. T009 detects decision/override-record tampering and treats the record as invalid;
13. T010 denies/logs unauthorized planning-data access and returns no prohibited commercial canary;
14. T011 enters controlled manual/degraded mode on outage/staleness;
15. T012 blocks unvalidated retraining/promotion and restores a verified known-good model/config/data state;
16. every result records data/model/config/forecast/approval state, correlation ID, evidence hash and limitations;
17. in GitHub Actions, `source_commit == GITHUB_SHA`;
18. `production_effectiveness_claim == false`;
19. `forecast_accuracy_claim == false`;
20. `legal_compliance_claim == false`;
21. `risk_score_change_authorized == false`;
22. `governance_gate_change_authorized == false`;
23. `evidence_id_allocation_authorized == false`;
24. `iaf_2026_003_closure_authorized == false`; and
25. `assumption_closure_authorized == false`.

## 8. Evidence schema

Each result records:

`test_id`, threat IDs, risk IDs, control IDs, requirement IDs, profile, architecture/threat-model/validation-plan/lab versions, source fixture IDs/hashes, data snapshot/version, feature schema/version, model/configuration/threshold version, forecast ID/hash/staleness, drift/data-quality state, manager approval/override state, access decision, detection events, rollback state, correlation ID, PASS/FAIL, evidence SHA-256 and limitations.

## 9. Detection interpretation

Detection is not treated as the sole control.

Examples:

- a poisoning alert does not replace source validation/quarantine;
- a backfill alert does not replace lineage/review;
- a skew alert does not replace scoring/promotion blocking;
- a drift alert does not replace model/performance review;
- forecast-integrity logging does not replace output invalidation;
- an approval log does not replace the material-commitment gate;
- an access alert does not replace authorization denial; and
- outage telemetry does not replace manual/degraded planning capability.

A hardened PASS is based on the **pipeline/decision outcome**, not merely an alert firing.

## 10. Repository replay rule

Canonical `EV-AI003-*` IDs and AI-003 control/risk reconciliation are deferred until GitHub Actions successfully replays the lab against an identifiable repository commit and retains the generated evidence artifact.

## 11. Open-audit-finding rule

`IAF-2026-003` remains open.

This synthetic lab may demonstrate a **manager-approval mechanism**, direct-commitment blocking and decision-record integrity. It does not demonstrate that `FF-01` operates in a production or production-equivalent FeatherForecast process and therefore does not by itself satisfy the finding's closure criteria.

## 12. Governance effect

Successful local execution does not:

- change AI-003 risk scores;
- validate or close `ASM-011` or `ASM-027`;
- upgrade production effectiveness of `FF-01`–`FF-04`;
- close `IAF-2026-003`;
- establish production forecast accuracy or reliability;
- establish Northstar security or supplier assurance;
- authorize a new governance gate; or
- allocate canonical AI-003 evidence IDs.

The governance position remains:

> **CONTINUE WITH MONITORING**

> **Portfolio boundary:** Duckworks, FeatherForecast, Northstar, all planners, files, datasets, features, models, forecasts, approvals, access events, failures and evidence in this validation are fictional or synthetic unless explicitly identified as a public source.
