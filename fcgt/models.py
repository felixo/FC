from __future__ import unicode_literals

from django.db import models


class Gallery(models.Model):
    art_host_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    art_city = models.CharField(max_length=200)
    art_mail = models.CharField(max_length=200)
    art_link = models.CharField(max_length=200)
    art_category = models.CharField(max_length=200)
    art_delete = models.BooleanField(default=False)
    art_vote = models.IntegerField(default=0)



class Vote(models.Model):
    art = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    vote_id = models.CharField(max_length=200)
    vote_is_it = models.BooleanField(default=False)