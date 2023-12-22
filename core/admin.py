from django.contrib import admin
from core.models import Contact, Blog

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name']
    # prepopulated_fields = {
    #     'full_name' : ('name', 'surname')
    # }


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title']
    actions = ['blog_activated', 'blog_deactivated']

    def blog_activated(self, request, queryset):
        queryset.update(status = True)

    def blog_deactivated(self, request, queryset):
        queryset.update(status = False)