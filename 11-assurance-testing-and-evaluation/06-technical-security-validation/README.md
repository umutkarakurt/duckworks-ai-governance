# Phase II Technical Security Validation

**Repository path:** `11-assurance-testing-and-evaluation/06-technical-security-validation/`  
**Status:** Phase II first-wave technical-assurance programme consolidated and closed at synthetic / commit-bound portfolio level — production effectiveness not established

[← Back to assurance, testing and evaluation](../README.md) · [← Main portfolio](../../README.md)

This folder contains reproducible security-validation plans, executable test implementations, failure/remediation evidence, same-test retesting, detection/control-signal validation and commit-bound replay evidence for selected Duckworks AI systems.

## Programme consolidation and closure

Start with these programme-level artifacts:

1. [`Duckworks_PhaseII_Technical_Assurance_Programme_Summary_v1.0.md`](Duckworks_PhaseII_Technical_Assurance_Programme_Summary_v1.0.md) — consolidated five-system result, quantitative view, canonical anchors and claim boundaries.
2. [`Duckworks_Cross_System_AI_Security_Control_and_Test_Matrix_v1.0.md`](Duckworks_Cross_System_AI_Security_Control_and_Test_Matrix_v1.0.md) — cross-system synthetic coverage by security/control theme.
3. [`Duckworks_Technical_AI_Security_Assurance_Methodology_v1.0.md`](Duckworks_Technical_AI_Security_Assurance_Methodology_v1.0.md) — reusable technical-assurance method and evidence-maturity ladder.
4. [`../../01-project-charter-and-context/02-objectives-and-scope/Duckworks_PhaseII_Technical_AI_Security_Assurance_Closure_Report_v1.0.md`](../../01-project-charter-and-context/02-objectives-and-scope/Duckworks_PhaseII_Technical_AI_Security_Assurance_Closure_Report_v1.0.md) — closure against original objectives/acceptance criteria and residual gaps.

Consolidated first-wave result:

- **5** differentiated AI-security system chains;
- **52** canonical campaign test cases;
- **52/52** deliberately seeded unsafe baseline outcomes reproduced;
- **52/52** hardened PASS outcomes;
- **40** supplemental automated unit tests;
- commit-bound replay for all five systems;
- **33** canonical technical-validation evidence records; and
- **0** production-effectiveness conclusions created from synthetic validation.

**Closure boundary:** first-wave build complete does not mean enterprise AI-security risk is resolved. Production integration/effectiveness, independent assurance and system-specific open findings/gaps remain visible.


## AI-006 PondGPT

PondGPT is the first completed Phase II technical-validation chain.

- 8/8 vulnerable seeded failures reproduced;
- 8/8 hardened PASS;
- commit-bound replay completed;
- canonical evidence reconciled as `EV-AI006-017–022`; and
- production effectiveness remains unverified.

See [`AI-006-pondgpt/`](AI-006-pondgpt/).

## AI-004 WingInspect Vision

WingInspect is the second completed Phase II technical-validation increment.

- vulnerable: 0 PASS / 8 FAIL;
- hardened: 8 PASS / 0 FAIL;
- commit-bound replay completed;
- AI-004 evidence reconciled as `EV-AI004-006–011`; and
- production effectiveness remains unverified.

See [`AI-004-winginspect/`](AI-004-winginspect/).

## AI-002 QuackBot

QuackBot is the third completed Phase II technical-validation increment and the first explicitly internet-facing customer-service RAG/API case.

Canonical result:

- vulnerable: **0 PASS / 12 FAIL**;
- hardened: **12 PASS / 0 FAIL**;
- unit tests: **8/8 PASS**;
- QuackBot semantic verifier: PASS;
- `QB-COMP-001`: PASS;
- commit `25525cc2c09c6b6557ddb9e7706fdaf81ce1796f`;
- run #147 / `34946047428`;
- retained artifact `quackbot-security-evidence-25525cc2c09c6b6557ddb9e7706fdaf81ce1796f`; and
- evidence reconciled as `EV-AI002-001–007`.

The interaction-disclosure assertion is kept separate from the twelve adversarial-security tests and does not establish full legal compliance.

