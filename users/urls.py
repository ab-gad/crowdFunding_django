from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name="user_profile"),
    path('edit/', views.edit, name='user_edit'),
    path('check_password/', views.check_password, name='check_password')

]