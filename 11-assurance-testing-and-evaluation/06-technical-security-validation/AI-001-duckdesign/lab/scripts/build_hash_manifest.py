from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
E = ROOT / "evidence" / "generated"

entries = []
for p in sorted(E.rglob("*")):
    if p.is_file() and p.name != "hash-manifest.json":
        entries.append({
            "path": p.relative_to(E).as_posix(),
            "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
        })

(E / "hash-manifest.json").write_text(
    json.dumps({"files": entries}, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)
print(f"hash-manifest={len(entries)} files")
