from django.urls import path

from .views import campaign, donation, rating, report, create

urlpatterns = [
    path('<int:campaign_id>/donate', donation.donate, name='campaign_donate'),
    path('create', create.create_campaign, name='create_campaign'),
]
