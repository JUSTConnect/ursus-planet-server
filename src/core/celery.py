import os


from celery import Celery, shared_task
from celery.schedules import crontab
from celery.utils.log import get_task_logger
from django.contrib.auth import get_user_model
from django.core.mail import send_mail


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
logger = get_task_logger(__name__)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute='0', hour='*/1'),
        send_notifications.s('hour'),
        name='Send hour notifications'
    )
    sender.add_periodic_task(
        crontab(minute=0, hour=0),
        send_notifications.s('day'),
        name='Send day notifications'
    )
    sender.add_periodic_task(
        crontab(day_of_week='monday'),
        send_notifications.s('week'),
        name='Send week notifications'
    )
    sender.add_periodic_task(
        crontab(minute=0, hour=0, day_of_month='1'),
        send_notifications.s('month'),
        name='Send month notifications'
    )


@shared_task
def add(x, y):
    return x + y


@app.task
def send_notifications(period: str):
    cabinet_list = get_user_model().objects.filter(
        cabinet_notifications_email=True,
        cabinet_notifications_frequency=period,
        email__isnull=False
    )
    project_list = get_user_model().objects.filter(
        project_notifications_email=True,
        project_notifications_frequency=period,
        email__isnull=False
    )
    send_mail(
        subject="Ursas cabinet email notification",
        from_email='support@ursasplanet.com',
        message=f"Here is your code",
        recipient_list=[user.email for user in cabinet_list],
        fail_silently=False,
    )
    send_mail(
        subject="Ursas project email notification",
        from_email='support@ursasplanet.com',
        message=f"Here is your code",
        recipient_list=[user.email for user in project_list],
        fail_silently=False,
    )
    return [[user.email for user in cabinet_list], [user.email for user in project_list]]


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


# app.conf.beat_schedule = {
#     'notifications-hour': {
#         'task': 'tasks.send_notifications',
#         'schedule': 1,
#     },
#     'notifications-day': {
#         'task': 'tasks.send_notifications',
#         'schedule': 10,
#     },
#     'notifications-week': {
#         'task': 'tasks.send_notifications',
#         'schedule': 10,
#     },
#     'notifications-month': {
#         'task': 'tasks.send_notifications',
#         'schedule': 10,
#     },
# }

app.conf.timezone = 'Africa/Abidjan'