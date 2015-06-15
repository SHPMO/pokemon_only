import random
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
from django.views.generic import View
from django.http import HttpResponse, Http404
import json
from pmo2015.models import MainComment, Player, Vote
from pmo2015.forms import MessageForm, BattleForm


def _return_me(error_code, **kwargs):
    kwargs["error"] = error_code
    return kwargs


def _guestbook(request, *args, **kwargs):
    form = MessageForm(request.POST)
    if not form.is_valid():
        if 'captcha' in form.errors:
            return _return_me(2)
        return _return_me(1)
    ip_address = request.META.get("REMOTE_ADDR")
    if ip_address is None:
        return _return_me(-1)
    try:
        MainComment.create(
            nickname=form.cleaned_data['nickname'],
            content=form.cleaned_data['message'],
            email=form.cleaned_data['email'],
            ip_address=ip_address
        )
    except:
        return _return_me(-1)
    return _return_me(0)


def _battle(request, *args, **kwargs):
    form = BattleForm(request.POST)
    if not form.is_valid():
        if 'captcha' in form.errors:
            return _return_me(4)
        return _return_me(1, errors=form.errors)

    player_name = form.cleaned_data['nickname']
    email = form.cleaned_data['email']
    taobao_id = form.cleaned_data['taobao']
    team = form.cleaned_data['team']
    team = random.choice(Vote.TEAM_CHOICES)[0] if team == 'random' else team
    ip_address = request.META.get("REMOTE_ADDR")
    if ip_address is None:
        return _return_me(-1)
    elif any(Player.objects.filter(email=email)):
        return _return_me(2)
    else:
        try:
            player = Player.create(
                player_name=player_name,
                email=email,
                taobao_id=taobao_id,
                signup_ip=ip_address,
                team=team
            )
        except AssertionError:
            return _return_me(3)
        except:
            return _return_me(-1)
    send_mail(
        '%s对战报名' % settings.EMAIL_SUBJECT_PREFIX, "",
        settings.EMAIL_HOST_USER, [email], fail_silently=False,
        html_message=loader.get_template('pmo2015/mails/battle_signup.html').render({
            'player': player,
            'base_url': settings.BASE_URL,
            'weibo_url': settings.WEIBO_URL,
            'contact_mail': settings.CONTACT_EMAIL
        }),
    )
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
