# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vokabel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nomen',
            name='sg1',
            field=models.CharField(default='abwandlung', max_length=100),
        ),
        migrations.AddField(
            model_name='nomen',
            name='sg2',
            field=models.CharField(default='abwandlung', max_length=100),
        ),
        migrations.AddField(
            model_name='nomen',
            name='sg3',
            field=models.CharField(default='abwandlung', max_length=100),
        ),
        migrations.AddField(
            model_name='nomen',
            name='sg4',
            field=models.CharField(default='abwandlung', max_length=100),
        ),
        migrations.AddField(
            model_name='nomen',
            name='sg5',
            field=models.CharField(default='abwandlung', max_length=100),
        ),
        migrations.AddField(
            model_name='nomen',
            name='sg6',
            field=models.CharField(default='abwandlung', max_length=100),
        ),
    ]
