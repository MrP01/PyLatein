# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vokabel', '0010_auto_20160205_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conjugation',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('vocal', models.CharField(max_length=1)),
            ],
        ),
    ]
