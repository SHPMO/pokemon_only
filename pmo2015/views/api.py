# -*- coding:utf-8 -*-
import random
from django.views.generic import View
from django.http import HttpResponse, Http404
import json
from pmo2015.models import MainComment, Player, Vote


def _return_me(error_code, **kwargs):
    kwargs["error"] = error_code
    return kwargs


def _guestbook(request, *args, **kwargs):
    nickname = request.POST.get("nickname", "")
    message = request.POST.get("message", "").strip()
    ip_address = request.META.get("REMOTE_ADDR")
    if nickname == "" or message == "":
        return _return_me(1)
    elif ip_address is None:
        return _return_me(-1)
    else:
        try:
            MainComment.create(
                nickname=nickname,
                content=message,
                email=request.POST.get("email"),
                ip_address=ip_address
            )
        except:
            return _return_me(-1)
    return _return_me(0)


def _battle(request, *args, **kwargs):
    player_id = request.POST.get("nickname")
    email = request.POST.get("email")
    taobao_id = request.POST.get("taobao")
    team = request.POST.get("team")
    ip_address = request.META.get("REMOTE_ADDR")
    if not all((player_id, email, taobao_id, team)):
        return _return_me(1)
    elif ip_address is None:
        print(0)
        return _return_me(-1)
    elif any(Player.objects.filter(email=email)):
        return _return_me(2)
    else:
        try:
            Player.create(
                player_id=player_id,
                email=email,
                taobao_id=taobao_id,
                signup_ip=ip_address,
                team=random.choice(Vote.TEAM_CHOICES)[0] if team == 'random' else team
            )
        except AssertionError:
            return _return_me(3)
        except:
            return _return_me(-1)
    return _return_me(0)


def _vote(request, *args, **kwargs):
    choice = request.POST.get("team").upper()
    ip_address = request.META.get("REMOTE_ADDR")
    if not all((choice, ip_address)) or choice not in {Vote.TEAM_AQUA, Vote.TEAM_MAGMA}:
        return _return_me(-1)
    if len(Vote.objects.filter(ip_address=ip_address)) > 0 or request.session.get('vote'):
        return _return_me(1)
    vote = Vote.objects.create(
        choice=choice,
        ip_address=ip_address
    )
    request.session['vote'] = vote.id
    return _return_me(0, vote=0 if choice == Vote.TEAM_AQUA else 1)

_api_list = {
    'guestbook': _guestbook,
    'battle': _battle,
    'vote': _vote
}


class ApiView(View):

    @staticmethod
    def post(request, sub=None, *args, **kwargs):
        if sub not in _api_list:
            raise Http404
        func = _api_list[sub]
        return HttpResponse(json.dumps(func(
            request, *args, **kwargs
        )), content_type='application/json')

    @staticmethod
    def get(*args, **kwargs):
        raise Http404
