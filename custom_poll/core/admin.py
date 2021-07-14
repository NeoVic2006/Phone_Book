from django.contrib import admin

# Register your models here.

from .models import Post, Answer
from . import models

#admin.site.register(Post)


# ------------------------------------


@admin.register(models.Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'date_created',
        'date_over',
        'description'
    ]

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'poll',
        'title',
        'technique'
    ]

@admin.register(models.Answer)
class AnswerInlineModel(admin.ModelAdmin):
    model = Answer
    list_display = [
        'answer_text',
        'question',
        'is_right'
    ]