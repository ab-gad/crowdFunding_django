from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('error_404/', views.error, name='error_404'),
]
