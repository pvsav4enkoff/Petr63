from fastapi import FastAPI, Path, HTTPException, Request, Form, status
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int = None
    username: str = None
    age: int = None


@app.get("/")
async def get_all_messages(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "messages": users})


@app.get("/user/{user_id}")
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "message": users[user_id - 1]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.post('/user/{username}/{age}', status_code=status.HTTP_201_CREATED)
async def app_user(request: Request, username, age, messages: str = Form()) -> HTMLResponse:
    us = User()
    if len(users) == 0:
        us.id = 1
    else:
        max_id = max(user.id for user in users)
        us.id = max_id + 1
    us.username = username
    us.age = age
    users.append(us)
    return templates.TemplateResponse("users.html", {"request": request, "messages": users})


@app.put('/user/{user_id}/{username}/{age}')
async def upd_user(user_id: int, username, age: int):
    try:
        if user_id not in users:
            users[user_id - 1] = {}
        users[user_id - 1]["id"] = user_id
        users[user_id - 1]["username"] = username
        users[user_id - 1]["age"] = age
        return f"User {user_id}  has been updated"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def del_user(user_id: int):
    try:
        del users[user_id - 1]
        return f"User {user_id} has been deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
