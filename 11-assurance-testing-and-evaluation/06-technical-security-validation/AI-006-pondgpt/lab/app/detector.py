from __future__ import annotations
import re
import unicodedata


def basic_injection_detector(text: str) -> bool:
    # Deliberately imperfect. Detection is not a security boundary.
    normalized = unicodedata.normalize("NFKC", text).lower()
    patterns = [
        r"ignore\s+(all\s+)?previous",
        r"attack_request\s*:",
        r"tool_request\s*:",
        r"reveal\s+restricted",
    ]
    return any(re.search(p, normalized) for p in patterns)
