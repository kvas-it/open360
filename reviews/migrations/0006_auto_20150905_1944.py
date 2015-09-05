# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20150806_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='is_comleted',
            new_name='is_completed',
        ),
    ]
