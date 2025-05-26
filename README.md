# fastapi-llm-simulator

This project simulates a backend service that simplifies complex technical concepts for different audiences.

## Features

- `/explain` endpoint accepts a technical concept + audience and returns a simplified explanation.
- Asynchronous simulated LLM response.
- Health check at `/health`.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn

## Setup

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
