"""
Model definitions for 360 reviews.
"""

from django.db import models
from django.conf import settings


class ReviewTemplate(models.Model):
    name = models.CharField(max_length=200, unique=True)
    descr = models.CharField(max_length=4096)
    is_frozen = models.BooleanField()

    def get_question_groups(self, ordered=False):
        """Return question groups from this review template."""
        ret = QuestionGroup.objects.filter(review_template=self)
        if ordered:
            ret = ret.order_by('order')
        return ret

    def __unicode__(self):
        return self.name


class ReviewerClass(models.Model):
    review_template = models.ForeignKey(ReviewTemplate)
    name = models.CharField(max_length=200, unique=True)
    descr = models.CharField(max_length=4096)
    is_self = models.BooleanField()

    def __unicode__(self):
        return (self.name + u' in review template: ' +
                unicode(self.review_template))


class QuestionGroup(models.Model):
    review_template = models.ForeignKey(ReviewTemplate)
    name = models.CharField(max_length=200, unique=True)
    descr = models.CharField(max_length=4096)
    order = models.IntegerField(default=0)

    def get_questions(self, ordered=False):
        """Return questions from this question group."""
        ret = Question.objects.filter(question_group=self)
        if ordered:
            ret = ret.order_by('order')
        return ret

    def __unicode__(self):
        return (self.name + u' in review template: ' +
                unicode(self.review_template))


class Question(models.Model):
    question_group = models.ForeignKey(QuestionGroup)
    type = 1
    text = models.CharField(max_length=4096)
    descr = models.CharField(max_length=4096)
    order = models.IntegerField(default=0)

    def __unicode__(self):
        return (self.text + u' in question group: ' +
                unicode(self.question_group))


class Review(models.Model):
    review_template = models.ForeignKey(ReviewTemplate)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    is_started = models.BooleanField()
    is_comleted = models.BooleanField()

    def __unicode__(self):
        return u'Review of ' + unicode(self.owner)


class AnswerSheet(models.Model):
    review = models.ForeignKey(Review)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    reviewer_class = models.ForeignKey(ReviewerClass)
    is_started = models.BooleanField()
    is_completed = models.BooleanField()

    def get_answers(self):
        """Return answers that belong to the answer sheet.

        The return value is a dictionary: question_id -> answer.
        """
        answers = {}
        for answer in Answer.objects.filter(answer_sheet=self):
            answers[answer.question.id] = answer
        return answers
        
    def __unicode__(self):
        return (u'Answers of ' + unicode(self.owner) +
                u' for ' + unicode(self.review))


class Answer(models.Model):
    answer_sheet = models.ForeignKey(AnswerSheet)
    question = models.ForeignKey(Question)
    value = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.value
