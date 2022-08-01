"""
    API for the application.
"""

from fastapi import FastAPI

# Defining a FastAPI application
app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to the API"}
