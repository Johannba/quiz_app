# quiz/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("create-category/", views.create_category, name="create_category"),
    path("category-list/", views.category_list, name="category_list"),
    path("create-question/", views.create_question, name="create_question"),
    path("question-list/", views.question_list, name="question_list"),
    path("take-quiz/", views.take_quiz, name="take_quiz"),
    path("quiz-results/<int:score>/", views.quiz_results, name="quiz_results"),
]
