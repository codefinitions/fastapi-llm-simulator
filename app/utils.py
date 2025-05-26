"""
Utility functions for the application.
"""

import asyncio


async def get_mock_explanation(concept: str, audience: str) -> str:
    """
    Simulates a call to a large language model (LLM) with artificial delay.

    Args:
        concept (str): The technical concept to explain.
        audience (str): The target audience.

    Returns:
        str: A simplified explanation string.
    """
    await asyncio.sleep(1)  # Simulate network or LLM delay
    return f"Imagine explaining '{concept}' to a '{audience}'. It's like describing magic in simple words!"
