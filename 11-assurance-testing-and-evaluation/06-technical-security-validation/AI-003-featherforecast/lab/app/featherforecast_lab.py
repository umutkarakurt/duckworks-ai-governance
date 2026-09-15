from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass
from typing import Any, Dict, List

LAB_VERSION = "featherforecast-lab-0.1.0"
ARCH_VERSION = "DW-AI003-ARCH-SEC-01 v1.0"
THREAT_VERSION = "DW-AI003-TM-01 v1.0"
PLAN_VERSION = "DW-AI003-VAL-SEC-01 v1.0"

DATA_SCHEMA_VERSION = "ff-data-schema-1.0"
FEATURE_VERSION = "ff-feature-pipeline-1.0"
MODEL_VERSION = "northstar-sim-forecast-model-1.0"
CONFIG_VERSION = "ff-config-1.0"
THRESHOLD_VERSION = "ff-threshold-policy-1.0"

COMMERCIAL_CANARY = "FF_COMMERCIAL_PLANNING_CANARY_92C"
KNOWN_GOOD_MODEL = "northstar-sim-forecast-model-1.0"
KNOWN_GOOD_CONFIG = "ff-config-1.0"
KNOWN_GOOD_DATA = "ff-approved-snapshot-2026w37"


@dataclass(frozen=True)
class CaseDef:
    test_id: str
    threats: List[str]
    risks: List[str]
    controls: List[str]
    requirements: List[str]


CASE_DEFS = {
    "FFSEC-T001": CaseDef(
        "FFSEC-T001",
        ["FFT-001", "FFT-002", "FFT-003", "FFT-004"],
        ["AI-003-R01", "AI-003-R02"],
        ["FF-02", "FF-04"],
        ["FF-SR-002", "FF-SR-003", "FF-SR-004", "FF-SR-005", "FF-SR-007"],
    ),
    "FFSEC-T002": CaseDef(
        "FFSEC-T002",
        ["FFT-005", "FFT-006", "FFT-007", "FFT-008"],
        ["AI-003-R01", "AI-003-R02"],
        ["FF-02", "FF-04"],
        ["FF-SR-003", "FF-SR-006", "FF-SR-007", "FF-SR-035"],
    ),
    "FFSEC-T003": CaseDef(
        "FFSEC-T003",
        ["FFT-010", "FFT-011", "FFT-012"],
        ["AI-003-R01", "AI-003-R02"],
        ["FF-02", "FF-03"],
        ["FF-SR-008", "FF-SR-009", "FF-SR-010", "FF-SR-013"],
    ),
    "FFSEC-T004": CaseDef(
        "FFSEC-T004",
        ["FFT-009", "FFT-014"],
        ["AI-003-R01", "AI-003-R02"],
        ["FF-02", "AI-GOV-02"],
        ["FF-SR-007", "FF-SR-008", "FF-SR-011", "FF-SR-013", "FF-SR-034"],
    ),
    "FFSEC-T005": CaseDef(
        "FFSEC-T005",
        ["FFT-015", "FFT-016", "FFT-040"],
        ["AI-003-R01", "AI-003-R02"],
        ["FF-02", "FF-03", "AI-GOV-02"],
        ["FF-SR-011", "FF-SR-012", "FF-SR-013", "FF-SR-015", "FF-SR-034"],
    ),
    "FFSEC-T006": CaseDef(
        "FFSEC-T006",
        ["FFT-017", "FFT-018", "FFT-019", "FFT-020", "FFT-021", "FFT-022", "FFT-023", "FFT-024"],
        ["AI-003-R01", "AI-003-R02"],
        ["FF-02", "FF-03"],
        ["FF-SR-010", "FF-SR-013", "FF-SR-014", "FF-SR-018", "FF-SR-019", "FF-SR-034"],
    ),
    "FFSEC-T007": CaseDef(
        "FFSEC-T007",
        ["FFT-025", "FFT-026", "FFT-027"],
        ["AI-003-R01", "AI-003-R02"],
        ["FF-01", "FF-02"],
        ["FF-SR-015", "FF-SR-016", "FF-SR-017", "FF-SR-020"],
    ),
    "FFSEC-T008": CaseDef(
        "FFSEC-T008",
        ["FFT-028", "FFT-029", "FFT-031", "FFT-032"],
        ["AI-003-R01"],
        ["FF-01"],
        ["FF-SR-020", "FF-SR-021", "FF-SR-022", "FF-SR-038"],
    ),
    "FFSEC-T009": CaseDef(
        "FFSEC-T009",
        ["FFT-030", "FFT-047", "FFT-048"],
        ["AI-003-R01", "AI-003-R03"],
        ["FF-01", "FF-04"],
        ["FF-SR-022", "FF-SR-023", "FF-SR-032", "FF-SR-036"],
    ),
    "FFSEC-T010": CaseDef(
        "FFSEC-T010",
        ["FFT-033", "FFT-034", "FFT-035", "FFT-036", "FFT-037", "FFT-038", "FFT-039"],
        ["AI-003-R03"],
        ["FF-04"],
        ["FF-SR-001", "FF-SR-024", "FF-SR-025", "FF-SR-026", "FF-SR-027", "FF-SR-033"],
    ),
    "FFSEC-T011": CaseDef(
        "FFSEC-T011",
        ["FFT-041", "FFT-042", "FFT-043"],
        ["AI-003-R01", "AI-003-R02"],
        ["FF-01", "FF-03", "AI-INC-01"],
        ["FF-SR-017", "FF-SR-028", "FF-SR-029", "FF-SR-032", "FF-SR-033"],
    ),
    "FFSEC-T012": CaseDef(
        "FFSEC-T012",
        ["FFT-020", "FFT-024", "FFT-045", "FFT-046"],
        ["AI-003-R01", "AI-003-R02"],
        ["FF-02", "FF-03", "AI-GOV-02", "AI-INC-01"],
        ["FF-SR-011", "FF-SR-012", "FF-SR-013", "FF-SR-014", "FF-SR-030", "FF-SR-031", "FF-SR-034"],
    ),
}


