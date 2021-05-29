from django.contrib import admin
from django.urls import path
from .views import show_page, translate, save_img

urlpatterns = [
    path('', show_page),
    path('upload/', save_img),
    path('translate/', translate),
]
