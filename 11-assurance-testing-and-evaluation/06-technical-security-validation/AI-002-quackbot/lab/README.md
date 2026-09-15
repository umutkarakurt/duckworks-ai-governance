# QuackBot Public-Facing RAG/API Security Lab

**Lab version:** `quackbot-lab-0.1.0`  
**System:** AI-002 — QuackBot  
**Status:** deterministic synthetic / non-production

This lab implements `QBSEC-T001`–`QBSEC-T012` using only the Python standard library.

The objective is **system-control validation**, not demonstration that a particular commercial LLM refuses malicious prompts.

## Profiles

**Vulnerable:** deliberately reproduces twelve unsafe outcomes across prompt/RAG injection, source integrity, customer authorization, sessions, material guidance, output handling, tool/egress, resource controls, data minimization and version integrity.

**Hardened:** reruns the same cases with deterministic authorization, provenance, session isolation, grounding/escalation, safe rendering, tool denial, resource limiting, redaction and change-regression controls.

## Commands

```bash
python scripts/run_campaign.py
python -m unittest discover -s tests -p "test_*.py"
python scripts/ci_verify.py
```

## Expected local result

- vulnerable: **0 PASS / 12 FAIL**
- hardened: **12 PASS / 0 FAIL**
- unit tests: **8 PASS**
- `QB-COMP-001`: **PASS**
- `source_commit`: `LOCAL_UNBOUND`
- `production_effectiveness_claim`: `false`

## AI interaction disclosure assertion

`QB-COMP-001` checks that the synthetic interaction flow shows an AI disclosure before or at first interaction. It is intentionally separate from the twelve adversarial-security cases. A PASS does not establish full legal compliance.

## Evidence boundary

The lab does not demonstrate production QuackBot security, real prompt-injection resistance, real BOLA/session security, real HelixRiver behavior, production customer-data protection, availability resilience, legal compliance or deployment readiness.

No `EV-AI002-*` IDs should be allocated until a clean commit-bound repository replay succeeds.
