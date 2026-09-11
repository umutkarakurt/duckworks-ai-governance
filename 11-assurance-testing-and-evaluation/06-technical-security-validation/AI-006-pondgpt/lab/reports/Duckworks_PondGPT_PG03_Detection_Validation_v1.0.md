# PondGPT PG-03 — Detection Validation Record

**Document ID:** DW-AI006-PG03-DET-01  
**Version:** 1.0  
**Date:** 10 September 2026  
**Status:** Synthetic lab detection-validation record; repository replay pending  
**Control linkage:** `PG-03`, supporting `PG-05`

## Purpose

This record separates **security prevention** from **detection coverage**. A prompt-injection detector is not treated as an authorization boundary.

## Observed result

The `PG03-T005` obfuscation set contains five safe synthetic variants. The deliberately simple detector identified **4 of 5** variants and missed **1 of 5**.

The hardened lab nevertheless returned:

- `restricted_context_chunks_total = 0`;
- `provider_restricted_chunks_total = 0`; and
- overall `PG03-T005 = PASS`.

This is the intended design outcome: a missed detector signal does not grant access because authorization is enforced independently and before context construction.

## Other detection/telemetry observations

All hardened test cases generate a `security_test.result` event and carry a consistent `security_test_id` and correlation ID across the events produced for that test. Relevant event families include authorization, retrieval, ingestion integrity, model/request policy, tool authorization/execution where applicable, and the final security-test result.

The lab records metadata and decisions rather than raw restricted document bodies in telemetry. `PG03-T007` confirms that the synthetic secret canary is absent from hardened telemetry.

## Limitation

This does not validate a production SIEM, alert pipeline, analyst response process, false-positive rate, detection latency, or enterprise detection threshold. The detector is a synthetic fixture used to demonstrate the architectural principle that **prevention must not depend on prompt-injection classification accuracy**.
