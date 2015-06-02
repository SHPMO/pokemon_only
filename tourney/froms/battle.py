from captcha.fields import CaptchaField
from django import forms

class BattleRegisterBaseForm(forms.Form):
    player_id = forms.CharField(max_length=30)
    email = forms.EmailField()
    taobao_id = forms.CharField(max_length=20)
    captcha = CaptchaField()
