# MiniLM-L6-v2 OpenAI API Embedding Service

This project exposes the [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) model as a REST service similar to OpenAI's embedding API.

## Features
- REST API with FastAPI
- Embedding generation for single or multiple texts
- OpenAI-compatible `/v1/embeddings` endpoint

## Installation

### Local Installation

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Start the server:

```bash
python app.py
```

or

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

### Docker Installation (Recommended)

Build and run with Docker:

```bash
# Build the image
docker build -t embedding-service .

# Run the container
docker run -p 8000:8000 embedding-service
```

The Dockerfile uses multi-stage builds and CPU-only PyTorch for optimal size.

## API Usage

### /v1/embeddings [POST]

**Request Body:**
```json
{
  "model": "string",
  "input": "string" or ["string1", "string2", ...]
}
```

**ex:**
```json
{
  "model": "sentence-transformers/all-MiniLM-L6-v2",
  "input": ["Hello world", "Sample text"]
}
```

**Response:**
```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "embedding": [...],
      "index": 0
    },
    ...
  ],
  "model": "sentence-transformers/all-MiniLM-L6-v2",
  "usage": {
    "prompt_tokens": 5,
    "total_tokens": 5
  }
}
```

## Notes
- The model and tokenizer are loaded at startup.
- Packages in `requirements.txt` are required.

## License
MIT
