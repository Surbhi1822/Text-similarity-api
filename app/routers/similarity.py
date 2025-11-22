import requests
import numpy as np
from fastapi import APIRouter
from app.models.schemas import TextPair
from app.core.config import settings

router = APIRouter(prefix="/similarity")

HF_API_URL = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

headers = {"Authorization": f"Bearer {settings.HF_API_KEY}"}

def get_embedding(text: str):
    response = requests.post(HF_API_URL, headers=headers, json={"inputs": text})
    return response.json()

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

@router.post("")
def compute_similarity(texts: TextPair):
    emb1 = get_embedding(texts.text1)
    emb2 = get_embedding(texts.text2)
    score = cosine_similarity(emb1, emb2)
    return {"similarity": score}
