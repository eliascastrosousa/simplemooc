from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('details/<slug>', details, name='details'),
    path('enrollment/<slug>', enrollment, name='enrollment'),

    
]
