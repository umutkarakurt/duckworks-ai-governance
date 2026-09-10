# Assurance, Testing and Evaluation

**Repository path:** `11-assurance-testing-and-evaluation/`  
**Status:** Portfolio assurance-readiness, challenge, and Phase II technical-security validation artifacts  

[← Back to main portfolio](../README.md)

This folder demonstrates how Duckworks moves beyond policy creation toward **evaluation, challenge, evidence quality, technical validation, and independent assurance readiness**.

## Subfolders

| Folder | Purpose |
|---|---|
| `01-nist-aria/` | Internal evaluation documentation informed by public NIST ARIA materials. |
| `02-adversarial-review/` | Skeptical multi-perspective review and structured findings register. |
| [`03-iso42001/`](03-iso42001/) | AIMS thematic evidence baseline and master traceability crosswalk. |
| [`04-internal-audit-and-corrective-action/`](04-internal-audit-and-corrective-action/) | Bounded synthetic audit, corrective-action, management-review and closure evidence. |
| [`05-aims-internal-audit-programme/`](05-aims-internal-audit-programme/) | Risk-based 45-control audit universe, 2026–2027 programme, first-wave DD-01/FF-01 testing and open findings. |
| [`06-technical-security-validation/`](06-technical-security-validation/) | Phase II controlled AI/application-security validation, beginning with AI-006 PondGPT and PG-03 prompt-injection/RAG-poisoning testing. |

## Current authoritative artifacts

- [`ISO/IEC 42001 AIMS Evidence Baseline v1.7`](03-iso42001/duckworks-iso42001-evidence-baseline-v1.7.md)
- [`AIMS Master Crosswalk v1.6`](03-iso42001/Duckworks_AIMS_Master_Crosswalk_v1.6.xlsx)
- [`AIMS internal-audit programme`](05-aims-internal-audit-programme/)
- [`DuckTalent AIMS improvement-cycle package`](04-internal-audit-and-corrective-action/AI-005-ducktalent/)
- [`PondGPT PG-03 Technical Security Validation Plan v1.0`](06-technical-security-validation/AI-006-pondgpt/Duckworks_PondGPT_PG03_Technical_Security_Validation_Plan_v1.0.md)
- [`AIMS objectives and support package`](../06-governance-operating-model/01-aims-objectives-and-support/)
- [`AIMS risk, opportunity and management-review cycle`](../12-monitoring-reporting-and-roadmap/01-aims-management-review-cycle/)

Earlier AIMS baseline and crosswalk versions are retained for traceability and are superseded by the versions listed above. Phase II technical-security artifacts use their own document versions and do not supersede the governance/AIMS evidence baseline.

## Assurance principle

A governance framework is not credible merely because documents exist. Material claims should be capable of being tested against evidence, and weaknesses should be visible rather than hidden.

This folder therefore supports questions such as:

- Can a reviewer reproduce the basis for a risk conclusion?
- Are controls actually evidenced?
- Are assumptions labelled?
- Are risk scores causally justified?
- Are owners and release decisions consistent across artifacts?
- Are framework mappings precise enough to be useful without overstating compliance?
- Can identified issues be tracked to remediation and closure evidence?
- Can a security requirement be converted into a repeatable technical test?
- Can a reviewer distinguish a safe final model answer from a genuinely enforced system security boundary?
- Can a baseline failure be reproduced, remediated, retested, and correlated to telemetry?

## Technical-validation boundary

Phase II technical validation is a **controlled engineering activity**, not independent audit assurance.

For AI-006 PondGPT, testing is limited to fictional Duckworks systems, synthetic data, locally controlled components, or explicitly authorized test environments under the Phase II scope addendum. A synthetic PASS may demonstrate that a defined mechanism blocked a defined attack in a specific lab version. It does **not** establish production security, sustained operating effectiveness, legal compliance, ISO conformity/certification, or validated residual-risk reduction.

## Independence

Internal Audit is treated as an independent third-line function. Second-line review, security engineering, adversarial testing, and project self-assessment should not be described as independent audit assurance.

---

> **Portfolio boundary:** Duckworks, Project W.I.N.G., its personnel, systems, datasets, decisions, controls, and evidence are fictional or synthetic unless a file explicitly identifies a public source. Folder descriptions explain the intended governance role of the artifacts; they do not convert draft, planned, or template material into implemented controls, legal compliance, certification, production effectiveness, or independent assurance.
