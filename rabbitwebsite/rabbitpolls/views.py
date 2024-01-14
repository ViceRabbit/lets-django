from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import bunnyquestion # databasseee

def index(request):
    latestquestions = bunnyquestion.objects.order_by("-dateofquest")[:5]
    context = { # in the html template, we reference stupid variables so
        "latestquestions": latestquestions,
    }
    return render(request, "rabbitpolls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(bunnyquestion, pk=question_id)
    return render(request, "rabbitpolls/details.html", {"thequestion": question})

def results(request, question_id):
    return HttpResponse(f"ok so you're looking at the RESULTS of question {question_id}")

def votes(request, question_id):
    return HttpResponse(f"ok now you're looking at the VOTES of question {question_id}")