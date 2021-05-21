from django.contrib import admin
from .models import Quiz, Answers


class AnswersInlineModel(admin.TabularInline):
    model = Answers
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
        AnswersInlineModel
    ]

@admin.register(Answers)

class AnswersAdmin(admin.ModelAdmin):
    list_display = [
        'answer',
        'is_correct',
        'question'
    ]