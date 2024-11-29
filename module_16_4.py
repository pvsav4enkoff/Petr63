from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str = None
    age: int = None


@app.get("/users")
async def get_all_messages() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def app_user(username: str, age: int):
    us = User()
    if len(users) == 0:
        us.id = 1
    else:
        max_id = max(user.id for user in users)
        us.id = max_id + 1
    us.username = username
    us.age = age
    users.append(us)
    return f"User {us.username} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def upd_user(user_id: int, username, age: int):
    try:
        if user_id not in users:
            users[user_id - 1] = {}
        users[user_id - 1]["id"] = user_id
        users[user_id - 1]["username"] = username
        users[user_id - 1]["age"] = age
        return users[user_id - 1]
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def del_user(user_id: int):
    try:
        del_us = users[user_id - 1]
        del users[user_id - 1]
        return del_us
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
