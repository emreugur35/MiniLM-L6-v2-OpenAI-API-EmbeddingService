# MiniLM-L6-v2 OpenAI API Embedding Service

This project exposes the [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) model as a REST service similar to OpenAI's embedding API.

## Features
- REST API with FastAPI
- Embedding generation for single or multiple texts
- OpenAI-compatible `/v1/embeddings` endpoint
- API key authentication for secure access

## Installation

### Local Installation

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Set your API key as an environment variable:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

3. Start the server:

```bash
python app.py
```

or

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

### Docker Installation (Recommended)

#### Option 1: Using docker run

Build and run with Docker:

```bash
# Build the image
docker build -t embedding-service .

# Run the container with API key
docker run -p 8000:8000 -e OPENAI_API_KEY="your-api-key-here" embedding-service
```

or directly from docker hub with:

```bash
docker run -d -p 8000:8000 -e OPENAI_API_KEY="test-api-key-123" --name embedding-service emreugur/embedding-service:latest

```

#### Option 2: Using docker-compose

1. Copy the example environment file:

```bash
cp .env.example .env
```

2. Edit `.env` file and set your API key:

```env
OPENAI_API_KEY=your-actual-api-key-here
```

3. Run with docker-compose:

```bash
docker-compose up -d

```


The Dockerfile uses multi-stage builds and CPU-only PyTorch for optimal size.

## API Usage

### Authentication

All API requests require authentication using a Bearer token. Include your API key in the Authorization header:

```bash
curl -X POST "http://localhost:8000/v1/embeddings" \
  -H "Authorization: Bearer your-api-key-here" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sentence-transformers/all-MiniLM-L6-v2",
    "input": ["Hello world", "Sample text"]
  }'
```

### /v1/embeddings [POST]

**Request Headers:**

```http
Authorization: Bearer your-api-key-here
Content-Type: application/json
```

**Request Body:**

```json
{
  "model": "string",
  "input": "string" or ["string1", "string2", ...]
}
```

**Example:**

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

- The model and tokenizer are loaded at startup
- API key authentication is required for all requests
- Packages in `requirements.txt` are required

## License

MIT
