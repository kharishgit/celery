from celery import shared_task

@shared_task
def add_notification():
    print("Working")

@shared_task
def new():
    print("Adding")