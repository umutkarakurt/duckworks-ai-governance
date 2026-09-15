# DuckDesign Software-Supply-Chain / Generated-Code / Tool-Privilege Security Lab

**Lab version:** `duckdesign-lab-0.1.0`  
**System:** AI-001 — DuckDesign AI  
**Status:** deterministic synthetic / non-production

This lab implements `DDSEC-T001`–`DDSEC-T012` from `DW-AI001-TM-01 v1.0` using only the Python standard library.

The objective is **system-control validation**, not demonstration that a particular foundation model generates universally secure engineering output or code.

## Profiles

**Vulnerable:** deliberately reproduces twelve unsafe outcomes across engineering-data leakage, imported-instruction trust, generated-code execution, dependency resolution/integrity, tool privilege, engineering validation, safety-gate bypass, approval integrity, material change, provenance and recovery.

**Hardened:** reruns identical cases with deterministic minimization/redaction, untrusted-content separation, staging/scanning/sandboxing, approved dependencies, hash checks, tool/egress denial, engineering validation, independent safety gate, approval-to-hash binding, change regression, provenance requirements and known-good rollback.

## Commands

```bash
python scripts/run_campaign.py
python -m unittest discover -s tests -p "test_*.py"
python scripts/ci_verify.py
python scripts/build_hash_manifest.py
```

## Expected local result

- vulnerable: **0 PASS / 12 FAIL**
- hardened: **12 PASS / 0 FAIL**
- unit tests: **10/10 PASS**
- semantic verifier: **PASS**
- `source_commit`: `LOCAL_UNBOUND`
- `production_effectiveness_claim`: `false`
- `product_safety_claim`: `false`
- `risk_score_change_authorized`: `false`
- `pilot_gate_change_authorized`: `false`
- `evidence_id_allocation_authorized`: `false`
- `iaf_2026_002_closure_authorized`: `false`

## Important safety/testing boundary

The lab does not execute destructive payloads against real systems.

Generated-code and tool-abuse cases are deterministic policy simulations. They demonstrate whether the synthetic control logic would allow, deny, quarantine or block a request/artifact.

## Evidence boundary

The lab does not demonstrate:

- production DuckDesign security;
- real AetherForge security or contractual compliance;
- real package/build/sandbox integrity;
- real CAD/simulation tool controls;
- product safety;
- machinery/product conformity;
- legal compliance; or
- operating effectiveness.

No `EV-AI001-*` IDs should be allocated until a clean commit-bound repository replay succeeds.

`IAF-2026-002` remains open.
