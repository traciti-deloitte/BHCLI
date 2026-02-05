from fastapi import APIRouter

from app.core.responses import not_implemented

router = APIRouter()


@router.post("/claims")
def create_claim():
    return not_implemented("Claim creation is not implemented.")


@router.get("/claims")
def list_claims():
    return not_implemented("Claim listing is not implemented.")


@router.get("/claims/{claim_id}")
def get_claim(claim_id: str):
    return not_implemented(f"Claim retrieval for {claim_id} is not implemented.")


@router.put("/claims/{claim_id}")
def update_claim(claim_id: str):
    return not_implemented(f"Claim update for {claim_id} is not implemented.")


@router.post("/claims/{claim_id}/link_evidence")
def link_claim_evidence(claim_id: str):
    return not_implemented(f"Claim evidence linking for {claim_id} is not implemented.")
