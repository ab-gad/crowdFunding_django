from rest_framework import serializers

from campaign.models import Campaign


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'
