#!/usr/bin/env bash

#command bash -c "python main.py"
echo "Gunicorn server starting"

# Allow passing workers as an environment variable or default to 2
WORKERS=${WORKERS:-2}

command bash -c "PYTHONPATH=./:src gunicorn main:app -w $WORKERS -k uvicorn.workers.UvicornWorker -b 0.0.0.0:9001 -t 120"
echo "Welcome"