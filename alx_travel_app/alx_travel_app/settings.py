# alx_travel_app/settings.py

# Celery Configuration
CELERY_BROKER_URL = 'amqp://localhost'  # RabbitMQ URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'rpc://'
CELERY_TIMEZONE = 'UTC'

