from django import http
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.views.generic.list import ListView

from app.forms.CreateArticleForm import CreateArticleForm
from app.models import Article, Author


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


class ArticleCreation(CreateView):
    model = Article
    template_name = 'articleCreateForm.html'
    form_class = CreateArticleForm
    success_url = '/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = Author(self.request.user.id)
        if form.is_valid():
            obj.save()
            return super(ArticleCreation, self).form_valid(form)

        form.add_error('username',
                       'Username must have a "a"')
        return super(ArticleCreation, self).form_invalid(form)