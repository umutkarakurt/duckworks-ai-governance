# AI-006 PondGPT — Supplier-Governance Evidence Package

**Supplier:** LanternMind Enterprise AI Ltd. (fictional)  
**Service:** Hosted enterprise LLM service supporting PondGPT  
**AI system:** `AI-006 — PondGPT`  
**Primary risk:** `AI-006-R01 — Privacy & data governance`  
**Primary control:** `AI-TPR-01 — AI Supplier Due Diligence & Contract Controls`  
**Control owner:** Percival Duckworth — Director Procurement & Vendor Assurance  
**System/risk owner:** Oliver Duckett — Head of IT & Cloud  
**Current gate:** Restricted pilot only; broader rollout blocked  
**Evidence classification:** Portfolio / synthetic / non-production

## Purpose

This worked case demonstrates a complete, bounded supplier-governance chain:

**intake → due diligence → evidence gaps → supplier risk → contractual treatment → gate decision → monitoring → material-change response → exit readiness**

The package closes the prior portfolio-design gap in AIMS theme `M13`. It does not prove that LanternMind exists, that any contract was executed, that any supplier evidence was independently verified, or that PondGPT is ready for production.

## Evidence chain

| Evidence ID | Artifact | Demonstrated state |
|---|---|---|
| `EV-AI006-009` | Supplier assessment | Synthetic due-diligence workflow demonstrated |
| `EV-AI006-010` | Due-diligence evidence register | Synthetic evidence collection and gap classification demonstrated |
| `EV-AI006-011` | Supplier risk assessment | Synthetic supplier-risk evaluation demonstrated |
| `EV-AI006-012` | Contract control schedule | Synthetic contractual treatment design demonstrated |
| `EV-AI006-013` | Supplier gate decision | Synthetic procurement/lifecycle decision demonstrated |
| `EV-AI006-014` | Monitoring, change and exit plan | Synthetic oversight and exit design demonstrated |
| `EV-AI006-015` | Material-change event and response | Synthetic supplier-change reassessment demonstrated |
| `EV-AI006-016` | Executable supplier gate and result | Synthetic gate implementation and execution demonstrated |

## Package contents

- [`AI-006_LanternMind_Supplier_Assessment_v1.0.md`](AI-006_LanternMind_Supplier_Assessment_v1.0.md)
- [`AI-006_LanternMind_Due_Diligence_Evidence_Register_v1.0.csv`](AI-006_LanternMind_Due_Diligence_Evidence_Register_v1.0.csv)
- [`AI-006_LanternMind_Supplier_Risk_Assessment_v1.0.md`](AI-006_LanternMind_Supplier_Risk_Assessment_v1.0.md)
- [`AI-006_LanternMind_Contract_Control_Schedule_v1.0.md`](AI-006_LanternMind_Contract_Control_Schedule_v1.0.md)
- [`AI-006_LanternMind_Supplier_Gate_Decision_v1.0.md`](AI-006_LanternMind_Supplier_Gate_Decision_v1.0.md)
- [`AI-006_LanternMind_Monitoring_Change_and_Exit_Plan_v1.0.md`](AI-006_LanternMind_Monitoring_Change_and_Exit_Plan_v1.0.md)
- [`AI-006_LanternMind_Material_Change_Event_v1.0.md`](AI-006_LanternMind_Material_Change_Event_v1.0.md)
- [`supplier_gate_config.json`](supplier_gate_config.json)
- [`supplier_gate_check.py`](supplier_gate_check.py)
- [`AI-006_LanternMind_Supplier_Gate_Run_Summary.json`](AI-006_LanternMind_Supplier_Gate_Run_Summary.json)

## Decision boundary

The synthetic case supports continued use only within the existing restricted pilot and approved source/data boundaries. It does not support broader rollout, sensitive-source expansion, production risk reduction, legal compliance, supplier certification, or independent assurance.

The supplier gate does not approve a supplier automatically. It converts evidence conditions into one of three review states and always requires an authorized human decision.

