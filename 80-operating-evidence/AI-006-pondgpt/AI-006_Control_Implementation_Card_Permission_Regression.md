# AI-006 PondGPT — Control Implementation Card

| **Field** | **Value** |
|---|---|
| **Document ID** | DW-POND-PG02-IMPL-01 |
| **Version / date** | 1.0 / 1 September 2026 |
| **AI system** | AI-006 — PondGPT |
| **Linked risk** | AI-006-R01 — Privacy & data governance |
| **Preventive dependency** | PG-01 — Permission-Aware Retrieval |
| **Control demonstrated** | PG-02 — Automated Permission Regression & DLP Tests |
| **Control type** | Detective |
| **Operating owner** | Oliver Duckett — Head of IT & Cloud |
| **Evidence status** | Synthetic technical implementation demonstration |
| **Production evidence** | Not available |
| **Classification** | Portfolio / Synthetic / Non-production |

## 1. Risk

Because retrieval permissions, connector ACL mappings, or authorization synchronization can be configured incorrectly, PondGPT may return restricted internal information to a user who is not authorized to access the underlying source, causing sensitive IP, employee, customer, or other confidential information to cross access boundaries.

## 2. Control

`PG-02 — Automated Permission Regression & DLP Tests` detects authorization drift or sensitive-source exposure after connector, permission, or configuration changes.

The control validates the preventive `PG-01 — Permission-Aware Retrieval` boundary by running a versioned test suite containing:

- authorized personas and positive access assertions;
- unauthorized personas and negative access assertions;
- synthetic sensitive records;
- DLP/exclusion assertions;
- entitlement-removal regression cases;
- intentionally seeded ACL/configuration defects;
- alert-generation expectations; and
- connector/corpus expansion gate expectations.

A material permission-regression failure must create an actionable exception and block connector/corpus expansion until remediation and successful retest.

## 3. Operating owner

**Oliver Duckett — Head of IT & Cloud**

The operating owner is responsible for the PondGPT identity, connector, retrieval, permission-synchronization, and test workflow represented by this control.

**Security challenge:** Cassandra Duckley — Chief Information Security Officer may independently challenge security design, alerting, and evidence. Internal Audit remains independent assurance and does not operate this control.

## 4. Trigger / frequency

The control is designed to operate:

- on every material connector change;
- on source-system permission/entitlement changes;
- on material PondGPT retrieval-policy or configuration changes;
- before expansion to a new repository/corpus;
- weekly as an automated regression suite; and
- after remediation of a permission or DLP failure.

## 5. Evidence produced

Expected evidence includes:

- versioned authorization matrix;
- test-persona identity/group assignments;
- synthetic test records;
- positive and negative permission assertions;
- DLP/exclusion assertions;
- permission-change synchronization results;
- connector ACL configuration/version;
- regression execution log;
- alert/security-event record;
- exception/failure ticket;
- evidence that connector/corpus expansion was blocked where required;
- remediation record; and
- successful retest before closure.

The worked synthetic evidence is stored in this package.

## 6. Effectiveness metrics

### Primary KCI — Permission Regression Assertion Conformance

**Formula**

`Assertions whose actual result matches the expected result / total executed assertions × 100`

For deliberately seeded faults, the expected result includes **detection, alerting, and expansion blocking**. A seeded authorization defect is not counted as a control failure when PG-02 detects and contains it as designed.

**Synthetic worked-example result:** 20 / 20 expected outcomes = **100%**

### Supporting KCI — Critical Failure Gate Enforcement

`Critical detected permission/DLP failures that block connector or corpus expansion / total critical detected permission/DLP failures × 100`

**Synthetic worked-example result:** 1 / 1 = **100%**

### Supporting KCI — DLP / Exclusion Enforcement

`DLP or pilot-exclusion assertions correctly enforced / total DLP or exclusion assertions × 100`

**Synthetic worked-example result:** 3 / 3 = **100%**

### Outcome KRI — Unauthorized Retrieval Escape Rate

`Confirmed unauthorized retrieval events that escape preventive/detective controls / total production retrieval events × 100`

**Production result:** Not evidenced.

This KRI is intentionally separate from test-suite conformance. A perfect synthetic regression run does not demonstrate zero production data leakage.

## 7. Current conclusion

The package demonstrates:

- a defined technical authorization boundary;
- positive and negative authorization testing;
- change-triggered permission regression;
- DLP/exclusion testing;
- deliberate fault injection;
- detection and exception creation;
- connector/corpus expansion blocking;
- remediation and retest; and
- an auditable technical evidence trail.

It does **not** demonstrate actual PondGPT architecture, actual enterprise authorization inheritance, actual production DLP enforcement, sustained operation, or production operating effectiveness.

**Evidence state:**  
**Designed → Synthetic technical implementation demonstrated → Synthetic technical execution demonstrated → Synthetic operation tested**

**Not evidenced:**  
**Production authorization validated → Sustained operating effectiveness → Independent assurance**


## 8. Executable implementation artifact

The synthetic control design is implemented as [`pg02_permission_regression_test.py`](pg02_permission_regression_test.py), with test metadata in [`pg02_test_config.json`](pg02_test_config.json).

The script is intentionally technology-neutral and uses only Python standard-library functionality. In a production implementation, the same control logic would require adapters to actual identity, source ACL, RAG connector, DLP/SSE/CASB, logging/SIEM, and change-management systems.

The executable artifact strengthens the evidence state from a documentation-only control to a **reproducible synthetic technical control demonstration**. It does not change the production evidence boundary.
