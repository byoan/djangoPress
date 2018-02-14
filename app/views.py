from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from app.forms.UpdateArticleForm import UpdateArticleForm
from app.forms.loginForm import LoginForm
from app.forms.registerForm import RegisterForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views import generic
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q

from app.forms.CreateArticleForm import CreateArticleForm
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


class ArticleCreation(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'articleCreateForm.html'
    form_class = CreateArticleForm
    success_url = '/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = User(self.request.user.id)
        obj.image = form.files.get("image")
        if obj.author is None:
            form.add_error(None,
                           'An error occurred while retrieving your account '
                           'information for the article creation')
            return super(ArticleCreation, self).form_invalid(form)

        if form.is_valid():
            obj.save()
            return super(ArticleCreation, self).form_valid(form)

        form.add_error(None,
                       _('The sent data is invalid. Please check your input'))
        return super(ArticleCreation, self).form_invalid(form)


class LoginView(generic.FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        if username is None or password is None:
            form.add_error(None,
                           _('All the fields must be filled'))
            return super(LoginView, self).form_invalid(form)

        user = authenticate(username=username,
                            password=password)

        if user is None:
            form.add_error(None,
                           _('Username or password incorrect'))
            return super(LoginView, self).form_invalid(form)

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

            if username is None or password is None:
                form.add_error(None,
                               _('All the fields must be filled'))
                return super(RegisterView, self).form_invalid(form)

            if len(password) < 8:
                form.add_error('password',
                               _('Your password must be 8 characters long min'))
                return super(LoginView, self).form_invalid(form)

            user = authenticate(username=username, password=password)
            login(self.request, user)
            return super(RegisterView, self).form_valid(form)


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = UpdateArticleForm
    template_name = 'articleUpdateForm.html'
    success_url = reverse_lazy('index')


class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'articleDeleteForm.html'
    success_url = reverse_lazy('index')


class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'

    def get_context_object_name(self, obj):
        return 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(author=context['profile'])
        return context


class SearchView(ListView):
    template_name = 'search.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['articles'] = Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query))
        return context
