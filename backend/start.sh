#!/bin/bash

pip install --upgrade pip
pip install -r /app/requirements.txt
pip install pydevd-pycharm~=201.6668.115

# use this in prod
# gunicorn app:api --worker-class=meinheld.gmeinheld.MeinheldWorker --worker-connections=1000 --workers=6 --threads=2 --reuse-port

gunicorn app:api -c /app/conf/gunicorn_conf.py --reload