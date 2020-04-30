from managers import data_manager


class UserRepository(data_manager.DataManager):
    def __init__(self):
        super().__init__()

    def get_all_users(self):
        query = f"SELECT * FROM users"
        return self.get_data(query)

    def get_user_by_id(self, id):
        query = f"SELECT * FROM users where id={id}"
        return self.get_data(query)
