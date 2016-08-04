#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

Nominate_choise = (
    ('BlackAndWhite','Черное и белое и серое'),
    ('ProfiVsHobby','Цветопробы'),
    ('Scatching','Скетчинг'),
    ('CopyPast','Copy Paste'),
    ('MiniArt','Мини-художники'),
)

class Gallery(models.Model):
    art_host_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    art_city = models.CharField(max_length=200)
    art_mail = models.CharField(max_length=200)
    art_link = models.CharField(max_length=200)
    art_category = models.CharField(max_length=200, choices=Nominate_choise)
    art_delete = models.BooleanField(default=False)
    art_vote = models.IntegerField(default=0)
    docfile = models.FileField(upload_to='arts')
    art_password = models.CharField(max_length=200)
    art_vote = models.IntegerField(default=0)

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.art_host_name) or u''


class Vote(models.Model):
    art = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    vote_id = models.ForeignKey(User, related_name='votes')
    vote_is_it = models.BooleanField(default=False)

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.art) or u''

class Shop(models.Model):
    city = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    web = models.CharField(max_length=200)

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''