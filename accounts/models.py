from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    image = models.ImageField('image', upload_to='user_profile/', null=True, blank=True)
    bio = models.CharField('bio', max_length=100, null=True, blank=True)