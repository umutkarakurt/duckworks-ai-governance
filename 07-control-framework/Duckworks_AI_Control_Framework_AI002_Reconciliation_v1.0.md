# Duckworks AI Control Framework — AI-002 Reconciliation Addendum

**Project:** W.I.N.G. — Workflows, Intelligence, Next-Generation Governance  
**Document ID:** DW-AICF-AI002-REC-01  
**Version:** 1.0  
**Effective date:** 15 September 2026  
**Owner:** AI Governance Lead  
**Base report:** `Duckworks_AI_Control_Framework_Report_v1.6.md`  
**Scope:** AI-002 QuackBot technical-evidence reconciliation  
**Status:** Controlled overlay pending next master control-framework consolidation

> Historical source-status labels are retained until the authoritative control-library source is separately revised. Reconciled evidence maturity controls interpretation.

## Reconciled AI-002 control view

| Control | Base source status | Reconciled evidence IDs | Reconciled evidence maturity | Current risk credit | Required next evidence | Decision |
|---|---|---|---|---|---|---|
| QB-01 — Curated RAG Source Allowlist | Partially implemented | EV-AI002-001–006 | Synthetic source-allowlist/provenance/integrity implementation, failure/remediation, operation testing and commit-bound replay demonstrated | No production risk-reduction credit | Real corpus inventory, source-owner approval, provenance/integrity records, stale-content handling, exceptions and owner review | **Upgrade evidence maturity only** |
| QB-02 — Grounding, Citation & Abstention Rules | Planned | EV-AI002-001–006 | Synthetic grounding/abstention/citation behavior implemented and tested for defined material-support cases | No production risk-reduction credit | Production-equivalent answer-quality evaluation, citation correctness, real approved corpus, exceptions, customer-impact review | **Upgrade evidence maturity; retain historical Planned source label** |
| QB-03 — Human Escalation SLA | Partially implemented | EV-AI002-001–006 | Synthetic escalation trigger/handoff behavior demonstrated; SLA timing/completion not tested | No production risk-reduction credit | Real handoff population, SLA timing, completion, staffing, exceptions, quality/outcome review | **Upgrade bounded trigger/handoff evidence only** |
| QB-04 — Prompt Injection & RAG Adversarial Testing | Planned | EV-AI002-001–006 | Synthetic adversarial-test design, technical implementation, failure reproduction, hardened retest and commit-bound reproducibility demonstrated | No production risk-reduction credit | Production-equivalent regression suite against authorized identity/RAG/tool/API/provider boundaries, defined cadence, exceptions and independent challenge | **Upgrade evidence maturity; retain historical Planned source label** |
| QB-05 — Least-Privilege Retrieval & Tool Boundaries | Partially implemented | EV-AI002-001–006 | Synthetic anonymous/private separation, server-side object authorization, session isolation, tool/egress denial and provider minimization demonstrated | No production risk-reduction credit | Real authentication/session/object authorization, connector/tool inventory, egress controls, denial/allow population, exceptions and owner review | **Upgrade evidence maturity only** |
| QB-06 — GenAI Security & Harm Monitoring | Planned | EV-AI002-001–006 | Synthetic security telemetry/control-signal generation and commit-bound replay demonstrated across the twelve-case campaign | No production risk-reduction credit | Production WAF/API/RAG/provider/SIEM signals, alert routing, responder handling, retention/redaction, missed-event analysis and defined-period outcomes | **Upgrade evidence maturity; retain historical Planned source label** |

## Supporting controls deliberately not upgraded

`AI-GOV-02` receives supporting evidence from `QBSEC-T012`, but this single system-specific change-regression test does not demonstrate enterprise-wide material-change governance.

`AI-TPR-01` receives supporting evidence from `QBSEC-T011`, but payload minimization/redaction does not demonstrate supplier due diligence, contract operation or verified supplier evidence.

`AI-INC-01` receives no maturity upgrade solely from this campaign.

## Interaction-transparency evidence

`EV-AI002-007` is deliberately kept outside the six QB control rows because it is a **legal-design assertion**, not an adversarial-security control test.

It demonstrates only that the synthetic hardened interaction flow contains the AI disclosure design requirement. It does not establish full EU AI Act Article 50 compliance.

## Governance interpretation

The portfolio claim may now move from:

> “QuackBot controls are design/status assertions only.”

To:

> “Defined QuackBot application/RAG/API security mechanisms have been implemented and exercised in a deterministic synthetic lab and reproduced against a specific repository commit.”

It must **not** move to:

> “QuackBot controls are effective in production.”

The production gate remains blocked.
