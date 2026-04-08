"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from .views import index_page,shop_page
from djangoapp .views import get_all_data,signup_page
from authenticate_app.views import SignupAPI

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',include('djangoapp.urls')),
    path('homepage',get_all_data,name='homepage'),
    path('',signup_page),
    path('',include('rest_app.urls')),
    path('signupp',SignupAPI.as_view())
]
