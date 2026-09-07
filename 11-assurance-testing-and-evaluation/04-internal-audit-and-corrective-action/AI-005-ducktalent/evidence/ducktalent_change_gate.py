#!/usr/bin/env python3
"""Synthetic DuckTalent change-gate control for CAPA-2026-001.

This portfolio demonstration does not process real applicant data and does not
establish production effectiveness or deployment authorization.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_EVIDENCE = {
    "risk_assessment",
    "impact_assessment",
    "rights_assessment",
    "privacy_assessment",
    "model_change_record",
    "dt02_result",
}
REQUIRED_ATTESTATIONS = {"technical_owner", "hr_process_owner"}


def assess(case: dict, baseline: dict) -> dict:
    approved = set(baseline["approved_features"])
    proposed = set(case["proposed_features"])
    unapproved = sorted(proposed - approved)

    baseline_weights = baseline["weights"]
    proposed_weights = case["proposed_weights"]
    changed_weights = sorted(
        key
        for key in set(baseline_weights) | set(proposed_weights)
        if baseline_weights.get(key) != proposed_weights.get(key)
    )
    declared = set(case.get("declared_weight_changes", []))
    undeclared_weight_changes = sorted(set(changed_weights) - declared)

    missing_evidence = sorted(REQUIRED_EVIDENCE - set(case.get("evidence_ids", {})))
    missing_attestations = sorted(
        key
        for key in REQUIRED_ATTESTATIONS
        if not case.get("attestations", {}).get(key, False)
    )
    dt02_status = case.get("evidence_ids", {}).get("dt02_result", {}).get("status")

    reasons = []
    if unapproved:
        reasons.append("UNAPPROVED_FEATURE")
    if undeclared_weight_changes:
        reasons.append("UNDECLARED_WEIGHT_CHANGE")
    if missing_evidence:
        reasons.append("MISSING_MANDATORY_EVIDENCE")
    if dt02_status not in {None, "pass"}:
        reasons.append("DT02_NOT_PASSING")
    if missing_attestations:
        reasons.append("MISSING_OWNER_ATTESTATION")

    decision = "blocked" if reasons else "eligible_for_governance_review"
    return {
        "case_id": case["case_id"],
        "decision": decision,
        "expected_decision": case["expected_decision"],
        "expected_result_met": decision == case["expected_decision"],
        "unapproved_features": unapproved,
        "changed_weights": changed_weights,
        "undeclared_weight_changes": undeclared_weight_changes,
        "missing_evidence": missing_evidence,
        "missing_attestations": missing_attestations,
        "reasons": reasons,
        "deployment_authorized": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    payload = json.loads(args.input.read_text(encoding="utf-8"))
    results = [assess(case, payload["baseline"]) for case in payload["cases"]]
    summary = {
        "control": "DuckTalent evidence-enforced change gate",
        "capa_id": "CAPA-2026-001",
        "evidence_boundary": "synthetic portfolio demonstration only",
        "total_cases": len(results),
        "expected_results_met": sum(r["expected_result_met"] for r in results),
        "blocked_cases": sum(r["decision"] == "blocked" for r in results),
        "governance_review_eligible_cases": sum(
            r["decision"] == "eligible_for_governance_review" for r in results
        ),
        "deployment_authorizations": 0,
        "overall_status": "pass" if all(r["expected_result_met"] for r in results) else "fail",
        "results": results,
    }
    args.output.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0 if summary["overall_status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
