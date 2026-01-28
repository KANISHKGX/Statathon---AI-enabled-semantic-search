from fastapi import APIRouter
from app.models.schemas import QueryRequest
from app.services.search_service import search

router = APIRouter()

@router.post("/search")
def search_job(req: QueryRequest):
    return search(req.query)
