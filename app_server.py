import bjoern
import os
import signal
import falcon
from routes import init_routes
import sys
import pydevd_pycharm

host = '0.0.0.0'
port = 8000
NUM_WORKERS = 1 #set this to 6+ for performance
worker_pids = []

api = falcon.API()
init_routes.init_app_routes(api)

sys.path.append("./debug/pydevd-pycharm.egg")
pydevd_pycharm.settrace('host.docker.internal',
                        port=8002,
                        stdoutToServer=True,
                        stderrToServer=True,
                        suspend=False)

bjoern.listen(api, host, port, reuse_port=True)
print(f"Bjoern server listening on port {port}")
bjoern.run()

'''
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
'''