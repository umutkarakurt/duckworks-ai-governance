from pathlib import Path
import sys, json
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from app.winginspect_lab import write_campaign
summary=write_campaign(ROOT/'evidence'/'generated')
print(json.dumps(summary,indent=2,sort_keys=True))
