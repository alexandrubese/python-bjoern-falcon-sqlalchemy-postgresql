import bjoern
import os
import signal
import sys
import pydevd_pycharm
import falcon
import rapidjson

from functools import partial
from routes import init_routes
from services import db_engine
from falcon import media


host = '0.0.0.0'
port = 8000
NUM_WORKERS = 5 #set this to 6+ for performance
worker_pids = []

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

api = falcon.API()
api.req_options.media_handlers.update(extra_handlers)
api.resp_options.media_handlers.update(extra_handlers)
db_connection = db_engine.connect()
init_routes.init_app_routes(api, db_connection)
'''
sys.path.append("./debug/pydevd-pycharm.egg")
pydevd_pycharm.settrace('host.docker.internal',
                        port=8002,
                        stdoutToServer=True,
                        stderrToServer=True,
                        suspend=False)
'''
bjoern.listen(api, host, port, reuse_port=True)
#print(f"Bjoern server listening on port {port}")
#bjoern.run()


for _ in range(NUM_WORKERS):
    pid = os.fork()
    if pid > 0:
        # in master
        worker_pids.append(pid)
    elif pid == 0:
        # in worker
        try:
            bjoern.run()
        except KeyboardInterrupt:
            pass
        exit()

print(f"Bjoern Worker pids: {worker_pids}")
try:
    for _ in range(NUM_WORKERS):
        os.wait()
except KeyboardInterrupt:
    for pid in worker_pids:
        os.kill(pid, signal.SIGINT)
