from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.conf import settings
from django.contrib.auth import authenticate, login

def register(request):
    template_name = 'register.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request,template_name, context)

@login_required()
def edit(request):
    pass

@login_required()
def profile(request):
    return render(request, 'profile.html')
