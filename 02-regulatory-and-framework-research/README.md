# Regulatory and Framework Research

**Repository path:** `02-regulatory-and-framework-research/`  
**Status:** Research baseline — verify currency before reuse  

[← Back to main portfolio](../README.md)

This folder contains the legal, regulatory, standards, framework, and technical-security reference research used to inform Project W.I.N.G. governance and Phase II security-engineering decisions.

## Current artifacts

- `Duckworks_AI_Governance_Regulatory_and_Framework_Research_Report_v1.0.md` — narrative research report using a stated evidence hierarchy and system-by-system applicability analysis.
- `Duckworks_AI_Governance_Regulatory_and_Framework_Research_Report_v1.0.pdf` — formatted review copy.
- `Duckworks_AI_Governance_Obligations_and_Guidance_Register_v1.0.xlsx` — structured obligations/guidance register for traceable review.
- [`Duckworks_Technical_AI_Security_Reference_and_Applicability_Baseline_v1.0.md`](Duckworks_Technical_AI_Security_Reference_and_Applicability_Baseline_v1.0.md) — Phase II PondGPT-specific technical-security baseline separating binding law, standards/frameworks, official cybersecurity guidance, technical threat references, and internal engineering requirements.
- The repository root [`REFERENCES.md`](../REFERENCES.md) is the controlled public-source catalogue.


## Phase II technical-security research

Phase II extends the research layer without treating security guidance as law.

For **AI-006 PondGPT**, the **[Technical AI Security Reference & Applicability Baseline](Duckworks_Technical_AI_Security_Reference_and_Applicability_Baseline_v1.0.md)** is the detailed working source for technical-security architecture, threat modelling, and later adversarial validation.

It distinguishes:

1. **Mandatory legal requirements** — only where the relevant legal scope and trigger are established, including GDPR and potentially NIS2; EU AI Act Article 15 is not currently asserted as mandatory for PondGPT because the documented intended purpose does not establish high-risk classification.
2. **Standards and formal frameworks** — including ISO/IEC 27001, ISO/IEC 42001, NIST CSF 2.0, NIST AI RMF, NIST AI 600-1, NIST AI 100-2 E2025, and NIST SP 800-218A.
3. **Official cybersecurity guidance** — including ENISA and the NCSC/international secure-AI-development guidance.
4. **Recognized technical threat/security references** — including MITRE ATLAS, OWASP GenAI Security, and OWASP API Security.
5. **Duckworks engineering requirements and assumptions** — internal design decisions used to make the synthetic portfolio technically executable.

Framework or technique mapping is used to improve coverage and traceability; it does not independently establish legal compliance, certification, control effectiveness, or production security.

## Evidence hierarchy

The project distinguishes:

1. **Binding legal text** — mandatory where the relevant scope and trigger apply.
2. **Official regulator, government, or competent-authority guidance** — interpretation, cybersecurity, and implementation support.
3. **Standards and formal frameworks** — voluntary unless made binding through another mechanism.
4. **Recognized technical threat/control guidance** — used for threat, architecture, test, and control design, not as law.
5. **Duckworks organizational practices and assumptions** — internal governance only.

## Important interpretation rule

Do not treat ISO, NIST, ENISA, MITRE, OWASP, OECD, or similar mappings as proof of legal compliance or certification. Likewise, a Duckworks High/Critical risk rating does not establish an EU AI Act legal classification.

Regulatory applicability remains dependent on intended purpose, legal role, jurisdiction, affected persons, product context, data processing, and current law. Re-verify primary sources before using this material for any real-world conclusion.

Living technical sources such as MITRE ATLAS and OWASP GenAI Security should also be re-checked when assigning current technique or category identifiers to a Phase II test case.

---

> **Portfolio boundary:** Duckworks, Project W.I.N.G., its personnel, systems, datasets, decisions, controls, and evidence are fictional or synthetic unless a file explicitly identifies a public source. Folder descriptions explain the intended governance role of the artifacts; they do not convert draft, planned, or template material into implemented controls, legal compliance, certification, or independent assurance.
