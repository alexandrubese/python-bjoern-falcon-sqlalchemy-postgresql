from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from entities.student_classes import students_classes_association
from .entities import Base


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    classes = relationship("Class", secondary=students_classes_association)
