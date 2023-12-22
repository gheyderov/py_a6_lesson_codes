from django.template import Library
register = Library()
from products.models import Category, Recipe


@register.simple_tag
def get_categories(limit):
    categories = Category.objects.all()[:limit]
    return categories


@register.inclusion_tag('includes/recent_recipes.html')
def recent_recipes(limit = 5):
    recipes = Recipe.objects.order_by('-created_at')[:limit]
    return {
        'recipes' : recipes
    }