# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('user_id', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=10)),
                ('password', models.IntegerField(max_length=15)),
                ('age', models.IntegerField(max_length=3)),
            ],
        ),
    ]
