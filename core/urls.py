from django.urls import path
from core.views import home, ContactView, export

urlpatterns = [
    path('', home, name = 'home'),
    path('export/', export, name = 'export'),
    path('contact/', ContactView.as_view(), name='contact')
]