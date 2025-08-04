from fastapi import APIRouter, Request
from app.schemas import SummaryRequest, SummaryResponse
from .utils.cache import get_cached_summary, set_cached_summary
from app.summarizer import summarize_text
from slowapi.errors import RateLimitExceeded
from slowapi.extension import Limiter
from slowapi.util import get_remote_address
from app.utils.rate_limiter import limiter

router = APIRouter()

@router.post("/summarize", response_model=SummaryResponse)
@limiter.limit("5/minute")
def summarize(req: SummaryRequest, request: Request):
    text=req.description

    cached =get_cached_summary(text)
    if cached:
        print("Cached Response...")
        return {"summary": cached, "cached":True}

    summary = summarize_text(req.description)
    set_cached_summary(text,summary)
    return SummaryResponse(summary=summary, cached=False)

@router.get("/health")
def read_router():
    return {"msg":"Welcome to the summarizer"}