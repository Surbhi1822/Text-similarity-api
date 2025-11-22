from fastapi import APIRouter
from app.models.schemas import TextPair
from sentence_transformers import SentenceTransformer, util
from app.core.config import settings
from app.utils.logging_config import setup_logging

router = APIRouter()
logger = setup_logging()

model = SentenceTransformer(settings.EMBEDDING_MODEL)

@router.post("/similarity")
def get_similarity(data: TextPair):
    logger.info(f"Calculating similarity between '{data.text1}' and '{data.text2}'")
    
    emb1 = model.encode(data.text1)
    emb2 = model.encode(data.text2)
    score = float(util.cos_sim(emb1, emb2))
    
    logger.info(f"Similarity score: {score}")
    
    return {"similarity": score}
