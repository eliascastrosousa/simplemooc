from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Enrollment
from .forms import ContactCourse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required()
def home(request):
    cursos = Course.objects.all()
    context = {
        'cursos':cursos,
        'nome' : 'elias',
        'sobrenome' : 'castro',
        'email' : 'eliascastrosousa@gmail.com'
    }
    return render(request, 'home.html', context)

@login_required()
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
    return render(request, 'details.html', context)

@login_required()
def enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment, created = Enrollment.objects.get_or_create(
        user = request.user,
        course=course
    )
    if created:
        enrollment.active()
        messages.success(request, 'Você foi inscrito no curso com sucesso.')
    else:
        messages.info(request, 'Você já está inscrito neste curso!')
    return redirect('profile')

