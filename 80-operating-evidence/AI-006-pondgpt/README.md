# AI-006 PondGPT — Permission Regression & DLP Operating-Evidence Demonstration

**AI system:** `AI-006 — PondGPT`  
**Primary risk:** `AI-006-R01 — Privacy & data governance`  
**Preventive boundary:** `PG-01 — Permission-Aware Retrieval`  
**Detective control demonstrated:** `PG-02 — Automated Permission Regression & DLP Tests`  
**Current governance gate:** Restricted pilot only  
**Evidence classification:** Portfolio / Synthetic / Non-production

## Purpose

This package demonstrates how Project W.I.N.G. can translate PondGPT's material authorization risk into a technical control-evidence chain:

**AI-006-R01 → PG-01 preventive authorization boundary → PG-02 detective validation → authorization matrix → automated-style regression execution → detected exception → remediation retest → control-test conclusion**

The package is deliberately different from the WingInspect worked example. It focuses on **technical access-control assurance**, not a human approval gate.

## Risk context

PondGPT is an internal enterprise LLM/RAG assistant. The material risk addressed here is that retrieval permissions or connector authorization could be misconfigured, causing PondGPT to return restricted internal information to a user who is not entitled to the underlying source.

The Duckworks target treatment for this scenario includes automated permission-regression tests, DLP, sensitive-source restrictions, and logging/alerting.

## Control relationship

### PG-01 — Permission-Aware Retrieval

Preventive control. PondGPT retrieval should inherit source-system authorization and deny cross-user or cross-role access. Restricted repositories remain excluded until permission inheritance is verified.

### PG-02 — Automated Permission Regression & DLP Tests

Detective control. A versioned test suite should use authorized and unauthorized personas plus synthetic sensitive records to identify authorization drift or DLP failure after connector, permission, or configuration changes.

This worked example demonstrates `PG-02` against the intended `PG-01` boundary.

## Evidence in this package

1. [`AI-006_Control_Implementation_Card_Permission_Regression.md`](AI-006_Control_Implementation_Card_Permission_Regression.md)  
   Defines the control objective, owner, trigger, evidence, decision rule, and metrics.

2. [`AI-006_Synthetic_Authorization_Matrix.csv`](AI-006_Synthetic_Authorization_Matrix.csv)  
   Defines synthetic personas, source repositories, source-system entitlements, pilot exclusions, and DLP restrictions.

3. [`AI-006_2026-09-01_SEC_Permission_Regression_Test_Log.csv`](AI-006_2026-09-01_SEC_Permission_Regression_Test_Log.csv)  
   Contains the synthetic test execution, including positive access, negative access, permission-change regression, DLP enforcement, one seeded connector-ACL defect, detection, blocking, remediation, and retest.

4. [`AI-006_2026-09-01_MON_Permission_Regression_Control_Test.md`](AI-006_2026-09-01_MON_Permission_Regression_Control_Test.md)  
   Assesses whether the control operated as designed within the synthetic test population.

## Deliberate seeded defect

The test population is not designed so that every authorization configuration is conveniently correct.

One synthetic connector configuration intentionally maps a Finance-restricted source to `All-Employees`. The regression suite detects that a General Employee can retrieve the source when the source-system policy says access should be denied. The test therefore:

- creates an exception;
- produces a security alert;
- blocks connector/corpus expansion;
- applies a corrected ACL mapping; and
- performs a successful remediation retest.

The control is being evaluated on whether it **detects and contains authorization drift**, not on whether the synthetic environment contains zero seeded faults.

## Assumption boundary

Two PondGPT assumptions remain material:

- `ASM-009` — PondGPT should not grant access to content a user could not otherwise access.
- `ASM-030` — the synthetic system inventory assumes PondGPT retrieval permissions inherit authorization from source systems and that the enterprise provider arrangement provides tenant isolation/no provider training.

This package improves the design and synthetic technical evidence around those assumptions. It does **not** validate them as production facts.

## Evidence maturity

Current demonstrated state:

**Designed → Synthetic technical execution demonstrated → Synthetic control operation tested**

Not demonstrated:

**Production authorization validated → Sustained operating effectiveness → Independent assurance**

## Assurance limitation

> **Synthetic control-execution evidence created solely for portfolio demonstration. It does not represent actual Duckworks, PondGPT, LanternMind, identity-provider, DLP, connector, or production activity.**

The package does not establish actual production permission inheritance, actual DLP effectiveness, real data-loss prevention, sustained permission synchronization, real alerting, or reduction of current PondGPT residual risk.

Accordingly, this package should not by itself change PondGPT's current **High (12)** residual-risk position, **Partially Effective** system control status, or restricted-pilot governance gate.


## Executable control demonstration

This package now includes a runnable synthetic implementation of `PG-02`:

- [`pg02_test_config.json`](pg02_test_config.json) — personas, control metadata, triggers, and seeded defect definition.
- [`pg02_permission_regression_test.py`](pg02_permission_regression_test.py) — deterministic Python control logic using only the standard library.
- [`AI-006_2026-09-01_SEC_Permission_Regression_Exception.json`](AI-006_2026-09-01_SEC_Permission_Regression_Exception.json) — generated exception evidence for the seeded Finance ACL defect.
- [`AI-006_2026-09-01_SEC_Permission_Regression_Run_Summary.json`](AI-006_2026-09-01_SEC_Permission_Regression_Run_Summary.json) — generated execution summary.

### Run locally

From this folder:

```bash
python pg02_permission_regression_test.py
```

The script reads the synthetic authorization matrix and configuration, executes the 20 control assertions, detects the deliberately seeded authorization defect, generates an exception, enforces the synthetic expansion gate, performs remediation/retest logic, and rewrites the execution evidence files.

No third-party Python packages or network access are required.

### Important interpretation

The script demonstrates that the **control logic is executable and evidence-producing**. It does not establish that real PondGPT production connectors, identity groups, DLP enforcement, SIEM integration, or source-system permissions operate this way.
