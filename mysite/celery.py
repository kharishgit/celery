from celery import Celery
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
app = Celery("client")
app.autodiscover_tasks()

app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.beat_schedule = {
    "send_notification" : {
        "task":"myapp.tasks.add_notification",
        "schedule":1.0
    },

"notify" : {
"task":"myapp.tasks.new",
"schedule":5.0
}
}