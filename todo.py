"""
    todo.py - A simple todo list application
"""

from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from model import Todo, TodoItem, TodoItems
from fastapi.templating import Jinja2Templates


# Defining todo router
todo_router = APIRouter()

todo_list = list()

templates = Jinja2Templates(directory="templates/")


@todo_router.post("/todo")
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)) -> templates.TemplateResponse:
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse("todo.html", {"request": request, "todos": todo_list})


@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todos(request: Request) -> templates.TemplateResponse:
    return templates.TemplateResponse("todo.html", {"request": request, "todos": todo_list})


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(request: Request,
                          todo_id: int = Path(..., title="Todo ID", gt=0)) -> templates.TemplateResponse:
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse("todo.html", {"request": request, "todos": todo})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo with supplied ID doesn't exist")


@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated",
                                                               gt=0)) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"message": "Todo updated successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo with supplied ID doesn't exist")


@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int = Path(..., title="Todo ID", gt=0)) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo_list.remove(todo)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo with supplied ID doesn't exist")


@todo_router.delete("/todo")
async def delete_all_todos() -> dict:
    todo_list.clear()
    return {"message": "All todos deleted successfully"}
