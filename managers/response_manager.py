import falcon
import rapidjson


class ResponseManager(object):
    def __init__(self, resp: falcon.response, body) -> falcon.response:
        self.resp = resp
        self.resp.body = rapidjson.dumps(body)

    def ok(self):
        self.resp.status = falcon.HTTP_200
        return self.resp

    def not_ok(self):
        self.resp.status = falcon.HTTP_500
        return self.resp
