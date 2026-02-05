from fastapi import APIRouter

from app.core.responses import not_implemented

router = APIRouter()


@router.get("/me")
def get_me():
    return not_implemented("User profile retrieval is not implemented.")


@router.get("/users")
def list_users():
    return not_implemented("User listing is not implemented.")


@router.post("/users/invite")
def invite_user():
    return not_implemented("User invitations are not implemented.")


@router.get("/roles")
def list_roles():
    return not_implemented("Role listing is not implemented.")


@router.put("/users/{user_id}/roles")
def update_user_roles(user_id: str):
    return not_implemented(f"Role updates for user {user_id} are not implemented.")
