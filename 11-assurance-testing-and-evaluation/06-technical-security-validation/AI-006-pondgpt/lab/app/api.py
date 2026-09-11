from __future__ import annotations
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from .config import PROFILES
from .service import PondGPTLab


class QueryRequest(BaseModel):
    actor: str = "user.general01"
    prompt: str
    requested_ids: list[str] = Field(default_factory=list)
    security_test_id: str = "MANUAL-LAB"
    correlation_id: str = "corr-manual-lab"
    pep_available: bool = True


def create_app(profile_name: str = "hardened") -> FastAPI:
    if profile_name not in PROFILES:
        raise ValueError(f"Unknown profile: {profile_name}")
    lab = PondGPTLab(PROFILES[profile_name])
    app = FastAPI(title=f"PondGPT synthetic security lab ({profile_name})", version="0.1.0")

    @app.get("/health")
    def health() -> dict:
        return {"status": "ok", "profile": profile_name, "synthetic": True}

    @app.post("/query")
    def query(req: QueryRequest) -> dict:
        try:
            obs = lab.query(
                req.actor, req.prompt, req.requested_ids,
                req.security_test_id, req.correlation_id, req.pep_available,
            )
        except KeyError as exc:
            raise HTTPException(status_code=400, detail=f"Unknown synthetic actor: {exc}") from exc
        return {
            "actor": obs.actor,
            "context_ids": obs.context_ids,
            "context_classifications": obs.context_classifications,
            "tool_decisions": obs.tool_decisions,
            "remote_autoload": obs.remote_autoload,
            "detector_hit": obs.detector_hit,
            "response": obs.response,
        }

    return app


app = create_app("hardened")
