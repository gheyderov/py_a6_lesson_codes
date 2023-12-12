from django.db import models
from products.models import AbstractModel
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Contact(models.Model):
    name = models.CharField('name', max_length=100)
    surname = models.CharField('surname', max_length=100, null=True, blank=True)
    full_name = models.CharField('full_name', max_length=200, null=True, blank=True)
    email = models.EmailField('email', max_length=40)
    subject = models.CharField('subject', max_length=100)
    message = models.TextField('message', max_length=255)
    


class Blog(AbstractModel):
    title = models.CharField('title', max_length=100)
    user = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
    description = models.CharField('description', max_length=255)
    image = models.ImageField('image', upload_to='blog_images', null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title