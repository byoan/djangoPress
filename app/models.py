from django.contrib.auth.models import User
from django.db import models


# class Author(models.Model):
#     username = models.CharField(max_length=200,
#                                 default=None,
#                                 blank=True,
#                                 help_text='username')
#
#     firstName = models.CharField(max_length=200,
#                                  default=None,
#                                  blank=True,
#                                  help_text='First Name')
#
#     lastName = models.CharField(max_length=200,
#                                 default=None,
#                                 blank=True,
#                                 help_text='Last Name')
#
#     def __str__(self):
#         return '{}'.format(self.username)


class Article(models.Model):
    title = models.CharField(max_length=200,
                             default=None,
                             blank=True,
                             help_text='Title')
    content = models.TextField(default=None,
                               blank=True,
                               help_text='Content')

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)
