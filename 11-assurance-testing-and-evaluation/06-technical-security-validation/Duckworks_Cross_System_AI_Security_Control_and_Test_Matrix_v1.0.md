# Project W.I.N.G. — Cross-System AI Security Control & Test Coverage Matrix

**Document ID:** DW-WING-SEC-MATRIX-01  
**Version:** 1.0  
**Effective date:** 15 September 2026  
**Owner:** Cassandra Duckley — Chief Information Security Officer  
**Status:** Phase II consolidated coverage view — synthetic / non-production

> This matrix shows **synthetic technical-assurance coverage**, not production control effectiveness. A `P` or `S` means the theme is exercised by the defined lab/evidence chain for that system; it does not mean the control is production-effective.

## 1. Legend

- **P — Primary:** directly challenged by one or more canonical campaign cases.
- **S — Supporting:** materially exercised by the campaign but not the primary assurance objective.
- **— — Not first-wave tested:** not a material target of that system's first-wave campaign.

Systems:

- **PG:** AI-006 PondGPT
- **WI:** AI-004 WingInspect Vision
- **QB:** AI-002 QuackBot
- **DD:** AI-001 DuckDesign AI
- **FF:** AI-003 FeatherForecast

## 2. Cross-system coverage

| Security / assurance theme | PG | WI | QB | DD | FF | Representative evidence / interpretation |
|---|:---:|:---:|:---:|:---:|:---:|---|
| Identity / authorization boundary | P | — | P | S | P | PG permission-aware retrieval; QB session/API/RAG authorization; FF planning-data access |
| Sensitive-data / provider boundary | P | — | P | P | P | restricted-context prevention, customer/planning/engineering-data boundaries and canary non-disclosure |
| Direct / indirect prompt injection | P | — | P | S | — | PondGPT and QuackBot primary; DuckDesign imported-content authority boundary is analogous but not a general RAG campaign |
| RAG / corpus poisoning | P | — | P | — | — | PondGPT and QuackBot challenge retrieved-content trust/integrity |
| Public API / session / anonymous abuse | S | — | P | — | — | QuackBot is the primary internet-facing API/RAG case |
| Adversarial-model / evasion robustness | — | P | — | — | — | WingInspect adversarial/occlusion/evasion case; model can remain imperfect while system controls contain the condition |
| Human release / approval / decision authority | — | P | S | P | P | WI release authority, QB escalation/handoff mechanics, DD engineer/safety approval, FF planning approval |
| Generated-code security | — | — | — | P | — | DD prohibited shell/file/network behavior and staging/scanning |
| Tool privilege / egress control | S | — | S | P | — | DD primary; PondGPT/QuackBot supporting tool/connector boundaries |
| Dependency / package integrity | — | — | S | P | — | DD dependency allowlisting/hash/provenance primary; QB supporting supplier/API dependency boundary |
| Build / artifact provenance / SBOM | — | — | — | P | — | DD promotion blocked when provenance/SBOM incomplete |
| Source-data poisoning / extreme-value manipulation | S | — | S | — | P | FF primary; PG/QB poisoning relates to retrieved-content/corpus rather than forecasting source data |
| Historical backfill / data-lineage integrity | — | — | — | — | P | FF unapproved history revision/backfill control |
| Training-serving schema / feature skew | — | S | — | — | P | FF primary; WI has supporting distribution/validation boundary rather than the same pipeline mechanism |
| Model / configuration / threshold integrity | S | S | S | P | P | DD and FF primary; other systems include change/replay/configuration controls |
| Drift / data-quality discrimination | — | S | — | — | P | FF primary; WI supports shift/validation but not the same forecasting drift classifier |
| Output / forecast / artifact integrity | S | P | S | P | P | system-specific output validity, artifact hash, forecast integrity and safe-release logic |
| Access logging / audit record integrity | S | S | P | S | P | correlated decision/access/security evidence across multiple systems |
| Detection / telemetry validation | P | P | P | P | P | all five increments separate control outcome from detector/control signal |
| Stale-state / availability handling | — | S | P | S | P | FF primary manual/degraded mode; QB public-service resilience; DD rollback; WI fail-safe release |
| Known-good rollback / recovery | S | S | S | P | P | DD/FF explicit; other systems have narrower remediation/replay/recovery evidence |
| Material-change / revalidation trigger | S | P | S | P | P | change should invalidate prior assurance where relevant |
| Third-party / provider technical boundary | S | S | S | S | S | provider/platform interaction represented, but **supplier assurance is not established** |
| Commit-bound reproducibility | P | P | P | P | P | all five canonical increments bound evidence to an exact repository commit |
| Governance reconciliation | P | P | P | P | P | every completed increment returns evidence to existing risk/control/gate logic |

