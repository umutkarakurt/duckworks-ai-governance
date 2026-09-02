#!/usr/bin/env python3
"""
Synthetic executable fairness-control demonstration for Duckworks Project W.I.N.G.

AI system: AI-005 — DuckTalent AI
Risk: AI-005-R01 — Fundamental rights & fairness
Preventive dependency: DT-01 — Job-Relevance Criteria & Proxy Feature Governance
Detective control: DT-02 — Pre-Deployment Fairness & Adverse-Impact Testing

Portfolio-only / synthetic / non-production.

This script does NOT:
- process real applicants;
- use real protected-characteristic data;
- establish legal discrimination;
- establish EU AI Act or employment-law compliance;
- define a legally meaningful adverse-impact threshold; or
- validate a real recruitment model.

It demonstrates an evidence-producing governance test:
approved features -> seeded unapproved proxy -> measurable outcome difference ->
deployment block -> remediation -> retest.
"""

from __future__ import annotations
from pathlib import Path
import csv
import json
import sys
from collections import defaultdict

BASE = Path(__file__).resolve().parent
DATASET = BASE / "AI-005_Synthetic_Applicant_Fairness_Test_Dataset.csv"
CONFIG = BASE / "dt02_test_config.json"
RESULTS_OUT = BASE / "AI-005_2026-09-02_FAIR_Fairness_Test_Results.csv"
EXCEPTION_OUT = BASE / "AI-005_2026-09-02_FAIR_Fairness_Exception.json"
SUMMARY_OUT = BASE / "AI-005_2026-09-02_FAIR_Fairness_Run_Summary.json"

RESULT_FIELDS = [
    "Applicant_ID","Matched_Pair_ID","Synthetic_Comparison_Group",
    "Approved_Feature_Score","Pre_Remediation_Score","Post_Remediation_Score",
    "Qualified_Label","Pre_Shortlisted","Post_Shortlisted",
    "Pre_Error_Type","Post_Error_Type","Control_Interpretation"
]

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def load_rows(path: Path):
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def approved_score(row):
    # Synthetic portfolio scoring function using only approved, job-related test features.
    exp = float(row["Relevant_Experience_Years"])
    skill = float(row["Skill_Match_Pct"])
    qual = float(row["Qualification_Match_Pct"])
    cert = float(row["Required_Certification"])
    return round((exp * 4.0) + (skill * 0.30) + (qual * 0.20) + (cert * 8.0), 2)

def pre_remediation_score(row):
    # Deliberately defective synthetic configuration:
    # career-gap penalty is not on the approved feature allow-list.
    return round(approved_score(row) - (float(row["Career_Gap_Months"]) * 0.80), 2)

def post_remediation_score(row):
    # Remediation removes the unapproved career-gap penalty.
    return approved_score(row)

def selected(score, threshold):
    return 1 if score >= threshold else 0

def error_type(qualified, selected_flag):
    if qualified == 1 and selected_flag == 0:
        return "FALSE_NEGATIVE"
    if qualified == 0 and selected_flag == 1:
        return "FALSE_POSITIVE"
    return "NONE"

def group_metrics(rows, stage):
    grouped = defaultdict(list)
    for r in rows:
        grouped[r["Synthetic_Comparison_Group"]].append(r)

    metrics = {}
    for group, items in grouped.items():
        selected_key = f"{stage}_Shortlisted"
        selected_count = sum(int(r[selected_key]) for r in items)
        qualified_count = sum(int(r["Qualified_Label"]) for r in items)
        tp = sum(1 for r in items if int(r["Qualified_Label"]) == 1 and int(r[selected_key]) == 1)
        fn = sum(1 for r in items if int(r["Qualified_Label"]) == 1 and int(r[selected_key]) == 0)
        fp = sum(1 for r in items if int(r["Qualified_Label"]) == 0 and int(r[selected_key]) == 1)
        metrics[group] = {
            "population": len(items),
            "selected": selected_count,
            "selection_rate": round(selected_count / len(items), 4) if items else None,
            "qualified": qualified_count,
            "true_positive_rate": round(tp / qualified_count, 4) if qualified_count else None,
            "false_negative_rate": round(fn / qualified_count, 4) if qualified_count else None,
            "false_positive_count": fp,
        }
    return metrics

