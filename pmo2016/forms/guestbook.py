from captcha.fields import CaptchaField
from django import forms


class MessageForm(forms.Form):
    nickname = forms.CharField(max_length=30)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(required=False)
    captcha = CaptchaField()
