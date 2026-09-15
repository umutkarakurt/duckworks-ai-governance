import unittest

from app.featherforecast_lab import all_test_ids, run_case


class FeatherForecastLabTests(unittest.TestCase):
    def test_test_population(self):
        self.assertEqual(len(all_test_ids()), 12)

    def test_vulnerable_profile_reproduces_all_seeded_failures(self):
        self.assertTrue(all(run_case(t, "vulnerable")["result"] == "FAIL" for t in all_test_ids()))

    def test_hardened_profile_passes_all_cases(self):
        self.assertTrue(all(run_case(t, "hardened")["result"] == "PASS" for t in all_test_ids()))

    def test_source_poisoning_is_quarantined(self):
        r = run_case("FFSEC-T001", "hardened")
        self.assertTrue(r["actual"]["batch_quarantined"])
        self.assertFalse(r["actual"]["batch_entered_approved_snapshot"])
        self.assertFalse(r["actual"]["forecast_generated_from_batch"])

    def test_training_serving_skew_blocks_scoring(self):
        r = run_case("FFSEC-T003", "hardened")
        self.assertTrue(r["actual"]["training_serving_skew_detected"])
        self.assertFalse(r["actual"]["scoring_allowed"])
        self.assertFalse(r["actual"]["promotion_allowed"])

    def test_drift_and_data_quality_are_distinguished(self):
        r = run_case("FFSEC-T006", "hardened")
        self.assertEqual(r["actual"]["quality_case"]["classification"], "DATA_QUALITY")
        self.assertEqual(r["actual"]["drift_case"]["classification"], "DRIFT")
        self.assertFalse(r["actual"]["automatic_promotion"])

    def test_manager_approval_boundary(self):
        r = run_case("FFSEC-T008", "hardened")
        self.assertTrue(r["actual"]["commitment_blocked"])
        self.assertFalse(r["actual"]["direct_commitment_created"])
        self.assertFalse(r["actual"]["approval_bypass_possible"])

    def test_unauthorized_planning_data_access(self):
        r = run_case("FFSEC-T010", "hardened")
        self.assertEqual(r["actual"]["access_decision"], "DENY")
        self.assertTrue(r["actual"]["access_logged"])
        self.assertFalse(r["actual"]["commercial_canary_in_response"])
        self.assertFalse(r["actual"]["commercial_canary_in_export"])

    def test_outage_enters_manual_mode(self):
        r = run_case("FFSEC-T011", "hardened")
        self.assertTrue(r["actual"]["forecast_marked_stale"])
        self.assertTrue(r["actual"]["manual_or_degraded_mode_active"])
        self.assertFalse(r["actual"]["decision_support_allowed_from_stale_forecast"])

    def test_known_good_rollback(self):
        r = run_case("FFSEC-T012", "hardened")
        self.assertTrue(r["actual"]["promotion_blocked"])
        self.assertTrue(r["actual"]["known_good_state_restored"])
        self.assertTrue(r["actual"]["rollback_model_matches"])
        self.assertTrue(r["actual"]["rollback_config_matches"])
        self.assertTrue(r["actual"]["rollback_data_matches"])


if __name__ == "__main__":
    unittest.main()
