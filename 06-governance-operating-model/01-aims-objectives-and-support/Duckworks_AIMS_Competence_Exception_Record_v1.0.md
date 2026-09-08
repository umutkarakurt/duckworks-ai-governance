# AIMS Competence and Authorization Exception Record

| Field | Value |
|---|---|
| Exception ID | `COMP-EXC-2026-001` |
| Date detected | 8 September 2026 |
| Control | Competence and scope-specific authorization gate |
| Related evidence | `EV-AIMS-004`; `EV-AIMS-005`; `EV-AIMS-008` |
| Status | Open pending synthetic remediation and renewal |
| Classification | Synthetic portfolio demonstration / non-production |

## Conditions detected

| Record | Condition | Immediate decision |
|---|---|---|
| `COMP-002` | WingInspect inspector authorization expired on 31 August 2026 and refresher is overdue | Block item-release authorization; route work to a currently authorized inspector |
| `COMP-003` | Supplier-governance assessment score is 74 against an 80 threshold | Block due-diligence completion recommendation; require learning and reassessment |

## Containment

- Neither record may perform the controlled activity.
- No local manager may bypass the block by altering dates, thresholds or activity scope.
- Existing system and supplier lifecycle gates remain unchanged.
- The synthetic exception is escalated to the relevant business owner and AI Governance Lead.

## Corrective actions and closure criteria

| Action | Owner | Due | Closure evidence |
|---|---|---|---|
| Complete inspector refresher and practical observation | Henrietta Duckwell | 15 September 2026 | Completion record, assessor result and renewed signed authorization |
| Complete supplier-risk remediation learning and reassessment | Percival Duckworth | 22 September 2026 | Assessment score at or above 80 and human authorization decision |
| Rerun executable eligibility gate | Eleanor Duckford | After both actions | Machine-readable result showing no failed conditions |
| Independently sample authorization evidence | Penelope Duckins | 30 September 2026 | Assurance note preserving independence and limitations |

Closure requires both remediation evidence and human authorization. A passed automated retest alone is insufficient.

