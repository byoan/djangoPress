from django import forms
from django.forms import widgets
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):

    username = forms.CharField(max_length=100)
    password1 = forms.CharField(
        widget=widgets.PasswordInput(),
        label=_('Enter a password')
    )
    password2 = forms.CharField(
        widget=widgets.PasswordInput(),
        label=_('Confirm your password')
    )
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(
        max_length=30,
        required=False,
        help_text=_('Optionnal')
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        help_text=_('Optionnal')
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2',)