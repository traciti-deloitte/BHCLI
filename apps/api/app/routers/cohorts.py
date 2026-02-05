from fastapi import APIRouter

from app.core.responses import not_implemented

router = APIRouter()


@router.get("/cohorts")
def list_cohorts():
    return not_implemented("Cohort listing is not implemented.")


@router.post("/cohorts")
def create_cohort():
    return not_implemented("Cohort creation is not implemented.")


@router.get("/cohorts/{cohort_id}")
def get_cohort(cohort_id: str):
    return not_implemented(f"Cohort retrieval for {cohort_id} is not implemented.")


@router.put("/cohorts/{cohort_id}")
def update_cohort(cohort_id: str):
    return not_implemented(f"Cohort update for {cohort_id} is not implemented.")
