# IAF-2026-002 — DuckDesign Synthetic Evidence Update

**Project:** Project W.I.N.G. — AIMS Internal Audit Programme  
**Document ID:** DW-AIMS-IAF-2026-002-EVID-01  
**Version:** 1.0  
**Date:** 15 September 2026  
**Finding:** `IAF-2026-002`  
**Control:** `DD-01 — Competent Engineer Approval`  
**Finding severity:** High  
**Finding status:** **Open — management response required**  
**Evidence classification:** Synthetic / non-production

## 1. Existing finding

The audit finding states that the `DD-01` source status is `Implemented`, but reviewed repository evidence did not contain a stable evidence ID, execution population, sample, exceptions, metrics or owner review.

The finding requires either:

- validated, retrievable and version-bound implementation/operating evidence; or
- an approved status downgrade with related risk reassessment and crosswalk update.

Independent validation is required for closure.

## 2. New evidence received

The DuckDesign Phase II validation increment now provides synthetic technical evidence including:

- `EV-AI001-001` — validation plan;
- `EV-AI001-002` — executable lab;
- `EV-AI001-003` — seeded findings/remediation;
- `EV-AI001-004` — hardened campaign/test report;
- `EV-AI001-005` — detection/control-signal validation;
- `EV-AI001-006` — commit-bound GitHub Actions replay; and
- `EV-AI001-007` — the narrow `DDSEC-T009` exact-artifact engineer-approval binding result.

`DDSEC-T009` demonstrates that the synthetic workflow binds approval to the exact reviewed artifact hash and invalidates the approval when the artifact changes.

## 3. Audit assessment of the new evidence

The new evidence **partially addresses mechanism existence and design traceability**.

It does not satisfy the finding's operating-evidence requirements because it does not provide:

- a real or production-equivalent DuckDesign approval population;
- a defined operating period;
- actual competent-engineer execution samples;
- exceptions / rejected approvals / overrides across a population;
- operating metrics;
- accountable owner review of defined-period performance; or
- independent validation of production or production-equivalent operation.

The synthetic test also explicitly sets `iaf_2026_002_closure_authorized=false`.

## 4. Finding disposition

**Disposition: KEEP OPEN.**

The new evidence should be cross-referenced to the finding because it reduces uncertainty about the intended technical mechanism. It does not justify finding closure, source-status validation or production risk-reduction credit.

The findings/actions register does not need to be rewritten solely for this synthetic evidence update because the recorded status remains accurate:

> **Open — management response required**

## 5. Closure evidence still required

Closure should continue to require either:

1. a validated production or production-equivalent evidence package covering the requested operating population/period, exceptions, metrics, owner review and independent validation; **or**
2. an approved status downgrade, related AI-001 risk reassessment and relevant control/evidence crosswalk updates.

## 6. Independence boundary

The Phase II technical-security lab is portfolio engineering/assurance evidence. It is not a substitute for the independent validation required by the audit finding.

No finding is auto-closed and no deployment decision is created by this record.
