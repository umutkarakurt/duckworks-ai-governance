# Project W.I.N.G. — Technical AI Security Assurance Methodology

**Document ID:** DW-WING-SEC-METH-01  
**Version:** 1.0  
**Effective date:** 15 September 2026  
**Owner:** Cassandra Duckley — Chief Information Security Officer  
**Governance owner:** Eleanor Duckford — AI Governance Lead  
**Status:** Reusable Phase II methodology — portfolio practice, fictional / synthetic / non-production

> This methodology is a Duckworks recommended organizational practice. It is informed by the project's adopted standards/frameworks and technical references, but it is not itself a legal requirement, certification scheme, formal standard or substitute for independent assurance.

## 1. Purpose

This methodology defines the reusable assurance pattern developed through Phase II.

Its goal is to answer a disciplined question:

> **Can a material AI-security risk be translated into an enforceable system boundary, challenged under a controlled weak condition, retested after hardening, reproduced from repository state, and reconciled into governance without overstating what the evidence proves?**

The method treats an AI system as an end-to-end information system rather than as an isolated model.

## 2. Assurance chain

The canonical Phase II chain is:

> **Architecture → Threat → Security requirement → Deliberately weak baseline → Test → Raw evidence → Finding → Remediation → Same-test retest → Detection/control-signal validation → Commit-bound replay → Control conclusion → Risk / governance reconciliation**

Each stage has a different evidentiary purpose.

| Stage | Assurance question | Minimum output |
|---|---|---|
| Architecture | What exists, who/what crosses which trust boundary, and where can control be enforced? | components, identities, data flows, trust boundaries, assumptions, security invariants |
| Threat model | What can go wrong, by what path, and with what security consequence? | threat register, attack/failure paths, priority, affected assets/controls |
| Security requirement | What must the system enforce regardless of model confidence? | explicit machine-testable requirement |
| Weak baseline | Can a known unsafe condition be reproduced deliberately? | seeded vulnerable profile / fixture |
| Test | Can the defined condition be challenged repeatably? | test case with expected/actual result |
| Raw evidence | What exactly happened? | structured result, logs/telemetry, version/state, hashes |
| Finding | What failed and why does it matter? | bounded finding linked to threat/risk/control |
| Remediation | What boundary changed? | configuration/code/data/control change |
| Same-test retest | Does the original challenge now produce the intended safe outcome? | identical-case hardened result |
| Detection validation | Was the event observable, and is detection separate from prevention? | event/control signal and limitations |
| Commit-bound replay | Can the result be reproduced from exact repository state? | CI run, commit, artifact/digest |
| Control conclusion | What mechanism is now demonstrated? | narrow evidence-maturity statement |
| Governance reconciliation | What changes—and what deliberately does not? | evidence ID, risk/control overlay, gate/finding/assumption decision |

## 3. Entry criteria

A system-specific technical-assurance increment should not begin until the following are available:

1. a registered AI/use-case identifier;
2. named business and technical ownership;
3. current governance position;
4. relevant risk scenario(s);
5. existing control IDs where applicable;
6. system architecture sufficient to identify trust boundaries;
7. explicit authorization boundary for testing;
8. synthetic or otherwise authorized data;
9. a defined claim boundary; and
10. a documented reason for selecting the system.

A missing fact should be recorded as **TBD / not evidenced** or a labelled design assumption. It must not be replaced silently with plausible production detail.

## 4. Architecture rules

Architecture is assurance design evidence, not production proof.

A Phase II architecture should identify, where relevant:

- users and service identities;
- model/provider boundaries;
- data stores;
- ingestion/retrieval pipelines;
- APIs and gateways;
- human approval/release points;
- tool/connector privilege;
- build/dependency/provenance boundaries;
- monitoring and evidence stores;
- third-party services;
- fail-safe behavior; and
- known-good recovery state.

Every material trust boundary should have either:

- an enforceable security requirement;
- an explicit monitoring requirement;
- an accepted gap; or
- a reason it is out of scope.

## 5. Threat-model rules

Threat modelling must preserve separation between:

- enterprise risk rating;
- technical threat priority;
- legal/regulatory classification; and
- test urgency.

A P0/P1 technical threat does not automatically change an enterprise risk score.

Threat statements should identify:

**actor/failure → precondition/path → boundary/control failure → consequence**

The threat model should include both:

- conventional cybersecurity mechanisms; and
- AI/ML-specific attack/failure mechanisms where relevant.

## 6. Security-requirement rules

A requirement should describe a **system outcome**, not model politeness or a preferred answer.

Good requirement:

> Unauthorized content must not enter the permitted context/provider boundary.

Weak requirement:

> The model should refuse confidential questions.

Good requirement:

> A material purchase commitment cannot proceed without valid authorized manager approval.

Weak requirement:

> The forecast should recommend sensible quantities.

Requirements should remain enforceable even if the AI output is wrong, adversarial, overconfident or unavailable.

## 7. Two-profile test model

Each first-wave campaign uses the same logical cases against two profiles.

### Vulnerable profile

The weak profile deliberately seeds an unsafe or uncontrolled state.

Its purpose is to demonstrate that:

- the test is capable of detecting meaningful failure;
- the unsafe state is observable;
- the finding is not generated from a permanently passing harness; and
- remediation has a measurable before/after effect.

### Hardened profile

The hardened profile reruns the **same challenge** after a documented control change.

