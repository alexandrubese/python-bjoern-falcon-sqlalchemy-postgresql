import falcon
import rapidjson

from functools import partial
from routes import init_routes
from services import db_engine
from falcon import media


''' For Debugging purposes '''

import sys
import pydevd_pycharm

sys.path.append("./debug/pydevd-pycharm.egg")
pydevd_pycharm.settrace('host.docker.internal',
                        port=8002,
                        stdoutToServer=True,
                        stderrToServer=True,
                        suspend=False)
json_handler = media.JSONHandler(
    dumps=partial(
        rapidjson.dumps,
        ensure_ascii=False, sort_keys=True
    ),
    loads=rapidjson.loads,
)
extra_handlers = {
    'application/json': json_handler,
}

# from middleware import (
#    ContentEncodingMiddleware,
# )

# api = falcon.API(middleware=[
#    ContentEncodingMiddleware(),
# ])

api = falcon.API()
api.req_options.media_handlers.update(extra_handlers)
api.resp_options.media_handlers.update(extra_handlers)
db_connection = db_engine.connect()
init_routes.init_app_routes(api, db_connection)
