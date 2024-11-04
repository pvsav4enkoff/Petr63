from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def main_page() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def welcome_admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user")
async def welcome_user(username = "Ilya",age = 32) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

@app.get("/user/{user_id}")
async def welcome_id(user_id: Annotated[int,Path(ge=1, le=100, description="Enter User ID", examples="1")]) -> dict:
    return {"message": f"Вы вошли как {user_id}"}


@app.get("/user/{username}/{age}")
async def welcom_id2(username: Annotated[str, Path( min_length=5, max_length=20, description="Enter username", examples="UrbanUser")], age: Annotated[int, Path(ge=18, le=120, description="Enter age", examples='24')]):
    return    {"message": f"Вы вошли как {username}, возраст {age}"}
