from django.db.models import fields
from rest_framework import serializers
from .models import Quiz, Answers

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = [
            'id', 
            'answer',
            'is_correct'
        ]

class RandomQuizSerializer(serializers.ModelSerializer):
    answers = AnswersSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = [
            'title',
            'answers'
        ]