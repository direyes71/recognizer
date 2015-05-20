# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_requestrecognizer_access'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestrecognizer',
            name='code',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
