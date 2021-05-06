from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Person, Orders



# view using render()
def index(request):
    person = Person.objects.all(),      
    
    
    return render(request, 'index.html', context={'person':person})

def about(request):
    return render(request, 'about.html')



