from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
	re_path(r'movie/$',views.MovieListView.as_view(),name='movies'),
	re_path(r'create/$', views.MovieCreatView.as_view(), name='movie-add'),
	re_path(r'test2/', views.movie_view),
    re_path(r'show_(?P<name>[a-zA-Z0-9#]+)/',views.handle, name = 'movie_chart'),
    re_path(r'show_(?P<name>[a-zA-Z0-9#]+)/popup1/(?P<id>[1-3]+)/$',views.handle, name = 'movie_chart'),
    re_path(r'^$', views.MovieListView.as_view(),name='movie-list')

    ]
