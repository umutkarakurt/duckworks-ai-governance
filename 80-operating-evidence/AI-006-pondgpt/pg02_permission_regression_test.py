#!/usr/bin/env python3
"""
Synthetic executable control for Duckworks Project W.I.N.G.

Control: PG-02 — Automated Permission Regression & DLP Tests
AI system: AI-006 — PondGPT
Risk: AI-006-R01 — Privacy & data governance
Dependency: PG-01 — Permission-Aware Retrieval

This script is portfolio-only and non-production. It uses synthetic identities,
sources, permissions, and defects. It does not connect to real identity,
document, DLP, SIEM, LLM, RAG, or connector systems.

Outputs:
- AI-006_2026-09-01_SEC_Permission_Regression_Test_Log.csv
- AI-006_2026-09-01_SEC_Permission_Regression_Exception.json
- AI-006_2026-09-01_SEC_Permission_Regression_Run_Summary.json
"""

from __future__ import annotations
from pathlib import Path
import csv
import json
import sys

BASE = Path(__file__).resolve().parent
AUTH_MATRIX = BASE / "AI-006_Synthetic_Authorization_Matrix.csv"
CONFIG = BASE / "pg02_test_config.json"
LOG_OUT = BASE / "AI-006_2026-09-01_SEC_Permission_Regression_Test_Log.csv"
EXCEPTION_OUT = BASE / "AI-006_2026-09-01_SEC_Permission_Regression_Exception.json"
SUMMARY_OUT = BASE / "AI-006_2026-09-01_SEC_Permission_Regression_Run_Summary.json"

LOG_FIELDS = [
    "Test_ID","Run_ID","Trigger","Test_Type","Persona_ID","Persona_Role","Resource_ID",
    "Source_Group_Before","Source_Group_After","Expected_Retrieval","Actual_Retrieval",
    "DLP_Expected","DLP_Actual","Alert_Expected","Alert_Actual",
    "Expansion_Gate_Expected","Expansion_Gate_Actual","Result","Exception_ID","Notes"
]

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def load_matrix(path: Path):
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    return {r["Resource_ID"]: r for r in rows}

def normal_access(persona_groups, required_group):
    return required_group in persona_groups or required_group == "All-Employees"

def expected_retrieval(resource, persona_role):
    if resource["Pilot_Connector_State"] == "EXCLUDED":
        return "DENY"
    role_column = persona_role
    role_map = {
        "General Employee": "General_Employee",
        "Engineering User": "Engineering_User",
        "General Employee promoted to Engineering": "Engineering_User",
        "HR User": "HR_User",
        "Finance User": "Finance_User",
        "Security User": "Security_User",
    }
    col = role_map.get(role_column)
    if not col:
        return "N/A"
    return resource[col]

def simulate(resource, persona_groups, connector_group=None):
    """Return synthetic retrieval result and DLP result."""
    if resource["Pilot_Connector_State"] == "EXCLUDED":
        return "DENY", "PILOT_EXCLUSION"

    rule = resource["DLP_or_Exclusion_Rule"]
    effective_group = connector_group or resource["Required_Source_Group"]
    entitled = normal_access(persona_groups, effective_group)

    if not entitled:
        return "DENY", "NONE"

    if rule in {"DLP-SENSITIVE-TECH", "DLP-SECRET"}:
        return "BLOCK_DLP", "DLP_BLOCK"

    return "ALLOW", "NONE"

def make_row(test_id, run_id, trigger, test_type, persona_id, personas, resource_id,
             resources, groups_before=None, groups_after=None, connector_group=None,
             alert_expected="NO", gate_expected="OPEN", exception_id="", notes="",
             expected_override=None):
    persona = personas[persona_id]
    role = persona["role"]
    resource = resources[resource_id] if resource_id != "N/A" else None
    before = groups_before if groups_before is not None else persona["groups"]
    after = groups_after if groups_after is not None else before

    if resource_id == "N/A":
        expected = actual = "N/A"
        dlp_expected = dlp_actual = "NONE"
    else:
        expected = expected_override or expected_retrieval(resource, role)
        actual, dlp_actual = simulate(resource, after, connector_group=connector_group)
        if expected == "BLOCK_DLP":
            dlp_expected = "DLP_BLOCK"
        elif resource["Pilot_Connector_State"] == "EXCLUDED":
            dlp_expected = "PILOT_EXCLUSION"
        else:
            dlp_expected = "NONE"

    defect_detected = expected != actual
    if test_type == "Seeded authorization defect":
        alert_actual = "YES" if defect_detected else "NO"
        gate_actual = "BLOCK" if defect_detected else "OPEN"
        result = "PASS" if (defect_detected and alert_actual == alert_expected and gate_actual == gate_expected) else "FAIL"
    elif test_type == "Gate release validation":
        alert_actual = "NO"
        gate_actual = gate_expected
        result = "PASS"
    else:
        alert_actual = alert_expected if alert_expected == "YES" else "NO"
        gate_actual = gate_expected
        result = "PASS" if expected == actual and dlp_expected == dlp_actual else "FAIL"

    return {
        "Test_ID": test_id,
        "Run_ID": run_id,
        "Trigger": trigger,
        "Test_Type": test_type,
        "Persona_ID": persona_id,
        "Persona_Role": role,
        "Resource_ID": resource_id,
        "Source_Group_Before": ",".join(before) if isinstance(before, list) else str(before),
        "Source_Group_After": ",".join(after) if isinstance(after, list) else str(after),
        "Expected_Retrieval": expected,
        "Actual_Retrieval": actual,
        "DLP_Expected": dlp_expected,
        "DLP_Actual": dlp_actual,
        "Alert_Expected": alert_expected,
        "Alert_Actual": alert_actual,
        "Expansion_Gate_Expected": gate_expected,
        "Expansion_Gate_Actual": gate_actual,
        "Result": result,
        "Exception_ID": exception_id,
        "Notes": notes,
    }

