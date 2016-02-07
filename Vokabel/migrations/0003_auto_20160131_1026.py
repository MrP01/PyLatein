# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vokabel', '0002_auto_20160130_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deklination',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
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
        migrations.RenameField(
            model_name='nomen',
            old_name='geschlecht',
            new_name='genus',
        ),
        migrations.AddField(
            model_name='nomen',
            name='pl1',
            field=models.CharField(default='form', max_length=100),
        ),
        migrations.AddField(
            model_name='nomen',
            name='pl2',
            field=models.CharField(default='form', max_length=100),
        ),
        migrations.AddField(
            model_name='nomen',
            name='pl3',
            field=models.CharField(default='form', max_length=100),
        ),
        migrations.AddField(
            model_name='nomen',
            name='pl4',
            field=models.CharField(default='form', max_length=100),
        ),
        migrations.AddField(
            model_name='nomen',
            name='pl5',
            field=models.CharField(default='form', max_length=100),
        ),
        migrations.AddField(
            model_name='nomen',
            name='pl6',
            field=models.CharField(default='form', max_length=100),
        ),
        migrations.AlterField(
            model_name='nomen',
            name='sg1',
            field=models.CharField(default='form', max_length=100),
        ),
        migrations.AlterField(
            model_name='nomen',
            name='sg2',
            field=models.CharField(default='form', max_length=100),
        ),
        migrations.AlterField(
            model_name='nomen',
            name='sg3',
            field=models.CharField(default='form', max_length=100),
        ),
        migrations.AlterField(
            model_name='nomen',
            name='sg4',
            field=models.CharField(default='form', max_length=100),
        ),
        migrations.AlterField(
            model_name='nomen',
            name='sg5',
            field=models.CharField(default='form', max_length=100),
        ),
        migrations.AlterField(
            model_name='nomen',
            name='sg6',
            field=models.CharField(default='form', max_length=100),
        ),
    ]
