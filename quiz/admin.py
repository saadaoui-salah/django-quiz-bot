from django.contrib import admin
from .models import Quiz, Answer


class answerInlineModel(admin.TabularInline):
    model = Answer
    fields = [
        'answer',
        'is_correct',
    ]    

@admin.register(Quiz)

class QuizAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'points',
        'difficulty'
    ]
    list_display = [
        'title',
        'updated_at', 
    ]
    inlines = [
        answerInlineModel
    ]

@admin.register(Answer)

class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer',
        'is_correct',
        'question'
    ]