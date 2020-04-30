import falcon
import rapidjson

'''
def parse_body(body):
    if not body:
        return rapidjson.dumps(body)
    else:
        return rapidjson.dumps(parse_list(body) if isinstance(body, list) else to_dict(body))
'''


class Manager(object):
    def __init__(self, resp: falcon.response, body) -> falcon.response:
        self.resp = resp
        self.resp.body = rapidjson.dumps(body)

    def ok(self):
        self.resp.status = falcon.HTTP_200
        return self.resp

    def not_ok(self):
        self.resp.status = falcon.HTTP_500
        return self.resp
