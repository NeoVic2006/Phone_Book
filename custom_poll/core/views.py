from rest_framework import generics, status
from .models import Polls, Question
from .serializes import PollSerializer, QuestionSerializer

# Third party imports 
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class Poll(generics.ListAPIView):
    serializer_class = PollSerializer
    queryset = Polls.objects.all()


class Questions(APIView):
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(poll__title=kwargs['topic'])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)

    def post(self, request, format=None, **kwargs):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


