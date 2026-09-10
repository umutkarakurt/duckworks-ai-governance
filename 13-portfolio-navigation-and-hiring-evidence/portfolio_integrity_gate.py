#!/usr/bin/env python3
"""Validate the v1.8 portfolio navigation and claim-boundary package."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parent


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def path_exists(reference: str) -> bool:
    candidate = REPO / reference
    return candidate.exists()


def main() -> int:
    config = json.loads((HERE / "portfolio_integrity_gate_config.json").read_text(encoding="utf-8"))
    competencies = read_csv(HERE / "Duckworks_Competency_to_Evidence_Map_v1.0.csv")
    claims = read_csv(HERE / "Duckworks_Portfolio_Claim_Boundary_Register_v1.0.csv")

    competency_ids = [row["Competency_ID"] for row in competencies]
    claim_ids = [row["Claim_ID"] for row in claims]
    evidence_paths = [row["Primary_Evidence_Path"] for row in competencies]
    evidence_paths += [row["Secondary_Evidence_Path"] for row in competencies]
    evidence_paths += [row["Evidence_Path"] for row in claims]

    checks = {
        "competency_count": len(competencies),
        "claim_count": len(claims),
        "unique_competency_ids": len(competency_ids) == len(set(competency_ids)),
        "unique_claim_ids": len(claim_ids) == len(set(claim_ids)),
        "required_competency_ids_present": set(config["required_competency_ids"]) == set(competency_ids),
        "required_claim_ids_present": set(config["required_claim_ids"]) == set(claim_ids),
        "invalid_strength_count": sum(row["Strength"] not in config["allowed_strengths"] for row in competencies),
        "strong_competency_count": sum(row["Strength"] == "Strong" for row in competencies),
        "missing_limitation_count": sum(not row["Material_Limitation"].strip() for row in competencies),
        "missing_claim_boundary_count": sum(not row["Boundary"].strip() for row in claims),
        "invalid_claim_status_count": sum(row["Status"] not in config["allowed_claim_statuses"] for row in claims),
        "invalid_path_count": sum(not path_exists(path) for path in sorted(set(evidence_paths))),
        "missing_required_file_count": sum(not (REPO / path).exists() for path in config["required_files"]),
        "required_cases_present": set(config["required_case_numbers"]).issubset({row["Interview_Case"] for row in competencies}),
        "automatic_maturity_upgrades": 0,
    }

    expected = config["expected"]
    assertions = {
        "competency_count_matches": checks["competency_count"] == expected["competency_count"],
        "claim_count_matches": checks["claim_count"] == expected["claim_count"],
        "competency_ids_unique": checks["unique_competency_ids"],
        "claim_ids_unique": checks["unique_claim_ids"],
        "required_ids_present": checks["required_competency_ids_present"] and checks["required_claim_ids_present"],
        "strength_values_valid": checks["invalid_strength_count"] == 0,
        "strong_competency_threshold_met": checks["strong_competency_count"] >= config["minimum_strong_competencies"],
        "limitations_complete": checks["missing_limitation_count"] == 0 and checks["missing_claim_boundary_count"] == 0,
        "claim_statuses_valid": checks["invalid_claim_status_count"] == expected["invalid_claim_status_count"],
        "evidence_paths_resolve": checks["invalid_path_count"] == expected["invalid_path_count"],
        "required_files_present": checks["missing_required_file_count"] == 0,
        "interview_cases_covered": checks["required_cases_present"],
        "no_automatic_maturity_upgrade": checks["automatic_maturity_upgrades"] == expected["automatic_maturity_upgrades"],
    }

    result = {
        "gate": "Portfolio integrity",
        "version": config["version"],
        "status": "PASS" if all(assertions.values()) else "FAIL",
        "assertions_passed": sum(assertions.values()),
        "assertions_total": len(assertions),
        "checks": checks,
        "assertions": assertions,
        "boundary": "This gate validates repository structure, traceability and claim boundaries. It does not validate production operation, legal compliance, certification or hiring outcomes."
    }
    output = HERE / "Duckworks_Portfolio_Integrity_Gate_Run_Summary.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())

