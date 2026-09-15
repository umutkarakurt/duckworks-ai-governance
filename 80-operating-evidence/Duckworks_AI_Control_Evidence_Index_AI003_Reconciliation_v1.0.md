# Duckworks AI Control Evidence Index — AI-003 Reconciliation Addendum

**Project:** W.I.N.G. — Workflows, Intelligence, Next-Generation Governance  
**Document ID:** DW-AIEI-AI003-REC-01  
**Version:** 1.0  
**Effective date:** 15 September 2026  
**Owner:** AI Governance Lead  
**Base register:** `Duckworks_AI_Control_Evidence_Index_v1.8.md`  
**Scope:** AI-003 FeatherForecast Phase II technical-security evidence only  
**Status:** Controlled reconciliation overlay pending next master-index consolidation

> This addendum does not replace or renumber any existing evidence record. It reserves `EV-AI003-001`–`EV-AI003-007` as stable evidence IDs and incorporates them into the current AI-003 evidence view.

## 1. New evidence records

| Evidence ID | AI entry | Risk ID | Control ID(s) | Artifact | Repository location | Evidence state | Synthetic / production | Demonstrates | Evidence owner | Decision impact | Next review trigger |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `EV-AI003-001` | AI-003 — FeatherForecast | AI-003-R01; R02; R03 | FF-01–FF-04 | FeatherForecast Technical Security Validation Plan v1.0 | `11-assurance-testing-and-evaluation/06-technical-security-validation/AI-003-featherforecast/` | Designed | Synthetic | Twelve-case data-integrity, poisoning/backfill, training-serving skew, drift, forecast-integrity, approval, access, outage and rollback campaign with explicit assertions and governance limits | Cassandra Duckley — CISO | Authorizes bounded synthetic validation only; no score/gate/accuracy/effectiveness credit | Architecture/threat-model/test-scope change; failed assertion; scheduled review |
| `EV-AI003-002` | AI-003 — FeatherForecast | AI-003-R01; R02; R03 | FF-01–FF-04 | Executable FeatherForecast Lab v0.1.0 | `11-assurance-testing-and-evaluation/06-technical-security-validation/AI-003-featherforecast/lab/` | Synthetic technical implementation demonstrated | Synthetic | Deterministic source validation/quarantine, history integrity, schema/feature skew, version/change, drift, forecast integrity, approval, access, staleness and rollback mechanisms | Cassandra Duckley — CISO | Demonstrates bounded implementation only; production integration/effectiveness and forecast accuracy unverified | Lab/control version; architecture change; failed regression; production integration |
| `EV-AI003-003` | AI-003 — FeatherForecast | AI-003-R01; R02; R03 | FF-01–FF-04 | Baseline Findings and Remediation v1.0 | `11-assurance-testing-and-evaluation/06-technical-security-validation/AI-003-featherforecast/lab/findings/` | Synthetic failure detection / remediation demonstrated | Synthetic | Twelve deliberately seeded unsafe pipeline/decision states reproduced and remediated using the same bounded test model | Cassandra Duckley — CISO | Demonstrates harness sensitivity and remediation logic; no production-vulnerability or forecast-accuracy conclusion | Remediation change; reopened finding; failed regression; architecture/control change |
| `EV-AI003-004` | AI-003 — FeatherForecast | AI-003-R01; R02; R03 | FF-01–FF-04 | Hardened Campaign + Technical Security Test Report v1.1 | `11-assurance-testing-and-evaluation/06-technical-security-validation/AI-003-featherforecast/lab/reports/` | Synthetic operation tested | Synthetic | Same twelve cases move from 12/12 seeded failures to 12/12 hardened PASS; 10/10 unit tests and semantic verification PASS | Cassandra Duckley — CISO | Supports bounded synthetic operation testing only; Continue-with-monitoring decision remains | Lab/control version; failed regression; production evidence; incident; lifecycle review |
| `EV-AI003-005` | AI-003 — FeatherForecast | AI-003-R01; R02; R03 | FF-02; FF-03; FF-04; supporting FF-01 | Detection and Control-Signal Validation v1.0 | `11-assurance-testing-and-evaluation/06-technical-security-validation/AI-003-featherforecast/lab/reports/` | Synthetic detection / control-signal validation demonstrated | Synthetic | Source-integrity, backfill, skew/change, drift/data-quality discrimination, forecast-integrity, approval-denial, access-denial, outage/staleness and rollback signals | Cassandra Duckley — CISO | Demonstrates bounded observability/control signals; no production monitoring, SOC or forecast-performance effectiveness claim | Telemetry/detector change; missed expected event; production integration |
| `EV-AI003-006` | AI-003 — FeatherForecast | AI-003-R01; R02; R03 | FF-01–FF-04 | Commit-Bound GitHub Actions Replay + Retained Evidence Artifact | `.github/workflows/evidence-tests.yml`; run #191 | Synthetic commit-bound reproducibility demonstrated | Synthetic | Python 3.12.14 replay on `285b5bdedaef1295d9648c46e17a1aaef7b3428b` verifies source binding, 12 vulnerable failures, 12 hardened PASS, 10 unit tests, semantic assertions and retained artifact `10396704621` | Cassandra Duckley — CISO | Establishes commit-bound synthetic reproducibility only; no production/risk/gate/accuracy credit | Workflow/lab/control version; failed CI; artifact-policy change; production evidence |
| `EV-AI003-007` | AI-003 — FeatherForecast | AI-003-R01; AI-003-R03 | FF-01; FF-04 | `FFSEC-T008/T009` Manager-Approval & Decision-Record Integrity Result | `11-assurance-testing-and-evaluation/06-technical-security-validation/AI-003-featherforecast/lab/evidence/generated/hardened/FFSEC-T008.json`; `FFSEC-T009.json`; test report v1.1 | Synthetic approval/decision-mechanism evidence demonstrated | Synthetic | A material commitment is blocked without valid manager approval and tampered decision/override evidence is invalidated | Tobias Duckman — Director Supply Chain / Cassandra Duckley — CISO | Narrows uncertainty about mechanism design; **does not demonstrate FF-01 production operation and does not close IAF-2026-003** | Production-equivalent FF-01 population/period evidence; overrides/exceptions/metrics/owner review; independent validation |

