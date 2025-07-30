from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="PR Summarizer Microservice")

app.include_router(router)
