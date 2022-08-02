"""
    Models for the application.
"""

from pydantic import BaseModel


class Item(BaseModel):
    item: str
    status: str


class Todo(BaseModel):
    id: int
    item: Item

    class Config:
        Schema_extra = {
            "Example": {
                "id": 1,
                "item": {"item": "Buy milk", "status": "pending"},
            }
        }


class TodoItem(BaseModel):
    item: Item

    class Config:
        Schema_extra = {
            "Example": {
                "item": "Read the next chapter of the book",
                "status": "pending",
            }
        }
