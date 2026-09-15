from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
E = ROOT / "evidence" / "generated"


def load(rel):
    return json.loads((E / rel).read_text(encoding="utf-8"))


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    s = load("campaign-summary.json")

    require(s["profiles"]["vulnerable"] == {"tests": 12, "pass": 0, "fail": 12}, "vulnerable profile mismatch")
    require(s["profiles"]["hardened"] == {"tests": 12, "pass": 12, "fail": 0}, "hardened profile mismatch")
    require(s["production_effectiveness_claim"] is False, "production effectiveness must remain false")
    require(s["forecast_accuracy_claim"] is False, "forecast accuracy claim must remain false")
    require(s["legal_compliance_claim"] is False, "legal compliance claim must remain false")
    require(s["risk_score_change_authorized"] is False, "risk score change must remain false")
    require(s["governance_gate_change_authorized"] is False, "governance gate change must remain false")
    require(s["evidence_id_allocation_authorized"] is False, "canonical evidence IDs must remain unallocated")
    require(s["iaf_2026_003_closure_authorized"] is False, "IAF-2026-003 must remain open")
    require(s["assumption_closure_authorized"] is False, "assumptions must remain open")
    require(s["current_governance_position"] == "CONTINUE_WITH_MONITORING", "governance position changed")

    sha = os.environ.get("GITHUB_SHA")
    require(s["source_commit"] == (sha if sha else "LOCAL_UNBOUND"), "source commit binding mismatch")

    t1 = load("hardened/FFSEC-T001.json")
    require(t1["actual"]["batch_quarantined"] is True, "poisoned batch not quarantined")
    require(t1["actual"]["batch_entered_approved_snapshot"] is False, "poisoned batch entered approved snapshot")
    require(t1["actual"]["forecast_generated_from_batch"] is False, "forecast generated from poisoned batch")

    t2 = load("hardened/FFSEC-T002.json")
    require(t2["actual"]["backfill_blocked"] is True, "unapproved backfill not blocked")
    require(t2["actual"]["review_required"] is True, "backfill review not required")
    require(t2["actual"]["approved_history_hash_after"] == t2["actual"]["approved_history_hash_before"], "approved history changed")

    t3 = load("hardened/FFSEC-T003.json")
    require(t3["actual"]["training_serving_skew_detected"] is True, "training-serving skew not detected")
    require(t3["actual"]["scoring_allowed"] is False, "skewed scoring allowed")
    require(t3["actual"]["promotion_allowed"] is False, "skewed promotion allowed")

    t5 = load("hardened/FFSEC-T005.json")
    require(t5["actual"]["material_change_detected"] is True, "model/config change not detected")
    require(t5["actual"]["prior_validation_invalidated"] is True, "prior validation not invalidated")
    require(t5["actual"]["promotion_allowed"] is False, "unvalidated changed baseline promoted")

    t6 = load("hardened/FFSEC-T006.json")
    require(t6["actual"]["quality_case"]["classification"] == "DATA_QUALITY", "quality case misclassified")
    require(t6["actual"]["drift_case"]["classification"] == "DRIFT", "drift case misclassified")
    require(t6["actual"]["automatic_promotion"] is False, "automatic promotion occurred")

    t8 = load("hardened/FFSEC-T008.json")
    require(t8["actual"]["commitment_blocked"] is True, "material commitment not blocked")
    require(t8["actual"]["direct_commitment_created"] is False, "direct commitment created without approval")
    require(t8["actual"]["approval_bypass_possible"] is False, "approval bypass remains possible")

    t10 = load("hardened/FFSEC-T010.json")
    require(t10["actual"]["access_decision"] == "DENY", "unauthorized access not denied")
    require(t10["actual"]["access_logged"] is True, "unauthorized access not logged")
    require(t10["actual"]["commercial_canary_in_response"] is False, "commercial canary leaked in response")
    require(t10["actual"]["commercial_canary_in_export"] is False, "commercial canary leaked in export")

    t11 = load("hardened/FFSEC-T011.json")
    require(t11["actual"]["forecast_marked_stale"] is True, "stale forecast not marked")
    require(t11["actual"]["manual_or_degraded_mode_active"] is True, "manual/degraded mode not active")
    require(t11["actual"]["decision_support_allowed_from_stale_forecast"] is False, "stale forecast still usable")

    t12 = load("hardened/FFSEC-T012.json")
    require(t12["actual"]["promotion_blocked"] is True, "unvalidated retraining promotion not blocked")
    require(t12["actual"]["known_good_state_restored"] is True, "known-good state not restored")
    require(t12["actual"]["rollback_model_matches"] is True, "rollback model mismatch")
    require(t12["actual"]["rollback_config_matches"] is True, "rollback config mismatch")
    require(t12["actual"]["rollback_data_matches"] is True, "rollback data mismatch")

    print("PASS: FeatherForecast campaign semantic verification")
    print("vulnerable=12/12 seeded unsafe outcomes reproduced")
    print("hardened=12/12 control assertions passed")
    print("production_effectiveness_claim=false")
    print("forecast_accuracy_claim=false")
    print("IAF-2026-003 closure=false")
    print("governance_position=CONTINUE_WITH_MONITORING")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise
