from django.db import models
from accounts.models import User

# Create your models here.

class AbstractModel(models.Model):
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    updated_at = models.DateTimeField('updated_at', auto_now=True)

    class Meta:
        abstract = True


class Recipe(AbstractModel):
    category = models.ForeignKey('Category', related_name='recipes', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', related_name='recipes')
    author = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE)

    title = models.CharField('title', max_length=100)
    small_description = models.CharField('small_description', max_length=100)
    description = models.CharField('description', max_length=100)
    image = models.ImageField('image', upload_to='recipe_images/')
    cover_image = models.ImageField('cover_image', upload_to='recipe_images/')

    def __str__(self) -> str:
        return self.title


class Category(AbstractModel):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField('title', max_length=100)

    def __str__(self) -> str:
        if self.parent:
            return f'{self.parent} - {self.title}'
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Tag(AbstractModel):
    title = models.CharField('title', max_length=100)

    def __str__(self) -> str:
        return self.title