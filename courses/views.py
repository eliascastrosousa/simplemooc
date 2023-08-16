from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import ContactCourse

def home(request):
    cursos = Course.objects.all()
    template_name = 'home.html'
    context = {
        'cursos':cursos,
        'nome' : 'elias',
        'sobrenome' : 'castro',
        'email' : 'eliascastrosousa@gmail.com'
    }
    return render(request, template_name, context)

"""
def details(request, id):
    course = get_object_or_404(Course, id=id)
    template_name = 'details.html'
    context = {'course':course}
    return render(request, template_name, context)
"""

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if request.method == 'POST':
        form = ContactCourse(request.POST)
    else:
        form = ContactCourse()

    context = {'course':course,
               'form':form
               }
    
    template_name = 'details.html'
    return render(request, template_name, context)