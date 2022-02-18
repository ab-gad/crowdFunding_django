from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('profile/', views.profile, name="user_profile"),
    path('donations/', views.donations, name="user_donations"),
    path('edit/', views.edit, name='user_edit'),
    path('delete/', views.delete, name='user_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)