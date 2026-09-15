# AI-002 QuackBot — Phase II Technical Architecture

**System:** AI-002 — QuackBot  
**Business function:** Customer Operations  
**Current governance gate:** **Pre-Production / Production Blocked**  
**Status:** Synthetic security-architecture baseline established; first local validation increment executed

## Current architecture

- [`Duckworks_QuackBot_Technical_Security_Architecture_v1.0.md`](Duckworks_QuackBot_Technical_Security_Architecture_v1.0.md)

Related validation:

- [`../../../11-assurance-testing-and-evaluation/06-technical-security-validation/AI-002-quackbot/`](../../../11-assurance-testing-and-evaluation/06-technical-security-validation/AI-002-quackbot/)

Local validation currently records **12/12 seeded vulnerable failures** and **12/12 hardened PASS**, but remains `LOCAL_UNBOUND` pending repository replay.

Two core invariants remain:

> **The model is not an access-control mechanism. Customer/account authorization must be enforced before private content enters model context.**

> **Retrieved content and model output are untrusted data. Neither acquires application authority because an LLM processed or generated it.**

## Evidence boundary

The architecture is a target design. The local lab demonstrates only synthetic behavior against that design.

It does not establish production API/session security, customer-data isolation, provider compliance, RAG integrity, legal compliance or deployment readiness.

The production gate remains **blocked**.