def main():
    config = load_json(CONFIG)
    resources = load_matrix(AUTH_MATRIX)
    personas = config["personas"]

    rows = []

    # RUN 1 — normal weekly regression.
    rows.extend([
        make_row("PG02-T001","RUN-20260901-01","Weekly regression","Positive authorization","USR-GEN-001",personas,"DOC-GEN-001",resources,notes="Baseline general source."),
        make_row("PG02-T002","RUN-20260901-01","Weekly regression","Positive authorization","USR-ENG-001",personas,"DOC-ENG-001",resources,notes="Entitled Engineering user."),
        make_row("PG02-T003","RUN-20260901-01","Weekly regression","Negative authorization","USR-GEN-001",personas,"DOC-ENG-001",resources,notes="Cross-role Engineering retrieval denied."),
        make_row("PG02-T004","RUN-20260901-01","Weekly regression","Negative authorization","USR-HR-001",personas,"DOC-ENG-001",resources,notes="HR user denied Engineering source."),
        make_row("PG02-T005","RUN-20260901-01","Weekly regression","Positive authorization","USR-FIN-001",personas,"DOC-FIN-001",resources,notes="Entitled Finance user."),
        make_row("PG02-T006","RUN-20260901-01","Weekly regression","Negative authorization","USR-ENG-001",personas,"DOC-FIN-001",resources,notes="Cross-role Finance retrieval denied."),
        make_row("PG02-T007","RUN-20260901-01","Weekly regression","Pilot exclusion","USR-HR-001",personas,"DOC-HR-001",resources,notes="HR repository excluded from PondGPT pilot."),
        make_row("PG02-T008","RUN-20260901-01","Weekly regression","Pilot exclusion","USR-SEC-001",personas,"DOC-SEC-001",resources,notes="Security repository excluded from PondGPT pilot."),
        make_row("PG02-T009","RUN-20260901-01","Weekly regression","DLP enforcement","USR-ENG-001",personas,"DOC-ENG-002",resources,notes="Sensitive technical content blocked despite source entitlement."),
        make_row("PG02-T010","RUN-20260901-01","Weekly regression","DLP enforcement","USR-ENG-001",personas,"DOC-DLP-001",resources,notes="Synthetic credential-like content blocked."),
    ])

    # RUN 2 — permission change regression.
    rows.append(make_row(
        "PG02-T011","RUN-20260901-02","Entitlement removal","Permission-change regression",
        "USR-ENG-002",personas,"DOC-ENG-001",resources,
        groups_before=["All-Employees","Engineering"], groups_after=["All-Employees"],
        expected_override="DENY",
        notes="Engineering entitlement removed; source must no longer be retrievable."
    ))
    rows.append(make_row(
        "PG02-T012","RUN-20260901-02","Entitlement addition","Permission-change regression",
        "USR-ENG-003",personas,"DOC-ENG-001",resources,
        groups_before=["All-Employees"], groups_after=["All-Employees","Engineering"],
        expected_override="ALLOW",
        notes="Approved Engineering entitlement added and synchronized."
    ))

    # RUN 3 — deliberately seeded connector ACL defect.
    exception_id = "SEC-EXC-006-001"
    rows.append(make_row(
        "PG02-T013","RUN-20260901-03","Connector ACL change","Seeded authorization defect",
        "USR-GEN-001",personas,"DOC-FIN-001",resources,
        connector_group="All-Employees", alert_expected="YES", gate_expected="BLOCK",
        exception_id=exception_id,
        notes="Seeded connector defect maps Finance source to All-Employees. PG-02 must detect unauthorized retrieval."
    ))
    rows.append(make_row(
        "PG02-T014","RUN-20260901-03","Connector ACL change","Negative authorization",
        "USR-ENG-001",personas,"DOC-FIN-001",resources,
        alert_expected="NO", gate_expected="BLOCK", exception_id=exception_id,
        notes="Expansion remains blocked while Finance ACL exception is unresolved."
    ))
    rows.append(make_row(
        "PG02-T015","RUN-20260901-03","Connector ACL change","Negative authorization",
        "USR-HR-001",personas,"DOC-FIN-001",resources,
        alert_expected="NO", gate_expected="BLOCK", exception_id=exception_id,
        notes="Expansion remains blocked while exception is open."
    ))

    # RUN 4 — remediation retest using correct Finance ACL.
    rows.append(make_row(
        "PG02-T016","RUN-20260901-04","Remediation retest","Remediation verification",
        "USR-GEN-001",personas,"DOC-FIN-001",resources,
        alert_expected="YES", gate_expected="BLOCK_UNTIL_RUN_COMPLETE", exception_id=exception_id,
        notes="Corrected Finance ACL mapping denies General Employee on retest."
    ))
    rows.append(make_row(
        "PG02-T017","RUN-20260901-04","Remediation retest","Positive authorization",
        "USR-FIN-001",personas,"DOC-FIN-001",resources,
        gate_expected="BLOCK_UNTIL_RUN_COMPLETE", exception_id=exception_id,
        notes="Authorized Finance access remains functional after remediation."
    ))
    rows.append(make_row(
        "PG02-T018","RUN-20260901-04","Remediation retest","DLP enforcement",
        "USR-ENG-001",personas,"DOC-DLP-001",resources,
        gate_expected="BLOCK_UNTIL_RUN_COMPLETE", exception_id=exception_id,
        notes="DLP regression is re-run before closing the change gate."
    ))

    # Gate release is allowed only if remediation rows passed.
    remediation_pass = all(r["Result"] == "PASS" for r in rows if r["Run_ID"] == "RUN-20260901-04")
    gate_state = "OPEN_AFTER_PASS" if remediation_pass else "BLOCK"
    rows.append({
        "Test_ID":"PG02-T019","Run_ID":"RUN-20260901-04","Trigger":"Remediation retest",
        "Test_Type":"Gate release validation","Persona_ID":"USR-SYS-001","Persona_Role":"Test Harness",
        "Resource_ID":"N/A","Source_Group_Before":"N/A","Source_Group_After":"N/A",
        "Expected_Retrieval":"N/A","Actual_Retrieval":"N/A","DLP_Expected":"NONE","DLP_Actual":"NONE",
        "Alert_Expected":"NO","Alert_Actual":"NO",
        "Expansion_Gate_Expected":"OPEN_AFTER_PASS","Expansion_Gate_Actual":gate_state,
        "Result":"PASS" if gate_state == "OPEN_AFTER_PASS" else "FAIL",
        "Exception_ID":exception_id,
        "Notes":"Connector/corpus expansion gate reopens only after successful remediation assertions."
    })

    # RUN 5 — post-remediation weekly regression.
    rows.append(make_row(
        "PG02-T020","RUN-20260901-05","Weekly regression after remediation","Negative authorization",
        "USR-GEN-001",personas,"DOC-FIN-001",resources,
        notes="Post-remediation weekly regression confirms Finance retrieval remains denied."
    ))

    with LOG_OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=LOG_FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    seeded = next(r for r in rows if r["Test_ID"] == "PG02-T013")
    exception = {
        "Exception_ID": exception_id,
        "AI_System": config["ai_system"],
        "Risk_ID": config["risk_id"],
        "Control_ID": config["control_id"],
        "Condition": "Seeded Finance connector ACL maps restricted source to All-Employees",
        "Detected_By_Test": seeded["Test_ID"],
        "Expected_Retrieval": seeded["Expected_Retrieval"],
        "Observed_Retrieval": seeded["Actual_Retrieval"],
        "Alert_Generated": seeded["Alert_Actual"],
        "Expansion_Gate": seeded["Expansion_Gate_Actual"],
        "Remediation": "Restore Finance-only connector ACL mapping and rerun affected regression subset",
        "Synthetic_Status": "Closed after successful remediation retest" if remediation_pass else "Open",
        "Evidence_Classification": config["evidence_classification"]
    }
    EXCEPTION_OUT.write_text(json.dumps(exception, indent=2), encoding="utf-8")

    summary = {
        "AI_System": config["ai_system"],
        "Risk_ID": config["risk_id"],
        "Control_ID": config["control_id"],
        "Control_Name": config["control_name"],
        "Executed_Assertions": len(rows),
        "Passed_Control_Outcomes": sum(1 for r in rows if r["Result"] == "PASS"),
        "Failed_Control_Outcomes": sum(1 for r in rows if r["Result"] != "PASS"),
        "Seeded_Authorization_Defects": 1,
        "Seeded_Defects_Detected": 1 if seeded["Result"] == "PASS" else 0,
        "Critical_Failures_Gate_Blocked": 1 if seeded["Expansion_Gate_Actual"] == "BLOCK" else 0,
        "Remediation_Retest_Passed": remediation_pass,
        "Final_Expansion_Gate": gate_state,
        "Evidence_State": "Designed -> Synthetic technical execution demonstrated -> Synthetic control operation tested",
        "Production_Operating_Effectiveness": "Not established"
    }
    SUMMARY_OUT.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(json.dumps(summary, indent=2))

    if summary["Failed_Control_Outcomes"] != 0:
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
