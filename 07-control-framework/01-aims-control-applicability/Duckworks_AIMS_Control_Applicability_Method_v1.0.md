# Duckworks AIMS Control Applicability Method

**Project:** W.I.N.G. — Workflows, Intelligence, Next-Generation Governance  
**Document ID:** DW-AIMS-CAM-001  
**Version:** 1.0  
**Effective date:** 9 September 2026  
**Owner:** AI Governance Lead  
**Approval status:** Approved within bounded synthetic portfolio exercise  
**Evidence ID:** EV-AIMS-017

> This method and its records are fictional or synthetic portfolio evidence. They do not demonstrate ISO/IEC 42001 conformity, certification, legal compliance, production operation, validated effectiveness or independent assurance.

## 1. Purpose

This method defines how Duckworks decides whether each canonical AI control is included, conditionally included or excluded from the proposed AIMS control set. It closes the portfolio's prior gap between risk/control design and an inspectable applicability rationale.

## 2. Authoritative inputs

- `04-risk-assessment/Duckworks_AI_Risk_Scenarios_v1.3.md`
- `07-control-framework/Duckworks_AI_Control_Framework_Report_v1.4.md`
- `80-operating-evidence/Duckworks_AI_Control_Evidence_Index_v1.6.md`
- `11-assurance-testing-and-evaluation/03-iso42001/duckworks-iso42001-evidence-baseline-v1.6.md`
- `11-assurance-testing-and-evaluation/03-iso42001/Duckworks_AIMS_Master_Crosswalk_v1.5.xlsx`

The local AIMS themes M01–M18 are portfolio identifiers, not ISO/IEC 42001 clause numbers. Normative requirement and Annex A mappings remain subject to verification against an authorized copy of the standard.

## 3. Decision states

| State | Meaning | Required rationale |
|---|---|---|
| Applicable | The control treats an identified risk or supports the AIMS across its approved scope. | Named scope, risk or management-system need, owner and evidence expectation |
| Conditionally applicable | Applicability depends on a defined architecture, supplier, data, lifecycle or use condition. | Testable condition, decision owner and evidence required to activate or deactivate |
| Not applicable | The control does not address the defined scope and no triggering condition exists. | Specific exclusion rationale, alternative treatment where needed and CRCO approval |
| Pending decision | Information is insufficient for a defensible decision. | Named information gap, owner, due date and interim restriction |

## 4. Assessment sequence

1. Confirm the control ID, purpose, owner and current source status.
2. Trace the control to documented risk IDs or an AIMS-wide governance need.
3. Define the exact AI-entry or management-system scope.
4. Decide applicable, conditionally applicable, not applicable or pending.
5. Record the inclusion, condition or exclusion rationale.
6. Link available evidence IDs without converting synthetic evidence into production credit.
7. Record the current risk-credit boundary and next evidence required.
8. Obtain human approval and establish review triggers.
9. Validate structural completeness with the executable applicability gate.
10. Reassess after a material change or by the next review date.

## 5. Evidence and status rules

A control may be applicable while planned, unimplemented or unsupported by evidence. Applicability does not prove implementation. Implementation does not prove operation. Synthetic operation does not prove production effectiveness. No row may support residual-risk reduction unless the risk methodology is applied to version-bound production evidence and the authorized decision is recorded.

Source-status inconsistencies remain visible. In particular, `DD-01` and `FF-01` retain an Implemented source label but have no linked evidence ID; the register classifies both as unsupported implementation assertions and grants no additional risk credit.

## 6. Approval and exceptions

The control owner proposes the decision. The AI Governance Lead checks traceability and evidence boundaries. The CRCO approves the applicability decision within the portfolio exercise. Internal Audit may challenge the design and records but does not own the decisions or controls it later audits.

A not-applicable decision requires a specific rationale, an alternative treatment where risk remains, and CRCO approval. The executable gate detects missing data but cannot approve an exclusion, accept risk, authorize deployment, close an action or claim conformity.

## 7. Review cadence

Review at least quarterly and after any material change to an AI system, intended purpose, data, model, integration, supplier, legal assumption, risk scenario, control design, evidence state, lifecycle gate or AIMS scope.

