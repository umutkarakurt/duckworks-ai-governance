from __future__ import annotations
import hashlib, json, os, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.quackbot_lab import (  # noqa: E402
    LAB_VERSION, ARCH_VERSION, THREAT_VERSION, PLAN_VERSION,
    ai_interaction_disclosure, all_test_ids, run_case,
)

EVIDENCE = ROOT / "evidence" / "generated"

def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def main():
    if EVIDENCE.exists():
        for p in sorted(EVIDENCE.rglob("*"), reverse=True):
            if p.is_file():
                p.unlink()
            elif p.is_dir():
                p.rmdir()
    EVIDENCE.mkdir(parents=True, exist_ok=True)

    source_commit = os.environ.get("GITHUB_SHA", "LOCAL_UNBOUND")
    profiles = {}
    telemetry_lines = []

    for profile in ("vulnerable", "hardened"):
        passed = failed = 0
        for test_id in all_test_ids():
            result = run_case(test_id, profile)
            write_json(EVIDENCE / profile / f"{test_id}.json", result)
            passed += result["result"] == "PASS"
            failed += result["result"] == "FAIL"
            telemetry_lines.append(json.dumps({
                "correlation_id": result["correlation_id"],
                "test_id": test_id,
                "profile": profile,
                "detection": result["detection"],
                "result": result["result"],
            }, sort_keys=True))
        profiles[profile] = {"tests": len(all_test_ids()), "pass": int(passed), "fail": int(failed)}

    disclosure = ai_interaction_disclosure("hardened")
    write_json(EVIDENCE / "compliance" / "QB-COMP-001.json", disclosure)
    (EVIDENCE / "telemetry.jsonl").write_text("\n".join(telemetry_lines) + "\n", encoding="utf-8")

    summary = {
        "campaign": "QuackBot Public-Facing RAG/API Technical Security Validation",
        "lab_version": LAB_VERSION,
        "architecture_version": ARCH_VERSION,
        "threat_model_version": THREAT_VERSION,
        "validation_plan_version": PLAN_VERSION,
        "source_commit": source_commit,
        "profiles": profiles,
        "compliance_assertions": {"QB-COMP-001": disclosure["result"]},
        "production_effectiveness_claim": False,
        "risk_score_change_authorized": False,
        "production_gate_change_authorized": False,
        "evidence_id_allocation_authorized": False,
    }
    write_json(EVIDENCE / "campaign-summary.json", summary)

    entries = []
    for p in sorted(EVIDENCE.rglob("*")):
        if p.is_file() and p.name != "hash-manifest.json":
            entries.append({
                "path": p.relative_to(EVIDENCE).as_posix(),
                "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
            })
    write_json(EVIDENCE / "hash-manifest.json", {"files": entries})
    print(json.dumps(summary, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
