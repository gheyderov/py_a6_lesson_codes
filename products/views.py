from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponse
from products.models import Recipe, Category, Tag
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, CreateView, UpdateView
from products.forms import CommentForm, SubCommentForm, RecipeCreateForm
from django.urls import reverse_lazy

# Create your views here.


class RecipeListView(ListView):
    template_name = 'recipes.html'
    model = Recipe
    context_object_name = 'recipes' # Recipe.objects.all()
    paginate_by = 2
    

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        tag = self.request.GET.get('tag')
        if category:
            queryset = queryset.filter(category__id = category)
        if tag:
            queryset = queryset.filter(tags__id = tag)
        if category and tag:
            queryset = queryset.filter(category__id = category, tags__id = tag)
        return queryset


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

# def recipes(request):
#     print(request.session.get('liked_posts'))
#     recipe_list = Recipe.objects.all()[::-1] # Select * from Recipe
#     categories = Category.objects.all()
#     context = {
#        "recipe_lists" : recipe_list,
#        "categories" : categories
#     }
#     return render(request, 'recipes.html', context)


class RecipeDetailView(FormMixin, DetailView):
    template_name = 'single.html'
    model = Recipe # recipe
    form_class = CommentForm # form
    subForm = SubCommentForm
    # success_url = reverse_lazy('recipe_detail')

    def get_success_url(self) -> str:
        return reverse_lazy('recipe_detail', kwargs = {'pk' : self.object.pk})

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        if 'parent' in self.request.POST:
            form = self.subForm
        form = self.get_form()
        self.object = self.get_object()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form: Any) -> HttpResponse:
        form.instance.parent_id = self.request.POST.get('parent', None)
        form.instance.user = self.request.user
        form.instance.recipe = self.object
        form.save()
        return super().form_valid(form)



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


class RecipeCreateView(CreateView):
    template_name = 'create_story.html'
    form_class = RecipeCreateForm
    # success_url = reverse_lazy('home')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
    

class RecipeUpdateView(UpdateView):
    template_name = 'create_story.html'
    form_class = RecipeCreateForm
    model = Recipe