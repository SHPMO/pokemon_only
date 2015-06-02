from django import forms
from django.conf import settings


class PmoField(forms.CharField):
    def validate(self, value):
        super().validate(value)
        if not settings.PMO_LIST.get(value, False):
            raise forms.ValidationError('Invalid pmo value: %s' % value)


class BaseForm(forms.Form):
    pmo = PmoField(max_length=10)
