from captcha.fields import CaptchaField
from django import forms


class BattleForm(forms.Form):
    nickname = forms.CharField(max_length=30)
    email = forms.EmailField()
    captcha = CaptchaField()
    taobao = forms.CharField(max_length=16, min_length=15)
    team = forms.CharField(max_length=6)
