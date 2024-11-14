from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
# from tasks import Task

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, index=True, unique=True)

    tasks = relationship("tasks", back_populates='users')

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))