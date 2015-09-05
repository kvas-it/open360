from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /reviews/
    url(r'^$', views.index, name='index'),
    # ex: /reviews/create-review
    url(r'^create-review/$', views.create_review, name='create-review'),
    # ex: /reviews/5/
    url(r'^(?P<review_id>[0-9]+)/$', views.review, name='review'),
    # ex: /reviews/answer-sheet/5/
    url(r'^answer-sheet/(?P<answer_sheet_id>[0-9]+)/$',
        views.answer_sheet, name='answer'),
    # ex: /reviews/answer-sheet/5/save/
    url(r'^answer-sheet/(?P<answer_sheet_id>[0-9]+)/save/$',
        views.save_answers, name='save-answers'),
]
