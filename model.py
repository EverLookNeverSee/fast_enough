"""
    Models for the application.
"""
from fastapi import Form
from pydantic import BaseModel
from typing import List, Optional


class Item(BaseModel):
    item: str
    status: str


class Todo(BaseModel):
    id: int
    item: Item

    @classmethod
    def as_form(
            cls, item: str = Form(...)
    ):
        return cls(item=item)

    class Config:
        Schema_extra = {
            "example": {
                "id": 1,
                "item": {"item": "Buy milk", "status": "pending"},
            }
        }


class TodoItem(BaseModel):
    item: Item

    class Config:
        schema_extra = {
            "example": {
                "item": "Read the next chapter of the book",
                "status": "pending",
            }
        }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {"item": "Read the next chapter of the book", "status": "pending"},
                    {"item": "Buy milk", "status": "pending"},
                ]
            }
        }
