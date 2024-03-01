#!/bin/sh
set -e

# Add the cron job to execute "python manage.py machinewise" every 5 minutes
echo "*/5 * * * * cd /app && python manage.py machinewise" | crontab -