from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("yo wsg chat; this is the rabbit polls!!")

def detail(request, question_id):
    return HttpResponse(f"ok so ur looking at question {question_id}")

def results(request, question_id):
    return HttpResponse(f"ok so you're looking at the RESULTS of question {question_id}")

def votes(request, question_id):
    return HttpResponse(f"ok now you're looking at the VOTES of question {question_id}")