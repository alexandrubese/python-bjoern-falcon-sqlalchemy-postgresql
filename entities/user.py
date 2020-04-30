from sqlalchemy import Column, Integer, String
from .entities import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s')>" % (
            self.name, self.fullname)
