from fastapi import APIRouter

from app.core.responses import not_implemented

router = APIRouter()


@router.post("/storyboards")
def create_storyboard():
    return not_implemented("Storyboard creation is not implemented.")


@router.get("/storyboards/{storyboard_id}")
def get_storyboard(storyboard_id: str):
    return not_implemented(f"Storyboard retrieval for {storyboard_id} is not implemented.")


@router.put("/storyboards/{storyboard_id}")
def update_storyboard(storyboard_id: str):
    return not_implemented(f"Storyboard update for {storyboard_id} is not implemented.")


@router.post("/storyboards/{storyboard_id}/claims/reorder")
def reorder_storyboard_claims(storyboard_id: str):
    return not_implemented(f"Storyboard claim reorder for {storyboard_id} is not implemented.")
