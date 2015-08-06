from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
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
    review = get_object_or_404(models.Review, pk=review_id)
    if review.owner != request.user:
        raise PermissionDenied('Review belongs to another user')
    answer_sheets = (models.AnswerSheet.objects
        .filter(review=review)
        .exclude(owner=request.user))
    return render(request, 'reviews/review.html', {
        'review': review, 'answer_sheets': answer_sheets
    })


def prepare_answer_data(answer_sheet):
    """Prepare answer data for displaying the answer sheet form."""
    answer_data = []
    answers = answer_sheet.get_answers()
    review_template = answer_sheet.review.review_template
    for group in review_template.get_question_groups(ordered=True):
        group_rec = {
            'question_group': group,
            'questions': []
        }
        answer_data.append(group_rec)
        for question in group.get_questions(ordered=True):
            question_rec = {
                'question': question,
                'answer_value': unicode(answers.get(question.id, ''))
            }
            group_rec['questions'].append(question_rec)
    return answer_data


@login_required
def answer_sheet(request, answer_sheet_id):
    answer_sheet = get_object_or_404(models.AnswerSheet, pk=answer_sheet_id)
    if answer_sheet.owner != request.user:
        raise PermissionDenied('Answers belong to another user')
    return render(request, 'reviews/answer_sheet.html', {
        'review': answer_sheet.review,
        'answer_sheet': answer_sheet, 
        'answer_data': prepare_answer_data(answer_sheet)
    })


@login_required
def save_answer(request, answer_sheet_id, question_id):
    return HttpResponse('Saving answer %s on answer sheet %s' %
            (question_id, answer_sheet_id))
