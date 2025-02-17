from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):  # Staff showing available polls
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):  # Staff explaining a poll
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):  # Staff showing results
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):  # Staff taking votes
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/vote.html', {'question': question})
