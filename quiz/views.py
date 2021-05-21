from django.shortcuts import render
from .serializers import RandomQuizSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Quiz

class RandomQuiz(APIView):
    def get(self, request, formate=None, **kwagrs):
        question = Quiz.objects.filter().order_by('?')[:1]
        serializer = RandomQuizSerializer(question, many=True)
        return Response(serializer.data)

