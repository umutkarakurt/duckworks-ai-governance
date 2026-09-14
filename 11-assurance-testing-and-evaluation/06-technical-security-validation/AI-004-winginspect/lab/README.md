# WingInspect Vision — Synthetic Adversarial-ML Security Lab

**Lab version:** `winginspect-lab-0.1.0`  
**System:** AI-004 WingInspect Vision  
**Validation plan:** `DW-AI004-VAL-SEC-01 v1.0`  
**Boundary:** synthetic / deterministic / non-production

Run:

```bash
python scripts/run_campaign.py
python -m unittest discover -s tests -p "test_*.py"
python scripts/ci_verify.py
```

The lab uses a deterministic computer-vision surrogate, not a production ML model. It tests challenge-set failure handling, quality fail-safe behavior, model/config/data integrity, dependency failure, and the Mandatory Human Release Gate. It does not establish real adversarial robustness, physical-world transferability, product safety, real camera behavior, real VisiCore behavior, production human effectiveness, or production operating effectiveness.
