#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Gallery, Vote, Shop

admin.site.register(Gallery)
admin.site.register(Vote)
admin.site.register(Shop)


# Register your models here.
