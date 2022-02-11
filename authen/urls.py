
from django.contrib import admin
from django.contrib.auth import views as dj_auth_views
from django.urls import include, path

from . import views

urlpatterns = [

    # authentications
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),

    
]