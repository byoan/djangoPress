from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from app.models import Article

class IndexView(ListView):
    template_name = 'home.html'

    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ArticleDetails(DetailView):
    template_name = 'article.html'

    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context