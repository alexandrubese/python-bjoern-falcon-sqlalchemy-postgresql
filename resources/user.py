import json

import falcon

from managers import response_manager
from repositories import user_repository


class User(object):
    def on_get_collection(self, req, resp):
        try:
            user_repo = user_repository.UserRepository()
            result = user_repo.get_all_users()

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
            result = user_repo.get_user_by_id(id)

            if result['status']:
                response_manager.Manager(resp, result).ok()
            else:
                response_manager.Manager(resp, result).not_ok()
        except Exception as error:
            error = json.dumps({"status": False, "messagess": str(error), "data": None})
            response_manager.Manager(resp, error).not_ok()

    def on_get_mock_user(self, req, resp):
        try:
            #response_manager.Manager(resp, {"Hello": "World!"}).ok()
            resp.body = json.dumps({"Hello": "World!"})
            resp.status = falcon.HTTP_200
        except Exception as error:
            error = json.dumps({"status": False, "messagess": str(error), "data": None})
            response_manager.Manager(resp, error).not_ok()
