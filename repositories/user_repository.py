class UserRepository(object):
    def get_all_users(self):
        return f"SELECT * FROM users"

    def get_user_by_id(self, id):
        return f"SELECT * FROM users where id={id}"
