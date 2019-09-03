from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *

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
	return render(request,'movie/index.html')