#!/bin/bash

pip install --upgrade pip
pip install -r /app/requirements.txt
pip install pydevd-pycharm~=201.6668.115

gunicorn app:api -c /app/conf/gunicorn_conf.py --reload