from rest_framework import serializers
from .models import Quiz, Answer

class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Answer
        fields = [
            'id',
            'answer',
            'is_correct',
        ]

class RandomQuizSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
    
        model = Quiz
        fields = [
            'title','answer'
        ]