from rest_framework import routers
from django.urls import path, include
from .views import CampaignList, campaign_detail

router = routers.DefaultRouter()
router.register(r'Campaign', CampaignList)
urlpatterns = [
    path('', include(router.urls)),
    path('detail/<int:cam_id>/', campaign_detail),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
