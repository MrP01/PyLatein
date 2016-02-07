# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vokabel', '0009_auto_20160203_1954'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Conjugation',
            new_name='VerbEndings',
        ),
    ]
