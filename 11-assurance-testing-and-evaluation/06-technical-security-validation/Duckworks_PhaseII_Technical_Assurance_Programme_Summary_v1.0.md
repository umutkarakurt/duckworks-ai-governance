# Project W.I.N.G. — Phase II Technical Assurance Programme Summary

**Document ID:** DW-WING-SEC-SUM-01  
**Version:** 1.0  
**Effective date:** 15 September 2026  
**Owner:** Eleanor Duckford — AI Governance Lead  
**Security owner:** Cassandra Duckley — Chief Information Security Officer  
**Technical owner:** Dr. Ada Duckfield — Head of Data & AI  
**Status:** First-wave Phase II technical-assurance programme consolidated and closed at synthetic / commit-bound portfolio level

> **Boundary:** “Closed” means the planned first-wave portfolio engineering and assurance work has been completed, consolidated and reconciled. It does **not** mean production controls are proven effective, residual risks are validated, legal compliance is established, product safety is proven, open audit findings are closed or independent assurance has occurred.

## 1. Executive conclusion

Phase II converted selected Duckworks AI-security risks from governance descriptions into **inspectable, executable and reproducible technical evidence** across five materially different AI system patterns:

1. internal RAG / GenAI;
2. computer vision / adversarial ML;
3. public-facing RAG / API;
4. engineering GenAI / generated code / software supply chain; and
5. predictive ML / data integrity / drift / operational decision support.

The programme now demonstrates a reusable assurance chain:

> **Architecture → Threat → Security requirement → Deliberately weak baseline → Adversarial / negative test → Raw evidence → Finding → Remediation → Same-test retest → Detection/control-signal validation → Commit-bound replay → Control conclusion → Risk / governance reconciliation**

The strongest defensible portfolio claim is:

> **Duckworks demonstrates how selected AI-security risks can be translated into testable system controls, challenged against deliberately weak conditions, hardened, rerun, bound to repository state, and reconciled back into governance decisions without treating synthetic PASS results as production effectiveness.**

## 2. Programme coverage

| System | Technical pattern | Canonical campaign | Vulnerable baseline | Hardened result | Supplemental unit tests | Canonical evidence | Current governance position |
|---|---|---|---:|---:|---:|---|---|
| AI-006 — PondGPT | Internal RAG / prompt injection / retrieval authorization | `PG03-T001–T008` | 8/8 seeded failures | 8/8 PASS | 6 | `EV-AI006-017–022` | Restricted pilot only |
| AI-004 — WingInspect Vision | Computer vision / adversarial ML / human release authority | `WISEC-T001–T008` | 8/8 seeded failures | 8/8 PASS | 6 | `EV-AI004-006–011` | Restricted pilot only |
| AI-002 — QuackBot | Public-facing RAG / API / customer interaction | `QBSEC-T001–T012` | 12/12 seeded failures | 12/12 PASS | 8 | `EV-AI002-001–007` | Pre-Production / Production Blocked |
| AI-001 — DuckDesign AI | Generated code / engineering data / software supply chain / tool privilege | `DDSEC-T001–T012` | 12/12 seeded failures | 12/12 PASS | 10 | `EV-AI001-001–007` | Restricted Pilot only |
| AI-003 — FeatherForecast | Predictive ML / poisoning / drift / decision resilience | `FFSEC-T001–T012` | 12/12 seeded failures | 12/12 PASS | 10 | `EV-AI003-001–007` | Continue with monitoring |

### Consolidated quantitative view

- **5** system-specific technical-assurance chains;
- **52** distinct campaign test cases;
- **104** profile executions when each case is counted once in vulnerable and once in hardened form;
- **52/52** deliberately seeded unsafe baseline outcomes reproduced;
- **52/52** hardened case outcomes passed;
- **40** supplemental automated unit tests across the five labs;
- **5** commit-bound repository replays;
- **5** retained CI evidence-artifact chains at the canonical reconciliation points;
- **33** canonical technical-validation evidence records across the five increments; and
- **0** production-effectiveness conclusions created by those synthetic results.

The counts above summarize the technical-validation increments only. They do not represent the total number of Project W.I.N.G. governance documents, controls or evidence records.

## 3. Canonical replay anchors

