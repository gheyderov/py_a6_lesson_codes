from django.contrib import admin
from products.models import Category, Tag, Recipe, RecipeImage, RecipeComment, BlockedIps
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
admin.site.register(RecipeComment)
admin.site.register(BlockedIps)


class RecipeImageAdmin(admin.TabularInline):
    model = RecipeImage


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'get_tags']
    list_display_links = ['id', 'title']
    list_editable = ['category']
    list_filter = ['category']
    # list_per_page = 2
    search_fields = ['title', 'category__title']
    inlines = [RecipeImageAdmin]
    # prepopulated_fields = {
    #     'slug' : ('title',)
    # }
    form = RecipeAdminForm

    def get_tags(self, obj):
        tags = []
        for tag in obj.tags.all():
            tags.append(tag.title)
        return tags