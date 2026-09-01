# AI-004 — WingInspect Vision Operating Evidence Package

This package demonstrates how a material AI risk is translated into an operating control and an auditable evidence trail.

## Evidence Chain

**AI-004 WingInspect Vision**  
↓  
**AI-004-R01 — Missed material manufacturing defect**  
↓  
**WI-01 — Qualified Human Final Inspection**  
↓  
**Mandatory Human Release Gate — worked operating mechanism**  
↓  
**Synthetic inspection execution records**  
↓  
**Control test**  
↓  
**Monitoring and production-evidence requirements**

## Files

### 1. Control Implementation Card

[`AI-004_Control_Implementation_Card_Human_Release_Gate.md`](./AI-004_Control_Implementation_Card_Human_Release_Gate.md)

Operationalizes the existing canonical control `WI-01 — Qualified Human Final Inspection` as a Mandatory Human Release Gate and defines its risk, performer, process owner, trigger, evidence, and effectiveness measurement.

### 2. Synthetic Inspection Log

[`AI-004_2026-09-01_APPROVAL_WingInspect_Inspection_Log_Sample.csv`](./AI-004_2026-09-01_APPROVAL_WingInspect_Inspection_Log_Sample.csv)

Contains synthetic inspection events demonstrating:

- qualified human review;
- accept/reject authority;
- human disagreement with AI output;
- documented overrides;
- timestamps; and
- final release/block decisions.

### 3. Control Test Record

[`AI-004_2026-09-01_MON_Human_Release_Gate_Control_Test.md`](./AI-004_2026-09-01_MON_Human_Release_Gate_Control_Test.md)

Tests the complete synthetic population against the `WI-01` human-final-inspection requirements as operationalized through the Mandatory Human Release Gate.

## Portfolio Disclaimer

All records in this package are synthetic and created solely for portfolio demonstration.

They do not represent real Duckworks manufacturing activity, actual model accuracy, measured defect rates, or validated production control effectiveness.
