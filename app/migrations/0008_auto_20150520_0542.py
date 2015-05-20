# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150520_0416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requestrecognizer',
            old_name='bArrayImage',
            new_name='imagenByteArray',
        ),
    ]
