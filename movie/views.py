from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
from django.views.generic.edit import CreateView
from movie.models import Movie
from django.urls import reverse_lazy


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


def homeview(request):
    if request.method == 'POST':
        print("sdf")
        return redirect("/")
    return render(request,'movie/movies.html')


class MovieCreatView(CreateView):
    model = Movie
    fields = ['movie_name','poster','word_cloud','tweets']
    template_name = 'movie/create.html'
