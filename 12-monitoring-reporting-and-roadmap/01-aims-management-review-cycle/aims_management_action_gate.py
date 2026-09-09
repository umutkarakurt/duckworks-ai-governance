#!/usr/bin/env python3
"""Evaluate synthetic AIMS management actions without closing or authorizing them."""

from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import date
from pathlib import Path


BASE = Path(__file__).resolve().parent


def evaluate(row: dict[str, str], as_of: date) -> tuple[str, list[str]]:
    status = row["Status"].strip().lower()
    due = date.fromisoformat(row["Due_Date"])
    reasons: list[str] = []

    if status == "closed":
        return "CLOSED_REQUIRES_HUMAN_VERIFICATION", ["RECORDED_CLOSED"]
    if due < as_of:
        reasons.append("DUE_DATE_PASSED")
        return "ESCALATE_OVERDUE", reasons
    if status == "blocked":
        reasons.append("DEPENDENCY_BLOCKED")
        return "BLOCKED_DEPENDENCY", reasons
    reasons.append("OPEN_NOT_YET_DUE")
    return "MONITOR_OPEN", reasons


def main() -> None:
    config = json.loads((BASE / "management_action_gate_config.json").read_text())
    as_of = date.fromisoformat(config["as_of_date"])
    with (BASE / config["tracker_file"]).open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))

    results = []
    for row in rows:
        result, reasons = evaluate(row, as_of)
        expected = config["expected_results"][row["Action_ID"]]
        results.append(
            {
                "action_id": row["Action_ID"],
                "owner": row["Owner"],
                "due_date": row["Due_Date"],
                "recorded_status": row["Status"],
                "result": result,
                "reasons": reasons,
                "expected_result": expected,
                "expected_result_met": result == expected,
                "action_closed_by_script": False,
            }
        )

    counts = Counter(item["result"] for item in results)
    expected_met = sum(item["expected_result_met"] for item in results)
    summary = {
        "gate_id": config["gate_id"],
        "as_of_date": config["as_of_date"],
        "actions_evaluated": len(results),
        "expected_results_met": expected_met,
        "failed_assertions": len(results) - expected_met,
        "overdue_escalations": counts["ESCALATE_OVERDUE"],
        "blocked_dependencies": counts["BLOCKED_DEPENDENCY"],
        "open_monitoring": counts["MONITOR_OPEN"],
        "recorded_closed": counts["CLOSED_REQUIRES_HUMAN_VERIFICATION"],
        "actions_auto_closed": 0,
        "human_decision_required": config["human_decision_required"],
        "evidence_boundary": config["evidence_boundary"],
        "results": results,
    }
    (BASE / config["summary_file"]).write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    if summary["failed_assertions"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

