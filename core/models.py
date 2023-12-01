from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField('name', max_length=100)
    email = models.EmailField('email', max_length=40)
    subject = models.CharField('subject', max_length=100)
    message = models.TextField('message', max_length=255)