"""disaster_managment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from donate_money import views
from accounts.views import login_view, logout_view, register,register_as_volunteer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('donate_money.urls')),
    path('', include('donate_goods.urls')),
    path('register/', register, name='register'),
    path('register_as_volunteer/', register_as_volunteer, name='register_as_volunteer'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('', include('homepage.urls')),

    path('',include('homepage.urls')),

]
