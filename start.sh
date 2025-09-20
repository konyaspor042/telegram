#!/bin/bash
source $VIRTUAL_ENV/bin/activate
exec gunicorn bot:app --bind 0.0.0.0:$PORT