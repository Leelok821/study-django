from django.contrib import admin

# Register your models here.

from .models import BookInfo, HeroInfo

admin.site.register([BookInfo, HeroInfo])