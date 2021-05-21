from django.urls import path
from .views import RandomQuiz

urlpatterns = [
    path("/", RandomQuiz.as_view())
]