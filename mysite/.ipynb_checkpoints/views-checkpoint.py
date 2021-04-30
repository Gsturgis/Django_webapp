from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from mysite.models import Person



# view using render()
def index(request):
    data = {
        "person": Person.objects.all(),      
    }
    print(data)
    return render(request, 'index.html', data)

def about(request):
    return render(request, 'about.html')



