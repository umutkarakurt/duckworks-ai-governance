import hashlib, json, os, platform
from dataclasses import dataclass
from pathlib import Path

LAB_VERSION = "winginspect-lab-0.1.0"
ARCH_VERSION = "DW-AI004-ARCH-SEC-01-v1.0"
THREAT_VERSION = "DW-AI004-TM-01-v1.0"
PLAN_VERSION = "DW-AI004-VAL-SEC-01-v1.0"
MODEL_VERSION = "synthetic-vision-surrogate-1.0.0"
DATASET_VERSION = "winginspect-fixtures-20260912-01"
APPROVED_MODEL_SHA = hashlib.sha256(b"winginspect-approved-model-v1").hexdigest()
APPROVED_CONFIG = {
    "preprocessing_version": "pre-1.0.0",
    "threshold_policy_version": "thr-1.0.0",
    "class_map_version": "classes-1.0.0",
    "defect_threshold": 0.25,
}
APPROVED_CONFIG_SHA = hashlib.sha256(json.dumps(APPROVED_CONFIG, sort_keys=True).encode()).hexdigest()

@dataclass(frozen=True)
class Profile:
    name: str
    quality_gate: bool
    integrity: bool
    provenance: bool
    validation_gate: bool
    fail_closed: bool
    human_release_required: bool
    model_can_release: bool

PROFILES = {
    "vulnerable": Profile("vulnerable", False, False, False, False, False, False, True),
    "hardened": Profile("hardened", True, True, True, True, True, True, False),
}

THREATS = {
    "WISEC-T001":["WIT-001","WIT-002","WIT-011"],
    "WISEC-T002":["WIT-003","WIT-005","WIT-006"],
    "WISEC-T003":["WIT-014","WIT-027"],
    "WISEC-T004":["WIT-012","WIT-013","WIT-015"],
    "WISEC-T005":["WIT-019","WIT-020","WIT-023"],
    "WISEC-T006":["WIT-021","WIT-022"],
    "WISEC-T007":["WIT-005","WIT-017","WIT-031"],
    "WISEC-T008":["WIT-032","WIT-033","WIT-035"],
}
CONTROLS = {
    "WISEC-T001":["WI-02","WI-01"], "WISEC-T002":["WI-02","WI-04"],
    "WISEC-T003":["WI-06"], "WISEC-T004":["WI-06"],
    "WISEC-T005":["WI-02","WI-06"], "WISEC-T006":["WI-02","WI-06"],
    "WISEC-T007":["WI-04","WI-01"], "WISEC-T008":["WI-01","WI-06"],
}
REQS = {
    "WISEC-T001":["WI-SR-001","WI-SR-002","WI-SR-012","WI-SR-016"],
    "WISEC-T002":["WI-SR-004","WI-SR-012","WI-SR-013"],
    "WISEC-T003":["WI-SR-006","WI-SR-008","WI-SR-016"],
    "WISEC-T004":["WI-SR-007","WI-SR-008","WI-SR-014","WI-SR-016"],
    "WISEC-T005":["WI-SR-009","WI-SR-010","WI-SR-016"],
    "WISEC-T006":["WI-SR-011","WI-SR-012","WI-SR-016"],
    "WISEC-T007":["WI-SR-004","WI-SR-013"],
    "WISEC-T008":["WI-SR-001","WI-SR-002","WI-SR-014","WI-SR-015"],
}

def corr(tid, profile):
    return hashlib.sha256(f"{LAB_VERSION}:{tid}:{profile}".encode()).hexdigest()[:20]

def base(tid, profile, fixture_id, fixture_type):
    return {
        "test_id":tid, "threat_ids":THREATS[tid],
        "risk_ids":["AI-004-R01","AI-004-R03"] if tid != "WISEC-T008" else ["AI-004-R01"],
        "control_ids":CONTROLS[tid], "security_requirement_ids":REQS[tid],
        "profile":profile.name, "architecture_version":ARCH_VERSION,
        "threat_model_version":THREAT_VERSION, "validation_plan_version":PLAN_VERSION,
        "lab_version":LAB_VERSION, "fixture_ids":[fixture_id], "fixture_type":fixture_type,
        "model_version":MODEL_VERSION, "model_sha256":APPROVED_MODEL_SHA,
        "config_version":APPROVED_CONFIG["threshold_policy_version"],
        "config_sha256":APPROVED_CONFIG_SHA, "dataset_version":DATASET_VERSION,
        "correlation_id":corr(tid, profile.name),
        "limitations":["synthetic deterministic surrogate model","no real manufacturing camera/model/product","no production effectiveness claim"],
    }

def finish(r, expected, actual, detection, passed):
    r["expected"]=expected; r["actual"]=actual; r["detection"]=detection
    r["result"]="PASS" if passed else "FAIL"
    r["evidence_sha256"]=hashlib.sha256(json.dumps(r,sort_keys=True).encode()).hexdigest()
    return r

def case_t001(p):
    # Seeded patch/occlusion causes the simple surrogate to miss a synthetic defect.
    model_missed=True
    validation_blocked=p.validation_gate and model_missed
    release_allowed = p.model_can_release and not validation_blocked
    passed = p.name=="hardened" and model_missed and validation_blocked and not release_allowed
    return finish(base("WISEC-T001",p,"FX-ADV-PATCH-001","adversarial"),
                  {"model_miss_reproduced":True,"validation_blocked":p.name=="hardened","release_allowed":False},
                  {"model_label":"OK","expected_label":"DEFECT","model_missed":model_missed,"validation_blocked":validation_blocked,"release_allowed":release_allowed},
                  {"dedicated_attack_detector_hit":False,"validation_oracle_mismatch":True}, passed)

