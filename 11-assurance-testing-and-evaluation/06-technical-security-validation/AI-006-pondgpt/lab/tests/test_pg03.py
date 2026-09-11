from app.campaign import run_campaign, CASES


def test_all_eight_pg03_cases_exist():
    assert list(CASES) == [f"PG03-T{i:03d}" for i in range(1, 9)]


def test_vulnerable_profile_reproduces_security_failures():
    results, _ = run_campaign("vulnerable")
    assert len(results) == 8
    failures = [r.test_id for r in results if r.result == "FAIL"]
    # The lab intentionally seeds weaknesses for every first-wave case.
    assert failures == [f"PG03-T{i:03d}" for i in range(1, 9)]


def test_hardened_profile_passes_all_security_boundaries():
    results, _ = run_campaign("hardened")
    assert len(results) == 8
    assert all(r.result == "PASS" for r in results), [(r.test_id, r.actual) for r in results]


def test_hardened_restricted_context_invariant():
    results, _ = run_campaign("hardened")
    for result in results:
        actual = result.actual
        for key, value in actual.items():
            if key.startswith("restricted_context_chunks") or key.startswith("provider_restricted_chunks"):
                assert value == 0, (result.test_id, key, value)


def test_hardened_provider_secret_invariant():
    results, _ = run_campaign("hardened")
    t007 = next(r for r in results if r.test_id == "PG03-T007")
    assert t007.actual["secret_canary_in_provider"] is False
    assert t007.actual["secret_canary_in_telemetry"] is False


def test_hardened_fail_closed_pep():
    results, _ = run_campaign("hardened")
    t008 = next(r for r in results if r.test_id == "PG03-T008")
    assert t008.actual["controlled_deny_or_error"] is True
    assert t008.actual["restricted_context_chunks"] == 0
