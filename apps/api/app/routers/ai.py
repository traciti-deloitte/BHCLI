from fastapi import APIRouter

from app.core.responses import not_implemented

router = APIRouter()


@router.post("/ai/claim_draft")
def draft_claim():
    return not_implemented("AI claim drafting is not implemented.")


@router.post("/ai/section_draft")
def draft_section():
    return not_implemented("AI section drafting is not implemented.")


@router.post("/ai/evidence_tag_suggest")
def suggest_evidence_tags():
    return not_implemented("AI evidence tagging is not implemented.")


@router.post("/ai/pii_scan")
def pii_scan():
    return not_implemented("AI PII scanning is not implemented.")


@router.get("/ai/jobs/{job_id}")
def get_ai_job(job_id: str):
    return not_implemented(f"AI job retrieval for {job_id} is not implemented.")
