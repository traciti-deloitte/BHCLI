from fastapi import APIRouter

from app.core.responses import not_implemented

router = APIRouter()


@router.post("/analysis_runs")
def create_analysis_run():
    return not_implemented("Analysis run creation is not implemented.")


@router.get("/analysis_runs")
def list_analysis_runs():
    return not_implemented("Analysis run listing is not implemented.")
