from django.shortcuts import render
from django.http import Http404

# Create your views here.
def home(request):
    raise Http404
