# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vokabel', '0006_auto_20160202_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='declination',
            name='description',
            field=models.CharField(default='description', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='declination',
            name='pl1',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='declination',
            name='pl2',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='declination',
            name='pl3',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='declination',
            name='pl4',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='declination',
            name='pl5',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='declination',
            name='pl6',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='declination',
            name='sg1',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='declination',
            name='sg2',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='declination',
            name='sg3',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='declination',
            name='sg4',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='declination',
            name='sg5',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='declination',
            name='sg6',
            field=models.CharField(max_length=12),
        ),
    ]
