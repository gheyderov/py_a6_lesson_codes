from django.urls import path
from products.views import recipes, recipe_detail, like_post

urlpatterns = [
    path('recipes/', recipes, name= 'recipes'),
    path('like_post/<int:pk>/', like_post, name= 'like_post'),
    path('recipe/<int:pk>/', recipe_detail, name = 'recipe_detail')
]