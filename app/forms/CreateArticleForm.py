from django import forms
from app.models import Article
from django.utils.translation import ugettext_lazy as _


class CreateArticleForm(forms.ModelForm):

    title = forms.CharField(
        max_length=100,
        required=True,
        label=_("Article title"),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        label=_("Content"),
        required=True
    )
    image = forms.ImageField(required=False)

    class Meta:
        model = Article
        fields = ('title', 'content', 'image')
