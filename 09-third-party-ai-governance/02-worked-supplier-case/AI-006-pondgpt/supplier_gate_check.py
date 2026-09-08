#!/usr/bin/env python3
"""Deterministic synthetic supplier-gate check for the PondGPT portfolio case."""

from __future__ import annotations

import json
from pathlib import Path


BASE = Path(__file__).resolve().parent
CONFIG_PATH = BASE / "supplier_gate_config.json"
OUTPUT_PATH = BASE / "AI-006_LanternMind_Supplier_Gate_Run_Summary.json"


def main() -> int:
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    prohibited = [key for key, active in config["prohibited_conditions"].items() if active]
    unmet_broader = [item for item in config["broader_rollout_conditions"] if item["status"] != "met"]
    pilot_failures = [item for item in config["restricted_pilot_conditions"] if not item["status"].startswith("met")]

    if prohibited or pilot_failures:
        decision = "BLOCK_SUPPLIER_USE"
    elif unmet_broader:
        decision = "CONDITIONAL_RESTRICTED_PILOT_ONLY"
    else:
        decision = "ELIGIBLE_FOR_BROADER_GOVERNANCE_REVIEW"

    assertions = {
        "automatic_approval_disabled": config["automatic_approval_permitted"] is False,
        "no_prohibited_condition_active": not prohibited,
        "restricted_pilot_conditions_satisfied": not pilot_failures,
        "broader_rollout_has_blockers": bool(unmet_broader),
        "decision_matches_expected": decision == config["expected_decision"],
        "broader_rollout_not_approved": decision != "ELIGIBLE_FOR_BROADER_GOVERNANCE_REVIEW",
    }

    summary = {
        "gate_id": config["gate_id"],
        "system_id": config["system_id"],
        "supplier": config["supplier"],
        "decision": decision,
        "human_authorization_required": True,
        "unmet_broader_rollout_conditions": [item["id"] for item in unmet_broader],
        "prohibited_conditions_active": prohibited,
        "restricted_pilot_condition_failures": [item["id"] for item in pilot_failures],
        "assertions": assertions,
        "assertions_passed": sum(assertions.values()),
        "assertions_failed": len(assertions) - sum(assertions.values()),
        "evidence_boundary": "Synthetic portfolio execution; no production effectiveness or supplier approval claim"
    }
    OUTPUT_PATH.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0 if all(assertions.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())

