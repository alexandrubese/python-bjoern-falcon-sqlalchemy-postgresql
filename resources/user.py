import json
from managers import data_manager
from managers import response_manager
from repositories import user_repository


class User(data_manager.DataManager):
    def __init__(self):
        super().__init__()

    def on_get_collection(self, req, resp):
        try:
            user_repo = user_repository.UserRepository()
            operation = user_repo.get_all_users()
            result = self.get_data(operation)

            if result['status']:
                response_manager.Manager(resp, result).ok()
            else:
                response_manager.Manager(resp, result).not_ok()
        except Exception as error:
            error = json.dumps({"status": False, "message": str(error), "data": None})
            response_manager.Manager(resp, error).not_ok()

    def on_get_item(self, req, resp, id):
        try:
            user_repo = user_repository.UserRepository()
            operation = user_repo.get_user_by_id(id)
            result = self.get_data(operation)

            if result['status']:
                response_manager.Manager(resp, result).ok()
            else:
                response_manager.Manager(resp, result).not_ok()
        except Exception as error:
            error = json.dumps({"status": False, "messagess": str(error), "data": None})
            response_manager.Manager(resp, error).not_ok()
