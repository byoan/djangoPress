from django import forms
from django.forms import widgets
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):

    username = forms.CharField(
        max_length=100,
        label=_("Username"),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label=_("Password"),
        widget=widgets.PasswordInput(attrs={'class': 'form-control'})
    )
