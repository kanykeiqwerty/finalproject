from .celery import app as celery_app
# from .tasks import send_email_task, send_beat_email
__all__=('celery_app',)
