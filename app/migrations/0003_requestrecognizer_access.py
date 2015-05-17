# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_requestrecognizer_result_recognizer'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestrecognizer',
            name='access',
            field=models.NullBooleanField(default=None),
        ),
    ]
