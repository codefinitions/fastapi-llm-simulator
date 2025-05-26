"""
Main application file that defines FastAPI routes.
"""

from fastapi import FastAPI, HTTPException
from models import ExplanationRequest, ExplanationResponse
from utils import get_mock_explanation

app = FastAPI()


@app.get("/health")
async def health_check():
    """
    Basic health check endpoint to ensure the API is running.
    Returns:
        dict: A status message.
    """
    return {"status": "ok"}


@app.post("/explain", response_model=ExplanationResponse)
async def explain_concept(request: ExplanationRequest):
    """
    Accepts a concept and audience, and returns a simplified explanation.

    Args:
        request (ExplanationRequest): Incoming request containing the concept and audience.

    Returns:
        ExplanationResponse: JSON object containing the concept, audience, and a simplified explanation.
    """
    try:
        explanation = await get_mock_explanation(request.concept, request.audience)
        return ExplanationResponse(
            concept=request.concept,
            audience=request.audience,
            explanation=explanation
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail="Something went wrong while generating the explanation.")
