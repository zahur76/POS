from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.admin_center, name="admin_center"),
]
