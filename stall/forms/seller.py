from django import forms
from stall.forms.bases import BaseForm


class SellerForm(BaseForm):
    circle_name = forms.CharField(max_length=40)
    circle_description = forms.CharField(required=False, widget=forms.Textarea)
    proposer_name = forms.CharField(max_length=20)
    proposer_sex = forms.CharField(max_length=20)
    proposer_qq = forms.CharField(required=False, max_length=11)
    proposer_phone = forms.CharField(max_length=20)
    proposer_id = forms.CharField(required=False, max_length=18)
