from django.shortcuts import render, get_object_or_404
from .models import Course
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

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(course)
            form = ContactCourse()
    else:
        form = ContactCourse()
    context['form'] = form 
    context['course'] = course
    template_name = 'details.html'
    return render(request, template_name, context)
