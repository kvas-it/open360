# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewerclass',
            name='review_template',
            field=models.ForeignKey(default=1, to='reviews.ReviewTemplate'),
            preserve_default=False,
        ),
    ]
