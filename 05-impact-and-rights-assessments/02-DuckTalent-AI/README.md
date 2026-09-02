# DuckTalent AI — Enhanced Impact and Rights Assessment

**Repository path:** `05-impact-and-rights-assessments/02-DuckTalent-AI/`  
**Status:** Pre-deployment / current gate: DO NOT DEPLOY  

[← Back to main portfolio](../../README.md) · [↑ Parent folder](../README.md)

This folder is the portfolio's most detailed system-specific assessment set. DuckTalent AI (AI-005) is a proposed recruitment decision-support capability that can materially influence access to employment.

## Current artifacts

- `Duckworks_Algorithmic_Impact_Assessment_DuckTalent_v1.0.md`
- `Duckworks_EU_Fundamental_Rights_Impact_Assessment_DuckTalent_v1.0.md`
- `Duckworks_GDPR_Data_Protection_Impact_Assessment_DuckTalent_v1.0.md`
- `01-huderia/` — Council of Europe HUDERIA-based assessment sequence.
- [`../../80-operating-evidence/AI-005-ducktalent/`](../../80-operating-evidence/AI-005-ducktalent/) — synthetic `DT-02` pre-deployment fairness/adverse-impact operating-evidence demonstration.

## Current governance position

**DO NOT DEPLOY with real applicants** until blocking legal, privacy, fairness, accessibility, human-oversight, security/vendor, validation, and evidence gaps are addressed and formally reviewed.

## Important legal distinctions

DuckTalent's recruitment purpose creates a strong preliminary route to EU AI Act Annex III recruitment classification, but legal role, final implementation facts, and applicable timing require Legal/Compliance confirmation.

The FRIA in this portfolio is intentionally described as **voluntary Article 27-aligned work on current Duckworks assumptions**, not as a claim that Article 27 legally requires Duckworks to perform that FRIA.

The DPIA treats a GDPR DPIA as required before deployment on the current project assumptions, while lawful basis, actual processing design, jurisdiction-specific employment rules, and any Article 36 prior-consultation question remain subject to verified facts and specialist review.

## Related operating evidence

The worked `DT-02 — Pre-Deployment Fairness & Adverse-Impact Testing` package demonstrates an executable synthetic control over 24 matched synthetic applicants. It deliberately introduces an unapproved `Career_Gap_Months` scoring penalty, detects the resulting matched-pair/group effect, blocks the deployment gate, removes the feature, and retests the complete synthetic population.

**Evidence state:** **Designed → Synthetic technical implementation demonstrated → Synthetic fairness execution demonstrated → Synthetic operation tested**

This is supporting portfolio evidence only. It does not validate real applicant fairness, production feature governance, legal discrimination compliance, lawful use of protected-characteristic data, or a change to the **DO NOT DEPLOY** gate.

## Reviewer focus

Look for consistency across intended purpose, human decision boundary, affected applicants, data use, risk treatment, contestability, fairness evidence, and the release decision.

---

> **Portfolio boundary:** Duckworks, Project W.I.N.G., its personnel, systems, datasets, decisions, controls, and evidence are fictional or synthetic unless a file explicitly identifies a public source. Folder descriptions explain the intended governance role of the artifacts; they do not convert draft, planned, or template material into implemented controls, legal compliance, certification, or independent assurance.
