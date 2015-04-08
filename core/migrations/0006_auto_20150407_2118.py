# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150407_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='beverage',
        ),
        migrations.AddField(
            model_name='location',
            name='alcohol',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='bathrooms',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='food',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='outdoor',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
    ]
