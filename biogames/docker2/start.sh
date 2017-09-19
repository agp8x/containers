#!/bin/bash

if [ ! -f /venv/bin/activate ]; then
	virtualenv /venv;
fi;
source /venv/bin/activate;
LIBRARY_PATH=/lib:/usr/lib pip install -r /biogames/requirements.txt;

until pg_isready -h db; do
	echo "Waiting for Postgres@db…";
	sleep 1;
done

/biogames/manage.py $@