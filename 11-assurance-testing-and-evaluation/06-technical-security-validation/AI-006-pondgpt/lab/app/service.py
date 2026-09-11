from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable
from .authz import AuthorizationPEP
from .config import SecurityProfile
from .detector import basic_injection_detector
from .fixtures import IDENTITIES, SECRET_CANARY, fresh_source_truth
from .ingestion import IngestionService
from .model_stub import infer_untrusted_intent
from .models import Document
from .renderer import OutputRenderer
from .telemetry import Telemetry
from .tool_gateway import ToolGateway


@dataclass
class QueryObservation:
    actor: str
    requested_ids: list[str]
    context_ids: list[str]
    context_classifications: list[str]
    provider_context_ids: list[str]
    provider_payload: str
    unauthorized_tool_actions: int
    tool_decisions: list[dict]
    remote_autoload: bool
    detector_hit: bool
    authz_statuses: list[str]
    response: str


class PondGPTLab:
    def __init__(self, profile: SecurityProfile) -> None:
        self.profile = profile
        self.telemetry = Telemetry()
        self.source_truth = fresh_source_truth()
        self.index: dict[str, Document] = dict(self.source_truth)
        self.pep = AuthorizationPEP(profile, self.telemetry)
        self.ingestion = IngestionService(profile, self.telemetry, self.source_truth, self.index)
        self.tool_gateway = ToolGateway(profile, self.telemetry)
        self.renderer = OutputRenderer(profile, self.telemetry)

    def _candidate_retrieval(
        self,
        actor: str,
        document_ids: Iterable[str],
        test_id: str,
        correlation_id: str,
    ) -> tuple[list[Document], list[str]]:
        identity = IDENTITIES[actor]
        returned: list[Document] = []
        statuses: list[str] = []

        for document_id in document_ids:
            doc = self.index.get(document_id)
            if not doc:
                continue

            self.telemetry.emit(
                "retrieval.query", test_id, correlation_id,
                subject_id=actor, document_id=document_id,
            )

            if self.profile.authorize_before_context:
                decision = self.pep.decide(identity, doc, test_id, correlation_id)
                statuses.append(decision.status)
                if not decision.allowed:
                    continue
                returned.append(doc)
                self.telemetry.emit(
                    "retrieval.chunk_return", test_id, correlation_id,
                    document_id=doc.document_id, classification=doc.classification,
                )
            else:
                # Deliberately weak order: candidate content is placed into context
                # before the authorization result is applied.
                returned.append(doc)
                self.telemetry.emit(
                    "retrieval.chunk_return", test_id, correlation_id,
                    document_id=doc.document_id, classification=doc.classification,
                    note="vulnerable_pre_authorization_return",
                )
                decision = self.pep.decide(identity, doc, test_id, correlation_id)
                statuses.append(decision.status)

        return returned, statuses

    def query(
        self,
        actor: str,
        prompt: str,
        requested_ids: list[str],
        test_id: str,
        correlation_id: str,
        pep_available: bool = True,
    ) -> QueryObservation:
        identity = IDENTITIES[actor]
        self.pep.available = pep_available

        self.telemetry.emit(
            "auth.token_validation", test_id, correlation_id,
            subject_id=actor, token_status="valid_synthetic",
            groups=list(identity.groups),
        )

        detector_hit = basic_injection_detector(prompt)
        self.telemetry.emit(
            "llm.security_detection", test_id, correlation_id,
            detector="basic-fixture-detector-v1", detected=detector_hit,
        )

        context, statuses = self._candidate_retrieval(actor, requested_ids, test_id, correlation_id)

        intent = infer_untrusted_intent(prompt, context)
        if self.profile.follow_retrieved_instructions and intent.secondary_document_ids:
            secondary, secondary_statuses = self._candidate_retrieval(
                actor, intent.secondary_document_ids, test_id, correlation_id
            )
            existing = {d.document_id for d in context}
            context.extend(d for d in secondary if d.document_id not in existing)
            statuses.extend(secondary_statuses)

        tool_decisions = []
        for tool in intent.requested_tools:
            td = self.tool_gateway.request(identity, tool, test_id, correlation_id)
            tool_decisions.append({
                "tool": td.tool,
                "decision": td.decision,
                "executed": td.executed,
                "subject_id": td.subject_id,
            })

        provider_parts = [f"PROMPT={prompt}"]
        provider_parts.extend(f"DOC={d.document_id}|CLASS={d.classification}|CONTENT={d.content}" for d in context)
        if self.profile.expose_secret_to_model:
            provider_parts.append(f"SYSTEM_SECRET={SECRET_CANARY}")
        provider_payload = "\n".join(provider_parts)

        self.telemetry.emit(
            "llm.request_policy", test_id, correlation_id,
            policy="provider_boundary",
            outbound_document_ids=[d.document_id for d in context],
            outbound_classifications=[d.classification for d in context],
            secret_tagged_value_count=1 if self.profile.expose_secret_to_model else 0,
        )

        render = self.renderer.render(intent.output, test_id, correlation_id)

        return QueryObservation(
            actor=actor,
            requested_ids=list(requested_ids),
            context_ids=[d.document_id for d in context],
            context_classifications=[d.classification for d in context],
            provider_context_ids=[d.document_id for d in context],
            provider_payload=provider_payload,
            unauthorized_tool_actions=sum(1 for t in tool_decisions if t["executed"] and t["tool"] != "read_public_status"),
            tool_decisions=tool_decisions,
            remote_autoload=render.remote_autoload,
            detector_hit=detector_hit,
            authz_statuses=statuses,
            response=render.rendered,
        )
