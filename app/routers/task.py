from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models.task import Task
from app.models.user import User
from app.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete, func
from slugify import slugify
from fastapi import APIRouter
router = APIRouter(prefix="/task", tags=["task"])

@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks_get = db.scalars(select(Task).where(Task.user_id != None)).all()
    return tasks_get

    pass
@router.get("/task_id")
async def task_by_id(task_id: int,db: Annotated[Session, Depends(get_db)]):
    query = db.scalars(select(Task).where(Task.id == task_id)).all()
    if len(query) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found')
    return query

    pass
@router.post("/create")
async def creat_task(user_id: int,db: Annotated[Session, Depends(get_db)], create_task: CreateTask):

    query = db.scalars(select(User).where(User.id == user_id)).all()
    if len(str(query))==2:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found')

    max_id = db.scalars(select(func.max(Task.id))).first()
    if max_id is not None:
        slug_name=f"task_{max_id+1}"
        content_name=f"content_{max_id+1}"
    else:
        slug_name = f"user_1"
        content_name = f"content_1"
    db.execute(insert(Task).values(title=create_task.title, content=content_name,
                                   priority=create_task.priority, user_id=user_id, slug=slug_name))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router.put("/update")
async def update_task(task_id: int,db: Annotated[Session, Depends(get_db)], update_task: UpdateTask):
    query = db.scalar(select(Task).where(Task.id == task_id))

    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found')

    db.execute(update(Task).where(Task.id == task_id).values(
        title=update_task.title,
        content=update_task.content,
        priority=update_task.priority))


    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task update is successful!'
    }

    pass
@router.delete("/delete")
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    query = db.scalars(select(User).where(Task.id == task_id)).all()
    if len(str(query))==2:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found')
    query = delete(Task).where(Task.id == task_id)
    db.execute(query)
    db.commit()
    return {"message": "User deleted successfully"}

