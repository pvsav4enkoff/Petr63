from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users() -> dict:
    return users
@app.post('/user/{username}/{age}')
async def app_user(username,age):
    ind=str(int(max(users,key=int))+1)
    users[ind]=f"Имя: {username}, возраст: {age}"
    return f"User {ind} is registered"
@app.put('/user/{user_id}/{username}/{age}')
async def upd_user(user_id,username,age):
    users[user_id]=f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"
@app.delete('/user/{user_id}')
async def del_user(user_id):
    users.pop(user_id)
    return f"User {user_id} has been deleted"