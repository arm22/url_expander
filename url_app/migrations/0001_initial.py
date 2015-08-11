# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('fin_url', models.URLField(blank=True, null=True)),
                ('org_url', models.URLField()),
                ('resp_code', models.IntegerField(max_length=3, blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
