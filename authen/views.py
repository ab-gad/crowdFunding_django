from django.contrib.auth import login as dj_login
from django.contrib.auth import logout as dj_logout
from django.shortcuts import redirect, render
from users.models import UserProfile
from .forms import LoginForm, RegisterForm

# Views


def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        UserProfile.objects.create(user_id=user.id, avatar=user.avatar)
        return redirect("login")
    return render(request, "authen/register.html", {"form": form})


def login(request):

    form = LoginForm(data=request.POST or None)
    if form.is_valid():
        dj_login(request, form.user_cache)
        return redirect("home")
    return render(request, "authen/login.html", {"form": form})


def logout(request):

    dj_logout(request)
    return redirect("login")






