from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /reviews/
    url(r'^$', views.index, name='index'),
    # ex: /reviews/5/
    url(r'^(?P<review_id>[0-9]+)/$', views.review, name='review'),
    # ex: /reviews/answer-sheet/5/
    url(r'^answer-sheet/(?P<answer_sheet_id>[0-9]+)/$',
        views.answer_sheet, name='answer'),
    # ex: /reviews/answer-sheet/5/4/save/
    url(r'^(?P<answer_sheet_id>[0-9]+)/(?P<question_id>[0-9]+)/save/$',
        views.save_answer, name='save-answer'),
]
