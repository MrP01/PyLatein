# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name="Nomen",
            fields=[
                ("id", models.AutoField(verbose_name="ID", primary_key=True, auto_created=True, serialize=False)),
                ("geschlecht", models.CharField(choices=[("m", "maskulin"), ("f", "feminin"), ("n", "neutrum")], max_length=1)),
            ],
        ),
    ]
