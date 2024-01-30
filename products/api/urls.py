from django.urls import path
from products.api.views import categories, tags, recipes

urlpatterns = [
    path('categories/', categories, name = 'categories'),
    path('tags/', tags, name = 'tags'),
    path('recipes/', recipes, name = 'recipes'),
]