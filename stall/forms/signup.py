from django import forms
from captcha.fields import CaptchaField
from stall.forms.bases import BaseForm


class SignupForm(BaseForm):
    email = forms.EmailField(max_length=30)
    password = forms.CharField(min_length=6, max_length=128)
    repassword = forms.CharField(max_length=128)
    type = forms.CharField(max_length=10)
    captcha = CaptchaField()
    circle_name = forms.CharField(max_length=40)
