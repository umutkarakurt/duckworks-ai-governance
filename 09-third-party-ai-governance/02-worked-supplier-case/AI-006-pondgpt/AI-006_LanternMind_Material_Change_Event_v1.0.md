# PondGPT Synthetic Supplier Material-Change Event

| Field | Record |
|---|---|
| Event ID | `SP-CHG-001` |
| Version / date | 1.0 / 8 September 2026 |
| Supplier | LanternMind Enterprise AI Ltd. (fictional) |
| System | `AI-006 — PondGPT` |
| Notice | Proposed migration from model route `LM-E4` to `LM-E5` and addition of `Northstar Inference B.V.` (fictional) as an inference subprocessor |
| Proposed effective date | 1 October 2026 |
| Triggered controls | `AI-TPR-01`; `AI-GOV-02`; `PG-02`; `PG-03`; `PG-05` |

## Assessment

The change affects model identity, processing chain, subprocessor access, evidence validity and technical test scope. The existing synthetic permission test does not establish that the new model route or subprocessor preserves tenant isolation, data-use restrictions, hosting, logging or security behavior.

## Response

**Reject activation within the PondGPT pilot until the conditions below are satisfied. Preserve the current restricted-pilot configuration.**

| Required action | Owner | Acceptance evidence | Status |
|---|---|---|---|
| Obtain full subprocessor purpose, locations, access and safeguards | Procurement + DPO | Updated register and approved privacy assessment | Open |
| Confirm no-training, retention/deletion and support-access obligations extend to the subprocessor | Procurement + Legal | Executed contract flow-down | Open |
| Obtain isolation, encryption and assurance evidence for the new processing chain | CISO | Reviewed architecture/test/assurance package | Open |
| Run permission-regression, prompt-injection/RAG and logging tests against the exact proposed route | IT & Cloud + CISO | Version-bound `PG-02/PG-03/PG-05` results | Open |
| Update system, supplier, risk, AIBOM/model and evidence records | AI Governance Lead | Approved version diff and crosswalk update | Open |
| Record an authorized revised gate decision before activation | CRCO | Revised decision ID | Open |

## Evidence disposition

`EV-AI006-001`–`006` remain valid only for their original synthetic test boundary. They cannot be generalized to `LM-E5` or the proposed subprocessor. `AI-006-R01` remains High and no broader rollout is permitted.

