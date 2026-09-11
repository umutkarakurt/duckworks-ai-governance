from __future__ import annotations
import argparse
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import platform
import subprocess
import sys

LAB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB))

from app.campaign import run_campaign, APP_VERSION, ARCH_VERSION, POLICY_VERSION, INDEX_VERSION, MODEL_PROFILE, SYSTEM_PROMPT_VERSION


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def file_sha256(path: Path) -> str:
    h = sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


def source_commit() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=LAB, text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return "PENDING_REPOSITORY_COMMIT"


def source_tree_sha256() -> str:
    """Hash the executable lab source/config, excluding generated evidence/cache files."""
    h = sha256()
    roots = [LAB / "app", LAB / "tests", LAB / "scripts"]
    extras = [LAB / "requirements.txt", LAB / "requirements-lock.txt", LAB / "pyproject.toml"]
    files = []
    for root in roots:
        files.extend(p for p in root.rglob("*") if p.is_file() and "__pycache__" not in p.parts)
    files.extend(p for p in extras if p.exists())
    for path in sorted(files, key=lambda x: str(x.relative_to(LAB))):
        rel = str(path.relative_to(LAB)).encode("utf-8")
        h.update(rel + b"\0")
        h.update(path.read_bytes())
        h.update(b"\0")
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(description="Run PondGPT PG-03 synthetic security campaign")
    ap.add_argument("--output", default=str(LAB / "evidence" / "generated"))
    args = ap.parse_args()
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)

    campaign_summary = {
        "document_id": "DW-AI006-PG03-RUN-01",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "synthetic": True,
        "production_effectiveness_claim": False,
        "architecture_version": ARCH_VERSION,
        "app_version": APP_VERSION,
        "policy_version": POLICY_VERSION,
        "index_version": INDEX_VERSION,
        "model_profile": MODEL_PROFILE,
        "system_prompt_version": SYSTEM_PROMPT_VERSION,
        "python_runtime": platform.python_version(),
        "source_commit": source_commit(),
        "source_tree_sha256": source_tree_sha256(),
        "profiles": {},
    }

    all_written: list[Path] = []
    for profile in ["vulnerable", "hardened"]:
        results, telemetry = run_campaign(profile)
        profile_dir = out / profile
        profile_dir.mkdir(parents=True, exist_ok=True)
        for result in results:
            p = profile_dir / f"{result.test_id}.json"
            write_json(p, result.to_dict())
            all_written.append(p)
        telemetry_path = profile_dir / "security-telemetry.jsonl"
        with telemetry_path.open("w", encoding="utf-8") as f:
            for event in telemetry:
                f.write(json.dumps(event, sort_keys=True, ensure_ascii=False) + "\n")
        all_written.append(telemetry_path)

        summary = {
            "tests": len(results),
            "pass": sum(r.result == "PASS" for r in results),
            "fail": sum(r.result == "FAIL" for r in results),
            "error": sum(r.result == "ERROR" for r in results),
            "blocked": sum(r.result == "BLOCKED" for r in results),
            "results": {r.test_id: r.result for r in results},
            "detector": {
                r.test_id: r.detection for r in results if r.test_id == "PG03-T005"
            },
        }
        campaign_summary["profiles"][profile] = summary

    summary_path = out / "campaign-summary.json"
    write_json(summary_path, campaign_summary)
    all_written.append(summary_path)

    manifest = {
        "manifest_id": "PG03-EVIDENCE-MANIFEST-001",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "files": {},
    }
    for path in sorted(all_written):
        manifest["files"][str(path.relative_to(LAB))] = file_sha256(path)
    manifest_path = out / "hash-manifest.json"
    write_json(manifest_path, manifest)

    print(json.dumps(campaign_summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
