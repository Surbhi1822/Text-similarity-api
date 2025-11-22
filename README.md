# Text Similarity API + UI

A simple FastAPI backend + a small HTML frontend to compute:

- Text similarity using cosine similarity
- Text embeddings using SentenceTransformers

### Endpoints
1. `/similarity` → similarity score  
2. `/embedding` → embedding preview  

---

Frontend is a tiny HTML page where users can input text and see similarity instantly.

This was built out of curiosity to understand embeddings & vector reasoning.

Tech Used:
- FastAPI
- Uvicorn
- HuggingFace SentenceTransformers
- HTML + JS frontend
