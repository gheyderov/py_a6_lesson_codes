from django.urls import path
from products.views import recipes

urlpatterns = [
    path('recipes/', recipes, name= 'recipes')
]