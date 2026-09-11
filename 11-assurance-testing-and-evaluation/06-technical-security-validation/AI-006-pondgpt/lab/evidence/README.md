# PG-03 Generated Evidence

This folder contains machine-generated evidence from the PondGPT synthetic PG-03 security lab.

- `generated/vulnerable/` retains the intentionally weak baseline results and telemetry.
- `generated/hardened/` retains the remediated-state results and telemetry.
- `generated/campaign-summary.json` summarizes both profiles.
- `generated/hash-manifest.json` records SHA-256 hashes of the generated evidence files.

The vulnerable evidence is intentionally preserved to demonstrate a real failure → remediation → identical retest chain. No baseline result should be described as a production vulnerability.

Canonical `EV-AI006-###` IDs are not assigned in this lab folder until the repository evidence-index reconciliation step.
