from __future__ import annotations
from pathlib import Path
import sys

LAB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB))

from app.campaign import run_campaign, CASES


def main() -> int:
    expected_ids = [f"PG03-T{i:03d}" for i in range(1, 9)]
    assert list(CASES) == expected_ids, list(CASES)

    vulnerable, vulnerable_events = run_campaign("vulnerable")
    hardened, hardened_events = run_campaign("hardened")

    vulnerable_failures = [r.test_id for r in vulnerable if r.result == "FAIL"]
    hardened_failures = [(r.test_id, r.actual) for r in hardened if r.result != "PASS"]

    assert vulnerable_failures == expected_ids, vulnerable_failures
    assert not hardened_failures, hardened_failures

    # Security invariant: hardened restricted/provider counts must be zero.
    for result in hardened:
        for key, value in result.actual.items():
            if key.startswith("restricted_context_chunks") or key.startswith("provider_restricted_chunks"):
                assert value == 0, (result.test_id, key, value)


    # Every hardened test must have end-to-end correlation and a result event.
    for result in hardened:
        events = [e for e in hardened_events if e["security_test_id"] == result.test_id]
        assert events, result.test_id
        expected_corr = result.evidence["correlation_id"]
        assert all(e["correlation_id"] == expected_corr for e in events), (result.test_id, expected_corr)
        assert any(e["event_family"] == "security_test.result" for e in events), result.test_id

    t007 = next(r for r in hardened if r.test_id == "PG03-T007")
    assert t007.actual["hr_canary_in_provider"] is False
    assert t007.actual["secret_canary_in_provider"] is False
    assert t007.actual["secret_canary_in_telemetry"] is False

    t008 = next(r for r in hardened if r.test_id == "PG03-T008")
    assert t008.actual["controlled_deny_or_error"] is True

    t006 = next(r for r in hardened if r.test_id == "PG03-T006")
    assert t006.actual["remote_autoload"] is False

    t005 = next(r for r in hardened if r.test_id == "PG03-T005")
    assert t005.actual["detector_misses"] >= 1
    assert t005.result == "PASS"  # proves detector is not the authorization boundary

    print("PG-03 CI verification: PASS")
    print("vulnerable profile: 0 PASS / 8 FAIL (expected seeded failures reproduced)")
    print("hardened profile: 8 PASS / 0 FAIL")
    print(f"T005 detector coverage: {t005.detection['coverage']} with security boundaries intact")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
