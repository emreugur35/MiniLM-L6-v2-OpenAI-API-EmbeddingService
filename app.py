from __future__ import annotations


from fastapi import FastAPI, Request
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import uvicorn
import tiktoken
from typing import Union, List

app = FastAPI()
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
tokenizer = tiktoken.get_encoding("cl100k_base")

class EmbeddingRequest(BaseModel):
    model: str
    input: Union[str, List[str]]

@app.post("/v1/embeddings")
def create_embedding(request: EmbeddingRequest):
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