## 3. Representative canonical test coverage

### PondGPT — PG-03

Primary technical themes:

- prompt injection;
- RAG poisoning / retrieved-content trust;
- authorization boundary;
- restricted-context / provider-boundary protection;
- detector-versus-prevention separation; and
- commit-bound replay.

Important interpretation:

> One detector variant can be missed while the authorization boundary still prevents restricted content from entering the model/provider context. Detection coverage is not the authorization control.

### WingInspect Vision

Primary technical themes:

- adversarial / corrupted visual input;
- robustness and validation mismatch;
- independent human release authority;
- fail-safe containment; and
- detection/control-signal validation.

Important interpretation:

> The model does not have to become invulnerable for the system-level control to pass. `WISEC-T001` remains a useful example: the surrogate model can still miss a patched/occluded defect while the hardened system blocks unsafe release through validation and human authority.

### QuackBot

Primary technical themes:

- public-facing RAG/API boundary;
- session/authorization isolation;
- prompt/RAG manipulation;
- unsafe API/resource behavior;
- customer-data leakage prevention;
- escalation/handoff mechanics; and
- AI-interaction disclosure as a separate design assertion.

Important interpretation:

> `QB-COMP-001` is a synthetic interaction-disclosure design assertion. It is deliberately separated from the adversarial-security campaign and does not establish full legal compliance.

### DuckDesign

Primary technical themes:

- engineering-IP/provider boundary;
- indirect imported-content authority;
- generated-code containment;
- dependency/hash integrity;
- CAD/simulation tool privilege;
- independent engineering validation;
- safety-gate bypass prevention;
- exact-artifact approval binding;
- material-change regression;
- provenance/SBOM; and
- known-good rollback.

Important interpretation:

> `DDSEC-T009` proves only the synthetic exact-artifact approval mechanism. It does not prove that competent-engineer approval operates across a real defined-period population.

### FeatherForecast

Primary technical themes:

- source-data poisoning;
- historical backfill integrity;
- training-serving skew;
- feature/model/configuration integrity;
- drift versus data-quality discrimination;
- forecast integrity/staleness;
- human planning approval;
- decision-record integrity;
- planning-data access;
- outage/manual fallback; and
- retraining/rollback.

Important interpretation:

> `FFSEC-T006` distinguishes only the defined synthetic data-quality and drift cases. It does not validate production drift thresholds or universal drift detection.

## 4. Control-family conclusions

### Strongest cross-system patterns

The portfolio has its strongest synthetic technical evidence around:

- explicit trust boundaries;
- human authority / release / commitment gates;
- version/change binding;
- negative/adversarial testing;
- fail-safe outcomes;
- evidence correlation;
- same-test remediation/retest; and
- commit-bound reproducibility.

### Moderate / system-specific coverage

Coverage exists but is concentrated in one or two systems for:

- adversarial computer vision;
- generated-code security;
- software-supply-chain provenance;
- forecasting poisoning/backfill;
- training-serving skew;
- drift interpretation; and
- public-facing API/resource controls.

This is acceptable for the first-wave portfolio because those are intentionally differentiated system cases.

## 5. Material technical coverage gaps at closure

The first-wave programme did **not** attempt to provide comprehensive coverage of every AI-security threat class.

Not materially covered, or only indirectly covered:

- model extraction / model stealing;
- membership inference / model inversion;
- privacy attacks against trained model parameters;
- federated-learning attacks;
- multi-agent / agent-to-agent trust;
- autonomous agent external-action safety at scale;
- real cloud/Kubernetes/IaC hardening;
- GPU/runtime isolation;
- cryptographic model signing across a real MLOps platform;
- real secrets-management infrastructure;
- full software-composition/container-scanning programme;
- sustained denial-of-service / capacity testing against real services;
- AI-007 shadow-GenAI discovery / endpoint / network containment; and
- production red-team operations against authorized live systems.

These should be treated as **future scope candidates only where a documented risk/use case justifies them**.

## 6. Coverage conclusion

The first-wave Phase II programme is broad enough to demonstrate a coherent assurance method across **five different AI system/security patterns** without pretending to be a comprehensive enterprise red-team programme.

The closure decision therefore favors:

> **consolidate and preserve the method; add new testing only when a new risk class, system architecture or production-evidence requirement justifies it.**
