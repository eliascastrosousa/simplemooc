from django.shortcuts import render
from .models import *

def index(request):
    
    context = {
        'nome' : 'elias',
        'sobrenome' : 'castro',
        'email' : 'eliascastrosousa@gmail.com'
    }
    return render(request, 'index.html', context)