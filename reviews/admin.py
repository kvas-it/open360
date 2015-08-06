from django.contrib import admin

from .models import (
        ReviewTemplate,
        ReviewerClass,
        QuestionGroup,
        Question,
        Review,
        AnswerSheet,
        Answer)


admin.site.register(ReviewTemplate)
admin.site.register(ReviewerClass)
admin.site.register(QuestionGroup)
admin.site.register(Question)
admin.site.register(Review)
admin.site.register(AnswerSheet)
admin.site.register(Answer)
