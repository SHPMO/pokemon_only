# -*- coding:utf-8 -*-
import random
from django.views.generic import View
from django.http import HttpResponse, Http404
import json
from pmo2015.models import MainComment, Player, Vote


def _return_me(error_code):
    return {"error": error_code}


def _guestbook(request, *args, **kwargs):
    nickname = request.POST.get("nickname", "")
    message = request.POST.get("message", "").strip()
    ip_address = request.META.get("REMOTE_ADDR", None)
    if nickname == "" or message == "":
        return _return_me(1)
    elif ip_address is None:
        return _return_me(-1)
    else:
        try:
            MainComment.create(
                nickname=nickname,
                content=message,
                email=request.POST.get("email", None),
                ip_address=ip_address
            )
        except:
            return _return_me(-1)
    return _return_me(0)


def _battle(request, *args, **kwargs):
    player_id = request.POST.get("nickname", None)
    email = request.POST.get("email", None)
    taobao_id = request.POST.get("taobao", None)
    team = request.POST.get("team", None)
    ip_address = request.META.get("REMOTE_ADDR", None)
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
        except Exception as e:

            return _return_me(-1)
    return _return_me(0)

_api_list = {
    'guestbook': _guestbook,
    'battle': _battle
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
