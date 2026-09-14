# AI-002 QuackBot — Phase II Technical Architecture

**System:** AI-002 — QuackBot  
**Business function:** Customer Operations  
**Current governance gate:** **Pre-Production / Production Blocked**  
**Status:** Synthetic security-architecture baseline established; technical validation not yet executed

## Current artifact

- [`Duckworks_QuackBot_Technical_Security_Architecture_v1.0.md`](Duckworks_QuackBot_Technical_Security_Architecture_v1.0.md)

The architecture turns QuackBot's public-facing GenAI/RAG/API risk into explicit trust boundaries and testable requirements.

Core boundaries include:

- public/anonymous versus authenticated customer mode;
- session and cache isolation;
- public versus customer-specific retrieval;
- RAG source allowlisting and provenance;
- retrieval authorization before context creation;
- hosted model/provider data minimization;
- grounding/citation/abstention;
- human escalation;
- safe output rendering;
- tool/action denial by default;
- rate/resource controls;
- telemetry/correlation; and
- model/config/KB/auth-policy change-triggered regression.

Two core invariants are:

> **The model is not an access-control mechanism. Customer/account authorization must be enforced before private content enters model context.**

> **Retrieved content and model output are untrusted data. Neither acquires application authority because an LLM processed or generated it.**

Related artifacts:

- [`../../03-threat-models/AI-002-quackbot/Duckworks_QuackBot_Threat_Model_v1.0.md`](../../03-threat-models/AI-002-quackbot/Duckworks_QuackBot_Threat_Model_v1.0.md)
- [`../../../02-regulatory-and-framework-research/Duckworks_QuackBot_Technical_Security_Reference_Applicability_Addendum_v1.0.md`](../../../02-regulatory-and-framework-research/Duckworks_QuackBot_Technical_Security_Reference_Applicability_Addendum_v1.0.md)

## Evidence boundary

This is a target design, not evidence that a production QuackBot deployment uses this architecture.

It does not establish operating effectiveness, customer-data isolation in production, legal compliance, supplier compliance, production RAG integrity, API security, or deployment readiness.

The production gate remains **blocked**.
