from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework import permissions


# Third party imports 
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializes import PostSerializer
from .models import Post


class TestView(APIView):

    permission_classes = (IsAuthenticated, )


    def get(self, request, *ars, **kwargs):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request, *ars, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        else:
            return Response(serializer.errors)