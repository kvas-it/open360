"""
Model definitions for 360 reviews.
"""

from django.db import models
from django.conf import settings


class ReviewTemplate(models.Model):
    name = models.CharField(max_length=200, unique=True)
    descr = models.CharField(max_length=4096)
    is_frozen = models.BooleanField()


class ReviewerClass(models.Model):
    review_template = models.ForeignKey(ReviewTemplate)
    name = models.CharField(max_length=200, unique=True)
    descr = models.CharField(max_length=4096)
    is_self = models.BooleanField()


class QuestionGroup(models.Model):
    review_template = models.ForeignKey(ReviewTemplate)
    name = models.CharField(max_length=200, unique=True)
    descr = models.CharField(max_length=4096)
    order = models.IntegerField(default=0)


class Question(models.Model):
    question_group = models.ForeignKey(QuestionGroup)
    type = 1
    text = models.CharField(max_length=4096)
    descr = models.CharField(max_length=4096)
    order = models.IntegerField(default=0)


class Review(models.Model):
    review_template = models.ForeignKey(ReviewTemplate)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    start_date = models.DateField()
    end_date = models.DateField()
    is_started = models.BooleanField()
    is_comleted = models.BooleanField()


class AnswerSheet(models.Model):
    review = models.ForeignKey(Review)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    reviewer_class = models.ForeignKey(ReviewerClass)
    is_started = models.BooleanField()
    is_comleted = models.BooleanField()


class Answer(models.Model):
    answer_sheet = models.ForeignKey(AnswerSheet)
    value = models.CharField(max_length=1024)
