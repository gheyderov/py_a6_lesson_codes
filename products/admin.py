from django.contrib import admin
from products.models import Category, Tag, Recipe, RecipeImage
from django import forms

# Register your models here.

class RecipeAdminForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'tags' : forms.CheckboxSelectMultiple
        }

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(RecipeImage)


class RecipeImageAdmin(admin.TabularInline):
    model = RecipeImage


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category']
    list_display_links = ['id', 'title']
    list_editable = ['category']
    list_filter = ['category']
    # list_per_page = 2
    search_fields = ['title', 'category__title']
    inlines = [RecipeImageAdmin]
    prepopulated_fields = {
        'slug' : ('title',)
    }
    form = RecipeAdminForm