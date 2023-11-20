# quiz/forms.py
from django import forms
from .models import Question, Choice, QuestionCategory, UserResponse


class QuestionCategoryForm(forms.ModelForm):
    class Meta:
        model = QuestionCategory
        fields = ["name"]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["category", "question_text", "is_published"]


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["choice_text", "is_correct"]


class UserResponseForm(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = ["selected_choice"]


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["choice_text"]
