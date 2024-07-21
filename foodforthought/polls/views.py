from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Recipe, Choice
from django.urls import reverse

# Create your views here.
def index(request):
    '''View for index page. Renders latest recipe list from poll.html.'''
    latest_poll_list = Recipe.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, "polls/poll.html", context)


def home(request):
    '''View for home.html page'''
    return render(request, "polls/home.html")


def detail(request, question_id):
    '''View for detail of recipe.'''
    recipe = get_object_or_404(Recipe, pk=question_id)
    return render(request, "polls/detail.html", {"recipe": recipe})


def results(request, question_id):
    '''View for results of recipe.'''
    recipe = get_object_or_404(Recipe, pk=question_id)
    return render(request, "polls/results.html", {"recipe": recipe})


def vote(request, question_id):
    '''View for voting of recipe.'''
    recipe = get_object_or_404(Recipe, pk=question_id)
    try:
        selected_choice = recipe.choice_set.get(
            pk=request.POST["choice"]
        )
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, "polls/detail.html", {
            "recipe": recipe,
            "error_message": "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a 
    # user hits the Back button.
        return HttpResponseRedirect(
            reverse("polls:results", args=(question_id,))
        )
