from pydantic import BaseModel, Field

class SummaryRequest(BaseModel):
    description: str = Field(..., min_length=1, description="Text to summarize")

class SummaryResponse(BaseModel):
    summary: str
    cached: bool = Field(..., description="Indicates if the response was returned from cache")
