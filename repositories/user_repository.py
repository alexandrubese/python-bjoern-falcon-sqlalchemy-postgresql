from sqlalchemy.orm.session import Session
from entities.user import User


class UserRepository(object):
    def __init__(self, session: Session):
        self.session = session

    def get_all_users(self):
        return self.session.query(User).all()

    def get_user_by_id(self, id):
        item = self.session.query(User).get(id)
        return item if item else {}

    def add_user(self, user):
        user = User(name=user["name"], fullname=user["fullname"])
        added_user = self.session.add(user)
        self.session.commit()
        return added_user
