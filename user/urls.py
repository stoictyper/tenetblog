from django.contrib import admin
from django.urls import path
from . import views
app_name="user"

urlpatterns = [
    path('signup/',views.signup, name="signup"),
    path('login/',views.loginn, name="login"),
    path('logout/',views.logoutt, name="logout"),
]
