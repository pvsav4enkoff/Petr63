from pydantic import BaseModel

class CreatUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int
class UpdatetUser(BaseModel):
    firstname: str
    lastname: str
    age: int
class CreateTask(BaseModel):
    title: str
    content: str
    priority: int
class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int
