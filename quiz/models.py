from django.db import models

# Create your models here.


class Quiz(models.Model):

    LEVEL = (
        (0,'Any'),
        (1,'Beginner'),
        (2,'Intermediate'),
        (3,'Advanced'),
        (4,'Expert'),
    )

    title = models.CharField(max_length=300)
    points =  models.SmallIntegerField()
    difficulty = models.IntegerField(choices=LEVEL, default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,auto_now_add=False)

class Answers(models.Model):
    question = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    answer = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,auto_now_add=False)
