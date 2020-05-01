from sqlalchemy import Column, Integer, String
from .entities import Base
from webargs import fields


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    @staticmethod
    def schema():
        return {
            "name": fields.Str(required=True),
            "fullname": fields.Str(required=True, validate=lambda p: len(p) > 6,
                                   error_messages={"validator_failed": "Value should be greater than 6 chars"})
        }
