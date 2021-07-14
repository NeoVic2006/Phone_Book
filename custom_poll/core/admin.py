from django.contrib import admin

# Register your models here.


from . import models


@admin.register(models.Polls)
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

    list_display = [
        'answer_text',
        'question',
        'is_right'
    ]