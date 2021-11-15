#!/usr/bin/env bash

PORT=${PORT:-8080}

exec gunicorn -b 0.0.0.0:$PORT app:app
