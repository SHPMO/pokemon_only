from django import forms
from captcha.fields import CaptchaField
from pmo2015.models import Vote


class BattleForm(forms.Form):
    nickname = forms.CharField(max_length=30)
    email = forms.EmailField()
    captcha = CaptchaField()
    taobao = forms.CharField(max_length=50)
    team = forms.CharField(max_length=6)
