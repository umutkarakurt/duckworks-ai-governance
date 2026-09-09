# AIMS Control Applicability

**Repository path:** `07-control-framework/01-aims-control-applicability/`  
**Milestone:** Project W.I.N.G. v1.6  
**Status:** Bounded synthetic control-applicability decision and validation demonstrated

This package converts the canonical control library into an inspectable applicability decision set:

**Risk or AIMS need → control → scope → applicability decision → rationale → owner → evidence state → required action → review trigger**

## Files

- `Duckworks_AIMS_Control_Applicability_Method_v1.0.md` — decision method, states, evidence rules and governance boundary.
- `Duckworks_AIMS_Control_Applicability_Register_v1.0.csv` — machine-readable authoritative register.
- `Duckworks_AIMS_Control_Applicability_Register_v1.0.xlsx` — formatted working register and management summary.
- `Duckworks_AIMS_Control_Applicability_Review_Record_CAR-2026-001.md` — synthetic human review and approval record.
- `aims_control_applicability_gate.py` — deterministic structural and semantic validation.
- `applicability_gate_config.json` — expected population and permitted decisions.
- `Duckworks_AIMS_Control_Applicability_Gate_Run_Summary.json` — reproducible gate output.

## Current result

- 45 canonical controls evaluated.
- 44 controls classified Applicable.
- `AI-TPR-01` classified Conditionally applicable.
- No control excluded.
- 9 controls have linked synthetic evidence after reconciliation.
- 36 controls have no linked evidence.
- `DD-01` and `FF-01` retain unsupported Implemented source labels and receive no additional risk credit.
- Zero structural validation failures.
- Human approval remains mandatory.

## Boundary

Applicability is not implementation, operation, effectiveness, legal compliance or ISO/IEC 42001 conformity. The executable gate cannot approve exclusions, accept risk, authorize deployment or close actions.