| System | Commit | Run | Canonical retained artifact | Evidence boundary |
|---|---|---|---|---|
| PondGPT | `4998f92238868e1b4f3341ae3ebfbc01bd7881f9` | #92 | `pondgpt-pg03-evidence-4998f92238868e1b4f3341ae3ebfbc01bd7881f9` | Commit-bound synthetic PG-03 reproducibility only |
| WingInspect | `8e8bb9e43aca3d4a9d2f5cfb6e401b8469c4ac0b` | #124 | `winginspect-security-evidence-8e8bb9e43aca3d4a9d2f5cfb6e401b8469c4ac0b` | Commit-bound synthetic system-level containment only |
| QuackBot | `25525cc2c09c6b6557ddb9e7706fdaf81ce1796f` | #147 | `quackbot-security-evidence-25525cc2c09c6b6557ddb9e7706fdaf81ce1796f` | Commit-bound synthetic public-RAG/API validation only |
| DuckDesign | `1c1fd170347dff466eb9d4a670e4355905119be2` | #166 | `duckdesign-security-evidence-1c1fd170347dff466eb9d4a670e4355905119be2` | Commit-bound synthetic engineering-control validation only |
| FeatherForecast | `285b5bdedaef1295d9648c46e17a1aaef7b3428b` | #191 | `featherforecast-security-evidence-285b5bdedaef1295d9648c46e17a1aaef7b3428b` | Commit-bound synthetic forecasting-pipeline validation only |

Later workflow runs may demonstrate repository integrity after reconciliation. They do not replace these canonical reconciliation anchors unless an explicit controlled re-baseline is performed.

## 4. What the programme proves

The programme provides inspectable evidence that the portfolio can:

- turn architecture and trust boundaries into threat hypotheses;
- distinguish AI-specific failure/attack mechanisms from conventional cyber boundaries;
- convert threats into explicit machine-testable requirements;
- build deliberately vulnerable and hardened profiles;
- use negative tests rather than only happy-path checks;
- preserve authorization and human authority even when model behavior is unreliable;
- separate prevention from detection;
- generate machine-readable raw evidence;
- bind evidence to exact repository state;
- detect configuration, data, model or artifact change where designed;
- preserve fail-safe / rollback behavior in defined synthetic cases;
- reconcile test results to existing risk/control IDs; and
- constrain governance claims when evidence is synthetic.

## 5. What the programme does not prove

The programme does **not** establish:

- production operating effectiveness;
- production forecast/model accuracy;
- universal robustness against adversarial attacks;
- real supplier/platform security;
- legal compliance or conformity;
- ISO/IEC 27001 or ISO/IEC 42001 certification/conformity;
- product safety;
- sustained human-review quality;
- real incident-response performance;
- independent assurance;
- actual organizational adoption at scale; or
- realized business/safety outcomes.

These are evidence boundaries, not hidden deficiencies.

## 6. Cross-system assurance themes

The five system increments collectively exercise the following themes:

- authorization and context boundary;
- sensitive-data / provider boundary;
- prompt injection and retrieved-content trust;
- API/session/public-exposure security;
- adversarial-model containment;
- human release / planning / escalation authority;
- generated-code and tool privilege;
- dependency / artifact / provenance integrity;
- data poisoning and historical-revision integrity;
- training-serving skew and material-change detection;
- drift / data-quality discrimination;
- telemetry / detection / evidence correlation;
- stale-state handling, fail-safe behavior and rollback; and
- governance reconciliation after technical testing.

Coverage is intentionally heterogeneous. A theme tested on one system is not assumed to be effective on every other system.

## 7. Open assurance gaps preserved at closure

The programme closes the **first-wave build**, not the unresolved enterprise evidence gaps.

Material open boundaries include:

- `IAF-2026-002` — DuckDesign competent-engineer approval evidence remains open;
- `IAF-2026-003` — FeatherForecast human-planning approval evidence remains open;
- DuckDesign production/product-safety evidence remains absent;
- FeatherForecast production forecast/drift/monitoring evidence remains absent;
- QuackBot production gate blockers remain unresolved;
- WingInspect model/system performance under real manufacturing conditions remains unverified;
- PondGPT production authorization inheritance, DLP/SIEM and provider behavior remain unverified; and
- supplier/platform claims remain subject to actual third-party evidence.

## 8. Programme closure statement

The first-wave Phase II technical-assurance programme is **COMPLETE FOR PORTFOLIO PUBLICATION** because:

- five materially different AI-security patterns have completed the defined technical evidence chain;
- vulnerable and hardened behavior is reproducible;
- canonical commits and evidence IDs exist;
- results have been reconciled into governance without unauthorized maturity upgrades; and
- residual evidence gaps remain visible.

Future technical work should therefore be **triggered by a documented gap, a new threat class, a material architecture/use change, evaluator feedback, or a requirement for production-equivalent evidence**—not by a desire to increase artifact count.
