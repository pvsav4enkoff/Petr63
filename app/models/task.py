from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from user import User
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)
    slug = Column(String, index=True, unique=True)


    user = relationship("users", back_populates='tasks')

from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))
