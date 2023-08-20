!/bin/bash

git fetch origin main

# Check for migration conflicts by comparing local and remote branches
git diff HEAD..origin/main --name-only -- '*/migrations/*.py' | grep '*/migrations/*.py'

# If diff command returns non-empty output, there are migration conflicts
if [ $? -eq 0 ]; then
  echo 'No migration conflicts detected.'
else
  echo 'Migration conflict detected. Exiting.'
  exit 1
fi

# Create new migrations
pipenv run python manage.py makemigrations

# Apply migrations
pipenv run python manage.py migrate