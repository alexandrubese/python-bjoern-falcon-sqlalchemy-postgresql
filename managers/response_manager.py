import falcon
import rapidjson
from sqlalchemy import inspect


def parse_list(items):
    return [to_dict(item) for item in items]


def to_dict(obj, with_relationships=True):
    d = {}
    for column in obj.__table__.columns:
        if with_relationships and len(column.foreign_keys) > 0:
            # Skip foreign keys
            continue
        d[column.name] = getattr(obj, column.name)

    if with_relationships:
        for relationship in inspect(type(obj)).relationships:
            val = getattr(obj, relationship.key)
            d[relationship.key] = to_dict(val) if val else None
    return d


def create_response(body):
    if not body:
        return rapidjson.dumps(body)
    else:
        return rapidjson.dumps(parse_list(body) if isinstance(body, list) else to_dict(body))


class Manager(object):
    def __init__(self, resp: falcon.response, body) -> falcon.response:
        self.resp = resp
        self.resp.body = create_response(body)

    def ok(self):
        self.resp.status = falcon.HTTP_200
        return self.resp

    def not_ok(self):
        self.resp.status = falcon.HTTP_500
        return self.resp
