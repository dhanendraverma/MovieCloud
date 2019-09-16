from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.views.generic.edit import CreateView
from django.views import generic
from movie.models import Movie
from django.urls import reverse_lazy, reverse
import pandas as pd
import numpy as np

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
    movie_object = Movie.objects.get(movie_name = "#"+kwargs['name'])
    if "id" not in kwargs.keys():
        id=''
    else:
        id = str(kwargs['id'])
    file_path = "C:/Users/hp/Desktop/Danjgo-Project/MovieCloud/media/Excel/#"+kwargs['name']+".xlsx"

    mov = pd.read_excel(file_path)

    random_val = np.random.randint(0,len(mov))
    tweet_id = str(mov.Tweet_Link.iloc[random_val]).split("/")[-1]
    print("random_val = "+str(random_val))
    print("User name is : "+str(mov.User_Name.iloc[random_val]))
    print("Tweet is : "+str(mov.Tweet.iloc[random_val]))


    if(id == '1'):
        random_val = np.random.randint(0,len(mov))
        tweet_id = str(mov.Tweet_Link.iloc[random_val]).split("/")[-1]
        print("random_val = "+str(random_val))
        print("User name is : "+str(mov.User_Name.iloc[random_val]))
        print("Tweet is : "+str(mov.Tweet.iloc[random_val]))
    elif(id=='2'):
        mov2 = mov[mov.Positive>=0.35]
        random_val = np.random.randint(0,len(mov2))
        tweet_id = str(mov2.Tweet_Link.iloc[random_val]).split("/")[-1]
        print("random_val = "+str(random_val))
        print("User name is : "+str(mov2.User_Name.iloc[random_val]))
        print("Tweet is : "+str(mov2.Tweet.iloc[random_val]))
    elif(id=='3'):
        mov2 = mov[mov.Negitive>=0.35]
        random_val = np.random.randint(0,len(mov2))
        tweet_id = str(mov2.Tweet_Link.iloc[random_val]).split("/")[-1]
        print("random_val = "+str(random_val))
        print("User name is : "+str(mov2.User_Name.iloc[random_val]))
        print("Tweet is : "+str(mov2.Tweet.iloc[random_val]))


    total = len(mov)
    pos = mov[mov.Positive!=0].Positive.count()
    #pos = mov.Positive.mean()*100
    #neg = mov.Negitive.mean()*100
    neg = mov[mov.Negitive!=0].Negitive.count()
    print(mov.head())
    context = {'movie':movie_object,'pos':(pos/total)*100,'neg':(neg/total)*100 ,'tweet_id':tweet_id ,'id':id}
    print(context)
    return render(request, 'movie/report.html', context)
