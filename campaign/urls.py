from django.urls import path

from .views import donation

urlpatterns = [
    path('<int:campaign_id>/donate', donation.donate, name='campaign_donate'),
]
