#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Gallery2
from django import forms
from django.utils.translation import ugettext_lazy as _



class ArtForm(forms.ModelForm):
    class Meta:
        model = Gallery2
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
        widgets = {
            'art_passwod': forms.TextInput(attrs={'placeholder': 'Пароль не должен совпадать с паролем вашей почты!'})
        }