No prior `EV-AI003-*` IDs existed in the master evidence index.

## 2. Current evidence population after reconciliation

| Metric | Result |
|---|---:|
| v1.8 base evidence records | 76 |
| AI-004 reconciliation records outside v1.8 | 6 |
| AI-002 reconciliation records outside v1.8 | 7 |
| AI-001 reconciliation records outside v1.8 | 7 |
| New AI-003 reconciliation records | 7 |
| Combined current evidence records | **103** |
| Available synthetic records | **97** |
| Not-available evidence records | **6** |
| Production-effectiveness conclusions supported | **0** |

## 3. Canonical replay metadata

| Field | Canonical value |
|---|---|
| Source commit | `285b5bdedaef1295d9648c46e17a1aaef7b3428b` |
| Workflow run | `#191` / `34971811660` |
| Job ID | `104389653093` |
| Python | `3.12.14` |
| Artifact | `featherforecast-security-evidence-285b5bdedaef1295d9648c46e17a1aaef7b3428b` |
| Artifact ID | `10396704621` |
| Artifact digest | `sha256:41ef49f1620d7c06fe3c3381c05f7a913be612895c08d36f47a18ef0554528ea` |
| Artifact size | `32,158 bytes` |
| Artifact retention expiry | `15 October 2026` |
| Uploaded artifact files | `29` |
| Hash-manifest covered files | `28`, excluding the manifest itself |
| Vulnerable profile | `0 PASS / 12 FAIL` |
| Hardened profile | `12 PASS / 0 FAIL` |
| Unit tests | `10/10 PASS` |
| Semantic verifier | `PASS` |

## 4. Evidence boundary

The new FeatherForecast evidence is synthetic and commit-bound. It can support claims of reproducible technical-control behavior in the defined lab only.

It cannot support:

- production FeatherForecast forecast accuracy;
- production poisoning resistance;
- universal drift detection or validated production drift thresholds;
- real Northstar platform security, configuration or supplier assurance;
- production data-lineage/integrity effectiveness;
- production `FF-01` manager-approval operation;
- real supplier/planning-data access-control effectiveness;
- sustained production availability/fallback/rollback effectiveness;
- legal compliance;
- production operating effectiveness;
- `IAF-2026-003` closure;
- residual-risk reduction; or
- a change to the Continue-with-monitoring governance position.

## 5. Consolidation rule

At the next full evidence-index consolidation, `EV-AI003-001`–`007` should be incorporated into the successor to v1.8 without changing their IDs or evidence-state conclusions.
