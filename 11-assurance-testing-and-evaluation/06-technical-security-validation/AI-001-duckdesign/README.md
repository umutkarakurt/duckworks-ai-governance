# AI-001 DuckDesign AI — Technical Security Validation

**System:** AI-001 — DuckDesign AI  
**Current governance gate:** **Restricted Pilot only**  
**Validation target:** `DD-01`–`DD-05`, with supporting `AI-GOV-02`, `AI-TPR-01` and `AI-INC-01` boundaries  
**Status:** deterministic synthetic lab v0.1.0 commit-bound replay completed; canonical evidence reconciliation completed

## Current artifacts

- [`Duckworks_DuckDesign_Technical_Security_Validation_Plan_v1.0.md`](Duckworks_DuckDesign_Technical_Security_Validation_Plan_v1.0.md)
- [`lab/`](lab/)
- [`lab/findings/Duckworks_DuckDesign_Baseline_Findings_and_Remediation_v1.0.md`](lab/findings/Duckworks_DuckDesign_Baseline_Findings_and_Remediation_v1.0.md)
- [`lab/reports/Duckworks_DuckDesign_Detection_and_Control_Signal_Validation_v1.0.md`](lab/reports/Duckworks_DuckDesign_Detection_and_Control_Signal_Validation_v1.0.md)
- [`lab/reports/Duckworks_DuckDesign_Technical_Security_Test_Report_v1.1.md`](lab/reports/Duckworks_DuckDesign_Technical_Security_Test_Report_v1.1.md)
- [`../../../80-operating-evidence/AI-001-duckdesign/Duckworks_DuckDesign_Evidence_Reconciliation_Record_v1.0.md`](../../../80-operating-evidence/AI-001-duckdesign/Duckworks_DuckDesign_Evidence_Reconciliation_Record_v1.0.md)

## Current commit-bound result

- vulnerable: **0 PASS / 12 FAIL**
- hardened: **12 PASS / 0 FAIL**
- unit tests: **10/10 PASS**
- semantic verifier: **PASS**
- Python: `3.12.14`
- source commit: `1c1fd170347dff466eb9d4a670e4355905119be2`
- Evidence reproducibility run: **#166 / `34961107816`**
- retained artifact: `duckdesign-security-evidence-1c1fd170347dff466eb9d4a670e4355905119be2`
- artifact ID: `10393790467`
- artifact digest: `sha256:fec7f78a7077d66890b9d00897eaf0bd21948a754912db77db89b7b1fa31edcb`
- artifact retention expiry: **15 October 2026**
- `production_effectiveness_claim=false`
- `product_safety_claim=false`
- `legal_compliance_claim=false`
- `risk_score_change_authorized=false`
- `pilot_gate_change_authorized=false`
- `evidence_id_allocation_authorized=false`
- `iaf_2026_002_closure_authorized=false`
- `assumption_closure_authorized=false`

## Interpretation

The lab tests **system and engineering boundaries**, not whether the model “behaves well.”

Examples:

- defined engineering-IP/secrets do not cross prohibited provider/log boundaries;
- imported content cannot alter validation/tool authority;
- generated code is staged/scanned and denied prohibited execution;
- unapproved dependencies do not resolve;
- package/hash mismatches block builds;
- CAD/simulation tool privilege and arbitrary egress are denied;
- unsafe engineering values fail independent validation;
- required safety validation cannot be bypassed;
- engineer approval is bound to an exact artifact hash;
- material changes trigger regression;
- incomplete provenance blocks promotion; and
- known-good rollback is verifiable.

## DD-01 / internal-audit boundary

The synthetic approval mechanism does **not** close `IAF-2026-002`.

Production or production-equivalent operating evidence for `DD-01` is still absent.

## Evidence maturity

Demonstrated:

**Designed → Synthetic technical implementation → Seeded failure reproduction → Hardened synthetic operation tested → Detection/control-signal validation → Commit-bound reproducibility → Canonical evidence reconciliation**

Not yet demonstrated:

**Production integration → Defined-period operating effectiveness → Product/outcome effectiveness → Independent assurance**

## Reconciled evidence IDs

`EV-AI001-001`–`EV-AI001-007` are now the stable evidence IDs for this first executable DuckDesign validation increment.

They cover the validation plan, executable lab, seeded findings/remediation, commit-bound hardened campaign, detection/control-signal validation, retained CI artifact, and the narrow `DDSEC-T009` exact-artifact approval-binding result.

## Next step

The DuckDesign first-wave technical-security increment is now reconciled.

The next evidence requirement is **production or production-equivalent operating evidence**, especially for `DD-01` and the open High finding `IAF-2026-002`.

A future broader-use decision would require real/production-equivalent approval populations, independent safety-validation records, benchmark/regression outcomes, engineering-data/provider evidence, version/provenance/change records, exceptions, metrics, owner review and independent assurance.

`ASM-007`, `ASM-020` and `ASM-025` remain open, `IAF-2026-002` remains open, and DuckDesign remains **Restricted Pilot only**.
