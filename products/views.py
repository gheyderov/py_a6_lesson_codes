from django.shortcuts import render
from products.models import Recipe, Category

# Create your views here.

def recipes(request):
    recipes = Recipe.objects.all()[::-1] # Select * from Recipe
    categories = Category.objects.all()
    context = {
       "recipe_lists" : recipes,
       "categories" : categories
    }
    return render(request, 'recipes.html', context)