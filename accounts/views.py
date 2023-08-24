from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.conf import settings
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, EditAccountsForm

def register(request):
    template_name = 'register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username = user.username, password = form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    context = {
        'form':form
    }
    return render(request,template_name, context)

@login_required()
def edit(request):
    template_name = 'edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountsForm(instance=request.user)
            context['success'] = True
    else:
        form = EditAccountsForm(instance=request.user)
    context['form'] = form
    return render(request,template_name, context)

@login_required()
def profile(request):
    return render(request, 'profile.html')

@login_required()
def editpassword(request):
    template_name = 'editpassword.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST , user = request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user = request.user)
    context['form'] = form
    return render(request,template_name, context)