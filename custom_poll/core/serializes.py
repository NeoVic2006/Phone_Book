from rest_framework import serializers
from .models import Answer, Polls, Question


class PollSerializer(serializers.ModelSerializer):
    class Meta:
       model = Polls
       fields = [
           'title', 
          
       ]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    class Meta:
       model = Question
       fields = [
           'title',
           'answer'
       ]

