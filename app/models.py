"""
Pydantic models for request and response validation.
"""

from pydantic import BaseModel, Field


class ExplanationRequest(BaseModel):
    """
    Schema for the incoming explanation request.
    """
    concept: str = Field(..., min_length=1, description="The technical concept to explain.")
    audience: str = Field(..., min_length=1, description="The target audience for the explanation.")


class ExplanationResponse(BaseModel):
    """
    Schema for the outgoing explanation response.
    """
    concept: str
    audience: str
    explanation: str
