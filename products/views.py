from django.shortcuts import render, get_object_or_404, HttpResponse
from products.models import Recipe, Category
from django.contrib import messages

# Create your views here.

def recipes(request):
    print(request.session.get('liked_posts'))
    recipe_list = Recipe.objects.all()[::-1] # Select * from Recipe
    categories = Category.objects.all()
    context = {
       "recipe_lists" : recipe_list,
       "categories" : categories
    }
    return render(request, 'recipes.html', context)


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, id = pk)
    recipe.view_count += 1
    recipe.save()

    arr = request.session.get('recently_viewed', [])

    if pk in arr:
        arr.remove(pk)
        recently_viewed_products = Recipe.objects.filter(pk__in = arr)
    else:
        recently_viewed_products = Recipe.objects.filter(pk__in = arr)
        arr.append(pk)
        request.session['recently_viewed'] = arr

    context = {
        'recipe' : recipe,
        'recently_viewed_products' : recently_viewed_products
    }
    return render(request, 'single.html', context)


# def like_post(request, pk):
#     messages.add_message(request, messages.SUCCESS, "Liked!")
#     request.session['liked_posts'] = request.session.get('liked_posts', ' ') + str(pk) + ' ' # 3 2 1 2
#     return render(request, 'recipes.html')

def like_post(request, pk):
    response = HttpResponse('Liked!')
    response.set_cookie('liked_posts', request.COOKIES.get('liked_posts', ' ') + str(pk) + ' ')
    return response