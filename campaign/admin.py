from django.contrib import admin

# Register your models here.

from .models import Campaign,Category,CampaignImage,Rating

admin.site.register(Campaign)
admin.site.register(Category)
admin.site.register(CampaignImage)
admin.site.register(Rating)