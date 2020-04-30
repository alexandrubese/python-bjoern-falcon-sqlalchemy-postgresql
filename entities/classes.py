from sqlalchemy import Column, Integer
from .entities import Base


class Class(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
