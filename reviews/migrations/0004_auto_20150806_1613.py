# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_answer_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answersheet',
            old_name='is_comleted',
            new_name='is_completed',
        ),
    ]
