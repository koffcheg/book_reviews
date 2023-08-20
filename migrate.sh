#!/bin/bash

git fetch origin main

# Check for migration conflicts by comparing local and remote branches
CONFLICT_FILES=$(git diff HEAD..origin/main --name-only -- '*/migrations/*.py')

# If diff command returns non-empty output, there are migration conflicts
if [ -z "$CONFLICT_FILES" ]; then
  echo 'No migration conflicts detected.'
else
  echo 'Migration conflict detected in the following files:'
  echo "$CONFLICT_FILES"
  exit 1
fi

# Create new migrations
pipenv run python manage.py makemigrations

# Apply migrations
pipenv run python manage.py migrate