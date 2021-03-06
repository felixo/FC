# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-14 10:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_host_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('art_city', models.CharField(max_length=200)),
                ('art_mail', models.CharField(max_length=200)),
                ('art_link', models.CharField(max_length=200)),
                ('art_category', models.CharField(choices=[('monochrome_lab', '\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u0438\u044f Monochromos'), ('polychrome_planet', '\u041f\u043b\u0430\u043d\u0435\u0442\u0430 Polychromos'), ('pitt_artist', 'PITT Artist \u0441\u043a\u0435\u0442\u0447'), ('albrecht_durer', 'Albrecht durer: \u0440\u0430\u0431\u043e\u0442\u0430\u044e\u0442 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044b'), ('connector', 'Connector: \u0441\u0430\u043c \u0441\u0435\u0431\u0435 \u043a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u043e\u0440'), ('little_castle', '\u0417\u0430\u043c\u043e\u043a \u043c\u0430\u043b\u0435\u043d\u044c\u043a\u0438\u0445 \u0445\u0443\u0434\u043e\u0436\u043d\u0438\u043a\u043e\u0432')], max_length=200)),
                ('art_delete', models.BooleanField(default=False)),
                ('docfile', models.FileField(upload_to='arts')),
                ('art_password', models.CharField(max_length=200)),
                ('art_vote', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_host_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('art_city', models.CharField(max_length=200)),
                ('art_mail', models.CharField(max_length=200)),
                ('art_link', models.CharField(max_length=200)),
                ('art_category', models.CharField(choices=[('monochrome_lab', '\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u0438\u044f Monochromos'), ('polychrome_planet', '\u041f\u043b\u0430\u043d\u0435\u0442\u0430 Polychromos'), ('pitt_artist', 'PITT Artist \u0441\u043a\u0435\u0442\u0447'), ('albrecht_durer', 'Albrecht durer: \u0440\u0430\u0431\u043e\u0442\u0430\u044e\u0442 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044b'), ('connector', 'Connector: \u0441\u0430\u043c \u0441\u0435\u0431\u0435 \u043a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u043e\u0440'), ('little_castle', '\u0417\u0430\u043c\u043e\u043a \u043c\u0430\u043b\u0435\u043d\u044c\u043a\u0438\u0445 \u0445\u0443\u0434\u043e\u0436\u043d\u0438\u043a\u043e\u0432')], max_length=200)),
                ('art_delete', models.BooleanField(default=False)),
                ('docfile', models.FileField(upload_to='arts')),
                ('art_password', models.CharField(max_length=200)),
                ('art_vote', models.IntegerField(default=0)),
                ('small_image', models.FileField(default='', upload_to='arts')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('adress', models.CharField(max_length=200)),
                ('web', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_is_it', models.BooleanField(default=False)),
                ('art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fcgt.Gallery2')),
                ('vote_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
