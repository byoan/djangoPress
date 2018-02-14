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
from django.views.static import serve
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from app.views import IndexView, ArticleDetails, ArticleCreation, RegisterView,\
    \
    LoginView, ArticleUpdate, ArticleDelete, ProfileView, SearchView
from django.contrib.auth import views as auth_views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _

from djangoPress import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT},
    ),
    url(r'login', LoginView.as_view(), name="login"),
    url(r'register', RegisterView.as_view(), name="register"),
    url(r'logout', auth_views.logout, {'next_page': '/'}, name='logout')
]

urlpatterns += i18n_patterns(
    url(_(r'profile/(?P<pk>\w+)'), ProfileView.as_view(), name='profile'),
    url(_(r'search$'), SearchView.as_view(), name='search'),
    url(_(r'create$'), ArticleCreation.as_view(), name="createArticle"),
    url(_(r'update/(?P<pk>\d+)'), ArticleUpdate.as_view(), name="updateArticle"),
    url(_(r'delete/(?P<pk>\d+)'), ArticleDelete.as_view(), name="deleteArticle"),
    url(_(r'^$'), IndexView.as_view(), name="index"),
    url(_(r'(?P<pk>\d+)'), ArticleDetails.as_view(), name="article"),
)
