from django.contrib.auth import login as dj_login
from django.contrib.auth import logout as dj_logout

from django.shortcuts import redirect, render

from users.models import User, UserProfile
from .forms import LoginForm, RegisterForm

# to create tokens 
from rest_framework_simplejwt.tokens import RefreshToken

#to make the link bring users back to our app
from django.contrib.sites.shortcuts import get_current_site

#to create a generic view
from rest_framework import generics

#to get our relative url and use it to create the absolute one
from django.urls import reverse

#to send Email
from .utils import Util

#to decode our retreivd token 
import jwt

#to get our app secret key from setting for decoding the token 
from django.conf import settings

def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        UserProfile.objects.create(user_id=user.id, avatar=user.avatar)
        # send activation mail
        # send_activation_email(request, form.cleaned_data.get('email'), user)

        # should give us 2 tokens (access & refresh)
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relativLink=reverse('email_verify')
        absolute_url = 'http://'+current_site+relativLink+"?token="+str(token)

        email_body = 'Hi'+user.first_name+"use the link below to verify your email \n"+absolute_url
        email_subject = "Crowd Funding App | Email Verification"

        data = {'email_body':email_body, 'email_subject':email_subject, 'to_email':user.email}

        Util.send_email(data)

        request.session['activate_MSG'] = 'Activation mail was sent to your mail'

        return redirect("login")
    return render(request, "authen/register.html", {"form": form})


def login(request):

    form = LoginForm(data=request.POST or None)
    if form.is_valid():
        dj_login(request, form.user_cache)
        return _redirect(request, "home")
    return render(request, "authen/login.html", {"form": form})


def logout(request):

    dj_logout(request)
    return redirect("login")



#helpers
def _redirect(request, url):

    nxt = request.GET.get("next", None)
    if nxt:
        return redirect(nxt)

    else:
        return redirect(url)

SECRET_KEY = 'django-insecure-$28^z=-b^#o2^77n)=zdj&1i*p&+itj2ie3=#eri-xe6w!5^1n'
class VerifyEmail(generics.GenericAPIView):
    def get(self,request):
        token = request.GET.get('token')
        print('token',token)
        try:
            tokenPayload =  jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            print('tokenPayload',tokenPayload)
            user = User.objects.get(pk=tokenPayload['user_id'])
            user.is_active = True
            user.save()
            print("SUCCESS")
            request.session['activate_MSG'] = 'Your Email Activated Successfully'
            return redirect("login")
        except:
            print('FAILURE')
            request.session['activate_MSG'] = 'Activation FAILD'
            return redirect("login")

