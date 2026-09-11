from __future__ import annotations
from dataclasses import dataclass
from .models import Identity
from .config import SecurityProfile
from .telemetry import Telemetry


@dataclass
class ToolDecision:
    tool: str
    decision: str
    executed: bool
    subject_id: str


class ToolGateway:
    def __init__(self, profile: SecurityProfile, telemetry: Telemetry) -> None:
        self.profile = profile
        self.telemetry = telemetry

    def request(self, identity: Identity, tool: str, test_id: str, correlation_id: str) -> ToolDecision:
        # No tool has real side effects. admin_export is synthetic and restricted.
        if self.profile.allow_model_tool_authority:
            allowed = True
            reason = "vulnerable_model_authority"
        else:
            allowed = tool == "read_public_status" and "employees" in identity.groups
            reason = "deterministic_user_policy" if allowed else "not_allowlisted_for_subject"

        decision = "ALLOW" if allowed else "DENY"
        self.telemetry.emit(
            "tool.authorization", test_id, correlation_id,
            subject_id=identity.subject_id, tool=tool, decision=decision, reason=reason,
        )
        if allowed:
            self.telemetry.emit(
                "tool.execution", test_id, correlation_id,
                subject_id=identity.subject_id, tool=tool, effect="synthetic_no_side_effect",
            )
        return ToolDecision(tool, decision, allowed, identity.subject_id)
