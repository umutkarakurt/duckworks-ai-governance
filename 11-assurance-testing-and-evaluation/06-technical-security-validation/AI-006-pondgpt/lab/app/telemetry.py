from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any


@dataclass
class Event:
    timestamp: str
    event_family: str
    security_test_id: str
    correlation_id: str
    details: dict[str, Any]


class Telemetry:
    def __init__(self) -> None:
        self.events: list[Event] = []

    def emit(self, family: str, test_id: str, correlation_id: str, **details: Any) -> None:
        # Deliberately log metadata/decisions, not raw prompt/document bodies.
        self.events.append(Event(
            timestamp=datetime.now(timezone.utc).isoformat(),
            event_family=family,
            security_test_id=test_id,
            correlation_id=correlation_id,
            details=details,
        ))

    def as_dicts(self) -> list[dict[str, Any]]:
        return [asdict(e) for e in self.events]

    def has_family(self, family: str, test_id: str) -> bool:
        return any(e.event_family == family and e.security_test_id == test_id for e in self.events)
