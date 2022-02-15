
from django.core import serializers
from django.db.models import Avg, Sum
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from taggit.models import Tag

from ..models import Campaign, Category


def show(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    images = campaign.images.all()
    average_rating = campaign.ratings.all().aggregate(Avg('value'))[
        'value__avg']

    # return user rating if found
    user_rating = 0

    if request.user.is_authenticated:
        prev_rating = campaign.ratings.filter(user_id=request.user.id)

        if prev_rating:
            user_rating = prev_rating[0].value

    if average_rating is None:
        average_rating = 0
    donations = campaign.donations.all().aggregate(Sum('amount'))[
        'amount__sum']
    if donations is None:
        donations = 0
    date_validation = False
    if campaign.end_date > timezone.now():
        date_validation = True
    tags = campaign.tags.all()
    delta = timezone.now() - campaign.start_date
    similar_camps = campaign.tags.similar_objects()
    categories = Category.objects.all()
    context = {'campaign_info': campaign, 'images': images, 'rating': average_rating*20,
               'tags': tags, 'donations': donations, 'days': delta.days, 'user_rating': user_rating,
               'rating_range': range(5, 0, -1), 'similar_camps': similar_camps[:6], "categories": categories, 'date_validation':date_validation}

    return render(request, 'campaign/show.html', context)


def cancel(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    donations = campaign.donations.all().aggregate(Sum('amount'))[
        'amount__sum']
    if donations is None:
        donations = 0
    if donations/campaign.target < 0.25:
        campaign.delete()
    return redirect('user_profile')


