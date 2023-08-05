from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_mail_task(subject, content, name, email):
    send_mail(
    subject= subject ,
    message=f"{content}\nFrom {name}",
    from_email=settings.EMAIL_HOST_USER,
    recipient_list=[email])