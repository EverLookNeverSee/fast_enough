"""
    todo.py - A simple todo list application
"""

from fastapi import APIRouter
from model import Todo


# Defining todo router
todo_router = APIRouter()

todo_list = list()


@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}


@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}
