from __future__ import annotations
from dataclasses import dataclass, asdict
from hashlib import sha256
import json
from typing import Any


def canonical_hash(payload: dict[str, Any]) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return sha256(raw).hexdigest()


@dataclass(frozen=True)
class Identity:
    subject_id: str
    groups: tuple[str, ...]


@dataclass(frozen=True)
class Document:
    document_id: str
    classification: str
    allowed_groups: tuple[str, ...]
    content: str
    contributor: str
    version: str
    approved: bool = True

    def envelope(self) -> dict[str, Any]:
        return {
            "document_id": self.document_id,
            "classification": self.classification,
            "allowed_groups": list(self.allowed_groups),
            "content": self.content,
            "contributor": self.contributor,
            "version": self.version,
            "approved": self.approved,
        }

    @property
    def envelope_hash(self) -> str:
        return canonical_hash(self.envelope())


@dataclass
class TestResult:
    test_id: str
    profile: str
    result: str
    threat_ids: list[str]
    control_ids: list[str]
    requirement_ids: list[str]
    actor: str
    expected: dict[str, Any]
    actual: dict[str, Any]
    detection: dict[str, Any]
    evidence: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
