"""artificial_intelligence_ambulance_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from ambulance_system.views import home,sign,adminmain,index,schedule,logout,search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),#主頁
    path('sign/home',index),
    path('sign/',sign),#登入頁面
    path('adminmain/',adminmain),#登入後的管理頁面
    path('index/',index),
    path('schedule/',schedule),
    path('logout/',logout),
    path('index/logout/',logout),
    path('index/search/',search)
]
