"""
    Models for the application.
"""

from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    item: str
