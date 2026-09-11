from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class SecurityProfile:
    name: str
    authorize_before_context: bool
    fail_open_on_pep_error: bool
    trust_staged_metadata: bool
    follow_retrieved_instructions: bool
    allow_model_tool_authority: bool
    remote_resource_autoload: bool
    expose_secret_to_model: bool
    quarantine_unapproved_poison: bool


VULNERABLE = SecurityProfile(
    name="vulnerable",
    authorize_before_context=False,
    fail_open_on_pep_error=True,
    trust_staged_metadata=True,
    follow_retrieved_instructions=True,
    allow_model_tool_authority=True,
    remote_resource_autoload=True,
    expose_secret_to_model=True,
    quarantine_unapproved_poison=False,
)

HARDENED = SecurityProfile(
    name="hardened",
    authorize_before_context=True,
    fail_open_on_pep_error=False,
    trust_staged_metadata=False,
    follow_retrieved_instructions=False,
    allow_model_tool_authority=False,
    remote_resource_autoload=False,
    expose_secret_to_model=False,
    quarantine_unapproved_poison=True,
)

PROFILES = {"vulnerable": VULNERABLE, "hardened": HARDENED}
