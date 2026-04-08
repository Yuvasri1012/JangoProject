from django.urls import path
from .views import about_page,signup_page,login_page,signup_action,login_action

urlpatterns = [
    path('about',about_page),
    path('signup',signup_page,name='signup'),
    path('login',login_page,name='login'),
    path('signup_action',signup_action),
    path('login_action',login_action)
]
