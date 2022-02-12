from django.contrib import admin

# Register your models here.

from .models import Campaign,Category

admin.site.register(Campaign)
admin.site.register(Category)