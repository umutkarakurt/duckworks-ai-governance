# PondGPT Supplier Gate Decision

| Field | Record |
|---|---|
| Decision ID | `TPR-GATE-AI006-2026-001` |
| Version / date | 1.0 / 8 September 2026 |
| Decision authority | Reginald Duckman — Chief Risk & Compliance Officer (synthetic exercise) |
| Process owner | Percival Duckworth — Director Procurement & Vendor Assurance |
| System/risk owner | Oliver Duckett — Head of IT & Cloud |
| Challengers | Cassandra Duckley — CISO; Daria Duckworth — DPO & Head of Privacy; Eleanor Duckford — AI Governance Lead |
| System | `AI-006 — PondGPT` |
| Supplier | LanternMind Enterprise AI Ltd. (fictional) |

## Decision

**Conditionally permit continuation of the existing restricted pilot. Do not approve broader rollout, sensitive-source expansion, production reliance or tool execution.**

**Machine-readable decision code:** `CONDITIONAL_RESTRICTED_PILOT_ONLY`

## Evidence considered

- `EV-AI006-001`–`006`: permission-boundary and regression-control evidence.
- `EV-AI006-009`: supplier intake and due-diligence assessment.
- `EV-AI006-010`: evidence register and unresolved gaps.
- `EV-AI006-011`: supplier risk assessment.
- `EV-AI006-012`: proposed contract control schedule.
- `EV-AI006-016`: executable supplier-gate result.

## Conditions maintained

1. Only approved pilot users and repositories may be connected.
2. Privileged, legal, HR-special-category, credential and unrestricted source-code sources remain excluded.
3. Tool execution remains disabled.
4. No blocking contract item may be recorded as implemented until executed and verified.
5. `PG-02` permission-regression testing remains mandatory before connector, group or corpus expansion.
6. Any supplier material change triggers reassessment before activation.

## Blocking conditions for broader rollout

- Executed clauses `TPR-CL-02` through `TPR-CL-09` and `TPR-CL-12`, as applicable.
- Verified tenant-isolation, encryption, hosting/transfer, subprocessor, retention/deletion and assurance evidence.
- Demonstrated production connector/identity/DLP/SIEM evidence and outcome monitoring.
- Tested continuity, export/restore and deletion procedures.
- Formal privacy/legal determination and authorized risk acceptance.

## Risk and evidence conclusion

`AI-006-R01` remains High. The decision gives no production risk-reduction credit and does not validate `ASM-030`. The gate must be reopened upon a blocking-condition failure, material supplier change, incident, evidence expiry, renewal or proposed expansion.
