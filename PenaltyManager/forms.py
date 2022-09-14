from django import forms
from django.db import models
from django.forms import fields
from PenaltyManager.models import Penalty


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class PenaltyForm(forms.ModelForm):

    class Meta:
        model = Penalty
        fields = ('__all__')
        widgets = {
            'date': forms.NumberInput(attrs={'type': 'date'}),
        }

