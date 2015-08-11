# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='resp_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
