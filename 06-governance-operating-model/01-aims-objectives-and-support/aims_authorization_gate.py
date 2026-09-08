#!/usr/bin/env python3
"""Synthetic AIMS competence eligibility gate for the Duckworks portfolio.

The script blocks expired, overdue, suspended, out-of-scope, incomplete or
below-threshold records. It cannot appoint a person or grant authorization.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path
import json
import sys

BASE = Path(__file__).resolve().parent
CONFIG = BASE / "authorization_gate_config.json"
OUTPUT = BASE / "Duckworks_AIMS_Authorization_Gate_Run_Summary.json"


def evaluate(record: dict, as_of: date) -> dict:
    reasons = []
    if not record["training_completed"]:
        reasons.append("TRAINING_INCOMPLETE")
    if record["assessment_score"] < record["assessment_threshold"]:
        reasons.append("ASSESSMENT_BELOW_THRESHOLD")
    if date.fromisoformat(record["authorization_expiry"]) < as_of:
        reasons.append("AUTHORIZATION_EXPIRED")
    if date.fromisoformat(record["refresher_due"]) < as_of:
        reasons.append("REFRESHER_OVERDUE")
    if record["suspension_active"]:
        reasons.append("SUSPENSION_ACTIVE")
    if not record["scope_match"]:
        reasons.append("SCOPE_MISMATCH")
    result = "BLOCKED" if reasons else "ELIGIBLE_FOR_HUMAN_AUTHORIZATION"
    return {
        "record_id": record["record_id"],
        "activity": record["activity"],
        "result": result,
        "reasons": reasons,
        "expected_result": record["expected_result"],
        "expected_result_met": result == record["expected_result"],
        "authorization_granted": False,
    }


def main() -> int:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    as_of = date.fromisoformat(config["as_of_date"])
    results = [evaluate(record, as_of) for record in config["records"]]
    summary = {
        "gate_id": config["gate_id"],
        "as_of_date": config["as_of_date"],
        "records_evaluated": len(results),
        "eligible_for_human_authorization": sum(r["result"].startswith("ELIGIBLE") for r in results),
        "blocked_records": sum(r["result"] == "BLOCKED" for r in results),
        "expired_authorizations_blocked": sum("AUTHORIZATION_EXPIRED" in r["reasons"] for r in results),
        "below_threshold_assessments_blocked": sum("ASSESSMENT_BELOW_THRESHOLD" in r["reasons"] for r in results),
        "expected_results_met": sum(r["expected_result_met"] for r in results),
        "failed_assertions": sum(not r["expected_result_met"] for r in results),
        "human_authorization_required": config["human_authorization_required"],
        "authorizations_granted_by_script": 0,
        "evidence_boundary": config["evidence_boundary"],
        "results": results,
    }
    OUTPUT.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 1 if summary["failed_assertions"] else 0


if __name__ == "__main__":
    sys.exit(main())
