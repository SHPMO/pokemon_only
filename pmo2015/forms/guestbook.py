from django import forms
from captcha.fields import CaptchaField


class MessageForm(forms.Form):
    nickname = forms.EmailField(max_length=30)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(required=False)
    captcha = CaptchaField()
