from sqlalchemy import Column, Integer, Table, ForeignKey
from .entities import Base

# many to many
students_classes_association = Table('students_classes', Base.metadata,
                                     Column('student_id', Integer, ForeignKey('students.id')),
                                     Column('class_id', Integer, ForeignKey('classes.id'))
                                     )
