from django.urls import path

from .views import campaign, create

urlpatterns = [
    path('create', create.create_campaign, name='create_campaign'),
    path('show/<int:campaign_id>', campaign.show, name='campaign_show'),
    path('<int:campaign_id>/cancel',campaign.cancel, name='campaign_cancel'),
]
