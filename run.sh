#!/usr/bin/env bash
set -e
export FLASK_APP=src.app
export FLASK_ENV=${FLASK_ENV:-production}
python3 -u -m flask run --host=0.0.0.0 --port=${PORT:-8080}

