import falcon
import json
from sqlalchemy.ext.declarative import DeclarativeMeta


def new_alchemy_encoder():
    _visited_objs = []

    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if obj in _visited_objs:
                    return None
                _visited_objs.append(obj)

                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    fields[field] = obj.__getattribute__(field)
                # a json-encodable dict
                return fields

            return json.JSONEncoder.default(self, obj)

    return AlchemyEncoder


class Manager(object):
    def __init__(self, resp: falcon.response, body) -> falcon.response:
        self.resp = resp
        self.resp.body = json.dumps(body, cls=new_alchemy_encoder(), check_circular=False)

    def ok(self):
        self.resp.status = falcon.HTTP_200
        return self.resp

    def not_ok(self):
        self.resp.status = falcon.HTTP_500
        return self.resp
