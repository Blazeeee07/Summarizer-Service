from pydantic import BaseModel, Field

class SummaryRequest(BaseModel):
    description: str = Field(..., min_length=1, description="Text to summarize")

class SummaryResponse(BaseModel):
    summary: str
