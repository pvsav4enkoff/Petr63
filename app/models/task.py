from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.models.user import User
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, unique=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey(User.__tablename__ + '.id'), index=True, nullable=False)
    slug = Column(String, index=True, unique=True)

    users = relationship('User', backref='tasks')
    # users = relationship('User', back_populates='Task')

from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))