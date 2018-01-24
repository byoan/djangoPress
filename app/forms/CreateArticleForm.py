from django import forms
from django.forms import widgets, ModelForm


from app.models import Article


class CreateArticleForm(forms.ModelForm):

    title = forms.CharField(
        max_length=100,
        required=True
    )
    content = forms.CharField(
        widget=forms.Textarea,
        required=True
    )

    class Meta:
        model = Article
        fields = ('title', 'content')