from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    re_path(r'test2/', views.movie_view),
    re_path(r'test3/', TemplateView.as_view(template_name="index.html")),
    ]