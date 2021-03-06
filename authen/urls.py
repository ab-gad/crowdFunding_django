
from django.contrib import admin
from django.contrib.auth import views as dj_auth_views
from django.urls import include, path

from . import views

urlpatterns = [

    # authentications
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    # change password
    path('password_change/', dj_auth_views.PasswordChangeView.as_view(template_name='authen/password/change.html'),
         name='password_change'),
    path('password_change/done/', dj_auth_views.PasswordChangeDoneView.as_view(template_name='authen/password/change_done.html'),
         name='password_change_done'),
    # Reset password form
    path('password_reset/', dj_auth_views.PasswordResetView.as_view(template_name='authen/password/reset_form.html',
        email_template_name='authen/password/reset_email.html',
        subject_template_name='authen/password/reset_email_subject.txt',),
        name='password_reset'),
     # Email sent display message
    path('password_reset/done/', dj_auth_views.PasswordResetDoneView.as_view(template_name='authen/password/reset_done.html'),
         name='password_reset_done'),
    # password reset successfully message
    path('reset/complete/', dj_auth_views.PasswordResetCompleteView.as_view(template_name='authen/password/reset_complete.html'),
         name='password_reset_complete'),        
    # Action to the link sent to email
     path('reset/<uidb64>/<token>/', dj_auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
] 

    

