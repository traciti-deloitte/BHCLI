from fastapi import APIRouter

from app.core.responses import not_implemented

router = APIRouter()


@router.get("/cities")
def list_cities():
    return not_implemented("City listing is not implemented.")


@router.post("/cities")
def create_city():
    return not_implemented("City creation is not implemented.")


@router.get("/cities/{city_id}")
def get_city(city_id: str):
    return not_implemented(f"City retrieval for {city_id} is not implemented.")


@router.put("/cities/{city_id}")
def update_city(city_id: str):
    return not_implemented(f"City update for {city_id} is not implemented.")
