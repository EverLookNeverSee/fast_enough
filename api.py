"""
    API for the application.
"""

from fastapi import APIRouter

# Defining a FastAPI router
router = APIRouter()


@router.get("/hello")
async def say_hello() -> dict:
    return {"message": "Hello"}
