from django import forms
from django.forms import widgets
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):

    username = forms.CharField(
        max_length=100,
        label=_('Enter a username'),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        widget=widgets.PasswordInput(attrs={'class': 'form-control'}),
        label=_('Enter a password')
    )
    password2 = forms.CharField(
        widget=widgets.PasswordInput(attrs={'class': 'form-control'}),
        label=_('Confirm your password')
    )
    email = forms.EmailField(
        max_length=100,
        widget=widgets.EmailInput(attrs={'class': 'form-control'}),
        label=_('Enter your email address')
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2')
