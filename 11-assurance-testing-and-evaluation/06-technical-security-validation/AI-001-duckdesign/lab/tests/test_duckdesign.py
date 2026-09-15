import unittest

from app.duckdesign_lab import all_test_ids, run_case


class DuckDesignLabTests(unittest.TestCase):
    def test_test_population(self):
        self.assertEqual(len(all_test_ids()), 12)

    def test_vulnerable_profile_reproduces_all_seeded_failures(self):
        self.assertTrue(all(run_case(t, "vulnerable")["result"] == "FAIL" for t in all_test_ids()))

    def test_hardened_profile_passes_all_cases(self):
        self.assertTrue(all(run_case(t, "hardened")["result"] == "PASS" for t in all_test_ids()))

    def test_provider_and_log_canaries_removed(self):
        r = run_case("DDSEC-T001", "hardened")
        self.assertFalse(r["actual"]["engineering_ip_canary_in_provider"])
        self.assertFalse(r["actual"]["secret_canary_in_provider"])
        self.assertFalse(r["actual"]["engineering_ip_canary_in_log"])
        self.assertFalse(r["actual"]["secret_canary_in_log"])

    def test_generated_code_boundary(self):
        r = run_case("DDSEC-T003", "hardened")
        self.assertTrue(r["actual"]["scanner_flagged_prohibited_behavior"])
        self.assertTrue(r["actual"]["sandbox_enforced"])
        self.assertFalse(r["actual"]["shell_allowed"])
        self.assertFalse(r["actual"]["external_network_allowed"])
        self.assertFalse(r["actual"]["artifact_promoted"])

    def test_unapproved_dependency_denied(self):
        r = run_case("DDSEC-T004", "hardened")
        self.assertTrue(r["actual"]["dependency_denied"])
        self.assertFalse(r["actual"]["dependency_resolved"])
        self.assertFalse(r["actual"]["public_registry_fallback_used"])

    def test_safety_gate_independent(self):
        r = run_case("DDSEC-T008", "hardened")
        self.assertTrue(r["actual"]["safety_gate_blocked"])
        self.assertFalse(r["actual"]["promotion_allowed"])
        self.assertFalse(r["actual"]["bypass_possible"])

    def test_approval_hash_binding(self):
        r = run_case("DDSEC-T009", "hardened")
        self.assertTrue(r["actual"]["approval_invalidated"])
        self.assertTrue(r["actual"]["rereview_required"])
        self.assertFalse(r["actual"]["approval_accepted"])

    def test_provenance_blocks_promotion(self):
        r = run_case("DDSEC-T011", "hardened")
        self.assertTrue(r["actual"]["artifact_quarantined"])
        self.assertFalse(r["actual"]["artifact_promoted"])

    def test_known_good_rollback(self):
        r = run_case("DDSEC-T012", "hardened")
        self.assertTrue(r["actual"]["known_good_state_restored"])
        self.assertTrue(r["actual"]["rollback_hash_verified"])
        self.assertTrue(r["actual"]["correlated_failure_event_present"])
        self.assertFalse(r["actual"]["automatic_risk_or_gate_change"])


if __name__ == "__main__":
    unittest.main()
