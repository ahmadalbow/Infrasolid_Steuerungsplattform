from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'pages/index.html',{'ahmad': [1,2,3,4,5]})

def gereate(request):
    return render(request, 'pages/gereate.html')

