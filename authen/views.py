from django.contrib import messages
from django.contrib.auth import login as dj_login
from django.contrib.auth import logout as dj_logout
from django.contrib.auth.forms import UserCreationForm
# from .token import \
#     AccountActivationTokenGenerator as TokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
# from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from users.models import User, UserProfile

from .forms import LoginForm, RegisterForm

# Views


def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        UserProfile.objects.create(user_id=user.id, avatar=user.avatar)
        # send activation mail
        # send_activation_email(request, form.cleaned_data.get('email'), user)

        return redirect("login")
    return render(request, "authen/register.html", {"form": form})


def login(request):

    form = LoginForm(data=request.POST or None)
    if form.is_valid():
        dj_login(request, form.user_cache)
        return redirect(request, "home")
    return render(request, "authen/login.html", {"form": form})


def logout(request):

    dj_logout(request)
    # messages.info(request, "You have successfully logged out.")
    return redirect("login")



