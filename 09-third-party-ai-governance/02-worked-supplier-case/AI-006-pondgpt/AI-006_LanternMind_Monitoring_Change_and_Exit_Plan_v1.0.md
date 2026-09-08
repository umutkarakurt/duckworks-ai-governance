# PondGPT Supplier Monitoring, Change and Exit Plan

**Plan ID:** `TPR-MON-AI006-2026-001`  
**Version / date:** 1.0 / 8 September 2026  
**Owner:** Percival Duckworth — Director Procurement & Vendor Assurance  
**System owner:** Oliver Duckett — Head of IT & Cloud

## 1. Monitoring plan

| Metric / event | Threshold | Frequency | Evidence | Owner | Response |
|---|---|---|---|---|---|
| Material supplier changes received before activation | 100% | Per change / quarterly confirmation | Notice and change log | Procurement | Block activation and open reassessment if notice is missing or late. |
| Unapproved subprocessors or locations | 0 | Monthly during pilot | Supplier register comparison | Procurement + DPO | Suspend affected processing/connector; assess transfer and contract impact. |
| Confirmed supplier security/privacy incidents | 0 unresolved | Continuous; monthly review | Incident notice and action log | CISO | Contain, preserve evidence, assess notification duties and invoke stop-use if needed. |
| Notification timeliness | Within executed contractual window; proposed target 24 hours | Per incident | Timestamped notice | CISO | Escalate breach; reassess supplier and lifecycle gate. |
| Critical assurance findings overdue | 0 | Quarterly | Assurance review tracker | CISO | Freeze expansion; require remediation and verification. |
| Evidence items expired or unavailable | 0 mandatory items for broader rollout | Quarterly / pre-renewal | Evidence register | Procurement | Preserve restricted-pilot gate; block renewal/expansion as applicable. |
| Permission-regression pass before expansion | 100% | Per connector/group/corpus change | `PG-02` run evidence | Head of IT & Cloud | Block expansion and open exception. |
| Availability below agreed objective | 2 consecutive periods or one material outage | Monthly | Service report and outage record | Head of IT & Cloud | Invoke continuity review and exit-readiness assessment. |
| Export/restore test success | 100% | Annually and pre-renewal | Test log | Head of IT & Cloud | Block renewal if unresolved. |
| Deletion evidence after termination/request | 100% | Per event | Supplier/subprocessor attestation | DPO | Escalate contract and privacy exception. |

## 2. Material-change workflow

1. Log the notice with exact service/model/version, affected data, regions, subprocessors and effective date.
2. Compare it with the approved supplier, privacy, security, risk, control and technical baselines.
3. Invalidate affected evidence where the change alters its scope or assumptions.
4. Run required technical regression/adversarial tests.
5. Obtain privacy, security, legal, procurement and AI-governance challenge.
6. Record approve, conditionally approve, reject or exit before activation.

## 3. Exit plan

| Phase | Required action | Evidence | Owner |
|---|---|---|---|
| Prepare | Maintain current data/source inventory, configuration inventory, dependency map and successor criteria. | Quarterly exit-readiness checklist | Head of IT & Cloud |
| Trigger | Activate for material breach, unacceptable change, repeated outage, unresolved critical finding, insolvency, legal restriction or strategic termination. | Authorized exit decision | CRCO + Business Owner |
| Contain | Disable new prompts/connectors, revoke supplier/admin access and preserve logs. | Access-revocation and preservation records | Head of IT & Cloud + CISO |
| Export | Export permitted content, configuration and audit evidence in documented formats; verify integrity and restore usability. | Export/restore test | Head of IT & Cloud |
| Transition | Move approved functions to a successor/manual process without importing unapproved data or unsafe configurations. | Transition acceptance record | Business Owner |
| Delete | Require deletion across primary, backup and subprocessor environments within the executed term. | Deletion attestation and exception record | DPO + Procurement |
| Close | Review residual obligations, incidents, IP, records retention and lessons learned. | Exit closure record | AI Governance Lead |

No successful export, restoration, transition or deletion has been performed in this synthetic case. Exit readiness is therefore designed, not operationally validated.

