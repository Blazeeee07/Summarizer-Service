from transformers import pipeline
from fastapi import HTTPException

MIN_SUMMARY_LENGTH = 60

summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=0)


def summarize_text(text: str) -> str:
    if len(text.strip()) < MIN_SUMMARY_LENGTH:
        raise HTTPException(status_code=400, detail="Description too short to summarize (minimum 60 characters).")

    result = summarizer(text, max_length=60, min_length=20, do_sample=False)
    return result[0]['summary_text']
