# AI-004 WingInspect Vision — Technical Security Validation

**System:** AI-004 — WingInspect Vision  
**Current governance gate:** Restricted pilot only  
**Validation target:** `WI-02`, `WI-04`, `WI-06`; supporting boundary `WI-01`  
**Status:** Deterministic synthetic lab v0.1.0 locally and commit-bound replayed; full workflow rerun pending after semantic-assertion fix

## Current artifacts

- [`Duckworks_WingInspect_Technical_Security_Validation_Plan_v1.0.md`](Duckworks_WingInspect_Technical_Security_Validation_Plan_v1.0.md)
- [`lab/`](lab/)
- [`lab/reports/Duckworks_WingInspect_Technical_Security_Test_Report_v1.0.md`](lab/reports/Duckworks_WingInspect_Technical_Security_Test_Report_v1.0.md)
- [`lab/findings/Duckworks_WingInspect_Baseline_Findings_and_Remediation_v1.0.md`](lab/findings/Duckworks_WingInspect_Baseline_Findings_and_Remediation_v1.0.md)
- [`lab/reports/Duckworks_WingInspect_Detection_Validation_v1.0.md`](lab/reports/Duckworks_WingInspect_Detection_Validation_v1.0.md)

## Current local result

- Vulnerable profile: **0 PASS / 8 FAIL**
- Hardened profile: **8 PASS / 0 FAIL**
- Unit tests: **6 passed**
- Local CI verifier: PASS
- Commit-bound repository replay: **PASS for WingInspect lab and artifact upload** against `5f06f4c13fc45ad3cdc15d5192d26e034f004863`
- GitHub Actions run: **Evidence reproducibility #115** (`34819514329`)
- CI runtime: Python `3.12.14`
- Retained evidence artifact: `winginspect-security-evidence-5f06f4c13fc45ad3cdc15d5192d26e034f004863`
- Artifact ID: `10338040691`
- Artifact digest: `sha256:d35cd1e5233f34fa0bcf7d04130f92ae6c0bc35640cba81dc148355b2f49285b`
- Overall workflow conclusion: **FAIL after WingInspect passed**, caused by an incorrect JSON path in the final Portfolio Integrity semantic assertion; correction pending clean rerun

`WISEC-T001` deliberately demonstrates that a model can still be evaded while the hardened system-level result passes: validation detects the miss, unsafe baseline use is blocked, and the human release boundary remains independent.

## Evidence maturity

Current local state:

**Designed → Synthetic technical implementation demonstrated → Local synthetic operation tested → Commit-bound technical replay demonstrated**

Not yet demonstrated:

**Clean full-workflow replay after semantic-assertion correction → Canonical evidence reconciliation → Production integration → Defined-period operating effectiveness → Outcome effectiveness → Independent assurance**

No new canonical evidence IDs are allocated yet. The WingInspect lab itself is commit-bound, but formal evidence reconciliation is intentionally deferred until the corrected full workflow completes green.

## Governance effect

No AI-004 residual-risk score, `ASM-008` / `ASM-028` status, production-effectiveness claim, or Restricted Pilot gate changes from this local result.
