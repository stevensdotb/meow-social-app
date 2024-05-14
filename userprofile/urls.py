from django.contrib import admin
from django.urls import path

from .views import user_profile

urlpatterns = [
    path("<str:username>/profile", user_profile, name="user_profile"),
]
