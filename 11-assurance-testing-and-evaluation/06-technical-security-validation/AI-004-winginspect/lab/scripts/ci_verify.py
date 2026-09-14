from pathlib import Path
import json, os
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'evidence'/'generated'
load=lambda p: json.loads((OUT/p).read_text())
s=load('campaign-summary.json')
assert s['production_effectiveness_claim'] is False
assert s['profiles']['vulnerable']=={'tests':8,'pass':0,'fail':8}
assert s['profiles']['hardened']=={'tests':8,'pass':8,'fail':0}
if os.getenv('GITHUB_SHA'): assert s['source_commit']==os.environ['GITHUB_SHA']
t1=load('hardened/WISEC-T001.json'); assert t1['actual']['model_missed'] and t1['actual']['validation_blocked'] and not t1['actual']['release_allowed'] and not t1['detection']['dedicated_attack_detector_hit']
t7=load('hardened/WISEC-T007.json'); assert t7['actual']['runtime_error'] and t7['actual']['manual_hold'] and not t7['actual']['release_allowed']
t8=load('hardened/WISEC-T008.json'); assert not t8['actual']['human_authorization_present'] and not t8['actual']['release_allowed'] and t8['actual']['reason']=='human_authorization_missing'
text='PASS\nvulnerable=8/8 seeded unsafe outcomes reproduced\nhardened=8/8 control assertions passed\nproduction_effectiveness_claim=false\n'
(OUT/'ci-verification.txt').write_text(text)
print(text,end='')
