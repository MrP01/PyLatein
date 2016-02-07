# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vokabel', '0012_auto_20160206_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='verb',
            name='future2Pl1',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='verb',
            name='future2Pl2',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='verb',
            name='future2Pl3',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='verb',
            name='future2Sg1',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='verb',
            name='future2Sg2',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='verb',
            name='future2Sg3',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
