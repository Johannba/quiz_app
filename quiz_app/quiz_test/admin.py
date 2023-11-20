# quiz/admin.py
from django.contrib import admin
from .models import QuestionCategory, Question, Choice


@admin.register(QuestionCategory)
class QuestionCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class ChoiceInline(
    admin.TabularInline
):  # Utilisation de TabularInline pour une présentation plus compacte
    model = Choice
    extra = 4  # Nombre de champs Choice à afficher


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ("question_text", "category", "is_published")
