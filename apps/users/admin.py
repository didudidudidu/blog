from django.contrib import admin

from .models import UserProfile
# Register your models here.


@admin.register(UserProfile)
class PostAdmin(admin.ModelAdmin):
    list_display = ['username', 'nick_name', 'birday', 'gender', 'address', 'mobile', ]
