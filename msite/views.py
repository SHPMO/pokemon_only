from django.shortcuts import render
from django.contrib.auth.models import User, Group, Permission


def home(request):
    return render(request, 'home.html')
