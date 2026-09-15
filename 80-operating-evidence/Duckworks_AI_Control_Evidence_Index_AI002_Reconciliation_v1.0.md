# Duckworks AI Control Evidence Index — AI-002 Reconciliation Addendum

**Project:** W.I.N.G. — Workflows, Intelligence, Next-Generation Governance  
**Document ID:** DW-AIEI-AI002-REC-01  
**Version:** 1.0  
**Effective date:** 15 September 2026  
**Owner:** AI Governance Lead  
**Base register:** `Duckworks_AI_Control_Evidence_Index_v1.8.md`  
**Scope:** AI-002 QuackBot Phase II technical-security evidence only  
**Status:** Controlled reconciliation overlay pending next master-index consolidation

> This addendum does not replace or renumber any existing evidence record. It reserves `EV-AI002-001`–`EV-AI002-007` as stable evidence IDs and incorporates them into the current AI-002 evidence view.

## 1. New evidence records

| Evidence ID | AI entry | Risk ID | Control ID(s) | Artifact | Repository location | Evidence state | Synthetic / production | Demonstrates | Evidence owner | Decision impact | Next review trigger |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EV-AI002-001 | AI-002 — QuackBot | AI-002-R01; R02; R03 | QB-01–QB-06 | Public-Facing RAG/API Technical Security Validation Plan v1.0 | 11-assurance-testing-and-evaluation/06-technical-security-validation/AI-002-quackbot/ | Designed | Synthetic | Twelve-case vulnerable/hardened campaign, exact assertions, evidence schema, legal-disclosure separation and non-production boundary | Cassandra Duckley — CISO | Authorizes bounded synthetic validation only; no score/gate/production-effectiveness credit | Architecture/threat-model/test-scope change; failed assertion; scheduled review |
| EV-AI002-002 | AI-002 — QuackBot | AI-002-R01; R02; R03 | QB-01–QB-06 | Executable QuackBot Lab v0.1.0 | 11-assurance-testing-and-evaluation/06-technical-security-validation/AI-002-quackbot/lab/ | Synthetic technical implementation demonstrated | Synthetic | Deterministic public/authenticated sessions, object authorization, RAG provenance, grounding/escalation, safe output, tool denial, resource controls, minimization and version integrity | Cassandra Duckley — CISO | Demonstrates bounded implementation only; production integration/effectiveness unverified | Lab/control version; architecture change; failed regression; production integration |
| EV-AI002-003 | AI-002 — QuackBot | AI-002-R01; R02; R03 | QB-01–QB-06 | Baseline Findings and Remediation v1.0 | 11-assurance-testing-and-evaluation/06-technical-security-validation/AI-002-quackbot/lab/findings/ | Synthetic failure detection / remediation demonstrated | Synthetic | Twelve deliberately seeded unsafe states are reproduced and remediated using the same bounded test model | Cassandra Duckley — CISO | Demonstrates harness sensitivity and remediation logic; no production-vulnerability conclusion | Remediation change; reopened finding; failed regression; architecture/control change |
| EV-AI002-004 | AI-002 — QuackBot | AI-002-R01; R02; R03 | QB-01–QB-06 | Hardened Campaign + Technical Security Test Report v1.1 | 11-assurance-testing-and-evaluation/06-technical-security-validation/AI-002-quackbot/lab/reports/ | Synthetic operation tested | Synthetic | Same twelve cases move from 12/12 seeded failures to 12/12 hardened PASS; system boundaries operate independently of model refusal | Cassandra Duckley — CISO | Supports bounded synthetic operation testing only; production remains blocked | Lab/control version; failed regression; production evidence; incident; lifecycle review |
| EV-AI002-005 | AI-002 — QuackBot | AI-002-R01; R02; R03 | QB-04; QB-05; QB-06; supporting QB-01–QB-03 | Detection and Control-Signal Validation v1.0 | 11-assurance-testing-and-evaluation/06-technical-security-validation/AI-002-quackbot/lab/reports/ | Synthetic detection / control-signal validation demonstrated | Synthetic | Injection, provenance, authorization, session, grounding, output, tool/egress, resource, minimization and change signals are observable without replacing preventive boundaries | Cassandra Duckley — CISO | Demonstrates bounded observability; no production SOC/SIEM effectiveness claim | Telemetry/detector change; missed expected event; production integration |
| EV-AI002-006 | AI-002 — QuackBot | AI-002-R01; R02; R03 | QB-01–QB-06 | Commit-Bound GitHub Actions Replay + Retained Evidence Artifact | `.github/workflows/evidence-tests.yml`; run #147 | Synthetic commit-bound reproducibility demonstrated | Synthetic | Python 3.12.14 replay on `25525cc2...` verifies source binding, 12 vulnerable failures, 12 hardened PASS, 8 unit tests, semantic assertions and retained artifact `10387591380` | Cassandra Duckley — CISO | Establishes commit-bound synthetic reproducibility only; no production/risk/gate credit | Workflow/lab/control version; failed CI; artifact-policy change; production evidence |
| EV-AI002-007 | AI-002 — QuackBot | AI-002-R03 | Governance / interaction-transparency design | AI Interaction Disclosure Design Assertion v1.0 | 11-assurance-testing-and-evaluation/06-technical-security-validation/AI-002-quackbot/lab/reports/ | Synthetic legal-design assertion demonstrated | Synthetic | Hardened synthetic interaction flow displays AI-interaction disclosure before or at first interaction | Amelia Duckett — General Counsel / Eleanor Duckford — AI Governance Lead | Demonstrates a design assertion only; no full Article 50 compliance conclusion | Legal-role/exception analysis; UI change; localization/accessibility change; production implementation review |

## 2. Current evidence population after reconciliation

| Metric | Result |
|---|---:|
| v1.8 base evidence records | 76 |
| AI-004 reconciliation records outside v1.8 | 6 |
| New AI-002 reconciliation records | 7 |
| Combined current evidence records | **89** |
| Available synthetic records | **83** |
| Not-available evidence records | **6** |
| Production-effectiveness conclusions supported | **0** |

## 3. Evidence boundary

The new QuackBot evidence is synthetic and commit-bound. It can support claims of reproducible technical-control behavior in the defined lab only.

It cannot support production QuackBot security, customer-data isolation in production, prompt-injection immunity, real provider compliance, legal compliance, production escalation SLA effectiveness, risk-score reduction or deployment approval.

## 4. Consolidation rule

At the next full evidence-index consolidation, `EV-AI002-001`–`007` should be incorporated into the successor to v1.8 without changing their IDs or evidence-state conclusions.
