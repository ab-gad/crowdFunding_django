from django.urls import path

from .views import campaign, create, rating, report, donation

urlpatterns = [
    path('create', create.create_campaign, name='create_campaign'),
    path('show/<int:campaign_id>', campaign.show, name='campaign_show'),
    path('<int:campaign_id>/cancel', campaign.cancel, name='campaign_cancel'),
    path('<int:campaign_id>/donate', donation.donate, name='campaign_donate'),
    path('<int:campaign_id>/report', report.campaign_report, name='campaign_report'),
    path('<int:campaign_id>/rate', rating.rate, name='campaign_rate'),

]
