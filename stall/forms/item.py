# coding=utf-8
from django import forms
from stall.forms.bases import BaseForm


class ItemForm(BaseForm):
    name = forms.CharField(max_length=50)
    item_type = forms.CharField(max_length=20)
    content = forms.CharField(max_length=100)
    price = forms.FloatField()
    url = forms.URLField(required=False)
    authors = forms.CharField(widget=forms.Textarea, required=False)
    introduction = forms.CharField(widget=forms.Textarea, required=False)
    forto = forms.CharField(max_length=20)
    is_restricted = forms.CharField(max_length=20)
    circle = forms.CharField(max_length=40)
    item_id = forms.IntegerField()
