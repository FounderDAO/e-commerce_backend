from django.contrib import admin
from django.urls import path
from .views import UserCreate

urlpatterns = [
    path('auth/', UserCreate.as_view()),
]
