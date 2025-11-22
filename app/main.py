from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import similarity
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # <-- this fixes your problem
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(similarity.router)

@app.get("/")
def home():
    return {"message": "Text Similarity API is running!"}
