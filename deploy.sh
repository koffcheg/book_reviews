#!/bin/bash

cd /book_reviews

source $(pipenv --venv)/bin/activate

git pull

pipenv install

python manage.py migrate

