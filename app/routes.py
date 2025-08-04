from fastapi import APIRouter, Request, HTTPException
from app.schemas import SummaryRequest, SummaryResponse
from .utils.cache import get_cached_summary, set_cached_summary
from app.summarizer import summarize_text
from slowapi.errors import RateLimitExceeded
from slowapi.extension import Limiter
from slowapi.util import get_remote_address
from app.utils.rate_limiter import limiter
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/summarize", response_model=SummaryResponse)
@limiter.limit("5/minute")
def summarize(req: SummaryRequest, request: Request):
    try:
        text = req.description

        cached = get_cached_summary(text)
        if cached:
            print("Cached Response...")
            return {"summary": cached, "cached": True}

        summary = summarize_text(text)
        set_cached_summary(text, summary)
        return SummaryResponse(summary=summary, cached=False)

    except Exception as e:
        logger.error(f"Summarization error: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to summarize the input text.")

@router.get("/health")
def read_router():
    return {"msg": "Welcome to the summarizer"}
