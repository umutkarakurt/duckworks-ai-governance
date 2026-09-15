# AI-001 DuckDesign AI — Detection and Control-Signal Validation

**Document ID:** DW-AI001-DET-SEC-01  
**Version:** 1.0  
**Date:** 15 September 2026  
**Status:** Local synthetic validation complete; repository replay pending  
**System:** AI-001 — DuckDesign AI

## 1. Purpose

This record separates **security/engineering outcome** from **detection signal**.

DuckDesign must not depend on an alert firing before data, dependency, execution, tool, validation, safety, approval or provenance boundaries are enforced.

## 2. Signal coverage

| Test | Primary control signal | Hardened outcome |
|---|---|---|
| T001 | DLP/redaction event | defined engineering-IP/secret canaries absent from prohibited sinks |
| T002 | indirect-instruction signal | imported content cannot alter tool/validation authority |
| T003 | generated-code policy event | scanner/sandbox prevents prohibited behavior and promotion |
| T004 | unapproved-dependency event | package denied; no public-registry fallback |
| T005 | dependency-integrity event | hash mismatch blocks build/promotion |
| T006 | tool/egress denial | high-impact action and arbitrary egress denied |
| T007 | engineering-validation failure | unsafe engineering value blocks promotion |
| T008 | safety-gate bypass denial | required independent validation cannot be skipped |
| T009 | approval-integrity mismatch | stale/wrong-artifact approval invalidated |
| T010 | material-change event | regression required and promotion blocked |
| T011 | provenance-incomplete event | artifact quarantined |
| T012 | rollback/reconstruction event | known-good state restored and hash verified |

## 3. Control hierarchy

The intended hierarchy is:

> **preventive/containment boundary → validation/detection signal → correlated evidence → governance conclusion**

Examples:

- DLP signal does not replace context minimization.
- Generated-code scanning does not replace the sandbox.
- Dependency-risk detection does not replace approved-registry/hash enforcement.
- Tool alerting does not replace least privilege.
- Engineering validation does not replace an independent safety gate where required.
- Approval logging does not replace exact-artifact binding.
- Provenance generation does not replace integrity verification.

## 4. Evidence limitations

The portfolio does not contain real:

- AetherForge provider telemetry;
- engineering DLP events;
- package-registry/proxy logs;
- source/build scanner outcomes;
- CAD/simulation tool authorization logs;
- product-safety test records;
- engineer approval populations;
- production SBOM/provenance attestations;
- incident-response/rollback outcomes; or
- defined-period operating metrics.

## 5. Governance consequence

The local result supports only a bounded synthetic conclusion.

It does not change risk scores, close assumptions, close `IAF-2026-002`, establish product safety or expand the Restricted Pilot.