See [`AI-002-quackbot/`](AI-002-quackbot/).

## AI-001 DuckDesign AI

DuckDesign is the fourth Phase II technical-security target and the first dedicated **engineering / generated-code / software-supply-chain / build-provenance / tool-privilege** case.

Canonical result:

- `DDSEC-T001`–`DDSEC-T012`;
- vulnerable: **0 PASS / 12 FAIL**;
- hardened: **12 PASS / 0 FAIL**;
- unit tests: **10/10 PASS**;
- semantic verifier: **PASS**;
- commit `1c1fd170347dff466eb9d4a670e4355905119be2`;
- run #166 / `34961107816`;
- retained artifact `duckdesign-security-evidence-1c1fd170347dff466eb9d4a670e4355905119be2`;
- evidence reconciled as `EV-AI001-001–007`; and
- `IAF-2026-002`: **remains open**.

Primary target controls:

- `DD-01 — Competent Engineer Approval`;
- `DD-02 — Independent Safety Validation Gate`;
- `DD-03 — Engineering Benchmark & Regression Suite`;
- `DD-04 — Engineering Data Boundary & DLP`; and
- `DD-05 — Design/Model Version Traceability`.

The commit-bound lab and reconciliation demonstrate bounded synthetic technical behavior only. They do not prove that `DD-01` operates in a production or production-equivalent process and therefore do not close the open High audit finding.

See [`AI-001-duckdesign/`](AI-001-duckdesign/).

## AI-003 FeatherForecast

FeatherForecast is the fifth Phase II technical-security target and the first dedicated **predictive-ML data integrity / poisoning / drift / operational decision-resilience** case.

Canonical result:

- `FFSEC-T001`–`FFSEC-T012`;
- vulnerable: **0 PASS / 12 FAIL**;
- hardened: **12 PASS / 0 FAIL**;
- unit tests: **10/10 PASS**;
- semantic verifier: **PASS**;
- commit `285b5bdedaef1295d9648c46e17a1aaef7b3428b`;
- run #191 / `34971811660`;
- retained artifact `featherforecast-security-evidence-285b5bdedaef1295d9648c46e17a1aaef7b3428b`;
- evidence reconciled as `EV-AI003-001–007`; and
- `IAF-2026-003`: **remains open**.

Primary target controls:

- `FF-01 — Human Planning Approval & Override`;
- `FF-02 — Back-Testing, Stress Testing & Challenger Review`;
- `FF-03 — Automated Drift Alerts & Retraining Trigger`; and
- `FF-04 — Supplier/Planning Data Access & Logging`.

The commit-bound lab and reconciliation demonstrate bounded synthetic pipeline/control behavior only. They do not prove production forecast accuracy, real poisoning resistance, Northstar security, sustained drift monitoring or production `FF-01` operation.

See [`AI-003-featherforecast/`](AI-003-featherforecast/).
## Evidence chain

**Risk → Threat → Security requirement → Deliberately weak baseline → Test → Raw evidence → Finding → Remediation → Same-test retest → Detection/control-signal validation → Commit-bound replay → Control conclusion → Risk/gate reconciliation**

## Evidence boundary

A successful synthetic validation chain does not establish production operation, product safety, product/machinery conformity, legal compliance, ISO conformity/certification, independent assurance or residual-risk reduction.

No lifecycle gate changes automatically from local/CI test success.

## Phase II closure / future trigger

The planned first-wave Phase II build is **closed**.

Do not add another system-specific synthetic campaign solely to increase coverage counts.

Reopen or extend technical assurance when there is a documented trigger such as:

- a new AI system with a materially new threat class;
- a material architecture/model/provider/data/tool/use change;
- an incident or control failure;
- production or production-equivalent evidence becoming available;
- an open finding requiring technical validation;
- an independent-review request; or
- a genuine portfolio/hiring credibility gap.

Potential future scope candidates include AI-007 shadow-GenAI discovery/containment, model extraction/privacy attacks, multi-agent trust, autonomous external-action safety, or production MLOps/cloud assurance—but none is a Phase II closure blocker.
