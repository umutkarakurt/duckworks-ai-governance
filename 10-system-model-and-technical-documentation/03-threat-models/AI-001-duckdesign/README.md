# AI-001 DuckDesign AI — Phase II Threat Model

**System:** AI-001 — DuckDesign AI  
**Current governance gate:** **Restricted Pilot only**  
**Architecture dependency:** `DW-AI001-ARCH-SEC-01 v1.0`  
**Status:** Threat-model baseline complete; validation plan / execution pending

## Current artifact

- [`Duckworks_DuckDesign_Threat_Model_v1.0.md`](Duckworks_DuckDesign_Threat_Model_v1.0.md)

The threat model covers:

- engineering-IP/provider leakage;
- indirect instruction injection through engineering/specification content;
- generated-code security;
- hallucinated/unapproved dependencies;
- dependency confusion / package compromise;
- artifact/build integrity;
- CAD/simulation tool privilege;
- arbitrary shell/file/network egress;
- engineering material/unit/range validation;
- safety-gate bypass;
- approval-to-artifact integrity;
- model/provider/config/tool drift;
- SBOM/provenance gaps; and
- known-good rollback/evidence reconstruction.

## Candidate validation set

`DDSEC-T001`–`DDSEC-T012` are **design-only** test IDs until a separate validation plan defines fixtures, vulnerable/hardened profiles, assertions and evidence schema.

No `EV-AI001-*` evidence IDs are allocated at this stage.

## Evidence boundary

The threat model identifies plausible attack/failure paths. It does not establish that a production vulnerability exists, that an attack occurred, or that `DD-01`–`DD-05` operate effectively.

`IAF-2026-002` remains open.

The lifecycle gate remains **Restricted Pilot only**.