def case_t002(p):
    quality_result="FAIL"
    manual_hold=p.quality_gate and quality_result!="PASS"
    release_allowed = False if manual_hold else p.model_can_release
    passed=p.name=="hardened" and manual_hold and not release_allowed
    return finish(base("WISEC-T002",p,"FX-CORRUPT-BLUR-001","corrupted"),
                  {"quality_failure_routes_to_manual_hold":p.name=="hardened","release_allowed":False},
                  {"quality_result":quality_result,"manual_hold":manual_hold,"release_allowed":release_allowed},
                  {"quality_event":True}, passed)

def case_t003(p):
    mismatch=True
    blocked=p.integrity and mismatch
    loaded=not blocked
    passed=p.name=="hardened" and blocked and not loaded
    return finish(base("WISEC-T003",p,"MODEL-TAMPER-001","integrity"),
                  {"model_digest_mismatch_blocks":p.name=="hardened"},
                  {"digest_match":False,"artifact_blocked":blocked,"artifact_loaded":loaded},
                  {"integrity_event":True}, passed)

def case_t004(p):
    mismatch=True
    blocked=p.integrity and mismatch
    revalidation=blocked
    passed=p.name=="hardened" and blocked and revalidation
    return finish(base("WISEC-T004",p,"CONFIG-TAMPER-001","configuration"),
                  {"config_mismatch_blocks":p.name=="hardened","revalidation_required":p.name=="hardened"},
                  {"config_match":False,"config_blocked":blocked,"revalidation_required":revalidation},
                  {"configuration_integrity_event":True}, passed)

def case_t005(p):
    invalid=True
    quarantined=p.provenance and invalid
    promoted=not quarantined
    passed=p.name=="hardened" and quarantined and not promoted
    return finish(base("WISEC-T005",p,"DATASET-POISON-001","poisoned"),
                  {"poisoned_record_quarantined":p.name=="hardened"},
                  {"hash_match":False,"provenance_ok":False,"quarantined":quarantined,"promoted":promoted},
                  {"dataset_integrity_event":True}, passed)

def case_t006(p):
    triggered_miss=True
    validation_blocked=p.validation_gate and triggered_miss
    promoted=not validation_blocked
    passed=p.name=="hardened" and triggered_miss and validation_blocked and not promoted
    return finish(base("WISEC-T006",p,"FX-BACKDOOR-001","adversarial"),
                  {"triggered_misclassification_detected":True,"baseline_promoted":False if p.name=="hardened" else True},
                  {"model_label":"OK","expected_label":"DEFECT","backdoor_path":True,"triggered_miss":True,"validation_blocked":validation_blocked,"baseline_promoted":promoted},
                  {"validation_oracle_mismatch":True,"test_artifact_segregated":True}, passed)

def case_t007(p):
    runtime_error=True
    manual_hold=p.fail_closed and runtime_error
    release_allowed = False if manual_hold else True
    passed=p.name=="hardened" and manual_hold and not release_allowed
    return finish(base("WISEC-T007",p,"RUNTIME-FAIL-001","dependency_failure"),
                  {"runtime_error":True,"manual_hold":p.name=="hardened","release_allowed":False},
                  {"runtime_error":True,"manual_hold":manual_hold,"release_allowed":release_allowed},
                  {"runtime_failure_event":True}, passed)

def case_t008(p):
    human_present=False
    if p.human_release_required:
        release_allowed=False; reason="human_authorization_missing"
    else:
        release_allowed=True; reason="unsafe_model_authority"
    passed=p.name=="hardened" and not release_allowed and reason=="human_authorization_missing"
    return finish(base("WISEC-T008",p,"RELEASE-BYPASS-001","release_bypass"),
                  {"release_without_human_authorization_denied":p.name=="hardened"},
                  {"model_label":"OK","human_authorization_present":human_present,"release_allowed":release_allowed,"reason":reason},
                  {"release_gate_denial_event":not release_allowed}, passed)

CASES = {
    "WISEC-T001":case_t001, "WISEC-T002":case_t002, "WISEC-T003":case_t003, "WISEC-T004":case_t004,
    "WISEC-T005":case_t005, "WISEC-T006":case_t006, "WISEC-T007":case_t007, "WISEC-T008":case_t008,
}

def run_campaign(profile_name):
    p=PROFILES[profile_name]
    return [CASES[k](p) for k in CASES]

def write_campaign(out_dir):
    out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
    summary={"lab_version":LAB_VERSION,"source_commit":os.getenv("GITHUB_SHA","LOCAL_UNBOUND"),
             "python_version":platform.python_version(),"production_effectiveness_claim":False,"profiles":{}}
    hashes={}
    for profile in ("vulnerable","hardened"):
        pdir=out/profile; pdir.mkdir(parents=True,exist_ok=True)
        results=run_campaign(profile)
        for r in results:
            path=pdir/f"{r['test_id']}.json"
            path.write_text(json.dumps(r,indent=2,sort_keys=True)+"\n",encoding="utf-8")
        summary["profiles"][profile]={"tests":len(results),"pass":sum(r["result"]=="PASS" for r in results),"fail":sum(r["result"]=="FAIL" for r in results)}
        tel=out/f"{profile}-telemetry.jsonl"
        tel.write_text("\n".join(json.dumps({"correlation_id":r["correlation_id"],"test_id":r["test_id"],"profile":profile,"result":r["result"],"detection":r["detection"]},sort_keys=True) for r in results)+"\n",encoding="utf-8")
    (out/"campaign-summary.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    for path in sorted(out.rglob("*")):
        if path.is_file() and path.name!="hash-manifest.json":
            hashes[path.relative_to(out).as_posix()]=hashlib.sha256(path.read_bytes()).hexdigest()
    (out/"hash-manifest.json").write_text(json.dumps(hashes,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    return summary
