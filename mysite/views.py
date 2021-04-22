from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# view using render()
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')