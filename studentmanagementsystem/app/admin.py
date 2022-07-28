from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class UserModel(UserAdmin):
    list_display = ['username','user_type']

admin.site.register(CustomUser,UserModel)