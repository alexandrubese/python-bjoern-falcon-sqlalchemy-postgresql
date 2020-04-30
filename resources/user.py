import rapidjson as json
import falcon
from managers.response_manager import ResponseManager
from repositories.user_repository import UserRepository


class User(object):
    def __init__(self, db_session):
        self.repository = UserRepository(db_session)

    def on_get_collection(self, req, resp):
        try:
            result = self.repository.get_all_users()
            ResponseManager(resp, result).ok()

        except Exception as error:
            error = {"status": False, "message": str(error), "data": None}
            ResponseManager(resp, error).not_ok()

    def on_post_collection(self, req, resp):
        try:
            body = req.media
            result = self.repository.add_user(body)
            ResponseManager(resp, result).ok()

        except Exception as error:
            error = {"status": False, "message": str(error), "data": None}
            ResponseManager(resp, error).not_ok()

    def on_get_item(self, req, resp, id):
        try:
            result = self.repository.get_user_by_id(id)
            ResponseManager(resp, result).ok()

        except Exception as error:
            error = {"status": False, "messagess": str(error), "data": None}
            ResponseManager(resp, error).not_ok()

    def on_get_mock_user(self, req, resp):
        try:
            resp.body = json.dumps({"Hello": "World!"})
            resp.status = falcon.HTTP_200
        except Exception as error:
            error = {"status": False, "messagess": str(error), "data": None}
            ResponseManager(resp, error).not_ok()
