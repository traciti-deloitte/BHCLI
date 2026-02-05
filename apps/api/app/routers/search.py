from fastapi import APIRouter

from app.core.responses import not_implemented

router = APIRouter()


@router.get("/search")
def search():
    return not_implemented("Search is not implemented.")
