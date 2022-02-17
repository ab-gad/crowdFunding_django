from rest_framework import routers
from django.urls import path, include
from .views import CampaignList, campaign_detail, user_detail, UserList

router = routers.DefaultRouter()
router.register(r'Campaign', CampaignList)
router.register(r'User', UserList)
urlpatterns = [
    path('', include(router.urls)),
    path('cam-detail/<int:cam_id>/', campaign_detail),
    path('usr-detail/<int:user_id>/', user_detail),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
