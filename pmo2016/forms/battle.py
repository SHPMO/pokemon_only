from django import forms
from captcha.fields import CaptchaField


class BattleForm(forms.Form):
    nickname = forms.CharField(max_length=30)
    email = forms.EmailField()
    captcha = CaptchaField()
    taobao = forms.CharField(max_length=5, min_length=5)
    phone = forms.CharField(max_length=20)
    receiver_name = forms.CharField(max_length=40)
