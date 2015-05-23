# coding=utf-8
from pmo2015.views.common import CommonView
from pmo2015.models import Player, Vote
import random


class RegisterView(CommonView):
    _sub_list = ["battle", "stall", "consign"]
    name = "register"

    def get(self, request, sub=None, *args, **kwargs):
        return super().get(request, sub, *args, **kwargs)

    def post(self, request, sub=None, *args, **kwargs):
        def return_me(error_code):
            kwargs["error"] = error_code
            return self.get(request, sub, *args, **kwargs)
        if sub == "battle":
            player_id = request.POST.get("nickname", None)
            email = request.POST.get("email", None)
            taobao_id = request.POST.get("taobao", None)
            team = request.POST.get("team", None)
            ip_address = request.META.get("REMOTE_ADDR", None)
            if not all((player_id, email, taobao_id, team)):
                return return_me(1)
            elif ip_address is None:
                return return_me(-1)
            elif any(Player.objects.filter(email=email)):
                return return_me(2)
            else:
                Player.objects.create(
                    player_id=player_id,
                    email=email,
                    taobao_id=taobao_id,
                    signup_ip=ip_address,
                    team=random.choice(Vote.TEAM_CHOICES)[0] if team == 'random' else team
                )
            return return_me(0)
