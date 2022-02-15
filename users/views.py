from campaign.models import Campaign, Donation
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import EditForm
from .models import UserProfile
from django.http import JsonResponse


@login_required(login_url='/auth/login/')
def profile(request):
    current_user_campaigns = Campaign.objects.filter(
        creator_id=request.user.id)
    return render(request, 'profile/base.html', {'campaigns': current_user_campaigns, 'donations': False})

@login_required(login_url='/auth/login/')
def edit(request):
    if request.method == "GET":
        current_user = request.user
        return render(request, 'user/edit.html', {'current_user': current_user})
    else:
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)
        form = EditForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            user = form.save()
            profile.avatar = user.avatar
            profile.save()
            return redirect('user_profile')
        return render(request, 'user/edit.html', {'current_user': current_user, 'form': form})

@login_required(login_url='/auth/login/')
def delete(request):
    request.user.delete()
    return redirect('logout')