# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vokabel', '0004_auto_20160201_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deklination',
            name='id',
        ),
        migrations.AddField(
            model_name='deklination',
            name='nomen',
            field=models.CharField(primary_key=True, max_length=5, default='1O', serialize=False),
            preserve_default=False,
        ),
    ]
