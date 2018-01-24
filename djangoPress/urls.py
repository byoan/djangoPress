"""djangoPress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from app.views import IndexView, ArticleDetails, ArticleCreation, RegisterView, \
    LoginView, ArticleUpdate, ArticleDelete, ProfileView
from django.contrib.auth import views as auth_views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'create$', ArticleCreation.as_view(), name="createArticle"),
    url(r'update/(?P<pk>\d+)', ArticleUpdate.as_view(), name="updateArticle"),
    url(r'delete/(?P<pk>\d+)', ArticleDelete.as_view(), name="deleteArticle"),
    url(r'profile/(?P<pk>\w+)', ProfileView.as_view(), name='profile'),
    url(r'(?P<pk>\d+)', ArticleDetails.as_view(), name="article"),
    url(r'login', LoginView.as_view(), name="login"),
    url(r'register', RegisterView.as_view(), name="register"),
    url(r'logout', auth_views.logout, {'next_page': '/'}, name='logout')
]

urlpatterns += i18n_patterns(
    url(_(r'^$'), IndexView.as_view(), name="index"),
)
