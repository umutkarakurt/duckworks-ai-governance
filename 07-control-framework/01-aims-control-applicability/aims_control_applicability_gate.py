#!/usr/bin/env python3
"""Validate the bounded synthetic Duckworks AIMS control-applicability register."""
from __future__ import annotations
import csv
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
CONFIG = json.loads((BASE / "applicability_gate_config.json").read_text(encoding="utf-8"))
ROWS = list(csv.DictReader((BASE / CONFIG["register"]).open(encoding="utf-8", newline="")))
REQUIRED = CONFIG["required_columns"]
CONTROL_RE = re.compile(r"^(?:AI-(?:GOV|INC|TPR)-\d{2}|(?:DD|QB|FF|WI|DT|PG|SH)-\d{2})$")
EVIDENCE_RE = re.compile(r"^EV-(?:AI\d{3}|AIMS)-\d{3}$")
failures = []

if len(ROWS) != CONFIG["expected_control_count"]:
    failures.append(f"CONTROL_COUNT:{len(ROWS)}")
if list(ROWS[0].keys()) != REQUIRED if ROWS else True:
    failures.append("SCHEMA_MISMATCH")

ids = [r.get("Control_ID", "").strip() for r in ROWS]
if len(ids) != len(set(ids)):
    failures.append("DUPLICATE_CONTROL_ID")
for row in ROWS:
    cid = row.get("Control_ID", "").strip()
    if not CONTROL_RE.fullmatch(cid):
        failures.append(f"INVALID_CONTROL_ID:{cid}")
    for field in REQUIRED:
        if not row.get(field, "").strip():
            failures.append(f"MISSING_{field}:{cid}")
    decision = row.get("Applicability_Decision", "")
    if decision not in CONFIG["allowed_decisions"]:
        failures.append(f"INVALID_DECISION:{cid}")
    if decision in {"Conditionally applicable", "Not applicable", "Pending decision"} and len(row.get("Conditional_or_Exclusion_Criteria", "").strip()) < 25:
        failures.append(f"MISSING_DECISION_CRITERIA:{cid}")
    if row.get("Production_Effectiveness_Claim") != "No":
        failures.append(f"UNSUPPORTED_PRODUCTION_CLAIM:{cid}")
    ev = row.get("Evidence_IDs", "")
    if ev != "None linked":
        for item in [x.strip() for x in ev.split(";") if x.strip()]:
            if not EVIDENCE_RE.fullmatch(item):
                failures.append(f"INVALID_EVIDENCE_ID:{cid}:{item}")

counts = {
    "Applicable": sum(r["Applicability_Decision"] == "Applicable" for r in ROWS),
    "Conditionally applicable": sum(r["Applicability_Decision"] == "Conditionally applicable" for r in ROWS),
    "Not applicable": sum(r["Applicability_Decision"] == "Not applicable" for r in ROWS),
    "Pending decision": sum(r["Applicability_Decision"] == "Pending decision" for r in ROWS),
}
evidence_linked = sum(r["Evidence_IDs"] != "None linked" for r in ROWS)
without_evidence = len(ROWS) - evidence_linked
unsupported = sum(
    r["Source_Implementation_Status"] == "Implemented" and r["Evidence_IDs"] == "None linked"
    for r in ROWS
)
expectations = {
    "control_count": len(ROWS) == CONFIG["expected_control_count"],
    "applicable": counts["Applicable"] == CONFIG["expected_applicable"],
    "conditionally_applicable": counts["Conditionally applicable"] == CONFIG["expected_conditionally_applicable"],
    "not_applicable": counts["Not applicable"] == CONFIG["expected_not_applicable"],
    "evidence_linked": evidence_linked == CONFIG["expected_evidence_linked"],
    "without_evidence": without_evidence == CONFIG["expected_without_evidence"],
    "unsupported_implemented_without_evidence": unsupported == CONFIG["expected_unsupported_implemented_without_evidence"],
}
for name, met in expectations.items():
    if not met:
        failures.append(f"EXPECTED_RESULT_MISMATCH:{name}")

summary = {
    "gate_id": CONFIG["gate_id"],
    "as_of_date": CONFIG["as_of_date"],
    "controls_evaluated": len(ROWS),
    "applicable": counts["Applicable"],
    "conditionally_applicable": counts["Conditionally applicable"],
    "not_applicable": counts["Not applicable"],
    "pending_decision": counts["Pending decision"],
    "evidence_linked_controls": evidence_linked,
    "controls_without_linked_evidence": without_evidence,
    "unsupported_implemented_without_evidence": unsupported,
    "expected_results_met": sum(expectations.values()),
    "expected_results_total": len(expectations),
    "failed_assertions": len(failures),
    "failures": failures,
    "human_approval_required": True,
    "decisions_auto_approved": 0,
    "risk_acceptances_created": 0,
    "production_effectiveness_claims_created": 0,
    "evidence_boundary": "Synthetic portfolio validation; automation does not approve applicability, exclusions, risk acceptance, deployment, conformity or production effectiveness",
}
(BASE / CONFIG["output"]).write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
print(json.dumps(summary, indent=2))
raise SystemExit(1 if failures else 0)

