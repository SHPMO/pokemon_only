# coding=utf-8
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from pmo2015.models import Vote


def home(request):
    if 'method' in request.GET:
        if Vote.objects.filter(ip_address=request.META.get("REMOTE_ADDR")).count() > 0 or request.session.get('vote'):
            return HttpResponse('true')
        else:
            return HttpResponse('')
    vote_aq = Vote.objects.filter(choice=Vote.TEAM_AQUA).count()
    vote_mg = Vote.objects.count() - vote_aq
    return render(
        request,
        "pmo2015/home.html",
        {
            'vote_aq': vote_aq,
            'vote_mg': vote_mg,
            'weibo_url': settings.WEIBO_URL
        }
    )


def test(request):
    return render(request, "pmo2015/base.html")
