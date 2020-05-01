import json

from sqlalchemy.orm.session import Session
from entities.user import User
from repositories.serializer import Serializer


class UserRepository(Serializer):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def get_all_users(self):
        return self.parse_list(self.session.query(User).all())

    def get_user_by_id(self, id):
        item = self.session.query(User).get(id)
        return self.parse_dict(item) if item else {}

    def add_user(self, body):
        user = User(**body)
        self.session.add(user)
        self.session.commit()
        return self.parse_dict(user) if user else {}

    def put_user(self, id, body):
        user = self.session.query(User).get(id)
        for item in body.keys():
            setattr(user, item, body[item])

        self.session.add(user)
        self.session.commit()
        return self.parse_dict(user) if user else {}

    def remove_user(self, id):
        user = self.session.query(User).filter_by(id=id)
        user.delete()
        self.session.commit()
        return {"status": True, "message": f"User with id {id} deleted successfully.", "data": None}
