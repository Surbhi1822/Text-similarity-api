from fastapi import APIRouter
from app.models.schemas import SingleText
from sentence_transformers import SentenceTransformer
from app.core.config import settings
from app.utils.logging_config import setup_logging

router = APIRouter()
logger = setup_logging()

model = SentenceTransformer(settings.EMBEDDING_MODEL)

@router.post("/embedding")
def get_embedding(data: SingleText):
    logger.info(f"Generating embedding for '{data.text[:30]}'...")

    vector = model.encode(data.text)
    
    return {
        "vector_dimension": len(vector),
        "sample_values": vector[:10].tolist()
    }
