from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'test2/', views.movie_view)
    ]