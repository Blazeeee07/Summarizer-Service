from fastapi import APIRouter
from app.schemas import SummaryRequest, SummaryResponse
from app.summarizer import summarize_text

router = APIRouter()

@router.post("/summarize", response_model=SummaryResponse)
def summarize(req: SummaryRequest):
    summary = summarize_text(req.description)
    return SummaryResponse(summary=summary)

@router.get("/health")
def read_router():
    return {"msg":"Welcome to the summarizer"}