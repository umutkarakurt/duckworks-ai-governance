# AI-002 QuackBot — Phase II Technical Architecture

**System:** AI-002 — QuackBot  
**Business function:** Customer Operations  
**Current governance gate:** **Pre-Production / Production Blocked**  
**Status:** Synthetic security architecture established; first technical-validation increment commit-bound and reconciled

## Current artifact

- [`Duckworks_QuackBot_Technical_Security_Architecture_v1.0.md`](Duckworks_QuackBot_Technical_Security_Architecture_v1.0.md)

Related artifacts:

- [`../../03-threat-models/AI-002-quackbot/Duckworks_QuackBot_Threat_Model_v1.0.md`](../../03-threat-models/AI-002-quackbot/Duckworks_QuackBot_Threat_Model_v1.0.md)
- [`../../../11-assurance-testing-and-evaluation/06-technical-security-validation/AI-002-quackbot/`](../../../11-assurance-testing-and-evaluation/06-technical-security-validation/AI-002-quackbot/)
- [`../../../80-operating-evidence/AI-002-quackbot/Duckworks_QuackBot_Evidence_Reconciliation_Record_v1.0.md`](../../../80-operating-evidence/AI-002-quackbot/Duckworks_QuackBot_Evidence_Reconciliation_Record_v1.0.md)

Canonical commit-bound replay:

`25525cc2c09c6b6557ddb9e7706fdaf81ce1796f`

The architecture preserves two critical invariants:

> **The model is not an access-control mechanism. Customer/account authorization is enforced before private content enters model context.**

> **Retrieved content and model output are untrusted data and do not acquire application authority through the LLM.**

## Evidence boundary

The successful synthetic replay does not prove that this target architecture exists in production or that real API/session/customer-data/provider boundaries are effective.

The production gate remains **blocked**.
