from django.urls import path
from products.api.views import CategoryAPIView, tags, RecipeListAPIView, RecipeRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name = 'categories'),
    path('tags/', tags, name = 'tags'),
    path('recipes/', RecipeListAPIView.as_view(), name = 'recipes'),
    path('recipe/<int:pk>/', RecipeRetrieveUpdateDestroyAPIView.as_view(), name = 'recipe_update'),
]