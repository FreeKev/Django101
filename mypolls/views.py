from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice

def index(request):
    # return HttpResponse("You're at index page")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'mypolls/index.html', { 'latest_question_list': latest_question_list })

def vote(request, question_id):
    # return HttpResponse("You're at vote page")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'mypolls/vote.html', {'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse("You're at results page")

def process_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse("Process (post) your vote")
