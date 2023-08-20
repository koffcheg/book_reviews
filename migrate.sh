#!/bin/bash

# Function to check for migration conflicts
check_migration_conflicts() {
  # Run 'python manage.py showmigrations --list' and filter lines ending with ']' (indicating leaf nodes)
  CONFLICTS=$(pipenv run python manage.py showmigrations --list | grep '\]$' | wc -l)

  if [ "$CONFLICTS" -gt "1" ]; then
    echo "Migration conflict detected. Please resolve manually."
    exit 1
  fi
}

git pull origin main

check_migration_conflicts

pipenv run python manage.py makemigrations

check_migration_conflicts

pipenv run python manage.py migrate
