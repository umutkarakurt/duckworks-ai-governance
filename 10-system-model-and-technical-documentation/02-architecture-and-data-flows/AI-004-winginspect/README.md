# AI-004 WingInspect Vision — Phase II Technical Architecture

**System:** AI-004 — WingInspect Vision  
**Current governance gate:** Restricted pilot only  
**Status:** Synthetic architecture baseline established; first technical-validation increment commit-bound and reconciled

## Current artifact

- [`Duckworks_WingInspect_Technical_Security_Architecture_v1.0.md`](Duckworks_WingInspect_Technical_Security_Architecture_v1.0.md)

The architecture preserves the core boundary:

> The vision model may flag or classify defects, but it cannot independently authorize product release.

Related artifacts:

- [`../../03-threat-models/AI-004-winginspect/Duckworks_WingInspect_Threat_Model_v1.0.md`](../../03-threat-models/AI-004-winginspect/Duckworks_WingInspect_Threat_Model_v1.0.md)
- [`../../../11-assurance-testing-and-evaluation/06-technical-security-validation/AI-004-winginspect/`](../../../11-assurance-testing-and-evaluation/06-technical-security-validation/AI-004-winginspect/)
- [`../../../80-operating-evidence/AI-004-winginspect/Duckworks_WingInspect_Evidence_Reconciliation_Record_v1.0.md`](../../../80-operating-evidence/AI-004-winginspect/Duckworks_WingInspect_Evidence_Reconciliation_Record_v1.0.md)

The successful commit-bound replay is tied to `8e8bb9e43aca3d4a9d2f5cfb6e401b8469c4ac0b` and does not convert this design artifact into evidence that the same architecture exists in production.

## Evidence boundary

The architecture and related lab do not establish a production camera/model architecture, real physical-world adversarial robustness, manufacturing/product-safety effectiveness, legal classification or production control effectiveness.
