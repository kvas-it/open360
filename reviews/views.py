from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from . import models


@login_required
def index(request):
    reviews = models.Review.objects.filter(owner=request.user)
    answer_sheets = models.AnswerSheet.objects.filter(owner=request.user)
    return render(request, 'reviews/index.html', {
        'my_reviews': reviews, 'my_answer_sheets': answer_sheets
    })


@login_required
def review(request, review_id):
    return HttpResponse('Review %s' % review_id)


@login_required
def answer_sheet(request, answer_sheet_id):
    return HttpResponse('Answer sheet %s' % answer_sheet_id)


@login_required
def save_answer(request, answer_sheet_id, question_id):
    return HttpResponse('Saving answer %s on answer sheet %s' %
            (question_id, answer_sheet_id))
