from django.shortcuts import render
from django.contrib.auth.models import User, Group, Permission
from django.http import Http404


def home(request):
    raise Http404
    return render(request, 'home.html')
