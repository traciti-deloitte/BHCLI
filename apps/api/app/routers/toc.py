from fastapi import APIRouter

from app.core.responses import not_implemented

router = APIRouter()


@router.post("/toc")
def create_toc():
    return not_implemented("ToC creation is not implemented.")


@router.get("/toc/{toc_id}")
def get_toc(toc_id: str):
    return not_implemented(f"ToC retrieval for {toc_id} is not implemented.")


@router.post("/toc/{toc_id}/version")
def create_toc_version(toc_id: str):
    return not_implemented(f"ToC versioning for {toc_id} is not implemented.")


@router.post("/toc/{toc_id}/nodes")
def create_toc_node(toc_id: str):
    return not_implemented(f"ToC node creation for {toc_id} is not implemented.")


@router.put("/toc/nodes/{node_id}")
def update_toc_node(node_id: str):
    return not_implemented(f"ToC node update for {node_id} is not implemented.")


@router.post("/toc/{toc_id}/edges")
def create_toc_edge(toc_id: str):
    return not_implemented(f"ToC edge creation for {toc_id} is not implemented.")


@router.delete("/toc/edges/{edge_id}")
def delete_toc_edge(edge_id: str):
    return not_implemented(f"ToC edge deletion for {edge_id} is not implemented.")


@router.post("/toc/nodes/{node_id}/link_evidence")
def link_toc_evidence(node_id: str):
    return not_implemented(f"ToC evidence linking for {node_id} is not implemented.")
