# Duckworks AIMS Document and Evidence Control Standard

| Field | Value |
|---|---|
| Document ID | `AIMS-STD-DOC-001` |
| Version | 1.0 |
| Effective date | 8 September 2026 |
| Owner | Eleanor Duckford — AI Governance Lead |
| Control linkage | `AI-GOV-03` |
| Evidence IDs | `EV-AIMS-006`; `EV-AIMS-007` |
| Classification | Synthetic portfolio demonstration / non-production |

## 1. Purpose

This standard defines how authoritative AIMS documents and evidence are identified, approved, protected, retrieved, reviewed, superseded and retained. It prevents a file's presence in the repository from being mistaken for approval, currency or effectiveness.

## 2. Required control metadata

Every priority record must identify:

- stable document or evidence ID;
- authoritative repository path and format;
- owner and approval status;
- effective and next-review dates;
- access classification and retention rule;
- prior or superseding version;
- linked risk, control, decision or objective where applicable; and
- evidence boundary.

## 3. Lifecycle

| State | Minimum condition |
|---|---|
| Draft | Owner and purpose identified; not authorized for reliance |
| Under review | Named reviewers and open comments recorded |
| Approved in synthetic exercise | Human approver, date, version and scope recorded; portfolio-only boundary retained |
| Superseded | Replacement identified; prior version preserved and excluded from current-use paths |
| Archived | Retention basis recorded; access restricted as appropriate |

## 4. Change and supersession controls

- Material content changes require a new version and review of dependent crosswalks, risks, controls, evidence and decisions.
- Canonical indices must point to the current version while preserving historical versions.
- Broken links, duplicate IDs, missing owners, overdue reviews and inconsistent version references are treated as document-control exceptions.
- Automated checks may identify inconsistencies but cannot approve content or determine legal retention obligations.

## 5. Access and retention

The v1.0 register applies a portfolio rule of current version plus seven years after supersession for priority governance records. This is a synthetic management-system design choice, not a legal conclusion. Real deployment would require Records Management, Legal, Privacy and contractual validation by record class and jurisdiction.

## 6. Review cadence

The AI Governance Lead reviews the priority register monthly and after each release. Internal Audit may test retrieval, authority, completeness and supersession without owning the register.

