from fastapi import FastAPI

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
async def welcome_id(user_id) -> dict:
    return {"message": f"Вы вошли как {user_id}"}

