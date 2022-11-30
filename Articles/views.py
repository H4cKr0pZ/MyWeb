from django.shortcuts import render
from django.http import HttpResponse
from . models import Article , Gallery
from sys import stdout
import time
import datetime

# Create your views here.

def index(request):
    articles = Article.objects.all()
    return render(request,'index.html',{'articles':articles})
#    return render(request,'home.html')



def articles(request):
    articles = Article.objects.all()
    return render(request,'index.html',{'articles':articles})

#    return HttpResponse("<h1>Articles</h1>")

def gallery(request):
    gallery = Gallery.objects.all()
    return render(request,'gallery.html',{'gallery':gallery})

def slow_print(str):
    for letter in str:
        stdout.write(letter)
        stdout.flush()
        time.sleep(0.50)