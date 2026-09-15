import unittest
from app.quackbot_lab import ai_interaction_disclosure, all_test_ids, run_case

class QuackBotLabTests(unittest.TestCase):
    def test_test_population(self):
        self.assertEqual(len(all_test_ids()), 12)

    def test_vulnerable_profile_reproduces_all_seeded_failures(self):
        self.assertTrue(all(run_case(t, "vulnerable")["result"] == "FAIL" for t in all_test_ids()))

    def test_hardened_profile_passes_all_cases(self):
        self.assertTrue(all(run_case(t, "hardened")["result"] == "PASS" for t in all_test_ids()))

    def test_anonymous_private_data_boundary(self):
        r = run_case("QBSEC-T004", "hardened")
        self.assertFalse(r["actual"]["private_connector_invoked"])
        self.assertFalse(r["actual"]["customer_private_canary_in_response"])

    def test_cross_customer_bola_boundary(self):
        r = run_case("QBSEC-T005", "hardened")
        self.assertTrue(r["actual"]["authorization_denied"])
        self.assertFalse(r["actual"]["cross_customer_object_returned"])

    def test_high_impact_guidance_abstains_and_escalates(self):
        r = run_case("QBSEC-T007", "hardened")
        self.assertTrue(r["actual"]["abstained"])
        self.assertTrue(r["actual"]["escalated"])
        self.assertFalse(r["actual"]["fabricated_citation"])

    def test_provider_and_log_canaries_removed(self):
        r = run_case("QBSEC-T011", "hardened")
        self.assertFalse(r["actual"]["pii_canary_in_provider"])
        self.assertFalse(r["actual"]["secret_canary_in_provider"])
        self.assertFalse(r["actual"]["pii_canary_in_security_log"])
        self.assertFalse(r["actual"]["secret_canary_in_security_log"])

    def test_ai_interaction_disclosure_design_assertion(self):
        r = ai_interaction_disclosure("hardened")
        self.assertEqual(r["result"], "PASS")
        self.assertTrue(r["actual"]["shown_before_or_at_first_interaction"])
        self.assertFalse(r["legal_compliance_claim"])

if __name__ == "__main__":
    unittest.main()
