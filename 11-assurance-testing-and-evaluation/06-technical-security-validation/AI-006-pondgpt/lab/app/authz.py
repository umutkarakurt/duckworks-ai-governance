from __future__ import annotations
from dataclasses import dataclass
from .models import Identity, Document
from .config import SecurityProfile
from .telemetry import Telemetry


@dataclass
class AuthzDecision:
    status: str
    allowed: bool
    reason: str


class AuthorizationPEP:
    def __init__(self, profile: SecurityProfile, telemetry: Telemetry) -> None:
        self.profile = profile
        self.telemetry = telemetry
        self.available = True

    def decide(self, identity: Identity, document: Document, test_id: str, correlation_id: str) -> AuthzDecision:
        if not self.available:
            allowed = self.profile.fail_open_on_pep_error
            status = "ALLOW" if allowed else "ERROR_DENY"
            reason = "pep_unavailable_fail_open" if allowed else "pep_unavailable_fail_closed"
        else:
            allowed = bool(set(identity.groups).intersection(document.allowed_groups)) or document.classification == "PUBLIC"
            status = "ALLOW" if allowed else "DENY"
            reason = "group_match" if allowed else "no_required_group"

        self.telemetry.emit(
            "retrieval.authorization", test_id, correlation_id,
            subject_id=identity.subject_id,
            document_id=document.document_id,
            classification=document.classification,
            decision=status,
            reason=reason,
        )
        return AuthzDecision(status, allowed, reason)
