from fastapi import APIRouter

from app.core.responses import not_implemented

router = APIRouter()


@router.post("/evidence/upload")
def upload_evidence():
    return not_implemented("Evidence upload is not implemented.")


@router.get("/evidence")
def list_evidence():
    return not_implemented("Evidence listing is not implemented.")


@router.get("/evidence/{evidence_id}")
def get_evidence(evidence_id: str):
    return not_implemented(f"Evidence retrieval for {evidence_id} is not implemented.")


@router.put("/evidence/{evidence_id}")
def update_evidence(evidence_id: str):
    return not_implemented(f"Evidence update for {evidence_id} is not implemented.")


@router.post("/evidence/{evidence_id}/excerpts")
def create_excerpt(evidence_id: str):
    return not_implemented(f"Excerpt creation for {evidence_id} is not implemented.")


@router.get("/evidence/{evidence_id}/excerpts")
def list_excerpts(evidence_id: str):
    return not_implemented(f"Excerpt listing for {evidence_id} is not implemented.")


@router.post("/evidence/{evidence_id}/process")
def process_evidence(evidence_id: str):
    return not_implemented(f"Re-processing for {evidence_id} is not implemented.")


@router.post("/evidence/bulk_import")
def bulk_import_evidence():
    return not_implemented("Evidence bulk import is not implemented.")
