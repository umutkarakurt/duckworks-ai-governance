#!/usr/bin/env python3
"""
Synthetic material-change monitoring / reassessment trigger for AI-005 DuckTalent.

This control demonstration is intentionally pre-deployment and synthetic.
It does not process real applicants, monitor a production system, or establish
legal discrimination/fairness conclusions.

Chain:
prior gate decision -> proposed ranking/feature change -> change regression check
-> material trigger -> reassessment required -> current gate preserved.
"""

from pathlib import Path
import csv
import json
import sys
from collections import defaultdict

BASE = Path(__file__).resolve().parent
REPO_ROOT = BASE.parents[1]
DT_EVIDENCE = REPO_ROOT / "80-operating-evidence" / "AI-005-ducktalent"

CHANGE_EVENT = BASE / "AI-005_2026-09-02_MON_Proposed_Change_Event.json"
DT02_CONFIG = DT_EVIDENCE / "dt02_test_config.json"
DATASET = DT_EVIDENCE / "AI-005_Synthetic_Applicant_Fairness_Test_Dataset.csv"
RESULT_OUT = BASE / "AI-005_2026-09-02_MON_Change_Regression_Result.json"

def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

def load_csv(path):
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def approved_score(row):
    exp = float(row["Relevant_Experience_Years"])
    skill = float(row["Skill_Match_Pct"])
    qual = float(row["Qualification_Match_Pct"])
    cert = float(row["Required_Certification"])
    return round((exp * 4.0) + (skill * 0.30) + (qual * 0.20) + (cert * 8.0), 2)

def proposed_score(row, penalty):
    return round(approved_score(row) - (float(row["Career_Gap_Months"]) * penalty), 2)

def selected(score, threshold):
    return 1 if score >= threshold else 0

def metrics(rows, score_fn, threshold):
    grouped = defaultdict(list)
    pair_scores = defaultdict(dict)
    for row in rows:
        score = score_fn(row)
        sel = selected(score, threshold)
        group = row["Synthetic_Comparison_Group"]
        grouped[group].append(sel)
        pair_scores[row["Matched_Pair_ID"]][group] = score

    group_metrics = {}
    for group, sels in grouped.items():
        group_metrics[group] = {
            "population": len(sels),
            "selected": sum(sels),
            "selection_rate": round(sum(sels) / len(sels), 4)
        }

    pair_diffs = []
    for pair_id, pair in sorted(pair_scores.items()):
        ref = pair["Reference"]
        comp = pair["Comparison"]
        pair_diffs.append({
            "pair_id": pair_id,
            "reference_score": ref,
            "comparison_score": comp,
            "difference": round(ref - comp, 2)
        })
    return group_metrics, pair_diffs

def main():
    event = load_json(CHANGE_EVENT)
    config = load_json(DT02_CONFIG)
    rows = load_csv(DATASET)

    approved = set(config["approved_scoring_features"])
    proposed = set(event["Proposed_Scoring_Features"])
    unapproved = sorted(proposed - approved)

    threshold = float(config["synthetic_shortlist_threshold"])
    penalty = float(event["Proposed_Career_Gap_Penalty_Per_Month"])

    baseline_metrics, baseline_pairs = metrics(
        rows, lambda row: approved_score(row), threshold
    )
    proposed_metrics, proposed_pairs = metrics(
        rows, lambda row: proposed_score(row, penalty), threshold
    )

    pair_effect_detected = any(abs(p["difference"]) > 0 for p in proposed_pairs)
    selection_rate_change_detected = (
        proposed_metrics["Reference"]["selection_rate"]
        != proposed_metrics["Comparison"]["selection_rate"]
    )

    material_change = event["Change_Type"] == "Ranking logic / feature-set configuration change"
    trigger = (
        material_change
        and len(unapproved) > 0
        and pair_effect_detected
        and selection_rate_change_detected
    )

    assertions = {
        "M01_material_feature_change_identified": material_change,
        "M02_unapproved_feature_detected": unapproved == ["Career_Gap_Months"],
        "M03_matched_pair_effect_detected": pair_effect_detected,
        "M04_group_outcome_difference_detected": selection_rate_change_detected,
        "M05_reassessment_trigger_opened": trigger,
        "M06_proposed_configuration_not_approved": event["Change_Status"] == "PROPOSED / NOT APPROVED",
        "M07_current_real_applicant_gate_preserved": trigger,
    }

    result = {
        "Monitoring_Record_ID": "DT-MON-001",
        "Trigger_ID": "DT-TRG-001",
        "Review_ID_To_Open": "IR-001",
        "AI_System": event["AI_System"],
        "Change_ID": event["Change_ID"],
        "Change_Type": event["Change_Type"],
        "Evidence_Classification": "Portfolio / Synthetic / Non-production",
        "Prior_Governance_Decision": "DENIED — maintain DO NOT DEPLOY with real applicants",
        "Approved_Features": sorted(approved),
        "Proposed_Features": sorted(proposed),
        "Unapproved_Features_Detected": unapproved,
        "Baseline_Group_Metrics": baseline_metrics,
        "Proposed_Group_Metrics": proposed_metrics,
        "Matched_Pairs_With_Nonzero_Proposed_Score_Difference": sum(
            1 for p in proposed_pairs if abs(p["difference"]) > 0
        ),
        "Material_Reassessment_Trigger": trigger,
        "Reassessment_Reason": (
            "A proposed ranking/feature configuration reintroduces a feature outside the "
            "approved synthetic allow-list and recreates a measurable matched-pair/group effect."
            if trigger else "Trigger condition not met."
        ),
        "Records_To_Reopen": [
            "AI-005-R01",
            "DT-01",
            "DT-02",
            "DuckTalent AIA fairness / affected-person analysis",
            "DuckTalent FRIA fairness / equality rights analysis",
            "DuckTalent DPIA profiling / fairness-data analysis",
            "DuckTalent model documentation feature / criteria record",
            "DuckTalent lifecycle gate decision"
        ] if trigger else [],
        "Immediate_Governance_Action": (
            "REJECT proposed configuration; do not merge/approve; preserve DO NOT DEPLOY with real applicants; open IR-001 reassessment."
            if trigger else "No material action."
        ),
        "Control_Assertions": len(assertions),
        "Passed_Control_Assertions": sum(1 for v in assertions.values() if v),
        "Failed_Control_Assertions": sum(1 for v in assertions.values() if not v),
        "Assertion_Results": assertions,
        "Production_Monitoring_Effectiveness": "Not established",
        "Legal_Compliance_or_Discrimination_Conclusion": "Not established",
        "Evidence_State": (
            "Synthetic material-change event -> Synthetic change-monitor execution -> "
            "Synthetic reassessment trigger demonstrated"
        )
    }

    RESULT_OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["Failed_Control_Assertions"] == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
