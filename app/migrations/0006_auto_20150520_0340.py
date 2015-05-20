# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_requestrecognizer_binary_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestrecognizer',
            name='binary_image',
            field=jsonfield.fields.JSONField(default=None, null=True),
        ),
    ]
