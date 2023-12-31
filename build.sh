#!/usr/bin/env bash
# exit on error
set -o errexit

npm install --prefix ./theme/static_src

python -m pip install --upgrade pip
pip install -r requirements.txt

python manage.py tailwind build
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
