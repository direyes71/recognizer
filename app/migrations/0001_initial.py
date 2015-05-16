# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestRecognizer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_register', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to=b'images')),
                ('status', models.PositiveSmallIntegerField(default=1, choices=[(1, b'Activo'), (2, b'Desactivado')])),
            ],
        ),
    ]
