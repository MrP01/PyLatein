# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vokabel', '0005_auto_20160202_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Declination',
            fields=[
                ('name', models.CharField(serialize=False, primary_key=True, max_length=5)),
                ('sg1', models.CharField(default='ending', max_length=12)),
                ('sg2', models.CharField(default='ending', max_length=12)),
                ('sg3', models.CharField(default='ending', max_length=12)),
                ('sg4', models.CharField(default='ending', max_length=12)),
                ('sg5', models.CharField(default='ending', max_length=12)),
                ('sg6', models.CharField(default='ending', max_length=12)),
                ('pl1', models.CharField(default='ending', max_length=12)),
                ('pl2', models.CharField(default='ending', max_length=12)),
                ('pl3', models.CharField(default='ending', max_length=12)),
                ('pl4', models.CharField(default='ending', max_length=12)),
                ('pl5', models.CharField(default='ending', max_length=12)),
                ('pl6', models.CharField(default='ending', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Noun',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('translation', models.CharField(max_length=100)),
                ('genus', models.CharField(max_length=1, choices=[('m', 'maskulin'), ('f', 'feminin'), ('n', 'neutrum')])),
                ('sg1', models.CharField(max_length=100)),
                ('sg2', models.CharField(max_length=100)),
                ('sg3', models.CharField(max_length=100)),
                ('sg4', models.CharField(max_length=100)),
                ('sg5', models.CharField(max_length=100)),
                ('sg6', models.CharField(max_length=100)),
                ('pl1', models.CharField(max_length=100)),
                ('pl2', models.CharField(max_length=100)),
                ('pl3', models.CharField(max_length=100)),
                ('pl4', models.CharField(max_length=100)),
                ('pl5', models.CharField(max_length=100)),
                ('pl6', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Deklination',
        ),
        migrations.DeleteModel(
            name='Nomen',
        ),
    ]
