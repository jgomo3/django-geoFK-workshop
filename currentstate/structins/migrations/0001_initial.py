# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('observations', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('feature', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
        migrations.AddField(
            model_name='inspection',
            name='structure',
            field=models.ForeignKey(to='structins.Structure'),
        ),
    ]
