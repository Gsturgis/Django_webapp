from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Person, Orders
from .forms import UserForm



# view using render()
def index(request):
    users = Person.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm
    return render(request, 'index.html', context={'users':users, 'form': form})

def about(request):
    return render(request, 'about.html')



