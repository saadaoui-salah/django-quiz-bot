from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Answer, Quiz
from .serializers import RandomQuizSerializer, AnswerSerializer

class RandomQuiz(APIView):
    
    def get(self, request, formate=None, **kwargs):
        question = Quiz.objects.filter().order_by('?')
        serializer = RandomQuizSerializer(question, many=True)
        return Response(serializer.data)