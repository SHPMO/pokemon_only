# -*- coding:utf-8 -*-
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=30)
    password = forms.CharField(max_length=128)
    type = forms.CharField(max_length=10)
    captcha = CaptchaField()
