# coding=utf-8
from django.conf import settings
from django.shortcuts import render
from pmo2015.models import Vote


def home(request):
    vote_aq = len(Vote.objects.filter(choice=Vote.TEAM_AQUA))
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
