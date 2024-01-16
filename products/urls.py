from django.urls import path
from products.views import RecipeListView, RecipeDetailView, like_post

urlpatterns = [
    path('recipes/', RecipeListView.as_view(), name= 'recipes'),
    path('like_post/<int:pk>/', like_post, name= 'like_post'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name = 'recipe_detail')
]