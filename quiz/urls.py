from django.urls import path
from .views import RandomQuiz

urlpatterns = [
    path("api/random/", RandomQuiz.as_view())
]