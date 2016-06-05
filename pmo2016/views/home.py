# coding=utf-8
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(
        request,
        "pmo2016/home.html",
        {}
    )


def test(request):
    return render(request, "pmo2016/base.html")
