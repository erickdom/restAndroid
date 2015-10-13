# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('send', models.CharField(default=b'', max_length=15, null=True, blank=True)),
                ('status', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('date_time',),
            },
        ),
    ]
