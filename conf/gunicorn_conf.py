import multiprocessing

bind = '0.0.0.0:8000'
#workers = multiprocessing.cpu_count() * 2 + 1
workers = 1
timeout = 36000 #this is set to 30 secs in prod
worker_connections = 1000
#worker_class = "meinheld.gmeinheld.MeinheldWorker"
