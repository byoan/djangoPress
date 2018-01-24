from django.contrib.auth import authenticate, login
from app.forms.loginForm import LoginForm
from app.forms.registerForm import RegisterForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.views.generic.list import ListView
from django.views import generic

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


class LoginView(generic.FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        if 'a' not in username:
            form.add_error('username',
                           'Username must have a "a"')
            return super(LoginView, self).form_invalid(form)

        if len(password) < 8:
            form.add_error('password',
                           'Min length of the password must be 8 characters')
            return super(LoginView, self).form_invalid(form)

        user = authenticate(username=username,
                            password=password)

        if user is None:
            form.add_error(None,
                           'Username or password incorrect')

        login(self.request, user)

        return super(LoginView, self).form_valid(form)

class RegisterView(generic.FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):

        if form.is_valid():
            # Save will use all the fields defined in the Meta class of the
            # RegisterForm form class
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(self.request, user)
            return super(RegisterView, self).form_valid(form)
