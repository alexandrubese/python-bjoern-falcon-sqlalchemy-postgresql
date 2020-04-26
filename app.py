import falcon
from services import database
from routes import init_routes

import sys

''' For Debugging purposes '''
import pydevd_pycharm

sys.path.append("./debug/pydevd-pycharm.egg")
pydevd_pycharm.settrace('host.docker.internal',
                        port=8002,
                        stdoutToServer=True,
                        stderrToServer=True)

# from middleware import (
#    ContentEncodingMiddleware,
# )

conn = database.connect()
# api = falcon.API(middleware=[
#    ContentEncodingMiddleware(),
# ])

api = falcon.API()
init_routes.init_app_routes(api, conn)