def _sha(data: Any) -> str:
    raw = json.dumps(data, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _hash_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _base_result(case: CaseDef, profile: str) -> Dict[str, Any]:
    source_fixture = {
        "fixture_id": f"FF-FIX-{case.test_id[-3:]}",
        "approved_data_snapshot": KNOWN_GOOD_DATA,
        "schema_version": DATA_SCHEMA_VERSION,
    }
    forecast_content = f"{case.test_id}:{profile}:forecast=synthetic"
    return {
        "test_id": case.test_id,
        "threat_ids": case.threats,
        "risk_ids": case.risks,
        "control_ids": case.controls,
        "requirement_ids": case.requirements,
        "profile": profile,
        "architecture_version": ARCH_VERSION,
        "threat_model_version": THREAT_VERSION,
        "validation_plan_version": PLAN_VERSION,
        "lab_version": LAB_VERSION,
        "source_fixture": source_fixture,
        "source_fixture_hash": _sha(source_fixture),
        "data_snapshot_version": KNOWN_GOOD_DATA,
        "feature_schema_version": FEATURE_VERSION,
        "model_version": MODEL_VERSION,
        "config_version": CONFIG_VERSION,
        "threshold_version": THRESHOLD_VERSION,
        "forecast_id": f"FF-FC-{case.test_id[-3:]}-{profile}",
        "forecast_hash": _hash_text(forecast_content),
        "forecast_stale": False,
        "manager_approval_state": "NOT_APPLICABLE",
        "access_decision": "NOT_APPLICABLE",
        "rollback_state": "NOT_APPLICABLE",
        "correlation_id": f"corr-{case.test_id.lower()}-{profile}",
        "production_effectiveness_claim": False,
        "forecast_accuracy_claim": False,
        "legal_compliance_claim": False,
        "limitations": [
            "deterministic synthetic forecasting-pipeline and decision-control surrogate",
            "no real Duckworks planning, procurement, production or supplier system",
            "no real Northstar service, contract, model or telemetry evidence",
            "no production forecast-accuracy, control-effectiveness, supplier-assurance or legal-compliance conclusion",
        ],
    }


def _finish(
    result: Dict[str, Any],
    passed: bool,
    expected: Dict[str, Any],
    actual: Dict[str, Any],
    detection: Dict[str, Any],
) -> Dict[str, Any]:
    result["expected"] = expected
    result["actual"] = actual
    result["detection"] = detection
    result["result"] = "PASS" if passed else "FAIL"
    tmp = copy.deepcopy(result)
    tmp.pop("evidence_sha256", None)
    result["evidence_sha256"] = _sha(tmp)
    return result


def run_case(test_id: str, profile: str) -> Dict[str, Any]:
    if test_id not in CASE_DEFS:
        raise KeyError(test_id)
    if profile not in {"vulnerable", "hardened"}:
        raise ValueError(profile)

    case = CASE_DEFS[test_id]
    r = _base_result(case, profile)
    hard = profile == "hardened"

    if test_id == "FFSEC-T001":
        actual = {
            "source_batch_id": "BATCH-POISON-001",
            "source_approved": False,
            "demand_value": 99999,
            "maximum_defined_synthetic_value": 5000,
            "poison_or_extreme_value_detected": hard,
            "batch_quarantined": hard,
            "batch_entered_approved_snapshot": not hard,
            "forecast_generated_from_batch": not hard,
        }
        detection = {"source_integrity_or_range_event": hard}
        passed = hard and actual["batch_quarantined"] and not actual["batch_entered_approved_snapshot"] and not actual["forecast_generated_from_batch"]
        return _finish(r, passed, {
            "batch_quarantined": True,
            "batch_entered_approved_snapshot": False,
            "forecast_generated_from_batch": False,
        }, actual, detection)

    if test_id == "FFSEC-T002":
        approved_history = "2026w01:100|2026w02:105|2026w03:103"
        proposed_history = "2026w01:100|2026w02:8000|2026w03:103"
        r["source_fixture"]["approved_history_hash"] = _hash_text(approved_history)
        actual = {
            "backfill_authorized": False,
            "approved_history_hash_before": _hash_text(approved_history),
            "proposed_history_hash": _hash_text(proposed_history),
            "backfill_applied": not hard,
            "review_required": hard,
            "backfill_blocked": hard,
            "approved_history_hash_after": _hash_text(approved_history if hard else proposed_history),
            "lineage_preserved": hard,
        }
        detection = {"historical_revision_review_event": hard}
        passed = hard and actual["backfill_blocked"] and actual["review_required"] and actual["lineage_preserved"] and actual["approved_history_hash_after"] == actual["approved_history_hash_before"]
        return _finish(r, passed, {
            "backfill_applied": False,
            "review_required": True,
            "approved_history_hash_preserved": True,
        }, actual, detection)

    if test_id == "FFSEC-T003":
        training_schema = ["demand_lag_1", "inventory", "lead_time_days"]
        scoring_schema = ["demand_lag_1", "inventory", "supplier_priority"]
        actual = {
            "training_schema_hash": _sha(training_schema),
            "scoring_schema_hash": _sha(scoring_schema),
            "schema_match": training_schema == scoring_schema,
            "training_serving_skew_detected": hard,
            "scoring_allowed": not hard,
            "promotion_allowed": not hard,
        }
        detection = {"training_serving_skew_event": hard}
        passed = hard and not actual["schema_match"] and actual["training_serving_skew_detected"] and not actual["scoring_allowed"] and not actual["promotion_allowed"]
        return _finish(r, passed, {
            "training_serving_skew_detected": True,
            "scoring_allowed": False,
            "promotion_allowed": False,
        }, actual, detection)

    if test_id == "FFSEC-T004":
        actual = {
            "approved_feature_version": FEATURE_VERSION,
            "observed_feature_version": "ff-feature-pipeline-1.1-unapproved",
            "approved_data_snapshot": KNOWN_GOOD_DATA,
            "observed_data_snapshot": "ff-unapproved-snapshot-backfill",
            "unauthorized_change_detected": hard,
            "revalidation_required": hard,
            "changed_pipeline_used": not hard,
            "promotion_allowed": not hard,
        }
        detection = {"feature_or_snapshot_change_event": hard}
        passed = hard and actual["unauthorized_change_detected"] and actual["revalidation_required"] and not actual["changed_pipeline_used"] and not actual["promotion_allowed"]
        return _finish(r, passed, {
            "unauthorized_change_detected": True,
            "revalidation_required": True,
            "changed_pipeline_used": False,
            "promotion_allowed": False,
        }, actual, detection)

    if test_id == "FFSEC-T005":
        actual = {
            "approved_model_version": MODEL_VERSION,
            "observed_model_version": "northstar-sim-forecast-model-1.1-unapproved",
            "approved_config_version": CONFIG_VERSION,
            "observed_config_version": "ff-config-1.1-unapproved",
            "approved_threshold_version": THRESHOLD_VERSION,
            "observed_threshold_version": "ff-threshold-policy-0.5-weakened",
            "material_change_detected": hard,
            "prior_validation_invalidated": hard,
            "promotion_allowed": not hard,
        }
        detection = {"model_config_threshold_change_event": hard}
        passed = hard and actual["material_change_detected"] and actual["prior_validation_invalidated"] and not actual["promotion_allowed"]
        return _finish(r, passed, {
            "material_change_detected": True,
            "prior_validation_invalidated": True,
            "promotion_allowed": False,
        }, actual, detection)

    if test_id == "FFSEC-T006":
        actual = {
            "quality_case": {
                "condition": "duplicate_records_and_missing_inventory",
                "classification": "DRIFT" if not hard else "DATA_QUALITY",
            },
            "drift_case": {
                "condition": "sustained_demand_distribution_shift",
                "classification": "HEALTHY" if not hard else "DRIFT",
            },
            "quality_and_drift_correctly_distinguished": hard,
            "retraining_triggered_for_defined_drift_case": hard,
            "review_required_before_promotion": hard,
            "automatic_promotion": not hard,
        }
        detection = {
            "data_quality_event": hard,
            "distribution_drift_event": hard,
        }
        passed = hard and actual["quality_case"]["classification"] == "DATA_QUALITY" and actual["drift_case"]["classification"] == "DRIFT" and actual["review_required_before_promotion"] and not actual["automatic_promotion"]
        return _finish(r, passed, {
            "quality_classification": "DATA_QUALITY",
            "drift_classification": "DRIFT",
            "automatic_promotion": False,
        }, actual, detection)

    if test_id == "FFSEC-T007":
        original = "forecast:product-A:week38:1200"
        mutated = "forecast:product-A:week38:9200"
        r["forecast_hash"] = _hash_text(original)
        r["forecast_stale"] = True
        actual = {
            "stored_forecast_hash": _hash_text(original),
            "observed_forecast_hash": _hash_text(mutated),
            "hash_match": _hash_text(original) == _hash_text(mutated),
            "forecast_age_hours": 72,
            "synthetic_freshness_limit_hours": 24,
            "forecast_stale": True,
            "version_binding_valid": False,
            "mutation_or_staleness_detected": hard,
            "forecast_invalidated": hard,
            "stale_presented_as_current": not hard,
            "decision_support_allowed": not hard,
        }
        detection = {"forecast_integrity_or_staleness_event": hard}
        passed = hard and not actual["hash_match"] and actual["forecast_stale"] and actual["forecast_invalidated"] and not actual["stale_presented_as_current"] and not actual["decision_support_allowed"]
        return _finish(r, passed, {
            "forecast_invalidated": True,
            "stale_presented_as_current": False,
            "decision_support_allowed": False,
        }, actual, detection)

    if test_id == "FFSEC-T008":
        r["manager_approval_state"] = "MISSING"
        actual = {
            "material_commitment_requested": True,
            "authorized_manager_approval_present": False,
            "approval_required": hard,
            "direct_commitment_created": not hard,
            "approval_bypass_possible": not hard,
            "commitment_blocked": hard,
        }
        detection = {"manager_approval_gate_denial_event": hard}
        passed = hard and actual["approval_required"] and actual["commitment_blocked"] and not actual["direct_commitment_created"] and not actual["approval_bypass_possible"]
        return _finish(r, passed, {
            "direct_commitment_created": False,
            "approval_bypass_possible": False,
            "commitment_blocked": True,
        }, actual, detection)

    if test_id == "FFSEC-T009":
        original = {
            "forecast_id": "FF-FC-009",
            "manager": "FF-MGR-SYN-001",
            "decision": "OVERRIDE",
            "rationale": "supplier capacity constraint",
        }
        tampered = dict(original)
        tampered["decision"] = "APPROVE"
        tampered["rationale"] = ""
        actual = {
            "original_record_hash": _sha(original),
            "observed_record_hash": _sha(tampered),
            "hash_match": _sha(original) == _sha(tampered),
            "tamper_detected": hard,
            "decision_evidence_valid": not hard,
            "investigation_required": hard,
        }
        detection = {"decision_record_integrity_event": hard}
        passed = hard and not actual["hash_match"] and actual["tamper_detected"] and not actual["decision_evidence_valid"] and actual["investigation_required"]
        return _finish(r, passed, {
            "tamper_detected": True,
            "decision_evidence_valid": False,
            "investigation_required": True,
        }, actual, detection)

    if test_id == "FFSEC-T010":
        r["access_decision"] = "DENY" if hard else "ALLOW"
        response = "[DENIED]" if hard else f"supplier_plan={COMMERCIAL_CANARY};forecast=1200"
        export = "" if hard else f"export:{COMMERCIAL_CANARY}"
        actual = {
            "requester_role": "unauthorized-contractor",
            "access_decision": r["access_decision"],
            "access_logged": hard,
            "commercial_canary_in_response": COMMERCIAL_CANARY in response,
            "commercial_canary_in_export": COMMERCIAL_CANARY in export,
            "response": response,
        }
        detection = {"unauthorized_access_denial_event": hard}
        passed = hard and actual["access_decision"] == "DENY" and actual["access_logged"] and not actual["commercial_canary_in_response"] and not actual["commercial_canary_in_export"]
        return _finish(r, passed, {
            "access_decision": "DENY",
            "access_logged": True,
            "commercial_canary_in_response": False,
            "commercial_canary_in_export": False,
        }, actual, detection)

    if test_id == "FFSEC-T011":
        r["forecast_stale"] = True
        actual = {
            "northstar_available": False,
            "source_feed_current": False,
            "last_forecast_age_hours": 96,
            "forecast_marked_stale": hard,
            "stale_presented_as_current": not hard,
            "manual_or_degraded_mode_active": hard,
            "decision_support_allowed_from_stale_forecast": not hard,
        }
        detection = {"platform_or_source_outage_event": hard}
        passed = hard and actual["forecast_marked_stale"] and actual["manual_or_degraded_mode_active"] and not actual["stale_presented_as_current"] and not actual["decision_support_allowed_from_stale_forecast"]
        return _finish(r, passed, {
            "forecast_marked_stale": True,
            "manual_or_degraded_mode_active": True,
            "decision_support_allowed_from_stale_forecast": False,
        }, actual, detection)

    if test_id == "FFSEC-T012":
        good_state = {
            "model": KNOWN_GOOD_MODEL,
            "config": KNOWN_GOOD_CONFIG,
            "data": KNOWN_GOOD_DATA,
        }
        proposed_state = {
            "model": "northstar-sim-forecast-model-1.1-unvalidated",
            "config": "ff-config-1.1-unvalidated",
            "data": "ff-poisoned-retrain-snapshot",
        }
        r["rollback_state"] = "VERIFIED_KNOWN_GOOD" if hard else "MISMATCHED_OR_UNVERIFIED"
        actual = {
            "retraining_data_approved": False,
            "challenger_validation_passed": False,
            "proposed_state_hash": _sha(proposed_state),
            "unvalidated_promotion_allowed": not hard,
            "promotion_blocked": hard,
            "known_good_state_hash": _sha(good_state),
            "known_good_state_restored": hard,
            "rollback_model_matches": hard,
            "rollback_config_matches": hard,
            "rollback_data_matches": hard,
            "revalidation_required": hard,
        }
        detection = {"unvalidated_promotion_or_rollback_event": hard}
        passed = hard and actual["promotion_blocked"] and actual["known_good_state_restored"] and actual["rollback_model_matches"] and actual["rollback_config_matches"] and actual["rollback_data_matches"] and actual["revalidation_required"] and not actual["unvalidated_promotion_allowed"]
        return _finish(r, passed, {
            "unvalidated_promotion_allowed": False,
            "known_good_state_restored": True,
            "rollback_model_matches": True,
            "rollback_config_matches": True,
            "rollback_data_matches": True,
        }, actual, detection)

    raise AssertionError(test_id)


def all_test_ids() -> List[str]:
    return list(CASE_DEFS.keys())
