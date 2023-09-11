from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm , UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.conf import settings
from django.contrib.auth import authenticate, login, get_user_model
from .forms import RegisterForm, EditAccountsForm,PasswordResetForm
from .models import PasswordReset as pr
from core.utils import generate_hash_key

User = get_user_model()

def register(request):
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
    return render(request,'register.html', context)

@login_required()
def edit(request):
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
    return render(request,'edit.html', context)

@login_required()
def profile(request):
    return render(request, 'profile.html')

@login_required()
def edit_password(request):
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST , user = request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user = request.user)
    context['form'] = form
    return render(request,'edit_password.html', context)

def password_reset(request):
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, 'password_reset.html', context)

def password_reset_confirm(request, key):
    context = {}
    reset = get_object_or_404(pr, key=key)
    form = SetPasswordForm(user=reset.user, data = request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, 'password_reset_confirm.html',context)
