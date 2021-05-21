from django.db.models import fields
from rest_framework import serializers
from .modesl import Quiz, Answers

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = [
            'id', 
            'answers',
            'is_correct'
        ]

class RandomQuizSerializer(serializers.ModelSerializer):
    answers = AnswersSerializer(any=True, read_only=True)
    class Meta:
        model = Quiz
        fields = [
            'title',
            'answer'
        ]