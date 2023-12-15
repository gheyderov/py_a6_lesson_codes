from django.shortcuts import render, get_object_or_404
from products.models import Recipe, Category

# Create your views here.

def recipes(request):
    recipe_list = Recipe.objects.all()[::-1] # Select * from Recipe
    categories = Category.objects.all()
    context = {
       "recipe_lists" : recipe_list,
       "categories" : categories
    }
    return render(request, 'recipes.html', context)


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, id = pk)
    context = {
        'recipe' : recipe,
    }
    return render(request, 'single.html', context)