from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('edit/', edit, name='edit'),
    path('edit_password/', edit_password, name='edit_password'),
    path('password_reset/', password_reset, name='password_reset'),
    path('password_reset_confirm/<key>', password_reset_confirm, name='password_reset_confirm')

]
