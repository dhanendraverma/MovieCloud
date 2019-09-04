from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls import static

urlpatterns = [
	re_path(r'movie/$',views.homeview,name='movies'),
	re_path(r'create/$', views.MovieCreatView.as_view(), name='movie-add'),
	re_path(r'test2/', views.movie_view),
    re_path(r'^$', views.homeview),
    ]