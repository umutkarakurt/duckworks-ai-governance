import sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from app.winginspect_lab import CASES, run_campaign
class Tests(unittest.TestCase):
    def test_case_population(self): self.assertEqual(list(CASES),[f'WISEC-T{i:03d}' for i in range(1,9)])
    def test_vulnerable(self): self.assertEqual([r['result'] for r in run_campaign('vulnerable')],['FAIL']*8)
    def test_hardened(self): self.assertEqual([r['result'] for r in run_campaign('hardened')],['PASS']*8)
    def test_t001(self):
        r=run_campaign('hardened')[0]; self.assertTrue(r['actual']['model_missed']); self.assertTrue(r['actual']['validation_blocked']); self.assertFalse(r['actual']['release_allowed'])
    def test_t007(self):
        r=run_campaign('hardened')[6]; self.assertTrue(r['actual']['manual_hold']); self.assertFalse(r['actual']['release_allowed'])
    def test_t008(self):
        r=run_campaign('hardened')[7]; self.assertFalse(r['actual']['release_allowed']); self.assertEqual(r['actual']['reason'],'human_authorization_missing')
if __name__=='__main__': unittest.main()
