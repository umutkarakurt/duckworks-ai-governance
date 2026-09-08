# PondGPT Supplier Risk Assessment

| Field | Record |
|---|---|
| Document ID | DW-TPR-AI006-002 |
| Version / date | 1.0 / 8 September 2026 |
| Assessment ID | `TPR-RISK-AI006-2026-001` |
| Supplier / service | LanternMind Enterprise AI Ltd. / hosted enterprise LLM (fictional) |
| Linked system risk | `AI-006-R01 — Privacy & data governance` |
| Control | `AI-TPR-01` |
| Risk owner | Oliver Duckett — Head of IT & Cloud |
| Assessment owner | Percival Duckworth — Director Procurement & Vendor Assurance |

## Scoring boundary

Severity and likelihood use the Duckworks five-point methodology. Scores support prioritization; they are not proof of probability, compliance or risk reduction. “Current” reflects the synthetic evidence available for this case. Target scores remain treatment objectives.

| Supplier risk ID | Scenario | Inherent | Current | Target | Treatment and evidence condition | Current disposition |
|---|---|---:|---:|---:|---|---|
| `SR-AI006-01` | Supplier retains or reuses Duckworks prompts/content for training or service improvement outside the approved purpose. | 4×4 = 16 High | 4×4 = 16 High | 4×1 = 4 Low | Executed restricted-use/no-training term plus verified configuration and retention evidence. | Open blocker for broader rollout |
| `SR-AI006-02` | Weak tenant isolation or support access exposes Duckworks content to another tenant or unauthorized supplier personnel. | 5×3 = 15 High | 5×3 = 15 High | 5×1 = 5 Moderate | Isolation architecture/test evidence, privileged-access control, logs and assurance review. | Open blocker for broader rollout |
| `SR-AI006-03` | Hosting, subprocessor or remote-access arrangements create an unassessed location or transfer exposure. | 4×3 = 12 High | 4×3 = 12 High | 4×1 = 4 Low | Complete location/subprocessor record, privacy review and advance change notice. | Open blocker for sensitive-source use |
| `SR-AI006-04` | A supplier incident is reported too late or with insufficient evidence for Duckworks to contain impact. | 4×3 = 12 High | 4×3 = 12 High | 4×1 = 4 Low | Executed 24-hour notice, named contacts, preservation/cooperation duty and exercise. | Open contractual condition |
| `SR-AI006-05` | An unannounced model, safety-policy or service change invalidates PondGPT testing and control assumptions. | 4×4 = 16 High | 4×4 = 16 High | 4×2 = 8 Moderate | Executed change notice, model/version record, reassessment trigger and pre-activation gate. | Open blocker; `SP-CHG-001` demonstrates response |
| `SR-AI006-06` | Outage, termination or lock-in prevents service continuity, evidence retrieval, data export or verified deletion. | 4×3 = 12 High | 4×3 = 12 High | 3×2 = 6 Moderate | Tested export/restore, fallback procedure, transition assistance and deletion attestation. | Open exit-readiness gap |

## Aggregate interpretation

Supplier evidence does not justify lowering the existing `AI-006-R01` position. PondGPT remains **High**, and production authorization must continue to use the inherent-risk position conservatively until evidence is accepted by the authorized risk owner.

## Decision

The supplier relationship is conditionally acceptable only for the existing restricted pilot and its approved data/repository boundary. Broader rollout, sensitive-source expansion and production reliance remain blocked.

