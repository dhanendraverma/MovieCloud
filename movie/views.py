from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.views.generic.edit import CreateView
from django.views import generic
from movie.models import Movie
from django.urls import reverse_lazy, reverse
import pandas as pd

def movie_view(request):
    if request.method == 'POST':
        form = movieForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = movieForm()
    return render(request, 'sample.html', {'form' : form})


def success(request):
    return HttpResponse('successfuly uploaded')



class MovieListView(generic.ListView):
    model = Movie
    template_name = 'movie/movies.html'



class MovieCreatView(CreateView):
    model = Movie
    fields = ['movie_name','poster','word_cloud','tweets']
    template_name = 'movie/create.html'

    def get_success_url(self):
        return reverse('movie-list')



def handle(request,**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))
    print(request)
    movie_object = Movie.objects.get(movie_name = "#"+value)
    file_path = "/home/venkatesh/Desktop/MovieCloud/media/Excel/#"+value+".xlsx"

    mov = pd.read_excel(file_path)
    print(mov.head())
    context = {'movie':movie_object}
    print(context)
    return render(request, 'movie/report.html', context)
