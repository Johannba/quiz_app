from django.shortcuts import render, redirect, get_object_or_404, redirect
from .forms import (
    QuestionCategoryForm,
    QuestionCategory,
    QuestionForm,
    ChoiceForm,
    UserResponseForm,
)
from .models import Question, Choice, UserResponse


def create_category(request):
    if request.method == "POST":
        form = QuestionCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "category_list"
            )  # Redirigez l'utilisateur vers la liste des catégories
    else:
        form = QuestionCategoryForm()
    return render(request, "quiz_test/create_category.html", {"form": form})


# quiz/views.py


def category_list(request):
    categories = QuestionCategory.objects.all()
    return render(request, "quiz_test/category_list.html", {"categories": categories})


def create_question(request):
    if request.method == "POST":
        question_form = QuestionForm(request.POST)
        choice_forms = [
            ChoiceForm(request.POST, prefix=str(i)) for i in range(4)
        ]  # Assuming 4 choices per question

        if question_form.is_valid() and all(form.is_valid() for form in choice_forms):
            question = question_form.save()
            for choice_form in choice_forms:
                choice = choice_form.save(commit=False)
                choice.question = question
                choice.save()
            return redirect("question_list")  # Redirect to the question list view

    else:
        question_form = QuestionForm()
        choice_forms = [
            ChoiceForm(prefix=str(i)) for i in range(4)
        ]  # Assuming 4 choices per question

    return render(
        request,
        "quiz_test/create_question.html",
        {"question_form": question_form, "choice_forms": choice_forms},
    )


def question_list(request):
    questions = Question.objects.filter(is_published=True)
    return render(request, "quiz_test/question_list.html", {"questions": questions})


def take_quiz(request):
    questions = Question.objects.filter(is_published=True)
    score = 0  # Initialisation du score

    if request.method == "POST":
        user = (
            request.user
        )  # Récupération de l'utilisateur actuel (si l'authentification utilisateur de Django est utilisée)
        user_responses = []

        for question in questions:
            answer_id = request.POST.get(f"question_{question.id}")
            if answer_id:
                choice = Choice.objects.get(id=answer_id)
                user_response = UserResponse(
                    user=user, question=question, selected_choice=choice
                )
                user_response.save()
                user_responses.append(user_response)

                if choice.is_correct:
                    score += 1  # Incrémentation du score pour chaque réponse correcte

        # Vous pouvez maintenant effectuer d'autres opérations avec les réponses, comme enregistrer l'ensemble des réponses dans la base de données, générer un rapport, etc.

        # Redirection vers la page de résultats (à personnaliser)
        return redirect(
            "quiz_results", score=score
        )  # Redirigez vers la page de résultats avec le score en tant que paramètre

    return render(request, "quiz_test/take_quiz.html", {"questions": questions})


def quiz_results(request, score):
    # Vous pouvez utiliser le score pour afficher les résultats du quiz
    return render(request, "quiz_test/quiz_results.html", {"score": score})
def quiz_results(request, score):
    # Vous pouvez utiliser le score pour afficher les résultats du quiz
    return render(request, "quiz_test/quiz_results.html", {"score": score})
