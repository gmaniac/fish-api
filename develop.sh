#!/usr/bin/env bash

source /var/app/venv/bin/activate && \
	cd /var/app/current && \
	flask run --host=0.0.0.0