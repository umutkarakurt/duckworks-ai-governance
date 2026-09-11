from __future__ import annotations
import re
from dataclasses import dataclass
from .config import SecurityProfile
from .telemetry import Telemetry

REMOTE = re.compile(r"https?://[^\s)>'\"]+", re.I)


@dataclass
class RenderDecision:
    rendered: str
    remote_autoload: bool
    remote_targets: list[str]


class OutputRenderer:
    def __init__(self, profile: SecurityProfile, telemetry: Telemetry) -> None:
        self.profile = profile
        self.telemetry = telemetry

    def render(self, output: str, test_id: str, correlation_id: str) -> RenderDecision:
        targets = REMOTE.findall(output)
        if targets and self.profile.remote_resource_autoload:
            autoload = True
            rendered = output
            outcome = "remote_autoload_would_occur_in_vulnerable_fixture"
        elif targets:
            autoload = False
            rendered = REMOTE.sub("[REMOTE_CONTENT_BLOCKED]", output)
            outcome = "remote_content_blocked"
        else:
            autoload = False
            rendered = output
            outcome = "no_remote_content"

        self.telemetry.emit(
            "llm.request_policy", test_id, correlation_id,
            policy="output_renderer", outcome=outcome,
            remote_target_count=len(targets), remote_autoload=autoload,
        )
        return RenderDecision(rendered, autoload, targets)