def paired_score_differences(rows, stage_score_key):
    pairs = defaultdict(dict)
    for r in rows:
        pairs[r["Matched_Pair_ID"]][r["Synthetic_Comparison_Group"]] = r

    diffs = []
    for pair_id, pair in sorted(pairs.items()):
        ref = pair["Reference"]
        comp = pair["Comparison"]
        diffs.append({
            "pair_id": pair_id,
            "reference_score": float(ref[stage_score_key]),
            "comparison_score": float(comp[stage_score_key]),
            "difference": round(float(ref[stage_score_key]) - float(comp[stage_score_key]), 2),
        })
    return diffs

def main():
    config = load_json(CONFIG)
    rows = load_rows(DATASET)
    threshold = float(config["synthetic_shortlist_threshold"])

    # Feature-governance assertion.
    approved = set(config["approved_scoring_features"])
    pre_used_features = approved | {config["seeded_unapproved_feature"]}
    post_used_features = approved.copy()

    pre_feature_violation = sorted(pre_used_features - approved)
    post_feature_violation = sorted(post_used_features - approved)

    results = []
    for row in rows:
        approved_val = approved_score(row)
        pre = pre_remediation_score(row)
        post = post_remediation_score(row)
        qualified = selected(approved_val, threshold)
        pre_sel = selected(pre, threshold)
        post_sel = selected(post, threshold)

        results.append({
            "Applicant_ID": row["Applicant_ID"],
            "Matched_Pair_ID": row["Matched_Pair_ID"],
            "Synthetic_Comparison_Group": row["Synthetic_Comparison_Group"],
            "Approved_Feature_Score": f"{approved_val:.2f}",
            "Pre_Remediation_Score": f"{pre:.2f}",
            "Post_Remediation_Score": f"{post:.2f}",
            "Qualified_Label": str(qualified),
            "Pre_Shortlisted": str(pre_sel),
            "Post_Shortlisted": str(post_sel),
            "Pre_Error_Type": error_type(qualified, pre_sel),
            "Post_Error_Type": error_type(qualified, post_sel),
            "Control_Interpretation": (
                "Synthetic comparison only; no real protected characteristic, applicant, legal threshold, "
                "or production model is represented."
            )
        })

    with RESULTS_OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=RESULT_FIELDS)
        writer.writeheader()
        writer.writerows(results)

    pre_metrics = group_metrics(results, "Pre")
    post_metrics = group_metrics(results, "Post")
    pre_pairs = paired_score_differences(results, "Pre_Remediation_Score")
    post_pairs = paired_score_differences(results, "Post_Remediation_Score")

    seeded_detected = (
        pre_feature_violation == [config["seeded_unapproved_feature"]]
        and any(abs(p["difference"]) > 0 for p in pre_pairs)
    )
    deployment_gate_pre = "BLOCK" if seeded_detected else "OPEN"

    remediation_pass = (
        post_feature_violation == []
        and all(abs(p["difference"]) == 0 for p in post_pairs)
        and post_metrics["Reference"]["selection_rate"] == post_metrics["Comparison"]["selection_rate"]
        and post_metrics["Reference"]["true_positive_rate"] == post_metrics["Comparison"]["true_positive_rate"]
    )
    deployment_gate_post = "ELIGIBLE_FOR_FURTHER_GOVERNANCE_REVIEW" if remediation_pass else "BLOCK"

    exception = {
        "Exception_ID": config["seeded_issue"]["issue_id"],
        "AI_System": config["ai_system"],
        "Risk_ID": config["risk_id"],
        "Preventive_Dependency": config["preventive_dependency"],
        "Control_ID": config["control_id"],
        "Condition": config["seeded_issue"]["condition"],
        "Unapproved_Feature_Detected": pre_feature_violation,
        "Pre_Remediation_Reference_Selection_Rate": pre_metrics["Reference"]["selection_rate"],
        "Pre_Remediation_Comparison_Selection_Rate": pre_metrics["Comparison"]["selection_rate"],
        "Pre_Remediation_Reference_TPR": pre_metrics["Reference"]["true_positive_rate"],
        "Pre_Remediation_Comparison_TPR": pre_metrics["Comparison"]["true_positive_rate"],
        "Deployment_Gate": deployment_gate_pre,
        "Remediation": "Remove Career_Gap_Months from scoring; retain approved job-related feature set; rerun full synthetic test population.",
        "Post_Remediation_Status": "Synthetic retest passed" if remediation_pass else "Synthetic retest failed",
        "Legal_Interpretation": "None. Synthetic governance evidence only."
    }
    EXCEPTION_OUT.write_text(json.dumps(exception, indent=2), encoding="utf-8")

    control_assertions = {
        "A01_unapproved_feature_detected": seeded_detected,
        "A02_pre_remediation_gate_blocked": deployment_gate_pre == "BLOCK",
        "A03_group_metrics_generated": all(
            pre_metrics[g]["selection_rate"] is not None and pre_metrics[g]["true_positive_rate"] is not None
            for g in ["Reference", "Comparison"]
        ),
        "A04_matched_pair_effect_detected": any(abs(p["difference"]) > 0 for p in pre_pairs),
        "A05_unapproved_feature_removed": post_feature_violation == [],
        "A06_post_matched_pairs_equal_on_score": all(abs(p["difference"]) == 0 for p in post_pairs),
        "A07_post_selection_rates_equal_in_matched_synthetic_population":
            post_metrics["Reference"]["selection_rate"] == post_metrics["Comparison"]["selection_rate"],
        "A08_post_true_positive_rates_equal_in_matched_synthetic_population":
            post_metrics["Reference"]["true_positive_rate"] == post_metrics["Comparison"]["true_positive_rate"],
        "A09_retest_passed": remediation_pass,
        "A10_final_gate_not_auto_approved": deployment_gate_post == "ELIGIBLE_FOR_FURTHER_GOVERNANCE_REVIEW",
    }

    summary = {
        "AI_System": config["ai_system"],
        "Risk_ID": config["risk_id"],
        "Control_ID": config["control_id"],
        "Control_Name": config["control_name"],
        "Synthetic_Applicants": len(results),
        "Matched_Pairs": len(pre_pairs),
        "Control_Assertions": len(control_assertions),
        "Passed_Control_Assertions": sum(1 for v in control_assertions.values() if v),
        "Failed_Control_Assertions": sum(1 for v in control_assertions.values() if not v),
        "Seeded_Unapproved_Feature": config["seeded_unapproved_feature"],
        "Seeded_Issue_Detected": seeded_detected,
        "Pre_Remediation_Gate": deployment_gate_pre,
        "Post_Remediation_Gate": deployment_gate_post,
        "Pre_Remediation_Group_Metrics": pre_metrics,
        "Post_Remediation_Group_Metrics": post_metrics,
        "Evidence_State": (
            "Designed -> Synthetic technical implementation demonstrated -> "
            "Synthetic fairness execution demonstrated -> Synthetic operation tested"
        ),
        "Production_Operating_Effectiveness": "Not established",
        "Legal_Compliance_or_Discrimination_Conclusion": "Not established",
        "Threshold_Boundary": config["threshold_boundary_note"],
        "Fairness_Interpretation": config["fairness_interpretation"]
    }
    SUMMARY_OUT.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(json.dumps(summary, indent=2))
    return 0 if summary["Failed_Control_Assertions"] == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
