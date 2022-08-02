"""
    API for the application.
"""

from fastapi import FastAPI
from todo import todo_router

# Defining a FastAPI application
app = FastAPI()


@app.get("/")
async def say_hello() -> dict:
    return {"message": "Hello"}

app.include_router(todo_router)
