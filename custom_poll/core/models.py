from django.db import models
from django.db.models.deletion import DO_NOTHING


class Polls(models.Model):
    class Meta:
        verbose_name = 'Poll'
        verbose_name_plural = 'Polls'
        ordering = ['id']

    name = models.CharField(max_length=255)
    title  = models.CharField(max_length=255, default="New Poll", verbose_name="Poll Title")
    date_created = models.DateTimeField(auto_now_add=True)
    date_over = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Question(models.Model):
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ['id']

    TYPE = (
        (0, 'Text'),
        (1, 'Single Choise'),
        (2, 'Multiple Choise')
    )

    poll = models.ForeignKey(Polls, related_name='question', on_delete=DO_NOTHING)
    title  = models.CharField(max_length=255, verbose_name="Title")
    technique = models.IntegerField(choices=TYPE, default=0, verbose_name="Type of question")

    def __str__(self):
        return self.title


class Answer(models.Model):
    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        ordering = ['id']

    question = models.ForeignKey(Question, related_name='answer', on_delete=DO_NOTHING)
    answer_text = models.CharField(max_length=255, verbose_name="Answer text")
    is_right = models.BooleanField(default=False)
 
    def __str__(self):
        return self.answer_text