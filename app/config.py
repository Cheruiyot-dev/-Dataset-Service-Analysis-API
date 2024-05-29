from celery import Celery


celery_app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

# Database configuration
DB_HOST = 'postgres'
DB_PORT = 5432
DB_NAME = 'dataset_analysis'
DB_USER = 'postgres'
DB_PASSWORD = ''
