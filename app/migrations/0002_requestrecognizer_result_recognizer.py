# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestrecognizer',
            name='result_recognizer',
            field=jsonfield.fields.JSONField(default=None, null=True),
        ),
    ]
