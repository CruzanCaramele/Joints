# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_location_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='bathrooms',
            new_name='bathroom',
        ),
    ]
