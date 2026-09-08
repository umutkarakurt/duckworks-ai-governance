# PondGPT Supplier Contract Control Schedule

**Schedule ID:** `TPR-CON-AI006-2026-001`  
**Version / date:** 1.0 / 8 September 2026  
**Status:** Synthetic proposed terms; no executed agreement claimed

This schedule operationalizes the Duckworks vendor-contract and DPA templates for the fictional LanternMind service. It is a governance artifact, not legal advice or an executed contract.

| Clause ID | Required control | Minimum requirement | Evidence / verification | Owner | Status |
|---|---|---|---|---|---|
| `TPR-CL-01` | Defined service and approved use | Identify service, model routing, approved users, repositories, integrations and prohibited data/actions. | Executed schedule; versioned service architecture | Procurement + Head of IT & Cloud | Proposed |
| `TPR-CL-02` | Restricted data use / no training | Supplier may process Duckworks data only to provide the service and may not train or improve models with it without separate written approval. | Executed term; configuration record; supplier attestation | DPO & Head of Privacy | Proposed — blocking |
| `TPR-CL-03` | Retention and deletion | Define retention per data type, deletion timing, backup treatment and evidence of deletion. | Configuration export; deletion procedure and attestation | DPO & Head of Privacy | Proposed — blocking |
| `TPR-CL-04` | Security and tenant isolation | Maintain documented isolation, encryption, privileged-access, vulnerability and secure-development controls. | Current assurance report; architecture/test evidence; remediation status | CISO | Proposed — blocking |
| `TPR-CL-05` | Hosting and transfers | Disclose processing/support locations and applicable transfer safeguards before processing begins. | Location register; approved transfer analysis | DPO & Head of Privacy | Proposed — blocking |
| `TPR-CL-06` | Subprocessors | Maintain a complete register and provide advance notice with a Duckworks objection/exit path. | Register; notice log; review decision | Procurement | Proposed — blocking |
| `TPR-CL-07` | Incident notification | Notify Duckworks without undue delay and within 24 hours of confirmed material impact; preserve evidence and cooperate. | Incident notice; timeline; evidence package; lessons learned | CISO | Proposed — blocking |
| `TPR-CL-08` | Material change notification | Provide 30 days’ advance notice for material model, routing, subprocessor, hosting, data-use, safety-policy or service changes; emergency changes reported promptly. | Notice; version diff; reassessment and acceptance record | AI Governance Lead | Proposed — blocking |
| `TPR-CL-09` | Audit and evidence access | Provide sufficient logs, assurance materials and investigation support, subject to proportionate safeguards. | Evidence-request and response log | Procurement + Internal Audit | Proposed — blocking |
| `TPR-CL-10` | Intellectual property | Define input/output rights, restricted uses, infringement handling and claims cooperation. | Executed terms and claim procedure | General Counsel | Proposed |
| `TPR-CL-11` | Resilience and continuity | Define availability, recovery, dependency disclosure, support and tested continuity obligations. | Service reports; recovery-test summary; outage review | Head of IT & Cloud | Proposed |
| `TPR-CL-12` | Exit, portability and deletion | Provide export, transition assistance, termination access window, return/deletion and subprocessor deletion evidence. | Successful export/restore test; termination checklist; deletion attestation | Head of IT & Cloud + DPO | Proposed — blocking |

## Acceptance rule

No “Proposed — blocking” item may be treated as an implemented contractual control. Broader rollout remains blocked until the relevant terms are executed and their technical/operational evidence is reviewed.

