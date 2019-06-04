from captcha.fields import CaptchaField
from django import forms

from stall.forms.bases import BaseForm


class LoginForm(BaseForm):
    email = forms.EmailField(max_length=30)
    password = forms.CharField(max_length=128)
    captcha = CaptchaField()
