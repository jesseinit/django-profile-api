#!/bin/bash

echo "<<<<<<<<<< Activate Virtual Env>>>>>>>>>>"
source /root/.local/share/virtualenvs/app-*/bin/activate
echo "<<<<<<<<<< Starting Server >>>>>>>>>>"
python manage.py runserver 0.0.0.0:8000
