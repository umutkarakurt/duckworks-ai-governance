# Duckworks Portfolio Evaluator Guide v1.0

## What this portfolio demonstrates

Project W.I.N.G. is a fictional, evidence-conscious AI governance case study. Its strongest evidence is not the number of documents. It is the traceable chain from inventory and risk through controls, execution evidence, testing, governance decisions, monitoring, management review and internal audit.

The portfolio is designed to demonstrate capability relevant to AI Governance Lead, Responsible AI, AI Risk, GRC, technology assurance and ISO/IEC 42001 readiness roles.

## Five-minute review

Use this route to determine whether a deeper review is worthwhile.

1. Read the [Executive AI Governance Decision Brief](../12-monitoring-reporting-and-roadmap/Duckworks_Executive_AI_Governance_Decision_Brief_v1.0.md).
2. Inspect the [AIMS Master Crosswalk v1.6](../11-assurance-testing-and-evaluation/03-iso42001/Duckworks_AIMS_Master_Crosswalk_v1.6.xlsx).
3. Open one worked evidence chain:
   - [WingInspect human release gate](../80-operating-evidence/AI-004-winginspect/)
   - [DuckTalent fairness and change response](../80-operating-evidence/AI-005-ducktalent/)
   - [PondGPT authorization regression](../80-operating-evidence/AI-006-pondgpt/)
4. Review the [claim-boundary register](Duckworks_Portfolio_Claim_Boundary_Register_v1.0.csv).

## Fifteen-minute review

Use this route to assess operating-model and assurance depth.

1. Follow the five-minute review.
2. Review the [AI Governance Charter](../06-governance-operating-model/) and RACI to understand decision rights and three-lines separation.
3. Review the [risk methodology](../04-risk-assessment/) and confirm that internal risk ratings are separated from legal classification.
4. Review the [PondGPT supplier case](../09-third-party-ai-governance/02-worked-supplier-case/AI-006-pondgpt/) for due diligence, contract conditions, monitoring and change response.
5. Review the [AIMS management-review cycle](../12-monitoring-reporting-and-roadmap/01-aims-management-review-cycle/) and [internal-audit programme](../11-assurance-testing-and-evaluation/05-aims-internal-audit-programme/).
6. Inspect the latest [Evidence reproducibility workflow](../.github/workflows/evidence-tests.yml) to see the executable controls and semantic checks.

## Thirty-minute review

Use this route for interview preparation, portfolio assurance or technical challenge.

1. Follow the fifteen-minute review.
2. Trace a single risk across the master crosswalk, source document, control evidence, test result and decision record.
3. Examine a deliberately failing scenario and its remediation:
   - DuckTalent unapproved proxy feature;
   - PondGPT Finance connector authorization defect; or
   - AIMS overdue or dependency-blocked management action.
4. Check that successful retesting does not silently create deployment approval, close unrelated risks or imply production effectiveness.
5. Review the [ISO/IEC 42001 evidence baseline v1.7](../11-assurance-testing-and-evaluation/03-iso42001/duckworks-iso42001-evidence-baseline-v1.7.md) and identify the retained enterprise evidence gaps.
6. Use the [competency-to-evidence map](Duckworks_Competency_to_Evidence_Map_v1.0.xlsx) to select role-relevant evidence.

## Three strongest evidence chains

### 1. WingInspect Vision: human authority over a safety-relevant decision

- Risk: a material defect is missed and an unsafe component progresses.
- Control: `WI-01`, qualified human final inspection and mandatory release authorization.
- Evidence: synthetic inspection records, overrides and control-test workpaper.
- Decision: restricted pilot remains in place.
- Limitation: no production operation, product-safety validation or measured risk reduction.

### 2. PondGPT: technical authorization and supplier governance

- Risk: retrieval or connector permissions expose restricted information.
- Controls: permission-aware retrieval and automated regression/DLP testing.
- Evidence: authorization matrix, executable test, seeded defect, exception, remediation and retest.
- Extension: supplier due diligence, contract controls, conditional gate and material-change response.
- Limitation: no validated production connector inheritance, live DLP/SIEM operation or real supplier assurance.

### 3. DuckTalent: fairness control, governance gate and change response

- Risk: ranking logic or proxy features disadvantage applicants.
- Controls: approved-feature governance and pre-deployment fairness/adverse-impact testing.
- Evidence: matched synthetic applicants, executable test, exception, blocked gate, remediation and retest.
- Extension: a later material-change event reintroduces the prohibited feature, triggers reassessment and preserves the deployment block.
- Limitation: no real applicants, legal discrimination finding or production fairness validation.

## Questions a skeptical evaluator should ask

1. Which records show a control actually operating, and which are only design artifacts?
2. What decision changed because of the evidence?
3. Which claims depend on synthetic data or fictional approvals?
4. Does a passing test grant deployment approval or merely satisfy one prerequisite?
5. Are owners, reviewers and Internal Audit responsibilities separated?
6. Which production evidence remains unavailable?
7. Can the results be regenerated from the repository?

## Suggested opening statement

> Project W.I.N.G. is a fictional AI governance portfolio built to show how I translate AI risks into owned controls, reproducible evidence, assurance tests and management decisions. The repository deliberately separates design evidence and synthetic execution from production effectiveness, legal compliance and certification claims.

