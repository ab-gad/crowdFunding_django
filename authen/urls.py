
from django.contrib import admin
from django.contrib.auth import views as dj_auth_views
from django.urls import include, path

from . import views

urlpatterns = [

    # authentications
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    # change password
    path('password_change/', dj_auth_views.PasswordChangeView.as_view(template_name='authen/password/change.html'),
         name='password_change'),
    path('password_change/done/', dj_auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
]     

    
]
