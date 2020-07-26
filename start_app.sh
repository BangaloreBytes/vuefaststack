#/bin/bash

pushd backend
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker