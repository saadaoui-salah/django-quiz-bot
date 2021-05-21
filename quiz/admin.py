from django.contrib import admin
from .models import Quiz, Answers

admin.site.register(Quiz)
admin.site.register(Answers)

class AnswersInlineModel(admin.TabularInline):
    model = Answers
    fields = [
        'answer',
        'is_correct',
    ]    

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