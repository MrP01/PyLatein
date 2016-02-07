# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vokabel', '0003_auto_20160131_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='nomen',
            name='translation',
            field=models.CharField(default='Übersetzung', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nomen',
            name='pl1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='nomen',
            name='pl2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='nomen',
            name='pl3',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='nomen',
            name='pl4',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='nomen',
            name='pl5',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='nomen',
            name='pl6',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='nomen',
            name='sg1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='nomen',
            name='sg2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='nomen',
            name='sg3',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='nomen',
            name='sg4',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='nomen',
            name='sg5',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='nomen',
            name='sg6',
            field=models.CharField(max_length=100),
        ),
    ]
