import bjoern
import os
import signal
from app import api

host = '127.0.0.1'
port = 8000
NUM_WORKERS = 6
worker_pids = []

bjoern.listen(api, host, port)
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