from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    """
    Displays the latest 5 published questions.

    Requires user authentication to access.
    Retrieves the 5 most recent Question objects ordered by publication date
    and renders them using the 'polls/poll.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered page displaying the latest questions.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/poll.html", context)


def details(request, question_id):
    """
    Displays details for a specific question.

    Retrieves the Question object by its primary key (question_id).
    If not found, raises a 404 error.
    Renders 'polls/detail.html' with the question in context.

    Args:
        request (HttpRequest): The HTTP request object.
        question_id (int): ID of the question to display.

    Returns:
        HttpResponse: Rendered detail page for the question.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    """
    Displays the results for a specific question.

    Retrieves the Question object by its primary key (question_id).
    If not found, raises a 404 error.
    Renders 'polls/results.html' with the question in context.

    Args:
        request (HttpRequest): The HTTP request object.
        question_id (int): ID of the question whose results to display.

    Returns:
        HttpResponse: Rendered results page for the question.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    """
    Handles voting on a specific choice for a question.

    Retrieves the Question object by its primary key (question_id).
    Attempts to get the selected choice from POST data.
    If no choice is selected or choice does not exist, re-renders the detail
    page with an error message.
    Otherwise, increments the vote count for the selected choice, saves it,
    and redirects to the results page.

    Args:
        request (HttpRequest): The HTTP request object containing POST data.
        question_id (int): ID of the question being voted on.

    Returns:
        HttpResponseRedirect: Redirect to the results page upon successful voting.
        HttpResponse: Re-rendered detail page with error if no choice selected.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Re-render the question voting form with an error message
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