A PASS may mean:

- deny;
- quarantine;
- invalidate;
- block promotion;
- require re-review;
- enter manual/degraded mode;
- preserve human authority;
- restore known-good state; or
- otherwise fail safely.

A PASS does not have to mean “the model answered correctly.”

## 8. Prevention and detection are separate

Detection is not a substitute for a preventive or containment boundary.

Examples:

- prompt-injection detection does not replace authorization;
- DLP alerting does not replace minimization/access control;
- drift alerting does not replace validation/review;
- output-integrity logging does not replace invalidation;
- approval logging does not replace a release/commitment gate; and
- outage telemetry does not replace fail-safe/manual operation.

A detection result should record:

1. whether the challenge occurred;
2. whether expected telemetry existed;
3. whether the event should have matched;
4. whether it fired; and
5. what system outcome occurred even if detection missed.

## 9. Evidence schema

A material result should retain, where relevant:

- test ID;
- threat ID(s);
- risk ID(s);
- control ID(s);
- requirement ID(s);
- profile;
- architecture/threat/validation/lab versions;
- fixture/data/model/configuration/artifact versions;
- identity/authorization state;
- input or sanitized payload;
- expected result;
- actual result;
- detection/control signals;
- correlation ID;
- result classification;
- limitations;
- evidence SHA-256; and
- source commit when commit-bound.

System-specific fields may extend this schema.

## 10. Evidence-maturity ladder

The Phase II portfolio uses the following practical maturity ladder.

| Level | Evidence state | What it can support |
|---|---|---|
| M0 | Narrative / status assertion | design intent only |
| M1 | Architecture + requirement | testable design |
| M2 | Synthetic technical implementation | mechanism exists in bounded lab |
| M3 | Seeded failure reproduced | harness can expose defined unsafe condition |
| M4 | Same-test hardened PASS | remediation works for defined synthetic case |
| M5 | Detection/control-signal validation | defined event is observable or explicitly missed |
| M6 | Commit-bound reproducibility | result linked to exact repository state and retained evidence |
| M7 | Governance reconciliation | stable evidence ID and bounded control/risk conclusion |
| M8 | Production integration | real system/configuration/data boundary evidenced |
| M9 | Defined-period operating effectiveness | population, period, exceptions, metrics and owner review |
| M10 | Outcome effectiveness / independent assurance | real outcome evidence and/or sufficiently independent validation |

Phase II first-wave closure reaches **M7** for the selected technical increments.

It deliberately does not claim M8–M10.

## 11. Commit-bound reproducibility

Before canonical evidence allocation, a system increment should have:

- an exact source commit;
- automated campaign execution;
- automated unit/semantic assertions;
- `source_commit == GITHUB_SHA` or equivalent repository binding;
- machine-readable evidence;
- retained artifact/digest or equivalent immutable reference; and
- explicit false flags for claims not authorized by the test.

Later successful CI runs confirm continuing repository integrity but do not automatically replace the canonical reconciliation anchor.

## 12. Governance reconciliation rules

Technical PASS must not automatically:

- reduce a risk score;
- close an assumption;
- close an internal-audit finding;
- change a lifecycle/governance gate;
- establish legal compliance;
- establish product safety;
- establish supplier assurance; or
- create a production-effectiveness claim.

A reconciliation record should state:

1. what new evidence exists;
2. what control mechanism is demonstrated;
3. what remains unproven;
4. whether source-status labels change;
5. whether risk scores change;
6. whether assumptions/findings close;
7. the current governance position; and
8. what production evidence would be needed for a stronger claim.

## 13. Independence rule

Engineering teams may build controls and run engineering tests.

That does not make the result **independent assurance**.

A claim of independent validation requires sufficient separation of responsibility, scope, criteria, evidence review and conclusion from the people who designed/operated the control.

Internal Audit should not be treated as having independently assured a control merely because an internal-audit finding exists in the synthetic portfolio.

## 14. Change and retest triggers

A system-specific technical increment should be reassessed when there is a material change to:

- intended purpose;
- model/provider;
- data source or schema;
- feature pipeline;
- prompt/system configuration;
- tool/connector privilege;
- dependency/build chain;
- authorization model;
- human decision authority;
- product/safety role;
- hosting/subprocessor;
- security-control implementation;
- monitoring/detection design; or
- relevant regulatory classification.

A failed control, incident, adverse outcome, audit finding or evidence expiry can also trigger retest.

## 15. Closure criteria for a system increment

A synthetic system increment is complete when:

- architecture and threat model are documented;
- material P0/P1 threats have testable requirements or explicit gaps;
- vulnerable cases reproduce intended seeded failures;
- remediation is documented;
- hardened same-test retest passes defined assertions;
- detection/control signals are evaluated;
- evidence is machine-readable;
- repository replay is commit-bound;
- stable evidence IDs are allocated through governance reconciliation;
- limitations are explicit; and
- no unauthorized production/compliance/risk/gate claim is created.

## 16. Programme-level closure rule

The Phase II first-wave programme may be closed when:

- multiple materially different AI patterns have completed the system-level chain;
- cross-system coverage has been consolidated;
- a reusable methodology exists;
- open evidence gaps are explicit;
- future work is trigger-driven rather than artifact-count-driven; and
- the portfolio can explain what the technical work proves in a short reviewer path.

Closure is therefore a **scope-completion decision**, not a statement that all AI-security risk is resolved.
