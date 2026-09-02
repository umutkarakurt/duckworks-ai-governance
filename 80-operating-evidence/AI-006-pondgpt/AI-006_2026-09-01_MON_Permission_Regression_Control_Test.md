# AI-006 PondGPT — PG-02 Permission Regression & DLP Control Test

| **Field** | **Value** |
|---|---|
| **Document ID** | DW-POND-PG02-TEST-01 |
| **Version / test date** | 1.0 / 1 September 2026 |
| **AI system** | AI-006 — PondGPT |
| **Risk** | AI-006-R01 — Privacy & data governance |
| **Preventive boundary** | PG-01 — Permission-Aware Retrieval |
| **Control tested** | PG-02 — Automated Permission Regression & DLP Tests |
| **Control owner** | Oliver Duckett — Head of IT & Cloud |
| **Test population** | 20 synthetic regression assertions across baseline, permission-change, DLP/exclusion, seeded-defect and remediation runs |
| **Evidence classification** | Portfolio / Synthetic / Non-production |

## 1. Control objective

Determine whether the worked `PG-02` regression process can identify authorization drift or sensitive-source exposure and prevent connector/corpus expansion until material failures are remediated.

The test does not evaluate actual PondGPT production architecture. It evaluates the **synthetic control logic and evidence chain**.

## 2. Expected control behavior

The control is considered to operate as designed within the synthetic population when:

1. authorized personas can retrieve permitted connected sources;
2. unauthorized personas cannot retrieve sources outside their source-system entitlements;
3. repositories excluded from the pilot remain inaccessible even to otherwise entitled users;
4. DLP-tagged synthetic sensitive content is blocked as specified;
5. permission removal/addition is reflected in regression results;
6. a seeded authorization defect is detected;
7. the seeded defect creates an alert and exception;
8. connector/corpus expansion is blocked while the material exception remains unresolved;
9. remediation restores the intended authorization boundary; and
10. expansion is reopened only after successful retest.

## 3. Population and sampling

**Population tested:** 20 synthetic test assertions.

**Sampling method:** Full-population test. No statistical sample was used.

The population includes:

- 6 baseline positive/negative authorization assertions;
- 2 pilot-exclusion assertions;
- 2 DLP assertions;
- 2 entitlement-change assertions;
- 3 seeded-defect / blocked-gate assertions;
- 4 remediation/retest assertions; and
- 1 post-remediation weekly regression assertion.

## 4. Test results

| **Test area** | **Population** | **Expected outcomes met** | **Result** |
|---|---:|---:|---|
| Baseline positive/negative authorization | 6 | 6 | Pass |
| Pilot repository exclusions | 2 | 2 | Pass |
| DLP enforcement | 2 | 2 | Pass |
| Permission-change synchronization | 2 | 2 | Pass |
| Seeded authorization-defect detection / containment | 3 | 3 | Pass |
| Remediation and gate-release retest | 4 | 4 | Pass |
| Post-remediation weekly regression | 1 | 1 | Pass |
| **Total** | **20** | **20** | **Pass** |

### 4.1 Deliberate authorization defect

`PG02-T013` intentionally introduces a connector ACL defect for `DOC-FIN-001 — Quarterly Cash Forecast Draft`.

The synthetic source-system policy requires the `Finance` group, but the seeded connector mapping exposes the source to `All-Employees`.

**Observed behavior:**

- General Employee retrieval: **ALLOW**
- Expected policy result: **DENY**
- PG-02 detection: **Yes**
- Alert generated: **Yes**
- Exception: `SEC-EXC-006-001`
- Connector/corpus expansion gate: **Blocked**

This is treated as a **successful detective-control assertion**, because the purpose of PG-02 is to detect permission drift and prevent expansion until remediation.

The underlying seeded configuration itself is defective; the detective control is considered successful because it identifies and contains that defect.

### 4.2 Remediation

The Finance connector ACL mapping is corrected and the relevant assertions are re-run.

The remediation run confirms:

- General Employee → Finance document: **DENY**
- Finance User → Finance document: **ALLOW**
- DLP regression: **PASS**
- Expansion gate: reopened only after the remediation run completed successfully.

## 5. Metrics

### Permission Regression Assertion Conformance

`20 expected outcomes met / 20 executed assertions × 100 = 100%`

### Seeded Unauthorized-Exposure Detection Rate

`1 detected seeded unauthorized exposure / 1 seeded unauthorized exposure × 100 = 100%`

### Critical Failure Gate Enforcement

`1 critical detected authorization failure that blocked expansion / 1 critical detected authorization failure × 100 = 100%`

### DLP / Pilot-Exclusion Enforcement

There are four exclusion/DLP-related execution rows in the full log. For the Control Implementation Card's focused KCI, the three substantive protection cases are:

- HR Restricted pilot exclusion;
- Engineering Highly Confidential DLP block; and
- Synthetic credential DLP block.

`3 correctly enforced / 3 tested substantive protection cases × 100 = 100%`

The Security Restricted exclusion is retained in the execution log as an additional corroborating exclusion case.

## 6. Exception analysis

| **Exception ID** | **Condition** | **Severity in synthetic test** | **Control response** | **Closure condition** | **Status** |
|---|---|---|---|---|---|
| SEC-EXC-006-001 | Finance source mapped to All-Employees at connector layer | Material authorization failure | Alert + expansion block + remediation test | Correct ACL mapping and full affected regression subset passes | Closed in synthetic demonstration |

No uncontrolled exception remains open in the synthetic test population.

## 7. Control-test conclusion

**Assessment:** `PG-02 — Automated Permission Regression & DLP Tests` operated as designed **within the synthetic test population**.

The evidence demonstrates that the proposed detective control can:

- exercise positive and negative permission assertions;
- validate entitlement changes;
- enforce synthetic DLP and pilot-source exclusions;
- detect a deliberately seeded authorization defect;
- generate an actionable exception;
- block expansion while the defect is unresolved; and
- require successful remediation testing before reopening the gate.

## 8. Assurance limitations

This result does **not** establish:

- actual PondGPT source-system authorization inheritance;
- actual LanternMind tenant isolation or provider data-use behavior;
- real identity-provider synchronization;
- real DLP/SSE/CASB operation;
- actual production connector ACLs;
- actual alert/SIEM integration;
- sustained weekly operation;
- real unauthorized-retrieval escape rate;
- actual reduction in current residual risk; or
- independent assurance.

`ASM-009` remains an open critical assumption.

The synthetic system inventory also identifies `ASM-030` as an open critical assumption concerning enterprise controls, tenant isolation/no provider training, and source-system authorization inheritance. This worked test does not validate that assumption as a production fact.

## 9. Production evidence required for stronger assurance

A real operating-effectiveness conclusion would require evidence such as:

- current architecture and connector inventory;
- identity-provider/group claims and source ACL mappings;
- service-account and privileged-connector review;
- source-system authorization test results;
- actual scheduled PG-02 execution logs over a defined period;
- DLP/SSE/CASB events;
- SIEM/security alerts and linked tickets;
- change records proving regression is triggered by permission/connector changes;
- actual failed-test gate enforcement;
- remediation and closure evidence;
- sensitive-source exclusion configuration;
- model/application/configuration version traceability; and
- periodic independent or second-line reperformance.

## 10. Evidence state

**Demonstrated:**  
**Designed → Synthetic technical execution demonstrated → Synthetic control operation tested**

**Not demonstrated:**  
**Production authorization validated → Sustained operating effectiveness → Validated risk reduction → Independent assurance**
