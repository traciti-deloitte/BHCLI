from fastapi import APIRouter

from app.core.responses import not_implemented

router = APIRouter()


@router.get("/people")
def list_people():
    return not_implemented("People listing is not implemented.")


@router.post("/people")
def create_person():
    return not_implemented("Person creation is not implemented.")


@router.get("/people/{person_id}")
def get_person(person_id: str):
    return not_implemented(f"Person retrieval for {person_id} is not implemented.")


@router.put("/people/{person_id}")
def update_person(person_id: str):
    return not_implemented(f"Person update for {person_id} is not implemented.")
