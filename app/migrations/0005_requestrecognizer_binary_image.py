# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_requestrecognizer_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestrecognizer',
            name='binary_image',
            field=models.BinaryField(default=None, null=True),
        ),
    ]
