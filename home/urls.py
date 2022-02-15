from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('error_404/', views.error, name='error_404'),
    path('search_page/', views.search, name='search_page'),
    path('home/category/<int:categoty_id>', views.category, name='category'),
    path('home/highest_projects/<int:project_id>', views.highest_projects, name='highest_projects'),

]

