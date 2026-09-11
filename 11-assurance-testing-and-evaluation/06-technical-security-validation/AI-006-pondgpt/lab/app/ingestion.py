from __future__ import annotations
from dataclasses import dataclass
from .models import Document
from .config import SecurityProfile
from .telemetry import Telemetry


@dataclass
class PublishResult:
    published: bool
    quarantined: bool
    reason: str
    source_hash: str | None
    staged_hash: str


class IngestionService:
    def __init__(self, profile: SecurityProfile, telemetry: Telemetry, source_truth: dict[str, Document], index: dict[str, Document]) -> None:
        self.profile = profile
        self.telemetry = telemetry
        self.source_truth = source_truth
        self.index = index

    def publish(self, document: Document, test_id: str, correlation_id: str) -> PublishResult:
        source = self.source_truth.get(document.document_id)
        source_hash = source.envelope_hash if source else None
        staged_hash = document.envelope_hash

        self.telemetry.emit(
            "ingestion.source_validation", test_id, correlation_id,
            document_id=document.document_id,
            contributor=document.contributor,
            version=document.version,
            approved=document.approved,
            source_truth_present=source is not None,
        )

        if self.profile.trust_staged_metadata:
            self.index[document.document_id] = document
            self.telemetry.emit(
                "ingestion.integrity", test_id, correlation_id,
                document_id=document.document_id,
                outcome="published_without_source_truth_validation",
                source_hash=source_hash,
                staged_hash=staged_hash,
            )
            return PublishResult(True, False, "vulnerable_trust_staged_metadata", source_hash, staged_hash)

        if source is not None and source_hash != staged_hash:
            self.telemetry.emit(
                "ingestion.integrity", test_id, correlation_id,
                document_id=document.document_id,
                outcome="rejected_hash_or_metadata_mismatch",
                source_hash=source_hash,
                staged_hash=staged_hash,
            )
            return PublishResult(False, True, "source_truth_mismatch", source_hash, staged_hash)

        if source is None and (not document.approved or self.profile.quarantine_unapproved_poison):
            self.telemetry.emit(
                "ingestion.integrity", test_id, correlation_id,
                document_id=document.document_id,
                outcome="quarantined_pending_approval",
                source_hash=None,
                staged_hash=staged_hash,
            )
            return PublishResult(False, True, "new_document_requires_approval", None, staged_hash)

        self.index[document.document_id] = document
        self.telemetry.emit(
            "ingestion.integrity", test_id, correlation_id,
            document_id=document.document_id,
            outcome="published",
            source_hash=source_hash,
            staged_hash=staged_hash,
        )
        return PublishResult(True, False, "validated", source_hash, staged_hash)
