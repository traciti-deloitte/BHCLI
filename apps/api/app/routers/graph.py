from fastapi import APIRouter

from app.core.responses import not_implemented

router = APIRouter()


@router.get("/graph/query_templates")
def list_query_templates():
    return not_implemented("Graph query templates are not implemented.")


@router.post("/graph/query")
def run_query():
    return not_implemented("Graph queries are not implemented.")


@router.get("/graph/saved_queries")
def list_saved_queries():
    return not_implemented("Saved graph queries are not implemented.")


@router.post("/graph/saved_queries")
def save_query():
    return not_implemented("Saving graph queries is not implemented.")
