# quiz/models.py
from django.db import models
from django.urls import reverse

from quiz_app.users.models import User


class QuestionCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        return reverse("category_question_list", args=[str(self.pk)])


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class UserResponse(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Utilisez le modèle User de Django pour gérer les utilisateurs
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s response to {self.question.question_text}"
