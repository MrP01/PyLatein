# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vokabel', '0011_conjugation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='verb',
            old_name='pluqperfPl1',
            new_name='pluqperfectPl1',
        ),
        migrations.RenameField(
            model_name='verb',
            old_name='pluqperfPl2',
            new_name='pluqperfectPl2',
        ),
        migrations.RenameField(
            model_name='verb',
            old_name='pluqperfPl3',
            new_name='pluqperfectPl3',
        ),
        migrations.RenameField(
            model_name='verb',
            old_name='pluqperfSg1',
            new_name='pluqperfectSg1',
        ),
        migrations.RenameField(
            model_name='verb',
            old_name='pluqperfSg2',
            new_name='pluqperfectSg2',
        ),
        migrations.RenameField(
            model_name='verb',
            old_name='pluqperfSg3',
            new_name='pluqperfectSg3',
        ),
    ]
