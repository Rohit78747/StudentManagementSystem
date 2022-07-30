"""studentmanagementsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views, Hod_View,Staff_Views,Student_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.Base,name='Base'),
#     Login path
    path('',views.Login,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='doLogout'),

    #profile Update

    path('profile',views.Profile,name='profile'),
    path('profile/update',views.Profile_Update,name='profile_update'),

    #This is hod panel url
    path('HOD/Home',Hod_View.Home,name='hod_home'),
    path('Hod/Student/Add',Hod_View.AddStudent,name="add_student")

]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


