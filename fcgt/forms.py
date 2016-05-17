#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Gallery
from django import forms
from django.utils.translation import ugettext_lazy as _



class ArtForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('art_host_name', 'art_city', 'art_mail',
                  'art_category', 'docfile', 'art_password')
        labels = {
            'art_host_name': _('ФИО'),
            'art_city': _('Город'),
            'art_mail': _('E-mail'),
            'art_category': _('Номинация'),
            'docfile': _('Загрузить файл (jpg, png, tiff)'),
            'art_password': _('Пароль'),
        }