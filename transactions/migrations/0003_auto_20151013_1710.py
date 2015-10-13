# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_transaction_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='folio_android',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='response',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(default=b'', max_length=4, null=True, blank=True),
        ),
    ]
