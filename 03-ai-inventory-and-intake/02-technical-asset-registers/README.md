# Technical Asset Registers

**Repository path:** `03-ai-inventory-and-intake/02-technical-asset-registers/`  
**Status:** Portfolio baseline / synthetic  

[← Back to main portfolio](../../README.md) · [↑ Parent folder](../README.md)

This folder contains lower-level technical registers that complement the AI system inventory.

## Current artifacts

- `Duckworks_AI_Asset_Inventory_v1.0.xlsx`
- `Duckworks_AI_Bill_of_Materials_Register_v1.0.xlsx`

## Purpose

The AI system inventory identifies the governed business use. These registers support technical traceability by documenting material assets and component dependencies associated with those systems.

A mature implementation would use this layer to support questions such as:

- Which model, service, library, API, dataset, connector, or infrastructure component supports the AI system?
- Which component is third-party supplied?
- Which versions or dependencies may invalidate prior evidence when changed?
- Which technical component creates security, licensing, resilience, or supply-chain exposure?

## Evidence rule

An asset register or AI BOM is not proof that all dependencies have been verified. Unknown or inferred component information should remain identified as such, and material vendor/model changes should feed the change-management and reassessment process.

---

> **Portfolio boundary:** Duckworks, Project W.I.N.G., its personnel, systems, datasets, decisions, controls, and evidence are fictional or synthetic unless a file explicitly identifies a public source. Folder descriptions explain the intended governance role of the artifacts; they do not convert draft, planned, or template material into implemented controls, legal compliance, certification, or independent assurance.
