from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from campaign.models import Campaign
from .serializers import CampaignSerializer


class CampaignList(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def campaign_detail(request, cam_id):
    try:
        campaign = Campaign.objects.get(cam_id=cam_id)
    except Campaign.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CampaignSerializer(campaign)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CampaignSerializer(campaign, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        campaign.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

