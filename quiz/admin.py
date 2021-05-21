from django.contrib import admin
from .models import Quiz, Answers

admin.site.register(Quiz)
admin.site.register(Answers)

class AnswersAdmin(admin.ModelAdmin):
    list_display = (
        'answers',
        'is_correct', 
        'questions'
    )