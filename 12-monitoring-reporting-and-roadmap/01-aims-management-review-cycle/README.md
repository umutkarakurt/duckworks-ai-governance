# AIMS Risk, Opportunity and Management Review Cycle

**Repository path:** `12-monitoring-reporting-and-roadmap/01-aims-management-review-cycle/`  
**Release:** v1.5  
**Version:** 1.0  
**Evidence classification:** Synthetic portfolio demonstration / non-production

[← Back to Monitoring, Reporting and Roadmap](../README.md)

## Purpose

This package demonstrates a bounded AIMS-wide review cycle that consumes the v1.4 objectives and support evidence, identifies management-system risks and opportunities, records decisions, assigns actions, and tests whether overdue or blocked actions are escalated.

**Objective performance → AIMS risk/opportunity → management review → decision → assigned action → deadline → executable escalation → follow-up**

## Evidence chain

| Evidence ID | Artifact | Demonstration |
|---|---|---|
| `EV-AIMS-009` | `Duckworks_AIMS_Risk_and_Opportunity_Method_v1.0.md` | AIMS-level risk and opportunity identification, scoring, response and review rules |
| `EV-AIMS-010` | `Duckworks_AIMS_Risk_and_Opportunity_Register_v1.0.csv` | Seven management-system risks and one portfolio opportunity with owners and treatments |
| `EV-AIMS-011` | `Duckworks_AIMS_Objectives_Period_2_Snapshot_v1.0.csv` | Release-triggered reconciliation of all eight objectives |
| `EV-AIMS-012` | `Duckworks_AIMS_Management_Review_Input_Pack_v1.0.md` | Consolidated objectives, risk, evidence, supplier, competence, audit and resource inputs |
| `EV-AIMS-013` | `Duckworks_AIMS_Management_Review_Record_MR-AIMS-2026-002.md` | Bounded synthetic management-review decisions and retained system gates |
| `EV-AIMS-014` | `Duckworks_AIMS_Management_Action_Tracker_v1.0.csv` | Six actions with owners, deadlines, dependencies and completion evidence |
| `EV-AIMS-015` | `aims_management_action_gate.py`, configuration and run summary | Deterministic overdue, blocked and open-action classification without automatic closure |
| `EV-AIMS-016` | `Duckworks_AIMS_Management_Action_Exception_Record_v1.0.md` | Escalation and containment for one overdue and one dependency-blocked action |

The companion workbook `Duckworks_AIMS_Risk_Opportunity_and_Management_Review_Register_v1.0.xlsx` consolidates the complete evidence chain in a filterable, formula-driven management view.

## Gate outcome

The synthetic follow-up gate evaluates six management actions as of 1 October 2026:

- one overdue action is escalated;
- one action remains blocked by external supplier dependencies;
- four open actions remain under monitoring;
- zero actions are automatically closed; and
- a human management decision remains required.

## Decision boundary

The management-review record is a fictional portfolio exercise. It does not represent a real Duckworks meeting, real approval, recurring AIMS operation, production control effectiveness, ISO/IEC 42001 conformity, certification, legal compliance or independent assurance. No system risk score or lifecycle gate is changed.

