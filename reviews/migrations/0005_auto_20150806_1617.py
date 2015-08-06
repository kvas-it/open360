# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20150806_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
