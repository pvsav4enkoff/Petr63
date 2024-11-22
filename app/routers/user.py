from app.backend.db_depends import get_db
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from app.models.user import User
from app.models.task import Task
from app.schemas  import CreateUser, UpdatetUser
from fastapi import APIRouter
from sqlalchemy import insert, select, update, delete, null, func
from slugify import slugify

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users_get = db.scalars(select(User).where(User.age != None)).all()
    return users_get


@router.get("/user_id")
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user_get = select(User).where(User.id == user_id)
    query = db.scalars(user_get).all()
    if len(query) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found')
    return query

# @router.put("/update/{user_id}")
@router.put("/update")
async def update_user(user_id: int, db: Annotated[Session, Depends(get_db)], updat_user: UpdatetUser):
    query = db.scalar(select(User).where(User.id == user_id))

    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found')

    db.execute(update(User).where(User.id == user_id).values(
        firstname=updat_user.firstname,
        lastname=updat_user.lastname,
        age=updat_user.age))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User update is successful!'
    }


@router.post("/create")
async def creat_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    max_id = db.scalars(select(func.max(User.id))).first()
    # print(max_id)
    if max_id is not None:
        slug_name=f"user{max_id+1}"
    else:
        slug_name = f"user1"
    db.execute(insert(User).values(username=create_user.username, firstname=create_user.firstname,
                                   lastname=create_user.lastname, age=create_user.age,slug=slug_name))

    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.delete("/delete")
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    query = db.scalars(select(User).where(User.id == user_id)).all()
    if len(str(query)) == 2:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found')
    query = delete(User).where(User.id == user_id)
    db.execute(query)
    db.commit()
    query = delete(Task).where(Task.user_id == user_id)
    db.execute(query)
    db.commit()
    return {"message": "User deleted successfully"}
