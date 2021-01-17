# DATABASE
from __future__ import unicode_literals # Reads all languages
from django.db import models

# Create your models here.

class Posts(models.Model):

    name = models.CharField(max_length=50)
    short_txt = models.TextField()
    body_txt = models.TextField()
    date = models.CharField(max_length=12)
    img = models.TextField()
    author = models.CharField(max_length=50)
    catname = models.CharField(max_length=50, default='-')
    catid = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        
        return self.name