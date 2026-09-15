# AI-002 QuackBot — AI Interaction Disclosure Design Assertion

**Document ID:** DW-AI002-COMP-TRANS-01  
**Version:** 1.0  
**Date:** 14 September 2026  
**System:** AI-002 — QuackBot  
**Status:** Synthetic design assertion — local PASS  
**Related machine record:** `evidence/generated/compliance/QB-COMP-001.json`

## 1. Purpose

This record keeps QuackBot's AI-interaction transparency check separate from the adversarial-security test set.

The QuackBot applicability addendum identifies EU AI Act Article 50 direct-interaction transparency as a mandatory-law applicability item for this customer-facing chatbot design, subject to confirmation of Duckworks' legal role and any applicable exception.

## 2. Synthetic assertion

The hardened synthetic interaction flow displays:

> **You are interacting with Duckworks QuackBot, an AI-assisted support service.**

before or at the first interaction.

Machine assertion:

`QB-COMP-001 — shown_before_or_at_first_interaction = true`

Local result: **PASS**

## 3. What this PASS demonstrates

It demonstrates only that the **synthetic target interaction flow contains the disclosure design requirement**.

## 4. What this PASS does not demonstrate

It does not establish:

- full Article 50 compliance;
- Duckworks' exact legal role;
- exception analysis;
- actual production UI placement;
- accessibility/usability effectiveness;
- language/localization sufficiency;
- production user comprehension; or
- broader EU AI Act compliance.

## 5. Governance effect

This assertion does not change AI-002 risk scores, control maturity, assumptions or the production-blocked gate.

It should remain separately traceable from `QBSEC-T001`–`QBSEC-T012` so a legal-transparency requirement is not misrepresented as a security penetration-test result.
