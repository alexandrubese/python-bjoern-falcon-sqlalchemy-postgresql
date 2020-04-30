from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from .entities import Base


class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    comments = relationship("Comment")
