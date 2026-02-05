from fastapi import APIRouter

from app.core.responses import not_implemented

router = APIRouter()


@router.get("/topics")
def list_topics():
    return not_implemented("Topic listing is not implemented.")


@router.post("/topics")
def create_topic():
    return not_implemented("Topic creation is not implemented.")


@router.get("/topics/{topic_id}")
def get_topic(topic_id: str):
    return not_implemented(f"Topic retrieval for {topic_id} is not implemented.")


@router.put("/topics/{topic_id}")
def update_topic(topic_id: str):
    return not_implemented(f"Topic update for {topic_id} is not implemented.")
