import os
from celery import Celery

# Set default Django settings module for 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_core.settings')

celery_app = Celery('a_core')

# Load configuration from Django settings module
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks in Django apps
celery_app.autodiscover_tasks()

# If you need to add any other configurations or updates, you can do so here.
