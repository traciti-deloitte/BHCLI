from fastapi import APIRouter

from app.core.responses import not_implemented

router = APIRouter()


@router.post("/dashboards")
def create_dashboard():
    return not_implemented("Dashboard creation is not implemented.")


@router.get("/dashboards/{dashboard_id}")
def get_dashboard(dashboard_id: str):
    return not_implemented(f"Dashboard retrieval for {dashboard_id} is not implemented.")


@router.put("/dashboards/{dashboard_id}")
def update_dashboard(dashboard_id: str):
    return not_implemented(f"Dashboard update for {dashboard_id} is not implemented.")
