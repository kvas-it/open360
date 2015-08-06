# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerSheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_started', models.BooleanField()),
                ('is_comleted', models.BooleanField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=4096)),
                ('descr', models.CharField(max_length=4096)),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('descr', models.CharField(max_length=4096)),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_started', models.BooleanField()),
                ('is_comleted', models.BooleanField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewerClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('descr', models.CharField(max_length=4096)),
                ('is_self', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ReviewTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('descr', models.CharField(max_length=4096)),
                ('is_frozen', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='review_template',
            field=models.ForeignKey(to='reviews.ReviewTemplate'),
        ),
        migrations.AddField(
            model_name='questiongroup',
            name='review_template',
            field=models.ForeignKey(to='reviews.ReviewTemplate'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_group',
            field=models.ForeignKey(to='reviews.QuestionGroup'),
        ),
        migrations.AddField(
            model_name='answersheet',
            name='review',
            field=models.ForeignKey(to='reviews.Review'),
        ),
        migrations.AddField(
            model_name='answersheet',
            name='reviewer_class',
            field=models.ForeignKey(to='reviews.ReviewerClass'),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_sheet',
            field=models.ForeignKey(to='reviews.AnswerSheet'),
        ),
    ]
