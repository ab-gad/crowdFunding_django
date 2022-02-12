from campaign.models import Campaign, Donation
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


@login_required
def profile(request):
    current_user_campaigns = Campaign.objects.filter(
        creator_id=request.user.id)
    return render(request, 'profile/base.html', {'campaigns': current_user_campaigns, 'donations': False})
