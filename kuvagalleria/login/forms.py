from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Enter Username')
    password = forms.CharField(label='Enter Password',
                               widget=forms.PasswordInput)

class Meta:
    fields = ["username", "password"]