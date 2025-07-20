# MiniLM-L6-v2 OpenAI API Embedding Service

This project exposes the [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) model as a REST service similar to OpenAI's embedding API.

## Features
- REST API with FastAPI
- Embedding generation for single or multiple texts
- OpenAI-compatible `/v1/embeddings` endpoint

## Installation

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

## API Usage

### /v1/embeddings [POST]

**Request Body:**
```json
{
  "model": "string",
  "input": "string" veya ["string1", "string2", ...]
}
```

**Örnek:**
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
