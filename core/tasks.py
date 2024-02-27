import time
from celery import shared_task
from products.models import Subscriber, Recipe
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


@shared_task
def export_data():
    print('Process Start')
    time.sleep(10)
    print('Process End')


@shared_task
def email_to_subscribers():
    mail_list = Subscriber.objects.values_list('email', flat=True)
    recipes = Recipe.objects.all()[:3]
    subject = "Latest Recipes"
    message = render_to_string('email-subscribers.html', {
                'recipes' : recipes
            })
    mail = EmailMultiAlternatives(
        subject= subject,
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=mail_list
    )
    mail.content_subtype = 'HTML'
    mail.send()