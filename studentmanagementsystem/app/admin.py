from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Course, SessionYear, Student, Staff, Subject,Staff_Notification,Staff_Leave


class UserModel(UserAdmin):
    list_display = ['username','user_type']

admin.site.register(CustomUser,UserModel)

admin.site.register(Course)
admin.site.register(SessionYear)

admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Staff_Notification)
admin.site.register(Staff_Leave)

