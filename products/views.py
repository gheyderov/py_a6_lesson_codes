from django.shortcuts import render
from products.models import Recipe, Category

# Create your views here.

def recipes(request):
    recipess = Recipe.objects.all()[::-1] # Select * from Recipe
    categories = Category.objects.all()
    context = {
       "recipe_lists" : recipess,
       "categories" : categories
    }
    return render(request, 'recipes.html', context)