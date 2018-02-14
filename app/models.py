import os
from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    def get_path(self, filename):
        return os.path.join(str(self.id), filename)

    title = models.CharField(max_length=200,
                             default=None,
                             blank=True,
                             help_text='Title')
    content = models.TextField(default=None,
                               blank=True,
                               help_text='Content')

    image = models.ImageField(upload_to=get_path,
                              blank=True,
                              null=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)
