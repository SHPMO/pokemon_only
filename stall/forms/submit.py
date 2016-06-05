from django import forms
from stall.forms.bases import BaseForm


class SubmitForm(BaseForm):
    booth = forms.IntegerField(required=False)
    remarks = forms.CharField(widget=forms.Textarea, required=False)
    agreement = forms.BooleanField()
    number_of_people = forms.IntegerField(required=False)
