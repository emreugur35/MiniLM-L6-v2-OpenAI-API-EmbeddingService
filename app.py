from __future__ import annotations

import os
from fastapi import FastAPI, Request, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import uvicorn
import tiktoken
from typing import Union, List

app = FastAPI()
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
tokenizer = tiktoken.get_encoding("cl100k_base")

# Security scheme for API key validation
security = HTTPBearer()

# Get API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def validate_api_key(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Validate the provided API key against the expected OpenAI API key"""
    if not OPENAI_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="API key not configured on server"
        )
    
    if credentials.credentials != OPENAI_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )

class EmbeddingRequest(BaseModel):
    model: str
    input: Union[str, List[str]]

@app.get("/health")
def health_check():
    """Health check endpoint for monitoring service availability"""
    return {
        "status": "healthy",
        "service": "embedding-service",
        "model": "sentence-transformers/all-MiniLM-L6-v2"
    }

@app.post("/v1/embeddings")
def create_embedding(request: EmbeddingRequest, api_key: HTTPAuthorizationCredentials = Depends(validate_api_key)):
    inputs = request.input if isinstance(request.input, list) else [request.input]
    embeddings = model.encode(inputs).tolist()

    data = []
    for i, emb in enumerate(embeddings):
        data.append({
            "object": "embedding",
            "embedding": emb,
            "index": i
        })

    token_count = sum(len(tokenizer.encode(i)) for i in inputs)

    return {
        "object": "list",
        "data": data,
        "model": "sentence-transformers/all-MiniLM-L6-v2",
        "usage": {
            "prompt_tokens": token_count,
            "total_tokens": token_count
        }
    }

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)