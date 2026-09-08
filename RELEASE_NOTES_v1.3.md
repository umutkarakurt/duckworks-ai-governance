# Duckworks AI Governance — Release Notes v1.3

**Release:** v1.3 — PondGPT Supplier Governance Milestone  
**Release date:** 8 September 2026  
**Repository baseline:** `0eefcfebf87c1ff64d9030053a7042f18b6a2846`  
**Scope:** Project W.I.N.G. portfolio evidence; AI-006 PondGPT and fictional supplier LanternMind Enterprise AI Ltd.

## Release outcome

This release closes the portfolio's worked third-party-governance gap with a bounded, synthetic supplier evidence chain. It demonstrates how Duckworks would assess, conditionally approve, monitor, challenge, and exit an external AI supplier without representing fictional records as production evidence.

The supplier gate authorizes **restricted pilot use only**. Production rollout remains blocked until five contractual and evidence conditions are satisfied and independently accepted.

## New supplier-governance package

Added under `09-third-party-ai-governance/02-worked-supplier-case/AI-006-pondgpt/`:

- supplier assessment and due-diligence evidence register;
- supplier risk assessment connected to `AI-006-R01`;
- contract control schedule with five rollout-blocking conditions;
- governance-gate decision and named challenge roles;
- monitoring, material-change, incident-notification, and exit plan;
- synthetic material-change event and escalation record;
- executable supplier-gate configuration, test, and run summary.

## Canonical records updated

- `Duckworks_AI_Risk_Scenarios_v1.3.md` now links PondGPT's risk treatment and rollout decision to supplier evidence.
- `Duckworks_AI_Control_Framework_Report_v1.3.md` now identifies the operating basis and evidence limitations for `AI-TPR-01`.
- `Duckworks_AI_Control_Evidence_Index_v1.3.md` adds `EV-AI006-009` through `EV-AI006-016`.
- `duckworks-iso42001-evidence-baseline-v1.3.md` updates M13 and M15 using the bounded supplier lifecycle.
- `Duckworks_AIMS_Master_Crosswalk_v1.2.xlsx` maps the supplier assessment, risk, controls, evidence, decision, and change trigger.
- repository and folder READMEs now route reviewers to the worked supplier case.

## Evidence and assertion summary

| Measure | Result |
|---|---:|
| Canonical evidence records | 42 |
| Available synthetic records | 36 |
| Explicitly unavailable records | 6 |
| New supplier evidence IDs | 8 |
| Supplier-gate assertions passed | 6 |
| Supplier-gate assertions failed | 0 |
| Production rollout blockers | 5 |

## Decision boundary

The package does not claim:

- completed supplier contracting;
- production deployment;
- independently validated control effectiveness;
- supplier evidence received from a real provider;
- ISO/IEC 42001 certification or full conformity.

The current decision is `CONDITIONAL_RESTRICTED_PILOT_ONLY`. Human authorization remains mandatory, and the executable check cannot approve a supplier or override the governance decision.

## Verification

The release package was checked for:

- successful execution of the PondGPT supplier-gate test;
- consistency of evidence IDs and referenced control/risk IDs;
- absence of spreadsheet formula-error values;
- visual rendering of all 11 crosswalk worksheets;
- valid JSON and CSV structure;
- repository-relative Markdown link targets against the staged and baseline repository trees.

