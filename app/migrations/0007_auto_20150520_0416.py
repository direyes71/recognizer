# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150520_0340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requestrecognizer',
            old_name='binary_image',
            new_name='bArrayImage',
        ),
    ]
